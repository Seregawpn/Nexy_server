# Permission Restart Lock Path Sync

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): INS-NA

## Diagnosis
PermissionRestart использовал дефолтный lock‑path и мог проверять не тот файл, что InstanceManagerIntegration.

## Root Cause
Отсутствие чтения unified_config для lock_file в PermissionRestartHandler.

## Optimal Fix
Синхронизировать lock‑path: читать instance_manager.lock_file из unified_config и использовать его в _is_other_instance_running.

## Verification
Перезапуск после разрешений должен видеть корректный lock‑файл и не стартовать второй экземпляр.

## Запрос/цель
Устранить рассинхрон lock‑path между InstanceManager и PermissionRestart.

## Контекст
- Файлы: modules/permission_restart/macos/permissions_restart_handler.py, config/unified_config.yaml
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Добавлено чтение UnifiedConfigLoader для lock_file в PermissionRestartHandler.

## Открытые вопросы
- Нужно ли добавить явный лог о выбранном lock‑path для диагностики?

## Следующие шаги
- Проверить рестарт после выдачи разрешений в packaged build.
