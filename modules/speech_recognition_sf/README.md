# SFSpeechRecognizer Module

## Обзор

Модуль стримингового распознавания речи на основе нативного macOS SFSpeechRecognizer.

## Преимущества

| Характеристика | SpeechRecognition (текущий) | SFSpeechRecognizer |
|----------------|-----------------------------|--------------------|
| Тип | Batch (весь буфер) | Streaming (реал. время) |
| Задержка | 1-3 сек после остановки | ~0-200ms |
| Интернет | Требуется | Опционально (On-Device) |
| Платформа | Кроссплатформенный | Только macOS |
| Стоимость | Бесплатно (лимиты Google) | Бесплатно |

## Архитектура

```
AVFAudioEngine
    │
    └─► audio_callback(data)
            │
            └─► SFSpeechRecognizer.append(data)
                    │
                    ├─► Промежуточные результаты (isFinal=False)
                    │
                    └─► Финальный результат (isFinal=True)
```

## API

```python
from modules.speech_recognition_sf import SFSpeechRecognizerWrapper

# Создание
recognizer = SFSpeechRecognizerWrapper(language="en-US")

# Проверка доступности
if await recognizer.is_available():
    
    # Начало стриминга
    await recognizer.start_recognition(
        on_result=lambda text, is_final: print(text),
        on_error=lambda error: print(error)
    )
    
    # Отправка аудио чанков (в реальном времени)
    recognizer.append_audio(audio_data)
    
    # Завершение
    final_text = await recognizer.finish_recognition()
```

## Требования

1. **macOS 10.15+**
2. **Разрешение Speech Recognition** в System Preferences
3. **PyObjC** для доступа к Speech framework

## Разрешения

В `Info.plist`:
```xml
<key>NSSpeechRecognitionUsageDescription</key>
<string>Nexy needs speech recognition to understand your voice commands.</string>
</key>
```

## Ограничения

1. **On-Device (локальное)**
   - Работает без интернета
   - Нет лимитов
   - Поддерживает не все языки

2. **Server-based (Siri)**
   - Требует интернет
   - Лимит: 1000 запросов/час
   - Все языки

## Статус

⬜ **Планируется** — требуется реализация

## Файлы

- `core/sf_speech_recognizer.py` — основной wrapper
- `core/types.py` — типы данных
- `tests/` — тесты



