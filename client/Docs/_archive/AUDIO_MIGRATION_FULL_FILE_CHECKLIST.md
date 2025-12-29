# Полный чек-лист файлов для миграции аудиосистемы

**Цель**: Учесть все возможные файлы, которые нужно проверить/изменить при создании и адаптации архитектуры  
**Дата**: 2025-01-XX  
**Статус**: Предварительное планирование

---

## 📋 Категории файлов

### 1. Новые файлы (создать)
### 2. Существующие файлы (изменить)
### 3. Файлы для проверки (зависимости)
### 4. Конфигурационные файлы
### 5. Тестовые файлы
### 6. Документация

---

## 1. Новые файлы (создать)

### 1.1 Core компоненты AVFoundation

| Файл | Путь | Статус | Приоритет | Зависимости |
|------|-----|--------|-----------|-------------|
| `contracts.py` | `modules/voice_recognition/core/avfoundation/contracts.py` | ❌ | Высокий | Нет |
| `mapping.py` | `modules/voice_recognition/core/avfoundation/mapping.py` | ❌ | Высокий | `contracts.py`, `sounddevice` |
| `input_state_machine.py` | `modules/voice_recognition/core/avfoundation/input_state_machine.py` | ❌ | Высокий | `contracts.py` |
| `output_state_machine.py` | `modules/voice_recognition/core/avfoundation/output_state_machine.py` | ❌ | Высокий | `contracts.py` |
| `route_manager.py` | `modules/voice_recognition/core/avfoundation/route_manager.py` | ❌ | Высокий | `contracts.py`, `mapping.py`, state machines |
| `reconcile_engine.py` | `modules/voice_recognition/core/avfoundation/reconcile_engine.py` | ❌ | Высокий | `route_manager.py`, `mapping.py` |
| `decision_engine.py` | `modules/voice_recognition/core/avfoundation/decision_engine.py` | ❌ | Высокий | `route_manager.py`, `interaction_matrix.yaml` |
| `debounce_manager.py` | `modules/voice_recognition/core/avfoundation/debounce_manager.py` | ❌ | Средний | `contracts.py` |

**Всего**: 8 файлов

---

### 1.2 Адаптеры

| Файл | Путь | Статус | Приоритет | Зависимости |
|------|-----|--------|-----------|-------------|
| `avf_monitor.py` | `modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py` | ❌ | Высокий | PyObjC, `contracts.py` |
| `avf_output.py` | `modules/voice_recognition/core/avfoundation/adapters/avf_output.py` | ❌ | Высокий | PyObjC, `contracts.py` |
| `google_input.py` | `modules/voice_recognition/core/avfoundation/adapters/google_input.py` | ❌ | Высокий | `speech_recognition`, `mapping.py` |

**Всего**: 3 файла

---

### 1.3 Интеграции

| Файл | Путь | Статус | Приоритет | Зависимости |
|------|-----|--------|-----------|-------------|
| `audio_route_manager_integration.py` | `integration/integrations/audio_route_manager_integration.py` | ❌ | Высокий | `route_manager.py`, EventBus, StateManager |

**Всего**: 1 файл

---

### 1.4 Тесты

| Файл | Путь | Статус | Приоритет | Зависимости |
|------|-----|--------|-----------|-------------|
| `test_avfoundation_contracts.py` | `tests/test_avfoundation_contracts.py` | ❌ | Средний | `contracts.py` |
| `test_avfoundation_mapping.py` | `tests/test_avfoundation_mapping.py` | ❌ | Средний | `mapping.py` |
| `test_avfoundation_state_machines.py` | `tests/test_avfoundation_state_machines.py` | ❌ | Средний | state machines |
| `test_avfoundation_route_manager.py` | `tests/test_avfoundation_route_manager.py` | ❌ | Высокий | `route_manager.py` |
| `test_audio_route_manager.py` | `tests/integration/test_audio_route_manager.py` | ❌ | Высокий | `audio_route_manager_integration.py` |

**Всего**: 5 файлов

---

### 1.5 Документация

| Файл | Путь | Статус | Приоритет | Зависимости |
|------|-----|--------|-----------|-------------|
| `README.md` | `modules/voice_recognition/core/avfoundation/README.md` | ❌ | Средний | Все компоненты |

**Всего**: 1 файл

