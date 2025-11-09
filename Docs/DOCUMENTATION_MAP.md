# Карта документации Nexy Client

**Цель**: Навигация по всей документации проекта. Показывает связи между документами и их назначение.

---

## 📋 Категории документов

### 1. Источники истины (правила и состояние)

**STATE_CATALOG.md** → `config/interaction_matrix.yaml` → `integration/core/gateways.py` → тесты

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `Docs/STATE_CATALOG.md` | Единый источник истины для осей состояния + таблица ownership | `config/interaction_matrix.yaml`, `integration/core/gateways.py` |
| `config/interaction_matrix.yaml` | Правила взаимодействия осей с приоритетами | `Docs/STATE_CATALOG.md`, `integration/core/gateways.py` |
<!-- CODE_REVIEW_ASSISTANT_PROMPT.md перенесён в _archive -->
| `.cursorrules` | Полные правила разработки (раздел 1.1 — источник истины) | Все документы |
| `Docs/CODE_REVIEW_ASSISTANT_PROMPT.md` | Промпт для архитектурного ревью (enforcement) | `.cursorrules`, `Docs/STATE_CATALOG.md`, `config/interaction_matrix.yaml` |

### 2. Концептуальные документы

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `Docs/PRODUCT_CONCEPT.md` | Концепция продукта, UX сценарии, 3 режима работы | `Docs/ARCHITECTURE_OVERVIEW.md` |
| `Docs/ARCHITECTURE_OVERVIEW.md` | Обзор архитектуры, роли компонентов, жизненные циклы | `Docs/PRODUCT_CONCEPT.md`, `Docs/STATE_CATALOG.md` |
| `Docs/first_run_flow_spec.md` | Спецификация первого запуска и запроса разрешений | `Docs/ARCHITECTURE_OVERVIEW.md` |

### 3. Планы и процессы

| Документ | Назначение | Связан с |
|----------|-----------|----------|
<!-- GLOBAL_DELIVERY_PLAN.md удалён как временный план -->
| `Docs/first_run_flow_spec.md` | Спецификация первого запуска и запроса разрешений | `Docs/ARCHITECTURE_OVERVIEW.md` |

### 4. Permission Restart (детали реализации)

| Документ | Назначение | Связан с |
|----------|-----------|----------|
<!-- PERMISSION_RESTART_KEY_POINTS.md и PERMISSION_RESTART_BLOCKERS.md перенесены в _archive -->

### 5. Технические артефакты

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `Docs/FEATURE_FLAGS.md` | Карта feature flags/kill-switches → код | `.cursorrules` (раздел 19) |
| `client/metrics/registry.md` | Реестр метрик с SLO порогами | `tests/perf/test_slo.py`, `Docs/GLOBAL_DELIVERY_PLAN.md` |
| `Docs/templates/change_impact.yaml` | Шаблон для Impact-гейт | `.cursorrules` (раздел 11) |
| `Docs/templates/ADR_MIN.md` | Шаблон микро-ADR | `.cursorrules` (раздел 14.7) |

### 6. ADR (Architecture Decision Records)

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `Docs/ADR_PERMISSION_EVENT_RACE_FIX.md` | ADR: исправление race condition в обработке событий разрешений | `integration/core/simple_module_coordinator.py`, `tests/test_coordinator_critical_subscriptions.py` |
| `Docs/change_impact_permission_event_race_fix.yaml` | Change Impact Analysis для race condition fix | `Docs/ADR_PERMISSION_EVENT_RACE_FIX.md` |

---

## 🔗 Связи между документами

