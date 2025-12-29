# План интеграции новой аудио-логики (MVP-12) в основной проект

**Статус**: План интеграции  
**Основан на**: `AUDIO_MIGRATION_MASTER_SPECIFICATION.md`, `AUDIO_MIGRATION_SEQUENCE_PLAN.md`, MVP-12 прототипы  
**Дата**: 2025-12-23

---

## 📋 Общая стратегия интеграции

### Принципы

1. **Минимальные изменения существующего кода** — новая логика добавляется через новую интеграцию
2. **Сохранение всех существующих событий EventBus** — обратная совместимость
3. **Feature flag для постепенного rollout** — возможность отката
4. **Единый источник истины** — новая логика управляет устройствами, старые интеграции используют её

---

## 🏗️ Архитектура интеграции

### Текущая архитектура (до изменений)

```
┌─────────────────────────────────────────────────────────────────┐
│                    ТЕКУЩАЯ АРХИТЕКТУРА                          │
└─────────────────────────────────────────────────────────────────┘

InputProcessingIntegration
    │
    ├─→ Публикует: voice.recording_start/stop
    │
    ▼
VoiceRecognitionIntegration
    │
    ├─→ Подписывается: voice.recording_start/stop
    ├─→ Управляет: SpeechRecognizer (sr.Microphone)
    ├─→ Публикует: voice.mic_opened/closed, voice.recognition_*
    │
    ▼
SpeechPlaybackIntegration
    │
    ├─→ Подписывается: grpc.response.audio
    ├─→ Управляет: SequentialSpeechPlayer (sounddevice.OutputStream)
    ├─→ Публикует: playback.started/completed/failed
```

### Новая архитектура (после интеграции)

```
┌─────────────────────────────────────────────────────────────────┐
│                    НОВАЯ АРХИТЕКТУРА                           │
└─────────────────────────────────────────────────────────────────┘

InputProcessingIntegration (БЕЗ ИЗМЕНЕНИЙ)
    │
    ├─→ Публикует: voice.recording_start/stop (как раньше)
    │
    ▼
┌─────────────────────────────────────────────────────────────────┐
│ AudioRouteManagerIntegration (НОВАЯ)                            │
│                                                                 │
│ • DeviceDiscovery (AVFoundation)                                │
│ • DeviceMapping (PortAudio)                                     │
│ • Мониторинг устройств (каждую секунду)                         │
│ • Управление input/output устройствами                          │
│ • Reconcile loop для принятия решений                          │
└─────────────────────────────────────────────────────────────────┘
    │
    ├─→ Подписывается: voice.recording_start/stop
    ├─→ Управляет: sounddevice.InputStream (единственный владелец микрофона)
    ├─→ Публикует: audio.input.active, audio.output.ready
    │
    ▼
VoiceRecognitionIntegration (АДАПТИРОВАННАЯ)
    │
    ├─→ Подписывается: voice.recording_start/stop, audio.input.active
    ├─→ НЕ управляет микрофоном напрямую (использует AudioRouteManager)
    ├─→ Получает аудио-данные из AudioRouteManager
    ├─→ Публикует: voice.mic_opened/closed, voice.recognition_* (как раньше)
    │
    ▼
SpeechPlaybackIntegration (АДАПТИРОВАННАЯ)
    │
    ├─→ Подписывается: grpc.response.audio, audio.output.ready
    ├─→ НЕ управляет output напрямую (использует AudioRouteManager)
    ├─→ Использует AVAudioEngine через AudioRouteManager
    ├─→ Публикует: playback.started/completed/failed (как раньше)
```

---

## 📦 Структура новых компонентов

### 1. Модуль: `modules/audio_route_manager/`

```
modules/audio_route_manager/
├── core/
│   ├── __init__.py
│   ├── contracts.py              # DeviceInfo, MappingResult, RouteSnapshot
│   ├── device_discovery.py       # AVFoundation discovery (из MVP-1)
│   ├── device_mapping.py          # PortAudio mapping (из MVP-2)
│   ├── route_manager.py          # Основной менеджер маршрутизации
│   ├── reconcile_engine.py       # Reconcile loop (из SPEC)
│   ├── input_state_machine.py     # FSM для input
│   ├── output_state_machine.py   # FSM для output
│   └── adapters/
│       ├── avf_input_adapter.py  # sounddevice.InputStream wrapper
│       └── avf_output_adapter.py  # AVAudioEngine wrapper
├── types.py                       # Типы для модуля
└── README.md                      # Документация модуля
```

