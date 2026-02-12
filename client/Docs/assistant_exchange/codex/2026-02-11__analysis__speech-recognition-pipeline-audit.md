# Speech Recognition Pipeline Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Speech/STT pipeline в целом централизован через `InputProcessingIntegration -> VoiceRecognitionIntegration -> GrpcClientIntegration -> SpeechPlaybackIntegration -> ModeManagementIntegration`, но есть 3 точечных риска: дубли terminal-path, конфликт sessionless cancel-контракта и конфигурационные задержки/зависания.

## Root Cause
1) Конфликт owner-логики между `ListeningWorkflow` и `InputProcessingIntegration` при короткой записи.  
2) Несогласованный контракт `grpc.request_cancel` (publisher допускает `session_id=None`, consumer отклоняет).  
3) Таймауты в конфиге/пайплайне дают либо лишнюю задержку (pre-send wait), либо слишком долгий hang (без RPC timeout).

## Optimal Fix
Goal: убрать второй путь mode decision и сделать deterministic cancel/latency-path для STT->gRPC.

Architecture Fit:
- Централизация остаётся в текущих владельцах интеграций, без реархитектуры.

Where it belongs:
- `integration/integrations/input_processing_integration.py`
- `integration/workflows/listening_workflow.py`
- `integration/integrations/interrupt_management_integration.py`
- `integration/integrations/grpc_client_integration.py`
- `config/unified_config.yaml`

Source of Truth:
- PTT lifecycle + terminal stop: `InputProcessingIntegration`
- Mode transitions: `ModeManagementIntegration`
- Cancel request ownership: `InterruptManagementIntegration` + `GrpcClientIntegration` contract
- session_id axis: `ApplicationStateManager`

Breaks architecture: no

Implementation Plan:
1. Убрать `mode.request(SLEEPING)` из `ListeningWorkflow` для short-recording ветки; оставить только событие/флаг для `InputProcessingIntegration` как единственного terminal owner.
2. Ужесточить cancel-контракт: либо всегда прокидывать `session_id` в `InterruptManagementIntegration`, либо в `GrpcClientIntegration._on_request_cancel` добавить fallback на last inflight session (один явный owner-путь, без silent drop).
3. Задать finite `integrations.grpc_client.request_timeout_sec` (например 20-30с) и переоценить `aggregate_timeout_sec`/pre-send wait.
4. Добавить contract-тесты: short-recording не запускает competing mode.request; sessionless cancel не теряет inflight запрос.

Code Touchpoints:
- `integration/workflows/listening_workflow.py`
- `integration/integrations/input_processing_integration.py`
- `integration/integrations/interrupt_management_integration.py`
- `integration/integrations/grpc_client_integration.py`
- `config/unified_config.yaml`

Concurrency Guard (if needed):
- state-guard + idempotency по `session_id`/`event_id` (без нового coordinator)

What to remove / merge:
- Remove: secondary short-recording sleep path in `ListeningWorkflow`
- Merge: sessionless cancel behavior into one contract path between interrupt/grpc integrations

## Verification
- Unit/contract tests:
  - `PYTHONPATH=. pytest -q tests/test_client_server_flow_contracts.py tests/test_interrupt_management_contract.py tests/test_speech_playback_session_id.py`
- Runtime checks:
  - TRACE delta: `recording_stop -> grpc.start`
  - TRACE delta: `grpc.start -> grpc.response(chunk=1)`
  - no duplicate terminal events per `session_id`

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы:
  - `AGENTS.md`
  - `Docs/DOCS_INDEX.md`
  - `Docs/PRE_CHANGE_CHECKLIST.md`
  - `Docs/PROJECT_REQUIREMENTS.md`
  - `Docs/ARCHITECTURE_OVERVIEW.md`
  - `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`
  - `Docs/FEATURE_FLAGS.md`
  - `Docs/CODEX_PROMPT.md`
  - `Docs/ANTIGRAVITY_PROMPT.md`
  - `Docs/assistant_exchange/TEMPLATE.md`
  - `Docs/FLOW_INTERACTION_SPEC.md` (sections 4.4/4.5/4.6)
  - `Docs/STATE_CATALOG.md` (session_id ownership)
- Source of Truth:
  - mode/session: `ApplicationStateManager` + `ModeManagementIntegration`
  - PTT terminal lifecycle: `InputProcessingIntegration`
- Дублирование:
  - найден secondary path short-recording sleep (`ListeningWorkflow`) vs primary release->processing path (`InputProcessingIntegration`)
- Feature Flags check:
  - новых флагов не вводилось
- Race check:
  - scenario: `interrupt.request` с `session_id=None` -> `grpc.request_cancel` rejected -> inflight request survives
  - guard: contract unification + fallback policy

## Запрос/цель
Проверить распознавание речи на дубли/конфликты/гонки, корректность серверной передачи и наличие задержек.

## Контекст
- Файлы: `integration/integrations/*`, `integration/workflows/*`, `modules/voice_recognition/*`, `modules/grpc_client/*`, `modules/speech_playback/*`
- Документы: canonical client/root docs + flow/state specs
- Ограничения: без реархитектуры, внутри текущих owners

## Решения/выводы
- Основной поток централизован и архитектурно корректен.
- Найдены локальные contract/race риски и latency-related config риски.
- Нужна точечная унификация terminal/cancel path, без новых сущностей.

## Открытые вопросы
- Приоритет UX: при `session_id=None` в cancel лучше fallback на last inflight или strict reject + hard assertion?

## Следующие шаги
1. Согласовать policy для sessionless cancel.
2. Внести точечные правки в 4 touchpoints.
3. Добавить 2 contract-теста и прогнать runtime TRACE-сценарий.
