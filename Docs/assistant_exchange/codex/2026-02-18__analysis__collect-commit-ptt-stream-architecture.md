# Collect-Commit PTT Stream Architecture

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-18
- ID (INS-###): N/A

## Diagnosis
Текущий контракт `StreamRequest` однофазный: первый валидный `prompt` запускает LLM немедленно.
При этом на клиенте уже есть ранний screenshot-capture, но нет server-side commit-гейта для старта LLM после release.

## Root Cause
Контрактный разрыв между client STT lifecycle (interim/final) и server processing lifecycle (single-shot prompt).
Механизм: `voice.recognition_completed` (interim) через gRPC consumer запускает `_maybe_send`; сервер получает обычный `prompt` и сразу идет в LLM/TTS.
Эффект: ранний старт LLM и риск неполного long-utterance.

## Optimal Fix
Цель: разделить intake и execution без смены владельцев архитектуры.

Architecture Fit:
- Client owner отправки: `GrpcClientIntegration`.
- Server owner выполнения: `StreamingWorkflowIntegration`.

Source of Truth:
- `session_id` + `phase` (`collect|commit`) в gRPC контракте.
- LLM-start only on `phase=commit`.

Breaks architecture: no

Implementation Plan:
1. Расширить `StreamRequest` полями фазового протокола (`phase`, `seq`, `commit_id`).
2. Client: interim STT и screenshot слать как `collect`.
3. Client: на release/final STT слать `commit`.
4. Server: хранить per-session collect buffer и запускать LLM только на commit.
5. Добавить idempotency/race guards (seq monotonic, commit-once, cancel tombstone).
6. Добавить E2E тесты на long-hold и out-of-order partials.

## Verification
- До commit в логах нет `llm iteration started`.
- После commit — ровно один старт LLM на сессию.
- interrupt во время collect/после commit корректно закрывает сессию.

## Информация об изменениях
- Что изменено: Изменения не вносились.
- Файлы: Нет.
- Причина/цель: Спроектировать target-архитектуру под long speech + early screenshot + deferred LLM start.
- Проверка: Сверка client/server owner-path и текущего proto.

## Запрос/цель
Определить, как организовать текущую архитектуру под сценарий "говорим долго, данные отправляются частями, LLM стартует только после release".

## Контекст
- Файлы: client/integration/integrations/{input_processing,voice_recognition,grpc_client,screenshot_capture}_integration.py; server/server/modules/grpc_service/streaming.proto; server/server/integrations/workflow_integrations/streaming_workflow_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md, server/server/Docs/FLOW_INTERACTION_SPEC.md
- Ограничения: без re-architecture, только эволюция существующего owner-path.

## Решения/выводы
- Ранний screenshot уже есть и архитектурно корректен.
- Ключевая недостающая часть — server-side commit gate.
- Правильный путь: collect/commit протокол в текущем gRPC owner path.

## Открытые вопросы
- Нужен ли commit timeout (auto-commit при пропаже release), или только явный release?

## Следующие шаги
- Согласовать поля proto и owner-правила commit.
- После согласования — внедрение и контрактные тесты.
