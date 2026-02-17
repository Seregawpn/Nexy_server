# Task Brief: browser CDP recovery + cancel path dedup

## Context
Пользователь подтвердил продолжение фикса нестабильности browser runtime (`Session with given id not found`, `Failed to open new tab - no browser is open`).

## Diagnosis
В owner-цепочке browser cancel был дублирующий путь: `keyboard.short_press -> BrowserUseIntegration._on_cancel_request`, параллельно с централизованным `interrupt.request -> grpc.request_cancel -> BrowserUseIntegration._on_cancel_request`.

## Root Cause
Архитектурный дубликат cancel-сигнала создавал риск double-cancel/close в середине browser task, что могло ронять CDP session lifecycle.

## Implementation
1. Удалена прямая подписка BrowserUseIntegration на `keyboard.short_press`.
2. Оставлен централизованный owner-путь отмены через `grpc.request_cancel` и `browser.cancel.request`.
3. Усилен retry-детектор в `BrowserUseModule` для CDP detachment сигналов:
   - `session with given id not found`
   - `no valid agent focus available`

## Architecture Gates
- Single Owner Gate: соблюден (owner cancel-path централизован в interrupt/grpc маршруте).
- Zero Duplication Gate: выполнен (удален дублирующий direct subscription).
- Anti-Race Gate: улучшен (уменьшен риск повторного close; расширен retry на CDP-detach).
- Flag Lifecycle Gate: новых флагов не добавлялось.

## Verification
- `python3 -m py_compile` для измененных файлов — OK.
- `git diff` подтверждает только целевые изменения.
- Поиск в `browser_use_integration.py` больше не содержит подписки на `keyboard.short_press`.

## Информация об изменениях
- Что изменено:
  - Удалён дублирующий cancel-path (`keyboard.short_press`) из BrowserUseIntegration.
  - Добавлены сигналы CDP-detach в retry logic BrowserUseModule.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/integrations/browser_use_integration.py`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`
- Причина/цель изменений:
  - Устранить race/дубли cancel и повысить устойчивость browser runtime при потере CDP session.
- Проверка:
  - `py_compile`, `git diff`, `rg`-проверка подписки.
