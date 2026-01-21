#!/usr/bin/env python3
"""
Stripe Service для работы с Stripe API
MVP 3: Stripe Service - создание Checkout Session

Feature ID: F-2025-017-stripe-payment
"""
import stripe
import time
import hashlib
import json
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class StripeService:
    """Service для работы с Stripe API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Инициализация Stripe Service"""
        self.api_key = api_key or os.getenv('STRIPE_SECRET_KEY')
        if not self.api_key:
            raise ValueError("STRIPE_SECRET_KEY not found")
        stripe.api_key = self.api_key
    
    def create_checkout_session(
        self,
        hardware_id: str,
        success_url: str,
        cancel_url: str,
        price_id: Optional[str] = None,
        customer_id: Optional[str] = None
    ) -> Dict:
        """
        Создать Checkout Session для подписки
        
        ⭐ КРИТИЧНО (из ARCHITECTURE_FIXES.md):
        - hardware_id ОБЯЗАТЕЛЬНО должен быть в metadata
        - Использовать idempotency_key для предотвращения дубликатов
        
        Args:
            hardware_id: Уникальный ID устройства (ОБЯЗАТЕЛЬНО)
            success_url: URL для редиректа после успешной оплаты
            cancel_url: URL для редиректа при отмене
            price_id: Опциональный Stripe Price ID (если не указан, создается динамически)
            customer_id: Опциональный Stripe Customer ID (если уже существует)
        
        Returns:
            Dict с checkout_url, session_id, customer_id, subscription_id
        """
        try:
            print(f"[STRIPE] Creating checkout session for hardware_id: {hardware_id}")
            
            # Параметры для создания сессии
            session_params = {
                'mode': 'subscription',
                'success_url': success_url,
                'cancel_url': cancel_url,
                
                # ⭐ КРИТИЧНО: Обязательная привязка hardware_id в metadata Checkout Session
                # Это необходимо для восстановления контекста в webhook handler
                'metadata': {
                    'hardware_id': hardware_id,
                },
                
                # ⭐ КРИТИЧНО: hardware_id в subscription metadata
                # Это необходимо для восстановления контекста в событиях customer.subscription.updated и т.д.
                # Большинство событий (invoice.payment_succeeded, customer.subscription.updated) приходят с subscription объектом
                'subscription_data': {
                    'metadata': {
                        'hardware_id': hardware_id,
                    },
                },
                
                # ⭐ Промокоды отключены (по требованию)
                # 'allow_promotion_codes': False,  # Не указываем, чтобы отключить промокоды
                
                # ⭐ Методы оплаты: Карта, Link, Apple Pay, Google Pay
                # - 'card': Обычные карты (Visa, Mastercard, etc.)
                # - 'link': Stripe Link (быстрая оплата с сохраненными данными)
                # - Apple Pay и Google Pay активируются автоматически, если:
                #   1. Включены в Stripe Dashboard (Settings → Payment methods)
                #   2. Домен верифицирован (для production) или используется localhost
                #   3. Браузер/устройство поддерживает эти методы
                # ⚠️ ВАЖНО: apple_pay и google_pay НЕ являются валидными значениями для payment_method_types
                # Они активируются автоматически Stripe через другие механизмы
                'payment_method_types': ['card', 'link'],
                
                # ⭐ Опционально: Настройки для Apple Pay / Google Pay
                # Эти настройки позволяют явно контролировать поведение Apple Pay/Google Pay
                # Если не указаны, Stripe использует настройки по умолчанию из Dashboard
                'payment_method_options': {
                    'card': {
                        'request_three_d_secure': 'automatic',  # 3D Secure для безопасности
                    },
                },
            }
            
            # ⭐ КРИТИЧНО: Для customer metadata в subscription mode нужно создать customer заранее
            # В subscription mode customer создается автоматически, но metadata нельзя установить через Checkout
            # Решение: создаем customer заранее с metadata (если не передан customer_id)
            if not customer_id:
                # Создаем customer с hardware_id в metadata заранее
                customer = self.create_customer(hardware_id=hardware_id)
                customer_id = customer['customer_id']
                print(f"[STRIPE] Customer created with metadata: {customer_id}")
            
            # Используем customer_id (созданный или переданный)
            session_params['customer'] = customer_id
            
            # Если указан price_id, используем его
            if price_id:
                session_params['line_items'] = [{
                    'price': price_id,
                    'quantity': 1,
                }]
            else:
                # Создаем динамический price
                session_params['line_items'] = [{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Nexy Premium',
                            'description': 'Unlimited access to Nexy AI Assistant',
                        },
                        'recurring': {
                            'interval': 'month',
                        },
                        'unit_amount': 2000,  # $20.00 в центах
                    },
                    'quantity': 1,
                }]
            
            # ⭐ КРИТИЧНО: Idempotency key для предотвращения дубликатов при ретраях
            # Включает хеш параметров, чтобы при изменении параметров создавался новый ключ
            # Формат: checkout_{hardware_id}_{день}_{hash_params}
            # Это гарантирует, что одинаковые параметры в один день = один checkout
            day_key = int(time.time() / 86400)
            
            # Создаем хеш из ключевых параметров, которые влияют на результат
            params_for_hash = {
                'payment_method_types': sorted(session_params.get('payment_method_types', [])),
                'price_id': price_id,
                'customer_id': customer_id,
                'success_url': session_params.get('success_url'),
                'cancel_url': session_params.get('cancel_url'),
            }
            # Если price_id не указан, включаем unit_amount в хеш
            if not price_id and 'line_items' in session_params:
                line_item = session_params['line_items'][0]
                if 'price_data' in line_item:
                    params_for_hash['unit_amount'] = line_item['price_data'].get('unit_amount')
                    params_for_hash['currency'] = line_item['price_data'].get('currency')
            
            params_hash = hashlib.md5(
                json.dumps(params_for_hash, sort_keys=True).encode()
            ).hexdigest()[:8]
            
            idempotency_key = f"checkout_{hardware_id}_{day_key}_{params_hash}"
            
            # ⭐ КРИТИЧНО: Idempotency key передается как именованный параметр функции create()
            # Это более безопасно и явно, чем передача в session_params
            session = stripe.checkout.Session.create(
                **session_params,
                idempotency_key=idempotency_key
            )
            
            result = {
                'checkout_url': session.url,
                'session_id': session.id,
                'customer_id': session.customer,
                'subscription_id': session.subscription,
                'idempotency_key': idempotency_key,
            }
            
            print(f"[STRIPE] ✅ Checkout session created: {session.id}")
            print(f"[STRIPE] URL: {session.url}")
            print(f"[STRIPE] Idempotency key: {idempotency_key}")
            
            # Проверка metadata
            if session.metadata and session.metadata.get('hardware_id') == hardware_id:
                print(f"[STRIPE] ✅ hardware_id в metadata подтвержден: {hardware_id}")
            else:
                print(f"[STRIPE] ⚠️  WARNING: hardware_id не найден в metadata!")
            
            return result
            
        except stripe.error.IdempotencyError as e:
            print(f"[STRIPE] ⚠️  Idempotency error (дубликат): {e}")
            # При idempotency error можно попробовать получить существующую сессию
            # Но для MVP 3 просто пробрасываем ошибку
            raise
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Stripe error: {e}")
            raise
        except Exception as e:
            print(f"[STRIPE] ❌ Error creating checkout: {e}")
            raise
    
    def get_checkout_session(self, session_id: str) -> Dict:
        """Получить информацию о Checkout Session"""
        try:
            session = stripe.checkout.Session.retrieve(session_id)
            return {
                'id': session.id,
                'status': session.status,
                'customer_id': session.customer,
                'subscription_id': session.subscription,
                'payment_status': session.payment_status,
                'metadata': dict(session.metadata) if session.metadata else {},
                'url': session.url,
            }
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Error retrieving session: {e}")
            raise
    
    def create_customer(
        self,
        hardware_id: str,
        email: Optional[str] = None
    ) -> Dict:
        """
        Создать Stripe Customer
        
        ⭐ КРИТИЧНО: hardware_id ОБЯЗАТЕЛЬНО должен быть в metadata
        """
        try:
            print(f"[STRIPE] Creating customer for hardware_id: {hardware_id}")
            
            customer_params = {
                'metadata': {
                    'hardware_id': hardware_id,
                },
            }
            
            if email:
                customer_params['email'] = email
            
            customer = stripe.Customer.create(**customer_params)
            
            print(f"[STRIPE] ✅ Customer created: {customer.id}")
            
            return {
                'customer_id': customer.id,
                'email': customer.email,
                'metadata': dict(customer.metadata) if customer.metadata else {},
            }
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Error creating customer: {e}")
            raise
    
    def create_portal_session(
        self,
        customer_id: str,
        return_url: Optional[str] = None
    ) -> Dict:
        """
        Создать Customer Portal Session для управления подпиской
        
        MVP 10: Customer Portal для обновления payment method, просмотра истории платежей и т.д.
        
        Args:
            customer_id: Stripe Customer ID
            return_url: URL для возврата из Portal (deep link)
        
        Returns:
            Dict с portal_url и session_id
        """
        try:
            print(f"[STRIPE] Creating portal session for customer: {customer_id}")
            
            # Формируем return_url для deep link
            if not return_url:
                base_url = os.getenv('DEEP_LINK_BASE_URL', 'nexy://payment/')
                return_url = f"{base_url}portal_return"
            
            session_params = {
                'customer': customer_id,
                'return_url': return_url,
            }
            
            # Создаем Portal Session
            session = stripe.billing_portal.Session.create(**session_params)
            
            print(f"[STRIPE] ✅ Portal session created: {session.url}")
            
            return {
                'portal_url': session.url,
                'session_id': session.id,
            }
        except stripe.error.StripeError as e:
            print(f"[STRIPE] ❌ Error creating portal session: {e}")
            raise
        except Exception as e:
            print(f"[STRIPE] ❌ Error creating portal session: {e}")
            raise
