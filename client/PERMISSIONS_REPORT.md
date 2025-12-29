# Nexy Client — Permissions & TCC Report

**Последнее обновление:** 2025-01-15  
**Владелец:** Permissions SWAT (FirstRun + PermissionRestart)

---

## 1. Обзор

- macOS privacy permissions закрываются в рамках `FirstRunPermissionsIntegration` + `PermissionRestartIntegration`.  
- TAL/TCC рестарт после выдачи прав подтверждён (`Docs/TAL_TESTING_CHECKLIST.md`).  
- Состояние и события описаны в `Docs/STATE_CATALOG.md` (оси `permissions.mic`, `permissions.screen`, `permissions.accessibility`, `permissions.first_run`).  
- Этот отчёт фиксирует текущее состояние, последние проверки и открытые действия.

---

## 2. Текущее состояние по разрешениям

| Permission | Интеграция / модуль | Статус (2025‑01‑15) | Проверено | Источник |
|------------|--------------------|---------------------|-----------|----------|
| Microphone (TCC) | `FirstRunPermissionsIntegration`, `modules/voice_recognition` | ✅ granted (beta devices) | `scripts/test_first_run_integration.sh` (см. воспроизведение) | `Docs/first_run_flow_spec.md` |
| Screen Capture | `modules/screenshot_capture`, first-run flow | ✅ granted | Manual checklist (PRE_PACKAGING_VERIFICATION) | `Docs/PRE_PACKAGING_VERIFICATION.md` |
| Accessibility | `modules/permissions/macos/accessibility_handler.py` | ✅ granted, используется публичный API `AXIsProcessTrustedWithOptions` | `modules/permissions/macos/accessibility_handler.py:23-52` | ✅ Исправлено (2025-01-15) |
| Input Monitoring | `FirstRunPermissionsIntegration` | ✅ not required post v2 (read-only) | First-run spec | `Docs/first_run_flow_spec.md` |
| Automation / Screen Recording restart | `PermissionRestartIntegration`, `SimpleModuleCoordinator` | ✅ restart flow в green, TAL hold активен 120 с | `Docs/TAL_TESTING_CHECKLIST.md` | TAL logs |

---

## 3. Flow & Flags

- **Флаги:**  
  - `permissions_first_run_completed.flag` — создаётся сразу после цикла запросов.  
  - `restart_completed.flag` — подтверждает успешный post-permission старт.  
  - Reset выполняем скриптом `python3 scripts/clear_first_run_flags.py`.
- **EventBus события:** `permissions.first_run_started`, `permissions.status_checked`, `permissions.changed`, `permissions.first_run_restart_pending`, `permissions.first_run_completed`.
- **Перезапуск:** `PermissionRestartIntegration` вызывает `PermissionsRestartHandler.trigger_restart()`; `SimpleModuleCoordinator` держит TAL (`disableAutomaticTermination_`) до `tray.ready`.

См. `Docs/first_run_flow_spec.md` и `Docs/TAL_TESTING_CHECKLIST.md` для детальных последовательностей.

---

## 4. Последние проверки

| Проверка | Дата | Результат | Логи / артефакты |
|----------|------|-----------|------------------|
| First-run + restart (permissions) | 2025-01-08 | ✅ pass | `scripts/test_first_run_integration.sh`, `log.md` |
| TAL hold / restart after permissions | 2025-01-12 | ✅ pass | `Docs/TAL_TESTING_CHECKLIST.md`, `scripts/check_tal_after_restart.py` |
| Tray termination (post permissions) | 2025-01-12 | ✅ pass | `Docs/PRE_PACKAGING_VERIFICATION.md`, `scripts/test_tray_termination.py` |

---

## 5. Открытые задачи

| ID | Описание | План действия | Статус |
|----|----------|---------------|--------|
| **TCC-AX-001** | Удалить использование приватного API `TCCAccessRequest` для Accessibility проверки. | Перевести на `AXIsProcessTrustedWithOptions`, обновить `modules/permission_restart/...`, добавить unit тест + логи. | ✅ **ЗАВЕРШЕНО** (2025-01-15): Используется публичный API `AXIsProcessTrustedWithOptions` в `modules/permissions/macos/accessibility_handler.py` |
| **PERM-RESET-002** | Добавить CLI helper для полного сброса TCC + флагов (удобно для QA). | Обновить `scripts/clear_first_run_flags.py` (проверка существующих значений, дружелюбные сообщения). |
| **PERM-LOG-003** | Ввести единый лог-формат `permissions.status_checked` для всех осей. | Обновить интеграцию и добавить описание в `Docs/STATE_CATALOG.md`. |

---

## 6. Связанные документы и тесты

- `Docs/first_run_flow_spec.md`
- `Docs/STATE_CATALOG.md` (оси `permissions.*`, `first_run`)
- `Docs/TAL_TESTING_CHECKLIST.md`
- `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md`
- `Docs/RESTART_AFTER_PERMISSIONS_ISSUE_ANALYSIS.md`
- `scripts/check_tal_after_restart.py`, `scripts/test_tal_assertion.py`, `scripts/test_restart_priority.sh`

---

**Примечание:** этот отчёт — оперативный. При каждом значимом изменении прав, API или обнаружении регрессии обновляйте таблицы и задачи. Ссылайтесь на него из `Docs/CURRENT_STATUS_REPORT.md` и `.cursorrules` для актуального статуса TCC.
