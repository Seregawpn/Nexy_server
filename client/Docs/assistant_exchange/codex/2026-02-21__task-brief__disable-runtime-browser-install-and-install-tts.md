# Disable Runtime Browser Install and Install TTS

## Task
По запросу пользователя убрать runtime-установку браузера и убрать речь/уведомления о процессе установки браузера.

## Architecture Fit
- Owner path сохранен: `BrowserUseModule` (runtime readiness), `BrowserUseIntegration` (user-facing сообщения).
- Mode owner-chain не изменен.

## Implementation
1. Runtime install отключен в owner-path `process()`:
- если preinstalled runtime отсутствует, сразу `BROWSER_TASK_FAILED` с `browser_runtime_missing_preinstalled_chromium_required`.
- fallback на runtime-install/uvx больше не выполняется.

2. Runtime install отключен в init-path:
- `initialize()` больше не стартует install task даже при отсутствии Chromium.

3. Жесткий guard от случайного использования installer-path:
- `_ensure_browser_installed()` теперь сразу кидает `runtime_browser_install_disabled_use_prebundled_runtime`.
- `_get_or_start_install_task()` теперь сразу кидает `runtime_browser_install_disabled_use_prebundled_runtime`.

4. Убрана install-озвучка/notify:
- В `BrowserUseIntegration._handle_install_status()` удалены сообщения
  "Browser is installing..." и связанный startup TTS.
- Оставлен только failure notify (без install-голоса).

5. Конфиг выровнен:
- `browser_use.allow_runtime_install: false`.

## Verification
- `python3 -m py_compile modules/browser_automation/module.py integration/integrations/browser_use_integration.py` — OK
- YAML parse `config/unified_config.yaml` — OK

## Информация об изменениях
- что изменено:
  - Удален runtime-install path из рабочего owner-flow browser-use.
  - Добавлены hard-disable guards на legacy installer methods.
  - Удалена речь о "установке браузера".
  - Отключен `allow_runtime_install` в конфиге.
- список файлов:
  - `modules/browser_automation/module.py`
  - `integration/integrations/browser_use_integration.py`
  - `config/unified_config.yaml`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__disable-runtime-browser-install-and-install-tts.md`
- причина/цель изменений:
  - Перейти на deterministic pre-bundled browser runtime для packaged app и убрать confusing install UX.
- проверка (что выполнено для валидации):
  - Синтаксические проверки Python и валидность YAML.
