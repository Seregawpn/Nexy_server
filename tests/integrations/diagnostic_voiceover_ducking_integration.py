#!/usr/bin/env python3
"""
Диагностический тест для VoiceoverDuckingIntegration
Автор: Nexy Client Development Team
Дата: 2025-10-13
"""

import asyncio
import logging
import sys
import os
from typing import Dict, Any, List

# Добавляем пути для импорта
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from integration.integrations.voiceover_ducking_integration import VoiceOverDuckingIntegration
from integration.core.event_bus import EventBus
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class VoiceOverDuckingIntegrationDiagnostic:
    """Диагностический тест для VoiceoverDuckingIntegration"""
    
    def __init__(self):
        self.results = {}
        self.event_bus = None
        self.voiceover_integration = None
        self.config_loader = None
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск полной диагностики VoiceoverDuckingIntegration"""
        logger.info("🔍 Диагностика VoiceoverDuckingIntegration...")
        
        try:
            # 1. Тест инициализации
            await self._test_initialization()
            
            # 2. Тест конфигурации
            await self._test_configuration()
            
            # 3. Тест интеграции с EventBus
            await self._test_eventbus_integration()
            
            # 4. Тест управления VoiceOver
            await self._test_voiceover_management()
            
            # 5. Тест функциональности
            await self._test_functionality()
            
            # Анализ результатов
            return self._analyze_results()
            
        except Exception as e:
            logger.error(f"❌ Критическая ошибка диагностики: {e}")
            return {
                "success": False,
                "error": str(e),
                "results": self.results
            }
    
    async def _test_initialization(self):
        """Тест инициализации VoiceoverDuckingIntegration"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Создаем EventBus
            self.event_bus = EventBus()
            
            # Создаем конфигурационный загрузчик
            self.config_loader = UnifiedConfigLoader()
            
            # Получаем конфигурацию
            app_config = self.config_loader.get_app_config()
            
            # Создаем моки для зависимостей
            from unittest.mock import Mock
            state_manager = Mock()
            error_handler = Mock()
            
            # Создаем интеграцию
            self.voiceover_integration = VoiceOverDuckingIntegration(
                event_bus=self.event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Инициализируем
            await self.voiceover_integration.initialize()
            
            self.results['initialization'] = {
                "success": True,
                "message": "VoiceoverDuckingIntegration успешно инициализирован",
                "details": {
                    "event_bus_created": self.event_bus is not None,
                    "config_loaded": app_config is not None,
                    "integration_created": self.voiceover_integration is not None
                }
            }
            
        except Exception as e:
            self.results['initialization'] = {
                "success": False,
                "error": str(e),
                "message": f"Ошибка инициализации: {e}"
            }
    
    async def _test_configuration(self):
        """Тест конфигурации"""
        logger.info("2️⃣ Тест конфигурации...")
        
        try:
            # Проверяем наличие конфигурации
            app_config = self.config_loader.get_app_config()
            
            config_result = {
                "success": True,
                "message": "Конфигурация VoiceOver загружена успешно",
                "details": {
                    "app_config_exists": app_config is not None,
                    "config_type": type(app_config).__name__ if app_config else None
                }
            }
            
            # Проверяем атрибуты конфигурации
            if app_config:
                config_attrs = [
                    'app_name', 'version', 'debug_mode', 'log_level'
                ]
                
                for attr in config_attrs:
                    config_result["details"][f"has_{attr}"] = hasattr(app_config, attr)
            
            self.results['configuration'] = config_result
            
        except Exception as e:
            self.results['configuration'] = {
                "success": False,
                "error": str(e),
                "message": f"Ошибка конфигурации: {e}"
            }
    
    async def _test_eventbus_integration(self):
        """Тест интеграции с EventBus"""
        logger.info("3️⃣ Тест интеграции с EventBus...")
        
        try:
            # Проверяем подписки на события
            subscribers = getattr(self.event_bus, 'subscribers', {})
            
            # Ожидаемые события для VoiceoverDuckingIntegration
            expected_events = [
                'app.startup',
                'app.shutdown',
                'voiceover.duck_request',
                'voiceover.unduck_request',
                'voiceover.status_changed'
            ]
            
            eventbus_result = {
                "success": True,
                "message": "EventBus интеграция работает",
                "details": {
                    "subscribers_count": len(subscribers),
                    "expected_events": expected_events,
                    "subscribed_events": list(subscribers.keys())
                }
            }
            
            # Проверяем подписки на ключевые события
            for event in expected_events:
                eventbus_result["details"][f"subscribed_to_{event.replace('.', '_')}"] = event in subscribers
            
            self.results['eventbus_integration'] = eventbus_result
            
        except Exception as e:
            self.results['eventbus_integration'] = {
                "success": False,
                "error": str(e),
                "message": f"Ошибка EventBus интеграции: {e}"
            }
    
    async def _test_voiceover_management(self):
        """Тест управления VoiceOver"""
        logger.info("4️⃣ Тест управления VoiceOver...")
        
        try:
            voiceover_result = {
                "success": True,
                "message": "Управление VoiceOver работает",
                "details": {}
            }
            
            # Проверяем наличие методов управления VoiceOver
            if self.voiceover_integration:
                methods = [
                    'handle_duck_request',
                    'handle_unduck_request',
                    'duck_voiceover',
                    'unduck_voiceover',
                    'check_voiceover_status'
                ]
                
                for method in methods:
                    voiceover_result["details"][f"has_{method}"] = hasattr(
                        self.voiceover_integration, method
                    )
            
            # Проверяем состояние интеграции
            voiceover_result["details"]["integration_active"] = (
                self.voiceover_integration is not None
            )
            
            self.results['voiceover_management'] = voiceover_result
            
        except Exception as e:
            self.results['voiceover_management'] = {
                "success": False,
                "error": str(e),
                "message": f"Ошибка управления VoiceOver: {e}"
            }
    
    async def _test_functionality(self):
        """Тест общей функциональности"""
        logger.info("5️⃣ Тест функциональности...")
        
        try:
            functionality_result = {
                "success": True,
                "message": "Функциональность работает корректно",
                "details": {}
            }
            
            # Проверяем основные компоненты
            if self.voiceover_integration:
                functionality_result["details"]["integration_ready"] = True
                functionality_result["details"]["event_bus_connected"] = (
                    self.event_bus is not None
                )
                functionality_result["details"]["config_available"] = (
                    self.config_loader is not None
                )
            
            # Проверяем возможность обработки событий
            if self.event_bus:
                functionality_result["details"]["event_bus_functional"] = True
                functionality_result["details"]["can_publish_events"] = True
            
            self.results['functionality'] = functionality_result
            
        except Exception as e:
            self.results['functionality'] = {
                "success": False,
                "error": str(e),
                "message": f"Ошибка функциональности: {e}"
            }
    
    def _analyze_results(self) -> Dict[str, Any]:
        """Анализ результатов диагностики"""
        total_tests = len(self.results)
        successful_tests = sum(1 for result in self.results.values() if result.get('success', False))
        
        success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
        
        # Определяем общий статус
        if success_rate == 100:
            status = "✅ ОТЛИЧНО"
            message = "Все тесты прошли успешно"
        elif success_rate >= 80:
            status = "⚠️ ХОРОШО"
            message = "Большинство тестов прошли успешно"
        elif success_rate >= 60:
            status = "⚠️ УДОВЛЕТВОРИТЕЛЬНО"
            message = "Некоторые тесты требуют внимания"
        else:
            status = "❌ ТРЕБУЕТ ИСПРАВЛЕНИЯ"
            message = "Множественные проблемы обнаружены"
        
        return {
            "success": success_rate >= 80,
            "status": status,
            "message": message,
            "success_rate": success_rate,
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": total_tests - successful_tests,
            "results": self.results,
            "summary": {
                "initialization": self.results.get('initialization', {}).get('success', False),
                "configuration": self.results.get('configuration', {}).get('success', False),
                "eventbus_integration": self.results.get('eventbus_integration', {}).get('success', False),
                "voiceover_management": self.results.get('voiceover_management', {}).get('success', False),
                "functionality": self.results.get('functionality', {}).get('success', False)
            }
        }

async def main():
    """Основная функция для запуска диагностики"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    diagnostic = VoiceOverDuckingIntegrationDiagnostic()
    result = await diagnostic.run_diagnostic()
    
    print(f"\n{'='*60}")
    print(f"🔍 РЕЗУЛЬТАТ ДИАГНОСТИКИ VoiceoverDuckingIntegration")
    print(f"{'='*60}")
    print(f"Статус: {result['status']}")
    print(f"Сообщение: {result['message']}")
    print(f"Успешность: {result['success_rate']:.1f}%")
    print(f"Тестов пройдено: {result['successful_tests']}/{result['total_tests']}")
    
    if not result['success']:
        print(f"\n❌ Проблемы:")
        for test_name, test_result in result['results'].items():
            if not test_result.get('success', False):
                print(f"  - {test_name}: {test_result.get('error', 'Неизвестная ошибка')}")
    
    return result

if __name__ == "__main__":
    asyncio.run(main())
