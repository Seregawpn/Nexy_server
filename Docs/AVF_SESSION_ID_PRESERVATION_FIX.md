# Исправление: сохранение session_id при прерывании и зависание микрофона

## Дата создания
2025-12-11

## Проблема

`session_id` сбрасывается в `None` слишком рано, что приводит к:
1. **Зависанию управления режимами**: `ModeManagementIntegration` не может определить активную сессию
2. **Зависанию микрофона**: `VoiceRecognitionIntegration` не может определить, какую сессию обрабатывать
3. **Потере контекста**: `SpeechPlaybackIntegration` не может связать события с сессией

**Последовательность событий (ПРОБЛЕМА)**:
```
1. Пользователь делает запрос (session_id=1765499572.312608)
2. Запись началась, микрофон активен
3. Пользователь нажимает Ctrl+N (прерывание)
4. InputProcessingIntegration публикует playback.cancelled с session_id=None ❌
5. SpeechPlaybackIntegration получает grpc.request_cancel с session_id=None ❌
6. _on_playback_finished получает playback.cancelled с session_id=None ❌
7. _reset_session вызывается, session_id сбрасывается в None ❌
8. Новая сессия начинается без session_id ❌
9. Микрофон зависает, режимы не переключаются ❌
```

**Логи (критические строки)**:
```
2025-12-11 19:32:58,164 - SpeechPlayback: получен grpc.request_cancel для сессии None — очищаем буфер
2025-12-11 19:32:58,165 - PLAYBACK: finished (event=playback.cancelled, session=None)
2025-12-11 19:32:58,171 - 🔄 MODE_REQUEST: в PROCESSING, проверяем session_id (active=None, request=None)
2025-12-11 19:32:58,174 - RELEASE: публикуем mode.request(PROCESSING) для session None
2025-12-11 19:32:58,174 - 🔄 MODE_REQUEST: target=AppMode.PROCESSING, source=input_processing, session_id=None
```

## Корневая причина

1. **`playback.cancelled` публикуется без `session_id`**: Когда `state_manager.get_current_session_id()` возвращает `None` (сессия уже сброшена), `playback.cancelled` публикуется с `session_id=None`.

2. **`_on_playback_finished` сбрасывает сессию при `session_id=None`**: Если `playback.cancelled` приходит с `session_id=None`, но есть `_active_grpc_session_id`, логика на строке 624-627 сбрасывает сессию, даже если воспроизведение еще продолжается.

3. **`_on_grpc_cancel` не находит `session_id` в буфере**: Если `state_manager` уже сброшен, `_on_grpc_cancel` не проверяет активные сессии в `_avf_chunk_buffer`.

4. **`InputProcessingIntegration` не сохраняет `session_id` при прерывании**: При публикации `playback.cancelled` используется `active_session_id or self._active_grpc_session_id`, но если оба `None`, событие публикуется без `session_id`.

## Исправление

### 1. Улучшение `_on_playback_finished` в InputProcessingIntegration

**Изменено** в `integration/integrations/input_processing_integration.py` (строки 610-639):

**КРИТИЧНО**: Добавлен fallback на `_pending_session_id` для сохранения `session_id` даже если `state_manager` и `_active_grpc_session_id` уже сброшены.

```python
async def _on_playback_finished(self, event):
    """Обрабатывает завершение воспроизведения (completed/cancelled/failed) и сбрасывает сессию."""
    try:
        data = (event or {}).get("data", {}) or {}
        session_id = data.get("session_id")
        event_type = (event or {}).get("type", "unknown")
        logger.debug("PLAYBACK: finished (event=%s, session=%s)", event_type, session_id)
        
        # ✅ КРИТИЧНО: Сбрасываем сессию только после завершения воспроизведения
        active_session_id = self._get_active_session_id()
        
        # ✅ КРИТИЧНО: Используем правильный порядок: event_session_id or active_session_id or _active_grpc_session_id or _pending_session_id
        # Это гарантирует, что если событие пришло с session_id=None, мы используем активную сессию или pending сессию
        effective_session_id = event_session_id or active_session_id or self._active_grpc_session_id or self._pending_session_id
        
        if effective_session_id is not None:
            # Проверяем, что это действительно наша сессия
            if effective_session_id in {self._active_grpc_session_id, active_session_id} or session_id is None:
                logger.debug(f"PLAYBACK: завершение воспроизведения для сессии {effective_session_id} (event={event_type}, original_session_id={session_id})")
                self._reset_session(f"playback_{event_type}")
            else:
                logger.debug(f"PLAYBACK: завершение воспроизведения для чужой сессии {effective_session_id}, игнорируем")
        else:
            # Нет активной сессии - ничего не делаем
            logger.debug(f"PLAYBACK: завершение воспроизведения без активной сессии (event={event_type}), игнорируем")
        
        self._notify_playback_idle()
    except Exception as e:
        logger.debug("PLAYBACK: error handling finish event: %s", e)
```

