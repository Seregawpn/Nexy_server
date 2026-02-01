# Centralized Permissions Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-12
- ID (INS-###): INS-008

## Diagnosis
Логика централизована, но есть риск stale-флага: при снятых разрешениях `are_all_granted` может остаться True и пропустить гейт.

## Root Cause
`_are_all_granted` инициализируется из `permissions_granted.flag`, но не сбрасывается при обнаружении missing разрешений → гейт принимает неверное решение.

## Optimal Fix
Сбрасывать `_are_all_granted=False` перед проверками в `start()`, обновлять по факту `all_granted`, и/или валидировать статус перед гейтами.

## Verification
Проверить сценарий: flag есть, права отозваны, first_run показывает missing → гейт должен блокировать input/screenshot/voiceover.

## Запрос/цель
Оценить корректность изменений по централизованным разрешениям и устранению двойных промптов.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, integration/core/simple_module_coordinator.py, integration/integrations/input_processing_integration.py
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md, /Users/sergiyzasorin/Fix_new/Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Основная идея корректна и снижает дублирующие промпты.
- Есть риск некорректного состояния при отозванных разрешениях.

## Найденные проблемы (если review)
- **Высокая**: stale `are_all_granted` при наличии `permissions_granted.flag` и отозванных разрешениях → гейт пропускает старт зависимых интеграций.

## Открытые вопросы
- Нужна ли поддержка деградации без рестарта после ручной выдачи прав?

## Следующие шаги
- Сброс `_are_all_granted` при запуске first_run и/или перепроверка статуса перед гейтами.

## Итоговый статус
**ЧАСТИЧНОЕ**
