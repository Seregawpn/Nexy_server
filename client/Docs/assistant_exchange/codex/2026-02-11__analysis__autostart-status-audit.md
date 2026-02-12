# Autostart Status Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11

## Что проверено
- Runtime-состояние LaunchAgent в user/session launchctl.
- Конфиг и интеграция `autostart_manager`.
- Packaging postinstall на предмет создания LaunchAgent.

## Факты
- `~/Library/LaunchAgents/com.nexy.assistant.plist` отсутствует.
- `launchctl print gui/<uid>/com.nexy.assistant` не возвращает активный job.
- Legacy `/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist` отсутствует.
- `packaging/pkg_scripts/postinstall` не создает LaunchAgent; только удаляет legacy plist.
- Интеграция `autostart_manager` подключена в startup order и мониторит статус.
- Потенциальная активация автозапуска в коде возможна только при `auto_repair=true` (в текущем конфиге `false`).

## Вывод
Сейчас автозапуск не активирован ни на уровне текущей системы, ни на уровне упаковки. В коде есть условный путь активации (repair), но он выключен конфигом.
