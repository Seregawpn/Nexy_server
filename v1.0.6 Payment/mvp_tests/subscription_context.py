#!/usr/bin/env python3
"""
Subscription Context - получение контекста подписки для LLM
MVP 5: Subscription Context

Feature ID: F-2025-017-stripe-payment
"""
from typing import Dict, Optional
from datetime import datetime
from subscription_repository import SubscriptionRepository

class SubscriptionContext:
    """Класс для получения контекста подписки"""
    
    def __init__(self, repository: Optional[SubscriptionRepository] = None):
        """Инициализация с repository"""
        self.repository = repository or SubscriptionRepository()
    
    def get_subscription_context(self, hardware_id: str) -> Dict:
        """
        Получить контекст подписки для передачи в LLM
        
        ⚠️ ВАЖНО: 
        1. last_payment_at и last_payment_amount получаются из таблицы payments,
           а не из subscriptions (согласно DOCUMENTATION_CONSISTENCY_FIXES.md)
        2. last_payment_* берется только из платежей со статусом 'succeeded',
           чтобы исключить failed/pending платежи
        3. Этот метод должен вызываться ПОСЛЕ get_or_create_subscription(),
           иначе для нового пользователя будет возвращен status=None вместо paid_trial
        
        Args:
            hardware_id: Уникальный ID устройства
        
        Returns:
            Dict с контекстом подписки для LLM
        """
        # Получаем подписку из БД
        subscription = self.repository.get_subscription(hardware_id)
        
        if not subscription:
            # Если подписки нет, возвращаем контекст для нового пользователя
            # ⚠️ ВАЖНО: В основной логике trial создается на первом запросе через get_or_create_subscription()
            # Этот метод должен вызываться ПОСЛЕ get_or_create_subscription(), иначе будет status=None
            return {
                "status": None,
                "message": "No subscription found. Trial will be activated on first request."
            }
        
        # ⭐ КРИТИЧНО: Получаем только успешные платежи (status='succeeded')
        # Это исключает failed/pending платежи, которые могут дать неверный контекст для LLM
        payments = self.repository.get_payments(hardware_id, limit=1, status='succeeded')
        last_payment = payments[0] if payments else None
        
        # Формируем контекст
        context = {
            "status": subscription.get('status'),
            "paid_trial_end_at": self._format_timestamp(subscription.get('paid_trial_end_at')),
            "current_period_end": self._format_timestamp(subscription.get('current_period_end')),
            "cancel_at_period_end": subscription.get('cancel_at_period_end', False),
            "payment_method_id": subscription.get('payment_method_id'),
            "stripe_subscription_id": subscription.get('stripe_subscription_id'),
            
            # ⚠️ last_payment_at и last_payment_amount получаются из таблицы payments
            "last_payment_at": self._format_timestamp(last_payment.get('created_at')) if last_payment else None,
            "last_payment_amount": float(last_payment.get('amount', 0)) / 100 if last_payment else None,  # Конвертируем из центов
            
            "grace_period_end_at": self._format_timestamp(subscription.get('grace_period_end_at')),
            
            # Будущие поля (если будут добавлены в БД)
            "is_admin_activated": subscription.get('is_admin_activated', False),
            "is_grandfathered": subscription.get('is_grandfathered', False),
        }
        
        return context
    
    def _format_timestamp(self, timestamp) -> Optional[str]:
        """Форматировать timestamp в ISO строку"""
        if not timestamp:
            return None
        
        if isinstance(timestamp, datetime):
            return timestamp.isoformat()
        elif isinstance(timestamp, str):
            return timestamp
        else:
            return None
    
    def get_context_summary(self, hardware_id: str) -> str:
        """
        Получить краткое текстовое описание статуса подписки
        
        Используется для логирования и отладки
        """
        context = self.get_subscription_context(hardware_id)
        
        if context.get('status') is None:
            return "No subscription (trial will be activated on first request)"
        
        status = context['status']
        summary_parts = [f"Status: {status}"]
        
        if context.get('paid_trial_end_at'):
            summary_parts.append(f"Trial ends: {context['paid_trial_end_at']}")
        
        if context.get('current_period_end'):
            summary_parts.append(f"Period ends: {context['current_period_end']}")
        
        if context.get('cancel_at_period_end'):
            summary_parts.append("(Scheduled for cancellation)")
        
        if context.get('last_payment_at'):
            summary_parts.append(f"Last payment: {context['last_payment_at']} (${context.get('last_payment_amount', 0):.2f})")
        
        return " | ".join(summary_parts)
