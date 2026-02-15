# Карта источников требований Nexy Client

Цель: фиксировать актуальные источники требований, владельцев и статусы без ссылок на удалённые файлы.

## Таблица источников

| Документ | Домен | Owner | Актуальность | Примечание |
|---|---|---|---|---|
| `.cursorrules` | Engineering rules | Tech Lead клиента | ✅ | Базовые правила разработки |
| `Docs/PROJECT_REQUIREMENTS.md` | Snapshot требований | Tech Lead клиента | ✅ | Канонический реестр REQ-* |
| `Docs/ARCHITECTURE_OVERVIEW.md` | Архитектура | Tech Lead клиента | ✅ | Границы слоёв и роли компонентов |
| `Docs/FLOW_INTERACTION_SPEC.md` | Event contracts | Tech Lead клиента | ✅ | Канон payload/event схем |
| `Docs/STATE_CATALOG.md` | State ownership | Tech Lead клиента | ✅ | Оси, владельцы, SoT |
| `config/interaction_matrix.yaml` | State rules | Tech Lead клиента | ✅ | Правила hard_stop/graceful/preference |
| `Docs/first_run_flow_spec.md` | Permissions first-run | Permissions SWAT | ✅ | V2 orchestrator/ledger policy |
| `PERMISSIONS_REPORT.md` | Permissions status | Permissions SWAT | ✅ | Статусы/ограничения по TCC |
| `Docs/FEATURE_FLAGS.md` | Feature flags | Tech Lead клиента | ✅ | Реестр флагов/kill-switches |
| `Docs/PACKAGING_FINAL_GUIDE.md` | Packaging | Release/Delivery | ✅ | Канонический release pipeline |
| `Docs/PRE_PACKAGING_VERIFICATION.md` | Packaging checks | Release/Delivery | ✅ | Детальные pre-packaging проверки |
| `Docs/PACKAGING_READINESS_CHECKLIST.md` | Packaging readiness | Release/Delivery | ✅ | Краткий readiness статус |
| `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md` | Versioning / publish | Release/Delivery | ✅ | Регламент версий и push policy |
| `client/metrics/registry.md` | Metrics/SLO | Tech Lead клиента | ✅ | Базовые метрики и пороги |
| `Docs/README.md` | Documentation index | Tech Lead клиента | ✅ | Master-index документации |
| `Docs/DOCUMENTATION_MAP.md` | Documentation navigation | Tech Lead клиента | ✅ | Навигатор по активным документам |

## Открытые GAP

| ID | Описание | Приоритет | Владелец | Статус |
|---|---|---|---|---|
| GAP-001 | Отсутствует автоматическая проверка битых ссылок в канонических docs | Medium | Tech Lead клиента | Открыто |
| GAP-002 | Есть остаточные legacy-ссылки в отдельных документах и отчётах | Medium | Tech Lead клиента | В работе |

## Домены

- Client Runtime: `.cursorrules`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/STATE_CATALOG.md`, `config/interaction_matrix.yaml`
- Permissions/TCC: `Docs/first_run_flow_spec.md`, `PERMISSIONS_REPORT.md`, `Docs/PROJECT_REQUIREMENTS.md`
- Packaging/Release: `Docs/PACKAGING_FINAL_GUIDE.md`, `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`, `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Observability: `client/metrics/registry.md`

---

Последнее обновление: 2026-02-15
