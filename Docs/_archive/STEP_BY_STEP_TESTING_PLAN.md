# Поэтапный план тестирования аудиосистемы

## Дата: 2025-12-09

## Цель
Разбить систему на маленькие части и тестировать каждую отдельно, чтобы точно определить, на каком этапе возникает проблема.

---

## ЭТАП 1: Проверка базовой инфраструктуры

### Тест 1.1: Проверка импортов и зависимостей

**Что проверяем:** Все модули импортируются без ошибок

**Команда:**
```bash
cd /Users/sergiyzasorin/Development/Nexy/client\(prod\)
python3 -c "
import sys
sys.path.insert(0, 'client')

# Проверка AVFoundation
try:
    from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
    print('✅ AVFAudioEngine импортирован')
except Exception as e:
    print(f'❌ AVFAudioEngine: {e}')

# Проверка SFSpeechRecognizer
try:
    from modules.speech_recognition_sf import SFSpeechRecognizerWrapper
    print('✅ SFSpeechRecognizerWrapper импортирован')
except Exception as e:
    print(f'❌ SFSpeechRecognizerWrapper: {e}')

# Проверка SpeechRecognition
try:
    import speech_recognition as sr
    print('✅ speech_recognition импортирован')
except Exception as e:
    print(f'❌ speech_recognition: {e}')

# Проверка numpy/scipy
try:
    import numpy as np
    from scipy import signal
    print('✅ numpy и scipy импортированы')
except Exception as e:
    print(f'❌ numpy/scipy: {e}')
"
```

**Ожидаемый результат:** Все модули импортируются без ошибок

**Если ошибка:** Установить недостающие зависимости

---

### Тест 1.2: Проверка разрешений macOS

**Что проверяем:** Разрешения для микрофона и Speech Recognition

**Команда:**
```bash
python3 -c "
import sys
sys.path.insert(0, 'client')

# Проверка разрешения микрофона
from modules.permissions.core.mac_permissions import MacPermissionsChecker
checker = MacPermissionsChecker()
mic_status = checker.check_microphone_permission()
print(f'🎤 Микрофон: {mic_status}')

# Проверка разрешения Speech Recognition
try:
    from Speech import SFSpeechRecognizer, SFSpeechRecognizerAuthorizationStatus
    auth_status = SFSpeechRecognizer.authorizationStatus()
    status_map = {
        0: 'notDetermined',
        1: 'denied',
        2: 'restricted',
        3: 'authorized'
    }
    print(f'🗣️ Speech Recognition: {status_map.get(auth_status, \"unknown\")}')
except Exception as e:
    print(f'❌ Ошибка проверки Speech Recognition: {e}')
"
```

**Ожидаемый результат:**
- Микрофон: `granted`
- Speech Recognition: `authorized`

**Если ошибка:** Включить разрешения в System Preferences → Privacy

---

## ЭТАП 2: Тестирование AVFAudioEngine

### Тест 2.1: Создание AVFAudioEngine

**Что проверяем:** AVFAudioEngine создаётся без ошибок

**Команда:**
```bash
python3 -c "
import sys
import asyncio
sys.path.insert(0, 'client')

from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
from modules.audio_avf.config.types import AudioConfig

async def test():
    config = AudioConfig(
        sample_rate=48000,
        channels=1,
        input_device=None  # Использовать системный по умолчанию
    )
    
    try:
        engine = AVFAudioEngine(config)
        print('✅ AVFAudioEngine создан успешно')
        print(f'   - Sample rate: {config.sample_rate}')
        print(f'   - Channels: {config.channels}')
        return True
    except Exception as e:
        print(f'❌ Ошибка создания AVFAudioEngine: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** `✅ AVFAudioEngine создан успешно`

**Если ошибка:** Проверить конфигурацию и разрешения

---

### Тест 2.2: Запись одного чанка аудио

**Что проверяем:** AVFAudioEngine может записать хотя бы один чанк

**Команда:**
```bash
python3 -c "
import sys
import asyncio
import time
sys.path.insert(0, 'client')

from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
from modules.audio_avf.config.types import AudioConfig

chunks_received = []
chunk_count = 0

