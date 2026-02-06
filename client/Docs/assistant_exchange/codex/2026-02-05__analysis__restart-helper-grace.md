# Restart Helper Grace Fix

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-005

## Diagnosis
Helper не учитывал lock_grace_ms из InstanceManager; возможна рассинхронизация окна grace.

## Root Cause
Жестко заданный LOCK_GRACE_MS=1500 в helper не синхронизирован с конфигом instance_manager.

## Optimal Fix
Считать lock_grace_ms из unified_config в PermissionsRestartHandler и передавать в helper.

## Verification
Ручная проверка: свежий битый lock JSON должен блокировать запуск; grace соответствует конфигу.

## Запрос/цель
Устранить остаточную гонку в helper при частично записанном lock-файле.

## Контекст
- Файлы: modules/permission_restart/macos/permissions_restart_handler.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новых источников истины

## Решения/выводы
- LOCK_GRACE_MS теперь берется из unified_config
- Helper учитывает grace из InstanceManager

## Открытые вопросы
- Нет

## Следующие шаги
- Ручной прогон сценария с битым lock
