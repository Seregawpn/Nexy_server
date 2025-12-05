# Audio System Invariants

## Дата создания
2025-12-02

## Назначение

Документ описывает invariants (инварианты) аудиосистемы Nexy - условия, которые всегда должны выполняться для корректной работы системы.

## INPUT Invariants

### INV-INPUT-001: Не перезапускает stream при LISTENING

**Условие:** INPUT не перезапускает stream, если `state == LISTENING`.

**Обоснование:** Перезапуск stream во время активного прослушивания приведет к потере аудио данных и нарушению пользовательского опыта.

**Проверка:**
```python
if self.state == RecognitionState.LISTENING:
    logger.warning("⚠️ [INPUT] Попытка перезапуска stream во время LISTENING - игнорируется")
    return
```

**Нарушение:** Если stream перезапускается во время LISTENING, это критическая ошибка.

### INV-INPUT-002: Всегда использует системный default

**Условие:** INPUT всегда использует системный default устройство через `SwitchAudioSource`.

**Обоснование:** `SwitchAudioSource` - единственный источник истины для определения default устройства в macOS. Использование PortAudio ID напрямую может привести к несоответствию с системными настройками.

**Проверка:**
```python
device_name = self._get_device_name_via_macos_api("input")
device_id = self._find_device_id_by_name(device_name, device_type="input")
```

**Нарушение:** Если используется PortAudio ID без проверки через `SwitchAudioSource`, это ошибка.

### INV-INPUT-003: Пересоздает stream только при IDLE или PENDING

**Условие:** INPUT пересоздает stream только при `state == IDLE` или `state == PENDING`.

**Обоснование:** Пересоздание stream в других состояниях может привести к потере данных или нарушению состояния.

**Проверка:**
```python
if self.state not in [RecognitionState.IDLE, RecognitionState.PENDING]:
    logger.warning(f"⚠️ [INPUT] Попытка пересоздания stream в состоянии {self.state} - игнорируется")
    return
```

**Нарушение:** Если stream пересоздается в других состояниях, это ошибка.

## OUTPUT Invariants

### INV-OUTPUT-001: Всегда закрывает старый stream перед созданием нового

**Условие:** OUTPUT всегда закрывает старый stream перед созданием нового.

**Обоснование:** Одновременное существование двух потоков для одного устройства может привести к конфликтам ресурсов и ошибкам PortAudio (-9986, -10851).

**Проверка:**
```python
# В AudioStreamManager.close_stream
if old_stream:
    await self.close_stream(old_stream, is_bluetooth)
    # Только после успешного закрытия создаем новый
result = await self.create_stream(new_config)
```

**Нарушение:** Если новый stream создается до закрытия старого, это критическая ошибка.

### INV-OUTPUT-002: Всегда использует системный default

**Условие:** OUTPUT всегда использует системный default устройство через `SwitchAudioSource`.

**Обоснование:** Аналогично INV-INPUT-002.

**Проверка:**
```python
device_name = self._get_output_device_name_via_macos_api()
device_id = self._find_device_id_by_name(device_name, device_type="output")
```

**Нарушение:** Если используется PortAudio ID без проверки через `SwitchAudioSource`, это ошибка.

### INV-OUTPUT-003: Для BT устройств использует device=None

**Условие:** OUTPUT для BT устройств использует `device=None` (не ищет ID в PortAudio).

**Обоснование:** BT устройства часто не видны в PortAudio сразу или имеют нестабильные ID. Использование `device=None` позволяет macOS управлять параметрами устройства автоматически.

**Проверка:**
```python
if is_bluetooth:
    device_id = None  # macOS управляет параметрами
else:
    device_id = self._find_device_id_by_name(device_name, device_type="output")
```

**Нарушение:** Если для BT устройства используется PortAudio ID, это может привести к ошибкам.

## Общие Invariants

### INV-COMMON-001: Все операции с streams защищены lock

**Условие:** Все операции с streams защищены lock (`threading.RLock`).

**Обоснование:** Защита от race conditions при concurrent доступе к streams из разных потоков.

**Проверка:**
```python
with self._lock:
    # Операции со stream
    stream = self._current_stream
    # ...
```

**Нарушение:** Если операции со stream выполняются без lock, это может привести к race conditions.

### INV-COMMON-002: Все ошибки -9986/-10851 обрабатываются с retry

**Условие:** Все ошибки PortAudio -9986 (Internal PortAudio error) и -10851 (Invalid Property Value) обрабатываются с retry логикой.

**Обоснование:** Эти ошибки часто временные и могут быть решены повторной попыткой с задержкой или изменением конфигурации.

**Проверка:**
```python
# В AudioStreamManager.create_stream
try:
    stream = sd.InputStream(...)
except sd.PortAudioError as e:
    if e.args[0] in [-9986, -10851]:
        # Retry с задержкой или безопасной конфигурацией
        await self._retry_with_safe_config(config, e.args[0])
```

**Нарушение:** Если ошибки -9986/-10851 не обрабатываются с retry, это может привести к нестабильности.

### INV-COMMON-003: Все device changes публикуются через DeviceChangePublisher

**Условие:** Все изменения устройств публикуются через `DeviceChangePublisher`, а не напрямую из компонентов.

**Обоснование:** Централизация мониторинга устройств обеспечивает единообразие, debounce и логирование.

**Проверка:**
```python
# В VoiceRecognitionIntegration и SpeechPlaybackIntegration
await self.event_bus.subscribe(
    "device.default_input_changed",
    self._on_input_device_changed,
    EventPriority.MEDIUM
)
```

**Нарушение:** Если компоненты мониторят устройства напрямую (polling), это нарушает архитектуру.

## Проверка Invariants

### Unit тесты

Invariants проверяются в unit тестах:
- `tests/test_audio_stream_manager.py` - проверка INV-COMMON-001, INV-COMMON-002
- `tests/test_device_change_publisher.py` - проверка INV-COMMON-003
- `tests/test_speech_recognizer_integration.py` - проверка INV-INPUT-001, INV-INPUT-002, INV-INPUT-003
- `tests/test_sequential_speech_player_integration.py` - проверка INV-OUTPUT-001, INV-OUTPUT-002, INV-OUTPUT-003

### Runtime проверки

В production коде добавлены runtime проверки с логированием предупреждений при нарушении invariants.

### Мониторинг

Метрики для мониторинга нарушений invariants:
- `stream_restart_during_listening` - количество попыток перезапуска stream во время LISTENING
- `stream_create_without_close` - количество попыток создания stream без закрытия старого
- `device_change_not_published` - количество изменений устройств, не опубликованных через DeviceChangePublisher

## Связанные документы

- `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` - общая архитектура аудиосистемы
- `Docs/AUDIO_DEVICE_CHANGE_PUBLISHER.md` - монитор устройств
- `Docs/AUDIO_STREAM_MANAGER.md` - менеджер PortAudio streams




