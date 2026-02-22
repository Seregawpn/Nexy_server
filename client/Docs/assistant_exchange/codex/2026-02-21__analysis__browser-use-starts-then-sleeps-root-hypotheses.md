# Browser Use: starts then sleeps — root cause analysis

## Context
- User symptom: after browser request assistant says search is starting, but task does not proceed and app returns to sleeping.
- Scope: client browser-use pipeline only.

## Diagnosis
- Observed owner-path is consistent with architecture: `ActionExecutionIntegration -> BrowserUseIntegration -> BrowserUseModule -> ProcessingWorkflow -> ModeManagementIntegration`.
- The phrase "Browser opened. Starting search now." is emitted only after `BROWSER_TASK_STARTED`, then any fast failure emits `BROWSER_TASK_FAILED`, which returns mode to sleeping.

## Root Cause candidates
1. Missing Gemini API key (highest probability)
- Evidence: `modules/browser_automation/module.py` requires `gemini_api_key` from env / `~/Library/Application Support/Nexy/credentials.yaml` / config; otherwise raises `ValueError`.
- Effect: started event can be emitted before LLM init, then immediate `BROWSER_TASK_FAILED`.

2. Browser runtime launch failure after local executable resolution
- Evidence: startup path resolves executable from `~/Library/Application Support/Nexy/chrome-nexy`, then Agent creation can fail with `browser_profile_init_failed`.
- Effect: identical UX (start phrase, then fail -> sleeping).

3. Runtime install/driver failure in packaged mode (medium)
- Evidence: frozen runtime relies on bundled playwright driver discovery; if missing/corrupt, install path fails.
- Effect: request ends with failed terminal; if failure is quick in cached states, user perceives "no action".

## Fast verification plan (5–15 min)
1. API key check
- Verify one source exists:
  - `echo $GEMINI_API_KEY`
  - `cat ~/Library/Application\ Support/Nexy/credentials.yaml`
- Expected failure log if missing:
  - `GEMINI_API_KEY not configured ...`

2. Browser executable check
- Verify runtime path and executable:
  - `ls -la ~/Library/Application\ Support/Nexy/chrome-nexy`
  - find chromium binary and run `file <binary>`
- Expected failure log:
  - `browser_profile_init_failed` or `chromium_executable_not_found_after_setup`

3. Install/driver check (packaged app)
- Verify driver discovery logs:
  - `Found playwright wrapper ...` or `Found playwright driver layout ...`
- Failure signature:
  - `Playwright driver not found in frozen bundle`

## Architecture gates
- Single owner preserved: mode transitions still owned by `ModeManagementIntegration`.
- No duplicate path required for fix: add preflight/error mapping in existing `BrowserUseModule` + user-facing terminal TTS in existing integration path.

## Verification
- Ensure each browser request ends with one of:
  - step events + completed terminal
  - explicit failed reason announced to user (not silent sleep)
- Ensure no second mode owner is introduced.

## Информация об изменениях
- Что изменено:
  - Добавлен аналитический отчёт по root-cause и гипотезам для browser-use.
- Список файлов:
  - `Docs/assistant_exchange/codex/2026-02-21__analysis__browser-use-starts-then-sleeps-root-hypotheses.md`
- Причина/цель изменений:
  - Зафиксировать архитектурно-совместимый диагноз и дешёвые проверки для быстрого подтверждения корня проблемы.
- Проверка (что выполнено для валидации):
  - Выполнен анализ runtime-цепочки и проверка ключевых точек в `BrowserUseIntegration`, `BrowserUseModule`, `ProcessingWorkflow`, `ModeManagementIntegration`.
