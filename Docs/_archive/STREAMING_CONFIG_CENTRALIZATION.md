# Централизация конфигурации стримингового распознавания

## ✅ Реализовано

Все параметры распознавания речи теперь централизованы в `config/unified_config.yaml` - единая точка управления.

---

## 📋 Централизованные параметры

### Общие параметры

```yaml
speech_recognition:
  language: "en-US"              # Язык распознавания (по умолчанию)
  default_sample_rate: 48000     # Sample rate по умолчанию (Hz)
```

### Стриминговое распознавание

```yaml
speech_recognition:
  streaming:
    enabled: true                 # Включить стриминговое распознавание
    on_device: true               # Предпочитать локальное распознавание
    language: null                # null = использовать общий language
    timeout_sec: 5.0             # Таймаут ожидания финального результата
    sample_rate: null             # null = использовать из audio_config или default_sample_rate
```

### Batch-распознавание (fallback)

```yaml
speech_recognition:
  batch:
    enabled: true                 # Включить fallback на batch-распознавание
    language: null                # null = использовать общий language
    sample_rate: null             # null = использовать из audio_config или default_sample_rate
```

---

## 🔄 Приоритет значений

### Language (язык)

1. **Стриминг:** `speech_recognition.streaming.language` (если не null)
2. **Batch:** `speech_recognition.batch.language` (если не null)
3. **Общий:** `speech_recognition.language` (fallback)
4. **Legacy:** `config.language` (для обратной совместимости)

### Sample Rate

1. **Стриминг:** `speech_recognition.streaming.sample_rate` (если не null)
2. **Batch:** `speech_recognition.batch.sample_rate` (если не null)
3. **Audio Config:** `audio_config.sample_rate` (если доступен)
4. **Общий:** `speech_recognition.default_sample_rate` (fallback)
5. **Хардкод:** `48000` (последний fallback)

### Timeout

1. **Стриминг:** `speech_recognition.streaming.timeout_sec`
2. **Хардкод:** `5.0` (fallback)

---

## 📝 Изменения в коде

### До централизации

```python
# ❌ Хардкод значений
language = self.config.language or "en-US"
on_device = True
timeout = 5.0
sample_rate = self._audio_config.sample_rate if self._audio_config else 48000
```

### После централизации

```python
# ✅ Чтение из unified_config.yaml
speech_config = loader.get("speech_recognition", {})
streaming_config = speech_config.get("streaming", {})

default_language = speech_config.get("language", "en-US")
streaming_language = streaming_config.get("language") or default_language
streaming_on_device = streaming_config.get("on_device", True)
streaming_timeout = streaming_config.get("timeout_sec", 5.0)
streaming_sample_rate = streaming_config.get("sample_rate") or (
    self._audio_config.sample_rate if self._audio_config else 
    speech_config.get("default_sample_rate", 48000)
)
```

---

## 🎯 Преимущества

1. **Единая точка управления** - все параметры в одном месте
2. **Гибкость** - легко менять параметры без изменения кода
3. **Консистентность** - одинаковые значения для всех компонентов
4. **Тестируемость** - легко менять параметры для тестов
5. **Документированность** - все параметры описаны в конфиге

---

## 🔧 Использование

### Изменение языка

```yaml
# unified_config.yaml
speech_recognition:
  language: "ru-RU"  # Изменить язык для всех режимов
```

### Изменение таймаута стриминга

```yaml
# unified_config.yaml
speech_recognition:
  streaming:
    timeout_sec: 10.0  # Увеличить таймаут до 10 секунд
```

### Отключение on-device режима

```yaml
# unified_config.yaml
speech_recognition:
  streaming:
    on_device: false  # Использовать серверное распознавание
```

### Разные языки для стриминга и batch

```yaml
# unified_config.yaml
speech_recognition:
  language: "en-US"  # Общий язык (fallback)
  streaming:
    language: "en-US"  # Язык для стриминга
  batch:
    language: "ru-RU"  # Язык для batch
```

---

## 📊 Сравнение: До и После

| Параметр | До | После |
|----------|-----|-------|
| Language | Хардкод `"en-US"` | `speech_recognition.language` |
| On-device | Хардкод `True` | `speech_recognition.streaming.on_device` |
| Timeout | Хардкод `5.0` | `speech_recognition.streaming.timeout_sec` |
| Sample rate | Хардкод `48000` | `speech_recognition.default_sample_rate` |

---

## ✅ Проверка централизации

Все параметры теперь читаются из конфигурации:

- ✅ `language` - из `speech_recognition.language` или `streaming.language`/`batch.language`
- ✅ `on_device` - из `speech_recognition.streaming.on_device`
- ✅ `timeout_sec` - из `speech_recognition.streaming.timeout_sec`
- ✅ `sample_rate` - из `speech_recognition.default_sample_rate` или `streaming.sample_rate`/`batch.sample_rate`

**Нет хардкода значений** (кроме fallback для обратной совместимости).



