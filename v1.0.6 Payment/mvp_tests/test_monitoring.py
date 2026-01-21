#!/usr/bin/env python3
"""
Тесты для PaymentMonitoring

Feature ID: F-2025-017-stripe-payment
"""
import unittest
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

from payment_monitoring import PaymentMonitoring
from subscription_repository import SubscriptionRepository


class TestPaymentMonitoring(unittest.TestCase):
    """Тесты для PaymentMonitoring"""
    
    def setUp(self):
        """Настройка тестов"""
        self.repository = SubscriptionRepository()
        self.monitoring = PaymentMonitoring(repository=self.repository)
    
    def test_get_metrics(self):
        """Тест получения метрик"""
        metrics = self.monitoring.get_metrics(force_refresh=True)
        
        self.assertIn('timestamp', metrics)
        self.assertIn('subscriptions', metrics)
        self.assertIn('payments', metrics)
        self.assertIn('quota_usage', metrics)
        self.assertIn('webhooks', metrics)
        self.assertIn('sync_status', metrics)
        
        # Проверяем структуру метрик подписок
        subscriptions = metrics['subscriptions']
        self.assertIn('total', subscriptions)
        self.assertIn('active', subscriptions)
        self.assertIn('by_status', subscriptions)
    
    def test_check_alerts(self):
        """Тест проверки алертов"""
        alerts = self.monitoring.check_alerts()
        
        self.assertIsInstance(alerts, list)
        
        # Проверяем структуру алертов
        if alerts:
            alert = alerts[0]
            self.assertIn('level', alert)
            self.assertIn('type', alert)
            self.assertIn('message', alert)
            self.assertIn(alert['level'], ['error', 'warning', 'info'])
    
    def test_get_health_status(self):
        """Тест получения статуса здоровья"""
        health = self.monitoring.get_health_status()
        
        self.assertIn('status', health)
        self.assertIn('timestamp', health)
        self.assertIn('alerts_count', health)
        self.assertIn(health['status'], ['healthy', 'degraded', 'unhealthy', 'error'])
    
    def test_metrics_caching(self):
        """Тест кэширования метрик"""
        # Первый запрос
        metrics1 = self.monitoring.get_metrics(force_refresh=False)
        
        # Второй запрос (должен использовать кэш)
        metrics2 = self.monitoring.get_metrics(force_refresh=False)
        
        # Метрики должны быть одинаковыми (из кэша)
        self.assertEqual(metrics1['timestamp'], metrics2['timestamp'])
        
        # Принудительное обновление
        metrics3 = self.monitoring.get_metrics(force_refresh=True)
        
        # Метрики должны обновиться
        self.assertNotEqual(metrics1['timestamp'], metrics3['timestamp'])


if __name__ == '__main__':
    unittest.main()