---

**ИТОГО новых файлов**: 18 файлов

---

## 2. Существующие файлы (изменить)

### 2.1 Интеграции (критично)

| Файл | Путь | Статус | Что изменить | Приоритет | Зависимости |
|------|-----|--------|--------------|-----------|-------------|
| `voice_recognition_integration.py` | `integration/integrations/voice_recognition_integration.py` | ✅ | Добавить проверку feature flag, делегирование RouteManager, fallback | Высокий | `audio_route_manager_integration.py` |
| `speech_playback_integration.py` | `integration/integrations/speech_playback_integration.py` | ✅ | Добавить проверку feature flag, использование AVFoundationAudioPlayback, конвертацию numpy → AVAudioPCMBuffer | Высокий | `avf_output.py` |
| `simple_module_coordinator.py` | `integration/core/simple_module_coordinator.py` | ✅ | Добавить создание `AudioRouteManagerIntegration`, обновить `startup_order` | Высокий | `audio_route_manager_integration.py` |

**Всего**: 3 файла

---

### 2.2 Модули (адаптация)

| Файл | Путь | Статус | Что изменить | Приоритет | Зависимости |
|------|-----|--------|--------------|-----------|-------------|
| `speech_recognizer.py` | `modules/voice_recognition/core/speech_recognizer.py` | ✅ | Получать device_index от RouteManager вместо AudioDeviceMonitor, убрать прямые вызовы `sd.default.device` | Высокий | `google_input.py`, `route_manager.py` |
| `player.py` | `modules/speech_playback/core/player.py` | ✅ | Использовать AVFoundationAudioPlayback вместо `sounddevice.OutputStream`, конвертация форматов | Высокий | `avf_output.py` |
| `audio_device_monitor.py` | `modules/voice_recognition/core/audio_device_monitor.py` | ⚠️ | **ОСТАВИТЬ** для fallback, добавить проверку feature flag | Средний | Нет |
| `audio_recovery_manager.py` | `modules/voice_recognition/core/audio_recovery_manager.py` | ✅ | Интегрировать с RouteManager, использовать новые события | Средний | `route_manager.py` |

**Всего**: 4 файла

---

### 2.3 Workflows (проверка)

| Файл | Путь | Статус | Что изменить | Приоритет | Зависимости |
|------|-----|--------|--------------|-----------|-------------|
| `listening_workflow.py` | `integration/workflows/listening_workflow.py` | ✅ | Проверить совместимость событий, возможно добавить события RouteManager | Низкий | EventBus события |
| `processing_workflow.py` | `integration/workflows/processing_workflow.py` | ✅ | Проверить совместимость событий | Низкий | EventBus события |

**Всего**: 2 файла

---

**ИТОГО файлов для изменения**: 9 файлов

---

## 3. Файлы для проверки (зависимости)

### 3.1 Интеграции (проверка совместимости)

| Файл | Путь | Статус | Что проверить | Приоритет |
|------|-----|--------|---------------|-----------|
| `input_processing_integration.py` | `integration/integrations/input_processing_integration.py` | ✅ | Совместимость событий `voice.recording_start/stop` | Низкий |
| `mode_management_integration.py` | `integration/integrations/mode_management_integration.py` | ✅ | Совместимость событий `app.mode_changed` | Низкий |
| `tray_controller_integration.py` | `integration/integrations/tray_controller_integration.py` | ✅ | Совместимость событий `microphone.started/stopped` | Низкий |
| `interrupt_management_integration.py` | `integration/integrations/interrupt_management_integration.py` | ✅ | Совместимость событий `playback.cancelled` | Низкий |
| `permission_restart_integration.py` | `integration/integrations/permission_restart_integration.py` | ✅ | Блокировка RouteManager во время restart | Средний |
| `first_run_permissions_integration.py` | `integration/integrations/first_run_permissions_integration.py` | ✅ | Блокировка RouteManager во время first_run | Средний |
| `updater_integration.py` | `integration/integrations/updater_integration.py` | ✅ | Блокировка RouteManager во время update | Средний |

**Всего**: 7 файлов

---

### 3.2 Core компоненты (проверка зависимостей)

