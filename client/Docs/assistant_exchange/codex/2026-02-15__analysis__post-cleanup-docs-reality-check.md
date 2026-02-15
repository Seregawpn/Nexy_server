# Post-cleanup Docs Reality Check

Дата: 2026-02-15

## Итог
Полного 100% соответствия «доки = код без переходных зон» пока нет.
После cleanup остались осознанные legacy-мосты и compatibility paths.

## Что подтверждено

- `scripts/verify_doc_links.py` проходит (битых ссылок в каноне нет).
- Startup SoT в `Docs/FLOW_INTERACTION_SPEC.md` синхронизирован на `IntegrationFactory.STARTUP_ORDER`.

## Остаточные расхождения/переходные зоны

1. Event compatibility bridge:
- Доки фиксируют `app.state_changed` как мост совместимости.
- Код реально публикует и использует `app.state_changed`:
  - `integration/core/state_manager.py`
  - `integration/integrations/screenshot_capture_integration.py`
  - `integration/integrations/interrupt_management_integration.py`

2. Permissions restart legacy-compat:
- В доках: legacy `permissions.first_run_restart_pending` остаётся для совместимости.
- В коде: путь присутствует (частично заморожен в V2, но не удалён):
  - `integration/integrations/permission_restart_integration.py`
  - `integration/core/simple_module_coordinator.py`
  - тесты `tests/test_coordinator_critical_subscriptions.py`

3. First-run verification wording:
- В части docs уже обновлено под polling в V2,
- но в отдельных местах ещё встречаются старые формулировки про single-probe (нужно дожать унификацию по всем документам).

4. Speech legacy compatibility:
- Доки: legacy text-tunneling и `speech.playback.request` отмечены как compatibility.
- Код: compatibility path всё ещё существует:
  - `integration/integrations/grpc_client_integration.py`
  - `integration/integrations/tts_integration.py`
  - `integration/integrations/action_execution_integration.py`

## Вывод

Состояние: **практически консистентно для текущей эксплуатации**, но не «финально очищено от legacy». Это контролируемая переходная архитектура, а не полный hard-cut.

## Рекомендация next step (финализация)

1. Решить судьбу `app.state_changed`: либо убрать мост, либо явно закрепить как поддерживаемый compatibility event.
2. Для permissions: завершить V2-only cutover и удалить runtime handling `permissions.first_run_restart_pending` после подтверждения тестами.
3. Для speech: определить срок удаления text-chunk legacy path и `speech.playback.request` compatibility.
4. После каждого cutover прогонять `scripts/verify_doc_links.py` + профильные tests.
