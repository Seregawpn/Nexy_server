# Task Brief

## Context
Нужно, чтобы упаковка запускалась только после автоматической проверки всех обязательных quality/prepack условий без ручного запуска отдельных скриптов.

## Changes
- Обновлен `packaging/build_final.sh` (этап PRELIGHT):
  1. Добавлен запуск `scripts/verify_packaging_readiness.py`.
  2. Добавлен запуск `scripts/problem_scan_gate.sh` в release-режиме:
     - `REQUIRE_BASEDPYRIGHT_IN_SCAN=true`.
- При падении любого из этих шагов устанавливается `PREFLIGHT_FAILED=true`, и упаковка останавливается до сборки.
- Логи обоих шагов пишутся в общий preflight лог (`$PREFLIGHT_LOG`).

## Verification
- `bash -n packaging/build_final.sh` → OK

## Impact
Теперь `./packaging/build_final.sh` сам выполняет:
- проверку packaging readiness,
- consolidated quality gate (blocking-only + required basedpyright),
и только после этого продолжает упаковку.
