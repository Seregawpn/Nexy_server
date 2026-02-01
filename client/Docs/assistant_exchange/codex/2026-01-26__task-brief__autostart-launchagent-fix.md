# Autostart LaunchAgent Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
Системный LaunchAgent указывал на несуществующий `nexy_launcher.sh`, что приводило к некорректному автозапуску и путям запуска из dist/dev.

## Root Cause
`/Library/LaunchAgents/com.sergiyzasorin.nexy.voiceassistant.plist` создавался с неверным ProgramArguments.

## Optimal Fix
Добавить postinstall в PKG, который всегда создаёт корректный LaunchAgent и указывает на `/Applications/Nexy.app/Contents/MacOS/Nexy`.

## Verification
После установки PKG:
- plist содержит корректный путь
- BOOT‑логи показывают запуск только из `/Applications/Nexy.app`

## Запрос/цель
Исправить автозапуск для будущих сборок.

## Контекст
- Файлы: packaging/build_final.sh, packaging/pkg_scripts/postinstall

## Решения/выводы
- Добавлен postinstall скрипт для генерации LaunchAgent.
- pkgbuild теперь включает scripts и distribution.xml требует scripts.

## Открытые вопросы
- Нет.

## Следующие шаги
- Пересобрать PKG/DMG через build_final.sh.
- Установить PKG и проверить лог запуска.
