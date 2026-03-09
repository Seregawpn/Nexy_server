# План замены Azure TTS на Edge TTS

## 📋 Цель
Полностью заменить Azure TTS на Edge TTS во всей системе.

## 🔄 Изменения

### 1. Создать EdgeTTSProvider
**Файл:** `modules/audio_generation/providers/edge_tts_provider.py`
- Реализовать `UniversalProviderInterface`
- Поддержка streaming через `edge_tts.Communicate.stream()`
- Конвертация MP3 → PCM для совместимости
- Настройки: voice, rate, volume, pitch

### 2. Обновить AudioProcessor
**Файл:** `modules/audio_generation/core/audio_processor.py`
- Заменить `AzureTTSProvider` на `EdgeTTSProvider`
- Обновить методы `_create_provider()` и `get_azure_config()` → `get_edge_tts_config()`
- Обновить комментарии и логи

### 3. Обновить AudioGenerationConfig
**Файл:** `modules/audio_generation/config.py`
- Удалить все Azure настройки
- Добавить Edge TTS настройки
- Обновить валидацию (не требует ключей)
- Обновить методы конфигурации

### 4. Обновить unified_config
**Файл:** `config/unified_config.py`
- Заменить `AudioConfig` с Azure на Edge TTS настройки
- Обновить `from_env()` метод

### 5. Обновить config.env.example
**Файл:** `config.env.example`
- Удалить Azure настройки
- Добавить Edge TTS настройки (опционально, т.к. не требует ключей)

### 6. Обновить requirements.txt
**Файл:** `server/requirements.txt`
- Оставить `edge-tts>=7.2.7`
- Опционально: удалить `azure-cognitiveservices-speech` (или оставить для совместимости)

## ✅ План выполнения

1. ✅ Создать EdgeTTSProvider
2. ✅ Обновить AudioProcessor
3. ✅ Обновить AudioGenerationConfig
4. ✅ Обновить unified_config
5. ✅ Обновить config.env.example
6. ✅ Протестировать
7. ✅ Удалить/закомментировать AzureTTSProvider (опционально)

