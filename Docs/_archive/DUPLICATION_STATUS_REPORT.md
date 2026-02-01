# Отчёт о статусе дублирования в аудиосистеме

**Дата:** 2025-12-05  
**Статус:** Частично исправлено, осталось дублирование

## ✅ Что уже централизовано

### 1. Закрытие потоков ✅ **ИСПРАВЛЕНО**
- **Было:** 13+ мест с прямыми вызовами `_stream_manager.close_stream()`
- **Стало:** 2 централизованных метода:
  - `_close_stream_safely()` (async)
  - `_close_stream_safely_sync()` (sync)
- **Статус:** ✅ **ПОЛНОСТЬЮ ЦЕНТРАЛИЗОВАНО**
- **Примечание:** Внутри этих методов всё ещё есть прямые вызовы `_stream_manager.close_stream()`, но это нормально, так как методы сами являются централизованными обёртками.

---

## ⚠️ Что ещё осталось (дублирование)

### 1. Определение Bluetooth устройств ⚠️ **ДУБЛИРОВАНИЕ ОСТАЛОСЬ**

**Централизованная функция:** ✅ `modules/audio_core/device_utils.py::is_bluetooth_device()`

**Дублирующиеся реализации:**
1. `modules/voice_recognition/core/speech_recognizer.py:1364` - `_is_bluetooth_device()` (статический метод)
   ```python
   def _is_bluetooth_device(name: str) -> bool:
       lowered = (name or "").lower()
       return any(keyword in lowered for keyword in ("bluetooth", "airpods", "beats", "headset", "earbud"))
   ```

2. `modules/speech_playback/core/player.py:1669` - `_is_bluetooth_device()` (метод экземпляра)
   ```python
   def _is_bluetooth_device(self, name: str) -> bool:
       lowered = name.lower()
       return any(keyword in lowered for keyword in ("bluetooth", "airpods", "airpod", "beats", "headset", "earbud"))
   ```
   ⚠️ **Отличие:** есть "airpod" (без 's')

3. `modules/audio_core/legacy_compat.py:271` - `DeviceParamsNormalizer.is_bluetooth_device()`
   ```python
   def is_bluetooth_device(self, device_name: str) -> bool:
       lowered = device_name.lower()
       return any(keyword in lowered for keyword in ("bluetooth", "airpods", "airpod", "beats", "headset", "earbud"))
   ```

4. `modules/voice_recognition/core/audio_recovery_manager.py:328` - `_is_bluetooth_device()` (функция)
   ```python
   def _is_bluetooth_device(device_name: str) -> bool:
       # Нужно проверить реализацию
   ```

**Использование:**
- `speech_recognizer.py`: 16 вызовов `_is_bluetooth_device()`
- `player.py`: 18 вызовов `_is_bluetooth_device()`
- `legacy_compat.py`: 1 вызов `is_bluetooth_device()`
- `audio_recovery_manager.py`: 2 вызова `_is_bluetooth_device()`

**Рекомендация:** Заменить все вызовы на `device_utils.is_bluetooth_device()` (опционально, для консистентности)

---

### 2. Поиск device_id по имени ⚠️ **ДУБЛИРОВАНИЕ ОСТАЛОСЬ**

**Централизованная функция:** ✅ `modules/audio_core/device_utils.py::find_device_id_by_name()`

**Дублирующиеся реализации:**
1. `modules/voice_recognition/core/speech_recognizer.py:1427` - `_find_device_id_by_name_input()`
2. `modules/voice_recognition/core/speech_recognizer.py:1858` - `_find_device_id_by_name()`
3. `modules/audio_core/core_audio_device_bus.py:303` - `_find_device_id_by_name()`
4. `modules/speech_playback/core/player.py:2603` - `_find_device_id_by_name()`
5. `modules/voice_recognition/core/audio_device_monitor.py:207` - встроенная логика в `_get_device_via_macos_api()`

**Рекомендация:** Заменить все вызовы на `device_utils.find_device_id_by_name()` (опционально)

---

### 3. Получение системного default устройства ⚠️ **ДУБЛИРОВАНИЕ ОСТАЛОСЬ**

**Централизованная функция:** ✅ `modules/audio_core/device_utils.py::get_system_default_device()`

