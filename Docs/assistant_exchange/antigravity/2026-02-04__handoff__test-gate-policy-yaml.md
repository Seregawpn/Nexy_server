## Автор
Codex

## Запрос / Цель
Вынести policy pre-commit test gate в YAML, чтобы управлять правилами без правки bash-скрипта.

## Контекст
- `server/config/test_gate_policy.yaml`
- `server/scripts/pre_commit_gate.sh`

## Решение
1. Добавлен конфиг policy:
- `server/config/test_gate_policy.yaml`
- Секции:
  - `critical_test_map`
  - `critical_full_suite_patterns`

2. Обновлен pre-commit gate:
- `server/scripts/pre_commit_gate.sh`
- Теперь policy читается из YAML (`server/config/test_gate_policy.yaml`).
- Скрипт валидирует структуру policy и использует только корректные строковые значения.
- Если policy отсутствует/некорректен, используется безопасный fallback (пустые правила).

## Проверка
- `bash server/scripts/pre_commit_gate.sh` (без staged Python) — корректный skip.
- `bash server/scripts/full_quality_scan.sh` — `74 passed`.

## Следующие шаги
1. Изменять mapping/patterns в `server/config/test_gate_policy.yaml` без редактирования скрипта.
2. При расширении тестового покрытия добавлять новые пары "critical path -> required tests" в YAML.
