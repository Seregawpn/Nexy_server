# Assistant Runtime V2 Category Matrix

Цель: зафиксировать базовые категории запросов и expected contract для развития системы без смешивания chat, describe и action lifecycle.

## Track A: Non-Action

### 1. Simple Conversation
- Примеры:
  - `Привет`
  - `Как дела?`
  - `Спасибо`
  - `Расскажи шутку`
- Expected contract:
  - `route = none`
  - `goal_state = empty`
  - `command = none`
  - не должно быть ложного продолжения старой action-задачи

### 2. Capability / Meta
- Примеры:
  - `Что ты умеешь?`
  - `Чем ты можешь помочь?`
- Expected contract:
  - `route = capability`
  - `goal_state = empty`
  - `command = none`

### 3. Screen Description
- Примеры:
  - `Что на экране?`
  - `Опиши экран`
  - `Что ты видишь?`
- Expected contract:
  - `route = describe`
  - `goal_state = empty`
  - `command = none`
  - старая action-задача не должна протекать в describe flow

## Track B: Action Single-Turn

### 4. Messages / WhatsApp
- complete request -> `command`
- missing field -> `clarification`
- route stays `messages|whatsapp`

### 5. System Control
- complete request -> `command`
- missing detail -> `clarification`

### 6. Browser
- direct browser task -> `command`
- unresolved target -> `clarification`

### 7. Google Search / Factual
- usually `command = none`
- `goal_state = empty|clear`

### 8. Payment / Subscription
- direct billing action -> `command` or URL/open flow
- unresolved detail -> `clarification`

### Current baseline status

- `Simple Conversation` — covered
- `Capability / Meta` — covered
- `Screen Description` — covered
- `Single-turn action` — covered
- `Multi-turn lifecycle` — covered
- `Noisy / ambiguous recovery` — covered

## Track C: Action Multi-Turn / Lifecycle

- `set`
- `keep`
- `replace`
- `clear`
- `empty`

Сюда входят:
- clarification chains
- slot fill follow-up
- cancel
- pivot / replacement
- noisy continuation
- pronoun continuation

## Development Order

1. `Simple Conversation baseline`
2. `Screen Description baseline`
3. `Single-turn action baseline`
4. `Multi-turn lifecycle baseline`
5. `Noisy / ambiguous follow-up baseline`

## Shared Contract Fields

Для каждой категории проверяем:
- `route`
- `goal_state`
- `lifecycle`
- `command / no-command`
- `memory needed / not needed`
- `clarification needed / not needed`
- `old context leakage`
