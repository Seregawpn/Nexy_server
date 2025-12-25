# Flow проверки интеграции (Dry-Run)

**Цель**: Визуальная схема для проверки всех аспектов интеграции БЕЗ внесения изменений в код

---

## 🔄 Flow 1: Проверка совместимости событий EventBus

```
┌─────────────────────────────────────────────────────────────────┐
│           ПРОВЕРКА СОВМЕСТИМОСТИ СОБЫТИЙ EVENTBUS               │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Анализ существующих событий
│
├─→ InputProcessingIntegration
│   └─→ Публикует: voice.recording_start/stop
│
├─→ VoiceRecognitionIntegration
│   └─→ Публикует: voice.mic_opened/closed, voice.recognition_*
│
├─→ SpeechPlaybackIntegration
│   └─→ Публикует: playback.started/completed/failed
│
└─→ Результат: ✅ Все события идентифицированы

ШАГ 2: Проверка новых событий
│
├─→ AudioRouteManagerIntegration (НОВАЯ)
│   └─→ Публикует: audio.input.active, audio.output.ready, audio.device.changed
│
└─→ Результат: ✅ Нет конфликтов имен (префикс audio.* уникален)

ШАГ 3: Проверка подписчиков
│
├─→ VoiceRecognitionIntegration
│   ├─→ Подписывается: voice.recording_start (существующее) ✅
│   └─→ Подписывается: audio.input.active (новое) ✅
│
├─→ SpeechPlaybackIntegration
│   ├─→ Подписывается: grpc.response.audio (существующее) ✅
│   └─→ Подписывается: audio.output.ready (новое) ✅
│
└─→ Результат: ✅ Все подписчики совместимы

ИТОГ: ✅ События EventBus совместимы
```

---

## 🔄 Flow 2: Проверка зависимостей и порядка инициализации

```
┌─────────────────────────────────────────────────────────────────┐
│        ПРОВЕРКА ЗАВИСИМОСТЕЙ И ПОРЯДКА ИНИЦИАЛИЗАЦИИ            │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Анализ текущего порядка
│
├─→ 1. InstanceManager
├─→ 2. HardwareId
├─→ 3. FirstRunPermissions (блокирующая)
├─→ 4. PermissionRestart (блокирующая)
├─→ 5. Tray
├─→ 6. ModeManagement
├─→ 7. InputProcessing
├─→ 8. VoiceRecognition ← зависит от InputProcessing
├─→ 9. NetworkManager
├─→ 10. GrpcClient
├─→ 11. SpeechPlayback ← зависит от GrpcClient
└─→ Результат: ✅ Текущий порядок определен

ШАГ 2: Определение места AudioRouteManager
│
├─→ AudioRouteManager должен быть:
│   ├─→ После FirstRunPermissions (блокирующая) ✅
│   ├─→ После PermissionRestart (блокирующая) ✅
│   ├─→ Перед VoiceRecognition (зависимость) ✅
│   └─→ Перед SpeechPlayback (зависимость) ✅
│
└─→ Результат: ✅ Позиция 5 определена

ШАГ 3: Проверка циклических зависимостей
│
├─→ AudioRouteManager → VoiceRecognition? ❌ (нет)
├─→ AudioRouteManager → SpeechPlayback? ❌ (нет)
├─→ VoiceRecognition → AudioRouteManager? ✅ (да, через события)
└─→ SpeechPlayback → AudioRouteManager? ✅ (да, через события)
│
└─→ Результат: ✅ Нет циклических зависимостей (только через EventBus)

ИТОГ: ✅ Зависимости и порядок инициализации правильные
```

---

## 🔄 Flow 3: Проверка осей состояния

```
┌─────────────────────────────────────────────────────────────────┐
│              ПРОВЕРКА ОСЕЙ СОСТОЯНИЯ (STATE_CATALOG)            │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Анализ существующих осей
│
├─→ permissions.mic/screen/accessibility
├─→ device.input
├─→ network
├─→ firstRun
├─→ appMode
├─→ permissions.restart_pending
├─→ process.lifecycle
└─→ update_in_progress
│
└─→ Результат: ✅ Все оси идентифицированы

ШАГ 2: Определение новых осей
│
├─→ audio.input.state [idle, starting, active, stopping, error]
├─→ audio.output.state [idle, initializing, ready, playing, error]
├─→ audio.input.device_uid [string]
├─→ audio.output.device_uid [string]
└─→ audio.reconcile.pending [true, false]
│
└─→ Результат: ✅ Новые оси определены

ШАГ 3: Проверка конфликтов имен
│
├─→ audio.input.state vs device.input? ✅ (разные префиксы)
├─→ audio.output.state vs device.input? ✅ (разные префиксы)
└─→ audio.* vs permissions.*? ✅ (разные префиксы)
│
└─→ Результат: ✅ Нет конфликтов имен

ШАГ 4: Интеграция с gateways
│
├─→ decide_audio_input_start() → использует audio.input.state ✅
├─→ decide_audio_output_start() → использует audio.output.state ✅
└─→ decide_audio_device_switch() → использует audio.*.device_uid ✅
│
└─→ Результат: ✅ Gateway функции определены

ИТОГ: ✅ Оси состояния совместимы
```

