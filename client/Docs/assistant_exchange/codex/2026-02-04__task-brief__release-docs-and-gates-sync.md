# Task Brief

## Context
После внедрения consolidated quality pipeline (`problem_scan.sh` / `problem_scan_gate.sh`) документы и release-suite оставались частично на старом pre-build-only процессе.

## Changes
1. `scripts/run_release_suite.py`
- Добавлен новый обязательный шаг `check_problem_scan_gate()`.
- Шаг запускает `scripts/problem_scan_gate.sh` с env `REQUIRE_BASEDPYRIGHT_IN_SCAN=true`.
- Встроен в `run_all_checks()` сразу после `pre_build_gate`.
- Добавлен импорт `os` для передачи env.

2. `Docs/PACKAGING_FINAL_GUIDE.md`
- В раздел предварительной верификации добавлен обязательный запуск:
  - `./scripts/pre_build_gate.sh --skip-tests`
  - `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh`
- В anti-patterns добавлен запрет пропуска `problem_scan_gate.sh`.
- В чек-лист перед merge добавлен пункт `problem_scan_gate (blocking=0)`.

3. `Docs/ARCHITECTURE_OVERVIEW.md`
- В `3.1) Quality Gates` добавлен канонический контур:
  - `scripts/problem_scan.sh` как consolidated scan,
  - `scripts/problem_scan_gate.sh` как release/CI blocker,
  - блокировка только по `blocking_issues`, при релизе `REQUIRE_BASEDPYRIGHT_IN_SCAN=true`.

4. `Docs/PROJECT_REQUIREMENTS.md`
- REQ-018 уточнен: для релизной готовности обязателен `problem_scan_gate` (`blocking_issues=0`).
- Verification для REQ-018 дополнен: `scripts/problem_scan_gate.sh`, `scripts/run_release_suite.py`.

5. `Docs/README.md`
- Добавлен раздел `Quality Gates (скрипты)` с индексом:
  - `pre_build_gate.sh`, `quality_strict.sh`, `problem_scan.sh`, `problem_scan_gate.sh`, `problem_scan_prioritize.py`, `setup_dev_env.sh`.

6. `Docs/FEATURE_FLAGS.md`
- Добавлен реестровый config-флаг `REQUIRE_BASEDPYRIGHT_IN_SCAN` (owner: release).

## Verification
- `./.venv/bin/ruff check scripts/run_release_suite.py` → OK
- `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh` → PASSED
  - `TOTAL_ISSUES=298`
  - `BLOCKING_ISSUES=0`

## Impact
- CI/release/docs теперь синхронизированы по одному блокирующему quality-критерию.
- Упаковочные инструкции больше не расходятся с фактическим процессом проверки.
