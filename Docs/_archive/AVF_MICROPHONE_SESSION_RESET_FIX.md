# Исправление: Сброс session_id при LONG_PRESS в режиме PROCESSING

## Дата
2025-12-11

## Проблема

Когда пользователь делает LONG_PRESS в режиме PROCESSING, микрофон активируется, но затем сразу же останавливается из-за конфликта с `playback.cancelled`.

### Последовательность событий (до исправления):

1. **LONG_PRESS** в режиме PROCESSING:
   - Публикует `playback.cancelled` с session_id старой сессии (строка 1564)
   - Публикует `voice.recording_start` с новым session_id (строка 1508)
   - Микрофон активируется с новым session_id

2. **`_on_playback_finished`** обрабатывает `playback.cancelled`:
   - Вызывает `_reset_session("playback_playback.cancelled")` (строка 640)
   - `_reset_session` сбрасывает `session_id` в `None` (строка 424)

3. **`voice.recording_stop`** приходит с новым session_id:
   - Но `active_session_id` уже `None`
   - Происходит session mismatch (строка 179)
   - Микрофон принудительно останавливается (строка 181-189)

### Результат:
- Микрофон активируется, но сразу же останавливается
- Пользователь не может говорить, так как микрофон уже закрыт

## Исправление

Добавлена проверка в `_on_playback_finished`: если микрофон активен с новой записью (`_recording_started=True`), **НЕ сбрасываем** `session_id`.

### Изменения в `integration/integrations/input_processing_integration.py`:

**Строки 613-650**: Добавлена проверка перед сбросом session_id:

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
- Микрофон активируется и остаётся активным
- Пользователь может говорить
- Микрофон останавливается только при `voice.recording_stop` с правильным session_id

## Тестирование

### Сценарий 1: LONG_PRESS в режиме PROCESSING

**Ожидаемое поведение**:
1. LONG_PRESS активирует микрофон
2. `playback.cancelled` не сбрасывает session_id (микрофон активен)
3. Микрофон остаётся активным
4. Пользователь может говорить

**Проверка в логах**:
- `⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id`
- Нет `SESSION RESET (playback_playback.cancelled)`
- Нет `⚠️ VOICE: recording_stop ignored (session mismatch)`

### Сценарий 2: Нормальная остановка воспроизведения

**Ожидаемое поведение**:
1. Воспроизведение завершается
2. `playback.completed` приходит
3. `_on_playback_finished` сбрасывает session_id (микрофон не активен)
4. Сессия очищается

**Проверка в логах**:
- `PLAYBACK: завершение воспроизведения для сессии {session_id}`
- `SESSION RESET (playback_playback.completed)`

## Файлы изменены

- `integration/integrations/input_processing_integration.py`:
  - Строки 625-631: Добавлена проверка активности микрофона перед сбросом session_id

## Статус

✅ **Исправление применено**: Проверка активности микрофона предотвращает сброс session_id при LONG_PRESS в режиме PROCESSING

---

## Связанные проблемы

- Исправление v1-v3 для залипания микрофона (см. `Docs/AVF_MICROPHONE_FIXES_COMPLETE.md`)
- Эта проблема была обнаружена при тестировании исправлений v1-v3

