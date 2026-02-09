"""
Subscription Module - Payment System Integration

Feature ID: F-2025-017-stripe-payment

Exports:
    - SubscriptionModule: Main module class
    - get_subscription_module: Singleton accessor  
    - initialize_subscription_module: Async initialization (call at startup)
    - CanProcessResult: Result of access check
"""

from .subscription_module import (
    SubscriptionModule,
    get_subscription_module,
    initialize_subscription_module,
    CanProcessResult
)

__all__ = [
    'SubscriptionModule',
    'get_subscription_module',
    'initialize_subscription_module',
    'CanProcessResult'
]

