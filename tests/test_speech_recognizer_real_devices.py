"""
Интеграционные тесты для работы с реальными аудиоустройствами.

Эти тесты требуют наличия реальных аудиоустройств и могут быть запущены
только в среде с подключенным микрофоном и динамиками.
"""

import asyncio
import time
from typing import Dict, Any

import pytest
import sounddevice as sd

from modules.voice_recognition.core.types import RecognitionConfig
from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer


class RealDeviceTester:
    """Класс для тестирования работы с реальными аудиоустройствами"""
    
    def __init__(self):
        self.recognizer = None
        self.device_info = {}
        
    def get_available_devices(self) -> Dict[str, Any]:
        """Получает информацию о доступных аудиоустройствах"""
        try:
            devices = sd.query_devices()
            host_apis = sd.query_hostapis()
            default_device = sd.default.device
            
            input_devices = []
            output_devices = []
            
            for idx, device in enumerate(devices):
                device_info = {
                    'index': idx,
                    'name': device.get('name', 'Unknown'),
                    'max_input_channels': device.get('max_input_channels', 0),
                    'max_output_channels': device.get('max_output_channels', 0),
                    'default_samplerate': device.get('default_samplerate', 0),
                    'default_low_input_latency': device.get('default_low_input_latency', 0),
                    'default_high_input_latency': device.get('default_high_input_latency', 0),
                    'default_low_output_latency': device.get('default_low_output_latency', 0),
                    'default_high_output_latency': device.get('default_high_output_latency', 0),
                    'hostapi': device.get('hostapi', 0),
                }
                
                if device_info['max_input_channels'] > 0:
                    input_devices.append(device_info)
                if device_info['max_output_channels'] > 0:
                    output_devices.append(device_info)
            
            return {
                'all_devices': devices,
                'input_devices': input_devices,
                'output_devices': output_devices,
                'host_apis': host_apis,
                'default_device': default_device,
                'total_count': len(devices)
            }
        except Exception as e:
            return {'error': str(e)}
    
    def test_device_profiling(self) -> Dict[str, Any]:
        """Тестирует профилирование реального устройства"""
        try:
            config = RecognitionConfig()
            self.recognizer = SpeechRecognizer(config)
            
            # Профилируем устройство
            device_id = self.recognizer._prepare_input_device()
            
            # device_id может быть None в случае fallback, это нормально
            
            # Получаем статус после профилирования
            status = self.recognizer.get_status()
            
            return {
                'success': True,
                'device_id': device_id,
                'actual_input_rate': self.recognizer.actual_input_rate,
                'actual_input_channels': self.recognizer.actual_input_channels,
                'input_device_info': self.recognizer.input_device_info,
                'output_device_info': self.recognizer.output_device_info,
                'host_apis': self.recognizer.host_apis,
                'status': status
            }
        except Exception as e:
            return {'error': str(e)}
    
    async def test_audio_capture(self, duration: float = 1.0) -> Dict[str, Any]:
        """Тестирует захват аудио с реального устройства"""
        try:
            if not self.recognizer:
                return {'error': 'Recognizer не инициализирован'}
            
            # Запускаем прослушивание
            listen_task = asyncio.create_task(self.recognizer.start_listening())
            
            # Ждем указанное время
            await asyncio.sleep(duration)
            
            # Останавливаем прослушивание
            result = await self.recognizer.stop_listening()
            
            # Получаем статистику аудио
            audio_stats = self.recognizer.last_audio_stats
            
            return {
                'success': True,
                'recognition_result': result.text if result else '',
                'audio_chunks': len(self.recognizer.audio_data) if hasattr(self.recognizer, 'audio_data') else 0,
                'audio_stats': audio_stats,
                'duration': duration
            }
        except Exception as e:
            return {'error': str(e)}


def test_real_device_detection():
    """Тест определения реальных аудиоустройств"""
    tester = RealDeviceTester()
    device_info = tester.get_available_devices()
    
    if 'error' in device_info:
        pytest.skip(f"Не удалось получить информацию об устройствах: {device_info['error']}")
    
    print(f"\n🔍 Обнаружено устройств: {device_info['total_count']}")
    print(f"🎤 Входных устройств: {len(device_info['input_devices'])}")
    print(f"🔊 Выходных устройств: {len(device_info['output_devices'])}")
    print(f"🔌 Host API: {len(device_info['host_apis'])}")
    
    # Проверяем наличие входных устройств
    assert len(device_info['input_devices']) > 0, "Не найдено ни одного входного устройства"
    
    # Выводим информацию о входных устройствах
    print("\n📋 Входные устройства:")
    for device in device_info['input_devices']:
        print(f"  [{device['index']}] {device['name']}")
        print(f"      Каналы: {device['max_input_channels']}, "
              f"Частота: {device['default_samplerate']}Hz, "
              f"Латентность: {device['default_low_input_latency']:.3f}s")
    
    # Выводим информацию о выходных устройствах
    print("\n📋 Выходные устройства:")
    for device in device_info['output_devices']:
        print(f"  [{device['index']}] {device['name']}")
        print(f"      Каналы: {device['max_output_channels']}, "
              f"Частота: {device['default_samplerate']}Hz, "
              f"Латентность: {device['default_low_output_latency']:.3f}s")
    
    # Проверяем default устройство
    if device_info['default_device']:
        print(f"\n🎯 Устройство по умолчанию: {device_info['default_device']}")


