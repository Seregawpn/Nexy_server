# Карта источников требований Nexy Client

**Цель**: Таблица всех документов, описывающих требования к проекту, с их статусом, областью ответственности и владельцами.

**Дата создания**: 2025-01-30  
**Версия**: 1.0  
**Владелец**: Tech Lead клиента

---

## Таблица документов

| Документ | Домен | Owner | Актуальность | Замечания / GAP'ы |
|----------|-------|-------|--------------|-------------------|
| `.cursorrules` | Все домены (правила разработки) | Tech Lead клиента | ✅ Актуален | Единый источник правил разработки, раздел 1.1 — источник истины для TCC/First-Run/Restart |
| `Docs/STATE_CATALOG.md` | Состояние системы (оси) | Tech Lead клиента | ✅ Актуален | Единый источник истины для осей состояния, таблица ownership |
| `config/interaction_matrix.yaml` | Правила взаимодействия осей | Tech Lead клиента | ✅ Актуален | Правила взаимодействия осей с приоритетами (hard_stop/graceful/preference) |
| `Docs/PRODUCT_CONCEPT.md` | UX, пользовательские сценарии | Product Owner | ✅ Актуален | Концепция продукта, 3 режима работы, UX сценарии |
| `Docs/ARCHITECTURE_OVERVIEW.md` | Архитектура, связи модулей | Tech Lead клиента | ✅ Актуален | Обзор архитектуры, роли компонентов, жизненные циклы |
| `Docs/first_run_flow_spec.md` | First-run, разрешения | Permissions SWAT | ✅ Актуален | Детальная логика запроса разрешений и перезапуска |
| `PERMISSIONS_REPORT.md` | TCC, разрешения | Permissions SWAT | ✅ Актуален | Актуальные статусы TCC, открытые задачи |
| `Docs/TAL_TESTING_CHECKLIST.md` | TAL, permission restart | Permissions SWAT | ✅ Актуален | Чек-лист TAL/permission restart с логами и тестами |
| `Docs/PACKAGING_FINAL_GUIDE.md` | Packaging, сборка | Release/Delivery | ✅ Актуален | Единственная инструкция по сборке .app/PKG, notarization |
| `Docs/PRE_PACKAGING_VERIFICATION.md` | Packaging, проверки | Release/Delivery | ✅ Актуален | Детальный чек-лист готовности перед упаковкой |
| `Docs/PACKAGING_READINESS_CHECKLIST.md` | Packaging, статус | Release/Delivery | ✅ Актуален | Короткое резюме статуса упаковки |
| `Docs/GLOBAL_DELIVERY_PLAN.md` | Deployment, rollout | Release/Delivery | ⚠️ Требует обновления | Фазы rollout, Azure/AppCast (DELIVERY-002: зафиксировать детали) |
| `Docs/CURRENT_STATUS_REPORT.md` | Статус релизов | Tech Lead клиента | ✅ Актуален | Живой статус релизов, критичные риски, тесты |
| `Docs/FEATURE_FLAGS.md` | Feature flags, kill-switches | Tech Lead клиента | ✅ Актуален | Карта feature flags/kill-switches → код |
| `client/metrics/registry.md` | Метрики, SLO | Tech Lead клиента | ✅ Актуален | Реестр метрик с SLO порогами |
| `Docs/DOCUMENTATION_MAP.md` | Навигация по документации | Tech Lead клиента | ✅ Актуален | Карта всей документации проекта, связи между документами |
| `Docs/PRODUCTION_RULES_SUMMARY.md` | Правила продакшн-уровня | Tech Lead клиента | ✅ Актуален | Краткое резюме правил уровня продакшн |
| `Docs/SERVER_PROTOBUF_SPECIFICATION.md` | gRPC, протокол | gRPC Service Owner | ✅ Актуален | Спецификация protobuf для gRPC |
| `Docs/templates/change_impact.yaml` | Impact-гейт | Tech Lead клиента | ✅ Актуален | Шаблон для Impact-гейт (обязателен для изменений >2 осей) |
| `Docs/templates/ADR_MIN.md` | ADR | Tech Lead клиента | ✅ Актуален | Шаблон микро-ADR |
| `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md` | TAL, exit handler | Permissions SWAT | ✅ Актуален | Анализ проблемы exit handler, TAL hold |
| `Docs/RESTART_AFTER_PERMISSIONS_ISSUE_ANALYSIS.md` | Permission restart | Permissions SWAT | ✅ Актуален | Анализ проблемы перезапуска после разрешений |
| `Docs/TRAY_TERMINATION_FIX.md` | Tray, termination | Tray Controller Owner | ✅ Актуален | Исправление проблемы termination guard |
| `Docs/COMPREHENSIVE_CHECK_2025-01-08.md` | Тестирование | QA | ✅ Актуален | Комплексная проверка инициализации, EventBus, режимов |
| `Docs/CRITICAL_PATHS_TEST_REPORT.md` | Тестирование | QA | ✅ Актуален | Отчёт по критическим путям тестирования |
| `Docs/AUDIO_ISSUES_ANALYSIS.md` | Аудио | Audio Owner | ✅ Актуален | Анализ проблем аудио |
| `Docs/AUDIO_FIXES_SUMMARY.md` | Аудио | Audio Owner | ✅ Актуален | Резюме исправлений аудио |
| `Docs/BLUETOOTH_FIX_SUMMARY.md` | Аудио, Bluetooth | Audio Owner | ✅ Актуален | Исправление проблемы Bluetooth |
| `Docs/PLAYBACK_LOGIC_CHECK.md` | Аудио, playback | Audio Owner | ✅ Актуален | Проверка логики воспроизведения |
| `Docs/TERMINAL_VS_APP_BUNDLE_DIFFERENCES.md` | Packaging, различия | Release/Delivery | ✅ Актуален | Различия между терминалом и .app bundle |
| `Docs/APP_BUNDLE_EXIT_ISSUE.md` | Packaging, exit | Release/Delivery | ✅ Актуален | Анализ проблемы exit в .app bundle |