async def audio_callback(data: bytes, sample_rate: int, channels: int):
    global chunk_count
    chunk_count += 1
    chunks_received.append({
        'data': data,
        'sample_rate': sample_rate,
        'channels': channels,
        'size': len(data)
    })
    print(f'📦 Чанк {chunk_count}: {len(data)} bytes, {sample_rate}Hz, {channels}ch')

async def test():
    config = AudioConfig(sample_rate=48000, channels=1)
    engine = AVFAudioEngine(config)
    
    try:
        print('🎤 Запуск записи...')
        success = await engine.start_input(callback=audio_callback)
        
        if not success:
            print('❌ Не удалось запустить запись')
            return False
        
        print('⏳ Ожидание чанков (3 секунды)...')
        await asyncio.sleep(3)
        
        print('🛑 Остановка записи...')
        result = await engine.stop_input()
        
        if chunk_count == 0:
            print('❌ Не получено ни одного чанка!')
            return False
        
        print(f'✅ Получено {chunk_count} чанков')
        print(f'   - Первый чанк: {chunks_received[0][\"size\"]} bytes')
        print(f'   - Sample rate: {chunks_received[0][\"sample_rate\"]}Hz')
        print(f'   - Channels: {chunks_received[0][\"channels\"]}')
        
        return True
        
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** Получено хотя бы 1 чанк с валидными данными

**Если ошибка:** Проблема с микрофоном или разрешениями

---

### Тест 2.3: Сохранение записанного аудио в WAV

**Что проверяем:** Записанное аудио можно сохранить и прослушать

**Команда:**
```bash
python3 -c "
import sys
import asyncio
import wave
import numpy as np
sys.path.insert(0, 'client')

from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
from modules.audio_avf.config.types import AudioConfig

audio_chunks = []
sample_rate = None
channels = None

async def audio_callback(data: bytes, sr: int, ch: int):
    global sample_rate, channels
    sample_rate = sr
    channels = ch
    audio_chunks.append(data)

async def test():
    config = AudioConfig(sample_rate=48000, channels=1)
    engine = AVFAudioEngine(config)
    
    try:
        print('🎤 Запись 2 секунды...')
        await engine.start_input(callback=audio_callback)
        await asyncio.sleep(2)
        result = await engine.stop_input()
        
        if not audio_chunks:
            print('❌ Нет аудио данных')
            return False
        
        # Объединяем чанки
        total_audio = b''.join(audio_chunks)
        print(f'📊 Всего записано: {len(total_audio)} bytes')
        
        # Анализ аудио
        audio_array = np.frombuffer(total_audio, dtype=np.int16)
        rms = np.sqrt(np.mean(audio_array.astype(np.float32) ** 2))
        print(f'📊 RMS: {rms:.2f}')
        print(f'📊 Min: {audio_array.min()}, Max: {audio_array.max()}, Mean: {audio_array.mean():.1f}')
        
        # Сохранение в WAV
        wav_path = '/tmp/test_avf_recording.wav'
        with wave.open(wav_path, 'wb') as wav_file:
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(2)  # int16
            wav_file.setframerate(sample_rate)
            wav_file.writeframes(total_audio)
        
        print(f'💾 Аудио сохранено: {wav_path}')
        print(f'   👉 ПРОСЛУШАЙТЕ ФАЙЛ для проверки качества')
        
        if rms < 100:
            print('⚠️ ВНИМАНИЕ: RMS очень низкий (< 100), возможно тишина')
        
        return True
        
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** 
- WAV файл создан
- RMS > 100 (есть звук)
- Файл можно прослушать

**Если ошибка:** Проверить микрофон и системные настройки звука

---

## ЭТАП 3: Тестирование SFSpeechRecognizer

### Тест 3.1: Создание и проверка доступности

**Что проверяем:** SFSpeechRecognizer можно создать и проверить доступность

**Команда:**
```bash
python3 -c "
import sys
import asyncio
sys.path.insert(0, 'client')

from modules.speech_recognition_sf import SFSpeechRecognizerWrapper

async def test():
    try:
        print('🔍 Создание SFSpeechRecognizerWrapper...')
        recognizer = SFSpeechRecognizerWrapper(language='en-US', on_device=True)
        print('✅ Recognizer создан')
        
        print('🔍 Проверка доступности...')
        is_available = await recognizer.is_available()
        
        if is_available:
            print('✅ SFSpeechRecognizer доступен')
            return True
        else:
            print('❌ SFSpeechRecognizer недоступен')
            print('   💡 Проверьте разрешения в System Preferences → Privacy → Speech Recognition')
            return False
            
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** `✅ SFSpeechRecognizer доступен`

