# Task Brief

## Context
Пайплайн `scripts/problem_scan_gate.sh` падал при наличии только warning-диагностик from basedpyright (`TOTAL_ISSUES>0`), что блокировало работу несмотря на отсутствие реальных error.

## Changes
- Обновлен `scripts/scan_problem_list.py`:
  - добавлено поле `summary.blocking_issues` (все issue, кроме `severity=warning`)
  - добавлен вывод `blocking_issues` в markdown-отчет.
- Обновлен `scripts/problem_scan_gate.sh`:
  - чтение `blocking_issues` из JSON (с fallback на `total_issues` для обратной совместимости)
  - gate теперь падает только по blocking-ошибкам
  - лог теперь показывает `blocking` и `total` отдельно.

## Verification
Запуск:
`REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh`

Результат:
- `basedpyright_status: ok`
- `TOTAL_ISSUES=467` (warnings)
- gate passed: `blocking: 0`

## Impact
Сканер продолжает собирать полный список проблем, но CI/локальный gate блокируется только по реальным блокирующим ошибкам.
