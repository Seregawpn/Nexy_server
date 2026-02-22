# Browser Failure Callbacks: English and Specific Reasons

## Task
Сделать callback-сообщения о сбоях browser-use более конкретными и на английском языке.

## Architecture Fit
- Owner path сохранен: `BrowserUseIntegration` отвечает за user-facing failure feedback.
- Дублирующие owner-пути не добавлены.

## Implementation
- Обновлен маппинг `_build_browser_failure_feedback(error_text)`:
  - API key missing
  - browser automation package missing
  - browser runtime missing
  - browser executable missing
  - bundled runtime misconfigured
  - Playwright driver missing
  - browser profile init failed
  - rate limit
  - service unavailable
  - timeout
  - network/TLS issues
  - internal error fallback
- Все сообщения теперь в английском и с формой: "I can't open the browser because ...".

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` — OK
- Проверка обновленных фраз через `rg` — OK

## Информация об изменениях
- что изменено:
  - Улучшены callback-фразы для browser failure: более точные причины, английский язык.
- список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__browser-failure-callbacks-english-and-specific.md`
- причина/цель изменений:
  - Пользователь должен получать понятное объяснение причины отказа browser-use, а не общий fail.
- проверка (что выполнено для валидации):
  - Синтаксическая проверка Python и проверка наличия новых сообщений.
