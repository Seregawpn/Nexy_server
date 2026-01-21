#!/usr/bin/env python3
"""
Скрипт для исправления алертов мониторинга

Использование:
    python fix_alerts.py [action]

    action может быть:
    - sync - запустить синхронизацию со Stripe
    - grace - запустить Grace Period Handler
    - analyze - проанализировать проблемы
    - all - выполнить все действия
"""
import sys
import os
from datetime import datetime

# Добавляем пути для импорта
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'server(Payment)', 'server', 'modules', 'subscription', 'core')))

from subscription_repository import SubscriptionRepository
from payment_monitoring import PaymentMonitoring


def analyze_alerts():
    """Анализ текущих алертов"""
    print('╔══════════════════════════════════════════════════════════════╗')
    print('║     📊 АНАЛИЗ АЛЕРТОВ                                       ║')
    print('╚══════════════════════════════════════════════════════════════╝')
    print()
    
    monitoring = PaymentMonitoring()
    health = monitoring.get_health_status()
    
    print('🚨 АЛЕРТЫ:')
    for alert in health.get('alerts', []):
        level_icon = {'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}.get(alert['level'], '•')
        print(f'  {level_icon} [{alert["level"].upper()}] {alert["type"]}: {alert["message"]}')
    print()
    
    # Детальный анализ проблемных подписок
    repo = SubscriptionRepository()
    
    # Получаем все подписки через SQL запрос
    conn = repo._get_connection()
    try:
        from psycopg2.extras import RealDictCursor
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM subscriptions")
            all_subs = [dict(row) for row in cur.fetchall()]
    finally:
        conn.close()
    
    # 1. Paid без stripe_subscription_id
    paid_without_stripe = [s for s in all_subs if s['status'] == 'paid' and not s.get('stripe_subscription_id')]
    
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('1. ❌ PAID БЕЗ STRIPE_SUBSCRIPTION_ID:')
    print(f'   Найдено: {len(paid_without_stripe)} подписок')
    if paid_without_stripe:
        print('   Примеры:')
        for sub in paid_without_stripe[:5]:
            print(f'     • {sub["hardware_id"][:30]}... - created_at: {sub.get("created_at")}')
        print('   ⚠️  Требует ручной проверки!')
    print()
    
    # 2. Status mismatch
    status_mismatch = [s for s in all_subs if s.get('stripe_subscription_id') and s.get('stripe_status') and s['status'] != 'paid' and s['stripe_status'] in ['active', 'trialing']]
    
    print('2. ⚠️  STATUS MISMATCH:')
    print(f'   Найдено: {len(status_mismatch)} подписок')
    if status_mismatch:
        print('   Примеры:')
        for sub in status_mismatch[:3]:
            print(f'     • {sub["hardware_id"][:30]}... - БД: {sub["status"]}, Stripe: {sub.get("stripe_status")}')
        print('   ✅ Можно исправить через синхронизацию')
    print()
    
    # 3. Billing problems
    billing_problems = [s for s in all_subs if s['status'] == 'billing_problem']
    expired_grace = [s for s in billing_problems if s.get('grace_period_end_at') and isinstance(s['grace_period_end_at'], datetime) and s['grace_period_end_at'] < datetime.now()]
    
    print('3. ⚠️  BILLING PROBLEMS:')
    print(f'   Найдено: {len(billing_problems)} подписок')
    print(f'   С истекшим grace_period: {len(expired_grace)}')
    if expired_grace:
        print('   ⚠️  Эти подписки должны быть переведены в limited_free_trial')
    print()
    
    return {
        'paid_without_stripe': len(paid_without_stripe),
        'status_mismatch': len(status_mismatch),
        'billing_problems': len(billing_problems),
        'expired_grace': len(expired_grace)
    }


def run_sync():
    """Запустить синхронизацию со Stripe"""
    print('╔══════════════════════════════════════════════════════════════╗')
    print('║     🔄 ЗАПУСК СИНХРОНИЗАЦИИ СО STRIPE                        ║')
    print('╚══════════════════════════════════════════════════════════════╝')
    print()
    
    try:
        from run_periodic_tasks import run_stripe_sync
        result = run_stripe_sync()
        
        if result.get('success'):
            print('✅ Синхронизация завершена успешно!')
            print(f"   Обработано подписок: {result.get('processed', 'N/A')}")
        else:
            print('❌ Ошибка синхронизации:', result.get('error'))
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()


def run_grace_period_handler():
    """Запустить Grace Period Handler"""
    print('╔══════════════════════════════════════════════════════════════╗')
    print('║     ⏰ ЗАПУСК GRACE PERIOD HANDLER                           ║')
    print('╚══════════════════════════════════════════════════════════════╝')
    print()
    
    try:
        from run_periodic_tasks import run_grace_period_handler
        result = run_grace_period_handler()
        
        if result.get('success'):
            print('✅ Grace Period Handler завершен успешно!')
            print(f"   Обработано подписок: {result.get('processed', 'N/A')}")
        else:
            print('❌ Ошибка:', result.get('error'))
    except Exception as e:
        print(f'❌ Ошибка: {e}')
        import traceback
        traceback.print_exc()


def main():
    """Главная функция"""
    action = sys.argv[1] if len(sys.argv) > 1 else 'analyze'
    
    if action == 'analyze':
        analyze_alerts()
    elif action == 'sync':
        run_sync()
    elif action == 'grace':
        run_grace_period_handler()
    elif action == 'all':
        print('🚀 Запуск всех действий...\n')
        analyze_alerts()
        print()
        run_sync()
        print()
        run_grace_period_handler()
        print()
        print('✅ Все действия завершены!')
        print('Проверьте результаты: python run_monitoring.py log')
    else:
        print(f'Неизвестное действие: {action}')
        print('Доступные действия: analyze, sync, grace, all')


if __name__ == '__main__':
    main()

