# Hotkey Shortcut Interception Diagnosis

## 1. Problem Statement (canonical)

Текущая проблема формулируется как:
- **shortcut interception / misrouting**, а не "возврат фокуса".

Симптом:
- при `Cmd+Space` (Spotlight/Alfred) событие частично перехватывается/перекладывается в путь Nexy;
- системный shortcut-flow ломается (launcher открывается нестабильно или теряет контекст).

## 2. What It Is / What It Is Not

Это:
- нарушение маршрутизации клавиатурного события (interception outside target combo).

Это не:
- первично focus-only баг.

Примечание:
- focus side effects могут быть вторичным проявлением, но root-cause находится в shortcut interception path.

## 3. Architecture Ownership

- Suppression policy owner:
  - `modules/input_processing/keyboard/mac/quartz_monitor.py`
- PTT lifecycle owner:
  - `integration/integrations/input_processing_integration.py`
- Focus policy owner (secondary guard):
  - `main.py`
  - `integration/core/simple_module_coordinator.py`

## 4. Required Invariant

Единственный допустимый interception:
- strict `Ctrl+N` (`Control && N && !Command && !Option && !Shift`).

Все остальные комбинации:
- mandatory pass-through (`intercepted=false`).

## 5. Implementation Implication

Primary KPI:
- отсутствие interception для нецелевых shortcut (`Cmd+Space`, `Cmd+Shift+A`, `Cmd+Tab`, `Ctrl+Cmd+N`).

Secondary KPI:
- отсутствие post-startup focus takeover.

## 6. Verification Focus

1. Проверять сначала interception logs, потом focus logs.
2. Считать fix успешным только если нецелевые shortcut идут по системному маршруту без участия Nexy.
3. Проверять `Ctrl+N` отдельно как единственный разрешенный interception path.

## 7. Links

- Requirements baseline:
  - `Docs/HOTKEY_CONFLICT_GUARD_REQUIREMENTS.md`
- Execution plan:
  - `Docs/HOTKEY_CONFLICT_GUARD_IMPLEMENTATION_PLAN.md`