### 2. Интеграция: `integration/integrations/audio_route_manager_integration.py`

```
AudioRouteManagerIntegration
├── Инициализация:
│   ├── DeviceDiscovery
│   ├── DeviceMapping
│   ├── RouteManager
│   └── Мониторинг устройств (thread)
│
├── Подписки EventBus:
│   ├── voice.recording_start → запуск input через reconcile
│   ├── voice.recording_stop → остановка input
│   ├── app.mode_changed → проверка необходимости переключения
│   └── permissions.first_run_* → блокировка активации
│
└── Публикации EventBus:
    ├── audio.input.active → input готов
    ├── audio.output.ready → output готов
    ├── audio.route.snapshot → диагностика
    └── audio.device.changed → уведомление о смене устройства
```

---

## 🔄 Поток событий (EventBus)

### Сценарий 1: Push-to-talk (запись)

```
1. InputProcessingIntegration
   └─→ Публикует: voice.recording_start {session_id: "123"}

2. AudioRouteManagerIntegration
   ├─→ Подписывается: voice.recording_start
   ├─→ Reconcile loop: проверяет состояние (permissions, first_run, devices)
   ├─→ Создает: sounddevice.InputStream (единственный владелец микрофона)
   ├─→ Публикует: audio.input.active {session_id: "123", device_uid: "..."}

3. VoiceRecognitionIntegration
   ├─→ Подписывается: audio.input.active
   ├─→ Получает аудио-данные из AudioRouteManager (callback)
   ├─→ Отправляет в Google SR
   └─→ Публикует: voice.mic_opened, voice.recognition_started (как раньше)

4. InputProcessingIntegration
   └─→ Публикует: voice.recording_stop {session_id: "123"}

5. AudioRouteManagerIntegration
   ├─→ Подписывается: voice.recording_stop
   ├─→ Останавливает: sounddevice.InputStream
   └─→ Публикует: audio.input.inactive {session_id: "123"}

6. VoiceRecognitionIntegration
   ├─→ Завершает распознавание
   └─→ Публикует: voice.recognition_completed, voice.mic_closed (как раньше)
```

### Сценарий 2: Воспроизведение ответа

```
1. GrpcClientIntegration
   └─→ Публикует: grpc.response.audio {session_id: "123", audio_bytes: ...}

2. SpeechPlaybackIntegration
   ├─→ Подписывается: grpc.response.audio
   ├─→ Проверяет: audio.output.ready (от AudioRouteManager)
   ├─→ Использует: AVAudioEngine через AudioRouteManager
   └─→ Публикует: playback.started/completed (как раньше)
```

### Сценарий 3: Переключение устройства

```
1. AudioRouteManagerIntegration (мониторинг thread)
   ├─→ Обнаруживает: изменение устройства (AVFoundation + PortAudio)
   ├─→ Reconcile loop: принимает решение о переключении
   ├─→ Переключает: sounddevice.InputStream (input) или AVAudioEngine (output)
   └─→ Публикует: audio.device.changed {type: "input|output", device_uid: "..."}

2. VoiceRecognitionIntegration / SpeechPlaybackIntegration
   ├─→ Подписывается: audio.device.changed
   └─→ Адаптируется к новому устройству (если нужно)
```

---

## 🔧 Детальный план реализации

### Этап 1: Создание модуля audio_route_manager (PR 1)

**Ветка**: `feature/audio-route-manager-module`  
**Дни**: 1-5

#### День 1-2: Базовые компоненты

**Файлы**:
- `modules/audio_route_manager/core/contracts.py`
- `modules/audio_route_manager/core/device_discovery.py`
- `modules/audio_route_manager/core/device_mapping.py`

**Источник**: Адаптация из MVP-1, MVP-2 прототипов

**Критерии**:
- [ ] Линтер проходит
- [ ] Тесты проходят (≥80% покрытие)
- [ ] Совместимость с существующими типами

