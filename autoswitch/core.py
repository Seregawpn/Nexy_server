"""
Основная логика для работы с аудио устройствами
"""

import subprocess
import sounddevice as sd
import numpy as np
import time
import logging
from typing import List, Dict, Any, Optional, Tuple
from .config import get_config, get_device_patterns, compile_patterns

logger = logging.getLogger(__name__)

class AudioCore:
    """Основной класс для работы с аудио устройствами"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or get_config()
        self.patterns = get_device_patterns()
        self.compiled_patterns = {
            name: compile_patterns(patterns) 
            for name, patterns in self.patterns.items()
        }
        
    def _run_command(self, cmd: List[str]) -> Tuple[bool, str]:
        """Выполняет команду и возвращает результат"""
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            return result.returncode == 0, result.stdout.strip()
        except subprocess.TimeoutExpired:
            logger.error(f"⏰ Таймаут команды: {' '.join(cmd)}")
            return False, "Timeout"
        except Exception as e:
            logger.error(f"❌ Ошибка выполнения команды {' '.join(cmd)}: {e}")
            return False, str(e)
    
    def list_inputs(self) -> List[str]:
        """Получает список input устройств"""
        success, output = self._run_command(['SwitchAudioSource', '-a', '-t', 'input'])
        if success and output:
            return [line.strip() for line in output.split('\n') if line.strip()]
        return []
    
    def list_outputs(self) -> List[str]:
        """Получает список output устройств"""
        success, output = self._run_command(['SwitchAudioSource', '-a', '-t', 'output'])
        if success and output:
            return [line.strip() for line in output.split('\n') if line.strip()]
        return []
    
    def get_current_input(self) -> Optional[str]:
        """Получает текущее input устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-c', '-t', 'input'])
        if success and output:
            return output.strip()
        return None
    
    def get_current_output(self) -> Optional[str]:
        """Получает текущее output устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-c', '-t', 'output'])
        if success and output:
            return output.strip()
        return None
    
    def set_input(self, device_name: str) -> bool:
        """Устанавливает input устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-t', 'input', '-s', device_name])
        if success:
            logger.info(f"✅ Input установлен: {device_name}")
        else:
            logger.error(f"❌ Не удалось установить input: {device_name} - {output}")
        return success
    
    def set_output(self, device_name: str) -> bool:
        """Устанавливает output устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-t', 'output', '-s', device_name])
        if success:
            logger.info(f"✅ Output установлен: {device_name}")
        else:
            logger.error(f"❌ Не удалось установить output: {device_name} - {output}")
        return success
    
    def set_inout(self, device_name: str) -> bool:
        """Устанавливает input и output на одно устройство (сцепка)"""
        logger.info(f"🔗 Сцепка IN+OUT на: {device_name}")
        
        # Проверяем, есть ли устройство в списках
        inputs = self.list_inputs()
        outputs = self.list_outputs()
        
        # Ищем точное совпадение или частичное
        input_device = None
        output_device = None
        
        # Сначала ищем точное совпадение
        for inp in inputs:
            if inp == device_name:
                input_device = inp
                break
        
        for out in outputs:
            if out == device_name:
                output_device = out
                break
        
        # Если точного совпадения нет, ищем частичное
        if not input_device:
            for inp in inputs:
                if device_name.lower() in inp.lower() or inp.lower() in device_name.lower():
                    input_device = inp
                    break
        
        if not output_device:
            for out in outputs:
                if device_name.lower() in out.lower() or out.lower() in device_name.lower():
                    output_device = out
                    break
        
        if not input_device:
            logger.error(f"❌ Устройство {device_name} не найдено в input списке")
            return False
        
        if not output_device:
            logger.error(f"❌ Устройство {device_name} не найдено в output списке")
            return False
        
        # Устанавливаем input
        input_success = self.set_input(input_device)
        if not input_success:
            return False
        
        # Небольшая задержка для стабилизации
        time.sleep(0.1)
        
        # Устанавливаем output
        output_success = self.set_output(output_device)
        if not output_success:
            return False
        
        logger.info(f"✅ Сцепка IN+OUT успешна: {input_device} -> {output_device}")
        return True
    
    def find_by_patterns(self, candidates: List[str], pattern_names: List[str]) -> Optional[str]:
        """Находит устройство по паттернам"""
        # Сначала проверяем, не игнорируется ли устройство
        ignored_patterns = self.compiled_patterns.get('ignored', [])
        
        for candidate in candidates:
            # Проверяем, не игнорируется ли устройство
            is_ignored = False
            for ignored_pattern in ignored_patterns:
                if ignored_pattern.search(candidate):
                    logger.debug(f"🚫 Игнорируем устройство: {candidate}")
                    is_ignored = True
                    break
            
            if is_ignored:
                continue
            
            # Ищем по нужным паттернам
            for pattern_name in pattern_names:
                if pattern_name in self.compiled_patterns:
                    for pattern in self.compiled_patterns[pattern_name]:
                        if pattern.search(candidate):
                            logger.debug(f"🎯 Найдено по паттерну {pattern_name}: {candidate}")
                            return candidate
        return None
    
    def query_input_idx(self, device_name: str) -> Optional[int]:
        """Находит индекс устройства в PortAudio"""
        try:
            devices = sd.query_devices()
            for i, device in enumerate(devices):
                if device['max_input_channels'] > 0 and device_name.lower() in device['name'].lower():
                    logger.debug(f"🔍 Найден PortAudio индекс для {device_name}: {i}")
                    return i
        except Exception as e:
            logger.error(f"❌ Ошибка поиска PortAudio индекса: {e}")
        return None
    
    def health_rms(self, device_idx: int, sample_rate: int = None) -> Tuple[float, float]:
        """Проверяет здоровье устройства через RMS"""
        if sample_rate is None:
            sample_rate = self.config['sample_rate']
        
        try:
            logger.debug(f"🔍 Health check для устройства {device_idx} ({self.config['health_duration']}s)")
            
            # Настройки для тестирования
            sd.default.device = (device_idx, None)
            sd.default.samplerate = sample_rate
            sd.default.channels = self.config['channels']
            sd.default.dtype = self.config['dtype']
            
            # Буфер для аудио данных
            audio_buffer = []
            
            def callback(indata, frames, time, status):
                if status:
                    logger.warning(f"⚠️  Audio status: {status}")
                audio_buffer.append(indata.copy())
            
            # Открываем поток на короткое время
            with sd.InputStream(callback=callback, 
                              device=device_idx,
                              channels=self.config['channels'],
                              samplerate=sample_rate,
                              dtype=self.config['dtype'],
                              blocksize=int(sample_rate * 0.05)):  # 50ms блоки
                
                time.sleep(self.config['health_duration'])
            
            # Анализируем аудио
            if audio_buffer:
                audio_data = np.concatenate(audio_buffer).astype(np.float32)
                rms = float(np.sqrt(np.mean(audio_data**2)))
                peak = float(np.max(np.abs(audio_data)))
                
                logger.debug(f"📊 Health check результат: RMS={rms:.6f}, Peak={peak:.6f}")
                return rms, peak
            else:
                logger.warning("⚠️  Нет аудио данных в health check")
                return 0.0, 0.0
                
        except Exception as e:
            logger.error(f"❌ Ошибка health check: {e}")
            return 0.0, 0.0
    
    def is_device_working(self, device_name: str) -> bool:
        """Проверяет, работает ли устройство"""
        device_idx = self.query_input_idx(device_name)
        if device_idx is None:
            logger.warning(f"⚠️  Не найден PortAudio индекс для {device_name}")
            return False
        
        rms, peak = self.health_rms(device_idx)
        is_working = rms >= self.config['rms_threshold']
        
        logger.info(f"🔍 Устройство {device_name}: RMS={rms:.6f}, работает={is_working}")
        return is_working
    
    def get_device_snapshot(self) -> Dict[str, Any]:
        """Получает снимок текущего состояния устройств"""
        return {
            'inputs': self.list_inputs(),
            'outputs': self.list_outputs(),
            'current_input': self.get_current_input(),
            'current_output': self.get_current_output()
        }

"""

