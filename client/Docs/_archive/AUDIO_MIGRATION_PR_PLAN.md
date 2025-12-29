# Migration PR Plan: Пошаговый план реализации по дням

**Статус**: Детальный план для реализации  
**Версия**: 1.0  
**Дата**: 2025-01-XX  
**Основан на**: `AUDIO_MIGRATION_COMPLETE_IMPLEMENTATION_PLAN.md`

**Примечание**: Этот документ является детальным PR-планом. Главный нормативный документ: `Docs/AUDIO_MIGRATION_MASTER_SPECIFICATION.md`

---

## 📋 Общая структура

**9 этапов, 42 дня работы, 9 PR**

Каждый PR соответствует одному этапу и может быть мержен независимо (при условии feature flags).

---

## 🎯 PR 1: Базовые компоненты (Этап 1)

**Ветка**: `feature/avfoundation-audio-stage1-contracts-mapping`  
**Дни**: 1-4  
**Файлы**: 2 новых + 1 тест

### День 1-2: contracts.py

**Файл**: `modules/voice_recognition/core/avfoundation/contracts.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `Confidence` enum
- [ ] Реализовать `DeviceTransport` enum
- [ ] Реализовать `DeviceSignature` dataclass
- [ ] Реализовать `RouteSnapshot` dataclass
- [ ] Реализовать `MappingResult` dataclass
- [ ] Добавить методы `__str__`, `input_changed()`, `output_changed()`, `is_usable()`

**Тесты**: `tests/test_avfoundation_contracts.py`
- [ ] Тест создания всех типов
- [ ] Тест методов RouteSnapshot
- [ ] Тест методов MappingResult
- [ ] Покрытие ≥80%

**Критерии готовности**:
- [ ] Линтер проходит
- [ ] Тесты проходят
- [ ] Покрытие ≥80%

---

### День 3-4: mapping.py

**Файл**: `modules/voice_recognition/core/avfoundation/mapping.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `DeviceMapper` класс
- [ ] Реализовать `normalize_device_name()`
- [ ] Реализовать `detect_transport()`
- [ ] Реализовать `build_signature()`
- [ ] Реализовать `find_portaudio_match()`
- [ ] Реализовать `get_device_index()`
- [ ] Реализовать кэширование
- [ ] Реализовать `clear_cache()`

**Тесты**: `tests/test_avfoundation_mapping.py`
- [ ] Тест normalize_device_name()
- [ ] Тест detect_transport() для всех типов
- [ ] Тест build_signature()
- [ ] Тест find_portaudio_match() (HIGH/MEDIUM/LOW/NONE)
- [ ] Тест get_device_index() с кэшем
- [ ] Тест clear_cache()
- [ ] Покрытие ≥80%

**Критерии готовности**:
- [ ] Линтер проходит
- [ ] Тесты проходят
- [ ] Покрытие ≥80%
- [ ] Тесты на реальных устройствах (Bluetooth/USB/Built-in)

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Документация обновлена (если нужно)
- [ ] Code review пройден

---

## 🎯 PR 2: State Machines (Этап 2)

**Ветка**: `feature/avfoundation-audio-stage2-state-machines`  
**Дни**: 5-8  
**Файлы**: 2 новых + обновление тестов

### День 5-6: input_state_machine.py

**Файл**: `modules/voice_recognition/core/avfoundation/input_state_machine.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `InputState` enum
- [ ] Реализовать `InputStateMachine` dataclass
- [ ] Реализовать `transition_to()`
- [ ] Реализовать `update_heartbeat()`
- [ ] Реализовать `check_heartbeat()`
- [ ] Реализовать `can_retry()`
- [ ] Реализовать `get_retry_backoff_sec()`
- [ ] Реализовать `should_rollback()`

**Тесты**: `tests/test_avfoundation_state_machines.py` (input часть)
- [ ] Тест переходов: STOPPED → STARTING → ACTIVE
- [ ] Тест переходов: ACTIVE → STOPPING → STOPPED
- [ ] Тест перехода: STARTING → FAILED (timeout)
- [ ] Тест перехода: ACTIVE → FAILED (heartbeat lost)
- [ ] Тест retry логики
- [ ] Тест heartbeat проверки
- [ ] Тест rollback логики
- [ ] Покрытие ≥80%

---

### День 7-8: output_state_machine.py

**Файл**: `modules/voice_recognition/core/avfoundation/output_state_machine.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `OutputState` enum
- [ ] Реализовать `OutputStateMachine` dataclass
- [ ] Реализовать `transition_to()`
- [ ] Реализовать `check_recreate_timeout()`
- [ ] Реализовать `can_retry()`
- [ ] Реализовать `get_retry_backoff_sec()`

