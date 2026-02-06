# Pre-Packaging Verification

Цель: короткая проверка перед запуском `./packaging/build_final.sh`.

## Команды

```bash
# 1) Базовый gate
./scripts/pre_build_gate.sh --skip-tests

# 2) Consolidated quality gate (release режим)
REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh

# 3) Packaging readiness
python3 scripts/verify_packaging_readiness.py
```

## Критерии

- Все 3 команды завершаются с кодом `0`.
- В `build_logs/problem_scan_latest.json`:
  - `summary.blocking_issues == 0`
  - `summary.basedpyright_status == "ok"`
- Нет критичных ошибок в output preflight-скриптов.

## Примечание

`build_final.sh` уже запускает readiness + problem scan автоматически, но этот файл полезен для ручной быстрой проверки до длительной упаковки.
