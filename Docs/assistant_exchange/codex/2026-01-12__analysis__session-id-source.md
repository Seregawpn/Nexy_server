# Session ID Source Enforcement

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
session_id мог быть невалидным и/или перезаписан не тем источником, что ломало поток gRPC.

## Root Cause
нет жесткого ограничения источника session_id и общей валидации uuid4 в местах чтения/передачи.

## Optimal Fix
- централизованная проверка uuid4 в selectors
- режимы принимают session_id только от input_processing
- gRPC использует только валидный session_id

## Verification
вручную: invalid session_id игнорируется, валидный проходит через mode.request → gRPC → server.

## Запрос/цель
обеспечить создание корректного session_id и его прохождение по пути без подмен.

## Контекст
- Файлы: integration/core/selectors.py, integration/integrations/mode_management_integration.py, integration/integrations/grpc_client_integration.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: единый писатель session_id

## Решения/выводы
- Добавлен централизованный is_valid_session_id.
- session_id принимается только от input_processing.

## Открытые вопросы
- Нужно ли логировать источник, который пытался записать невалидный session_id, в error_handler?

## Следующие шаги
- Прогнать PTT сценарий и проверить логи.
