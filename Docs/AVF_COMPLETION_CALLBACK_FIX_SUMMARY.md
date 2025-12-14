# Исправление Completion Callback в AVFAudioEngine

## Проблема

Completion callback для `AVAudioPlayerNode.scheduleBuffer_atTime_options_completionHandler_` не создавался через PyObjC, что приводило к тому, что событие `audio.playback.completed` не публиковалось.

## Исправления

### 1. Упрощение создания callback

**Было**: Попытка использовать `objc.ObjCBlock` (не существует в этой версии PyObjC) и `objc.callbackFor` (не работает с void (^)(void))

**Стало**: Сохранение Python функции напрямую и передача её в `scheduleBuffer` - PyObjC может автоматически преобразовать Python callable в Objective-C блок.

```python
# Попытка 1: Передать функцию напрямую (PyObjC может автоматически преобразовать)
_AVF_COMPLETION_CALLBACK = playback_completion_handler_impl
```

### 2. Улучшение fallback таймера

**Было**: Fallback таймер создавался, но не всегда запускался

**Стало**: Fallback таймер всегда запускается через event loop, если он доступен:

```python
# ✅ КРИТИЧНО: Запускаем fallback таймер через event loop
if self._ensure_loop_attached():
    self._submit_to_event_loop(_fallback_timeout(), is_async=True)
    logger.debug(f"✅ [AVF] Fallback таймер запущен через event loop")
```

### 3. Обработка ошибок при передаче callback

**Было**: Если передача функции не работала, возникала ошибка

**Стало**: Если передача функции не работает, пробуем передать `None` и полагаемся на fallback таймер:

```python
try:
    if callback_to_use is not None:
        self._player_node.scheduleBuffer_atTime_options_completionHandler_(
            audio_buffer, None, 0, callback_to_use
        )
except Exception as schedule_error:
    # Если передача функции не работает, пробуем None
    self._player_node.scheduleBuffer_atTime_options_completionHandler_(
        audio_buffer, None, 0, None
    )
```

## Текущий статус

- ✅ Completion callback инициализируется (сохраняется как Python функция)
- ✅ Fallback таймер запускается через event loop
- ⚠️ Событие `playback.completed` всё ещё не приходит в тестах

## Следующие шаги

1. **Проверить, вызывается ли callback**: Добавить логирование в `playback_completion_handler_impl` для проверки, вызывается ли он вообще
2. **Проверить fallback таймер**: Убедиться, что fallback таймер действительно срабатывает и публикует событие
3. **Проверить публикацию события**: Убедиться, что событие `audio.playback.completed` публикуется и доходит до подписчиков

## Рекомендации

1. **Использовать fallback таймер как основной механизм**: Если callback не работает, fallback таймер должен быть надёжным способом определения завершения воспроизведения
2. **Увеличить таймаут в тестах**: Fallback таймер срабатывает через `duration + 0.5` секунды, поэтому тесты должны ждать дольше
3. **Добавить больше логирования**: Для диагностики проблем с callback и fallback таймером


