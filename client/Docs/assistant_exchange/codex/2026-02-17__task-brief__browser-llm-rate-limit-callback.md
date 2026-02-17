# Task Brief: Browser LLM Rate-Limit Callback

## Context
По runtime-логам Dev в браузерном сценарии встречаются ошибки Gemini API `429 RESOURCE_EXHAUSTED` (quota exceeded). Нужно давать пользователю явный callback: "Превышен лимит. Попробуйте позже.".

## Goal
Добавить централизованный callback-путь для rate-limit ошибок LLM в browser-flow без дублирования owners и без изменения общей архитектуры.

## Changes
1. В `GeminiLLMAdapter` добавлено распознавание rate-limit ошибок:
- `_is_rate_limited_error(...)`.
- отдельный флаг дедупликации уведомления: `_rate_limited_notified`.
- в `ainvoke` при rate-limit отправляется `llm_error_callback` с `reason="llm_rate_limited"`.

2. В `BrowserUseIntegration` расширен `on_llm_error`:
- для `reason="llm_rate_limited"` публикуется:
  - `system.notification`: "Превышен лимит. Попробуйте позже."
  - `grpc.tts_request` с `source="browser_llm_rate_limited"` и тем же текстом.

3. Добавлены тесты:
- callback `llm_rate_limited` в integration -> notification + TTS.
- детекторы ошибок в `GeminiLLMAdapter` для rate-limit и service-unavailable.

## Architecture Gates
- Single Owner Gate: LLM error classification в `GeminiLLMAdapter`, UX callback в `BrowserUseIntegration`.
- Zero Duplication Gate: не добавлялся второй callback-path в workflow/processing.
- Anti-Race Gate: дедуп через `_rate_limited_notified`.
- Flag Lifecycle Gate: новые флаги runtime используются (`_rate_limited_notified`).

## Verification
- `pytest -q tests/test_browser_install_contracts.py tests/test_token_reporting.py`
- Result: `14 passed in 9.83s`
- Runtime check (`/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`) подтвердил наличие реальных `429 RESOURCE_EXHAUSTED` и browser session recovery errors (`Failed to open new tab - no browser is open`).

## Информация об изменениях
- Что изменено:
  - Добавлен reason `llm_rate_limited` для callback при 429/quota.
  - Добавлено пользовательское сообщение/озвучка "Превышен лимит. Попробуйте позже.".
  - Добавлены тесты на новый callback и на детекторы ошибок.
- Список файлов:
  - `modules/browser_automation/module.py`
  - `integration/integrations/browser_use_integration.py`
  - `tests/test_browser_install_contracts.py`
  - `tests/test_token_reporting.py`
- Причина/цель изменений:
  - Убрать неявные browser LLM-fail состояния и давать ясный user-facing callback при лимите.
- Проверка (что выполнено для валидации):
  - Прогнаны целевые тесты, проверены свежие runtime-логи с реальными 429.
