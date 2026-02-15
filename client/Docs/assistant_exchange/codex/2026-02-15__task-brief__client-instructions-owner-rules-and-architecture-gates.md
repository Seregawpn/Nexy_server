# Task Brief: client instructions sync (owner rules + architecture gates)

Дата: 2026-02-15

## Что сделано

Обновлены инструкции и канонические документы client-only, чтобы правила архитектуры были закреплены не только в CI, но и в документации:

1. `AGENTS.md`
- Добавлен раздел `Architecture Gates (обязательно, client-only)`:
  - one event, one owner
  - mode owner path
  - запрет second-path workaround
  - legacy/fallback expiry requirement
  - запрет новых `sys.path.insert` вне `main.py`
  - feature flag runtime-usage requirement
- Добавлен `PR Gate Policy` с обязательным `Single Owner Check`.
- Добавлен `CI/Local Enforcement` со ссылками на `scripts/verify_architecture_guards.py`.

2. `Docs/ARCHITECTURE_OVERVIEW.md`
- Расширен чек-лист инвариантов PR:
  - critical event owner policy
  - legacy expiry
  - sys.path restriction
  - no dead flags
- Добавлен подраздел `10.1) Архитектурные гейты (client-only)`:
  - перечислены machine-enforced checks
  - зафиксированы owner-gates в CI/local
  - описана baseline policy (блок новых нарушений).

3. `Docs/PROJECT_REQUIREMENTS.md`
- Добавлен раздел `9. Architecture Governance (Client-only)`.
- Добавлены новые требования:
  - `REQ-029`: one event, one owner (critical events)
  - `REQ-030`: обязательные architecture guards в CI/local pre-build
  - `REQ-031`: runtime legacy/fallback требует expiry
  - `REQ-032`: dead feature flags запрещены
- Обновлен `Implementation Map` (добавлены REQ-029..032).
- Обновлены даты ревизии документа.

## Проверки
- `python3 scripts/verify_architecture_guards.py` -> OK
- `python3 scripts/verify_feature_flags.py` -> OK

## Scope
- Изменения только в директории `client/`.
- Серверные инструкции/файлы не изменялись.