**Дублирующиеся реализации:**
1. `modules/voice_recognition/core/speech_recognizer.py:1393` - `_get_system_default_input_name()`
2. `modules/voice_recognition/core/speech_recognizer.py:1489` - `_get_system_default_input_index()`
3. `modules/voice_recognition/core/speech_recognizer.py:1592` - `_get_system_default_input_index_fallback()`
4. `modules/speech_playback/core/player.py` - `_query_system_default_output()` (нужно проверить)
5. `modules/audio_core/core_audio_device_bus.py` - `_get_current_device_info()` (нужно проверить)
6. `modules/voice_recognition/core/audio_device_monitor.py:135` - `_get_current_input_device()`

**Рекомендация:** Заменить все вызовы на `device_utils.get_system_default_device()` (опционально)

---

### 4. Классификация устройств ⚠️ **ДУБЛИРОВАНИЕ ОСТАЛОСЬ**

**Централизованная функция:** ✅ `modules/audio_core/device_utils.py::classify_device()`

**Дублирующиеся реализации:**
1. `modules/voice_recognition/core/speech_recognizer.py` - `_classify_input_device()`
2. `modules/speech_playback/core/player.py` - `_classify_output_device()`

**Рекомендация:** Заменить все вызовы на `device_utils.classify_device()` (опционально)

---

### 5. Определение remote устройств ⚠️ **ДУБЛИРОВАНИЕ ОСТАЛОСЬ**

**Централизованная функция:** ✅ `modules/audio_core/device_utils.py::is_remote_device()`

**Дублирующиеся реализации:**
1. `modules/voice_recognition/core/speech_recognizer.py` - `_is_remote_device()`
2. `modules/speech_playback/core/player.py` - `_is_remote_device()`

**Рекомендация:** Заменить все вызовы на `device_utils.is_remote_device()` (опционально)

---

### 6. Построение StreamConfig ⚠️ **ДУБЛИРОВАНИЕ ОСТАЛОСЬ**

**Централизованная функция:** ✅ `modules/audio_core/device_utils.py::build_stream_config()`

**Дублирующиеся реализации:**
1. `modules/voice_recognition/core/speech_recognizer.py` - `_build_stream_config_for_device()`

**Рекомендация:** Заменить все вызовы на `device_utils.build_stream_config()` (опционально)

---

## 📊 Итоговая статистика

### Полностью централизовано:
- ✅ **Закрытие потоков:** 13+ мест → 2 метода

### Частично централизовано (создан модуль, но не заменены вызовы):
- ⚠️ **Определение Bluetooth:** 4+ места → 1 централизованная функция (но вызовы не заменены)
- ⚠️ **Поиск device_id:** 5+ мест → 1 централизованная функция (но вызовы не заменены)
- ⚠️ **Получение default:** 6+ мест → 1 централизованная функция (но вызовы не заменены)
- ⚠️ **Классификация:** 2 места → 1 централизованная функция (но вызовы не заменены)
- ⚠️ **Remote устройства:** 2 места → 1 централизованная функция (но вызовы не заменены)
- ⚠️ **StreamConfig:** 1 место → 1 централизованная функция (но вызовы не заменены)

---

## 🎯 Рекомендации

### Критично (уже сделано):
- ✅ Создан централизованный модуль `device_utils.py`
- ✅ Проверены блокировки на deadlocks
- ✅ Централизовано закрытие потоков

### Опционально (можно сделать постепенно):
- ⚠️ Заменить все `_is_bluetooth_device()` на `device_utils.is_bluetooth_device()`
- ⚠️ Заменить все `_find_device_id_by_name()` на `device_utils.find_device_id_by_name()`
- ⚠️ Заменить все `_get_system_default_*()` на `device_utils.get_system_default_device()`
- ⚠️ Заменить все `_classify_*_device()` на `device_utils.classify_device()`
- ⚠️ Заменить все `_is_remote_device()` на `device_utils.is_remote_device()`
- ⚠️ Заменить все `_build_stream_config_for_device()` на `device_utils.build_stream_config()`

### Важно:
- ✅ **Новые модули должны использовать `device_utils.py`** для предотвращения нового дублирования
- ✅ **Старые модули можно обновлять постепенно** при рефакторинге

---

## ✅ Выводы

1. **Критичное дублирование устранено:** закрытие потоков полностью централизовано
2. **Инфраструктура готова:** создан `device_utils.py` с централизованными функциями
3. **Осталось опциональное дублирование:** старые методы всё ещё используются, но это не критично
4. **Рекомендация:** использовать `device_utils.py` в новых модулях, старые обновлять постепенно

**Статус:** ✅ **Критичное дублирование устранено, опциональное осталось (не критично)**

