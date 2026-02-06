# Restart/Autostart Conflict Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
Остался один потенциальный race в helper‑проверке lock‑файла: при поврежденном/частично записанном JSON helper трактует lock как отсутствующий и может запустить второй инстанс.

## Root Cause
Helper не повторяет InstanceManager логику «fresh invalid JSON ⇒ считать lock валидным».

## Optimal Fix
В helper трактовать invalid/empty lock JSON как «instance running» при свежем mtime (использовать lock_grace_ms), чтобы не запускать второй процесс.

## Verification
Симулировать частично записанный lock‑файл в момент запуска helper: убедиться, что запуск пропущен.

## Запрос/цель
Перепроверить возможные конфликты/гонки после фикса restart.

## Контекст
- Файлы: modules/permission_restart/macos/permissions_restart_handler.py, modules/instance_manager/core/instance_manager.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Основной фикс корректен
- Есть 1 узкое окно в helper‑check при invalid lock JSON

## Найденные проблемы (если review)
- Helper не учитывает lock_grace_ms при invalid JSON

## Открытые вопросы
- Нужен ли дополнительный guard на reuse PID с non‑Nexy процессом

## Следующие шаги
- Добавить grace‑проверку в helper