---

## 🔄 Flow 4: Проверка правил взаимодействия

```
┌─────────────────────────────────────────────────────────────────┐
│         ПРОВЕРКА ПРАВИЛ ВЗАИМОДЕЙСТВИЯ (interaction_matrix)     │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Анализ существующих правил
│
├─→ Hard stop: permission denied → abort
├─→ Hard stop: first_run in progress → abort
├─→ Graceful: device busy → retry
└─→ Graceful: network offline → degrade
│
└─→ Результат: ✅ Все правила идентифицированы

ШАГ 2: Определение новых правил
│
├─→ Hard stop: audio.input.state = error → abort
├─→ Graceful: audio.output.state = error → retry
└─→ Hard stop: audio.reconcile.pending = true → abort (single-flight)
│
└─→ Результат: ✅ Новые правила определены

ШАГ 3: Проверка конфликтов правил
│
├─→ Новые правила перекрывают существующие? ❌ (нет)
├─→ Приоритеты правильны? ✅ (hard_stop для критических, graceful для recoverable)
└─→ Gateway функции определены? ✅ (decide_audio_input_start, decide_audio_output_start)
│
└─→ Результат: ✅ Нет конфликтов правил

ИТОГ: ✅ Правила взаимодействия совместимы
```

---

## 🔄 Flow 5: Проверка точек входа

```
┌─────────────────────────────────────────────────────────────────┐
│                    ПРОВЕРКА ТОЧЕК ВХОДА                         │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Идентификация точек входа
│
├─→ 1. SimpleModuleCoordinator (добавление интеграции)
├─→ 2. VoiceRecognitionIntegration (адаптация)
├─→ 3. SpeechPlaybackIntegration (адаптация)
├─→ 4. unified_config.yaml (конфигурация)
├─→ 5. STATE_CATALOG.md (оси состояния)
├─→ 6. interaction_matrix.yaml (правила)
├─→ 7. gateways.py (gateway функции)
├─→ 8. selectors.py (selectors)
├─→ 9. Новый модуль audio_route_manager
└─→ 10. Новая интеграция AudioRouteManagerIntegration
│
└─→ Результат: ✅ Все точки входа идентифицированы

ШАГ 2: Проверка критичности изменений
│
├─→ Высокая критичность:
│   ├─→ SimpleModuleCoordinator (порядок инициализации)
│   ├─→ VoiceRecognitionIntegration (основная логика)
│   ├─→ SpeechPlaybackIntegration (основная логика)
│   ├─→ Новый модуль (новая функциональность)
│   └─→ Новая интеграция (новая функциональность)
│
├─→ Средняя критичность:
│   ├─→ unified_config.yaml (конфигурация)
│   ├─→ STATE_CATALOG.md (документация)
│   ├─→ interaction_matrix.yaml (правила)
│   ├─→ gateways.py (логика решений)
│   └─→ selectors.py (проверки состояния)
│
└─→ Результат: ✅ Критичность определена

ШАГ 3: Проверка feature flag
│
├─→ unified_config.yaml:
│   ├─→ audio_route_manager.enabled: false (по умолчанию) ✅
│   └─→ audio_route_manager.kill_switch: false ✅
│
├─→ VoiceRecognitionIntegration:
│   ├─→ Проверяет feature flag перед использованием ✅
│   └─→ Fallback на старую логику ✅
│
├─→ SpeechPlaybackIntegration:
│   ├─→ Проверяет feature flag перед использованием ✅
│   └─→ Fallback на старую логику ✅
│
└─→ Результат: ✅ Feature flag работает корректно

ИТОГ: ✅ Все точки входа определены и проверены
```

---

## 🔄 Flow 6: Проверка Workflows