**Если ошибка:** Включить разрешение Speech Recognition

---

### Тест 3.2: Запуск сессии распознавания

**Что проверяем:** Можно запустить сессию распознавания

**Команда:**
```bash
python3 -c "
import sys
import asyncio
sys.path.insert(0, 'client')

from modules.speech_recognition_sf import SFSpeechRecognizerWrapper

results_received = []
errors_received = []

def on_result(text: str, is_final: bool):
    results_received.append({'text': text, 'is_final': is_final})
    status = 'ФИНАЛЬНЫЙ' if is_final else 'промежуточный'
    print(f'📝 Результат ({status}): \"{text[:50]}...\"')

def on_error(error: str):
    errors_received.append(error)
    print(f'❌ Ошибка: {error}')

async def test():
    try:
        recognizer = SFSpeechRecognizerWrapper(language='en-US', on_device=True)
        
        if not await recognizer.is_available():
            print('❌ Recognizer недоступен')
            return False
        
        print('🎤 Запуск сессии распознавания...')
        started = await recognizer.start_recognition(
            on_result=on_result,
            on_error=on_error,
            sample_rate=48000
        )
        
        if not started:
            print('❌ Не удалось запустить сессию')
            return False
        
        print('✅ Сессия запущена')
        print('⏳ Ожидание 1 секунда...')
        await asyncio.sleep(1)
        
        # Проверяем состояние
        state = getattr(recognizer, '_state', None)
        print(f'📊 Состояние: {state}')
        
        if len(errors_received) > 0:
            print(f'⚠️ Получено {len(errors_received)} ошибок')
            return False
        
        print('✅ Сессия работает корректно')
        return True
        
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** `✅ Сессия запущена` и состояние = `RECOGNIZING`

**Если ошибка:** Проблема с запуском сессии

---

### Тест 3.3: Отправка тестового аудио чанка

**Что проверяем:** Можно отправить аудио чанк в recognizer

**Команда:**
```bash
python3 -c "
import sys
import asyncio
import numpy as np
sys.path.insert(0, 'client')

from modules.speech_recognition_sf import SFSpeechRecognizerWrapper

results_received = []

def on_result(text: str, is_final: bool):
    results_received.append({'text': text, 'is_final': is_final})
    status = 'ФИНАЛЬНЫЙ' if is_final else 'промежуточный'
    print(f'📝 Результат ({status}): \"{text[:50]}...\"')

def on_error(error: str):
    print(f'❌ Ошибка: {error}')

async def test():
    try:
        recognizer = SFSpeechRecognizerWrapper(language='en-US', on_device=True)
        
        if not await recognizer.is_available():
            print('❌ Recognizer недоступен')
            return False
        
        print('🎤 Запуск сессии...')
        started = await recognizer.start_recognition(
            on_result=on_result,
            on_error=on_error,
            sample_rate=48000
        )
        
        if not started:
            print('❌ Не удалось запустить сессию')
            return False
        
        # Создаём тестовый чанк (тишина + небольшой сигнал)
        print('📦 Создание тестового аудио чанка...')
        sample_rate = 48000
        duration = 0.1  # 100ms
        samples = int(sample_rate * duration)
        
        # Генерируем простой синусоидальный сигнал (440Hz)
        t = np.linspace(0, duration, samples)
        signal = np.sin(2 * np.pi * 440 * t) * 0.3  # Тихий сигнал
        audio_float = (signal * 32767).astype(np.int16)
        audio_bytes = audio_float.tobytes()
        
        print(f'📦 Отправка чанка: {len(audio_bytes)} bytes, {sample_rate}Hz')
        success = recognizer.append_audio(audio_bytes, sample_rate, channels=1)
        
        if not success:
            print('❌ append_audio() вернул False')
            state = getattr(recognizer, '_state', None)
            print(f'   Состояние recognizer: {state}')
            return False
        
        print('✅ Чанк отправлен успешно')
        await asyncio.sleep(0.5)  # Даём время на обработку
        
        print('🛑 Завершение распознавания...')
        final_text = await recognizer.finish_recognition(timeout=2.0)
        
        print(f'📊 Получено результатов: {len(results_received)}')
        print(f'📊 Финальный текст: \"{final_text}\"')
        
        return True
        
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** `✅ Чанк отправлен успешно`