#### День 3-4: State Machines

**Файлы**:
- `modules/audio_route_manager/core/input_state_machine.py`
- `modules/audio_route_manager/core/output_state_machine.py`

**Источник**: Из `AUDIO_MIGRATION_MASTER_SPECIFICATION.md`

**Критерии**:
- [ ] Все состояния определены
- [ ] Переходы валидируются
- [ ] Тесты покрывают все переходы

#### День 5: Reconcile Engine

**Файлы**:
- `modules/audio_route_manager/core/reconcile_engine.py`

**Источник**: Из `AUDIO_MIGRATION_MASTER_SPECIFICATION.md`

**Критерии**:
- [ ] Single-flight механизм работает
- [ ] Debounce по устройствам работает
- [ ] Тесты на "device storm"

---

### Этап 2: Route Manager Core (PR 2)

**Ветка**: `feature/audio-route-manager-core`  
**Дни**: 6-10

#### День 6-7: Route Manager

**Файлы**:
- `modules/audio_route_manager/core/route_manager.py`

**Источник**: Из `AUDIO_MIGRATION_MASTER_SPECIFICATION.md`

**Функциональность**:
- Управление input/output состояниями
- Интеграция с reconcile engine
- Принятие решений через gateways

**Критерии**:
- [ ] Все решения через reconcile
- [ ] Нет прямого доступа к состоянию (только через selectors)
- [ ] Decision logs в каноническом формате

#### День 8-9: Adapters

**Файлы**:
- `modules/audio_route_manager/core/adapters/avf_input_adapter.py`
- `modules/audio_route_manager/core/adapters/avf_output_adapter.py`

**Источник**: Адаптация из MVP-12 прототипов

**Функциональность**:
- `AVFInputAdapter`: обертка над `sounddevice.InputStream`
- `AVFOutputAdapter`: обертка над `AVAudioEngine`

**Критерии**:
- [ ] Единственный владелец микрофона (sounddevice)
- [ ] Fallback samplerate работает
- [ ] Переключение устройств работает

#### День 10: Интеграция компонентов

**Файлы**:
- `modules/audio_route_manager/core/route_manager.py` (доработка)

**Критерии**:
- [ ] Все компоненты интегрированы
- [ ] Тесты end-to-end проходят

---

### Этап 3: Интеграция с EventBus (PR 3)

**Ветка**: `feature/audio-route-manager-integration`  
**Дни**: 11-15

#### День 11-12: AudioRouteManagerIntegration

**Файлы**:
- `integration/integrations/audio_route_manager_integration.py`

**Функциональность**:
- Инициализация RouteManager
- Подписки на EventBus события
- Публикация событий
- Мониторинг устройств (thread)

**Подписки**:
```python
await self.event_bus.subscribe("voice.recording_start", self._on_recording_start, EventPriority.HIGH)
await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop, EventPriority.HIGH)
await self.event_bus.subscribe("app.mode_changed", self._on_mode_changed, EventPriority.MEDIUM)
await self.event_bus.subscribe("permissions.first_run_started", self._on_first_run_started, EventPriority.CRITICAL)
await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.CRITICAL)
```

**Публикации**:
```python
await self.event_bus.publish("audio.input.active", {
    "session_id": session_id,
    "device_uid": device_uid,
    "device_name": device_name
})

await self.event_bus.publish("audio.output.ready", {
    "device_uid": device_uid,
    "device_name": device_name
})

await self.event_bus.publish("audio.device.changed", {
    "type": "input" | "output",
    "old_device_uid": old_uid,
    "new_device_uid": new_uid
})
```

**Критерии**:
- [ ] Все события определены в контракте
- [ ] Подписки работают
- [ ] Публикации работают

#### День 13-14: Адаптация VoiceRecognitionIntegration

**Файлы**:
- `integration/integrations/voice_recognition_integration.py`

