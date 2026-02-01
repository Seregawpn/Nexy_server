# Update First-Run Rules

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Текущие правила first-run описывали status-check и settings-fallback, что не соответствует согласованной логике «без status-check, sequential activation, settings-only только для Full Disk Access».

## Root Cause
Документы расходились с текущими намерениями по UX и потоку first-run, создавая риск неправильной реализации и диагностики.

## Optimal Fix
Обновить спецификацию first-run и требования REQ-010 под последовательную активацию без статус-проверок и с settings-only для Full Disk Access.

## Verification
Сверить обновленные документы с конфигом `integrations.permissions.required_permissions` и фактической логикой first-run; повторный запуск после очистки флагов.

## Запрос/цель
Обновить правила и документировать идеальную архитектуру first-run под согласованную логику.

## Контекст
- Файлы: Docs/first_run_flow_spec.md, Docs/PROJECT_REQUIREMENTS.md, PERMISSIONS_REPORT.md
- Документы: Docs/PROJECT_REQUIREMENTS.md (REQ-010)
- Ограничения: Accessibility не изменяется

## Решения/выводы
- Убраны ссылки на status-check, smart/legacy режимы и settings-fallback (кроме Full Disk Access).
- Зафиксирована последовательная активация разрешений по списку.

## Открытые вопросы
- Требуется ли обновить связанные тестовые чек-листы (если они ожидают status-check логов).

## Следующие шаги
- Проверить актуальность `scripts/test_first_run_integration.sh` относительно новых правил.
- При необходимости обновить чек-листы в Docs.
