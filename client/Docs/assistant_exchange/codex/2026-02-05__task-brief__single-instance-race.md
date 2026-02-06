# Single Instance Race Fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-05
- ID (INS-###): INS-NA

## Diagnosis
Возможна гонка при старте: второй процесс видит свежий lock-файл с неполным JSON, считает его невалидным и удаляет, что приводит к двум активным экземплярам.

## Root Cause
Нет grace-паузы для чтения lock-файла: частично записанный JSON трактуется как невалидный → cleanup → параллельный старт.

## Optimal Fix
Добавить lock_grace_ms и считать свежий lock валидным, чтобы не удалять его при частичной записи. Конфиг вынести в unified_config и использовать в InstanceManagerIntegration.

## Verification
Запустить два процесса одновременно и убедиться, что второй корректно завершится как duplicate без удаления свежего lock.

## Запрос/цель
Убрать запуск двух экземпляров при гонке старта.

## Контекст
- Файлы: modules/instance_manager/core/instance_manager.py, modules/instance_manager/core/types.py, integration/integrations/instance_manager_integration.py, config/unified_config.yaml
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без нового источника истины

## Решения/выводы
- Добавлен grace-период на lock-файл; конфиг централизован.

## Открытые вопросы
- Нужен ли отдельный log-сигнал для диагностики race случаев?

## Следующие шаги
- Проверить поведение при параллельных стартах.