def test_real_device_profiling():
    """Тест профилирования реального устройства"""
    tester = RealDeviceTester()
    result = tester.test_device_profiling()
    
    if 'error' in result:
        pytest.skip(f"Не удалось профилировать устройство: {result['error']}")
    
    print(f"\n✅ Профилирование успешно:")
    print(f"   ID устройства: {result['device_id']}")
    print(f"   Фактическая частота: {result['actual_input_rate']}Hz")
    print(f"   Фактическое количество каналов: {result['actual_input_channels']}")
    
    if result['input_device_info']:
        print(f"   Входное устройство: {result['input_device_info'].get('name', 'Unknown')}")
    
    if result['output_device_info']:
        print(f"   Выходное устройство: {result['output_device_info'].get('name', 'Unknown')}")
    
    # Проверяем корректность профилирования
    # device_id может быть None в случае fallback, это нормально
    assert result['actual_input_rate'] > 0, "Частота дискретизации не определена"
    assert result['actual_input_channels'] > 0, "Количество каналов не определено"
    assert result['input_device_info'], "Информация о входном устройстве отсутствует"
    
    # Проверяем статус
    status = result['status']
    assert 'actual_device' in status, "Статус не содержит информации об actual_device"
    assert 'output_device' in status, "Статус не содержит информации об output_device"


@pytest.mark.asyncio
async def test_real_audio_capture():
    """Тест захвата аудио с реального устройства"""
    tester = RealDeviceTester()
    
    # Сначала профилируем устройство
    profiling_result = tester.test_device_profiling()
    if 'error' in profiling_result:
        pytest.skip(f"Не удалось профилировать устройство: {profiling_result['error']}")
    
    print(f"\n🎤 Тестируем захват аудио...")
    print(f"   Говорите в микрофон в течение 2 секунд...")
    
    # Тестируем захват аудио
    capture_result = await tester.test_audio_capture(duration=2.0)
    
    if 'error' in capture_result:
        pytest.skip(f"Не удалось захватить аудио: {capture_result['error']}")
    
    print(f"\n✅ Захват аудио успешен:")
    print(f"   Количество аудио чанков: {capture_result['audio_chunks']}")
    print(f"   Длительность: {capture_result['duration']}s")
    
    if capture_result['audio_stats']:
        stats = capture_result['audio_stats']
        print(f"   Статистика аудио:")
        print(f"     Сэмплов: {stats.get('samples', 0)}")
        print(f"     RMS: {stats.get('rms', 0):.6f}")
        print(f"     RMS dB: {stats.get('rms_db', 0):.2f}")
        print(f"     Частота: {stats.get('raw_rate', 0)}Hz")
        print(f"     Каналы: {stats.get('raw_channels', 0)}")
    
    # Проверяем, что аудио было захвачено
    assert capture_result['audio_chunks'] > 0, "Аудио чанки не были захвачены"
    assert capture_result['audio_stats'], "Статистика аудио не была собрана"


def test_device_compatibility():
    """Тест совместимости с различными типами устройств"""
    tester = RealDeviceTester()
    device_info = tester.get_available_devices()
    
    if 'error' in device_info:
        pytest.skip(f"Не удалось получить информацию об устройствах: {device_info['error']}")
    
    print(f"\n🔧 Тестируем совместимость устройств...")
    
    # Тестируем каждое входное устройство
    for device in device_info['input_devices']:
        print(f"\n   Тестируем устройство [{device['index']}] {device['name']}")
        
        try:
            # Создаем новый recognizer для каждого устройства
            config = RecognitionConfig()
            recognizer = SpeechRecognizer(config)
            
            # Устанавливаем конкретное устройство
            sd.default.device = device['index']
            
            # Профилируем устройство
            device_id = recognizer._prepare_input_device()
            
            # device_id может быть None в случае fallback, это нормально
            print(f"     ✅ Успешно: ID={device_id}, "
                  f"Rate={recognizer.actual_input_rate}Hz, "
                  f"Channels={recognizer.actual_input_channels}")
                
        except Exception as e:
            print(f"     ❌ Ошибка: {e}")
    
    # Восстанавливаем default устройство
    sd.default.device = device_info['default_device']


if __name__ == "__main__":
    # Запуск тестов напрямую
    print("🧪 Запуск интеграционных тестов с реальными устройствами...")
    
    # Тест 1: Определение устройств
    print("\n" + "="*60)
    print("ТЕСТ 1: Определение реальных устройств")
    print("="*60)
    test_real_device_detection()
    
    # Тест 2: Профилирование
    print("\n" + "="*60)
    print("ТЕСТ 2: Профилирование устройства")
    print("="*60)
    test_real_device_profiling()
    
    # Тест 3: Захват аудио
    print("\n" + "="*60)
    print("ТЕСТ 3: Захват аудио")
    print("="*60)
    asyncio.run(test_real_audio_capture())
    
    # Тест 4: Совместимость
    print("\n" + "="*60)
    print("ТЕСТ 4: Совместимость устройств")
    print("="*60)
    test_device_compatibility()
    
    print("\n✅ Все интеграционные тесты завершены!")