| Файл | Путь | Статус | Что проверить | Приоритет |
|------|-----|--------|---------------|-----------|
| `event_bus.py` | `integration/core/event_bus.py` | ✅ | Поддержка новых событий RouteManager | Низкий |
| `state_manager.py` | `integration/core/state_manager.py` | ✅ | Новые оси состояния (audio.input.device, audio.output.device) | Средний |
| `selectors.py` | `integration/core/selectors.py` | ✅ | Новые селекторы для audio устройств | Средний |
| `gateways.py` | `integration/core/gateways.py` | ✅ | Новый gateway `decide_route_manager_reconcile` | Высокий |
| `error_handler.py` | `integration/core/error_handler.py` | ✅ | Новые коды ошибок для RouteManager | Низкий |

**Всего**: 5 файлов

---

### 3.3 Модули (проверка совместимости)

| Файл | Путь | Статус | Что проверить | Приоритет |
|------|-----|--------|---------------|-----------|
| `types.py` | `modules/voice_recognition/core/types.py` | ✅ | Совместимость типов с новыми contracts | Низкий |
| `device_selector.py` | `modules/voice_recognition/utils/device_selector.py` | ✅ | Совместимость с новым mapping | Низкий |
| `audio_utils.py` | `modules/voice_recognition/utils/audio_utils.py` | ✅ | Совместимость утилит | Низкий |
| `core_audio.py` | `modules/speech_playback/macos/core_audio.py` | ✅ | Совместимость с AVFoundation | Низкий |
| `performance.py` | `modules/speech_playback/macos/performance.py` | ✅ | Совместимость метрик | Низкий |
| `security.py` | `modules/speech_playback/macos/security.py` | ✅ | Совместимость entitlements | Низкий |

**Всего**: 6 файлов

---

**ИТОГО файлов для проверки**: 18 файлов

---

## 4. Конфигурационные файлы

### 4.1 Основные конфигурации

| Файл | Путь | Статус | Что изменить | Приоритет |
|------|-----|--------|--------------|-----------|
| `unified_config.yaml` | `config/unified_config.yaml` | ✅ | Добавить секцию `audio_system` (уже добавлено) | Высокий |
| `interaction_matrix.yaml` | `config/interaction_matrix.yaml` | ✅ | Добавить правила RouteManager (уже добавлено) | Высокий |
| `FEATURE_FLAGS.md` | `Docs/FEATURE_FLAGS.md` | ✅ | Зарегистрировать feature flags (уже добавлено) | Высокий |
| `registry.md` | `client/metrics/registry.md` | ✅ | Добавить метрики RouteManager (уже добавлено) | Высокий |

**Всего**: 4 файла (все уже обновлены)

---

### 4.2 Схемы конфигурации

| Файл | Путь | Статус | Что изменить | Приоритет |
|------|-----|--------|--------------|-----------|
| `config_schema.yaml` | `config/schemas/config_schema.yaml` | ⚠️ | Добавить схему для `audio_system` | Средний |
| `interaction_matrix_schema.yaml` | `config/schemas/interaction_matrix_schema.yaml` | ⚠️ | Проверить совместимость с новыми правилами | Средний |

**Всего**: 2 файла

---

### 4.3 Packaging конфигурации

| Файл | Путь | Статус | Что проверить | Приоритет |
|------|-----|--------|---------------|-----------|
| `entitlements.plist` | `packaging/entitlements.plist` | ✅ | Проверить, что AVFoundation не требует новых entitlements | Средний |
| `Info.plist` | `packaging/Info.plist` | ✅ | Проверить NSMicrophoneUsageDescription | Низкий |
| `requirements.txt` | `requirements.txt` | ✅ | Проверить наличие PyObjC | Низкий |
| `pyproject.toml` | `pyproject.toml` | ✅ | Проверить зависимости, линтеры | Низкий |

**Всего**: 4 файла

---

**ИТОГО конфигурационных файлов**: 10 файлов

---

## 5. Тестовые файлы (существующие)

### 5.1 Интеграционные тесты

| Файл | Путь | Статус | Что проверить/изменить | Приоритет |
|------|-----|--------|------------------------|-----------|
| `test_interrupt_playback.py` | `tests/test_interrupt_playback.py` | ✅ | Совместимость с новым AVFoundation output | Низкий |

**Всего**: 1 файл

---

### 5.2 Диагностические скрипты

