# Task Brief: browser open fallback + PTT beep recovery hardening

## Context
Проблема: 
- `browser_use` иногда не открывает страницу, когда приходит только `url` без `task`.
- После длительной работы при disabled Quartz tap появлялся beep и PTT мог оставаться в деградированном состоянии до рестарта приложения.

## Architecture Fit
- Browser task owner: `modules/browser_automation/module.py` (`BrowserUseModule.process`).
- Input lifecycle owner: `integration/integrations/input_processing_integration.py` (`InputProcessingIntegration`).
- Source of Truth по mode/session не менялся: `ModeManagementIntegration -> ModeController -> ApplicationStateManager`.

## Implementation
1. В `BrowserUseModule` добавлена централизованная нормализация входа:
- `url` используется как fallback, если `task` отсутствует;
- при отсутствии и `task`, и `url` возвращается terminal `BROWSER_TASK_FAILED` с `error=missing_task_or_url`.

2. В `InputProcessingIntegration` усилен secure-input recovery:
- добавлен таймер длительного `tap_disabled`;
- добавлен recovery-путь перезапуска monitor (`stop_monitoring` -> `start_monitoring`);
- при успешном восстановлении tap возвращаются `ptt_available=True` и снятие secure-input состояния.

3. Добавлены тесты:
- URL fallback/missing input для browser module;
- recovery monitor restart для secure-input healthcheck.

## Verification
- Команда: `pytest -q tests/test_browser_module_ready_bypass.py tests/test_input_secure_input_healthcheck.py`
- Результат: `6 passed in 1.79s`

## Информация об изменениях
- Что изменено:
  - Централизован fallback `url -> task` в owner-модуле browser automation.
  - Добавлен автоматический recovery Quartz monitor при длительном `tap_disabled`.
  - Добавлены unit-тесты на оба сценария.
- Список файлов:
  - `modules/browser_automation/module.py`
  - `integration/integrations/input_processing_integration.py`
  - `tests/test_browser_module_ready_bypass.py`
  - `tests/test_input_secure_input_healthcheck.py`
  - `Docs/assistant_exchange/codex/2026-02-17__task-brief__browser-open-and-ptt-beep-recovery.md`
- Причина/цель изменений:
  - Устранить кейсы, когда browser команда не открывает страницу при `url`-only payload.
  - Снизить вероятность ручного рестарта приложения при долгой сессии и деградации keyboard tap.
- Проверка (что выполнено для валидации):
  - Добавлены и пройдены целевые тесты на fallback и recovery.
