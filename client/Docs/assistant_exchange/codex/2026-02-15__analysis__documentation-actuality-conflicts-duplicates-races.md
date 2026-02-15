# Анализ актуальности документации: конфликты, дубли, race-risk

Дата: 2026-02-15
Область: `Docs/` + сверка с текущим кодом клиента

## Ключевой вывод
Документация частично неактуальна: канонические документы содержат конфликтующие правила и множество ссылок на отсутствующие артефакты. Это создаёт дублирование источников истины и риск внедрения конкурирующей логики.

## Подтверждённые конфликты

1. **Конфликт источника порядка first-run permissions**
- `Docs/PROJECT_REQUIREMENTS.md` фиксирует источник порядка как `integrations.permissions.required_permissions`.
- `Docs/first_run_flow_spec.md` фиксирует источник порядка как `integrations.permissions_v2.order`.
- В коде V2 действительно используется полный `permissions_v2` конфиг.

2. **Конфликт модели проверки разрешений (single-probe vs polling)**
- `Docs/first_run_flow_spec.md` декларирует «no polling loops / single post-trigger probe».
- В коде `modules/permissions/v2/orchestrator.py` используется полноценный polling цикл (`_poll_until_done`) для `AUTO_DIALOG` шагов.

3. **Конфликт Source of Truth по оси `firstRun` внутри одного документа**
- В `Docs/STATE_CATALOG.md` в карточке оси `firstRun` source-of-truth = ledger (`permission_ledger.json`).
- В ownership-таблице того же документа source-of-truth для `firstRun` указан как `permissions_first_run_completed.flag`.

4. **Конфликт статуса актуальности карты требований**
- `Docs/REQUIREMENTS_SOURCE_MAP.md` помечает множество документов как «✅ Актуален», но эти файлы отсутствуют в репозитории.
- Там же указан GAP «отсутствует PROJECT_REQUIREMENTS.md», при том что файл существует.

## Дубли и неактуальные ссылки

1. **Дублирующие/расходящиеся карты документации**
- `Docs/README.md`, `Docs/DOCUMENTATION_MAP.md`, `Docs/REQUIREMENTS_SOURCE_MAP.md` одновременно описывают «канонические» документы, но дают несовместимые списки.

2. **Ссылки на несуществующий файл gateway-реализации**
- `Docs/DOCUMENTATION_MAP.md` и `Docs/ARCHITECTURE_OVERVIEW.md` ссылаются на `integration/core/gateways.py`, тогда как фактическая реализация — директория `integration/core/gateways/`.

3. **Массовые битые ссылки на отсутствующие документы/скрипты**
- Примеры отсутствующих ссылок: `Docs/CURRENT_STATUS_REPORT.md`, `Docs/GLOBAL_DELIVERY_PLAN.md`, `Docs/TAL_TESTING_CHECKLIST.md`, `Docs/TRAY_TERMINATION_FIX.md`, `scripts/test_first_run_integration.sh`, `modules/permission_restart/core/restart_scheduler.py`.

## Race-risk (документационный)

1. **Race внедрения из-за двух конкурирующих owner-политик first-run**
- Разные документы задают разный owner-путь (legacy required_permissions vs V2 order/ledger).
- Риск: изменения могут попасть сразу в два пути (legacy + V2), что создаст недетерминированное поведение в first-run/permission-restart.

2. **Race по выбору механизма проверки шага permission flow**
- Документы требуют single-probe, код реально использует polling loop.
- Риск: при «фиксах по документации» можно частично удалить polling-гварды и вернуть застревания/ложные исходы в ожидании пользователя.

## Минимальный план исправления документации (без реархитектуры)

1. Назначить единый SoT-документ-индекс: `Docs/README.md`.
2. Удалить/архивировать устаревшие разделы в `Docs/DOCUMENTATION_MAP.md` и `Docs/REQUIREMENTS_SOURCE_MAP.md`.
3. Синхронизировать first-run policy в тройке документов:
   - `Docs/PROJECT_REQUIREMENTS.md`
   - `Docs/first_run_flow_spec.md`
   - `Docs/STATE_CATALOG.md`
4. Привести все ссылки к реальным путям (`integration/core/gateways/`, существующие скрипты/доки).
5. Зафиксировать явный статус: `legacy removed / v2 only` для permission flow, чтобы убрать двойной owner path.

## Проверенные артефакты
- Документы: `Docs/README.md`, `Docs/DOCUMENTATION_MAP.md`, `Docs/REQUIREMENTS_SOURCE_MAP.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/first_run_flow_spec.md`, `Docs/STATE_CATALOG.md`, `Docs/ARCHITECTURE_OVERVIEW.md`.
- Код: `integration/integrations/first_run_permissions_integration.py`, `modules/permissions/v2/orchestrator.py`, `config/unified_config.yaml`, `integration/core/integration_factory.py`, `integration/core/simple_module_coordinator.py`.