---

## Критичные GAP'ы

| ID | Описание | Приоритет | Владелец | Статус |
|----|----------|-----------|----------|--------|
| GAP-001 | `Docs/GLOBAL_DELIVERY_PLAN.md` требует детализации Azure/AppCast rollout | Medium | Release/Delivery | Открыто (DELIVERY-002) |
| GAP-002 | Отсутствует единый snapshot требований (`PROJECT_REQUIREMENTS.md`) | High | Tech Lead клиента | В работе (этап 1 нормализации) |
| GAP-003 | Отсутствует привязка требований к реализации и тестам | High | Tech Lead клиента | В работе (этап 1 нормализации) |

---

## Домены требований

### Client Runtime
- **Документы**: `.cursorrules`, `Docs/STATE_CATALOG.md`, `config/interaction_matrix.yaml`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PRODUCT_CONCEPT.md`
- **Владелец**: Tech Lead клиента
- **Статус**: ✅ Актуален

### Permissions/TCC
- **Документы**: `Docs/first_run_flow_spec.md`, `PERMISSIONS_REPORT.md`, `Docs/TAL_TESTING_CHECKLIST.md`, `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md`, `Docs/RESTART_AFTER_PERMISSIONS_ISSUE_ANALYSIS.md`
- **Владелец**: Permissions SWAT
- **Статус**: ✅ Актуален (кроме TCC-AX-001: замена приватного API)

### Packaging
- **Документы**: `Docs/PACKAGING_FINAL_GUIDE.md`, `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`, `Docs/TERMINAL_VS_APP_BUNDLE_DIFFERENCES.md`, `Docs/APP_BUNDLE_EXIT_ISSUE.md`
- **Владелец**: Release/Delivery
- **Статус**: ✅ Актуален

### Deployment
- **Документы**: `Docs/GLOBAL_DELIVERY_PLAN.md`
- **Владелец**: Release/Delivery
- **Статус**: ⚠️ Требует обновления (GAP-001)

### Testing/QA
- **Документы**: `Docs/COMPREHENSIVE_CHECK_2025-01-08.md`, `Docs/CRITICAL_PATHS_TEST_REPORT.md`, `Docs/TAL_TESTING_CHECKLIST.md`
- **Владелец**: QA
- **Статус**: ✅ Актуален

### Audio
- **Документы**: `Docs/AUDIO_ISSUES_ANALYSIS.md`, `Docs/AUDIO_FIXES_SUMMARY.md`, `Docs/BLUETOOTH_FIX_SUMMARY.md`, `Docs/PLAYBACK_LOGIC_CHECK.md`
- **Владелец**: Audio Owner
- **Статус**: ✅ Актуален

### Feature Flags & Metrics
- **Документы**: `Docs/FEATURE_FLAGS.md`, `client/metrics/registry.md`
- **Владелец**: Tech Lead клиента
- **Статус**: ✅ Актуален

### gRPC/Protocol
- **Документы**: `Docs/SERVER_PROTOBUF_SPECIFICATION.md`
- **Владелец**: gRPC Service Owner
- **Статус**: ✅ Актуален

---

## Процесс обновления

1. **При обнаружении нового документа требований**: добавить в таблицу с указанием домена, владельца и статуса
2. **При изменении документа**: обновить статус актуальности и замечания
3. **При обнаружении GAP'а**: добавить в раздел "Критичные GAP'ы" с приоритетом и владельцем
4. **Регулярная ревизия**: еженедельный sync для проверки актуальности всех документов

---

**Последнее обновление**: 2025-01-30  
**Следующая ревизия**: 2025-02-06

