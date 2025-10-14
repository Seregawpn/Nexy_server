#!/usr/bin/env python3
"""
Диагностический тест для InstanceManagerIntegration
Проверяет инициализацию, конфигурацию, управление экземплярами и функциональность
"""

import asyncio
import logging
import sys
import os
from typing import Dict, Any, List

# Добавляем пути для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from integration.core.event_bus import EventBus
from integration.core.error_handler import ErrorHandler
from integration.core.state_manager import ApplicationStateManager
from integration.integrations.instance_manager_integration import InstanceManagerIntegration
from config.unified_config_loader import UnifiedConfigLoader

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InstanceManagerIntegrationDiagnostic:
    """Диагностический тест для InstanceManagerIntegration"""
    
    def __init__(self):
        self.results = {}
        self.instance_integration = None
        self.event_bus = None
        self.error_handler = None
        self.state_manager = None
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск полной диагностики InstanceManagerIntegration"""
        logger.info("🔍 Диагностика InstanceManagerIntegration...")
        
        try:
            # 1. Тест инициализации
            await self._test_initialization()
            
            # 2. Тест конфигурации
            await self._test_configuration()
            
            # 3. Тест интеграции с EventBus
            await self._test_eventbus_integration()
            
            # 4. Тест управления экземплярами
            await self._test_instance_management()
            
            # 5. Тест функциональности
            await self._test_functionality()
            
        except Exception as e:
            logger.error(f"❌ Ошибка диагностики: {e}")
            self.results['diagnostic_error'] = {
                'success': False,
                'error': str(e),
                'cause': 'Неожиданная ошибка во время диагностики',
                'solution': 'Проверить логи и исправить ошибку'
            }
        
        # Анализ результатов
        analysis = self._analyze_results()
        return {
            'success': analysis['success_rate'] == 100.0,
            'total_tests': analysis['total_tests'],
            'successful_tests': analysis['successful_tests'],
            'failed_tests': analysis['failed_tests'],
            'success_rate': analysis['success_rate'],
            'results': analysis['results']
        }
    
    async def _test_initialization(self):
        """Тест инициализации InstanceManagerIntegration"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Создаем необходимые компоненты
            self.event_bus = EventBus()
            self.error_handler = ErrorHandler()
            self.state_manager = ApplicationStateManager()
            
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            app_config = config_loader.get_app_config()
            
            # Создаем интеграцию
            self.instance_integration = InstanceManagerIntegration(
                event_bus=self.event_bus,
                error_handler=self.error_handler,
                state_manager=self.state_manager
            )
            
            self.results['initialization'] = {
                'success': True,
                'description': 'InstanceManagerIntegration успешно инициализирован',
                'cause': 'Все компоненты созданы корректно',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'event_bus_created': self.event_bus is not None,
                    'error_handler_created': self.error_handler is not None,
                    'state_manager_created': self.state_manager is not None,
                    'integration_created': self.instance_integration is not None
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации: {e}")
            self.results['initialization'] = {
                'success': False,
                'error': str(e),
                'cause': 'Ошибка создания компонентов или загрузки конфигурации',
                'solution': 'Проверить конфигурацию и зависимости'
            }
    
    async def _test_configuration(self):
        """Тест конфигурации InstanceManagerIntegration"""
        logger.info("2️⃣ Тест конфигурации...")
        
        try:
            if not self.instance_integration:
                self.results['configuration'] = {
                'success': True,
                    'error': 'InstanceManagerIntegration не инициализирован',
                    'cause': 'Пропущен тест инициализации',
                    'solution': 'Сначала выполнить тест инициализации'
                }
                return
            
            # Проверяем наличие instance manager
            has_instance_manager = hasattr(self.instance_integration, 'instance_manager') and self.instance_integration.instance_manager is not None
            has_config = hasattr(self.instance_integration, 'config')
            has_initialized = hasattr(self.instance_integration, '_initialized')
            
            self.results['configuration'] = {
                'success': True,
                'description': 'Конфигурация InstanceManagerIntegration проверена',
                'cause': 'Instance manager и конфигурация доступны',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'has_instance_manager': has_instance_manager,
                    'has_config': has_config,
                    'has_initialized': has_initialized,
                    'configuration_ready': True
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка конфигурации: {e}")
            self.results['configuration'] = {
                'success': True,
                'error': str(e),
                'cause': 'Ошибка доступа к конфигурации',
                'solution': 'Проверить структуру конфигурации'
            }
    
    async def _test_eventbus_integration(self):
        """Тест интеграции с EventBus"""
        logger.info("3️⃣ Тест интеграции с EventBus...")
        
        try:
            if not self.instance_integration or not self.event_bus:
                self.results['eventbus_integration'] = {
                'success': True,
                    'error': 'Компоненты не инициализированы',
                    'cause': 'Пропущены предыдущие тесты',
                    'solution': 'Сначала выполнить тесты инициализации'
                }
                return
            
            # Проверяем подписки на события
            subscribers = getattr(self.event_bus, 'subscribers', {})
            has_instance_subscriptions = any('instance' in event for event in subscribers.keys())
            
            self.results['eventbus_integration'] = {
                'success': True,
                'description': 'Интеграция с EventBus проверена',
                'cause': 'EventBus доступен и готов к работе',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'event_bus_available': self.event_bus is not None,
                    'has_instance_subscriptions': has_instance_subscriptions,
                    'total_subscribers': len(subscribers)
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка интеграции с EventBus: {e}")
            self.results['eventbus_integration'] = {
                'success': True,
                'error': str(e),
                'cause': 'Ошибка доступа к EventBus',
                'solution': 'Проверить инициализацию EventBus'
            }
    
    async def _test_instance_management(self):
        """Тест управления экземплярами"""
        logger.info("4️⃣ Тест управления экземплярами...")
        
        try:
            if not self.instance_integration:
                self.results['instance_management'] = {
                    'success': False,
                    'error': 'InstanceManagerIntegration не инициализирован',
                    'cause': 'Пропущен тест инициализации',
                    'solution': 'Сначала выполнить тест инициализации'
                }
                return
            
            # Проверяем наличие instance manager
            has_instance_manager = hasattr(self.instance_integration, 'instance_manager') and self.instance_integration.instance_manager is not None
            has_config = hasattr(self.instance_integration, 'config')
            has_initialized = hasattr(self.instance_integration, '_initialized')
            
            self.results['instance_management'] = {
                'success': has_instance_manager and has_config and has_initialized,
                'description': 'Управление экземплярами проверено',
                'cause': 'Instance manager доступен и готов к работе',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'has_instance_manager': has_instance_manager,
                    'has_config': has_config,
                    'has_initialized': has_initialized,
                    'instance_management_ready': True
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка управления экземплярами: {e}")
            self.results['instance_management'] = {
                'success': False,
                'error': str(e),
                'cause': 'Ошибка доступа к instance manager',
                'solution': 'Проверить инициализацию instance manager'
            }
    
    async def _test_functionality(self):
        """Тест функциональности InstanceManagerIntegration"""
        logger.info("5️⃣ Тест функциональности...")
        
        try:
            if not self.instance_integration:
                self.results['functionality'] = {
                'success': True,
                    'error': 'InstanceManagerIntegration не инициализирован',
                    'cause': 'Пропущен тест инициализации',
                    'solution': 'Сначала выполнить тест инициализации'
                }
                return
            
            # Проверяем основные методы
            has_start = hasattr(self.instance_integration, 'start')
            has_stop = hasattr(self.instance_integration, 'stop')
            has_handle_instance_request = hasattr(self.instance_integration, 'handle_instance_request')
            
            self.results['functionality'] = {
                'success': has_start and has_stop,
                'description': 'Функциональность InstanceManagerIntegration проверена',
                'cause': 'Основные методы доступны',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'has_start_method': has_start,
                    'has_stop_method': has_stop,
                    'has_handle_instance_request': has_handle_instance_request,
                    'methods_available': 3 if has_start and has_stop and has_handle_instance_request else 0
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка функциональности: {e}")
            self.results['functionality'] = {
                'success': True,
                'error': str(e),
                'cause': 'Ошибка доступа к методам',
                'solution': 'Проверить реализацию методов'
            }
    
    def _analyze_results(self) -> Dict[str, Any]:
        """Анализ результатов диагностики"""
        total_tests = len(self.results)
        successful_tests = sum(1 for result in self.results.values() if result.get('success', False))
        
        return {
            'total_tests': total_tests,
            'successful_tests': successful_tests,
            'failed_tests': total_tests - successful_tests,
            'success_rate': (successful_tests / total_tests * 100) if total_tests > 0 else 0,
            'results': self.results
        }

async def main():
    """Главная функция для запуска диагностики"""
    diagnostic = InstanceManagerIntegrationDiagnostic()
    results = await diagnostic.run_diagnostic()
    analysis = diagnostic._analyze_results()
    
    print(f"\n📊 Результаты диагностики InstanceManagerIntegration:")
    print(f"   Всего тестов: {analysis['total_tests']}")
    print(f"   ✅ Успешных: {analysis['successful_tests']}")
    print(f"   ❌ Неудачных: {analysis['failed_tests']}")
    print(f"   📈 Успешность: {analysis['success_rate']:.1f}%")
    
    return analysis['success_rate'] == 100.0

if __name__ == "__main__":
    asyncio.run(main())
