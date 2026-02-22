# Remove Sys Path Proto Import Duplication

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-21
- ID (INS-###): N/A

## Diagnosis
В `GrpcClient` был нецентрализованный import-path owner через `sys.path.insert/append`, что нарушало architecture guard и создавало потенциальный конфликт runtime import order.

## Root Cause
Legacy fallback-импорт protobuf модулей модифицировал глобальный `sys.path` в runtime, тем самым создавая второй путь разрешения модулей вне entrypoint owner.

## Optimal Fix
Заменен path-mutation подход на file-based import loader с кэшем, без `sys.path` модификаций:
1. package import (`modules.grpc_client.proto.*`)
2. file-based import из client proto директории
3. file-based fallback из server proto директорий

## Verification
- `cd client && python3 scripts/verify_architecture_guards.py` -> OK
- `cd client && pytest -q tests/test_grpc_client_interim_commit_gate.py tests/test_centralization_regressions.py` -> 6 passed
- `cd client && pytest -q tests/test_interrupt_playback.py tests/test_speech_playback_pipeline_diagnostic.py` -> 19 passed

## Информация об изменениях
- Что изменено:
  - Удалены `sys.path.insert/append` из `GrpcClient._import_proto_modules`.
  - Добавлен безопасный file-based loader protobuf модулей и кэш `_proto_modules`.
- Файлы:
  - `client/modules/grpc_client/core/grpc_client.py`
- Причина/цель:
  - Устранить architecture-guard нарушение и убрать дубль owner-path для proto import.
- Проверка:
  - Architecture guard + регрессии grpc/interrupt/playback.

## Запрос/цель
Убрать дубли/конфликты import условий и подтвердить, что поведение не сломано.

## Контекст
- Связано с phase-routing стабилизацией и общими anti-duplication требованиями.

## Решения/выводы
- Нарушение `sys_path_insert_outside_entrypoint` устранено.
- Import owner-path стал централизован и предсказуем.

## Открытые вопросы
- Нужен ли отдельный smoke на packaged runtime для file-based fallback из server proto директории.

## Следующие шаги
- Добавить малый unit-test на `_import_proto_modules` для обоих fallback сценариев.
