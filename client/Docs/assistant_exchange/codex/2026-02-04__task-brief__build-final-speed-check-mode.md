# Task Brief

## Context
Пользователь запросил быстрый режим проверки соответствия (библиотеки/расширения/форматы/quality) в основном packaging скрипте, чтобы не запускать полную сборку каждый раз.

## Changes
1. `packaging/build_final.sh`
- Добавлен новый флаг `--speed-check`.
- В режиме `--speed-check`:
  - выполняются обязательные quality/preflight проверки,
  - пропускаются очистка / TCC reset / удаление старого приложения,
  - после успешного preflight скрипт завершает работу с `exit 0` без сборки/подписи/нотарификации.
- Обновлен header usage/help комментарий в скрипте.

2. `Docs/PACKAGING_FINAL_GUIDE.md`
- Добавлен пример команды:
  - `./packaging/build_final.sh --speed-check`

## Verification
- `bash -n packaging/build_final.sh` → OK
- `./packaging/build_final.sh --speed-check` → PASS
  - readiness gate PASS
  - problem_scan_gate PASS
  - preflight проверки PASS
  - финальное сообщение: SPEED-CHECK соответствует требованиям

## Impact
Теперь есть единый быстрый запуск в том же каноническом скрипте упаковки:
- для моментальной проверки соответствия окружения/библиотек/конфига/quality,
- без длительной полной упаковки.
