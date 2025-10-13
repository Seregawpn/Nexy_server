#!/usr/bin/env python3
"""
Отдельный модуль для тестирования распознавания речи
"""

import sys
import os
import asyncio
import time
import logging
import subprocess

# Добавляем пути
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


from modules.voice_recognition.core.speech_recognizer import SpeechRecognizer
from modules.voice_recognition.core.types import RecognitionConfig

class SpeechRecognitionTester:
    """Тестер распознавания речи"""
    
    def __init__(self):
        self.recognizer = None
        self.is_running = False
        
    def setup_recognizer(self):
        """Настройка распознавателя речи"""
        config = RecognitionConfig(
            language='ru-RU',
            sample_rate=16000,
            chunk_size=1024,
            channels=1,
            dtype='int16',
            energy_threshold=300,
            dynamic_energy_threshold=True,
            pause_threshold=0.8,
            phrase_threshold=0.3,
            non_speaking_duration=0.8
        )
        
        self.recognizer = SpeechRecognizer(config)
        print("✅ Распознаватель речи настроен")
        
    async def test_device_selection(self):
        """Тестирует выбор аудио устройства"""
        print("\n🔍 Тестирование выбора аудио устройства...")
        
        if not self.recognizer:
            self.setup_recognizer()
            
        device_index = self.recognizer._pick_input_device()
        print(f"📱 Выбранное устройство: {device_index}")
        
        # Показываем информацию об устройстве
        import sounddevice as sd
        if device_index is not None:
            device_info = sd.query_devices(device_index)
            print(f"📊 Информация об устройстве:")
            print(f"  Название: {device_info['name']}")
            print(f"  Каналы: {device_info['max_input_channels']}")
            print(f"  Частота: {device_info.get('default_samplerate', 'unknown')} Hz")
        
        return device_index
        
    async def test_audio_capture(self, duration=5):
        """Тестирует захват аудио"""
        print(f"\n🎤 Тестирование захвата аудио ({duration} секунд)...")
        print("💬 Говорите в микрофон...")
        
        if not self.recognizer:
            self.setup_recognizer()
            
        # Начинаем прослушивание
        success = await self.recognizer.start_listening()
        if not success:
            print("❌ Не удалось начать прослушивание")
            return False
            
        print("✅ Прослушивание начато")
        
        # Ждем указанное время
        await asyncio.sleep(duration)
        
        # Останавливаем прослушивание
        result = await self.recognizer.stop_listening()
        
        print(f"\n📊 Результаты захвата:")
        print(f"  Текст: '{result.text}'")
        print(f"  Ошибка: {result.error if result.error else 'Нет'}")
        print(f"  Длительность: {result.duration:.2f}s")
        print(f"  Язык: {result.language}")
        
        return result.text is not None and len(result.text) > 0
        
    async def test_continuous_recognition(self, max_attempts=3):
        """Тестирует непрерывное распознавание"""
        print(f"\n🔄 Тестирование непрерывного распознавания ({max_attempts} попыток)...")
        
        successful_recognitions = 0
        
        for attempt in range(1, max_attempts + 1):
            print(f"\n--- Попытка {attempt}/{max_attempts} ---")
            print("💬 Говорите что-нибудь (3 секунды)...")
            
            success = await self.test_audio_capture(duration=3)
            if success:
                successful_recognitions += 1
                print("✅ Распознавание успешно")
            else:
                print("❌ Распознавание не удалось")
                
            if attempt < max_attempts:
                print("⏳ Пауза 2 секунды...")
                await asyncio.sleep(2)
        
        print(f"\n📈 Итоги непрерывного тестирования:")
        print(f"  Успешных распознаваний: {successful_recognitions}/{max_attempts}")
        print(f"  Процент успеха: {successful_recognitions/max_attempts*100:.1f}%")
        
        return successful_recognitions > 0
        
    async def test_different_languages(self):
        """Тестирует распознавание на разных языках"""
        print("\n🌍 Тестирование разных языков...")
        
        languages = [
            ('ru-RU', 'Русский'),
            ('en-US', 'English'),
            ('uk-UA', 'Українська')
        ]
        
        results = {}
        
        for lang_code, lang_name in languages:
            print(f"\n--- Тестирование {lang_name} ({lang_code}) ---")
            
            # Создаем новый распознаватель для каждого языка
            config = RecognitionConfig(
                language=lang_code,
                sample_rate=16000,
                chunk_size=1024,
                channels=1,
                dtype='int16',
                energy_threshold=300,
                dynamic_energy_threshold=True,
                pause_threshold=0.8,
                phrase_threshold=0.3,
                non_speaking_duration=0.8
            )
            
            recognizer = SpeechRecognizer(config)
            
            print(f"💬 Говорите на {lang_name} (3 секунды)...")
            success = await recognizer.start_listening()
            
            if success:
                await asyncio.sleep(3)
                result = await recognizer.stop_listening()
                
                results[lang_name] = {
                    'success': result.text is not None and len(result.text) > 0,
                    'text': result.text,
                    'error': result.error
                }
                
                print(f"  Результат: '{result.text}'")
                print(f"  Успех: {'✅' if results[lang_name]['success'] else '❌'}")
            else:
                results[lang_name] = {'success': False, 'text': '', 'error': 'Failed to start'}
                print("  ❌ Не удалось начать прослушивание")
        
        return results
        
    def show_status(self):
        """Показывает статус распознавателя"""
        if not self.recognizer:
            print("❌ Распознаватель не инициализирован")
            return
            
        status = self.recognizer.get_status()
        print("\n📊 Статус распознавателя:")
        print(f"  Состояние: {status['state']}")
        print(f"  Прослушивание: {'Да' if status['is_listening'] else 'Нет'}")
        print(f"  Чанки аудио: {status['audio_data_chunks']}")
        print(f"  Язык: {status['config']['language']}")
        print(f"  Частота: {status['config']['sample_rate']} Hz")
        print(f"  Размер чанка: {status['config']['chunk_size']}")
        print(f"  Каналы: {status['config']['channels']}")
        
        metrics = status['metrics']
        print(f"\n📈 Метрики:")
        print(f"  Всего распознаваний: {metrics['total_recognitions']}")
        print(f"  Успешных: {metrics['successful_recognitions']}")
        print(f"  Неудачных: {metrics['failed_recognitions']}")
        print(f"  Процент успеха: {metrics['success_rate']:.1f}%")
        print(f"  Средняя уверенность: {metrics['average_confidence']:.2f}")
        
    async def interactive_mode(self):
        """Интерактивный режим тестирования"""
        print("\n🎮 Интерактивный режим")
        print("Доступные команды:")
        print("  1 - Тест выбора устройства")
        print("  2 - Тест захвата аудио (5 сек)")
        print("  3 - Тест захвата аудио (3 сек)")
        print("  4 - Непрерывное тестирование")
        print("  5 - Тест разных языков")
        print("  6 - Показать статус")
        print("  7 - Настроить распознаватель")
        print("  q - Выход")
        
        while True:
            try:
                command = input("\nВведите команду (1-7, q): ").strip().lower()
                
                if command == 'q':
                    print("👋 Выход из интерактивного режима")
                    break
                elif command == '1':
                    await self.test_device_selection()
                elif command == '2':
                    await self.test_audio_capture(5)
                elif command == '3':
                    await self.test_audio_capture(3)
                elif command == '4':
                    await self.test_continuous_recognition(3)
                elif command == '5':
                    await self.test_different_languages()
                elif command == '6':
                    self.show_status()
                elif command == '7':
                    self.setup_recognizer()
                else:
                    print("❌ Неизвестная команда")
                    
            except KeyboardInterrupt:
                print("\n👋 Выход по Ctrl+C")
                break
            except Exception as e:
                print(f"❌ Ошибка: {e}")

async def main():
    """Основная функция"""
    print("🎤 Тестер распознавания речи Nexy")
    print("=" * 50)
    
    tester = SpeechRecognitionTester()
    
    # Автоматические тесты
    print("🚀 Запуск автоматических тестов...")
    
    # 1. Тест выбора устройства
    device = await tester.test_device_selection()
    if device is None:
        print("❌ Не удалось выбрать аудио устройство")
        return
    
    # 2. Тест захвата аудио
    audio_success = await tester.test_audio_capture(3)
    
    # 3. Показываем статус
    tester.show_status()
    
    # 4. Интерактивный режим
    if audio_success:
        print("\n✅ Базовые тесты прошли успешно!")
        await tester.interactive_mode()
    else:
        print("\n⚠️ Базовые тесты не прошли.")
        print("🔧 Возможные причины:")
        print("  - Микрофон не работает")
        print("  - Нет разрешений на микрофон")
        print("  - Другие приложения используют микрофон")
        print("\n💡 Попробуйте интерактивный режим для детального тестирования")
        await tester.interactive_mode()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Тестирование прервано пользователем")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
