## Автор
Codex

## Запрос / Цель
Добавить policy для pre-commit: для критичных модулей запускать расширенные/полные тесты.

## Контекст
- `server/scripts/pre_commit_gate.sh`

## Решение
В `pre_commit_gate.sh` добавлены два уровня критичности:

1. `critical_test_map` (таргетированный расширенный набор тестов):
- `streaming_workflow_integration.py` → `test_streaming_workflow_mcp.py`, `test_grpc_mcp_integration.py`
- `assistant_response_parser.py` → `test_assistant_response_parser.py`, `test_streaming_workflow_mcp.py`
- `json_stream_extractor.py` → `test_streaming_workflow_mcp.py`
- `grpc_service_integration.py` и `modules/grpc_service/` → `test_grpc_mcp_integration.py`, `test_grpc_identifier_validation.py`
- `config/prompts.py` → `test_prompt_keywords.py`, `test_config_validation.py`
- `config/unified_config.py` → `test_config_validation.py`, `test_config_drift.py`

2. `critical_full_suite_patterns` (всегда full suite):
- `server/modules/subscription/`
- `server/api/webhooks/stripe_webhook.py`
- `server/main.py`

Если staged изменения попадают в full-suite паттерны, pre-commit запускает весь `server/tests`.

## Проверка
- `bash server/scripts/pre_commit_gate.sh` (без staged python) — корректный skip.
- `bash server/scripts/full_quality_scan.sh` — `74 passed`.

## Следующие шаги
1. При необходимости расширять `critical_test_map` по мере добавления новых тестов.
2. Держать `critical_full_suite_patterns` минимальным, чтобы не замедлять commit без нужды.
