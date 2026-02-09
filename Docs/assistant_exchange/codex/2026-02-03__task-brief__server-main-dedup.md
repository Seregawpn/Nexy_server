# Server main.py dedup

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
Дублирующие проверки портов и двойная отмена задач в `server/main.py` создавали лишние ветки и риск гонок.

## Root Cause
Разрозненные проверки (precheck + try/except) и отсутствие явного контроля `shutdown_event.wait()`.

## Optimal Fix
Убрать precheck портов, оставить единую обработку ошибок при bind; отменить `metrics_task` один раз; явно управлять `shutdown_wait_task`.

## Verification
Занятые порты: единый путь ошибки. Штатный shutdown: нет pending-задач и двойной отмены.

## Запрос/цель
Убрать дубли и потенциальные конфликты в запуске/остановке серверов.

## Контекст
- Файлы: `server/main.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения архитектуры

## Решения/выводы
- Precheck портов удален, опора на реальный bind.
- `metrics_task` отменяется только в `finally`.
- `shutdown_wait_task` отменяется при выходе.

## Открытые вопросы
- Нужны ли улучшенные сообщения об ошибке gRPC bind внутри `run_server` (если он глотает исключение).

## Следующие шаги
- При необходимости добавить логирование конкретной ошибки bind внутри `modules.grpc_service.core.grpc_server`.
