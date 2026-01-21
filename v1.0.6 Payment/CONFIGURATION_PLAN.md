# ⚙️ План конфигурации платежной системы

**Feature ID:** F-2025-017-stripe-payment  
**Date:** 2025-12-09

---

## 📋 Обзор

Этот документ описывает все изменения конфигурации, необходимые для реализации платежной системы.

---

## 🔧 Server Configuration

### Файл: `server(Messages)/server/config/unified_config.py`

#### 1. Добавить новые dataclass

```python
from dataclasses import dataclass, field
from typing import Optional, List
import os

@dataclass
class StripeConfig:
    """Конфигурация Stripe API"""
    api_key_test: Optional[str] = None
    api_key_live: Optional[str] = None
    webhook_secret_test: Optional[str] = None
    webhook_secret_live: Optional[str] = None
    use_test_mode: bool = True
    checkout_cooldown_hours: int = 24
    grace_period_days: int = 1
    trial_days: int = 14
    
    @classmethod
    def from_env(cls) -> 'StripeConfig':
        """Загрузка конфигурации из environment variables"""
        return cls(
            api_key_test=os.getenv('STRIPE_API_KEY_TEST'),
            api_key_live=os.getenv('STRIPE_API_KEY_LIVE'),
            webhook_secret_test=os.getenv('STRIPE_WEBHOOK_SECRET_TEST'),
            webhook_secret_live=os.getenv('STRIPE_WEBHOOK_SECRET_LIVE'),
            use_test_mode=os.getenv('STRIPE_USE_TEST_MODE', 'true').lower() == 'true',
            checkout_cooldown_hours=int(os.getenv('STRIPE_CHECKOUT_COOLDOWN_HOURS', '24')),
            grace_period_days=int(os.getenv('STRIPE_GRACE_PERIOD_DAYS', '1')),
            trial_days=int(os.getenv('STRIPE_TRIAL_DAYS', '14'))
        )
    
    @property
    def api_key(self) -> Optional[str]:
        """Возвращает текущий API key (test или live)"""
        return self.api_key_test if self.use_test_mode else self.api_key_live
    
    @property
    def webhook_secret(self) -> Optional[str]:
        """Возвращает текущий webhook secret (test или live)"""
        return self.webhook_secret_test if self.use_test_mode else self.webhook_secret_live

@dataclass
class QuotaConfig:
    """Конфигурация квот для limited_free_trial"""
    daily_limit: int = 5
    weekly_limit: int = 25
    monthly_limit: int = 50
    enabled: bool = True
    
    @classmethod
    def from_env(cls) -> 'QuotaConfig':
        """Загрузка конфигурации из environment variables"""
        return cls(
            daily_limit=int(os.getenv('QUOTA_DAILY_LIMIT', '5')),
            weekly_limit=int(os.getenv('QUOTA_WEEKLY_LIMIT', '25')),
            monthly_limit=int(os.getenv('QUOTA_MONTHLY_LIMIT', '50')),
            enabled=os.getenv('QUOTA_ENABLED', 'true').lower() == 'true'
        )

@dataclass
class SubscriptionConfig:
    """Конфигурация подписок"""
    cache_ttl_seconds: int = 30
    auto_checkout_enabled: bool = True
    trial_warnings_enabled: bool = True
    trial_warning_days: List[int] = field(default_factory=lambda: [2, 1, 0])
    
    @classmethod
    def from_env(cls) -> 'SubscriptionConfig':
        """Загрузка конфигурации из environment variables"""
        warning_days_str = os.getenv('SUBSCRIPTION_TRIAL_WARNING_DAYS', '2,1,0')
        warning_days = [int(d) for d in warning_days_str.split(',')]
        return cls(
            cache_ttl_seconds=int(os.getenv('SUBSCRIPTION_CACHE_TTL_SECONDS', '30')),
            auto_checkout_enabled=os.getenv('SUBSCRIPTION_AUTO_CHECKOUT_ENABLED', 'true').lower() == 'true',
            trial_warnings_enabled=os.getenv('SUBSCRIPTION_TRIAL_WARNINGS_ENABLED', 'true').lower() == 'true',
            trial_warning_days=warning_days
        )
```

#### 2. Обновить `FeaturesConfig`

```python
@dataclass
class FeaturesConfig:
    """Конфигурация фича-флагов"""
    use_module_coordinator: bool = True
    use_workflow_integrations: bool = True
    use_fallback_manager: bool = True
    forward_assistant_actions: bool = False  # Существующий
    # NEW: Payment system feature flags
    enable_payment_system: bool = False  # Feature flag для включения/выключения
    enable_quota_enforcement: bool = True
    enable_auto_checkout: bool = True
    enable_trial_warnings: bool = True
    
    @classmethod
    def from_env(cls) -> 'FeaturesConfig':
        return cls(
            use_module_coordinator=os.getenv('USE_MODULE_COORDINATOR', 'true').lower() == 'true',
            use_workflow_integrations=os.getenv('USE_WORKFLOW_INTEGRATIONS', 'true').lower() == 'true',
            use_fallback_manager=os.getenv('USE_FALLBACK_MANAGER', 'true').lower() == 'true',
            forward_assistant_actions=os.getenv('FORWARD_ASSISTANT_ACTIONS', 'false').lower() == 'true',
            # NEW: Payment system flags
            enable_payment_system=os.getenv('ENABLE_PAYMENT_SYSTEM', 'false').lower() == 'true',
            enable_quota_enforcement=os.getenv('ENABLE_QUOTA_ENFORCEMENT', 'true').lower() == 'true',
            enable_auto_checkout=os.getenv('ENABLE_AUTO_CHECKOUT', 'true').lower() == 'true',
            enable_trial_warnings=os.getenv('ENABLE_TRIAL_WARNINGS', 'true').lower() == 'true'
        )
```

