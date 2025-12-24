#!/usr/bin/env python3
"""
Прототип 4: Активация Output (AVAudioEngine)

Цель: Проверить, что AVAudioEngine корректно воспроизводит аудио
"""

import sys
import logging
import numpy as np
import time
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    from AVFoundation import (
        AVAudioEngine,
        AVAudioPlayerNode,
        AVAudioFormat,
        AVAudioPCMBuffer,
        AVAudioSession
    )
    from Foundation import NSRunLoop
    PYOBJC_AVAILABLE = True
    logger.info("✅ PyObjC доступен")
except ImportError as e:
    PYOBJC_AVAILABLE = False
    logger.error(f"❌ PyObjC не доступен: {e}")
    sys.exit(1)


class OutputPlaybackPrototype:
    """Прототип для тестирования воспроизведения через AVAudioEngine"""
    
    def __init__(self):
        self.engine = None
        self.player_node = None
        self.session = None
    
    def setup_audio_session(self):
        """Настройка AVAudioSession"""
        try:
            self.session = AVAudioSession.sharedInstance()
            
            error = None
            success = self.session.setCategory_withOptions_error_(
                "AVAudioSessionCategoryPlayback",
                0,  # No options
                error
            )
            
            if not success:
                logger.error("❌ Ошибка настройки категории AVAudioSession")
                return False
            
            success = self.session.setActive_error_(True, error)
            if not success:
                logger.error("❌ Ошибка активации AVAudioSession")
                return False
            
            logger.info("✅ AVAudioSession настроен")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка настройки AVAudioSession: {e}")
            return False
    
    def initialize_engine(self):
        """Инициализация AVAudioEngine"""
        try:
            self.engine = AVAudioEngine.alloc().init()
            self.player_node = AVAudioPlayerNode.alloc().init()
            
            # Attach player node
            self.engine.attachNode_(self.player_node)
            
            # Connect to main mixer
            main_mixer = self.engine.mainMixerNode()
            self.engine.connect_to_format_(
                self.player_node,
                main_mixer,
                None  # Use engine's format
            )
            
            logger.info("✅ AVAudioEngine инициализирован")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации AVAudioEngine: {e}")
            return False
    
    def generate_test_audio(self, duration_sec: float = 1.0, sample_rate: int = 16000) -> np.ndarray:
        """Генерация тестового аудио (синусоида 440Hz)"""
        t = np.linspace(0, duration_sec, int(sample_rate * duration_sec))
        frequency = 440.0  # A4 note
        audio = np.sin(2 * np.pi * frequency * t).astype(np.float32)
        return audio
    
    def numpy_to_pcm_buffer(self, audio_data: np.ndarray, sample_rate: int = 16000) -> AVAudioPCMBuffer:
        """
        Конвертация numpy array в AVAudioPCMBuffer
        
        ВАЖНО: Это упрощенная версия. Полная реализация требует работы с ObjC memory management.
        """
        try:
            # Получаем формат engine
            engine_format = self.engine.outputNode().outputFormatForBus_(0)
            target_sample_rate = int(engine_format.sampleRate())
            target_channels = engine_format.channelCount()
            
            logger.info(f"  🔄 Конвертация: {sample_rate}Hz → {target_sample_rate}Hz, channels: 1 → {target_channels}")
            
            # TODO: Реализовать sample rate conversion
            # TODO: Реализовать channel conversion
            # TODO: Создать AVAudioPCMBuffer и скопировать данные
            
            # Временная заглушка
            logger.warning("  ⚠️ Конвертация numpy → AVAudioPCMBuffer не реализована полностью")
            logger.warning("  ⚠️ Требуется работа с ObjC memory management")
            
            return None
            
        except Exception as e:
            logger.error(f"  ❌ Ошибка конвертации: {e}")
            return None
    
    def play_audio_chunk(self, audio_data: np.ndarray, sample_rate: int = 16000) -> bool:
        """Воспроизведение аудио чанка"""
        try:
            if not self.engine or not self.player_node:
                logger.error("❌ AVAudioEngine не инициализирован")
                return False
            
            # Конвертируем numpy в PCM buffer
            pcm_buffer = self.numpy_to_pcm_buffer(audio_data, sample_rate)
            
            if not pcm_buffer:
                logger.error("❌ Не удалось создать PCM buffer")
                return False
            
            # Schedule buffer
            self.player_node.scheduleBuffer_completionHandler_(pcm_buffer, None)
            
            # Start playing if not already
            if not self.player_node.isPlaying():
                self.player_node.play()
            
            logger.info("✅ Аудио чанк запланирован для воспроизведения")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка воспроизведения: {e}")
            return False
    
    def test_basic_playback(self):
        """Тестирование базового воспроизведения"""
        logger.info("\n📋 Тест 1: Базовое воспроизведение")
        
        # Генерируем тестовое аудио
        audio = self.generate_test_audio(duration_sec=1.0, sample_rate=16000)
        logger.info(f"  🔊 Сгенерировано тестовое аудио: {len(audio)} samples, 1.0 сек")
        
        # Воспроизводим
        success = self.play_audio_chunk(audio, sample_rate=16000)
        
        if success:
            # Ждем завершения воспроизведения
            logger.info("  ⏳ Ожидание завершения воспроизведения...")
            time.sleep(2.0)  # Даем время на воспроизведение
        
        return success
    
    def test_format_conversion(self):
        """Тестирование конвертации форматов"""
        logger.info("\n📋 Тест 2: Конвертация форматов")
        
        # Генерируем аудио в разных форматах
        formats = [
            (16000, 1),  # 16kHz mono
            (44100, 1),  # 44.1kHz mono
            (48000, 1),  # 48kHz mono
        ]
        
        success_count = 0
        
        for sample_rate, channels in formats:
            logger.info(f"  🔄 Тестирование: {sample_rate}Hz, {channels} channel(s)")
            audio = self.generate_test_audio(duration_sec=0.5, sample_rate=sample_rate)
            
            if self.play_audio_chunk(audio, sample_rate=sample_rate):
                success_count += 1
                time.sleep(1.0)
        
        return success_count == len(formats)
    
    def run_tests(self):
        """Запуск всех тестов"""
        logger.info("=" * 80)
        logger.info("ПРОТОТИП 4: Активация Output (AVAudioEngine)")
        logger.info("=" * 80)
        
        # Настройка сессии
        if not self.setup_audio_session():
            logger.error("❌ Не удалось настроить AVAudioSession")
            return False
        
        # Инициализация engine
        if not self.initialize_engine():
            logger.error("❌ Не удалось инициализировать AVAudioEngine")
            return False
        
        # Запуск engine
        try:
            error = None
            if not self.engine.startAndReturnError_(error):
                logger.error("❌ Не удалось запустить AVAudioEngine")
                return False
            logger.info("✅ AVAudioEngine запущен")
        except Exception as e:
            logger.error(f"❌ Ошибка запуска AVAudioEngine: {e}")
            return False
        
        success_count = 0
        total_tests = 0
        
        # Тест 1: Базовое воспроизведение
        total_tests += 1
        if self.test_basic_playback():
            success_count += 1
        
        # Тест 2: Конвертация форматов
        total_tests += 1
        if self.test_format_conversion():
            success_count += 1
        
        # Остановка engine
        try:
            self.engine.stop()
            logger.info("✅ AVAudioEngine остановлен")
        except Exception as e:
            logger.warning(f"⚠️ Ошибка остановки engine: {e}")
        
        # Итоги
        logger.info("\n" + "=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего тестов: {total_tests}")
        logger.info(f"Успешных: {success_count}")
        
        success_rate = (success_count / total_tests * 100) if total_tests > 0 else 0
        logger.info(f"\n📊 Успешность: {success_rate:.1f}%")
        
        success = success_rate >= 80.0
        
        if success:
            logger.info("\n✅ ПРОТОТИП 4 ПРОЙДЕН: Воспроизведение работает")
        else:
            logger.error("\n❌ ПРОТОТИП 4 ПРОВАЛЕН: Есть проблемы с воспроизведением")
            logger.warning("  ⚠️ Примечание: Конвертация numpy → AVAudioPCMBuffer требует доработки")
        
        return success


def main():
    """Главная функция"""
    prototype = OutputPlaybackPrototype()
    success = prototype.run_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

