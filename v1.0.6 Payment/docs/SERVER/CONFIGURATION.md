# ⚙️ Конфигурация сервера

**→ Основной документ:** `../CONFIGURATION_PLAN.md`

---

## 📋 Краткое описание

План конфигурации для платежной системы включает:
- `StripeConfig` — API keys, webhook secrets
- `QuotaConfig` — лимиты (5/25/50)
- `SubscriptionConfig` — cache TTL, auto checkout
- `FeaturesConfig` — feature flags
- `KillSwitchesConfig` — kill switches

---

## 🔗 Полная документация

**См. `../CONFIGURATION_PLAN.md`** для:
- Детального описания всех dataclass
- Environment variables
- Примеров кода
- Валидации конфигурации

---

## 📝 Быстрая ссылка

**Файл для изменения:** `server(Messages)/server/config/unified_config.py`

**Основные компоненты:**
- `StripeConfig.from_env()` — загрузка из environment variables
- `QuotaConfig.from_env()` — лимиты квот
- `SubscriptionConfig.from_env()` — настройки подписок
- `FeaturesConfig.enable_payment_system` — feature flag
- `KillSwitchesConfig.disable_payment_system` — kill switch

---

**Следующий шаг:** Откройте `../CONFIGURATION_PLAN.md` для детального плана

