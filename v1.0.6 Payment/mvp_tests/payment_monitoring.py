#!/usr/bin/env python3
"""
Payment Monitoring - мониторинг платежной системы

Feature ID: F-2025-017-stripe-payment
Отслеживание метрик, алертов и состояния системы
"""
import logging
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from collections import defaultdict
from subscription_repository import SubscriptionRepository
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class PaymentMonitoring:
    """
    Мониторинг платежной системы
    
    Отслеживает:
    - Метрики (количество подписок, платежей, использование квот)
    - Алерты (ошибки, проблемы синхронизации)
    - Состояние системы
    """
    
    def __init__(self, repository: Optional[SubscriptionRepository] = None):
        """Инициализация мониторинга"""
        self.repository = repository or SubscriptionRepository()
        self._metrics_cache: Dict[str, any] = {}
        self._metrics_cache_time: Optional[datetime] = None
        self._metrics_cache_ttl = timedelta(minutes=5)  # Кэш метрик на 5 минут
    
    def get_metrics(self, force_refresh: bool = False) -> Dict:
        """
        Получить метрики системы
        
        Args:
            force_refresh: Принудительно обновить кэш
        
        Returns:
            Dict с метриками
        """
        # Проверяем кэш
        if not force_refresh and self._metrics_cache_time:
            if datetime.now() - self._metrics_cache_time < self._metrics_cache_ttl:
                return self._metrics_cache
        
        try:
            metrics = {
                'timestamp': datetime.now().isoformat(),
                'subscriptions': self._get_subscription_metrics(),
                'payments': self._get_payment_metrics(),
                'quota_usage': self._get_quota_metrics(),
                'webhooks': self._get_webhook_metrics(),
                'sync_status': self._get_sync_metrics()
            }
            
            # Обновляем кэш
            self._metrics_cache = metrics
            self._metrics_cache_time = datetime.now()
            
            return metrics
            
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting metrics: {e}")
            return {
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            }
    
    def _get_subscription_metrics(self) -> Dict:
        """Получить метрики подписок"""
        try:
            conn = self.repository._get_connection()
            try:
                from psycopg2.extras import RealDictCursor
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    # Общее количество подписок
                    cur.execute("SELECT COUNT(*) as total FROM subscriptions")
                    total = cur.fetchone()['total']
                    
                    # Количество по статусам
                    cur.execute("""
                        SELECT status, COUNT(*) as count 
                        FROM subscriptions 
                        GROUP BY status
                    """)
                    by_status = {row['status']: row['count'] for row in cur.fetchall()}
                    
                    # Активные подписки (paid, paid_trial)
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE status IN ('paid', 'paid_trial')
                    """)
                    active = cur.fetchone()['count']
                    
                    # Подписки с проблемами (billing_problem)
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE status = 'billing_problem'
                    """)
                    billing_problems = cur.fetchone()['count']
                    
                    # Подписки с истекшим trial
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE status = 'paid_trial' 
                          AND paid_trial_end_at IS NOT NULL 
                          AND paid_trial_end_at <= NOW()
                    """)
                    expired_trials = cur.fetchone()['count']
                    
                    # Подписки с истекшим grace period
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE status = 'billing_problem' 
                          AND grace_period_end_at IS NOT NULL 
                          AND grace_period_end_at <= NOW()
                    """)
                    expired_grace_periods = cur.fetchone()['count']
                    
                    return {
                        'total': total,
                        'active': active,
                        'by_status': by_status,
                        'billing_problems': billing_problems,
                        'expired_trials': expired_trials,
                        'expired_grace_periods': expired_grace_periods
                    }
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting subscription metrics: {e}")
            return {'error': str(e)}
    
    def _get_payment_metrics(self) -> Dict:
        """Получить метрики платежей"""
        try:
            conn = self.repository._get_connection()
            try:
                from psycopg2.extras import RealDictCursor
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    # Общее количество платежей
                    cur.execute("SELECT COUNT(*) as total FROM payments")
                    total = cur.fetchone()['total']
                    
                    # Количество по статусам
                    cur.execute("""
                        SELECT status, COUNT(*) as count 
                        FROM payments 
                        GROUP BY status
                    """)
                    by_status = {row['status']: row['count'] for row in cur.fetchall()}
                    
                    # Успешные платежи
                    cur.execute("""
                        SELECT COUNT(*) as count, SUM(amount) as total_amount 
                        FROM payments 
                        WHERE status = 'succeeded'
                    """)
                    succeeded_row = cur.fetchone()
                    succeeded = succeeded_row['count'] or 0
                    total_amount = succeeded_row['total_amount'] or 0
                    
                    # Неудачные платежи
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM payments 
                        WHERE status = 'failed'
                    """)
                    failed = cur.fetchone()['count'] or 0
                    
                    # Платежи за последние 24 часа
                    cur.execute("""
                        SELECT COUNT(*) as count, SUM(amount) as total_amount 
                        FROM payments 
                        WHERE created_at >= NOW() - INTERVAL '24 hours'
                    """)
                    last_24h_row = cur.fetchone()
                    last_24h_count = last_24h_row['count'] or 0
                    last_24h_amount = last_24h_row['total_amount'] or 0
                    
                    return {
                        'total': total,
                        'by_status': by_status,
                        'succeeded': succeeded,
                        'failed': failed,
                        'total_amount_cents': total_amount,
                        'total_amount_usd': total_amount / 100 if total_amount else 0,
                        'last_24h': {
                            'count': last_24h_count,
                            'amount_cents': last_24h_amount,
                            'amount_usd': last_24h_amount / 100 if last_24h_amount else 0
                        }
                    }
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting payment metrics: {e}")
            return {'error': str(e)}
    
    def _get_quota_metrics(self) -> Dict:
        """Получить метрики использования квот"""
        try:
            conn = self.repository._get_connection()
            try:
                from psycopg2.extras import RealDictCursor
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    # Подписки с limited_free_trial
                    cur.execute("""
                        SELECT COUNT(*) as total,
                               SUM(usage_daily_count) as total_daily,
                               SUM(usage_weekly_count) as total_weekly,
                               SUM(usage_monthly_count) as total_monthly,
                               AVG(usage_daily_count) as avg_daily,
                               AVG(usage_weekly_count) as avg_weekly,
                               AVG(usage_monthly_count) as avg_monthly
                        FROM subscriptions 
                        WHERE status = 'limited_free_trial'
                    """)
                    row = cur.fetchone()
                    
                    # Подписки, достигшие лимитов
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE status = 'limited_free_trial'
                          AND (usage_daily_count >= 5 
                               OR usage_weekly_count >= 25 
                               OR usage_monthly_count >= 50)
                    """)
                    at_limit = cur.fetchone()['count'] or 0
                    
                    return {
                        'total_limited_trial': row['total'] or 0,
                        'total_usage': {
                            'daily': row['total_daily'] or 0,
                            'weekly': row['total_weekly'] or 0,
                            'monthly': row['total_monthly'] or 0
                        },
                        'average_usage': {
                            'daily': float(row['avg_daily'] or 0),
                            'weekly': float(row['avg_weekly'] or 0),
                            'monthly': float(row['avg_monthly'] or 0)
                        },
                        'at_limit': at_limit
                    }
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting quota metrics: {e}")
            return {'error': str(e)}
    
    def _get_webhook_metrics(self) -> Dict:
        """Получить метрики webhooks"""
        try:
            conn = self.repository._get_connection()
            try:
                from psycopg2.extras import RealDictCursor
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    # Общее количество событий
                    cur.execute("SELECT COUNT(*) as total FROM subscription_events")
                    total = cur.fetchone()['total']
                    
                    # Количество по типам событий
                    cur.execute("""
                        SELECT event_type, COUNT(*) as count 
                        FROM subscription_events 
                        GROUP BY event_type
                        ORDER BY count DESC
                        LIMIT 10
                    """)
                    by_type = {row['event_type']: row['count'] for row in cur.fetchall()}
                    
                    # Обработанные события
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscription_events 
                        WHERE processed = TRUE
                    """)
                    processed = cur.fetchone()['count']
                    
                    # Необработанные события
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscription_events 
                        WHERE processed = FALSE
                    """)
                    unprocessed = cur.fetchone()['count']
                    
                    # События за последние 24 часа
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscription_events 
                        WHERE created_at >= NOW() - INTERVAL '24 hours'
                    """)
                    last_24h = cur.fetchone()['count']
                    
                    return {
                        'total': total,
                        'by_type': by_type,
                        'processed': processed,
                        'unprocessed': unprocessed,
                        'last_24h': last_24h
                    }
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting webhook metrics: {e}")
            return {'error': str(e)}
    
    def _get_sync_metrics(self) -> Dict:
        """Получить метрики синхронизации"""
        try:
            conn = self.repository._get_connection()
            try:
                from psycopg2.extras import RealDictCursor
                with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    # Подписки с stripe_subscription_id
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE stripe_subscription_id IS NOT NULL 
                          AND stripe_subscription_id != ''
                    """)
                    with_stripe_id = cur.fetchone()['count']
                    
                    # Подписки без stripe_subscription_id, но со статусом paid
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE status = 'paid' 
                          AND (stripe_subscription_id IS NULL 
                               OR stripe_subscription_id = '')
                    """)
                    paid_without_stripe = cur.fetchone()['count']
                    
                    # Подписки с несоответствием статусов
                    cur.execute("""
                        SELECT COUNT(*) as count 
                        FROM subscriptions 
                        WHERE stripe_subscription_id IS NOT NULL 
                          AND stripe_subscription_id != ''
                          AND stripe_status IS NOT NULL
                          AND status != stripe_status
                    """)
                    status_mismatch = cur.fetchone()['count']
                    
                    return {
                        'with_stripe_id': with_stripe_id,
                        'paid_without_stripe': paid_without_stripe,
                        'status_mismatch': status_mismatch
                    }
            finally:
                conn.close()
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting sync metrics: {e}")
            return {'error': str(e)}
    
    def check_alerts(self) -> List[Dict]:
        """
        Проверить алерты
        
        Returns:
            List[Dict] со списком алертов
        """
        alerts = []
        
        try:
            metrics = self.get_metrics(force_refresh=True)
            
            # Алерт: Необработанные webhook события
            webhooks = metrics.get('webhooks', {})
            unprocessed = webhooks.get('unprocessed', 0)
            if unprocessed > 0:
                alerts.append({
                    'level': 'warning',
                    'type': 'unprocessed_webhooks',
                    'message': f'Found {unprocessed} unprocessed webhook events',
                    'count': unprocessed
                })
            
            # Алерт: Подписки с проблемами оплаты
            subscriptions = metrics.get('subscriptions', {})
            billing_problems = subscriptions.get('billing_problems', 0)
            if billing_problems > 0:
                alerts.append({
                    'level': 'warning',
                    'type': 'billing_problems',
                    'message': f'Found {billing_problems} subscriptions with billing problems',
                    'count': billing_problems
                })
            
            # Алерт: Истекшие trial периоды
            expired_trials = subscriptions.get('expired_trials', 0)
            if expired_trials > 0:
                alerts.append({
                    'level': 'info',
                    'type': 'expired_trials',
                    'message': f'Found {expired_trials} expired trial subscriptions (will be handled by Trial Handler)',
                    'count': expired_trials
                })
            
            # Алерт: Истекшие grace periods
            expired_grace = subscriptions.get('expired_grace_periods', 0)
            if expired_grace > 0:
                alerts.append({
                    'level': 'warning',
                    'type': 'expired_grace_periods',
                    'message': f'Found {expired_grace} expired grace periods (will be handled by Grace Period Handler)',
                    'count': expired_grace
                })
            
            # Алерт: Несоответствие статусов
            sync = metrics.get('sync_status', {})
            status_mismatch = sync.get('status_mismatch', 0)
            if status_mismatch > 0:
                alerts.append({
                    'level': 'warning',
                    'type': 'status_mismatch',
                    'message': f'Found {status_mismatch} subscriptions with status mismatch (need sync)',
                    'count': status_mismatch
                })
            
            # Алерт: Подписки paid без stripe_subscription_id
            paid_without_stripe = sync.get('paid_without_stripe', 0)
            if paid_without_stripe > 0:
                alerts.append({
                    'level': 'error',
                    'type': 'paid_without_stripe',
                    'message': f'Found {paid_without_stripe} paid subscriptions without stripe_subscription_id',
                    'count': paid_without_stripe
                })
            
            # Алерт: Подписки, достигшие лимитов квот
            quota = metrics.get('quota_usage', {})
            at_limit = quota.get('at_limit', 0)
            if at_limit > 0:
                alerts.append({
                    'level': 'info',
                    'type': 'quota_limit_reached',
                    'message': f'Found {at_limit} subscriptions at quota limit',
                    'count': at_limit
                })
            
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error checking alerts: {e}")
            alerts.append({
                'level': 'error',
                'type': 'monitoring_error',
                'message': f'Error checking alerts: {str(e)}'
            })
        
        return alerts
    
    def get_health_status(self) -> Dict:
        """
        Получить статус здоровья системы
        
        Returns:
            Dict со статусом здоровья
        """
        try:
            alerts = self.check_alerts()
            
            # Определяем общий статус
            has_errors = any(alert['level'] == 'error' for alert in alerts)
            has_warnings = any(alert['level'] == 'warning' for alert in alerts)
            
            if has_errors:
                status = 'unhealthy'
            elif has_warnings:
                status = 'degraded'
            else:
                status = 'healthy'
            
            return {
                'status': status,
                'timestamp': datetime.now().isoformat(),
                'alerts_count': len(alerts),
                'errors_count': sum(1 for a in alerts if a['level'] == 'error'),
                'warnings_count': sum(1 for a in alerts if a['level'] == 'warning'),
                'alerts': alerts
            }
            
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error getting health status: {e}")
            return {
                'status': 'error',
                'timestamp': datetime.now().isoformat(),
                'error': str(e)
            }
    
    def log_metrics(self):
        """Логировать метрики"""
        try:
            metrics = self.get_metrics(force_refresh=True)
            
            logger.info("=" * 60)
            logger.info("PAYMENT SYSTEM METRICS")
            logger.info("=" * 60)
            
            # Подписки
            subs = metrics.get('subscriptions', {})
            logger.info(f"Subscriptions: total={subs.get('total', 0)}, active={subs.get('active', 0)}")
            logger.info(f"  By status: {subs.get('by_status', {})}")
            logger.info(f"  Billing problems: {subs.get('billing_problems', 0)}")
            logger.info(f"  Expired trials: {subs.get('expired_trials', 0)}")
            
            # Платежи
            payments = metrics.get('payments', {})
            logger.info(f"Payments: total={payments.get('total', 0)}, succeeded={payments.get('succeeded', 0)}")
            logger.info(f"  Total amount: ${payments.get('total_amount_usd', 0):.2f}")
            logger.info(f"  Last 24h: {payments.get('last_24h', {}).get('count', 0)} payments, ${payments.get('last_24h', {}).get('amount_usd', 0):.2f}")
            
            # Квоты
            quota = metrics.get('quota_usage', {})
            logger.info(f"Quota usage: {quota.get('total_limited_trial', 0)} limited_free_trial subscriptions")
            logger.info(f"  At limit: {quota.get('at_limit', 0)}")
            
            # Webhooks
            webhooks = metrics.get('webhooks', {})
            logger.info(f"Webhooks: total={webhooks.get('total', 0)}, processed={webhooks.get('processed', 0)}")
            logger.info(f"  Unprocessed: {webhooks.get('unprocessed', 0)}")
            
            # Синхронизация
            sync = metrics.get('sync_status', {})
            logger.info(f"Sync: with_stripe_id={sync.get('with_stripe_id', 0)}")
            logger.info(f"  Status mismatch: {sync.get('status_mismatch', 0)}")
            
            logger.info("=" * 60)
            
        except Exception as e:
            logger.error(f"[PaymentMonitoring] Error logging metrics: {e}")


def main():
    """Главная функция для запуска мониторинга"""
    import sys
    
    monitoring = PaymentMonitoring()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'metrics':
            # Вывести метрики
            metrics = monitoring.get_metrics(force_refresh=True)
            import json
            print(json.dumps(metrics, indent=2, default=str))
        
        elif command == 'alerts':
            # Проверить алерты
            alerts = monitoring.check_alerts()
            import json
            print(json.dumps(alerts, indent=2, default=str))
        
        elif command == 'health':
            # Получить статус здоровья
            health = monitoring.get_health_status()
            import json
            print(json.dumps(health, indent=2, default=str))
        
        elif command == 'log':
            # Логировать метрики
            monitoring.log_metrics()
        
        else:
            print(f"Unknown command: {command}")
            print("Usage: python payment_monitoring.py [metrics|alerts|health|log]")
            sys.exit(1)
    else:
        # По умолчанию - логировать метрики
        monitoring.log_metrics()
        alerts = monitoring.check_alerts()
        if alerts:
            print("\n⚠️  ALERTS:")
            for alert in alerts:
                print(f"  [{alert['level'].upper()}] {alert['message']}")


if __name__ == '__main__':
    main()