**Если ошибка:** Проблема с форматом аудио или состоянием recognizer

---

## ЭТАП 4: Интеграция AVF + SFSpeechRecognizer

### Тест 4.1: Запись через AVF и отправка в SFSpeechRecognizer

**Что проверяем:** AVF записывает, чанки отправляются в SFSpeechRecognizer

**Команда:**
```bash
python3 -c "
import sys
import asyncio
sys.path.insert(0, 'client')

from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
from modules.audio_avf.config.types import AudioConfig
from modules.speech_recognition_sf import SFSpeechRecognizerWrapper

results_received = []
chunks_sent = 0
chunks_failed = 0

def on_result(text: str, is_final: bool):
    results_received.append({'text': text, 'is_final': is_final})
    status = 'ФИНАЛЬНЫЙ' if is_final else 'промежуточный'
    print(f'📝 [{status}]: \"{text[:50]}...\"')

def on_error(error: str):
    print(f'❌ Ошибка recognizer: {error}')

async def test():
    try:
        # Создаём recognizer
        recognizer = SFSpeechRecognizerWrapper(language='en-US', on_device=True)
        
        if not await recognizer.is_available():
            print('❌ Recognizer недоступен')
            return False
        
        # Запускаем сессию
        print('🎤 Запуск сессии распознавания...')
        started = await recognizer.start_recognition(
            on_result=on_result,
            on_error=on_error,
            sample_rate=48000
        )
        
        if not started:
            print('❌ Не удалось запустить сессию')
            return False
        
        # Создаём AVF engine
        config = AudioConfig(sample_rate=48000, channels=1)
        engine = AVFAudioEngine(config)
        
        async def audio_callback(data: bytes, sample_rate: int, channels: int):
            global chunks_sent, chunks_failed
            success = recognizer.append_audio(data, sample_rate, channels)
            if success:
                chunks_sent += 1
                if chunks_sent <= 3:  # Логируем первые 3
                    print(f'✅ Чанк {chunks_sent} отправлен: {len(data)} bytes')
            else:
                chunks_failed += 1
                print(f'❌ Чанк не отправлен (failed: {chunks_failed})')
        
        print('🎤 Запуск записи через AVF...')
        print('💬 ГОВОРИТЕ СЕЙЧАС (3 секунды)...')
        await engine.start_input(callback=audio_callback)
        await asyncio.sleep(3)
        await engine.stop_input()
        
        print(f'📊 Статистика:')
        print(f'   - Отправлено чанков: {chunks_sent}')
        print(f'   - Неудачных: {chunks_failed}')
        print(f'   - Получено результатов: {len(results_received)}')
        
        if chunks_sent == 0:
            print('❌ Ни один чанк не был отправлен!')
            return False
        
        print('🛑 Завершение распознавания...')
        final_text = await recognizer.finish_recognition(timeout=2.0)
        
        print(f'📊 Финальный результат: \"{final_text}\"')
        
        return True
        
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** 
- Чанки отправляются (`chunks_sent > 0`)
- Получены промежуточные результаты
- Финальный результат не пустой

**Если ошибка:** Проблема интеграции между AVF и SFSpeechRecognizer

---

## ЭТАП 5: Тестирование Batch распознавания

### Тест 5.1: Распознавание через Google Speech API

**Что проверяем:** Batch распознавание работает с тестовым аудио

**Команда:**
```bash
python3 -c "
import sys
import asyncio
import numpy as np
sys.path.insert(0, 'client')

import speech_recognition as sr

