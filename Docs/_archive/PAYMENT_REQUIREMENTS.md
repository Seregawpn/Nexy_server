# Payment System Requirements
Feature ID: F-2025-017-stripe-payment

## 1) Scope
Эти требования фиксируют разделение ответственности client/server и обязательное правило:
**обработка речи (ASR/LLM/TTS) только на сервере**.

## 2) Architecture Ownership
Server (`server/server/`):
- Единственный владелец логики подписок, квот и статусов.
- Единственный владелец обработки речи (ASR/LLM/TTS).
- Единственный владелец Stripe webhook обработки.

Client (`client/`):
- UI, EventBus, deep links.
- Отображение статуса подписки.
- Открытие Stripe URL (checkout/portal) по событиям.
- Запрещены локальные вычисления квот и локальная обработка речи.

## 3) Functional Requirements

### REQ-PS-001: Centralized Source of Truth
Все решения по доступу/квотам принимаются только в `SubscriptionModule`.

### REQ-PS-002: Server-Only Speech
ASR/LLM/TTS выполняются только на сервере.
Клиент не должен генерировать речь или выполнять локальное распознавание.

### REQ-PS-003: Gate Enforcement
`StreamingWorkflowIntegration` обязан вызывать `subscription_module.can_process()` перед обработкой,
и `increment_usage()` только после успешной генерации.

### REQ-PS-004: Webhook Idempotency
Обработка вебхуков Stripe должна быть идемпотентной через `subscription_events` и UNIQUE constraint.

### REQ-PS-005: Client Reactivity
Клиент слушает `subscription.status_updated` и обновляет UI.
Клиент не считает квоты и не определяет статус.

### REQ-PS-006: Deep Link Sync
`nexy://payment/*` приводит к `payment.sync_requested` для синхронизации статуса.

## 4) Non-Functional Requirements
- Логи решений формата: `subscription_gate=allow|deny reason=...`.
- Все ошибки оплаты не инициируют локальный TTS на клиенте.
- Все сетевые вызовы оплаты идут через server API.

## 5) Verification Checklist
Server:
- SubscriptionModule инициализируется и виден в логах.
- Gate всегда вызывается до обработки.
- Webhook возвращает 400 на invalid signature.

Client:
- Нет локальной ASR/LLM/TTS логики.
- EventBus получает `subscription.status_updated`.
- Deep links вызывают `payment.sync_requested`.

## 6) References
- `Docs/PAYMENT_FLOW_EXPLAINED.md`
- `Docs/PAYMENT_UPDATE_CONTROLLER.md`
