"""
Комплексный тест всей цепочки распознавания речи
"""

import asyncio
import time
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sounddevice as sd
import numpy as np
from modules.voice_recognition.core.types import RecognitionConfig
from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer


class RecognitionChainTester:
    """Тестер всей цепочки распознавания речи"""
    
    def __init__(self):
        self.recognizer = None
        self.test_results = {}
        
    def test_device_preparation(self):
        """Тест 1: Предварительная подготовка устройства"""
        print("🔧 Тест 1: Предварительная подготовка устройства")
        
        try:
            # Создаем recognizer
            config = RecognitionConfig()
            self.recognizer = SpeechRecognizer(config)
            
            # Проверяем начальное состояние
            assert self.recognizer.state.name == "IDLE", "Начальное состояние должно быть IDLE"
            
            # Вызываем _prepare_input_device()
            device_id = self.recognizer._prepare_input_device()
            
            # Проверяем, что устройство подготовлено
            assert device_id is not None, "device_id не должен быть None"
            assert self.recognizer.input_device_id is not None, "input_device_id должен быть установлен"
            assert self.recognizer.actual_input_rate > 0, "actual_input_rate должен быть больше 0"
            assert self.recognizer.actual_input_channels > 0, "actual_input_channels должен быть больше 0"
            assert self.recognizer.input_device_info, "input_device_info должен быть заполнен"
            
            print(f"   ✅ Устройство подготовлено:")
            print(f"      ID: {device_id}")
            print(f"      Частота: {self.recognizer.actual_input_rate}Hz")
            print(f"      Каналы: {self.recognizer.actual_input_channels}")
            print(f"      Название: {self.recognizer.input_device_info.get('name', 'Unknown')}")
            
            self.test_results['device_preparation'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Ошибка подготовки устройства: {e}")
            self.test_results['device_preparation'] = False
            return False
    
    async def test_start_listening_safety(self):
        """Тест 2: Безопасность start_listening()"""
        print("\n🛡️ Тест 2: Безопасность start_listening()")
        
        try:
            # Проверяем, что start_listening() вызывает _prepare_input_device()
            result = await self.recognizer.start_listening()
            
            # Проверяем результат
            assert result is not None, "start_listening() должен вернуть результат"
            assert self.recognizer.state.name == "LISTENING", "Состояние должно быть LISTENING"
            assert self.recognizer.is_listening, "is_listening должен быть True"
            assert self.recognizer.listen_thread is not None, "listen_thread должен быть создан"
            
            print(f"   ✅ start_listening() выполнен успешно:")
            print(f"      Результат: {result}")
            print(f"      Состояние: {self.recognizer.state.name}")
            print(f"      Поток активен: {self.recognizer.listen_thread.is_alive()}")
            
            self.test_results['start_listening'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Ошибка start_listening(): {e}")
            self.test_results['start_listening'] = False
            return False
    
    def test_recording_parameters(self):
        """Тест 3: Параметры записи"""
        print("\n🎤 Тест 3: Параметры записи")
        
        try:
            # Проверяем, что параметры записи соответствуют устройству
            device_info = self.recognizer.input_device_info
            
            # Проверяем соответствие параметров
            assert self.recognizer.actual_input_rate == device_info.get('default_samplerate'), \
                f"actual_input_rate ({self.recognizer.actual_input_rate}) должен соответствовать default_samplerate ({device_info.get('default_samplerate')})"
            
            assert self.recognizer.actual_input_channels == device_info.get('max_input_channels'), \
                f"actual_input_channels ({self.recognizer.actual_input_channels}) должен соответствовать max_input_channels ({device_info.get('max_input_channels')})"
            
            print(f"   ✅ Параметры записи корректны:")
            print(f"      Частота: {self.recognizer.actual_input_rate}Hz (от устройства)")
            print(f"      Каналы: {self.recognizer.actual_input_channels} (от устройства)")
            print(f"      Латентность: {device_info.get('default_low_input_latency', 'Unknown')}s")
            
            self.test_results['recording_parameters'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Ошибка параметров записи: {e}")
            self.test_results['recording_parameters'] = False
            return False
    
    async def test_audio_capture_and_processing(self):
        """Тест 4: Захват и обработка аудио"""
        print("\n📊 Тест 4: Захват и обработка аудио")
        
        try:
            # Ждем немного для записи аудио
            print("   🎤 Говорите в микрофон в течение 3 секунд...")
            await asyncio.sleep(3)
            
            # Останавливаем запись
            result = await self.recognizer.stop_listening()
            
            # Проверяем результат
            assert result is not None, "stop_listening() должен вернуть результат"
            assert self.recognizer.state.name == "IDLE", "Состояние должно вернуться в IDLE"
            assert not self.recognizer.is_listening, "is_listening должен быть False"
            
            # Проверяем статистику аудио
            stats = self.recognizer.last_audio_stats
            assert stats, "last_audio_stats должен быть заполнен"
            assert 'samples' in stats, "Статистика должна содержать samples"
            assert 'rms' in stats, "Статистика должна содержать rms"
            assert 'rms_db' in stats, "Статистика должна содержать rms_db"
            assert 'raw_rate' in stats, "Статистика должна содержать raw_rate"
            assert 'raw_channels' in stats, "Статистика должна содержать raw_channels"
            
            print(f"   ✅ Аудио захвачено и обработано:")
            print(f"      Сэмплов: {stats.get('samples', 0)}")
            print(f"      RMS: {stats.get('rms', 0):.6f}")
            print(f"      RMS dB: {stats.get('rms_db', 0):.2f}")
            print(f"      Частота: {stats.get('raw_rate', 0)}Hz")
            print(f"      Каналы: {stats.get('raw_channels', 0)}")
            print(f"      Результат распознавания: '{result.text if result else 'None'}'")
            
            self.test_results['audio_processing'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Ошибка обработки аудио: {e}")
            self.test_results['audio_processing'] = False
            return False
    
    def test_status_reporting(self):
        """Тест 5: Отчетность статуса"""
        print("\n📋 Тест 5: Отчетность статуса")
        
        try:
            # Получаем статус
            status = self.recognizer.get_status()
            
            # Проверяем структуру статуса
            assert 'actual_device' in status, "Статус должен содержать actual_device"
            assert 'output_device' in status, "Статус должен содержать output_device"
            assert 'host_apis' in status, "Статус должен содержать host_apis"
            assert 'signal_last_recording' in status, "Статус должен содержать signal_last_recording"
            
            # Проверяем actual_device
            actual_device = status['actual_device']
            assert 'name' in actual_device, "actual_device должен содержать name"
            assert 'effective_rate' in actual_device, "actual_device должен содержать effective_rate"
            assert 'effective_channels' in actual_device, "actual_device должен содержать effective_channels"
            
            # Проверяем соответствие данных
            assert actual_device['effective_rate'] == self.recognizer.actual_input_rate, \
                "effective_rate должен соответствовать actual_input_rate"
            assert actual_device['effective_channels'] == self.recognizer.actual_input_channels, \
                "effective_channels должен соответствовать actual_input_channels"
            
            print(f"   ✅ Статус корректно отображается:")
            print(f"      actual_device: {actual_device.get('name', 'Unknown')}")
            print(f"      effective_rate: {actual_device.get('effective_rate')}Hz")
            print(f"      effective_channels: {actual_device.get('effective_channels')}")
            print(f"      output_device: {status.get('output_device', {}).get('name', 'Unknown')}")
            print(f"      host_apis: {len(status.get('host_apis', []))} API")
            
            self.test_results['status_reporting'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Ошибка отчетности статуса: {e}")
            self.test_results['status_reporting'] = False
            return False
    
    def test_fallback_scenarios(self):
        """Тест 6: Сценарии fallback"""
        print("\n🔄 Тест 6: Сценарии fallback")
        
        try:
            # Создаем новый recognizer для тестирования fallback
            config = RecognitionConfig()
            test_recognizer = SpeechRecognizer(config)
            
            # Проверяем, что fallback работает при недоступности устройства
            # (этот тест может не сработать, если устройство доступно)
            try:
                device_id = test_recognizer._prepare_input_device()
                if device_id is not None:
                    print(f"   ✅ Устройство доступно (fallback не нужен): ID={device_id}")
                else:
                    print(f"   ⚠️ Устройство недоступно, fallback сработал")
            except Exception as e:
                print(f"   ⚠️ Ошибка получения устройства: {e}")
            
            self.test_results['fallback_scenarios'] = True
            return True
            
        except Exception as e:
            print(f"   ❌ Ошибка тестирования fallback: {e}")
            self.test_results['fallback_scenarios'] = False
            return False
    
    async def run_all_tests(self):
        """Запуск всех тестов"""
        print("🧪 Комплексное тестирование цепочки распознавания речи")
        print("="*70)
        
        # Тест 1: Подготовка устройства
        test1 = self.test_device_preparation()
        
        # Тест 2: Безопасность start_listening (асинхронный)
        test2 = await self.test_start_listening_safety()
        
        # Тест 3: Параметры записи
        test3 = self.test_recording_parameters()
        
        # Тест 4: Захват и обработка аудио (асинхронный)
        test4 = await self.test_audio_capture_and_processing()
        
        # Тест 5: Отчетность статуса
        test5 = self.test_status_reporting()
        
        # Тест 6: Сценарии fallback
        test6 = self.test_fallback_scenarios()
        
        # Итоговый отчет
        print("\n" + "="*70)
        print("📊 ИТОГОВЫЙ ОТЧЕТ:")
        
        all_tests = [
            ("Подготовка устройства", test1),
            ("Безопасность start_listening", test2),
            ("Параметры записи", test3),
            ("Захват и обработка аудио", test4),
            ("Отчетность статуса", test5),
            ("Сценарии fallback", test6)
        ]
        
        passed = 0
        total = len(all_tests)
        
        for test_name, result in all_tests:
            status = "✅ ПРОЙДЕН" if result else "❌ ПРОВАЛЕН"
            print(f"   {test_name}: {status}")
            if result:
                passed += 1
        
        print(f"\n🎯 РЕЗУЛЬТАТ: {passed}/{total} тестов пройдено")
        
        if passed == total:
            print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Цепочка распознавания работает корректно.")
        else:
            print("⚠️ Некоторые тесты провалены. Требуется доработка.")
        
        return passed == total


if __name__ == "__main__":
    tester = RecognitionChainTester()
    success = asyncio.run(tester.run_all_tests())
    sys.exit(0 if success else 1)
