#!/usr/bin/env python3
"""Тест прямой работы библиотеки SpeechRecognition с микрофоном (без AVF)"""

import sys
import logging
import time

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def test_speech_recognition_direct():
    """Тест прямой работы SpeechRecognition с микрофоном"""
    print("=" * 60)
    print("ТЕСТ: Прямая работа SpeechRecognition с микрофоном")
    print("=" * 60)
    
    try:
        import speech_recognition as sr
        
        print("\n✅ Библиотека speech_recognition импортирована")
        
        # Создаём Recognizer
        recognizer = sr.Recognizer()
        print("✅ Recognizer создан")
        
        # Создаём Microphone
        microphone = sr.Microphone()
        print("✅ Microphone создан")
        
        # Настраиваем для фонового шума
        print("\n🔧 Настраиваем микрофон для фонового шума...")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print(f"✅ Энергетический порог установлен: {recognizer.energy_threshold}")
        
        # Записываем аудио
        print("\n🎤 Начинаем запись...")
        print("💡 Произнесите короткую фразу на английском (например, 'Hello' или 'Hi')")
        print("💡 Запись будет длиться 3 секунды...")
        
        with microphone as source:
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            print(f"✅ Аудио записано: {len(audio.frame_data)} bytes, {audio.sample_rate}Hz, {audio.sample_width} bytes/sample")
        
        # Распознаём речь
        print("\n🔍 Начинаем распознавание через Google Speech API...")
        print("💡 Это может занять несколько секунд...")
        
        try:
            start_time = time.time()
            text = recognizer.recognize_google(audio, language="en-US")
            elapsed_time = time.time() - start_time
            
            print(f"\n✅ Распознавание успешно за {elapsed_time:.2f}s!")
            print(f"📝 Распознанный текст: '{text}'")
            print("\n✅ ТЕСТ ПРОЙДЕН!")
            return True
            
        except sr.UnknownValueError:
            print("\n❌ Google Speech API не смог распознать речь")
            print("💡 Возможные причины:")
            print("   - Тишина в аудио")
            print("   - Неразборчивая речь")
            print("   - Неправильный язык (en-US vs реальный язык)")
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН (UnknownValueError)")
            return False
            
        except sr.RequestError as e:
            print(f"\n❌ Ошибка запроса к Google Speech API: {e}")
            print("💡 Возможные причины:")
            print("   - Нет интернета")
            print("   - Google Speech API недоступен")
            print("   - Rate limit превышен")
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН (RequestError)")
            return False
            
    except ImportError as e:
        print(f"\n❌ Ошибка импорта: {e}")
        print("💡 Установите библиотеку: pip install SpeechRecognition")
        return False
        
    except Exception as e:
        print(f"\n❌ Неожиданная ошибка: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_speech_recognition_direct()
    sys.exit(0 if success else 1)

