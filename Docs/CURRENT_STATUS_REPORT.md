# Nexy Client — Current Status Report

**Дата обновления:** 2025-01-15  
**Контакты:** Tech Lead клиента (@nexy-client-core)

---

## 1. Выпуск: где мы находимся

| Канал | Статус | Комментарий / источники |
|-------|--------|-------------------------|
| Dev (CLI) | ✅ активен | Все интеграции инициализируются без ошибок (`Docs/COMPREHENSIVE_CHECK_2025-01-08.md`). |
| Beta (подписанный `.app`) | ✅ сборка протестирована | `Docs/PRE_PACKAGING_VERIFICATION.md` + `Docs/PACKAGING_READINESS_CHECKLIST.md` фиксируют полный проход чек-листа. |
| Production rollout | ⏳ готовим контрольный список | Сборка/нотаризация готовы; ждём утверждения по `GLOBAL_DELIVERY_PLAN.md`. |

---

## 2. Ключевые возможности

| Возможность | Статус | Источник истины | Комментарий |
|-------------|--------|-----------------|-------------|
| First‑Run Permissions Flow | ✅ Работает энд‑ту‑энд | `Docs/first_run_flow_spec.md`, `integration/integrations/first_run_permissions_integration.py` | Автоматический перезапуск после выдачи прав, флаги в `~/Library/Application Support/Nexy`. |
| Permission Restart & TAL | ✅ Исправлено, тесты в green | `Docs/TAL_TESTING_CHECKLIST.md`, `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md` | TAL hold обновляется каждые 30 с, timeout увеличен до 120 с, сценарии happy/fatal покрыты. |
| Tray / Application termination guard | ✅ Готово | `Docs/TRAY_TERMINATION_FIX.md`, `Docs/PRE_PACKAGING_VERIFICATION.md` | `applicationShouldTerminate()` now returns `False`, quit handler настроен до `app.run()`. |
| Packaging / Notarization | ✅ Process locked | `Docs/PACKAGING_FINAL_GUIDE.md`, `Docs/PRE_PACKAGING_VERIFICATION.md` | PyInstaller → pkgbuild/productbuild → notarization dry-run прошли, см. логи в `rebuild_logs/`. |
| Audio pipeline & playback | ✅ Stable | `Docs/COMPREHENSIVE_CHECK_2025-01-08.md`, `Docs/PLAYBACK_LOGIC_CHECK.md` | Lazy start/stop работает, Bluetooth (AirPods) подтверждён. |
| Voice recognition | ✅ baseline | `modules/voice_recognition/core/*`, `Docs/LOG_ANALYSIS_2025-01-08.md` | Нет регрессий в логах, EventBus события `voice.recognition.*` публикуются. |

---

## 3. Оставшиеся риски / TODO

| ID | Описание | Priority | Владелец | Источники |
|----|----------|----------|----------|-----------|
| TCC-AX-001 | Перевести проверку Accessibility с приватного `TCCAccessRequest` на публичный API | High | Permissions SWAT | `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md` §3 |
| AUDIO-035 | Уточнить debounce/ retry для HAL Error 35 (редко, но всплывает в логах) | Medium | Audio | `Docs/AUDIO_ISSUES_ANALYSIS.md`, `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md` |
| DELIVERY-002 | Зафиксировать Azure/AppCast шаги в новом `GLOBAL_DELIVERY_PLAN.md` | Medium | Release | `Docs/GLOBAL_DELIVERY_PLAN.md` (требует актуализации) |

---

## 4. Проверки и метрики

- ✅ `Docs/COMPREHENSIVE_CHECK_2025-01-08.md` — green (инициализация, EventBus, режимы, Bluetooth playback).
- ✅ `scripts/test_tray_termination.py`, `scripts/test_critical_paths.py`, `scripts/test_tal_assertion.py` — последний прогон см. `Docs/PRE_PACKAGING_VERIFICATION.md`.
- ✅ Machine checks: `scripts/validate_schemas.py`, `scripts/verify_no_direct_state_access.py`, `scripts/verify_rule_coverage.py` — включены в CI (`.github/workflows/ci.yml`).
- ✅ Packaging Regression Checklist (см. `.cursorrules §11.2`) — заполнен, логи в `rebuild_logs/`.
- 🔄 Мониторинг метрик (`client/metrics/registry.md`) — SLO в норме, но требует обновления при появлении новых доменов.

---

## 5. Что изменилось с прошлого отчёта

- **Этап 1 нормализации требований (RELEASE_INTEGRITY_PLAN) завершён**:
  - Создан `Docs/PROJECT_REQUIREMENTS.md` — единый snapshot требований (req_version 2025.02)
  - Создан `Docs/REQUIREMENTS_SOURCE_MAP.md` — карта всех документов требований с их статусом
  - Добавлены скрипты: `scripts/update_requirements_snapshot.py`, `scripts/check_requirements_mapping.py`
  - Обновлён `client/VERSION_INFO.json` с req_version и checksum
  - Обновлён `.cursorrules` с процессом обновления требований (раздел 11.3)
- **Этап 2 Pre-build gate (RELEASE_INTEGRITY_PLAN) завершён**:
  - Создан `scripts/pre_build_gate.sh` — единый скрипт для всех обязательных проверок перед сборкой
  - Обновлён `.github/workflows/ci.yml` — добавлен job `pre-build-gate` для автоматической проверки в CI
  - Pre-build gate включает: линтеры, unit-тесты, статические проверки, специализированные проверки (TAL, permissions, updater)
  - Обновлён `.cursorrules` с процессом pre-build gate (раздел 11.4)
- Консолидация TAL документации → `Docs/TAL_TESTING_CHECKLIST.md` (вместо 5 разных файлов).
- Добавлен Packaging Readiness summary, теперь статус перед релизом фиксируется в одном месте.
- Убраны дублирующие скрипты схем (только `scripts/validate_schemas.py`).

---

## 6. Следующие шаги

1. **RELEASE_INTEGRITY_PLAN этап 3**: Реализовать Release Suite (интеграционный цикл) — сборка dev-билда, headless запуск, критические интеграционные тесты.
2. Закрыть TCC-AX-001 (обновить интеграцию + добавить тесты) до следующего релиза.
3. Заполнить `Docs/GLOBAL_DELIVERY_PLAN.md` деталями по Azure/AppCast rollout и согласовать с Ops.
4. Освежить этот отчёт после следующего полного прогона `rebuild_from_scratch.sh` и TAL чек-листа.

---

**Примечание:** Этот файл — оперативный источник статуса. Все структурные правила и инварианты по-прежнему берём из `.cursorrules`, `Docs/STATE_CATALOG.md`, `Docs/PROJECT_REQUIREMENTS.md` и `Docs/PACKAGING_FINAL_GUIDE.md`.
