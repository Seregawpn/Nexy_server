# Feature Architecture Compliance Check

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-11
- ID (INS-###): INS-005

## Diagnosis
Обнаружены несоответствия между cookbook и фактическими API/конфигом: упоминание несуществующего метода загрузчика и расхождение реестра флагов с unified_config.

## Root Cause
Обновления шаблонов и документации выполнены частично → ссылки и примеры не синхронизированы → риск архитектурного дрейфа.

## Optimal Fix
Синхронизировать cookbook, реестр флагов и unified_config.yaml, чтобы все примеры соответствовали реальным API и структуре конфигурации.

## Verification
DoD: cookbook использует существующие методы загрузчика, feature flags зарегистрированы и отражены в unified_config.yaml.

## Запрос/цель
Проверить соответствие обновленных шаблонов архитектуре и указать необходимые правки.

## Контекст
- Файлы: integration/integrations/_template_integration.py, scripts/verify_cookbook_poc.py, Docs/guides/COOKBOOK_ADD_FEATURE.md, client/config/unified_config_loader.py, client/config/unified_config.yaml, Docs/FEATURE_FLAGS.md
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md

## Решения/выводы
- TemplateIntegration соответствует EventBus envelope и использует UnifiedConfigLoader.get_feature_config().
- В cookbook осталась ссылка на get_config(), которого нет в UnifiedConfigLoader.
- Реестр флагов содержит template_feature, но unified_config.yaml не содержит этого флага.

## Открытые вопросы
- Нужно ли добавить template_feature/ks_template_feature в unified_config.yaml или убрать их из реестра?

## Следующие шаги
- Исправить ссылку на API в cookbook.
- Синхронизировать Docs/FEATURE_FLAGS.md с unified_config.yaml.
