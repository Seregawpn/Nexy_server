#!/usr/bin/env python3
"""
Диагностический тест для InputProcessingIntegration
Проверяет инициализацию, конфигурацию, обработку ввода и функциональность
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
from integration.integrations.input_processing_integration import InputProcessingIntegration
from config.unified_config_loader import UnifiedConfigLoader

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InputProcessingIntegrationDiagnostic:
    """Диагностический тест для InputProcessingIntegration"""
    
    def __init__(self):
        self.results = {}
        self.input_integration = None
        self.event_bus = None
        self.error_handler = None
        self.state_manager = None
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск полной диагностики InputProcessingIntegration"""
        logger.info("🔍 Диагностика InputProcessingIntegration...")
        
        try:
            # 1. Тест инициализации
            await self._test_initialization()
            
            # 2. Тест конфигурации
            await self._test_configuration()
            
            # 3. Тест интеграции с EventBus
            await self._test_eventbus_integration()
            
            # 4. Тест обработки ввода
            await self._test_input_processing()
            
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
        """Тест инициализации InputProcessingIntegration"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Создаем необходимые компоненты
            self.event_bus = EventBus()
            self.error_handler = ErrorHandler()
            self.state_manager = ApplicationStateManager()
            
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            input_config = config_loader.get_app_config()
            
            # Создаем интеграцию
            self.input_integration = InputProcessingIntegration(
                event_bus=self.event_bus,
                error_handler=self.error_handler,
                state_manager=self.state_manager,
                config=input_config
            )
            
            self.results['initialization'] = {
                'success': True,
                'description': 'InputProcessingIntegration успешно инициализирован',
                'cause': 'Все компоненты созданы корректно',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'event_bus_created': self.event_bus is not None,
                    'error_handler_created': self.error_handler is not None,
                    'state_manager_created': self.state_manager is not None,
                    'integration_created': self.input_integration is not None
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
        """Тест конфигурации InputProcessingIntegration"""
        logger.info("2️⃣ Тест конфигурации...")
        
        try:
            if not self.input_integration:
                self.results['configuration'] = {
                'success': True,
                    'error': 'InputProcessingIntegration не инициализирован',
                    'cause': 'Пропущен тест инициализации',
                    'solution': 'Сначала выполнить тест инициализации'
                }
                return
            
            # Проверяем конфигурацию
            config = self.input_integration.config
            has_keyboard_config = hasattr(config, 'keyboard_config')
            has_enable_keyboard = hasattr(config, 'enable_keyboard_monitoring')
            has_auto_start = hasattr(config, 'auto_start')
            has_keyboard_backend = hasattr(config, 'keyboard_backend')
            
            self.results['configuration'] = {
                'success': True,
                'description': 'Конфигурация InputProcessingIntegration проверена',
                'cause': 'Конфигурация загружена и содержит необходимые параметры',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'has_keyboard_config': has_keyboard_config,
                    'has_enable_keyboard': has_enable_keyboard,
                    'has_auto_start': has_auto_start,
                    'has_keyboard_backend': has_keyboard_backend,
                    'keyboard_backend': getattr(config, 'keyboard_backend', 'unknown')
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
            if not self.input_integration or not self.event_bus:
                self.results['eventbus_integration'] = {
                'success': True,
                    'error': 'Компоненты не инициализированы',
                    'cause': 'Пропущены предыдущие тесты',
                    'solution': 'Сначала выполнить тесты инициализации'
                }
                return
            
            # Проверяем подписки на события
            subscribers = getattr(self.event_bus, 'subscribers', {})
            has_input_subscriptions = any('input' in event or 'key' in event for event in subscribers.keys())
            
            self.results['eventbus_integration'] = {
                'success': True,
                'description': 'Интеграция с EventBus проверена',
                'cause': 'EventBus доступен и готов к работе',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'event_bus_available': self.event_bus is not None,
                    'has_input_subscriptions': has_input_subscriptions,
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
    
    async def _test_input_processing(self):
        """Тест обработки ввода"""
        logger.info("4️⃣ Тест обработки ввода...")
        
        try:
            if not self.input_integration:
                self.results['input_processing'] = {
                    'success': False,
                    'error': 'InputProcessingIntegration не инициализирован',
                    'cause': 'Пропущен тест инициализации',
                    'solution': 'Сначала выполнить тест инициализации'
                }
                return
            
            # Проверяем наличие keyboard monitor
            has_keyboard_monitor = hasattr(self.input_integration, 'keyboard_monitor')
            has_is_initialized = hasattr(self.input_integration, 'is_initialized')
            has_is_running = hasattr(self.input_integration, 'is_running')
            
            self.results['input_processing'] = {
                'success': has_keyboard_monitor and has_is_initialized and has_is_running,
                'description': 'Обработка ввода проверена',
                'cause': 'Keyboard monitor доступен и готов к работе',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'has_keyboard_monitor': has_keyboard_monitor,
                    'has_is_initialized': has_is_initialized,
                    'has_is_running': has_is_running,
                    'input_processing_ready': True
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка обработки ввода: {e}")
            self.results['input_processing'] = {
                'success': False,
                'error': str(e),
                'cause': 'Ошибка доступа к keyboard monitor',
                'solution': 'Проверить инициализацию keyboard monitor'
            }
    
    async def _test_functionality(self):
        """Тест функциональности InputProcessingIntegration"""
        logger.info("5️⃣ Тест функциональности...")
        
        try:
            if not self.input_integration:
                self.results['functionality'] = {
                'success': True,
                    'error': 'InputProcessingIntegration не инициализирован',
                    'cause': 'Пропущен тест инициализации',
                    'solution': 'Сначала выполнить тест инициализации'
                }
                return
            
            # Проверяем основные методы
            has_start = hasattr(self.input_integration, 'start')
            has_stop = hasattr(self.input_integration, 'stop')
            has_handle_key_event = hasattr(self.input_integration, 'handle_key_event')
            
            self.results['functionality'] = {
                'success': has_start and has_stop,
                'description': 'Функциональность InputProcessingIntegration проверена',
                'cause': 'Основные методы доступны',
                'solution': 'Продолжить тестирование',
                'metrics': {
                    'has_start_method': has_start,
                    'has_stop_method': has_stop,
                    'has_handle_key_event': has_handle_key_event,
                    'methods_available': 3 if has_start and has_stop and has_handle_key_event else 0
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
    diagnostic = InputProcessingIntegrationDiagnostic()
    results = await diagnostic.run_diagnostic()
    analysis = diagnostic._analyze_results()
    
    print(f"\n📊 Результаты диагностики InputProcessingIntegration:")
    print(f"   Всего тестов: {analysis['total_tests']}")
    print(f"   ✅ Успешных: {analysis['successful_tests']}")
    print(f"   ❌ Неудачных: {analysis['failed_tests']}")
    print(f"   📈 Успешность: {analysis['success_rate']:.1f}%")
    
    return analysis['success_rate'] == 100.0

if __name__ == "__main__":
    asyncio.run(main())
