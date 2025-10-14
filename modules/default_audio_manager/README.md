# DefaultAudioManager

Модуль управления аудио через системные дефолты macOS.

## Концепция

Вместо сложной логики переключения аудио устройств, этот модуль использует системные дефолты macOS. Приложение просто следует настройкам пользователя в системе.

## Преимущества

- **Простота**: Нет сложной логики переключения устройств
- **Надежность**: Следует системным настройкам macOS
- **Совместимость**: Работает с любыми устройствами, поддерживаемыми macOS
- **Производительность**: Минимальные накладные расходы
- **Пользовательский контроль**: Пользователь сам выбирает устройства в системе

## Архитектура

```
DefaultAudioManager
├── DefaultAudioManager (основной класс)
├── HealthChecker (проверка здоровья микрофона)
├── DefaultAudioConfig (конфигурация)
└── Types (типы данных)
```

## Основные компоненты

### DefaultAudioManager

Основной класс, управляющий аудио потоками:

- Запуск/остановка потоков с `device=None`
- Мониторинг здоровья микрофона
- Автоматическое переоткрытие при ошибках
- Callback система для событий

### HealthChecker

Проверка здоровья микрофона через RMS анализ:

- Анализ RMS значений
- Определение статуса (HEALTHY/SILENT/ERROR)
- Настраиваемые пороги
- Callback уведомления

### DefaultAudioConfig

Конфигурация модуля:

- Параметры аудио (sample rate, channels, dtype)
- Настройки health check
- Обработка ошибок
- Логирование

## Использование

### Базовое использование

```python
from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig

# Создание конфигурации
config = DefaultAudioConfig()

# Создание менеджера
manager = DefaultAudioManager(config)

# Запуск
await manager.start()

# Проверка здоровья
is_healthy = manager.is_healthy()

# Остановка
await manager.stop()
```

### С конфигурацией

```python
from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig

# Кастомная конфигурация
config = DefaultAudioConfig(
    input_sample_rate=24000,
    health_check_interval=2.0,
    auto_reopen_on_error=True
)

manager = DefaultAudioManager(config)
```

### Async context manager

```python
async with DefaultAudioManager(config) as manager:
    # Работа с аудио
    audio_data = manager.get_audio_data()
    is_healthy = manager.is_healthy()
```

## Конфигурация

### unified_config.yaml

```yaml
default_audio:
  input_sample_rate: 16000
  output_sample_rate: 48000
  input_channels: 1
  output_channels: 1
  dtype: "int16"
  chunk_size: 1024
  
  health_check_interval: 1.0
  health_check_duration: 0.3
  rms_threshold: 1e-4
  silent_threshold: 1e-6
  
  auto_reopen_on_error: true
  max_retry_attempts: 3
  retry_delay: 0.5
  error_cooldown: 2.0
  
  enable_debug_logging: false
  log_health_checks: true
  log_stream_events: true
```

## События

### StreamStateCallback

```python
def on_state_change(state: AudioStreamState):
    print(f"Состояние потока: {state.value}")

config.on_stream_state_change = on_state_change
```

### HealthStatusCallback

```python
def on_health_change(status: HealthStatus):
    print(f"Статус здоровья: {status.value}")

config.on_health_status_change = on_health_change
```

### ErrorCallback

```python
def on_error(error: StreamError):
    print(f"Ошибка: {error.error_message}")

config.on_error = on_error
```

### MetricsCallback

```python
def on_metrics(metrics: AudioMetrics):
    print(f"RMS: {metrics.rms_value:.6f}")

config.on_metrics_update = on_metrics
```

## Состояния

### AudioStreamState

- `STOPPED` - Потоки остановлены
- `STARTING` - Запуск потоков
- `RUNNING` - Потоки работают
- `STOPPING` - Остановка потоков
- `ERROR` - Ошибка в потоках

### HealthStatus

- `UNKNOWN` - Статус неизвестен
- `HEALTHY` - Микрофон работает
- `SILENT` - Микрофон тихий
- `ERROR` - Ошибка микрофона

## Метрики

### AudioMetrics

- `rms_value` - RMS значение
- `peak_value` - Пиковое значение
- `sample_count` - Количество сэмплов
- `error_count` - Количество ошибок
- `last_health_check` - Время последней проверки
- `stream_uptime` - Время работы потока

## Обработка ошибок

### Автоматическое переоткрытие

При включенном `auto_reopen_on_error` модуль автоматически переоткрывает потоки при ошибках.

### Retry логика

- `max_retry_attempts` - Максимальное количество попыток
- `retry_delay` - Задержка между попытками
- `error_cooldown` - Пауза после ошибки

## Логирование

### Уровни логирования

- `enable_debug_logging` - Включить отладочные логи
- `log_health_checks` - Логировать проверки здоровья
- `log_stream_events` - Логировать события потоков

### Примеры логов

```
✅ [AUDIO] Аудио потоки запущены успешно
🏥 [HEALTH] Статус изменился: healthy
📊 [METRICS] RMS: 0.004503, Peak: 0.012345
🔄 [STATE] Состояние изменилось: running
```

## Интеграция

### С EventBus

```python
from integration.integrations.default_audio_integration import DefaultAudioIntegration

integration = DefaultAudioIntegration(event_bus, state_manager, error_handler)
await integration.start()
```

### С SpeechRecognizer

```python
# SpeechRecognizer использует device=None
stream = sd.InputStream(
    device=None,  # Системный дефолт
    samplerate=16000,
    channels=1,
    dtype="int16"
)
```

## Тестирование

### Базовые тесты

```bash
python3 quick_default_test.py
```

### Полное тестирование

```bash
python3 test_default_audio_scenarios.py
```

### Интеграционные тесты

```bash
python3 test_default_audio_integration.py
```

## Миграция с AudioDeviceManager

### Что изменить

1. Заменить `AudioDeviceIntegration` на `DefaultAudioIntegration`
2. Убрать `device_index` из `SpeechRecognizer`
3. Обновить конфигурацию в `unified_config.yaml`
4. Удалить старый модуль `audio_device_manager`

### Что сохранить

1. EventBus систему
2. ApplicationStateManager
3. ErrorHandler
4. Основную архитектуру приложения

## Troubleshooting

### Микрофон не работает

1. Проверить разрешения в System Settings → Privacy & Security → Microphone
2. Проверить настройки в System Settings → Sound → Input
3. Проверить подключение устройств

### AirPods не работают

1. Убедиться, что AirPods выбраны и во Input, и в Output
2. Подождать 0.5-1 секунду для активации HFP
3. Проверить Bluetooth подключение

### Ошибки потоков

1. Проверить, что нет других приложений, использующих микрофон
2. Перезапустить приложение
3. Проверить системные логи

## Производительность

### Оптимизация

- Увеличить `health_check_interval` для снижения нагрузки
- Уменьшить `health_check_duration` для быстрых проверок
- Отключить отладочное логирование в production

### Мониторинг

- Следить за метриками `AudioMetrics`
- Отслеживать количество ошибок
- Мониторить время работы потоков
