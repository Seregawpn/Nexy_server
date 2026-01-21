#!/usr/bin/env python3
"""
Запуск мониторинга платежной системы

Использование:
    python run_monitoring.py [metrics|alerts|health|log]

Feature ID: F-2025-017-stripe-payment
"""
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

from payment_monitoring import PaymentMonitoring
from logging_config import init_payment_logging
import logging

# Настраиваем логирование
init_payment_logging()
logger = logging.getLogger(__name__)


def main():
    """Главная функция"""
    monitoring = PaymentMonitoring()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'metrics':
            # Вывести метрики в JSON
            metrics = monitoring.get_metrics(force_refresh=True)
            import json
            print(json.dumps(metrics, indent=2, default=str))
        
        elif command == 'alerts':
            # Проверить алерты
            alerts = monitoring.check_alerts()
            import json
            print(json.dumps(alerts, indent=2, default=str))
            
            # Вывести критичные алерты
            critical = [a for a in alerts if a['level'] == 'error']
            if critical:
                print("\n❌ CRITICAL ALERTS:")
                for alert in critical:
                    print(f"  - {alert['message']}")
                sys.exit(1)
        
        elif command == 'health':
            # Получить статус здоровья
            health = monitoring.get_health_status()
            import json
            print(json.dumps(health, indent=2, default=str))
            
            # Вывести статус
            status = health.get('status', 'unknown')
            if status == 'healthy':
                print("\n✅ System is healthy")
                sys.exit(0)
            elif status == 'degraded':
                print("\n⚠️  System is degraded")
                sys.exit(1)
            else:
                print("\n❌ System is unhealthy")
                sys.exit(2)
        
        elif command == 'log':
            # Логировать метрики
            monitoring.log_metrics()
            alerts = monitoring.check_alerts()
            if alerts:
                print("\n⚠️  ALERTS:")
                for alert in alerts:
                    level_icon = {
                        'error': '❌',
                        'warning': '⚠️',
                        'info': 'ℹ️'
                    }.get(alert['level'], '•')
                    print(f"  {level_icon} [{alert['level'].upper()}] {alert['message']}")
        
        else:
            print(f"Unknown command: {command}")
            print("Usage: python run_monitoring.py [metrics|alerts|health|log]")
            sys.exit(1)
    else:
        # По умолчанию - логировать метрики и проверить алерты
        monitoring.log_metrics()
        alerts = monitoring.check_alerts()
        if alerts:
            print("\n⚠️  ALERTS:")
            for alert in alerts:
                level_icon = {
                    'error': '❌',
                    'warning': '⚠️',
                    'info': 'ℹ️'
                }.get(alert['level'], '•')
                print(f"  {level_icon} [{alert['level'].upper()}] {alert['message']}")


if __name__ == '__main__':
    main()