| Файл | Путь | Статус | Что проверить/изменить | Приоритет |
|------|-----|--------|------------------------|-----------|
| `run_diagnostics.py` | `run_diagnostics.py` | ✅ | Добавить диагностику RouteManager | Низкий |
| `diagnostic_audio_device_manager.py` | `diagnostic_audio_device_manager.py` | ✅ | Адаптировать под AVFoundation | Низкий |
| `diagnostic_voice_recognition.py` | `diagnostic_voice_recognition.py` | ✅ | Адаптировать под RouteManager | Низкий |
| `diagnostic_speech_playback.py` | `diagnostic_speech_playback.py` | ✅ | Адаптировать под AVFoundation | Низкий |

**Всего**: 4 файла

---

**ИТОГО тестовых файлов**: 5 файлов

---

## 6. Документация

### 6.1 Архитектурная документация

| Файл | Путь | Статус | Что изменить | Приоритет |
|------|-----|--------|--------------|-----------|
| `AUDIO_SYSTEM_ARCHITECTURE.md` | `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` | ✅ | Обновить под новую архитектуру | Средний |
| `AVFOUNDATION_AUDIO_ARCHITECTURE_PROPOSAL.md` | `Docs/AVFOUNDATION_AUDIO_ARCHITECTURE_PROPOSAL.md` | ✅ | Обновить под финальную архитектуру | Средний |
| `STATE_CATALOG.md` | `Docs/STATE_CATALOG.md` | ✅ | Добавить новые оси состояния (audio.input.device, audio.output.device) | Высокий |
| `PROJECT_REQUIREMENTS.md` | `Docs/PROJECT_REQUIREMENTS.md` | ✅ | Обновить требования для RouteManager | Средний |

**Всего**: 4 файла

---

### 6.2 Руководства по интеграции

| Файл | Путь | Статус | Что изменить | Приоритет |
|------|-----|--------|--------------|-----------|
| `INTEGRATION_GUIDE.md` | `modules/voice_recognition/INTEGRATION_GUIDE.md` | ✅ | Обновить под RouteManager | Средний |
| `INTEGRATION_GUIDE.md` | `modules/speech_playback/INTEGRATION_GUIDE.md` | ✅ | Обновить под AVFoundation | Средний |
| `MACOS_PACKAGING_GUIDE.md` | `modules/speech_playback/MACOS_PACKAGING_GUIDE.md` | ✅ | Проверить entitlements для AVFoundation | Низкий |

**Всего**: 3 файла

---

**ИТОГО документации**: 7 файлов

---

## 📊 Итоговая статистика

| Категория | Количество файлов | Статус |
|-----------|------------------|--------|
| **Новые файлы** | 18 | ❌ Не созданы |
| **Файлы для изменения** | 9 | ⚠️ Частично готовы |
| **Файлы для проверки** | 18 | ✅ Существуют |
| **Конфигурационные файлы** | 10 | ✅ Большинство обновлено |
| **Тестовые файлы** | 5 | ✅ Существуют |
| **Документация** | 7 | ✅ Существует |
| **ИТОГО** | **67 файлов** | |

---

## 🎯 Приоритизация

### Критично (начать первым)

1. ✅ Конфигурация (`unified_config.yaml`, `interaction_matrix.yaml`, `FEATURE_FLAGS.md`, `registry.md`)
2. ❌ `contracts.py` - базовые типы
3. ❌ `mapping.py` - маппинг устройств
4. ❌ `route_manager.py` - основная логика
5. ❌ `audio_route_manager_integration.py` - интеграция с EventBus
6. ✅ `simple_module_coordinator.py` - добавить RouteManager
7. ⚠️ `voice_recognition_integration.py` - адаптация
8. ⚠️ `speech_playback_integration.py` - адаптация

### Важно (после критичных)

9. ❌ State machines (`input_state_machine.py`, `output_state_machine.py`)
10. ❌ Адаптеры (`avf_monitor.py`, `avf_output.py`, `google_input.py`)
11. ⚠️ `speech_recognizer.py` - адаптация
12. ⚠️ `player.py` - адаптация
13. ✅ `gateways.py` - добавить `decide_route_manager_reconcile`
14. ✅ `STATE_CATALOG.md` - добавить новые оси

### Желательно (после важных)

