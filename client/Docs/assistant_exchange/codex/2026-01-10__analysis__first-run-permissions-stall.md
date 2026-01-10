# Анализ: first-run пауза и неактивация микрофона

## Контекст
- Пользователь: после разрешения микрофона — пауза ~15+ сек, затем запрос Input Monitoring; после выдачи — иконка активного микрофона, но запись/приветствие не стартуют.
- Лог: `log.md` (в основном системные логи).

## Наблюдения
- В проекте зафиксирован таймаут first-run ожидания 15 секунд (REQ-010).
- Архитектура: first-run permissions + permission_restart должны вести через EventBus и централизованные gateways (ARCHITECTURE_OVERVIEW.md в архиве).
- В репозитории отсутствуют обязательные актуальные документы `Docs/*` (использованы архивные версии для ориентации).

## Гипотезы
1) Пауза ~15 сек — ожидаемая задержка между шагами first-run (config `permissions.first_run.max_wait_sec`).
2) После выдачи Input Monitoring приложение должно перезапуститься (REQ-011), но перезапуск не произошёл или завис в guard-логике → микрофон не активируется.
3) Состояние first-run/permission_restart не синхронизировано (флаги/состояния), из-за чего слушание не стартует и приветствие не запускается.

## Рекомендованные проверки
- Посмотреть app-логи Nexy вокруг `permissions.first_run_*`, `permission_restart.*`, `voice.recognition_*`, `playback.*`.
- Проверить флаги в `~/Library/Application Support/Nexy/` (permissions_first_run_completed.flag, restart_completed.flag).
- Верифицировать конфиг `permissions.first_run.max_wait_sec` и gating в `permission_restart`.

