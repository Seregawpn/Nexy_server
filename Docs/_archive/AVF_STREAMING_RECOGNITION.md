# AVFoundation + SFSpeechRecognizer Streaming Recognition

## Обзор

Этот документ описывает интеграцию стримингового распознавания речи на основе нативных macOS API:
- **AVFAudioEngine** — захват аудио через AVFoundation
- **SFSpeechRecognizer** — распознавание речи в реальном времени

## Сравнение подходов

### Batch (предыдущий подход)

```
┌─────────────────────────────────────────────────────────────┐
│  LONG_PRESS → Запись → Накопление → RELEASE → Распознавание │
│                                                 │           │
│                                        ┌────────▼────────┐  │
│                                        │ Google API     │  │
│                                        │ (1-3 сек)      │  │
│                                        └────────┬────────┘  │
│                                                 │           │
│                                          Результат          │
└─────────────────────────────────────────────────────────────┘
```

**Проблема:** Задержка 1-3 секунды после отпускания клавиши.

### Streaming (новый подход)

```
┌─────────────────────────────────────────────────────────────┐
│  LONG_PRESS → Запись + Отправка чанков → RELEASE → Результат│
│                       │                             │       │
│              ┌────────▼────────┐                    │       │
│              │ SFSpeechRecog.  │────────────────────┘       │
│              │ (real-time)     │    ~0-200ms                │
│              └─────────────────┘                            │
└─────────────────────────────────────────────────────────────┘
```

**Преимущество:** Результат готов почти мгновенно (~0-200ms) после отпускания клавиши.

## Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                    VoiceRecognitionIntegration              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  _on_recording_start():                                      │
│    ├─► SFSpeechRecognizer.start_recognition()               │
│    └─► AVFAudioEngine.start_input(callback)                 │
│                                                              │
│  audio_callback(data):                                       │
│    └─► SFSpeechRecognizer.append_audio(data)  ← real-time   │
│                                                              │
│  _on_recording_stop():                                       │
│    ├─► AVFAudioEngine.stop_input()                          │
│    └─► SFSpeechRecognizer.finish_recognition()              │
│            │                                                 │
│            └─► voice.recognition_completed (~0-200ms)       │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## Конфигурация

### unified_config.yaml

```yaml
speech_recognition:
  streaming:
    enabled: true           # Включить стриминговое распознавание
    on_device: true         # Локальное распознавание (без интернета)
    language: "en-US"       # Язык распознавания
    timeout_sec: 5.0        # Таймаут финального результата

  batch:
    enabled: true           # Fallback на batch (SpeechRecognition library)
    language: "en-US"
```

### Environment Variables

- `NEXY_DISABLE_STREAMING_RECOGNITION=true` — отключить стриминг, использовать batch

## Компоненты

### SFSpeechRecognizerWrapper

Файл: `modules/speech_recognition_sf/core/sf_speech_recognizer.py`

```python
from modules.speech_recognition_sf import SFSpeechRecognizerWrapper

recognizer = SFSpeechRecognizerWrapper(language="en-US", on_device=True)

# Проверка доступности
if await recognizer.is_available():
    
    # Запуск стриминга
    await recognizer.start_recognition(
        on_result=lambda text, is_final: print(text),
        on_error=lambda error: print(error),
        sample_rate=48000
    )
    
    # Отправка аудио чанков (в реальном времени)
    recognizer.append_audio(audio_data, sample_rate=48000, channels=1)
    
    # Завершение и получение финального результата
    final_text = await recognizer.finish_recognition(timeout=5.0)
```

### Состояния распознавания

```python
class RecognitionState(Enum):
    IDLE = "idle"           # Готов к работе
    STARTING = "starting"   # Запуск
    RECOGNIZING = "recognizing"  # Активное распознавание
    FINISHING = "finishing" # Завершение
    FINISHED = "finished"   # Завершено
    ERROR = "error"         # Ошибка
```

## Требования

### macOS

1. **macOS 10.15+** (Catalina и выше)
2. **Speech Recognition Permission** — пользователь должен разрешить распознавание речи

### Info.plist

```xml
<key>NSSpeechRecognitionUsageDescription</key>
<string>Nexy needs speech recognition to understand your voice commands.</string>
```

### PyObjC

Speech framework доступен через PyObjC:

```python
from Speech import SFSpeechRecognizer, SFSpeechAudioBufferRecognitionRequest
```

## Режимы работы

### On-Device (локальный)

- **Преимущества:**
  - Работает без интернета
  - Нет лимитов на количество запросов
  - Низкая задержка

- **Ограничения:**
  - Поддерживает не все языки
  - Качество может быть ниже

### Server-based (Siri)

- **Преимущества:**
  - Высокое качество распознавания
  - Поддержка всех языков

- **Ограничения:**
  - Требует интернет
  - Лимит: 1000 запросов/час

## Fallback механизм

Если стриминговое распознавание недоступно:

1. `SFSpeechRecognizer.is_available()` → `false`
2. Автоматический fallback на batch-распознавание
3. Используется `SpeechRecognition` library + Google Speech API

```python
if self._use_streaming and self._sf_recognizer is not None:
    # Streaming path
    final_text = await self._sf_recognizer.finish_recognition()
elif self._audio_buffer:
    # Batch fallback
    await self._recognize_avf_audio(total_audio, sample_rate, channels, session_id)
```

## Логирование

### Стриминг

```
🎤 [SFSpeech] Запуск стримингового распознавания для session 123456
🎤 [SFSpeech] Отправлен чанк: 4096 bytes
🎤 [SFSpeech] Отправлен чанк: 4096 bytes
🎤 [SFSpeech] Завершение стримингового распознавания...
✅ [SFSpeech] Стриминговый результат: 'Hello world' (session=123456)
```

### Batch fallback

```
🔊 [AVF] Накоплен чанк: 4096 bytes (всего: 8192 bytes)
🔊 [AVF] Накоплено 32768 bytes аудио для batch-распознавания
📤 [AVF] Отправляем на распознавание: 32768 bytes, 48000Hz, 1ch
✅ [AVF] Распознавание успешно: 'Hello world' (session=123456)
```

## Метрики

| Метрика | Batch | Streaming |
|---------|-------|-----------|
| Задержка после RELEASE | 1-3 сек | 0-200 мс |
| Требует интернет | Да | Опционально |
| Промежуточные результаты | Нет | Да |
| CPU нагрузка | Низкая | Средняя |

## Тестирование

### Ручное тестирование

1. Запустить приложение
2. Нажать и удерживать Control+N
3. Произнести команду
4. Отпустить Control+N
5. Проверить время до появления результата

### Логи для проверки

```bash
# Проверить режим работы
grep "SFSpeech\|стриминг\|streaming" log.md
```

## Известные ограничения

1. **Только macOS** — SFSpeechRecognizer не кроссплатформенный
2. **Требует разрешение** — пользователь должен разрешить Speech Recognition
3. **Лимиты Apple** — для server-based режима 1000 запросов/час

## Связанные документы

- `modules/speech_recognition_sf/README.md` — документация модуля
- `Docs/AVF_SPEECH_RECOGNITION_FLOW.md` — полный поток распознавания
- `config/unified_config.yaml` — конфигурация



