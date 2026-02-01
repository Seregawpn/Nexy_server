# Аудит: Race Conditions, Дубли и Централизация Конфигурации

## 🔍 Найденные проблемы

### 1. ⚠️ **Race Condition: `_google_audio_chunks`**

**Проблема:**
- `_google_audio_chunks` изменяется из **callback потока** (строка ~782) и из **основного async потока** (строки ~770, ~826, ~1030, ~1043, ~1484)
- Нет синхронизации (lock) между потоками
- Может привести к потере данных или некорректному состоянию

**Места изменений:**
```python
# Поток 1 (callback от listen_in_background):
def callback(recognizer, audio):
    self._google_audio_chunks.append(audio)  # ❌ Без синхронизации

# Поток 2 (основной async):
self._google_audio_chunks = []  # ❌ Без синхронизации
if self._google_audio_chunks and len(self._google_audio_chunks) > 0:  # ❌ Чтение без синхронизации
    self._google_audio_data = self._google_audio_chunks[-1]
```

**Риск:** Высокий - может привести к потере аудио данных или крашу

---

### 2. ⚠️ **Hardcoded значения sample_rate**

**Проблема:**
- `48000` встречается в 6 местах (строки 118, 121, 263, 595, 1124)
- `16000` встречается в 1 месте (строка 1701)
- Есть конфигурация `audio.input.target_rate: 16000`, но не везде используется

**Места:**
```python
self._streaming_sample_rate: int = 48000  # ❌ Hardcoded
self._batch_sample_rate: int = 48000      # ❌ Hardcoded
default_sample_rate = speech_config.get("default_sample_rate", 48000)  # ❌ Fallback hardcoded
target_sample_rate = 16000  # Google Speech API стандарт  # ❌ Hardcoded
```

**Риск:** Средний - рассинхронизация конфигурации

---

### 3. ⚠️ **Hardcoded timeout/delay значения**

**Проблема:**
- `await asyncio.sleep(0.5)` - hardcoded (строка 1002)
- `recognizer.adjust_for_ambient_noise(microphone, duration=0.5)` - hardcoded (строка 790)
- Нет централизации в конфиге

**Места:**
```python
await asyncio.sleep(0.5)  # ❌ Hardcoded - ждём завершения callback'ов
recognizer.adjust_for_ambient_noise(microphone, duration=0.5)  # ❌ Hardcoded
```

**Риск:** Низкий - но усложняет настройку

---

### 4. ⚠️ **Дублирование очистки `_google_audio_chunks`**

**Проблема:**
- `_google_audio_chunks = []` устанавливается в 6+ местах
- Риск забыть очистку в каком-то месте

**Места:**
- Строка 770: `self._google_audio_chunks: list = []` (начало записи)
- Строка 826: `self._google_audio_chunks = []` (ошибка активации)
- Строка 837: `self._google_audio_chunks = []` (ошибка AVF)
- Строка 1030: `self._google_audio_chunks = []` (ошибка нет данных)
- Строка 1043: `self._google_audio_chunks = []` (очистка после остановки)
- Строка 1484: `self._google_audio_chunks = []` (finally после распознавания)

**Риск:** Низкий - но усложняет поддержку

---

### 5. ⚠️ **Отсутствие синхронизации для `_recording_active`**

**Проблема:**
- `_recording_active` изменяется из разных мест без синхронизации
- Может быть race condition между async и sync потоками

**Места:**
```python
self._recording_active = True   # Строка 716
self._recording_active = False  # Строки 829, 841, 861, 918, 951, 2069, 2101
```

**Риск:** Средний - может привести к некорректному состоянию

---

### 6. ⚠️ **Неиспользуемые переменные**

**Проблема:**
- `_google_listening_thread` - объявлена, но не используется (строка 104)
- `_google_listening_event` - объявлена, но не используется активно (строка 105)

**Риск:** Низкий - но загрязняет код

---

## ✅ Решения

### Решение 1: Добавить Lock для `_google_audio_chunks`