```
┌─────────────────────────────────────────────────────────────┐
│                    .cursorrules (правила)                    │
│              Раздел 1.1: Источник истины                     │
└──────────────────┬──────────────────────────────────────────┘
                   │ ссылается на
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              Docs/STATE_CATALOG.md (оси состояния)           │
│              + Таблица ownership                             │
└──────────────────┬──────────────────────────────────────────┘
                   │ синхронизируется с
                   ▼
┌─────────────────────────────────────────────────────────────┐
│          config/interaction_matrix.yaml (правила)            │
└──────────────────┬──────────────────────────────────────────┘
                   │ реализуется в
                   ▼
┌─────────────────────────────────────────────────────────────┐
│         integration/core/gateways.py (логика решений)        │
└──────────────────┬──────────────────────────────────────────┘
                   │ тестируется в
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              tests/test_gateways.py (тесты)                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│         Docs/PRODUCTION_RULES_SUMMARY.md                     │
│          (краткая выжимка правил и артефактов)              │
└──────────────────┬──────────────────────────────────────────┘
                   │ указывает на
                   ▼
┌─────────────────────────────────────────────────────────────┐
│         config/interaction_matrix.yaml (правила restart)     │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Проверка согласованности

### Синхронизация STATE_CATALOG ↔ interaction_matrix

**Правило**: Все оси из `STATE_CATALOG.md` должны присутствовать в `interaction_matrix.yaml` (если влияют на решения).

**Текущие оси в STATE_CATALOG.md**:
- ✅ permissions.mic, permissions.screen, permissions.accessibility
- ✅ device.input, network, firstRun, appMode
- ⚠️ permissions.restart_pending, process.lifecycle (Phase 2 — не в production)

**Текущие оси в interaction_matrix.yaml**:
- ✅ Permission.mic, Permission.screen, Permission.accessibility
- ✅ Device.input, Network, FirstRun, appMode
- ✅ permissions.restart_pending, process.lifecycle (Phase 2)

**Статус**: ✅ Синхронизировано

### Синхронизация interaction_matrix ↔ gateways

**Правило**: Все правила из `interaction_matrix.yaml` должны быть реализованы в `integration/core/gateways.py`.

**Проверка**: См. `tests/test_gateways.py` для проверки соответствия.

---

## 📍 Быстрый навигатор

**Хочу понять что делаем (правила):**
→ `Docs/STATE_CATALOG.md` + `config/interaction_matrix.yaml`

**Хочу понять как делаем (реализация):**
→ `config/interaction_matrix.yaml` (детализация правил)

**Хочу сделать ревью кода:**
→ `.cursorrules` (разделы 11, 17–21) + `Docs/CODE_REVIEW_ASSISTANT_PROMPT.md`

**Хочу изменить поведение:**
→ `.cursorrules` раздел 11 "Инвариант: изменил поведение? обнови 4 артефакта"

**Хочу понять архитектуру:**
→ `Docs/ARCHITECTURE_OVERVIEW.md` + `Docs/PRODUCT_CONCEPT.md`

**Хочу упаковать приложение:**
→ `Docs/PACKAGING_FINAL_GUIDE.md` (единственная инструкция)

**Хочу проверить метрики:**
→ `client/metrics/registry.md` + `tests/perf/test_slo.py`

---

## 🗄 Archived (справочные материалы)

Перенесены для сохранения истории; не являются базовыми источниками истины и не должны использоваться в качестве актуальных правил.

- `Docs/_archive/PERMISSION_RESTART_LOGIC.md`
- `Docs/_archive/PERMISSION_RESTART_AND_ACTIVATION_PROMPT.md`
- `Docs/_archive/PERMISSION_RESTART_ACTIVATION_PROBLEM_PROMPT.md`
- `Docs/_archive/PROMPT_PERMISSION_RESTART_FIX.md`
- `Docs/_archive/PERMISSION_MONITORING_FEATURE.md`
- `Docs/_archive/Video.md`
- `Docs/_archive/NEXY_CLIENT_DEVELOPMENT_RULES.md`

Для актуальных правил см. `.cursorrules`, `Docs/STATE_CATALOG.md`, `config/interaction_matrix.yaml`.

---

**Владелец**: Tech Lead клиента  
**Последнее обновление**: 2025-01-15

