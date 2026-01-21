# Subscription Module

**Feature ID:** F-2025-017-stripe-payment  
**Status:** Phase 0 Complete - Infrastructure Ready

## Структура модуля

```
modules/subscription/
├── __init__.py
├── module.py              # Основной модуль (Phase 3)
├── adapter.py             # Адаптер для UniversalModuleInterface (Phase 3)
├── core/
│   ├── state_machine.py   # State Machine для подписок (Phase 3)
│   └── quota_checker.py   # Проверка квот (Phase 3)
└── providers/
    └── (будут добавлены в Phase 3)
```

## Следующие шаги

- **Phase 1:** База данных и репозитории
- **Phase 2:** Stripe интеграция (базовая)
- **Phase 3:** Subscription Module (сервер)
