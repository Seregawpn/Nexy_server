# Почему callback не передавался - анализ ошибки

**Дата:** 2025-12-02

## Проблема

При рефакторинге для использования `AudioStreamManager` callback `_audio_callback` не передавался в `StreamConfig`, хотя должен был.

## Цепочка вызовов (ПРАВИЛЬНАЯ)

```
1. _start_audio_stream()
   └─> Вызывает _get_stream_config()
       └─> Вызывает _stream_config_resolver.resolve_stream_config(
               callback=self._audio_callback  ✅ ПРАВИЛЬНО передается
           )
       └─> Возвращает dict: {
               'device': None,
               'channels': 1,
               'callback': self._audio_callback  ✅ Callback ЕСТЬ в dict
           }

2. _start_audio_stream() продолжает
   └─> Создает StreamConfig(
           callback=stream_config.get('callback')  ✅ ДОЛЖНО брать из dict
       )
   
3. AudioStreamManager.create_stream(stream_config_obj)
   └─> Передает callback в sd.OutputStream(callback=config.callback)  ✅
```

## Что было на самом деле (ОШИБКА)

```
1. _start_audio_stream()
   └─> Вызывает _get_stream_config()
       └─> Возвращает dict с callback=self._audio_callback  ✅

2. _start_audio_stream() продолжает
   └─> Создает StreamConfig(
           callback=None  ❌ ИГНОРИРУЕТ callback из dict!
       )
   
3. AudioStreamManager.create_stream(stream_config_obj)
   └─> Передает callback=None в sd.OutputStream  ❌
```

## Почему это произошло?

### Вероятная причина 1: Неправильное понимание архитектуры

Разработчик мог подумать:
- "Callback устанавливается где-то в AudioStreamManager автоматически"
- "Callback не нужен в StreamConfig, он устанавливается позже"
- "PortAudio сам найдет callback"

**Реальность:** PortAudio (`sd.OutputStream`) **требует** callback при создании потока. Без callback поток создается, но не знает, откуда брать данные.

### Вероятная причина 2: Комментарий вводил в заблуждение

Возможно, был комментарий типа:
```python
callback=None,  # Callback устанавливается в _audio_callback через sd.OutputStream
```

Этот комментарий **неправильный** - он предполагает, что callback устанавливается автоматически, но на самом деле его нужно **передать** при создании потока.

### Вероятная причина 3: Рефакторинг без полного понимания

При переходе на `AudioStreamManager`:
- Старый код мог устанавливать callback напрямую в `sd.OutputStream`
- Новый код должен передавать callback через `StreamConfig`
- Разработчик не заметил, что callback нужно брать из `stream_config.get('callback')`

## Почему это не было обнаружено сразу?

1. **Поток создавался успешно** - `sd.OutputStream()` не падает, если callback=None
2. **Поток стартовал успешно** - `stream.start()` работает без callback
3. **Данные добавлялись в буфер** - `chunk_buffer.add_chunk()` работает независимо
4. **Нет ошибок в логах** - PortAudio просто не вызывает callback, но не выдает ошибку

**Единственный признак проблемы:** Аудио не воспроизводится, но это обнаруживается только при тестировании.

## Как это должно было быть реализовано?

### Правильный паттерн:

```python
# 1. Получаем конфигурацию с callback
stream_config = self._get_stream_config(...)  # Возвращает dict с 'callback'

# 2. Создаем StreamConfig, БЕРЕМ callback из dict
stream_config_obj = StreamConfig(
    ...
    callback=stream_config.get('callback'),  # ✅ Берем из dict
    ...
)

# 3. AudioStreamManager передает callback в PortAudio
sd.OutputStream(callback=config.callback)  # ✅ Callback передается
```

### Неправильный паттерн (что было):

```python
# 1. Получаем конфигурацию с callback
stream_config = self._get_stream_config(...)  # Возвращает dict с 'callback'

# 2. Создаем StreamConfig, ИГНОРИРУЕМ callback из dict
stream_config_obj = StreamConfig(
    ...
    callback=None,  # ❌ Игнорируем callback из dict
    ...
)

# 3. AudioStreamManager передает callback=None в PortAudio
sd.OutputStream(callback=None)  # ❌ Callback не передается
```

## Уроки

1. **Всегда проверяйте передачу callback** при создании PortAudio потоков
2. **Не полагайтесь на комментарии** - проверяйте фактическое поведение
3. **Тестируйте воспроизведение** после рефакторинга, а не только создание потока
4. **Логируйте вызовы callback** для диагностики (первые N вызовов)
5. **Поток может создаться успешно**, но не работать без callback

## Как предотвратить в будущем?

1. **Добавить проверку** в `AudioStreamManager.create_stream()`:
   ```python
   if config.callback is None and stream_type == "output":
       logger.warning("⚠️ OUTPUT stream создается без callback - воспроизведение не будет работать!")
   ```

2. **Добавить тест** на наличие callback в StreamConfig для OUTPUT потоков

3. **Документировать требование** callback для OUTPUT потоков в StreamConfig

