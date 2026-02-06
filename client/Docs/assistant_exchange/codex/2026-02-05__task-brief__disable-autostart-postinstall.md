# Disable Autostart Postinstall

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): INS-000

## Diagnosis
PKG postinstall создавал legacy LaunchAgent, что включало автозапуск независимо от кода.

## Root Cause
`packaging/pkg_scripts/postinstall` генерировал `/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist` и bootstrap’ил job.

## Optimal Fix
Отключить создание LaunchAgent в postinstall и удалить legacy plist при установке.

## Verification
После установки нет файла plist и автозапуска.

## Запрос/цель
Полностью убрать функционал автозапуска на уровне упаковки.

## Контекст
- Файлы: packaging/pkg_scripts/postinstall
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новых источников истины

## Решения/выводы
- Postinstall больше не создает LaunchAgent.
- При установке удаляется legacy plist.

## Открытые вопросы
- Нужно ли оставлять опцию для автозапуска в будущих версиях.

## Следующие шаги
- Перепаковать приложение и установить.
- Проверить, что autostart не срабатывает.
