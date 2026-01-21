# Ideal First-Run Permissions Architecture

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Текущий first-run поток не гарантирует единый оркестратор статусов и fallback‑открытие System Settings для non‑promptable разрешений, из‑за чего часть запросов не визуализируется.

## Root Cause
Нет строгого контракта: status‑check → activate → recheck → settings‑fallback → restart gate → restart integration, что приводит к пропускам и спорной UX‑последовательности.

## Optimal Fix
Определить и закрепить архитектуру: единственный оркестратор first-run, единственный источник порядка, централизованная публикация событий и restart‑gate через permission_restart.

## Verification
Проверка по логам first-run + tccd после очистки флагов; последовательность должна строго соответствовать required_permissions, с fallback‑открытием Settings для Accessibility/Input Monitoring/FDA.

## Запрос/цель
Предварительно определить целевую архитектуру первого запуска для корректного запроса разрешений, перезапуска и отсутствия блокировок/конфликтов.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, modules/permissions/first_run/*, integration/integrations/permission_restart_integration.py, integration/core/simple_module_coordinator.py
- Документы: Docs/PROJECT_REQUIREMENTS.md (REQ-010/011/012), Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без реархитектуры, сохранить порядок интеграций и EventBus

## Решения/выводы
- Оркестратор first-run обязан принимать решения и публиковать события; activators только триггерят OS.
- Порядок разрешений — только из unified_config.yaml.
- Перезапуск — только через permission_restart (coordinator‑gate), без локальных обходов.

## Открытые вопросы
- Есть ли in‑app логи на каждое разрешение (status_before/after + fallback)?
- Используется ли settings‑fallback для Accessibility/Input Monitoring/FDA в текущем билде?

## Следующие шаги
- Утвердить архитектурный контракт и добавить недостающую наблюдаемость (логи + события).
- Сформировать минимальный план изменений по месту (first_run_permissions_integration + activator + status_checker).
