# WhatsApp Module Plan Review

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-29
- ID (INS-###): INS-UNKNOWN

## Diagnosis
План описан на высоком уровне, но не привязан к существующим интеграциям/feature flags/EventBus, поэтому риск появления второго источника истины и обхода центра управления.

## Root Cause
Отсутствие явного размещения логики в слоях архитектуры клиента/сервера → разрозненное управление флагами и командами → риск конфликтов с текущими Messages/ActionExecution и prompt gating.

## Optimal Fix
Сформировать план как новую клиентскую интеграцию + модуль + строгая регистрация feature flag и команд через текущие централизованные точки (unified_config, action_execution_integration, server response validation).

## Verification
DoD: фича отключается полностью через unified_config и server env; при включении — единый путь команд и единый источник истины; QR онбординг видим и идемпотентен.

## Запрос/цель
Оценить предложенный план интеграции WhatsApp и дать архитектурно-совместимый план.

## Контекст
- Файлы: client/integration/integrations/action_execution_integration.py, Docs/FEATURE_FLAGS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md, Whatsapp/ARCHITECTURE.md
- Документы: AGENTS.md, Docs/_archive/CODEX_PROMPT.md
- Ограничения: без реархитектуры, без новых источников истины

## Решения/выводы
- Нужна интеграция в существующий EventBus и feature gating, иначе будет дублирование и обход центра управления.
- QR онбординг должен быть отдельным состоянием и событийным контрактом, а не локальным флагом.

## Открытые вопросы
- Где будет храниться WhatsApp сессия (клиентский sandbox path)?
- Нужен ли серверный command validation для новых команд (whatsapp_send/read)?

## Следующие шаги
- Привязать план к конкретным слоям архитектуры и точкам расширения.
- Уточнить контракт событий и фич-флаг на клиенте и сервере.
