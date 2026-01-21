#!/usr/bin/env python3
"""
Универсальный скрипт для запуска всех периодических задач

Использование:
    python run_periodic_tasks.py [task_name]
    
    task_name может быть:
    - trial_handler - запуск Trial Handler
    - grace_period_handler - запуск Grace Period Handler
    - sync_service - запуск Sync Service
    - quota_reset - запуск Quota Reset (daily/weekly/monthly)
    - monitoring - запуск Monitoring
    - all - запуск всех задач (по умолчанию)

Или через cron:
    0 */6 * * * cd /path/to/mvp_tests && source venv/bin/activate && python run_periodic_tasks.py trial_handler
    0 */6 * * * cd /path/to/mvp_tests && source venv/bin/activate && python run_periodic_tasks.py grace_period_handler
    0 * * * * cd /path/to/mvp_tests && source venv/bin/activate && python run_periodic_tasks.py sync_service

Feature ID: F-2025-017-stripe-payment
"""
import sys
import os
import logging
from datetime import datetime
from typing import Dict, Optional

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Добавляем путь к mvp_tests для импорта
sys.path.insert(0, os.path.dirname(__file__))

def run_trial_handler() -> Dict:
    """Запуск Trial Expiration Handler"""
    logger.info("Starting Trial Expiration Handler...")
    
    try:
        from trial_handler import TrialExpirationHandler
        from subscription_repository import SubscriptionRepository
        
        repository = SubscriptionRepository()
        handler = TrialExpirationHandler(repository=repository)
        
        stats = handler.check_expired_trials()
        
        logger.info(
            f"Trial Handler completed: "
            f"processed={stats['processed']}, "
            f"transitions={stats['transitions']}, "
            f"notifications={stats['notifications']}, "
            f"checkouts={stats['checkouts_created']}"
        )
        
        if stats['errors']:
            logger.error(f"Trial Handler errors: {len(stats['errors'])}")
            for error in stats['errors']:
                logger.error(f"  - {error}")
        
        return {
            'success': len(stats['errors']) == 0,
            'task': 'trial_handler',
            'stats': stats
        }
    
    except Exception as e:
        logger.error(f"Trial Handler error: {e}", exc_info=True)
        return {
            'success': False,
            'task': 'trial_handler',
            'error': str(e)
        }


def run_grace_period_handler() -> Dict:
    """Запуск Grace Period Handler"""
    logger.info("Starting Grace Period Handler...")
    
    try:
        from grace_period_handler import GracePeriodHandler
        from subscription_repository import SubscriptionRepository
        
        repository = SubscriptionRepository()
        handler = GracePeriodHandler(repository=repository)
        
        stats = handler.check_expired_grace_periods()
        
        logger.info(
            f"Grace Period Handler completed: "
            f"processed={stats['processed']}, "
            f"transitions={stats['transitions']}, "
            f"notifications={stats['notifications']}"
        )
        
        if stats['errors']:
            logger.error(f"Grace Period Handler errors: {len(stats['errors'])}")
            for error in stats['errors']:
                logger.error(f"  - {error}")
        
        return {
            'success': len(stats['errors']) == 0,
            'task': 'grace_period_handler',
            'stats': stats
        }
    
    except Exception as e:
        logger.error(f"Grace Period Handler error: {e}", exc_info=True)
        return {
            'success': False,
            'task': 'grace_period_handler',
            'error': str(e)
        }


def run_sync_service() -> Dict:
    """Запуск Sync Service"""
    logger.info("Starting Stripe Sync Service...")
    
    try:
        from stripe_sync_service import StripeSyncService
        
        sync_service = StripeSyncService()
        
        stats = sync_service.sync_all_subscriptions(batch_size=20, delay_ms=40)
        
        logger.info(
            f"Sync Service completed: "
            f"total={stats['total']}, "
            f"success={stats['success']}, "
            f"skipped={stats['skipped']}, "
            f"errors={stats['errors']}, "
            f"mismatches={stats['mismatches_found']}, "
            f"transitions={stats['transitions']}"
        )
        
        if stats['errors'] > 0:
            logger.warning(f"Sync Service errors: {stats['errors']}")
            # Логируем ошибки из results
            for result in stats.get('results', []):
                if not result.get('success'):
                    logger.warning(f"  - {result.get('hardware_id')}: {result.get('result')}")
        
        return {
            'success': stats['errors'] == 0,
            'task': 'sync_service',
            'stats': stats
        }
    
    except Exception as e:
        logger.error(f"Sync Service error: {e}", exc_info=True)
        return {
            'success': False,
            'task': 'sync_service',
            'error': str(e)
        }