**Изменения**:
```python
# ДОБАВИТЬ: Feature flag
self._use_audio_route_manager = unified_config.get('audio_route_manager', {}).get('enabled', False)

# ИЗМЕНИТЬ: _on_recording_start
async def _on_recording_start(self, event):
    if self._first_run_in_progress:
        return
    
    if self._use_audio_route_manager:
        # Новая логика: AudioRouteManager управляет микрофоном
        # Мы только ждем audio.input.active и получаем данные
        session_id = event.get("session_id")
        await self.event_bus.publish("audio.input.request_start", {
            "session_id": session_id
        })
        # Ждем audio.input.active для получения аудио-данных
    else:
        # Старая логика (fallback)
        if not self.config.simulate and self._recognizer:
            await self._recognizer.start_listening()
```

**Критерии**:
- [ ] Feature flag работает
- [ ] Обратная совместимость сохранена
- [ ] Все существующие события публикуются

#### День 15: Адаптация SpeechPlaybackIntegration

**Файлы**:
- `integration/integrations/speech_playback_integration.py`

**Изменения**:
```python
# ДОБАВИТЬ: Feature flag
self._use_audio_route_manager = unified_config.get('audio_route_manager', {}).get('enabled', False)

# ИЗМЕНИТЬ: _on_audio_chunk
async def _on_audio_chunk(self, event):
    if self._use_audio_route_manager:
        # Новая логика: используем AVAudioEngine через AudioRouteManager
        # Проверяем audio.output.ready перед воспроизведением
        # Используем AVFOutputAdapter для воспроизведения
    else:
        # Старая логика (fallback)
        # Используем SequentialSpeechPlayer как раньше
```

**Критерии**:
- [ ] Feature flag работает
- [ ] Обратная совместимость сохранена
- [ ] Все существующие события публикуются

---

### Этап 4: Интеграция в SimpleModuleCoordinator (PR 4)

**Ветка**: `feature/audio-route-manager-coordinator`  
**Дни**: 16-18

#### День 16-17: Добавление в координатор

**Файлы**:
- `integration/core/simple_module_coordinator.py`

**Изменения**:
```python
# ДОБАВИТЬ: Импорт
from integration.integrations.audio_route_manager_integration import AudioRouteManagerIntegration

# ДОБАВИТЬ: В _create_integrations() (после FirstRunPermissions, перед VoiceRecognition)
self.integrations['audio_route_manager'] = AudioRouteManagerIntegration(
    event_bus=self.event_bus,
    state_manager=self.state_manager,
    error_handler=self.error_handler,
    config=audio_route_config
)
```

**Порядок инициализации** (обновленный):
1. InstanceManager
2. HardwareId
3. FirstRunPermissions
4. PermissionRestart
5. **AudioRouteManager** ← НОВОЕ (должно быть перед VoiceRecognition)
6. Tray
7. ModeManagement
8. InputProcessing
9. VoiceRecognition ← зависит от AudioRouteManager
10. NetworkManager
11. ...
12. SpeechPlayback ← зависит от AudioRouteManager

**Критерии**:
- [ ] Порядок инициализации правильный
- [ ] Зависимости разрешены
- [ ] Нет циклических зависимостей

#### День 18: Конфигурация

**Файлы**:
- `config/unified_config.yaml`

**Добавить**:
```yaml
audio_route_manager:
  enabled: false  # Feature flag (по умолчанию выключен)
  device_monitoring_interval_sec: 1.0
  reconcile_debounce_ms: 500
  input:
    fallback_samplerates: [48000, 16000, 44100, 48000]
    blocksize: 1024
  output:
    auto_device_switch: true
```

**Критерии**:
- [ ] Конфигурация загружается
- [ ] Feature flag работает
- [ ] Все параметры настраиваемы

---

### Этап 5: Тестирование и отладка (PR 5)

**Ветка**: `feature/audio-route-manager-testing`  
**Дни**: 19-25

#### День 19-20: Unit тесты

**Файлы**:
- `tests/test_audio_route_manager.py`
- `tests/test_audio_route_manager_integration.py`

**Критерии**:
- [ ] Покрытие ≥80%
- [ ] Все edge cases покрыты
- [ ] Тесты на device storm

#### День 21-22: Integration тесты

**Файлы**:
- `tests/integration/test_audio_route_manager_e2e.py`

**Сценарии**:
- Push-to-talk с переключением устройств
- Воспроизведение с переключением устройств
- Device storm (множественные переключения)

