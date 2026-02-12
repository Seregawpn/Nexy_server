# Task Brief: Remove inter-step pause in permissions_v2

## Goal
Убрать искусственную задержку между шагами first-run pipeline.

## Change
- `config/unified_config.yaml`
  - `integrations.permissions_v2.inter_step_pause_s: 3.0 -> 0.0`

## Result
- Между шагами first-run больше нет дополнительной паузы.
- Общий timeout pipeline сокращается на сумму межшаговых пауз.