def run_quota_reset() -> Dict:
    """Запуск Quota Reset"""
    logger.info("Starting Quota Reset...")
    
    try:
        from run_quota_reset import reset_daily, reset_weekly, reset_monthly
        from datetime import date, timedelta
        
        today = date.today()
        results = {}
        
        # Ежедневный сброс (всегда)
        logger.info("Running daily reset...")
        reset_daily()
        results['daily'] = {'success': True}
        
        # Еженедельный сброс (понедельник)
        if today.weekday() == 0:  # Понедельник
            logger.info("Running weekly reset (Monday)...")
            reset_weekly()
            results['weekly'] = {'success': True}
        else:
            results['weekly'] = {'skipped': True, 'reason': 'not_monday'}
        
        # Ежемесячный сброс (1-е число)
        if today.day == 1:
            logger.info("Running monthly reset (1st of month)...")
            reset_monthly()
            results['monthly'] = {'success': True}
        else:
            results['monthly'] = {'skipped': True, 'reason': 'not_first_day'}
        
        return {'success': True, 'results': results}
    except Exception as e:
        logger.error(f"Error running quota reset: {e}", exc_info=True)
        return {'success': False, 'error': str(e)}


def run_monitoring() -> Dict:
    """Запуск Monitoring"""
    logger.info("Starting Payment Monitoring...")
    
    try:
        from payment_monitoring import PaymentMonitoring
        
        monitoring = PaymentMonitoring()
        
        # Логируем метрики
        monitoring.log_metrics()
        
        # Проверяем алерты
        alerts = monitoring.check_alerts()
        
        # Получаем статус здоровья
        health = monitoring.get_health_status()
        
        return {
            'success': health.get('status') != 'error',
            'task': 'monitoring',
            'health_status': health.get('status'),
            'alerts_count': len(alerts),
            'errors_count': health.get('errors_count', 0),
            'warnings_count': health.get('warnings_count', 0)
        }
    except Exception as e:
        logger.error(f"Monitoring error: {e}", exc_info=True)
        return {
            'success': False,
            'task': 'monitoring',
            'error': str(e)
        }


def main():
    """Главная функция"""
    task_name = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    logger.info(f"Starting periodic tasks (task: {task_name})")
    
    results = []
    
    if task_name == 'trial_handler' or task_name == 'all':
        result = run_trial_handler()
        results.append(result)
    
    if task_name == 'grace_period_handler' or task_name == 'all':
        result = run_grace_period_handler()
        results.append(result)
    
    if task_name == 'sync_service' or task_name == 'all':
        result = run_sync_service()
        results.append(result)
    
    if task_name == 'quota_reset' or task_name == 'all':
        result = run_quota_reset()
        results.append(result)
    
    if task_name == 'monitoring' or task_name == 'all':
        result = run_monitoring()
        results.append(result)
    
    if task_name not in ['trial_handler', 'grace_period_handler', 'sync_service', 'quota_reset', 'monitoring', 'all']:
        logger.error(f"Unknown task: {task_name}")
        logger.info("Available tasks: trial_handler, grace_period_handler, sync_service, quota_reset, monitoring, all")
        return 1
    
    # Итоговая статистика
    total_tasks = len(results)
    successful_tasks = sum(1 for r in results if r['success'])
    failed_tasks = total_tasks - successful_tasks
    
    logger.info(
        f"All tasks completed: "
        f"total={total_tasks}, "
        f"success={successful_tasks}, "
        f"failed={failed_tasks}"
    )
    
    # Возвращаем код выхода
    return 0 if failed_tasks == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