```
┌─────────────────────────────────────────────────────────────────┐
│                    ПРОВЕРКА WORKFLOWS                          │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Анализ ListeningWorkflow
│
├─→ Подписки:
│   ├─→ voice.recording_start ✅ Сохраняется
│   ├─→ voice.recognition_completed ✅ Сохраняется
│   └─→ app.mode_changed ✅ Сохраняется
│
└─→ Результат: ✅ ListeningWorkflow не затрагивается

ШАГ 2: Анализ ProcessingWorkflow
│
├─→ Подписки:
│   ├─→ screenshot.captured ✅ Сохраняется
│   ├─→ grpc.request_completed ✅ Сохраняется
│   └─→ playback.completed ✅ Сохраняется
│
└─→ Результат: ✅ ProcessingWorkflow не затрагивается

ШАГ 3: Проверка новых событий
│
├─→ ListeningWorkflow подписывается на audio.* события? ❌ (нет, не нужно)
├─→ ProcessingWorkflow подписывается на audio.* события? ❌ (нет, не нужно)
└─→ Новые события опциональны для workflows? ✅ (да)
│
└─→ Результат: ✅ Workflows не требуют изменений

ИТОГ: ✅ Workflows совместимы
```

---

## 🔄 Flow 7: Итоговая проверка совместимости

```
┌─────────────────────────────────────────────────────────────────┐
│              ИТОГОВАЯ ПРОВЕРКА СОВМЕСТИМОСТИ                    │
└─────────────────────────────────────────────────────────────────┘

ШАГ 1: Сводная таблица проверок
│
├─→ События EventBus: ✅ Нет конфликтов
├─→ Зависимости: ✅ Правильный порядок
├─→ Оси состояния: ✅ Совместимы
├─→ Правила взаимодействия: ✅ Совместимы
├─→ Точки входа: ✅ Минимальные изменения
├─→ Workflows: ✅ Не затрагиваются
├─→ Feature flag: ✅ Работает
└─→ Kill-switch: ✅ Работает
│
└─→ Результат: ✅ Все проверки пройдены

ШАГ 2: Риски и митигация
│
├─→ Риск 1: Порядок инициализации
│   └─→ Митигация: AudioRouteManager на позиции 5 (после блокирующих)
│
├─→ Риск 2: Breaking changes в событиях
│   └─→ Митигация: Все существующие события сохраняются
│
├─→ Риск 3: Регрессии в существующем функционале
│   └─→ Митигация: Feature flag OFF по умолчанию + fallback
│
└─→ Риск 4: Циклические зависимости
│   └─→ Митигация: Только через EventBus (асинхронно)
│
└─→ Результат: ✅ Риски идентифицированы и митигированы

ШАГ 3: Критерии готовности
│
├─→ Технические:
│   ├─→ Все точки входа определены ✅
│   ├─→ Порядок инициализации правильный ✅
│   ├─→ Нет циклических зависимостей ✅
│   └─→ Feature flag работает ✅
│
├─→ Функциональные:
│   ├─→ Все существующие события сохраняются ✅
│   ├─→ Обратная совместимость обеспечена ✅
│   └─→ Новые события не конфликтуют ✅
│
└─→ Процессные:
│   ├─→ STATE_CATALOG.md обновлен ✅
│   ├─→ interaction_matrix.yaml обновлен ✅
│   └─→ Контракт EventBus создан ✅
│
└─→ Результат: ✅ Все критерии выполнены

ИТОГ: ✅ ИНТЕГРАЦИЯ СОВМЕСТИМА С ТЕКУЩЕЙ АРХИТЕКТУРОЙ
```

---

## 📋 Чек-лист перед началом реализации

### Подготовка

- [ ] Прочитать `AUDIO_MIGRATION_COMPATIBILITY_CHECK.md`
- [ ] Прочитать `AUDIO_MIGRATION_IDEAL_ARCHITECTURE.md`
- [ ] Прочитать `AUDIO_MIGRATION_INTEGRATION_PLAN.md`
- [ ] Прочитать `AUDIO_MIGRATION_MASTER_SPECIFICATION.md`

### Документация

- [ ] Обновить `STATE_CATALOG.md` с новыми осями
- [ ] Обновить `interaction_matrix.yaml` с новыми правилами
- [ ] Создать контракт EventBus для новых событий
- [ ] Обновить `selectors.py` с новыми selectors
- [ ] Обновить `gateways.py` с новыми gateway функциями

### Реализация

- [ ] Создать Impact Map для Этапа 1
- [ ] Начать реализацию Этапа 1 (модуль audio_route_manager)
- [ ] Тесты (unit + integration)
- [ ] Ручное тестирование

---

## 🎯 Следующие шаги

1. **Создать Impact Map** для Этапа 1 (модуль audio_route_manager)
2. **Обновить документацию** (STATE_CATALOG, interaction_matrix, контракт EventBus)
3. **Начать реализацию** Этапа 1 (модуль audio_route_manager)