**Тесты**: `tests/test_avfoundation_state_machines.py` (output часть)
- [ ] Тест переходов: READY → RECREATING → READY
- [ ] Тест перехода: RECREATING → ERROR (timeout)
- [ ] Тест перехода: ERROR → RECREATING (retry)
- [ ] Тест retry логики
- [ ] Тест timeout проверки
- [ ] Покрытие ≥80%

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Покрытие ≥80%
- [ ] Code review пройден

---

## 🎯 PR 3: Route Manager Core - Part 1 (Этап 3, дни 9-12)

**Ветка**: `feature/avfoundation-audio-stage3-route-manager-core-1`  
**Дни**: 9-12  
**Файлы**: 2 новых + обновление тестов

### День 9-10: debounce_manager.py

**Файл**: `modules/voice_recognition/core/avfoundation/debounce_manager.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `DebounceConfig` dataclass
- [ ] Реализовать `DebounceManager` класс
- [ ] Реализовать `get_debounce_delay_ms()`
- [ ] Реализовать `reset_device()`
- [ ] Реализовать `clear_all()`

**Тесты**: `tests/test_avfoundation_route_manager.py` (debounce часть)
- [ ] Тест get_debounce_delay_ms() для всех транспортов
- [ ] Тест инкремента счетчика
- [ ] Тест reset_device()
- [ ] Тест clear_all()
- [ ] Покрытие ≥80%

---

### День 11-12: decision_engine.py

**Файл**: `modules/voice_recognition/core/avfoundation/decision_engine.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `Decision` enum
- [ ] Реализовать `DecisionContext` dataclass
- [ ] Реализовать `DecisionEngine` класс
- [ ] Реализовать `decide_route_manager_reconcile()`
- [ ] Реализовать `format_decision_log()`
- [ ] Реализовать все правила из interaction_matrix.yaml

**Тесты**: `tests/test_avfoundation_route_manager.py` (decision часть)
- [ ] Тест ABORT при first_run
- [ ] Тест ABORT при restart_pending
- [ ] Тест ABORT при update_in_progress
- [ ] Тест ABORT при mic denied
- [ ] Тест RETRY при device_busy
- [ ] Тест DEGRADE при network_offline
- [ ] Тест NOOP при отсутствии изменений
- [ ] Тест START при нормальных условиях
- [ ] Тест format_decision_log()
- [ ] Pairwise тесты (≥12 комбинаций)
- [ ] Негативные тесты (≥2)
- [ ] Покрытие ≥80%

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Pairwise тесты созданы
- [ ] Decision-логи в каноническом формате
- [ ] Code review пройден

---

## 🎯 PR 4: Route Manager Core - Part 2 (Этап 3, дни 13-16)

**Ветка**: `feature/avfoundation-audio-stage3-route-manager-core-2`  
**Дни**: 13-16  
**Файлы**: 2 новых + обновление тестов

### День 13-14: reconcile_engine.py

**Файл**: `modules/voice_recognition/core/avfoundation/reconcile_engine.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `ReconcileResult` dataclass
- [ ] Реализовать `ReconcileEngine` класс
- [ ] Реализовать `create_snapshot()`
- [ ] Реализовать `determine_desired_route()`
- [ ] Реализовать `compare_routes()`

**Тесты**: `tests/test_avfoundation_route_manager.py` (reconcile часть)
- [ ] Тест create_snapshot()
- [ ] Тест determine_desired_route() с user_selection
- [ ] Тест determine_desired_route() с system_default
- [ ] Тест determine_desired_route() fallback
- [ ] Тест compare_routes() input_changed
- [ ] Тест compare_routes() output_changed
- [ ] Тест compare_routes() no_changes
- [ ] Покрытие ≥80%

---

### День 15-16: route_manager.py

**Файл**: `modules/voice_recognition/core/avfoundation/route_manager.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `AudioRouteManager` класс
- [ ] Реализовать `__init__()`
- [ ] Реализовать `set_event_loop()`
- [ ] Реализовать `set_callbacks()`
- [ ] Реализовать `reconcile_routes()` с single-flight
- [ ] Реализовать `_apply_input_change()`
- [ ] Реализовать `_apply_output_change()`
- [ ] Реализовать `get_active_input_device()`
- [ ] Реализовать `get_active_output_device()`