```python
# В __init__:
self._google_audio_chunks_lock = threading.Lock()

# В callback:
def callback(recognizer, audio):
    with self._google_audio_chunks_lock:
        self._google_audio_chunks.append(audio)

# В основном потоке:
with self._google_audio_chunks_lock:
    if self._google_audio_chunks and len(self._google_audio_chunks) > 0:
        self._google_audio_data = self._google_audio_chunks[-1]
    self._google_audio_chunks = []
```

---

### Решение 2: Централизовать sample_rate в конфиге

**В `unified_config.yaml`:**
```yaml
audio:
  input:
    target_rate: 16000  # ✅ Уже есть
  output:
    source_rate: 48000  # ✅ Уже есть
  common:
    default_sample_rate: 48000  # ✅ Добавить для fallback
```

**В коде:**
```python
# Заменить все hardcoded значения на чтение из конфига
loader = UnifiedConfigLoader()
avf_config = loader.get_audio_avf_config()
default_sample_rate = avf_config.get('common', {}).get('default_sample_rate', 48000)
target_sample_rate = avf_config.get('input', {}).get('target_rate', 16000)
```

---

### Решение 3: Централизовать timeout/delay в конфиге

**В `unified_config.yaml`:**
```yaml
audio:
  google_recognition:
    callback_wait_sec: 0.5  # Ожидание завершения callback'ов
    ambient_noise_duration_sec: 0.5  # Длительность настройки фонового шума
```

**В коде:**
```python
callback_wait = avf_config.get('google_recognition', {}).get('callback_wait_sec', 0.5)
await asyncio.sleep(callback_wait)
```

---

### Решение 4: Создать метод для очистки состояния

```python
def _clear_google_recording_state(self):
    """Централизованная очистка состояния Google записи"""
    with self._google_audio_chunks_lock:
        self._google_audio_chunks = []
    self._google_audio_data = None
    self._google_stop_listening = None
    self._google_listening_event = None
    # ... остальные переменные
```

---

### Решение 5: Добавить синхронизацию для `_recording_active`

```python
self._recording_lock = threading.Lock()

def _set_recording_active(self, value: bool):
    with self._recording_lock:
        self._recording_active = value
```

---

## 📊 Приоритет исправлений

1. **Критично:** Решение 1 (Lock для `_google_audio_chunks`) - race condition
2. **Важно:** Решение 2 (Централизация sample_rate) - рассинхронизация конфига
3. **Желательно:** Решение 3 (Централизация timeout/delay) - улучшение настройки
4. **Желательно:** Решение 4 (Метод очистки) - упрощение поддержки
5. **Низкий приоритет:** Решение 5 (Lock для `_recording_active`) - менее критично

---

## 🔍 Дополнительные проверки

### Проверка централизации конфигурации

**✅ Уже централизовано:**
- `audio.avf.diagnostics.activation_duration_sec` - ✅
- `audio.avf.diagnostics.deactivation_pause_sec` - ✅
- `audio.input.target_rate` - ✅
- `audio.output.source_rate` - ✅

**❌ Нужно централизовать:**
- `sample_rate` fallback значения (48000, 16000) - ❌
- `callback_wait_sec` (0.5) - ❌
- `ambient_noise_duration_sec` (0.5) - ❌

---

## 📝 Итоговый чек-лист

- [ ] Добавить `threading.Lock` для `_google_audio_chunks`
- [ ] Заменить все hardcoded `48000` на чтение из конфига
- [ ] Заменить hardcoded `16000` на `audio.input.target_rate`
- [ ] Добавить `audio.google_recognition.callback_wait_sec` в конфиг
- [ ] Добавить `audio.google_recognition.ambient_noise_duration_sec` в конфиг
- [ ] Создать метод `_clear_google_recording_state()` для централизованной очистки
- [ ] Удалить неиспользуемые переменные (`_google_listening_thread`)
- [ ] Добавить синхронизацию для `_recording_active` (опционально)






