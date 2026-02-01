# Исправление применено: Сброс session_id при LONG_PRESS в режиме PROCESSING

## Дата
2025-12-11

## Проблема (из логов пользователя)

Когда пользователь делает LONG_PRESS в режиме PROCESSING:
1. Микрофон активируется
2. Но затем сразу же останавливается
3. Пользователь не может говорить

### Анализ логов:

```
21:30:29,562 - LONG_PRESS: в PROCESSING режиме, прерываем текущую обработку и начинаем новую запись
21:30:29,562 - LONG_PRESS: публикуем playback.cancelled для прерывания текущей обработки
21:30:29,563 - SESSION RESET (playback_playback.cancelled)
21:30:29,564 - Session ID сброшен в state_manager (reason: playback_playback.cancelled)
21:30:29,806 - voice.recording_stop приходит с session_id=1765506626.465406
21:30:29,806 - active_session_id=None (уже сброшен!)
21:30:29,807 - ⚠️ VOICE: recording_stop ignored (session mismatch: active=None, request=1765506626.465406)
21:30:29,807 - ⚠️ VOICE: Session mismatch, но микрофон активен - принудительно останавливаем микрофон
21:30:29,908 - ✅ [Google] Google микрофон принудительно остановлен (session mismatch)
```

**Корневая причина**: `_on_playback_finished` сбрасывает `session_id` в `None` **ДО** того, как микрофон активируется с новой сессией.

## Исправление

Добавлена проверка в `_on_playback_finished`: если микрофон активен с новой записью (`_recording_started=True`), **НЕ сбрасываем** `session_id`.

### Изменения в `integration/integrations/input_processing_integration.py`:

**Строки 625-632**: Добавлена проверка перед сбросом session_id:

```python
# ✅ КРИТИЧНО: Проверяем, не активен ли микрофон с новой сессией
# Если микрофон активен и _recording_started=True, значит LONG_PRESS уже активировал новую запись
# В этом случае НЕ сбрасываем session_id, чтобы не потерять новую сессию
mic_active = self.state_manager.is_microphone_active()
if mic_active and self._recording_started:
    logger.warning(f"⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id (event={event_type}, event_session_id={event_session_id}, active={active_session_id})")
    self._notify_playback_idle()
    return
```

**Строки 37-38**: Добавлена поддержка `config=None`:

```python
def __init__(self, event_bus: EventBus, state_manager: ApplicationStateManager, 
             error_handler: ErrorHandler, config: Optional[InputProcessingConfig] = None):
```

**Строки 40-48**: Добавлена загрузка конфига из unified_config, если `config=None`:

```python
# ✅ КРИТИЧНО: Если config=None, загружаем из unified_config
if config is None:
    from config.unified_config_loader import UnifiedConfigLoader
    loader = UnifiedConfigLoader()
    unified_config = loader.load_config()
    self.config = unified_config.input_processing
else:
    self.config = config
```

## Последовательность событий (после исправления):

1. **LONG_PRESS** в режиме PROCESSING:
   - Публикует `playback.cancelled` с session_id старой сессии
   - Публикует `voice.recording_start` с новым session_id
   - Микрофон активируется с новым session_id
   - `_recording_started = True`

2. **`_on_playback_finished`** обрабатывает `playback.cancelled`:
   - Проверяет: `mic_active=True` и `_recording_started=True`
   - **НЕ вызывает** `_reset_session` (выходит раньше)
   - `session_id` остаётся установленным

3. **`voice.recording_stop`** приходит с новым session_id:
   - `active_session_id` совпадает с `request_session_id`
   - Нет session mismatch
   - Микрофон останавливается нормально

### Результат:
- ✅ Микрофон активируется и остаётся активным
- ✅ Пользователь может говорить
- ✅ Микрофон останавливается только при `voice.recording_stop` с правильным session_id

## Файлы изменены

- `integration/integrations/input_processing_integration.py`:
  - Строки 37-38: Поддержка `config=None`
  - Строки 40-48: Загрузка конфига из unified_config, если `config=None`
  - Строки 625-632: Проверка активности микрофона перед сбросом session_id

## Тестирование

Создан тест `scripts/test_long_press_in_processing_mode.py` для проверки сценария.

**Ожидаемое поведение в логах**:
- `⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id`
- Нет `SESSION RESET (playback_playback.cancelled)`
- Нет `⚠️ VOICE: recording_stop ignored (session mismatch)`

## Статус

✅ **Исправление применено**: Проверка активности микрофона предотвращает сброс session_id при LONG_PRESS в режиме PROCESSING

---

## Связанные проблемы

- Исправление v1-v3 для залипания микрофона (см. `Docs/AVF_MICROPHONE_FIXES_COMPLETE.md`)
- Эта проблема была обнаружена при анализе логов пользователя

