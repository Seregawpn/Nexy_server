# Architecture Governance (Root Canon)

Этот документ фиксирует обязательные архитектурные гейты для предотвращения дублей, конфликтов и гонок.

## 1. Single Owner Gate

- Для каждой архитектурной оси есть один владелец (Source of Truth).
- Запрещено создавать второй путь принятия решений.
- Любое изменение обязано явно указать owner.

## 2. Zero Duplication Gate

- Логика с высоким сходством (>=70%) не копируется, а объединяется.
- В change-set должно быть явно указано:
  - что было дубликатом;
  - что стало единым владельцем.

## 3. Anti-Race Gate

- Любой shared mutable state должен иметь явный guard:
  - `single-flight`;
  - `lock`/`mutex`;
  - `state-guard`;
  - `idempotency`.
- Для event-driven потоков обязательно проверять:
  - повторные события;
  - out-of-order доставку;
  - конкурентные вызовы на один контекст (session/request/hardware_id).

## 4. Flag Lifecycle Gate

- Каждый флаг обязан:
  - иметь runtime-потребителя;
  - быть описан в документации;
  - иметь единый default без конфликта code/docs.
- Флаг без runtime-ветки запрещен (dead flag).

## 5. Legacy Path Policy

- Legacy/fallback путь допускается только как временная миграция.
- Для каждого такого пути обязателен:
  - owner;
  - условие отключения;
  - срок удаления.
- Legacy path без срока удаления запрещен.

## 6. Definition of Done (Architecture)

Изменение считается корректным, только если:

1. `Centralized: yes`
2. `Breaks architecture: no`
3. Дубликаты удалены или объединены
4. Race guards присутствуют и протестированы
5. Flag lifecycle синхронизирован (code/docs/runtime)
