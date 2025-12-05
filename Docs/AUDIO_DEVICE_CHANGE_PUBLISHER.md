# DeviceChangePublisher - Единый монитор устройств

## Дата создания
2025-12-02

## Назначение

`DeviceChangePublisher` - единый компонент для мониторинга изменений аудио устройств INPUT и OUTPUT в системе macOS. Он обеспечивает событийную реакцию на смену устройств через Core Audio нотификации с fallback на polling.

## Архитектура

### Компоненты

**Файл:** `modules/audio_core/device_change_publisher.py`

**Ответственность:**
- Единый мониторинг INPUT и OUTPUT устройств
- Подписка на Core Audio нотификации (приоритет 1)
- Fallback на polling при недоступности Core Audio
- Публикация событий в EventBus: `device.default_input_changed` / `device.default_output_changed`
- Debounce для rapid device switch (300ms)
- Логирование источника (CoreAudio vs polling)

### Инициализация

```python
from modules.audio_core.device_change_publisher import DeviceChangePublisher

publisher = DeviceChangePublisher(event_bus)
await publisher.start_monitoring(monitor_input=True, monitor_output=True)
```

### События EventBus

**Публикует:**
- `device.default_input_changed` - смена INPUT устройства
- `device.default_output_changed` - смена OUTPUT устройства
- `device.monitoring_started` - запуск мониторинга
- `device.monitoring_stopped` - остановка мониторинга

**Формат события `device.default_*_changed`:**
```python
{
    "device_name": str,           # Имя устройства
    "device_id": Optional[int],   # PortAudio ID (None для BT)
    "is_bluetooth": bool,         # Является ли устройство Bluetooth
    "source": str,                # "core_audio" или "polling"
    "old_device_name": Optional[str],
    "old_device_id": Optional[int]
}
```

## Механизм работы

### Приоритет 1: Core Audio нотификации

При успешной инициализации `CoreAudioManager` подписывается на нотификации Core Audio:
- `kAudioHardwarePropertyDefaultInputDevice` для INPUT
- `kAudioHardwarePropertyDefaultOutputDevice` для OUTPUT

**Преимущества:**
- Мгновенная реакция на смену устройства (без задержки polling)
- Низкая нагрузка на систему (событийная модель)
- Надежность (системные нотификации macOS)

### Fallback: Polling

Если Core Audio нотификации недоступны, используется polling:
- Интервал: 1.0s для обычных устройств, 5.0s для BT устройств
- Использует `SwitchAudioSource` как единственный источник истины
- Сравнение по имени устройства (не ID)

**Когда используется:**
- Core Audio недоступен (не macOS или ошибка инициализации)
- Ошибка подписки на Core Audio нотификации

### Debounce

Для предотвращения rapid device switch используется debounce механизм:
- Задержка: 300ms
- Отменяет предыдущий таймер при новом событии
- Публикует событие только после стабилизации

## Использование в интеграциях

### VoiceRecognitionIntegration

```python
# Подписка на события INPUT устройства
await self.event_bus.subscribe(
    "device.default_input_changed",
    self._on_input_device_changed,
    EventPriority.MEDIUM
)

def _on_input_device_changed(self, event_data):
    """Обработка смены INPUT устройства"""
    device_name = event_data.get("device_name")
    device_id = event_data.get("device_id")
    is_bluetooth = event_data.get("is_bluetooth", False)
    
    # Переключение устройства в SpeechRecognizer
    if self._recognizer:
        self._recognizer.on_device_changed(device_name, device_id, is_bluetooth)
```

### SpeechPlaybackIntegration

```python
# Подписка на события OUTPUT устройства
await self.event_bus.subscribe(
    "device.default_output_changed",
    self._on_output_device_changed,
    EventPriority.MEDIUM
)

def _on_output_device_changed(self, event_data):
    """Обработка смены OUTPUT устройства"""
    device_name = event_data.get("device_name")
    device_id = event_data.get("device_id")
    is_bluetooth = event_data.get("is_bluetooth", False)
    
    # Переключение устройства в SequentialSpeechPlayer
    if self._player:
        self._player.switch_output_device(device_name, device_id, is_bluetooth)
```

## Логирование

### Уровни логирования

- **INFO**: Запуск/остановка мониторинга, смена устройств, источник события
- **DEBUG**: Детали polling цикла, debounce срабатывания
- **WARNING**: Ошибки подписки на Core Audio, fallback на polling
- **ERROR**: Критические ошибки в callback или polling цикле

### Примеры логов

```
✅ CoreAudioManager инициализирован (notifications: True)
✅ [INPUT] Core Audio нотификации активированы (событийная реакция)
✅ [OUTPUT] Core Audio нотификации активированы (событийная реакция)
🔔 [INPUT] Core Audio нотификация: default input устройство изменилось
🔔 [INPUT] Смена устройства: "Built-in Microphone" → "AirPods Pro" (source: core_audio)
```

## Интеграция в SimpleModuleCoordinator

`DeviceChangePublisherIntegration` добавляется в `SimpleModuleCoordinator` на позиции 9 (перед `voice_recognition` и `speech_playback`):

```python
def _create_integrations(self):
    # ...
    device_change_publisher = DeviceChangePublisherIntegration(
        self.event_bus,
        self.state_manager,
        self.error_handler
    )
    # ...
```

## Тестирование

См. `tests/test_device_change_publisher.py` и `tests/test_device_change_publisher_integration.py` для unit и integration тестов.

## Миграция с старого polling

**До (старый подход):**
- `AudioDeviceMonitor` в `SpeechRecognizer` (polling каждые 0.5s)
- `OutputMonitorThread` в `SequentialSpeechPlayer` (polling каждые 1.0s)
- Дублирование логики мониторинга

**После (новый подход):**
- Единый `DeviceChangePublisher` для INPUT и OUTPUT
- Core Audio нотификации (мгновенная реакция)
- Fallback на polling только при необходимости
- Централизованное логирование и debounce

## Связанные документы

- `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` - общая архитектура аудиосистемы
- `Docs/AUDIO_STREAM_MANAGER.md` - менеджер PortAudio streams
- `Docs/AUDIO_INVARIANTS.md` - invariants системы




