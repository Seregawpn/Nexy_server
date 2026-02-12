# Task Brief: plan testing sequence and interaction gates

## Context
- Запрошено усилить план: четкая последовательность тестирования, точки взаимодействия, проверки корректности и защита от поломок соседних частей.

## What was added
- В governance-план добавлен обязательный раздел `13. Test Strategy`:
  - строгий порядок тестирования (preflight -> unit -> integration -> e2e -> regression),
  - interaction points matrix (producer/consumer/contract/risk/validation),
  - correctness gates перед merge,
  - минимальный блокирующий набор тестов,
  - evidence bundle для PR.

## File updated
- `Docs/assistant_exchange/codex/2026-02-11__task-brief__first-run-restart-centralization-governance-plan.md`

## Outcome
- План теперь содержит полный тестовый контур и точки контроля целостности.
- Риск сломать соседние части уменьшен за счет явных merge-гейтов и scope-контроля.

