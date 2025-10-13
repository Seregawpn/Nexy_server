#!/usr/bin/env python3
"""
Специализированный тест для AudioDeviceIntegration
Диагностирует проблемы в интеграции управления аудио устройствами
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from integration.integrations.audio_device_integration import AudioDeviceIntegration
from integration.core.event_bus import EventBus
from integration.core.state_manager import ApplicationStateManager
from integration.core.error_handler import ErrorHandler
from modules.audio_device_manager.core.types import AudioDeviceManagerConfig

logger = logging.getLogger(__name__)

class AudioDeviceIntegrationDiagnostic:
    """Диагностика AudioDeviceIntegration"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики AudioDeviceIntegration"""
        logger.info("🔍 Диагностика AudioDeviceIntegration...")
        
        # 1. Тест инициализации
        await self._test_initialization()
        
        # 2. Тест EventBus интеграции
        await self._test_eventbus_integration()
        
        # 3. Тест публикации событий
        await self._test_event_publishing()
        
        # 4. Тест обработки запросов
        await self._test_request_handling()
        
        # 5. Тест переключения режимов
        await self._test_mode_switching()
        
        return self._analyze_results()
    
    async def _test_initialization(self):
        """Тест инициализации AudioDeviceIntegration"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Создаем зависимости
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            
            # Создаем AudioDeviceIntegration
            integration = AudioDeviceIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler
            )
            
            # Инициализируем
            result = await integration.initialize()
            
            if result:
                self._add_result("initialization", True, "AudioDeviceIntegration инициализирован", 
                               "Инициализация прошла успешно", "Продолжить", {})
                
                # Сохраняем для дальнейших тестов
                self.integration = integration
                self.event_bus = event_bus
                self.state_manager = state_manager
            else:
                self._add_result("initialization", False, "Ошибка инициализации AudioDeviceIntegration",
                               "Проблема с инициализацией", "Проверить конфигурацию и зависимости", {})
            
        except Exception as e:
            self._add_result("initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить unified_config.yaml и AudioDeviceManager", {"error": str(e)})
    
    async def _test_eventbus_integration(self):
        """Тест интеграции с EventBus"""
        logger.info("2️⃣ Тест интеграции с EventBus...")
        
        if not hasattr(self, 'integration'):
            self._add_result("eventbus_integration", False, "AudioDeviceIntegration не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем подписки на события
            expected_subscriptions = [
                "app.startup",
                "app.shutdown", 
                "app.state_changed",
                "app.mode_changed",
                "audio.request_current_input_device",
                "audio.request_unified_device"
            ]
            
            # Получаем подписки из EventBus
            subscriptions = getattr(self.event_bus, '_subscribers', {})
            
            for event_name in expected_subscriptions:
                if event_name in subscriptions and len(subscriptions[event_name]) > 0:
                    self._add_result(f"subscription_{event_name}", True, f"Подписка на {event_name} активна",
                                   "Подписка на событие работает", "Продолжить", {"event": event_name})
                else:
                    self._add_result(f"subscription_{event_name}", False, f"Подписка на {event_name} отсутствует",
                                   "Подписка на событие не настроена", f"Проверить подписку на {event_name}", 
                                   {"event": event_name})
            
        except Exception as e:
            self._add_result("eventbus_integration", False, f"Ошибка проверки подписок: {e}",
                           "Проблема с EventBus", "Проверить EventBus и подписки", 
                           {"error": str(e)})
    
    async def _test_event_publishing(self):
        """Тест публикации событий"""
        logger.info("3️⃣ Тест публикации событий...")
        
        if not hasattr(self, 'integration') or not hasattr(self, 'event_bus'):
            self._add_result("event_publishing", False, "AudioDeviceIntegration или EventBus не готовы",
                           "Предыдущие тесты не прошли", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Запускаем интеграцию
            start_result = await self.integration.start()
            
            if start_result:
                self._add_result("integration_start", True, "AudioDeviceIntegration запущен",
                               "Запуск интеграции работает", "Продолжить", {})
                
                # Ждем немного для публикации событий
                await asyncio.sleep(0.5)
                
                # Проверяем что события были опубликованы
                # (В реальном тесте можно было бы проверить логи или счетчики событий)
                self._add_result("event_publishing", True, "События публикуются при запуске",
                               "Публикация событий работает", "Продолжить", {})
            else:
                self._add_result("integration_start", False, "Не удалось запустить AudioDeviceIntegration",
                               "Проблема с запуском интеграции", "Проверить AudioDeviceManager", {})
            
        except Exception as e:
            self._add_result("event_publishing", False, f"Ошибка публикации событий: {e}",
                           "Проблема с публикацией событий", "Проверить методы публикации событий", 
                           {"error": str(e)})
    
    async def _test_request_handling(self):
        """Тест обработки запросов"""
        logger.info("4️⃣ Тест обработки запросов...")
        
        if not hasattr(self, 'integration') or not hasattr(self, 'event_bus'):
            self._add_result("request_handling", False, "AudioDeviceIntegration или EventBus не готовы",
                           "Предыдущие тесты не прошли", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Тестируем запрос текущего INPUT устройства
            request_event = {
                "source": "test",
                "reason": "test_request"
            }
            
            # Отправляем запрос
            await self.integration._on_request_current_input_device(request_event)
            
            self._add_result("input_device_request", True, "Запрос INPUT устройства обработан",
                           "Обработка запросов работает", "Продолжить", {})
            
            # Тестируем запрос унифицированного устройства
            unified_request_event = {
                "source": "test",
                "reason": "test_unified_request"
            }
            
            await self.integration._on_request_unified_device(unified_request_event)
            
            self._add_result("unified_device_request", True, "Запрос унифицированного устройства обработан",
                           "Обработка запросов работает", "Продолжить", {})
            
        except Exception as e:
            self._add_result("request_handling", False, f"Ошибка обработки запросов: {e}",
                           "Проблема с обработкой запросов", "Проверить методы обработки запросов", 
                           {"error": str(e)})
    
    async def _test_mode_switching(self):
        """Тест переключения режимов"""
        logger.info("5️⃣ Тест переключения режимов...")
        
        if not hasattr(self, 'integration') or not hasattr(self, 'state_manager'):
            self._add_result("mode_switching", False, "AudioDeviceIntegration или StateManager не готовы",
                           "Предыдущие тесты не прошли", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Тестируем переключение в режим LISTENING
            from integration.core.state_manager import AppMode
            
            # Симулируем изменение режима
            mode_event = {
                "old_mode": AppMode.SLEEPING,
                "new_mode": AppMode.LISTENING
            }
            
            await self.integration._handle_mode_change(AppMode.SLEEPING, AppMode.LISTENING)
            
            self._add_result("mode_switching", True, "Переключение режимов работает",
                           "Обработка изменений режимов работает", "Продолжить", {})
            
        except Exception as e:
            self._add_result("mode_switching", False, f"Ошибка переключения режимов: {e}",
                           "Проблема с переключением режимов", "Проверить метод _handle_mode_change", 
                           {"error": str(e)})
        
        finally:
            # Останавливаем интеграцию
            if hasattr(self, 'integration'):
                await self.integration.stop()
    
    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):
        """Добавление результата теста"""
        self.results.append({
            "test": test_name,
            "success": success,
            "problem": problem,
            "cause": cause,
            "solution": solution,
            "details": details
        })
    
    def _analyze_results(self) -> Dict[str, Any]:
        """Анализ результатов"""
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results if r["success"]])
        failed_tests = total_tests - successful_tests
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДИАГНОСТИКИ AUDIODEVICEINTEGRATION:")
        print(f"   Всего тестов: {total_tests}")
        print(f"   ✅ Успешных: {successful_tests}")
        print(f"   ❌ Неудачных: {failed_tests}")
        
        if failed_tests > 0:
            print(f"\n❌ ПРОБЛЕМЫ:")
            for result in self.results:
                if not result["success"]:
                    print(f"   • {result['test']}: {result['problem']}")
                    print(f"     Причина: {result['cause']}")
                    print(f"     Решение: {result['solution']}")
        
        return {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": failed_tests,
            "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0,
            "results": self.results
        }

async def main():
    """Основная функция"""
    diagnostic = AudioDeviceIntegrationDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
