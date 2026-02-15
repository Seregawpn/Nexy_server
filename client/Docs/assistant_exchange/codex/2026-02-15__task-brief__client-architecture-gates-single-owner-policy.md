# Task Brief: client architecture gates + single-owner policy

Дата: 2026-02-15

## Scope
Только client-репозиторий (`/client`).
Серверные файлы/пайплайны не изменялись.

## Что внедрено

1. Новый client-only архитектурный gate-скрипт
- `scripts/verify_architecture_guards.py`
- Проверки:
  - `sys.path.insert` вне entrypoint (`main.py`)
  - owner-policy для критичных publisher событий (`app.mode_changed`, `processing.terminal`)
  - runtime legacy markers без expiry-note (`LEGACY_EXPIRY:`)
  - dead feature flags (`config/features` без runtime usage)
- Режим baseline-aware: блокируются только НОВЫЕ нарушения.

2. Baseline архитектурного долга
- `scripts/architecture_guard_baseline.json`
- Зафиксирован текущий технический долг, чтобы не ломать текущую ветку, но запрещать его рост.

3. CI интеграция (client)
- `.github/workflows/ci.yml`
- Добавлен шаг `Architecture guards (client-only)`:
  - `python scripts/verify_architecture_guards.py`

4. Локальный pre-build gate
- `scripts/pre_build_gate.sh`
- Добавлена обязательная проверка:
  - `scripts/verify_architecture_guards.py`

5. PR policy (обязательные поля)
- `.github/PULL_REQUEST_TEMPLATE.md`
- Добавлен блок `Single Owner Check`:
  - owner axis
  - source of truth
  - removed/merged duplicate path
  - second-path guard
  - legacy/fallback expiry
- Добавлен checklist-пункт про critical event owner и прохождение architecture guards.

## Валидация
- `python3 scripts/verify_architecture_guards.py` -> OK
- `PYTHONPATH=. pytest -q tests/test_mode_management_mode_request_dedup.py` -> 5 passed

## Примечание по стратегии
Использован baseline-подход, чтобы:
- не блокировать существующий legacy-долг одномоментно,
- но сделать новые дубли/вторые пути/нераскрытые legacy ветки "дорогими" на PR/CI уровне.