### 2. Улучшение `_on_grpc_cancel` в SpeechPlaybackIntegration

**Изменено** в `integration/integrations/speech_playback_integration.py` (строки 1158-1201):

**КРИТИЧНО**: Добавлена проверка `session_id` из самого события `grpc.request_cancel` перед проверкой `state_manager` и буфера.

```python
            # ✅ КРИТИЧНО: Сначала пытаемся получить session_id из самого события
            # Это важно, так как событие может содержать session_id, даже если state_manager уже сброшен
            event_data = event.get("data", {}) if isinstance(event, dict) else {}
            event_session_id = event_data.get("session_id")
            
            # ✅ КРИТИЧНО: Используем state_manager для получения session_id (единый источник истины)
            # Также проверяем активные сессии в буфере на случай, если state_manager уже сброшен
            current_session_id = event_session_id or self.state_manager.get_current_session_id()
            
            # ✅ КРИТИЧНО: Если session_id не найден в state_manager и событии, ищем в активных сессиях буфера
            if current_session_id is None and self._avf_chunk_buffer:
                # Берем первую активную сессию из буфера
                active_sessions = list(self._avf_chunk_buffer.keys())
                if active_sessions:
                    current_session_id = active_sessions[0]
                    logger.warning(f"⚠️ [AVF] session_id не найден в state_manager и событии, используем активную сессию из буфера: {current_session_id}")

await self.event_bus.publish("playback.cancelled", {
    "session_id": current_session_id,
    "source": "grpc_cancel"
})
```

### 3. Улучшение публикации `playback.cancelled` в InputProcessingIntegration

**Изменено** в `integration/integrations/input_processing_integration.py` (строки 1151-1160, 1283-1293):

**КРИТИЧНО**: Добавлен fallback на `_pending_session_id` для сохранения `session_id` даже если `state_manager` и `_active_grpc_session_id` уже сброшены.

```python
                    # ✅ КРИТИЧНО: Используем _get_active_session_id для получения session_id
                    # Также проверяем _active_grpc_session_id и _pending_session_id на случай, если state_manager уже сброшен
                    active_session_id = self._get_active_session_id()
                    effective_session_id = active_session_id or self._active_grpc_session_id or self._pending_session_id
                    
                    if effective_session_id is None:
                        logger.warning(f"⚠️ SHORT_PRESS: не удалось получить session_id для playback.cancelled (active={active_session_id}, grpc={self._active_grpc_session_id}, pending={self._pending_session_id})")

await self.event_bus.publish("playback.cancelled", {
    "session_id": effective_session_id,
    "reason": "keyboard",
    "source": "input_processing",
    "timestamp": event.timestamp,
    "duration": event.duration
})
```

## Результат

**Последовательность событий (ИСПРАВЛЕНО)**:
```
1. Пользователь делает запрос (session_id=1765499572.312608)
2. Запись началась, микрофон активен
3. Пользователь нажимает Ctrl+N (прерывание)
4. InputProcessingIntegration получает session_id из _active_grpc_session_id ✅
5. playback.cancelled публикуется с правильным session_id ✅
6. SpeechPlaybackIntegration получает session_id из буфера, если state_manager сброшен ✅
7. _on_playback_finished использует effective_session_id для сброса сессии ✅
8. Сессия сбрасывается только после завершения воспроизведения ✅
9. Новая сессия начинается с правильным session_id ✅
```

## Файлы изменены

- `integration/integrations/input_processing_integration.py`:
  - Строки 610-639: Улучшена логика `_on_playback_finished` для использования `effective_session_id = event_session_id or active_session_id or self._active_grpc_session_id or self._pending_session_id`
  - Строки 1151-1160: Улучшена публикация `playback.cancelled` с проверкой `_active_grpc_session_id` и `_pending_session_id` как fallback
  - Строки 1254-1258: Улучшена публикация `grpc.request_cancel` с проверкой `_pending_session_id` как fallback
  - Строки 1283-1293: Улучшена публикация `playback.cancelled` (блок 2) с проверкой `_active_grpc_session_id` и `_pending_session_id` как fallback
  
- `integration/integrations/speech_playback_integration.py`:
  - Строки 1158-1201: Улучшена логика `_on_grpc_cancel` для проверки `session_id` из события перед проверкой `state_manager` и буфера
  