15. ❌ Тесты (5 файлов)
16. ⚠️ `audio_recovery_manager.py` - интеграция
17. ⚠️ Workflows - проверка совместимости
18. ⚠️ Документация - обновление

---

## 🔍 Детальный анализ зависимостей

### Зависимости новых компонентов

```
contracts.py
  └─ Нет зависимостей

mapping.py
  ├─ contracts.py
  └─ sounddevice

input_state_machine.py
  └─ contracts.py

output_state_machine.py
  └─ contracts.py

route_manager.py
  ├─ contracts.py
  ├─ mapping.py
  ├─ input_state_machine.py
  └─ output_state_machine.py

reconcile_engine.py
  ├─ route_manager.py
  └─ mapping.py

decision_engine.py
  ├─ route_manager.py
  └─ interaction_matrix.yaml

debounce_manager.py
  └─ contracts.py

avf_monitor.py
  ├─ PyObjC
  └─ contracts.py

avf_output.py
  ├─ PyObjC
  └─ contracts.py

google_input.py
  ├─ speech_recognition
  └─ mapping.py

audio_route_manager_integration.py
  ├─ route_manager.py
  ├─ EventBus
  ├─ StateManager
  └─ ErrorHandler
```

---

## ✅ Чек-лист проверки перед началом реализации

### Подготовка

- [x] Конфигурация создана (`unified_config.yaml`)
- [x] Feature flags зарегистрированы (`FEATURE_FLAGS.md`)
- [x] Метрики добавлены (`registry.md`)
- [x] Правила добавлены (`interaction_matrix.yaml`)
- [x] ADR создан
- [x] Change Impact создан
- [x] Структура директорий создана

### Реализация (порядок)

- [ ] `contracts.py` - базовые типы
- [ ] `mapping.py` - маппинг устройств
- [ ] `input_state_machine.py` - State Machine для input
- [ ] `output_state_machine.py` - State Machine для output
- [ ] `debounce_manager.py` - Debounce логика
- [ ] `decision_engine.py` - Decision логика
- [ ] `reconcile_engine.py` - Reconcile логика
- [ ] `route_manager.py` - Основной RouteManager
- [ ] `avf_monitor.py` - AVFoundation мониторинг
- [ ] `avf_output.py` - AVFoundation output
- [ ] `google_input.py` - Google Input адаптер
- [ ] `audio_route_manager_integration.py` - Интеграция
- [ ] Обновить `simple_module_coordinator.py`
- [ ] Адаптировать `voice_recognition_integration.py`
- [ ] Адаптировать `speech_playback_integration.py`
- [ ] Адаптировать `speech_recognizer.py`
- [ ] Адаптировать `player.py`
- [ ] Обновить `gateways.py`
- [ ] Обновить `STATE_CATALOG.md`

### Тестирование

- [ ] Unit тесты для contracts
- [ ] Unit тесты для mapping
- [ ] Unit тесты для state machines
- [ ] Unit тесты для route_manager
- [ ] Integration тесты для RouteManager
- [ ] Pairwise тесты (≥12 комбинаций)
- [ ] Негативные тесты (≥2)

### Документация

- [ ] README для avfoundation модуля
- [ ] Обновить `AUDIO_SYSTEM_ARCHITECTURE.md`
- [ ] Обновить `INTEGRATION_GUIDE.md` для voice_recognition
- [ ] Обновить `INTEGRATION_GUIDE.md` для speech_playback

---

## 📝 Примечания

1. **Все feature flags по умолчанию `false`** - безопасный старт
2. **Kill-switches готовы** - мгновенный откат возможен
3. **Fallback на старую систему** - если feature flag выключен или kill-switch активен
4. **Порядок реализации критичен** - начинать с `contracts.py`, затем `mapping.py`, затем остальные
5. **Тесты создавать параллельно** - не откладывать на конец

---

## 🎯 Итог

**Всего файлов для учета**: 67 файлов

- **18 новых** - нужно создать
- **9 изменений** - нужно адаптировать
- **18 проверок** - проверить совместимость
- **10 конфигураций** - большинство уже обновлено
- **5 тестов** - адаптировать существующие
- **7 документации** - обновить

**Текущий прогресс**: ~15% (конфигурация готова, структура создана)

**Следующий шаг**: Начать реализацию с `contracts.py`