async def test():
    try:
        # Создаём тестовое аудио (1 секунда синусоиды 440Hz)
        sample_rate = 16000  # Google требует 16kHz
        duration = 1.0
        samples = int(sample_rate * duration)
        
        t = np.linspace(0, duration, samples)
        signal = np.sin(2 * np.pi * 440 * t) * 0.5
        audio_int16 = (signal * 32767).astype(np.int16)
        audio_bytes = audio_int16.tobytes()
        
        print(f'📦 Тестовое аудио: {len(audio_bytes)} bytes, {sample_rate}Hz')
        
        # Создаём AudioData
        audio_data = sr.AudioData(audio_bytes, sample_rate, 2)
        
        # Распознаём
        recognizer = sr.Recognizer()
        print('🔍 Отправка на Google Speech API...')
        
        try:
            text = recognizer.recognize_google(audio_data, language='en-US')
            print(f'✅ Распознано: \"{text}\"')
            return True
        except sr.UnknownValueError:
            print('⚠️ Google Speech API не смог распознать (ожидаемо для тестового сигнала)')
            print('   Это нормально - тестовый сигнал не является речью')
            return True  # Считаем успехом, т.к. API работает
        except sr.RequestError as e:
            print(f'❌ Ошибка запроса: {e}')
            print('   💡 Проверьте интернет-соединение')
            return False
            
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()
        return False

result = asyncio.run(test())
exit(0 if result else 1)
"
```

**Ожидаемый результат:** Google Speech API отвечает (даже если UnknownValueError - это нормально)

**Если ошибка:** Проблема с интернетом или API

---

## ЭТАП 6: Полная интеграция через VoiceRecognitionIntegration

### Тест 6.1: Запуск приложения и проверка инициализации

**Что проверяем:** VoiceRecognitionIntegration инициализируется корректно

**Команда:**
```bash
cd /Users/sergiyzasorin/Development/Nexy/client\(prod\)
export NEXY_DEBUG_SAVE_AUDIO=true
python client/main.py 2>&1 | grep -E "(SFSpeech|AVF|VoiceRecognition)" | head -20
```

**Ожидаемый результат:** Видим логи успешной инициализации

**Если ошибка:** Проблема с конфигурацией или зависимостями

---

### Тест 6.2: Запись через приложение

**Что проверяем:** При нажатии Ctrl+N запись начинается

**Действия:**
1. Запустить приложение
2. Зажать Ctrl+N
3. Произнести короткую фразу
4. Отпустить Ctrl+N

**Проверка логов:**
```bash
# В другом терминале
tail -f ~/Library/Logs/Nexy/*.log | grep -E "(recording_start|microphone.opened|SFSpeech|AVF)"
```

**Ожидаемый результат:**
- `voice.recording_start`
- `microphone.opened`
- `[AVF] Микрофон открыт`
- `[SFSpeech] Стриминговая сессия запущена` (если стриминг доступен)

**Если ошибка:** Проблема с обработкой событий или запуском записи

---

## Чек-лист тестирования

Используйте этот чек-лист для отслеживания прогресса:

- [ ] **Этап 1.1**: Импорты работают
- [ ] **Этап 1.2**: Разрешения macOS включены
- [ ] **Этап 2.1**: AVFAudioEngine создаётся
- [ ] **Этап 2.2**: AVF записывает чанки
- [ ] **Этап 2.3**: WAV файл создаётся и прослушивается
- [ ] **Этап 3.1**: SFSpeechRecognizer доступен
- [ ] **Этап 3.2**: Сессия запускается
- [ ] **Этап 3.3**: Чанки отправляются
- [ ] **Этап 4.1**: AVF + SFSpeechRecognizer работают вместе
- [ ] **Этап 5.1**: Batch распознавание работает
- [ ] **Этап 6.1**: Приложение запускается
- [ ] **Этап 6.2**: Запись через приложение работает

---

## Рекомендации

1. **Тестируйте по порядку** - не переходите к следующему этапу, пока текущий не работает
2. **Фиксируйте результаты** - записывайте, какие тесты прошли, а какие нет
3. **Проверяйте логи** - каждый тест выводит подробную информацию
4. **Используйте WAV файлы** - прослушивайте записанное аудио для проверки качества
5. **Изолируйте проблемы** - если тест падает, не переходите дальше, пока не исправите

---

## Быстрый старт

Запустите все тесты последовательно:

```bash
cd /Users/sergiyzasorin/Development/Nexy/client\(prod\)

# Этап 1
echo "=== ЭТАП 1: Инфраструктура ==="
# Запустите тесты 1.1 и 1.2

# Этап 2
echo "=== ЭТАП 2: AVFAudioEngine ==="
# Запустите тесты 2.1, 2.2, 2.3

# Этап 3
echo "=== ЭТАП 3: SFSpeechRecognizer ==="
# Запустите тесты 3.1, 3.2, 3.3

# И так далее...
```