**Тесты**: `tests/test_avfoundation_route_manager.py` (основной)
- [ ] Тест reconcile_routes() single-flight
- [ ] Тест reconcile_routes() pending
- [ ] Тест _apply_input_change()
- [ ] Тест _apply_output_change()
- [ ] Тест get_active_input_device()
- [ ] Тест get_active_output_device()
- [ ] Интеграционные тесты
- [ ] Покрытие ≥80%

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Single-flight механизм работает
- [ ] Reconcile loop работает
- [ ] Code review пройден

---

## 🎯 PR 5: Адаптеры (Этап 4)

**Ветка**: `feature/avfoundation-audio-stage4-adapters`  
**Дни**: 17-21  
**Файлы**: 3 новых + обновление тестов

### День 17-18: avf_monitor.py

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `DeviceInfo` dataclass
- [ ] Реализовать `AVFoundationDeviceMonitor` класс
- [ ] Реализовать `_setup_notifications()`
- [ ] Реализовать `routeChanged_()` (NSNotification handler)
- [ ] Реализовать `_check_devices_instant()`
- [ ] Реализовать `_query_devices()`
- [ ] Реализовать `_process_device_changes()`
- [ ] Реализовать `start_monitoring()`
- [ ] Реализовать `_monitor_loop()` (polling)
- [ ] Реализовать `stop_monitoring()`
- [ ] Реализовать `get_current_devices()`

**Тесты**: `tests/test_avfoundation_adapters.py` (monitor часть)
- [ ] Тест start_monitoring()
- [ ] Тест stop_monitoring()
- [ ] Тест _query_devices()
- [ ] Тест _process_device_changes()
- [ ] Тест get_current_devices()
- [ ] Покрытие ≥80%

---

### День 19-20: avf_output.py

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/avf_output.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `ChunkInfo` dataclass
- [ ] Реализовать `AVFoundationAudioPlayback` класс
- [ ] Реализовать `initialize()`
- [ ] Реализовать `play_chunk()`
- [ ] Реализовать `_numpy_to_pcm_buffer()`
- [ ] Реализовать sample rate conversion (16kHz → 48kHz)
- [ ] Реализовать channel conversion
- [ ] Реализовать `stop_playback()`
- [ ] Реализовать `shutdown()`

**Тесты**: `tests/test_avfoundation_adapters.py` (output часть)
- [ ] Тест initialize()
- [ ] Тест play_chunk()
- [ ] Тест _numpy_to_pcm_buffer()
- [ ] Тест sample rate conversion
- [ ] Тест channel conversion
- [ ] Тест stop_playback()
- [ ] Тест shutdown()
- [ ] Покрытие ≥80%

---

### День 21: google_input.py

