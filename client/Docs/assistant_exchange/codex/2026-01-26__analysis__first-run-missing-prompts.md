# First Run Missing Prompts

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-26
- ID (INS-###): INS-000 (registry missing)

## Diagnosis
First-run V2 последовательно запускает шаги, но реальные диалоги появляются только для promptable разрешений с доступными активаторами; остальные шаги выполняются без видимого prompt.

## Root Cause
Конфигурация `permissions_v2.steps` + реализация проберов → Accessibility/Full Disk Access идут через Settings-only, Contacts зависит от доступности Contacts framework → пользователь видит только mic/screen/input.

## Optimal Fix
Проверить доступность Contacts/Quartz в упакованном рантайме, логирование trigger/ledger, и при необходимости обеспечить fallback открытия Settings для недоступных диалогов.

## Verification
- Логи `[CONTACTS_PROBER]`, `[AX_PROBER]`, `[FDA_PROBER]`
- `permission_ledger.json` содержит все 6 шагов
- System Settings открывается на шагах accessibility/full_disk_access

## Запрос/цель
Проанализировать, почему не запрашиваются все разрешения при первом запуске.

## Контекст
- Файлы: integration/integrations/first_run_permissions_integration.py, modules/permissions/v2/orchestrator.py, modules/permissions/v2/probers/*, config/unified_config.yaml
- Документы: Docs/first_run_flow_spec.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- Диалоги появляются только там, где trigger реально доступен в рантайме.
- Settings-only шаги не показывают модальные запросы.

## Открытые вопросы
- Доступен ли `Contacts` framework в .app bundle на проблемной сборке?

## Следующие шаги
- Проверить логи проберов и ledger на конкретном запуске.
- При отсутствии Contacts/Quartz — исправить упаковку или добавить Settings fallback.
