# Browser Failure Fallback: User-Facing TTS Reasons

## Task
Добавить fallback-объяснение причин, если browser task не срабатывает, и озвучивать понятную причину пользователю.

## Architecture Fit
- Owner path сохранен: `BrowserUseIntegration` отвечает за user-facing feedback по browser terminal.
- Install-озвучка не возвращалась.

## Implementation
1. В `BrowserUseIntegration` добавлен mapper ошибок:
- `_build_browser_failure_feedback(error_text)`
- классифицирует типовые причины (`missing runtime`, `missing executable`, `missing API key`, `rate limit`, `503`, `timeout`, `network/tls`).

2. Добавлен единый announcer:
- `_announce_browser_failure(session_id, error_text, source)`
- публикует `system.notification` + TTS с понятной причиной.
- дедуп по `session_id` (5 секунд), чтобы не дублировать речь при повторных terminal/fallback событиях.

3. Включение в owner-flow:
- на `BROWSER_TASK_FAILED` из progress stream,
- на exception path в `_run_process`.

## Verification
- `python3 -m py_compile integration/integrations/browser_use_integration.py` — OK
- Проверка наличия новых точек вызова/методов через `rg` — OK

## Информация об изменениях
- что изменено:
  - Добавлен fallback user-facing reason mapping для browser failures.
  - Добавлена озвучка причины сбоя с dedup-защитой.
  - Install-озвучка не добавлялась и остается отключенной.
- список файлов:
  - `integration/integrations/browser_use_integration.py`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__browser-failure-fallback-tts-reasons.md`
- причина/цель изменений:
  - Убрать silent fail UX: пользователь должен слышать, почему browser не сработал.
- проверка (что выполнено для валидации):
  - Синтаксическая проверка Python-модуля и проверка точек интеграции fallback-обработки.
