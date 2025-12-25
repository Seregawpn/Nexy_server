# Критические баги A и B исправлены

**Дата**: 2025-12-23  
**Статус**: ✅ Все критические баги исправлены

---

## ✅ Исправление A: `_play_test_sound_worker` использует неправильный `startAndReturnError_`

**Проблема**: В `_play_test_sound_worker` остался старый код с неправильным вызовом `startAndReturnError_`.

**Исправление**:
- Заменен `error = None; if not self.output_playback.engine.startAndReturnError_(error):` 
- На `if not self.output_playback._engine_start():`
- Используется helper метод из `OutputPlaybackPrototype`

**Файл**: `mvp12_full_input_output/test_full_input_output.py` (строка ~956)

---

## ✅ Исправление B: Signature логика может давать ложные срабатывания

**Проблема**: Сравнение signature использовало смешанные данные (`last_input_device_uid` + `current_input_device_data`), что могло давать дребезг при device storm.

**Исправление**:
1. **Добавлены отдельные переменные для подписей**:
   - `self.last_input_signature: Optional[tuple] = None` в `__init__`
   - `self.last_output_signature: Optional[tuple] = None` в `__init__`

2. **Установка начальных подписей** в `_get_initial_devices()`:
   ```python
   self.last_input_signature = (
       self.current_input_device_data["uid"],
       self.current_input_device_data["name"],
       self.current_input_device_data["sample_rate"],
       self.current_input_device_data["max_input_channels"],
   )
   self.last_output_signature = (
       self.current_output_device_data["uid"],
       self.current_output_device_data["name"],
       self.current_output_device_data["sample_rate"],
       self.current_output_device_data["max_output_channels"],
   )
   ```

3. **Обновление подписей** в `_monitor_devices()` после успешного переключения:
   ```python
   if self._switch_input_device(current_input):
       self.current_input_device_data = current_input
       self.last_input_device_uid = current_input['uid']
       self.last_input_signature = current_signature  # Обновляем подпись
   ```

4. **Сравнение только с сохраненной подписью**:
   ```python
   current_signature = (...)
   if self.last_input_signature != current_signature:
       # Переключение
   ```

**Результат**: Детерминированное сравнение, избегает дребезга при device storm.

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

---

## ✅ Проверка C: `_engine_start()` корректный в MVP-6

**Проверено**: `_engine_start()` в `mvp6_output_playback/test_output_playback.py` использует правильный PyObjC паттерн:
```python
ok, err = self.engine.startAndReturnError_(None)
if not ok:
    logger.error(f"AVAudioEngine start failed: {err}")
return bool(ok)
```

**Статус**: ✅ Корректный

---

## ✅ Улучшение D: Комментарий про output switching

**Добавлено**: В `_switch_output_device()` добавлен комментарий и логирование:
- Комментарий про "follow-system-default" режим
- Логирование режима при переключении: `"ℹ️  Режим: follow-system-default + engine recreate"`

**Файл**: `mvp12_full_input_output/test_full_input_output.py`

---

## 📊 Итоговый статус

- ✅ Баг A исправлен
- ✅ Баг B исправлен (критично для стабильности)
- ✅ Проверка C пройдена
- ✅ Улучшение D добавлено
- ✅ Ошибок линтера нет

**Готово к тестированию** 🎯

