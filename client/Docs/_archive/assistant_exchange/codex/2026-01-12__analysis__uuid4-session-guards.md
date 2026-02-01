# UUID4 Session Guards

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): <из Docs/CRM_INSTRUCTION_REGISTRY.md>

## Diagnosis
gRPC падает до отправки из‑за нестрокового session_id; вероятно запускается старый процесс без актуальных guards.

## Root Cause
Несогласованный тип session_id → .strip() в gRPC клиенте → исключение до отправки; возможный источник float — устаревший бинарь/процесс.

## Optimal Fix
Единый uuid4 контракт: валидация в ApplicationStateManager, source‑guard в mode_management, и строгая проверка на client/server boundary.

## Verification
Полный перезапуск клиента, проверка uuid4 в логах и отсутствие ошибки `.strip`.

## Запрос/цель
Проверить причину отсутствия отправки на сервер и предложить архитектурно корректный фикс.

## Контекст
- Файлы: `integration/core/state_manager.py`, `integration/integrations/mode_management_integration.py`, `integration/integrations/grpc_client_integration.py`, `server/modules/grpc_service/core/grpc_server.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`

## Решения/выводы
- float не создается в текущих input_processing/voice_recognition; вероятна устаревшая сборка.

## Открытые вопросы
- Требуется ли жесткое отклонение не‑uuid4 на server boundary с отдельным error code?

## Следующие шаги
- Добавить guards на SoT + boundary; перезапустить клиент из репо.