#### 3. Обновить `KillSwitchesConfig`

```python
@dataclass
class KillSwitchesConfig:
    """Конфигурация kill-switch"""
    disable_module_coordinator: bool = False
    disable_workflow_integrations: bool = False
    disable_forward_assistant_actions: bool = False  # Существующий
    # NEW: Payment system kill-switches
    disable_payment_system: bool = False  # Kill-switch для экстренного отключения
    disable_quota_enforcement: bool = False
    disable_auto_checkout: bool = False
    
    @classmethod
    def from_env(cls) -> 'KillSwitchesConfig':
        return cls(
            disable_module_coordinator=os.getenv('NEXY_KS_DISABLE_MODULE_COORDINATOR', 'false').lower() == 'true',
            disable_workflow_integrations=os.getenv('NEXY_KS_DISABLE_WORKFLOW_INTEGRATIONS', 'false').lower() == 'true',
            disable_forward_assistant_actions=os.getenv('NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS', 'false').lower() == 'true',
            # NEW: Payment system kill-switches
            disable_payment_system=os.getenv('NEXY_KS_DISABLE_PAYMENT_SYSTEM', 'false').lower() == 'true',
            disable_quota_enforcement=os.getenv('NEXY_KS_DISABLE_QUOTA_ENFORCEMENT', 'false').lower() == 'true',
            disable_auto_checkout=os.getenv('NEXY_KS_DISABLE_AUTO_CHECKOUT', 'false').lower() == 'true'
        )
```

#### 4. Обновить `UnifiedServerConfig`

```python
@dataclass
class UnifiedServerConfig:
    """
    Единая конфигурация сервера
    """
    # ... существующие поля ...
    features: FeaturesConfig = field(default_factory=FeaturesConfig.from_env)
    kill_switches: KillSwitchesConfig = field(default_factory=KillSwitchesConfig.from_env)
    # ... другие существующие поля ...
    
    # NEW: Payment system configuration
    stripe: StripeConfig = field(default_factory=StripeConfig.from_env)
    quota: QuotaConfig = field(default_factory=QuotaConfig.from_env)
    subscription: SubscriptionConfig = field(default_factory=SubscriptionConfig.from_env)
    
    # ... остальные поля ...
```

---

## 🔐 Environment Variables

### Обязательные переменные (для production)

```bash
# Stripe API Keys
STRIPE_API_KEY_TEST=sk_test_...
STRIPE_API_KEY_LIVE=sk_live_...
STRIPE_WEBHOOK_SECRET_TEST=whsec_...
STRIPE_WEBHOOK_SECRET_LIVE=whsec_...

# Feature Flags
ENABLE_PAYMENT_SYSTEM=true
ENABLE_QUOTA_ENFORCEMENT=true
ENABLE_AUTO_CHECKOUT=true
ENABLE_TRIAL_WARNINGS=true

# Kill Switches (по умолчанию false)
NEXY_KS_DISABLE_PAYMENT_SYSTEM=false
NEXY_KS_DISABLE_QUOTA_ENFORCEMENT=false
NEXY_KS_DISABLE_AUTO_CHECKOUT=false
```

### Опциональные переменные (с дефолтами)

```bash
# Stripe Settings
STRIPE_USE_TEST_MODE=true
STRIPE_CHECKOUT_COOLDOWN_HOURS=24
STRIPE_GRACE_PERIOD_DAYS=1
STRIPE_TRIAL_DAYS=14

# Quota Settings
QUOTA_DAILY_LIMIT=5
QUOTA_WEEKLY_LIMIT=25
QUOTA_MONTHLY_LIMIT=50
QUOTA_ENABLED=true

# Subscription Settings
SUBSCRIPTION_CACHE_TTL_SECONDS=30
SUBSCRIPTION_AUTO_CHECKOUT_ENABLED=true
SUBSCRIPTION_TRIAL_WARNINGS_ENABLED=true
SUBSCRIPTION_TRIAL_WARNING_DAYS=2,1,0
```

---

## 📝 Проверка конфигурации

### В коде (при инициализации)

```python
# В StreamingWorkflowIntegration.__init__()
def __init__(self, config: UnifiedServerConfig, ...):
    self.config = config
    
    # Проверка обязательных полей
    if config.features.enable_payment_system:
        if not config.stripe.api_key:
            raise ValueError(
                "[F-2025-017-stripe-payment] Stripe API key not configured. "
                "Set STRIPE_API_KEY_TEST or STRIPE_API_KEY_LIVE"
            )
        if not config.stripe.webhook_secret:
            logger.warning(
                "[F-2025-017-stripe-payment] Stripe webhook secret not configured. "
                "Webhook verification will fail."
            )
```

---

## ✅ Чеклист реализации

- [ ] Добавить `StripeConfig` dataclass
- [ ] Добавить `QuotaConfig` dataclass
- [ ] Добавить `SubscriptionConfig` dataclass
- [ ] Обновить `FeaturesConfig` с payment flags
- [ ] Обновить `KillSwitchesConfig` с payment kill-switches
- [ ] Обновить `UnifiedServerConfig` с новыми полями
- [ ] Добавить проверки конфигурации при инициализации
- [ ] Обновить документацию с environment variables

---

**Статус:** ✅ Готово к реализации




