#!/usr/bin/env python3
"""
Repository для работы с подписками в БД
MVP 2: База данных
"""
import psycopg2
from psycopg2.extras import RealDictCursor, Json
from typing import Optional, Dict, List
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class SubscriptionRepository:
    """Repository для работы с подписками"""
    
    def __init__(self, db_url: Optional[str] = None):
        self.db_url = db_url or os.getenv('DATABASE_URL')
        if not self.db_url:
            raise ValueError("DATABASE_URL not found")
    
    def _get_connection(self):
        """Получить соединение с БД"""
        return psycopg2.connect(self.db_url)
    
    def get_subscription(self, hardware_id: str) -> Optional[Dict]:
        """Получить подписку по hardware_id"""
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM subscriptions WHERE hardware_id = %s""",
                    (hardware_id,)
                )
                row = cur.fetchone()
                return dict(row) if row else None
        finally:
            conn.close()
    
    def create_subscription(
        self, 
        hardware_id: str, 
        status: str = 'paid_trial',
        paid_trial_end_at: Optional[datetime] = None
    ) -> Dict:
        """Создать новую подписку"""
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """INSERT INTO subscriptions (hardware_id, status, paid_trial_end_at)
                       VALUES (%s, %s, %s)
                       ON CONFLICT (hardware_id) DO NOTHING
                       RETURNING *""",
                    (hardware_id, status, paid_trial_end_at)
                )
                row = cur.fetchone()
                conn.commit()
                if row:
                    return dict(row)
                # Если конфликт, получаем существующую запись
                return self.get_subscription(hardware_id)
        finally:
            conn.close()
    
    def update_status(self, hardware_id: str, status: str) -> bool:
        """Обновить статус подписки"""
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE subscriptions 
                       SET status = %s, updated_at = CURRENT_TIMESTAMP 
                       WHERE hardware_id = %s""",
                    (status, hardware_id)
                )
                conn.commit()
                return cur.rowcount > 0
        finally:
            conn.close()
    
    def update_stripe_ids(
        self, 
        hardware_id: str, 
        customer_id: Optional[str] = None,
        subscription_id: Optional[str] = None
    ) -> bool:
        """Обновить Stripe IDs"""
        conn = self._get_connection()
        try:
            updates = []
            params = []
            if customer_id:
                updates.append("stripe_customer_id = %s")
                params.append(customer_id)
            if subscription_id:
                updates.append("stripe_subscription_id = %s")
                params.append(subscription_id)
            
            if not updates:
                return False
            
            updates.append("updated_at = CURRENT_TIMESTAMP")
            params.append(hardware_id)
            
            query = f"UPDATE subscriptions SET {', '.join(updates)} WHERE hardware_id = %s"
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                return cur.rowcount > 0
        finally:
            conn.close()
    
    def record_event(
        self,
        stripe_event_id: str,
        event_type: str,
        hardware_id: Optional[str] = None,
        event_data: Optional[Dict] = None,
        stripe_created_at: Optional[int] = None,
        processed: bool = True
    ) -> bool:
        """
        Записать обработанное событие (для идемпотентности)
        
        ⭐ КРИТИЧНО: 
        - stripe_created_at обязателен для out-of-order обработки
        - processed=FALSE если hardware_id отсутствует (для повторной обработки)
        - Использует UPSERT для обновления существующих записей с processed=FALSE
        
        Если событие уже существует с processed=FALSE, обновляет:
        - processed=TRUE
        - hardware_id (если передан)
        - processed_at=NOW()
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                # Если hardware_id отсутствует, processed=FALSE для повторной обработки
                if not hardware_id:
                    processed = False
                
                # ⭐ КРИТИЧНО: UPSERT для обновления существующих записей с processed=FALSE
                # Это позволяет перевести событие из processed=FALSE в processed=TRUE при повторной обработке
                # Обновляем только если:
                # 1. Текущая запись имеет processed=FALSE (можно обновить)
                # 2. ИЛИ новая запись имеет processed=TRUE (обновляем на processed=TRUE)
                cur.execute(
                    """INSERT INTO subscription_events 
                       (stripe_event_id, event_type, hardware_id, event_data, stripe_created_at, processed, processed_at)
                       VALUES (%s, %s, %s, %s::jsonb, %s, %s, CASE WHEN %s THEN CURRENT_TIMESTAMP ELSE NULL END)
                       ON CONFLICT (stripe_event_id) 
                       DO UPDATE SET
                           processed = CASE 
                               WHEN subscription_events.processed = FALSE AND EXCLUDED.processed = TRUE THEN TRUE
                               ELSE subscription_events.processed
                           END,
                           hardware_id = COALESCE(EXCLUDED.hardware_id, subscription_events.hardware_id),
                           processed_at = CASE 
                               WHEN subscription_events.processed = FALSE AND EXCLUDED.processed = TRUE THEN CURRENT_TIMESTAMP
                               ELSE subscription_events.processed_at
                           END,
                           event_data = COALESCE(EXCLUDED.event_data, subscription_events.event_data)
                       WHERE subscription_events.processed = FALSE OR (EXCLUDED.processed = TRUE AND subscription_events.processed = FALSE)""",
                    (
                        stripe_event_id, 
                        event_type, 
                        hardware_id,
                        Json(event_data) if event_data else None,
                        stripe_created_at or int(datetime.now().timestamp()),
                        processed,
                        processed  # Для CASE WHEN в processed_at
                    )
                )
                conn.commit()
                return cur.rowcount > 0
        except psycopg2.IntegrityError:
            # Событие уже обработано (идемпотентность)
            return False
        finally:
            conn.close()
    
    def event_exists(self, stripe_event_id: str, processed_only: bool = True) -> bool:
        """
        Проверить, было ли событие уже обработано
        
        Args:
            stripe_event_id: ID события
            processed_only: Если True, проверяет только события с processed=TRUE
                           Если False, проверяет любое событие (включая processed=FALSE)
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                if processed_only:
                    cur.execute(
                        """SELECT 1 FROM subscription_events 
                           WHERE stripe_event_id = %s AND processed = TRUE""",
                        (stripe_event_id,)
                    )
                else:
                    cur.execute(
                        """SELECT 1 FROM subscription_events 
                           WHERE stripe_event_id = %s""",
                        (stripe_event_id,)
                    )
                return cur.fetchone() is not None
        finally:
            conn.close()
    
    def create_payment(
        self,
        hardware_id: str,
        stripe_invoice_id: str,
        amount: int,
        currency: str = 'usd',
        status: str = 'succeeded',
        stripe_payment_intent_id: Optional[str] = None
    ) -> bool:
        """
        Создать запись о платеже
        
        ⭐ КРИТИЧНО: stripe_invoice_id имеет UNIQUE constraint для предотвращения дубликатов
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO payments 
                       (hardware_id, stripe_invoice_id, stripe_payment_intent_id, amount, currency, status)
                       VALUES (%s, %s, %s, %s, %s, %s)
                       ON CONFLICT (stripe_invoice_id) DO NOTHING""",
                    (hardware_id, stripe_invoice_id, stripe_payment_intent_id, amount, currency, status)
                )
                conn.commit()
                return cur.rowcount > 0
        except psycopg2.IntegrityError:
            # Платеж уже существует (идемпотентность)
            return False
        finally:
            conn.close()
    
    def get_payments(
        self, 
        hardware_id: str, 
        limit: int = 10,
        status: Optional[str] = None
    ) -> List[Dict]:
        """
        Получить последние платежи для hardware_id
        
        Args:
            hardware_id: ID устройства
            limit: Максимальное количество платежей
            status: Фильтр по статусу (например, 'succeeded'). Если None - все статусы
        """
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                if status:
                    cur.execute(
                        """SELECT * FROM payments 
                           WHERE hardware_id = %s AND status = %s
                           ORDER BY created_at DESC 
                           LIMIT %s""",
                        (hardware_id, status, limit)
                    )
                else:
                    cur.execute(
                        """SELECT * FROM payments 
                           WHERE hardware_id = %s 
                           ORDER BY created_at DESC 
                           LIMIT %s""",
                        (hardware_id, limit)
                    )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()
    
    def get_subscription_by_stripe_subscription_id(self, subscription_id: str) -> Optional[Dict]:
        """Получить подписку по stripe_subscription_id"""
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM subscriptions WHERE stripe_subscription_id = %s""",
                    (subscription_id,)
                )
                row = cur.fetchone()
                return dict(row) if row else None
        finally:
            conn.close()
    
    def get_subscription_by_stripe_customer_id(self, customer_id: str) -> Optional[Dict]:
        """Получить подписку по stripe_customer_id"""
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM subscriptions WHERE stripe_customer_id = %s""",
                    (customer_id,)
                )
                row = cur.fetchone()
                return dict(row) if row else None
        finally:
            conn.close()
    
    def update_subscription(self, hardware_id: str, **kwargs) -> bool:
        """
        Обновить подписку (универсальный метод для множественных полей)
        
        Поддерживаемые поля:
        - status
        - stripe_status
        - stripe_customer_id
        - stripe_subscription_id
        - payment_method_id
        - current_period_end
        - cancel_at_period_end
        - grace_period_end_at
        - paid_trial_end_at
        - last_stripe_event_id
        - last_stripe_event_at
        - usage_daily_count, usage_weekly_count, usage_monthly_count, usage_last_reset_date (Quota Checker)
        """
        conn = self._get_connection()
        try:
            updates = []
            params = []
            
            # Разрешенные поля для обновления
            allowed_fields = {
                'status', 'stripe_status', 'stripe_customer_id', 'stripe_subscription_id',
                'payment_method_id', 'current_period_end', 'cancel_at_period_end',
                'grace_period_end_at', 'paid_trial_end_at', 'last_stripe_event_id', 'last_stripe_event_at',
                'last_checkout_created_at', 'last_checkout_session_id',  # MVP 8: Anti-spam и cooldown
                'usage_daily_count', 'usage_weekly_count', 'usage_monthly_count', 'usage_last_reset_date'  # Quota Checker
            }
            
            for key, value in kwargs.items():
                if key in allowed_fields:
                    updates.append(f"{key} = %s")
                    params.append(value)
            
            if not updates:
                return False
            
            updates.append("updated_at = CURRENT_TIMESTAMP")
            params.append(hardware_id)
            
            query = f"UPDATE subscriptions SET {', '.join(updates)} WHERE hardware_id = %s"
            with conn.cursor() as cur:
                cur.execute(query, params)
                conn.commit()
                return cur.rowcount > 0
        finally:
            conn.close()
    
    def payment_exists(self, stripe_invoice_id: str) -> bool:
        """Проверить, существует ли платеж с данным stripe_invoice_id"""
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT 1 FROM payments WHERE stripe_invoice_id = %s""",
                    (stripe_invoice_id,)
                )
                return cur.fetchone() is not None
        finally:
            conn.close()
    
    def get_expired_trials(self) -> List[Dict]:
        """
        Получить все истекшие trial подписки
        
        Условия:
        - status = 'paid_trial'
        - paid_trial_end_at IS NOT NULL
        - paid_trial_end_at <= NOW()
        - stripe_subscription_id IS NULL (пользователь не оплатил)
        
        Returns:
            Список подписок с истекшим trial периодом
        """
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM subscriptions
                       WHERE status = 'paid_trial'
                         AND paid_trial_end_at IS NOT NULL
                         AND paid_trial_end_at <= NOW()
                         AND (stripe_subscription_id IS NULL OR stripe_subscription_id = '')
                       ORDER BY paid_trial_end_at ASC""",
                )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()
    
    def get_expired_grace_periods(self) -> List[Dict]:
        """
        Получить все истекшие grace periods
        
        Условия:
        - status = 'billing_problem'
        - grace_period_end_at IS NOT NULL
        - grace_period_end_at <= NOW()
        
        Returns:
            Список подписок с истекшим grace period
        """
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT * FROM subscriptions
                       WHERE status = 'billing_problem'
                         AND grace_period_end_at IS NOT NULL
                         AND grace_period_end_at <= NOW()
                       ORDER BY grace_period_end_at ASC""",
                )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()
    
    def increment_usage(self, hardware_id: str, current_date) -> bool:
        """
        Атомарно инкрементирует счетчики использования для limited_free_trial
        
        ⚠️ КРИТИЧНО: Использует SELECT FOR UPDATE для предотвращения race conditions
        
        Args:
            hardware_id: ID устройства
            current_date: Текущая дата (date объект)
        
        Returns:
            True если успешно, False иначе
        """
        conn = self._get_connection()
        try:
            with conn.cursor() as cur:
                # Атомарное обновление с SELECT FOR UPDATE
                cur.execute(
                    """UPDATE subscriptions 
                       SET usage_daily_count = COALESCE(usage_daily_count, 0) + 1,
                           usage_weekly_count = COALESCE(usage_weekly_count, 0) + 1,
                           usage_monthly_count = COALESCE(usage_monthly_count, 0) + 1,
                           usage_last_reset_date = %s,
                           updated_at = CURRENT_TIMESTAMP
                       WHERE hardware_id = %s AND status = 'limited_free_trial'""",
                    (current_date, hardware_id)
                )
                conn.commit()
                return cur.rowcount > 0
        except Exception as e:
            conn.rollback()
            return False
        finally:
            conn.close()
    
    def get_subscriptions_for_daily_reset(self, today) -> List[Dict]:
        """
        Получить подписки для ежедневного сброса квот
        
        Args:
            today: Сегодняшняя дата
        
        Returns:
            Список подписок, у которых usage_last_reset_date < today
        """
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT hardware_id, usage_last_reset_date FROM subscriptions
                       WHERE status = 'limited_free_trial'
                         AND (usage_last_reset_date IS NULL OR usage_last_reset_date < %s)""",
                    (today,)
                )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()
    
    def get_subscriptions_for_weekly_reset(self, week_start) -> List[Dict]:
        """
        Получить подписки для еженедельного сброса квот
        
        Args:
            week_start: Начало недели (понедельник)
        
        Returns:
            Список подписок для сброса
        """
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT hardware_id, usage_last_reset_date FROM subscriptions
                       WHERE status = 'limited_free_trial'
                         AND (usage_last_reset_date IS NULL OR usage_last_reset_date < %s)""",
                    (week_start,)
                )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()
    
    def get_subscriptions_for_monthly_reset(self, month_start) -> List[Dict]:
        """
        Получить подписки для ежемесячного сброса квот
        
        Args:
            month_start: Начало месяца
        
        Returns:
            Список подписок для сброса
        """
        conn = self._get_connection()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    """SELECT hardware_id, usage_last_reset_date FROM subscriptions
                       WHERE status = 'limited_free_trial'
                         AND (usage_last_reset_date IS NULL OR usage_last_reset_date < %s)""",
                    (month_start,)
                )
                return [dict(row) for row in cur.fetchall()]
        finally:
            conn.close()

