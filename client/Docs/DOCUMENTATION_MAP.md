# Карта документации Nexy Client

**Цель**: Навигация по всей документации проекта. Показывает связи между документами и их назначение.

**См. также:** `Docs/REQUIREMENTS_SOURCE_MAP.md` — карта источников требований (матрица требований с владельцами и статусами).

---

## 📋 Категории документов

### 1. Источники истины (правила и состояние)

**STATE_CATALOG.md** → `config/interaction_matrix.yaml` → `integration/core/gateways/common.py + integration/core/gateways/permission_gateways.py` → тесты

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `Docs/STATE_CATALOG.md` | Единый источник истины для осей состояния + таблица ownership | `config/interaction_matrix.yaml`, `integration/core/gateways/common.py + integration/core/gateways/permission_gateways.py` |
| `config/interaction_matrix.yaml` | Правила взаимодействия осей с приоритетами | `Docs/STATE_CATALOG.md`, `integration/core/gateways/common.py + integration/core/gateways/permission_gateways.py` |
| `.cursorrules` | Полные правила разработки (раздел 1.1 — источник истины) | Все документы |

### 2. Концептуальные документы

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `Docs/PRODUCT_CONCEPT.md` | Концепция продукта, UX сценарии, 3 режима работы | `Docs/ARCHITECTURE_OVERVIEW.md` |
| `Docs/ARCHITECTURE_OVERVIEW.md` | Обзор архитектуры, роли компонентов, жизненные циклы | `Docs/PRODUCT_CONCEPT.md`, `Docs/STATE_CATALOG.md` |
| `Docs/FLOW_INTERACTION_SPEC.md` | **Канон взаимодействий**: Flow, контракты событий, форматы payload | `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/STATE_CATALOG.md` |
| `Docs/first_run_flow_spec.md` | Спецификация первого запуска и запроса разрешений | `Docs/ARCHITECTURE_OVERVIEW.md`, `PERMISSIONS_REPORT.md` |
| `client/_Docs_ARCHIVED/CURRENT_STATUS_REPORT.md` | Исторический статус релизов (reference) | `.cursorrules`, `Docs/PRE_PACKAGING_VERIFICATION.md` |

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
| `client/metrics/registry.md` | Реестр метрик с SLO порогами | `tests/perf/test_slo.py`, `client/_Docs_ARCHIVED/GLOBAL_DELIVERY_PLAN.md` (reference) |
| `client/_Docs_ARCHIVED/templates/change_impact.yaml` | Исторический шаблон для Impact-гейт (reference) | `.cursorrules` (раздел 11) |
| `client/_Docs_ARCHIVED/templates/ADR_MIN.md` | Исторический шаблон микро-ADR (reference) | `.cursorrules` (раздел 14.7) |

### 6. Packaging & Delivery

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `client/_Docs_ARCHIVED/RELEASE_TESTING_GUIDE.md` | Исторический план тестирования релиза (reference) | `Docs/PACKAGING_FINAL_GUIDE.md` |
| `Docs/PACKAGING_FINAL_GUIDE.md` | Единственная инструкция по сборке .app/PKG, notarization | `.cursorrules` §2, §11.2 |
| `Docs/PRE_PACKAGING_VERIFICATION.md` | Канонический чек-лист и логи готовности перед упаковкой | `Docs/PACKAGING_FINAL_GUIDE.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md` |
| `client/_Docs_ARCHIVED/PREFLIGHT_TEST_GUIDE.md` | Исторический preflight-тест first-run flow (reference) | `Docs/first_run_flow_spec.md` |
| `client/_Docs_ARCHIVED/TESTING_PACKAGED_APP.md` | Исторический гайд тестирования packaged app (reference) | `Docs/PACKAGING_FINAL_GUIDE.md` |
| `Docs/PACKAGING_READINESS_CHECKLIST.md` | Короткое резюме статуса упаковки, указывает на `PRE_PACKAGING_VERIFICATION.md` | `.cursorrules` §11.2 |
| `client/_Docs_ARCHIVED/PACKAGING_VERIFICATION_CHECKLIST.md` | Исторический чек-лист проверки артефактов (reference) | `scripts/verify_packaging_artifacts.sh` |
| `client/_Docs_ARCHIVED/GLOBAL_DELIVERY_PLAN.md` | Исторический rollout plan (reference) | `Docs/PACKAGING_FINAL_GUIDE.md` |
| `client/PERMISSIONS_REPORT.md` | Актуальные статусы TCC, открытые задачи | `Docs/STATE_CATALOG.md`, `client/_Docs_ARCHIVED/TAL_TESTING_CHECKLIST.md` (reference) |

### 7. ADR (Architecture Decision Records)

| Документ | Назначение | Связан с |
|----------|-----------|----------|
| `client/_Docs_ARCHIVED/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md` | Исторический ADR миграции на AVFoundation (reference) | `modules/audio_avf/`, `integration/integrations/` |

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
│         integration/core/gateways/common.py + integration/core/gateways/permission_gateways.py (логика решений)        │
└──────────────────┬──────────────────────────────────────────┘
                   │ тестируется в
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              tests/test_gateways.py (тесты)                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│    client/_Docs_ARCHIVED/PRODUCTION_RULES_SUMMARY.md         │
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

**Правило**: Все правила из `interaction_matrix.yaml` должны быть реализованы в `integration/core/gateways/common.py + integration/core/gateways/permission_gateways.py`.

**Проверка**: См. `tests/test_gateways.py` для проверки соответствия.

---

## 📍 Быстрый навигатор

**Хочу понять что делаем (правила):**
→ `Docs/STATE_CATALOG.md` + `config/interaction_matrix.yaml`

**Хочу понять как делаем (реализация):**
→ `config/interaction_matrix.yaml` (детализация правил)

**Хочу сделать ревью кода:**
→ `.cursorrules` (разделы 11, 17–21)

**Хочу изменить поведение:**
→ `.cursorrules` раздел 11 "Инвариант: изменил поведение? обнови 4 артефакта"

**Хочу понять архитектуру:**
→ `Docs/ARCHITECTURE_OVERVIEW.md` + `Docs/PRODUCT_CONCEPT.md`

**Хочу упаковать приложение:**
→ `Docs/PACKAGING_FINAL_GUIDE.md` (инструкция) + `Docs/PRE_PACKAGING_VERIFICATION.md` (детальный чек-лист) + `Docs/PACKAGING_READINESS_CHECKLIST.md` (резюме статуса)

**Хочу проверить метрики:**
→ `client/metrics/registry.md` + `tests/perf/test_slo.py`

---

## 🗄 Archived (справочные материалы)

Перенесены для сохранения истории; не являются базовыми источниками истины и не должны использоваться в качестве актуальных правил.

С 2025-12-28: исторические планы и отчеты по аудио-миграции перенесены в `Docs/_archive`.
С 2025-01-XX: разовые отчеты и устаревшие документы переносятся в `Docs/_archive`.

- `Docs/_archive/PREFLIGHT_CHECKS.md`
- `Docs/_archive/PREFLIGHT_IMPLEMENTATION_PLAN.md`
- `Docs/_archive/PRE_PACKAGING_VERIFICATION.md`
- `Docs/_archive/PACKAGING_READINESS_CHECKLIST.md`

Для актуальных правил см. `.cursorrules`, `Docs/STATE_CATALOG.md`, `config/interaction_matrix.yaml`.

---

**Владелец**: Tech Lead клиента  
**Последнее обновление**: 2025-01-15
