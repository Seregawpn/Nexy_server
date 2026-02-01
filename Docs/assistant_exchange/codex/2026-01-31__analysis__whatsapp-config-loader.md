# WhatsApp Config Loader Alignment

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-31
- ID (INS-###): INS-005

## Diagnosis
WhatsApp конфиг читается из features, хотя в unified_config.yaml он в корне, из-за чего интеграция не подписывается.

## Root Cause
Неверный источник конфигурации → loader.get_feature_config("whatsapp") возвращает пусто → enabled остаётся False → нет подписки на whatsapp.request.

## Optimal Fix
Перенести чтение WhatsApp конфигурации на корневой ключ через отдельный метод loader.get_whatsapp_config и использовать его в интеграции/фабрике/guards.

## Verification
Manual: перезапуск, лог подписки, отправка команды send_whatsapp_message, отсутствие dispatch to 0 subscriber(s).

## Запрос/цель
Исправить загрузку WhatsApp конфигурации без изменения структуры unified_config.yaml.

## Контекст
- Файлы: client/config/unified_config_loader.py, client/integration/integrations/whatsapp_integration.py, client/integration/core/integration_factory.py, client/integration/integrations/action_execution_integration.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без breaking changes

## Решения/выводы
- Добавлен root-loader для whatsapp и заменены все обращения к feature-config для этой фичи.

## Найденные проблемы (если review)
- n/a

## Открытые вопросы
- Нужно ли добавить kill-switch для whatsapp в features, если потребуется.

## Следующие шаги
- Прогнать ручную проверку подписки и dispatch.