import subprocess
import sounddevice as sd
import numpy as np
import time
import logging
from typing import List, Dict, Any, Optional, Tuple
from .config import get_config, get_device_patterns, compile_patterns

logger = logging.getLogger(__name__)

class AudioCore:
    """Основной класс для работы с аудио устройствами"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or get_config()
        self.patterns = get_device_patterns()
        self.compiled_patterns = {
            name: compile_patterns(patterns) 
            for name, patterns in self.patterns.items()
        }
        
    def _run_command(self, cmd: List[str]) -> Tuple[bool, str]:
        """Выполняет команду и возвращает результат"""
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            return result.returncode == 0, result.stdout.strip()
        except subprocess.TimeoutExpired:
            logger.error(f"⏰ Таймаут команды: {' '.join(cmd)}")
            return False, "Timeout"
        except Exception as e:
            logger.error(f"❌ Ошибка выполнения команды {' '.join(cmd)}: {e}")
            return False, str(e)
    
    def list_inputs(self) -> List[str]:
        """Получает список input устройств"""
        success, output = self._run_command(['SwitchAudioSource', '-a', '-t', 'input'])
        if success and output:
            return [line.strip() for line in output.split('\n') if line.strip()]
        return []
    
    def list_outputs(self) -> List[str]:
        """Получает список output устройств"""
        success, output = self._run_command(['SwitchAudioSource', '-a', '-t', 'output'])
        if success and output:
            return [line.strip() for line in output.split('\n') if line.strip()]
        return []
    
    def get_current_input(self) -> Optional[str]:
        """Получает текущее input устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-c', '-t', 'input'])
        if success and output:
            return output.strip()
        return None
    
    def get_current_output(self) -> Optional[str]:
        """Получает текущее output устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-c', '-t', 'output'])
        if success and output:
            return output.strip()
        return None
    
    def set_input(self, device_name: str) -> bool:
        """Устанавливает input устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-t', 'input', '-s', device_name])
        if success:
            logger.info(f"✅ Input установлен: {device_name}")
        else:
            logger.error(f"❌ Не удалось установить input: {device_name} - {output}")
        return success
    
    def set_output(self, device_name: str) -> bool:
        """Устанавливает output устройство"""
        success, output = self._run_command(['SwitchAudioSource', '-t', 'output', '-s', device_name])
        if success:
            logger.info(f"✅ Output установлен: {device_name}")
        else:
            logger.error(f"❌ Не удалось установить output: {device_name} - {output}")
        return success
    
    def set_inout(self, device_name: str) -> bool:
        """Устанавливает input и output на одно устройство (сцепка)"""
        logger.info(f"🔗 Сцепка IN+OUT на: {device_name}")
        
        # Проверяем, есть ли устройство в списках
        inputs = self.list_inputs()
        outputs = self.list_outputs()
        
        # Ищем точное совпадение или частичное
        input_device = None
        output_device = None
        
        # Сначала ищем точное совпадение
        for inp in inputs:
            if inp == device_name:
                input_device = inp
                break
        
        for out in outputs:
            if out == device_name:
                output_device = out
                break
        
        # Если точного совпадения нет, ищем частичное
        if not input_device:
            for inp in inputs:
                if device_name.lower() in inp.lower() or inp.lower() in device_name.lower():
                    input_device = inp
                    break
        
        if not output_device:
            for out in outputs:
                if device_name.lower() in out.lower() or out.lower() in device_name.lower():
                    output_device = out
                    break
        
        if not input_device:
            logger.error(f"❌ Устройство {device_name} не найдено в input списке")
            return False
        
        if not output_device:
            logger.error(f"❌ Устройство {device_name} не найдено в output списке")
            return False
        
        # Устанавливаем input
        input_success = self.set_input(input_device)
        if not input_success:
            return False
        
        # Небольшая задержка для стабилизации
        time.sleep(0.1)
        
        # Устанавливаем output
        output_success = self.set_output(output_device)
        if not output_success:
            return False
        
        logger.info(f"✅ Сцепка IN+OUT успешна: {input_device} -> {output_device}")
        return True
    
    def find_by_patterns(self, candidates: List[str], pattern_names: List[str]) -> Optional[str]:
        """Находит устройство по паттернам"""
        # Сначала проверяем, не игнорируется ли устройство
        ignored_patterns = self.compiled_patterns.get('ignored', [])
        
        for candidate in candidates:
            # Проверяем, не игнорируется ли устройство
            is_ignored = False
            for ignored_pattern in ignored_patterns:
                if ignored_pattern.search(candidate):
                    logger.debug(f"🚫 Игнорируем устройство: {candidate}")
                    is_ignored = True
                    break
            
            if is_ignored:
                continue
            
            # Ищем по нужным паттернам
            for pattern_name in pattern_names:
                if pattern_name in self.compiled_patterns:
                    for pattern in self.compiled_patterns[pattern_name]:
                        if pattern.search(candidate):
                            logger.debug(f"🎯 Найдено по паттерну {pattern_name}: {candidate}")
                            return candidate
        return None
    
    def query_input_idx(self, device_name: str) -> Optional[int]:
        """Находит индекс устройства в PortAudio"""
        try:
            devices = sd.query_devices()
            for i, device in enumerate(devices):
                if device['max_input_channels'] > 0 and device_name.lower() in device['name'].lower():
                    logger.debug(f"🔍 Найден PortAudio индекс для {device_name}: {i}")
                    return i
        except Exception as e:
            logger.error(f"❌ Ошибка поиска PortAudio индекса: {e}")
        return None
    
    def health_rms(self, device_idx: int, sample_rate: int = None) -> Tuple[float, float]:
        """Проверяет здоровье устройства через RMS"""
        if sample_rate is None:
            sample_rate = self.config['sample_rate']
        
        try:
            logger.debug(f"🔍 Health check для устройства {device_idx} ({self.config['health_duration']}s)")
            
            # Настройки для тестирования
            sd.default.device = (device_idx, None)
            sd.default.samplerate = sample_rate
            sd.default.channels = self.config['channels']
            sd.default.dtype = self.config['dtype']
            
            # Буфер для аудио данных
            audio_buffer = []
            
            def callback(indata, frames, time, status):
                if status:
                    logger.warning(f"⚠️  Audio status: {status}")
                audio_buffer.append(indata.copy())
            
            # Открываем поток на короткое время
            with sd.InputStream(callback=callback, 
                              device=device_idx,
                              channels=self.config['channels'],
                              samplerate=sample_rate,
                              dtype=self.config['dtype'],
                              blocksize=int(sample_rate * 0.05)):  # 50ms блоки
                
                time.sleep(self.config['health_duration'])
            
            # Анализируем аудио
            if audio_buffer:
                audio_data = np.concatenate(audio_buffer).astype(np.float32)
                rms = float(np.sqrt(np.mean(audio_data**2)))
                peak = float(np.max(np.abs(audio_data)))
                
                logger.debug(f"📊 Health check результат: RMS={rms:.6f}, Peak={peak:.6f}")
                return rms, peak
            else:
                logger.warning("⚠️  Нет аудио данных в health check")
                return 0.0, 0.0
                
        except Exception as e:
            logger.error(f"❌ Ошибка health check: {e}")
            return 0.0, 0.0
    
    def is_device_working(self, device_name: str) -> bool:
        """Проверяет, работает ли устройство"""
        device_idx = self.query_input_idx(device_name)
        if device_idx is None:
            logger.warning(f"⚠️  Не найден PortAudio индекс для {device_name}")
            return False
        
        rms, peak = self.health_rms(device_idx)
        is_working = rms >= self.config['rms_threshold']
        
        logger.info(f"🔍 Устройство {device_name}: RMS={rms:.6f}, работает={is_working}")
        return is_working
    
    def get_device_snapshot(self) -> Dict[str, Any]:
        """Получает снимок текущего состояния устройств"""
        return {
            'inputs': self.list_inputs(),
            'outputs': self.list_outputs(),
            'current_input': self.get_current_input(),
            'current_output': self.get_current_output()
        }
