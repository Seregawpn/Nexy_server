"""
Простой диагностический тест для DefaultAudioIntegration
Проверяет основные аспекты работы новой аудио интеграции
"""

import asyncio
import logging
import time
import sys
import os
from typing import Dict, Any, List, Optional
import traceback

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleDiagnosticDefaultAudioIntegration:
    """Простой диагностический класс для DefaultAudioIntegration"""
    
    def __init__(self):
        self.results = {}
        self.errors = []
        self.warnings = []
        self.start_time = time.time()
        
    async def run_all_tests(self) -> Dict[str, Any]:
        """Запуск всех диагностических тестов"""
        logger.info("🚀 ЗАПУСК ПРОСТОЙ ДИАГНОСТИКИ DEFAULT AUDIO INTEGRATION")
        logger.info("=" * 60)
        
        # Список тестов
        tests = [
            ("Импорт модулей", self.test_imports),
            ("Создание интеграции", self.test_integration_creation),
            ("Запуск интеграции", self.test_integration_startup),
            ("Функциональность", self.test_functionality),
            ("Остановка интеграции", self.test_integration_shutdown)
        ]
        
        # Запуск тестов
        for test_name, test_func in tests:
            try:
                logger.info(f"\n🧪 ТЕСТ: {test_name}")
                logger.info("-" * 40)
                
                result = await test_func()
                self.results[test_name] = {
                    "status": "SUCCESS" if result else "FAILED",
                    "details": result if isinstance(result, dict) else {"result": result}
                }
                
                if result:
                    logger.info(f"✅ {test_name}: УСПЕХ")
                else:
                    logger.error(f"❌ {test_name}: НЕУДАЧА")
                    
            except Exception as e:
                logger.error(f"❌ {test_name}: ОШИБКА - {e}")
                self.results[test_name] = {
                    "status": "ERROR",
                    "error": str(e),
                    "traceback": traceback.format_exc()
                }
                self.errors.append(f"{test_name}: {e}")
        
        # Генерация отчета
        return self.generate_report()
    
    async def test_imports(self) -> bool:
        """Тест импорта всех необходимых модулей"""
        try:
            # Импорт основных компонентов
            from integration.integrations.default_audio_integration import (
                DefaultAudioIntegration, DefaultAudioIntegrationConfig
            )
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            
            logger.info("✅ Все модули импортированы успешно")
            return True
            
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта: {e}")
            return False
    
    async def test_integration_creation(self) -> bool:
        """Тест создания интеграции"""
        try:
            from integration.integrations.default_audio_integration import (
                DefaultAudioIntegration, DefaultAudioIntegrationConfig
            )
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            
            # Создание компонентов
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            # Создание интеграции
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            logger.info("✅ DefaultAudioIntegration создан успешно")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания интеграции: {e}")
            return False
    
    async def test_integration_startup(self) -> bool:
        """Тест запуска интеграции"""
        try:
            from integration.integrations.default_audio_integration import (
                DefaultAudioIntegration, DefaultAudioIntegrationConfig
            )
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            
            # Создание компонентов
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            # Создание интеграции
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            # Инициализация
            init_result = await integration.initialize()
            if not init_result:
                logger.error("❌ Ошибка инициализации")
                return False
            
            # Запуск
            start_result = await integration.start()
            if not start_result:
                logger.error("❌ Ошибка запуска")
                return False
            
            logger.info("✅ Интеграция запущена успешно")
            
            # Сохраняем интеграцию для следующих тестов
            self.integration = integration
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка запуска интеграции: {e}")
            return False
    
    async def test_functionality(self) -> Dict[str, Any]:
        """Тест функциональности"""
        try:
            if not hasattr(self, 'integration'):
                logger.error("❌ Интеграция не создана")
                return {"status": "ERROR", "error": "Integration not created"}
            
            integration = self.integration
            
            # Тестируем функциональность
            is_healthy = integration.is_healthy()
            health_status = integration.get_health_status()
            metrics = integration.get_metrics()
            
            logger.info(f"🏥 Здоровье: {health_status.value} (healthy: {is_healthy})")
            logger.info(f"📊 Метрики: RMS={metrics.rms_value:.6f}, Peak={metrics.peak_value:.6f}")
            
            # Получаем аудио данные
            audio_data = integration.get_audio_data(max_samples=1000)
            logger.info(f"🎵 Получено аудио данных: {len(audio_data)} сэмплов")
            
            return {
                "status": "SUCCESS",
                "is_healthy": is_healthy,
                "health_status": health_status.value,
                "rms_value": metrics.rms_value,
                "peak_value": metrics.peak_value,
                "audio_samples": len(audio_data)
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования функциональности: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_integration_shutdown(self) -> bool:
        """Тест остановки интеграции"""
        try:
            if not hasattr(self, 'integration'):
                logger.error("❌ Интеграция не создана")
                return False
            
            integration = self.integration
            
            # Останавливаем
            stop_result = await integration.stop()
            
            if stop_result:
                logger.info("✅ Интеграция остановлена успешно")
                return True
            else:
                logger.error("❌ Ошибка остановки")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка остановки интеграции: {e}")
            return False
    
    def generate_report(self) -> Dict[str, Any]:
        """Генерация итогового отчета"""
        end_time = time.time()
        total_time = end_time - self.start_time
        
        # Подсчет результатов
        total_tests = len(self.results)
        successful_tests = sum(1 for result in self.results.values() if result["status"] == "SUCCESS")
        failed_tests = sum(1 for result in self.results.values() if result["status"] == "FAILED")
        error_tests = sum(1 for result in self.results.values() if result["status"] == "ERROR")
        
        success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
        
        report = {
            "summary": {
                "total_tests": total_tests,
                "successful": successful_tests,
                "failed": failed_tests,
                "errors": error_tests,
                "success_rate": success_rate,
                "total_time": total_time
            },
            "results": self.results,
            "errors": self.errors,
            "warnings": self.warnings
        }
        
        # Вывод отчета
        logger.info("\n" + "=" * 60)
        logger.info("📊 ИТОГОВЫЙ ОТЧЕТ ДИАГНОСТИКИ")
        logger.info("=" * 60)
        logger.info(f"Всего тестов: {total_tests}")
        logger.info(f"Успешных: {successful_tests}")
        logger.info(f"Неудачных: {failed_tests}")
        logger.info(f"Ошибок: {error_tests}")
        logger.info(f"Успешность: {success_rate:.1f}%")
        logger.info(f"Общее время: {total_time:.2f}s")
        
        if self.errors:
            logger.info(f"\n❌ ОШИБКИ ({len(self.errors)}):")
            for error in self.errors:
                logger.info(f"   - {error}")
        
        if success_rate >= 90:
            logger.info("\n🎉 ДИАГНОСТИКА ПРОЙДЕНА УСПЕШНО!")
        elif success_rate >= 70:
            logger.info("\n⚠️ ДИАГНОСТИКА ПРОЙДЕНА С ПРЕДУПРЕЖДЕНИЯМИ")
        else:
            logger.info("\n❌ ДИАГНОСТИКА НЕ ПРОЙДЕНА")
        
        return report

async def main():
    """Основная функция"""
    diagnostic = SimpleDiagnosticDefaultAudioIntegration()
    report = await diagnostic.run_all_tests()
    return report

if __name__ == "__main__":
    try:
        report = asyncio.run(main())
        exit(0 if report["summary"]["success_rate"] >= 70 else 1)
    except KeyboardInterrupt:
        logger.info("\n⏹ Диагностика прервана пользователем")
        exit(1)
    except Exception as e:
        logger.error(f"\n💥 Критическая ошибка: {e}")
        traceback.print_exc()
        exit(1)
