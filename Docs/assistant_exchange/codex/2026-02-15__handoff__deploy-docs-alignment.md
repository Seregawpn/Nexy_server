# Handoff: Deploy Docs & Scripts Alignment

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-15
- ID (INS-###): N/A

## Diagnosis
Каноничные деплой/релиз документы расходились с фактической Azure-средой и реальными скриптами (устаревшие VM/RG, неверный source of truth версии, несуществующий publish script).

## Root Cause
Исторические документы и utility-скрипты обновлялись несинхронно -> операторские шаги из rulebook не исполнялись как есть -> ручные обходы и ошибки при прод-деплое.

## Optimal Fix
Обновлены active rulebooks и базовые deploy/release скрипты до текущего контура `NetworkWatcherRG/Nexy`, добавлен отсутствующий `publish_assets_and_sync.py`, зафиксирован `VERSION` как primary source of truth для runtime version.

## Verification
- Проверка синтаксиса shell-скриптов: `bash -n` (ok)
- Проверка python script: `py_compile` и `--help` (ok)
- Проверка ссылок в active docs: удалены критичные несоответствия для каноничных деплой/релиз flow.

## Запрос/цель
Привести документацию и скрипты деплоя/релиза в полностью рабочее и непротиворечивое состояние.

## Контекст
- Файлы: `server/Docs/SERVER_DEPLOYMENT_GUIDE.md`, `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md`, `server/Docs/RELEASE_AND_UPDATE_GUIDE.md`, `server/scripts/publish_assets_and_sync.py`, `server/scripts/update_server_version.sh`
- Документы: `server/Docs/VERSION_MANAGEMENT.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`
- Ограничения: без реархитектуры, только выравнивание текущего прод-процесса.

## Решения/выводы
- Каноничный publish flow теперь опирается на реальный скрипт `server/scripts/publish_assets_and_sync.py`.
- Manual deploy flow не использует некорректный запуск оркестратор-скрипта внутри VM.
- Версия в runtime стандартизирована вокруг `server/VERSION` + sync manifest.

## Открытые вопросы
- Нужна ли полная миграция всех legacy-скриптов в `server/scripts/` на новый IP/host policy (вне каноничных flow).

## Следующие шаги
- Прогнать один dry-run release: `python3 server/scripts/publish_assets_and_sync.py --dry-run`.
- Прогнать один controlled deploy по новому блоку из `SERVER_DEPLOYMENT_GUIDE.md` на staging/production.