**Критерии**:
- [ ] Все сценарии проходят
- [ ] Нет race conditions
- [ ] Нет memory leaks

#### День 23-25: Ручное тестирование

**Чек-лист**:
- [ ] Push-to-talk работает
- [ ] Переключение input устройств работает
- [ ] Переключение output устройств работает
- [ ] Воспроизведение работает
- [ ] Все существующие функции работают (fallback mode)
- [ ] Feature flag работает (включение/выключение)

---

## 🔄 Миграционный путь

### Фаза 1: Подготовка (неделя 1-2)

1. Создать модуль `audio_route_manager`
2. Создать интеграцию `AudioRouteManagerIntegration`
3. Добавить feature flag в конфигурацию
4. **Feature flag: OFF** (по умолчанию)

### Фаза 2: Shadow mode (неделя 3-4)

1. Включить feature flag для тестовых пользователей (1%)
2. Параллельная работа: старая логика + новая логика
3. Мониторинг метрик и ошибок
4. **Feature flag: 1% пользователей**

### Фаза 3: Gradual rollout (неделя 5-8)

1. Увеличить процент пользователей: 1% → 25% → 50% → 75%
2. Мониторинг на каждом этапе
3. Откат при проблемах
4. **Feature flag: 25% → 50% → 75%**

### Фаза 4: Full rollout (неделя 9)

1. Включить для всех пользователей (100%)
2. Удалить старую логику (опционально)
3. **Feature flag: 100%**

---

## 🛡️ Защита от ошибок

### Kill-switch

```yaml
# unified_config.yaml
audio_route_manager:
  enabled: false  # Мгновенный откат
  kill_switch: true  # Принудительное отключение
```

### Fallback механизм

- Если `audio_route_manager.enabled = false` → используется старая логика
- Если AudioRouteManager падает → автоматический fallback на старую логику
- Логирование всех ошибок для диагностики

---

## 📊 Метрики для мониторинга

### Input метрики

- `audio_input_start_success_rate` — процент успешных запусков input
- `audio_input_device_switch_latency_ms` — задержка переключения устройств
- `audio_input_fallback_triggered` — количество срабатываний fallback

### Output метрики

- `audio_output_start_success_rate` — процент успешных запусков output
- `audio_output_device_switch_latency_ms` — задержка переключения устройств
- `audio_output_fallback_triggered` — количество срабатываний fallback

### Общие метрики

- `audio_reconcile_loop_duration_ms` — длительность reconcile loop
- `audio_device_storm_events` — количество событий device storm
- `audio_route_manager_errors` — количество ошибок RouteManager

---

## ✅ Критерии успеха

### Технические

- [ ] Все тесты проходят (unit + integration)
- [ ] Нет регрессий в существующем функционале
- [ ] Метрики соответствуют SLO
- [ ] Нет memory leaks
- [ ] Нет race conditions

### Функциональные

- [ ] Push-to-talk работает стабильно
- [ ] Переключение устройств работает плавно
- [ ] Воспроизведение работает без задержек
- [ ] Все существующие функции работают (fallback mode)

### Процессные

- [ ] Feature flag работает корректно
- [ ] Kill-switch работает мгновенно
- [ ] Мониторинг метрик настроен
- [ ] Документация обновлена

---

## 📝 Следующие шаги

1. **Создать Impact Map** для каждого этапа
2. **Обновить STATE_CATALOG.md** с новыми осями состояния
3. **Обновить interaction_matrix.yaml** с новыми правилами
4. **Создать контракт EventBus** для новых событий
5. **Начать реализацию Этапа 1**

---

## 🔗 Связанные документы

- `Docs/AUDIO_MIGRATION_MASTER_SPECIFICATION.md` — нормативная спецификация
- `Docs/AUDIO_MIGRATION_SEQUENCE_PLAN.md` — план последовательности
- `audio_migration_prototypes/mvp12_full_input_output/ARCHITECTURE_DIAGRAM.md` — схема MVP-12
- `Docs/STATE_CATALOG.md` — каталог состояний
- `config/interaction_matrix.yaml` — матрица взаимодействий