**Файл**: `modules/voice_recognition/core/avfoundation/adapters/google_input.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `GoogleInputController` класс
- [ ] Реализовать `get_microphone()`
- [ ] Реализовать `update_device()`
- [ ] Реализовать `get_current_device()`

**Тесты**: `tests/test_avfoundation_adapters.py` (input часть)
- [ ] Тест get_microphone() с device_index
- [ ] Тест get_microphone() без device_index (system default)
- [ ] Тест update_device()
- [ ] Тест get_current_device()
- [ ] Покрытие ≥80%

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] PyObjC зависимости проверены
- [ ] Code review пройден

---

## 🎯 PR 6: Интеграция (Этап 5)

**Ветка**: `feature/avfoundation-audio-stage5-integration`  
**Дни**: 22-24  
**Файлы**: 1 новый + 1 изменение + интеграционные тесты

### День 22-23: audio_route_manager_integration.py

**Файл**: `integration/integrations/audio_route_manager_integration.py`

**Задачи**:
- [ ] Создать файл
- [ ] Реализовать `AudioRouteManagerIntegration` класс
- [ ] Реализовать `__init__()`
- [ ] Реализовать `initialize()` с feature flags проверкой
- [ ] Реализовать `start()`
- [ ] Реализовать `stop()`
- [ ] Реализовать подписки на события
- [ ] Реализовать `_on_reconcile_requested()`
- [ ] Реализовать `_create_snapshot()`
- [ ] Реализовать `_create_decision_context()`
- [ ] Реализовать `_on_device_changed()`
- [ ] Реализовать `_on_first_run_started()`
- [ ] Реализовать `_on_restart_pending()`
- [ ] Реализовать `_on_update_in_progress()`
- [ ] Реализовать `_on_mode_changed()`
- [ ] Реализовать callbacks (_on_input_start, _on_input_stop, _on_output_recreate)
- [ ] Реализовать `get_active_input_device()`
- [ ] Реализовать `get_active_output_device()`

**Тесты**: `tests/integration/test_audio_route_manager.py`
- [ ] Тест initialize()
- [ ] Тест start()
- [ ] Тест stop()
- [ ] Тест _on_reconcile_requested()
- [ ] Тест _on_device_changed()
- [ ] Интеграционные тесты (happy_path, device_changed, blocking_conditions, fallback)
- [ ] Покрытие ≥80%

---

### День 24: simple_module_coordinator.py

**Файл**: `integration/core/simple_module_coordinator.py`

**Задачи**:
- [ ] Добавить импорт `AudioRouteManagerIntegration`
- [ ] Добавить создание интеграции в `_create_integrations()`
- [ ] Обновить `startup_order` (добавить `'audio_route_manager'` после `'speech_playback'`)
- [ ] Добавить проверку зависимостей (voice_recognition, speech_playback)

**Тесты**: Обновить `tests/test_init_order.py`
- [ ] Тест порядка инициализации с RouteManager
- [ ] Тест зависимостей

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Интеграционные тесты проходят
- [ ] Порядок инициализации корректен
- [ ] Code review пройден

---

## 🎯 PR 7: Адаптация существующих интеграций (Этап 6)

**Ветка**: `feature/avfoundation-audio-stage6-adapt-integrations`  
**Дни**: 25-28  
**Файлы**: 2 изменения + обновление тестов

### День 25-26: voice_recognition_integration.py

**Файл**: `integration/integrations/voice_recognition_integration.py`

**Задачи**:
- [ ] Добавить проверку feature flag `audio_system.avfoundation_route_manager_enabled`
- [ ] Получать `device_index` от RouteManager вместо прямого использования
- [ ] Использовать `GoogleInputController` для получения Microphone
- [ ] Добавить fallback на старую логику (если флаг выключен)
- [ ] Обновить `_on_recording_start()` для использования RouteManager

**Тесты**: Обновить существующие тесты
- [ ] Тест с feature flag включен
- [ ] Тест с feature flag выключен (fallback)
- [ ] Тест получения device_index от RouteManager

---

### День 27-28: speech_playback_integration.py

**Файл**: `integration/integrations/speech_playback_integration.py`

**Задачи**:
- [ ] Добавить проверку feature flag `audio_system.avfoundation_output_enabled`
- [ ] Использовать `AVFoundationAudioPlayback` вместо `sounddevice.OutputStream`
- [ ] Конвертация numpy → AVAudioPCMBuffer
- [ ] Добавить fallback на старую логику (если флаг выключен)
- [ ] Обновить `_on_audio_chunk()` для использования AVFoundation

**Тесты**: Обновить существующие тесты
- [ ] Тест с feature flag включен
- [ ] Тест с feature flag выключен (fallback)
- [ ] Тест конвертации numpy → AVAudioPCMBuffer

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Fallback логика работает
- [ ] Code review пройден

---

## 🎯 PR 8: Адаптация модулей (Этап 7)

**Ветка**: `feature/avfoundation-audio-stage7-adapt-modules`  
**Дни**: 29-32  
**Файлы**: 2 изменения + обновление тестов

### День 29-30: speech_recognizer.py

**Файл**: `modules/voice_recognition/core/speech_recognizer.py`

**Задачи**:
- [ ] Получать `device_index` от RouteManager вместо `AudioDeviceMonitor`
- [ ] Убрать прямые вызовы `sd.default.device`
- [ ] Использовать `GoogleInputController` для получения Microphone
- [ ] Обновить `_run_listening()` для использования RouteManager
- [ ] Сохранить fallback на старую логику (если флаг выключен)

**Тесты**: Обновить существующие тесты
- [ ] Тест с RouteManager
- [ ] Тест fallback на старую логику

---

### День 31-32: player.py

**Файл**: `modules/speech_playback/core/player.py`

**Задачи**:
- [ ] Использовать `AVFoundationAudioPlayback` вместо `sounddevice.OutputStream`
- [ ] Конвертация форматов
- [ ] Сохранить fallback на старую логику (если флаг выключен)
- [ ] Обновить `_start_audio_stream()` для использования AVFoundation

**Тесты**: Обновить существующие тесты
- [ ] Тест с AVFoundation
- [ ] Тест fallback на старую логику

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Тесты проходят
- [ ] Линтер проходит
- [ ] Fallback логика работает
- [ ] Code review пройден

---

## 🎯 PR 9: Gateways, State Catalog, Тестирование (Этапы 8-9)

**Ветка**: `feature/avfoundation-audio-stage8-9-final`  
**Дни**: 33-42  
**Файлы**: 2 изменения + документация + финальные тесты

### День 33-34: gateways.py

**Файл**: `integration/core/gateways.py`

**Задачи**:
- [ ] Добавить функцию `decide_route_manager_reconcile(snapshot: Snapshot) -> Decision`
- [ ] Реализовать правила из `interaction_matrix.yaml`
- [ ] Канонический формат decision-логов

**Тесты**: Обновить `tests/test_gateways.py`
- [ ] Тест decide_route_manager_reconcile()
- [ ] Pairwise тесты (≥12 комбинаций)
- [ ] Негативные тесты (≥2)
- [ ] Проверка decision-логов в каноническом формате

---

### День 35: STATE_CATALOG.md

**Файл**: `Docs/STATE_CATALOG.md`

**Задачи**:
- [ ] Добавить оси `audio.input.device` и `audio.output.device`
- [ ] Обновить таблицу ownership
- [ ] Обновить метрики

---

### День 36-40: Интеграционное тестирование

**Задачи**:
- [ ] Создать `tests/integration/test_audio_route_manager.py`
- [ ] Реализовать все сценарии:
  - [ ] Happy path
  - [ ] Device changed
  - [ ] Blocking conditions
  - [ ] Fallback
  - [ ] Mapping failures
  - [ ] Network offline
  - [ ] Device busy

---

### День 41-42: Документация

**Задачи**:
- [ ] Создать `modules/voice_recognition/core/avfoundation/README.md`
- [ ] Обновить `Docs/AUDIO_SYSTEM_ARCHITECTURE.md`
- [ ] Обновить `modules/voice_recognition/INTEGRATION_GUIDE.md`
- [ ] Обновить `modules/speech_playback/INTEGRATION_GUIDE.md`

---

**PR Checklist**:
- [ ] Все задачи выполнены
- [ ] Все тесты проходят
- [ ] Линтер проходит
- [ ] Документация обновлена
- [ ] Pre-build gate проходит
- [ ] Code review пройден

---

## 📊 Итоговая таблица PR

| PR | Этап | Дни | Файлов | Тестов | Статус |
|----|------|-----|--------|--------|--------|
| PR 1 | Базовые компоненты | 1-4 | 2 новых | 1 новый | ⏳ Ожидает |
| PR 2 | State Machines | 5-8 | 2 новых | Обновление | ⏳ Ожидает |
| PR 3 | Route Manager Core-1 | 9-12 | 2 новых | Обновление | ⏳ Ожидает |
| PR 4 | Route Manager Core-2 | 13-16 | 2 новых | Обновление | ⏳ Ожидает |
| PR 5 | Адаптеры | 17-21 | 3 новых | Обновление | ⏳ Ожидает |
| PR 6 | Интеграция | 22-24 | 1 новый + 1 изменение | 1 новый | ⏳ Ожидает |
| PR 7 | Адаптация интеграций | 25-28 | 2 изменения | Обновление | ⏳ Ожидает |
| PR 8 | Адаптация модулей | 29-32 | 2 изменения | Обновление | ⏳ Ожидает |
| PR 9 | Gateways, Final | 33-42 | 2 изменения + docs | Обновление | ⏳ Ожидает |

**Всего**: 9 PR, 42 дня, 18 новых файлов, 9 изменений

---

## 🚀 Команды для начала работы

### PR 1: Базовые компоненты

```bash
cd /Users/sergiyzasorin/Fix_new/client

# Создать ветку
git checkout -b feature/avfoundation-audio-stage1-contracts-mapping

# Проверить готовность
scripts/prepare_audio_migration.sh
python3 scripts/verify_audio_migration_compliance.py

# Начать реализацию
# День 1-2: contracts.py
# День 3-4: mapping.py
```

---

## ✅ Критерии готовности каждого PR

### Обязательные

- [ ] Все задачи этапа выполнены
- [ ] Тесты проходят (≥80% покрытие)
- [ ] Линтер проходит без ошибок
- [ ] Pre-build gate проходит (для финальных PR)
- [ ] Code review пройден

### Рекомендуемые

- [ ] Документация обновлена
- [ ] Примеры добавлены
- [ ] Интеграционные тесты проходят

---

## 📝 Примечания

1. **Feature flags по умолчанию `false`** - безопасный старт
2. **Каждый PR может быть мержен независимо** (при условии feature flags)
3. **Fallback на старую систему** - если feature flag выключен
4. **Тесты создаются параллельно** - не откладывать на конец
5. **Code review обязателен** - после каждого PR

---

**Этот план служит основой для пошаговой реализации миграции аудиосистемы.**