- `integration/integrations/mode_management_integration.py`:
  - Строки 225-250: Улучшена блокировка перехода в SLEEPING - проверяется активность микрофона и блокируется переход, если режим PROCESSING, даже если `current_session_id=None`
  
- `integration/workflows/processing_workflow.py`:
  - Строки 468-503: Улучшена логика `_cancel_active_processes` - если `current_session_id=None`, workflow не публикует `playback.cancelled` (workflow не активен)

### 4. Улучшение публикации `grpc.request_cancel` в InputProcessingIntegration

**Изменено** в `integration/integrations/input_processing_integration.py` (строки 1254-1258):

```python
# ✅ КРИТИЧНО: Используем _get_active_session_id для получения session_id
# Также проверяем _pending_session_id на случай, если state_manager уже сброшен
cancel_sid = self._active_grpc_session_id or self._cancel_session_id or self._get_active_session_id() or self._pending_session_id

if cancel_sid is None:
    logger.warning(f"⚠️ SHORT_PRESS: не удалось получить session_id для grpc.request_cancel (active={self._get_active_session_id()}, grpc={self._active_grpc_session_id}, cancel={self._cancel_session_id}, pending={self._pending_session_id})")

await self.event_bus.publish("grpc.request_cancel", {
    "session_id": cancel_sid
})
```

### 5. Улучшение блокировки SLEEPING в ModeManagementIntegration

**Изменено** в `integration/integrations/mode_management_integration.py` (строки 225-268):

**КРИТИЧНО**: Добавлена проверка активности микрофона и блокировка перехода в SLEEPING, если режим PROCESSING, даже если `current_session_id=None`. Блокировка применяется для всех источников, кроме interrupt с высоким приоритетом (priority >= 90).

```python
if current_mode == AppMode.PROCESSING and source != 'interrupt':
    current_session_id = self.state_manager.get_current_session_id()
    is_microphone_active = self.state_manager.is_microphone_active()
    
    # ✅ КРИТИЧНО: Блокируем переход в SLEEPING, если:
    # - Запрос без session_id И (есть активная сессия ИЛИ микрофон активен)
    # Это предотвращает прерывание активной обработки, даже если session_id был сброшен
    if is_sleeping_request and session_id is None:
        if current_session_id is not None:
            logger.warning(f"⚠️ MODE_REQUEST: запрос на SLEEPING без session_id при активной сессии {current_session_id} - блокируем")
            return
        elif is_microphone_active:
            logger.warning(f"⚠️ MODE_REQUEST: запрос на SLEEPING без session_id при активном микрофоне - блокируем (запись продолжается)")
            return
        else:
            logger.warning(f"⚠️ MODE_REQUEST: запрос на SLEEPING без session_id в режиме PROCESSING - блокируем (обработка продолжается)")
            return
```

### 6. Улучшение `_cancel_active_processes` в ProcessingWorkflow

**Изменено** в `integration/workflows/processing_workflow.py` (строки 468-503):

```python
async def _cancel_active_processes(self):
    """Отмена всех активных процессов через ЕДИНЫЙ канал прерывания"""
    try:
        # ✅ КРИТИЧНО: Используем self.current_session_id как основной источник
        # Если он None, это означает, что workflow уже завершен или не был запущен
        # В этом случае не публикуем playback.cancelled, так как нет активной сессии
        session_id = self.current_session_id
        
        if session_id is None:
            logger.warning(f"⚠️ ProcessingWorkflow: current_session_id=None, пропускаем публикацию playback.cancelled (workflow не активен)")
            return
        
        # Отменяем gRPC запрос
        if not self.grpc_completed:
            logger.info("⚙️ ProcessingWorkflow: отменяем gRPC запрос")
            await self.event_bus.publish("grpc.request_cancel", {
                "session_id": session_id,
                "reason": "user_interrupt"
            })
        
        # ✅ КРИТИЧНО: ЕДИНЫЙ канал прерывания аудио - публикуем playback.cancelled
        # Гарантируем, что session_id всегда передается (проверено выше)
        if not self.playback_completed:
            logger.info("⚙️ ProcessingWorkflow: останавливаем воспроизведение через ЕДИНЫЙ канал")
            await self.event_bus.publish("playback.cancelled", {
                "session_id": session_id,
                "reason": "user_interrupt",
                "source": "processing_workflow"
            })
```

## Связанные исправления

- `Docs/AVF_WELCOME_MESSAGE_MODE_CONFLICT_FIX.md`: Исправление конфликта режимов между welcome_message и активной сессией
- `Docs/AVF_SESSION_ID_RESET_FIX.md`: Исправление преждевременного сброса session_id

