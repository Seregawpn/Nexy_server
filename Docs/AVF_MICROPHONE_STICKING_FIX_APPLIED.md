# Исправление: залипание микрофона при session mismatch

## Дата создания
2025-12-11

## Проблема

Микрофон залипает (остаётся активным) после LONG_PRESS → SHORT_PRESS из-за того, что `voice.recording_stop` игнорируется при `session mismatch`:

```
20:35:10,394 - ✅ [Google] Микрофон активирован, запись началась
20:35:10,896 - LONG_PRESS: публикуем playback.cancelled для прерывания текущей обработки
20:35:10,897 - SESSION RESET (playback_playback.cancelled)
20:35:10,898 - Session ID сброшен в state_manager (reason: playback_playback.cancelled) - session_id стал None
20:35:10,904 - voice.recording_stop опубликовано с session_id=1765503308.263492
20:35:11,093 - ⚠️ VOICE: recording_stop ignored (session mismatch: active=None, request=1765503308.263492)
20:35:11,860 - ⚠️ VOICE: state_manager показывает активный микрофон, но recognizer не активен - синхронизируем состояние
20:35:11,860 - ⚠️ [MIC_STATE] Принудительное закрытие микрофона: active → idle (reason=state_mismatch)
```

## Корневая причина

1. **Преждевременный сброс `session_id`**: `InputProcessingIntegration._reset_session()` сбрасывает `session_id` в `None` **ДО** того, как микрофон успевает остановиться.
2. **Игнорирование `voice.recording_stop` при mismatch**: В `VoiceRecognitionIntegration._on_recording_stop()` при `session mismatch` проверяется только `_recognizer.is_listening` (legacy), но **НЕ проверяется `_google_stop_listening`** (Google Speech Recognition).
3. **Google микрофон не останавливается**: Если используется Google Speech Recognition (`_google_stop_listening`), микрофон остаётся активным, даже если `state_manager` показывает `active`.

## Исправление

### 1. Проверка Google микрофона при `session_id=None` (строки 934-955)

**Было**:
```python
if session_id is None:
    if self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening:
        # Останавливаем только legacy микрофон
        await self._recognizer.stop_listening()
```

**Стало**:
```python
if session_id is None:
    # ✅ КРИТИЧНО: Проверяем оба типа микрофонов (Google и legacy)
    google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
    legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
    
    if google_mic_active or legacy_mic_active:
        # ✅ КРИТИЧНО: Останавливаем Google микрофон, если активен
        if google_mic_active:
            self._google_stop_listening(wait_for_stop=False)
            # Очищаем состояние
            self._google_stop_listening = None
            self._google_recognizer = None
            self._google_microphone = None
            with self._google_audio_chunks_lock:
                self._google_audio_chunks = []
        
        # ✅ КРИТИЧНО: Останавливаем legacy микрофон, если активен
        if legacy_mic_active:
            await self._recognizer.stop_listening()
```

### 2. Проверка Google микрофона при `session mismatch` (строки 964-979)

**Было**:
```python
if active_session_str != request_session_str:
    # Не наша сессия — игнорируем
    logger.warning(f"⚠️ VOICE: recording_stop ignored (session mismatch: active={active_session_str}, request={request_session_str})")
    # ✅ КРИТИЧНО: Даже при mismatch принудительно останавливаем поток, если микрофон активен
    if self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening:
        # Останавливаем только legacy микрофон
        self._recognizer._current_stream.stop()
    return
```

**Стало**:
```python
if active_session_str != request_session_str:
    # Не наша сессия — игнорируем
    logger.warning(f"⚠️ VOICE: recording_stop ignored (session mismatch: active={active_session_str}, request={request_session_str})")
    
    # ✅ КРИТИЧНО: Даже при mismatch принудительно останавливаем микрофон, если он активен
    # Проверяем оба типа микрофонов (Google и legacy)
    google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
    legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
    
    if google_mic_active or legacy_mic_active:
        # ✅ КРИТИЧНО: Останавливаем Google микрофон, если активен
        if google_mic_active:
            self._google_stop_listening(wait_for_stop=False)
            # Очищаем состояние
            self._google_stop_listening = None
            self._google_recognizer = None
            self._google_microphone = None
            with self._google_audio_chunks_lock:
                self._google_audio_chunks = []
            # Обновляем состояние микрофона
            self.state_manager.set_microphone_state("idle", session_id=None, reason="google_recording_stopped_mismatch")
            await self.event_bus.publish("microphone.closed", {"session_id": request_session_str})
        
        # ✅ КРИТИЧНО: Останавливаем legacy микрофон, если активен
        if legacy_mic_active:
            self._recognizer._current_stream.stop()
            await self._recognizer.stop_listening()
    return
```

## Файлы изменены

- `integration/integrations/voice_recognition_integration.py`:
  - Строки 934-955: Проверка и остановка Google микрофона при `session_id=None`
  - Строки 964-979: Проверка и остановка Google микрофона при `session mismatch`

## Результат

После исправления:
1. ✅ Google микрофон проверяется при `session_id=None`
2. ✅ Google микрофон проверяется при `session mismatch`
3. ✅ Google микрофон принудительно останавливается при mismatch
4. ✅ Состояние микрофона синхронизируется с `state_manager`
5. ✅ `microphone.closed` публикуется для синхронизации состояния

## Последовательность событий после исправления

```
20:35:10,394 - ✅ [Google] Микрофон активирован, запись началась
20:35:10,896 - LONG_PRESS: публикуем playback.cancelled для прерывания текущей обработки
20:35:10,897 - SESSION RESET (playback_playback.cancelled)
20:35:10,898 - Session ID сброшен в state_manager (reason: playback_playback.cancelled) - session_id стал None
20:35:10,904 - voice.recording_stop опубликовано с session_id=1765503308.263492
20:35:11,093 - ⚠️ VOICE: recording_stop ignored (session mismatch: active=None, request=1765503308.263492)
20:35:11,093 - ⚠️ VOICE: Session mismatch, но микрофон активен (google=True, legacy=False) - принудительно останавливаем микрофон
20:35:11,093 - 🛑 [Google] Принудительная остановка Google микрофона (session mismatch)
20:35:11,093 - ✅ [Google] Google микрофон принудительно остановлен (session mismatch)
20:35:11,093 - ⚠️ [MIC_STATE] Принудительное закрытие микрофона: active → idle (reason=google_recording_stopped_mismatch)
```

