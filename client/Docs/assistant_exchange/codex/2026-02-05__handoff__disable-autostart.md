# Disable Autostart

## Метаданные
- Ассистент: codex
- Тип: handoff
- Дата: 2026-02-05
- ID (INS-###): INS-000

## Diagnosis
Автозапуск держится на legacy LaunchAgent в /Library/LaunchAgents.

## Root Cause
LaunchAgent запускает Nexy на логине → дубли.

## Optimal Fix
Отключить LaunchAgent через launchctl bootout (без удаления plist).

## Verification
launchctl print system/com.sergiyzasorin.nexy.voiceassistant → not found; автозапуск не происходит.

## Запрос/цель
Отключить автоматический запуск без удаления файлов.

## Контекст
- Файлы: /Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: не удалять plist

## Решения/выводы
Нужен sudo для bootout, в среде ассистента интерактивный пароль недоступен.

## Открытые вопросы
Нужно ли также отключать другие LaunchAgent/Daemon (если появятся).

## Следующие шаги
Выполнить команду вручную с sudo.
