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

## Runtime Focus/VoiceOver Smoke (обязательно)

Перед релизной упаковкой дополнительно выполнить ручной smoke:

1. Запустить приложение (cold start), одновременно открыть Spotlight/поиск macOS.
2. Убедиться, что Spotlight не закрывается и фокус не перехватывается.
3. Включить VoiceOver (Command+F5), повторить запуск и hotkey-сценарий.
4. Проверить, что VoiceOver продолжает навигацию, а Nexy работает штатно.
5. Просмотреть свежий хвост логов (`~/Library/Logs/Nexy/nexy.log`, `~/Library/Logs/Nexy/nexy-dev.log`) и убедиться в отсутствии loop-pattern (`SAFE_EXIT` каскад, повторные startup/shutdown пачки).

## Примечание

`build_final.sh` уже запускает readiness + problem scan автоматически, но этот файл полезен для ручной быстрой проверки до длительной упаковки.
