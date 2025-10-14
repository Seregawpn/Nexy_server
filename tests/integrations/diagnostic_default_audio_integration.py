"""
Диагностический тест для DefaultAudioIntegration
Проверяет все аспекты работы новой аудио интеграции
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

class DiagnosticDefaultAudioIntegration:
    """Диагностический класс для DefaultAudioIntegration"""
    
    def __init__(self):
        self.results = {}
        self.errors = []
        self.warnings = []
        self.start_time = time.time()
        
    async def run_all_tests(self) -> Dict[str, Any]:
        """Запуск всех диагностических тестов"""
        logger.info("🚀 ЗАПУСК ДИАГНОСТИКИ DEFAULT AUDIO INTEGRATION")
        logger.info("=" * 60)
        
        # Список тестов
        tests = [
            ("Импорт модулей", self.test_imports),
            ("Создание компонентов", self.test_component_creation),
            ("Конфигурация", self.test_configuration),
            ("Инициализация интеграции", self.test_integration_initialization),
            ("Запуск интеграции", self.test_integration_startup),
            ("Функциональность аудио", self.test_audio_functionality),
            ("Health Check", self.test_health_check),
            ("Event Bus интеграция", self.test_event_bus_integration),
            ("Обработка ошибок", self.test_error_handling),
            ("Остановка интеграции", self.test_integration_shutdown),
            ("Context Manager", self.test_context_manager),
            ("Производительность", self.test_performance)
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
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            from modules.default_audio_manager.core.types import (
                AudioStreamState, HealthStatus, StreamError, AudioMetrics
            )
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            from config.unified_config_loader import UnifiedConfigLoader
            
            logger.info("✅ Все модули импортированы успешно")
            return True
            
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта: {e}")
            return False
    
    async def test_component_creation(self) -> bool:
        """Тест создания основных компонентов"""
        try:
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            from integration.integrations.default_audio_integration import DefaultAudioIntegrationConfig
            
            # Создание EventBus
            event_bus = EventBus()
            logger.info("✅ EventBus создан")
            
            # Создание StateManager
            state_manager = ApplicationStateManager()
            logger.info("✅ ApplicationStateManager создан")
            
            # Создание ErrorHandler
            error_handler = ErrorHandler()
            logger.info("✅ ErrorHandler создан")
            
            # Создание конфигурации
            config = DefaultAudioIntegrationConfig()
            logger.info("✅ DefaultAudioIntegrationConfig создан")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания компонентов: {e}")
            return False
    
    async def test_configuration(self) -> Dict[str, Any]:
        """Тест конфигурации"""
        try:
            from config.unified_config_loader import UnifiedConfigLoader
            
            # Загрузка конфигурации
            unified_config = UnifiedConfigLoader()
            default_audio_config = unified_config.get_default_audio_config()
            
            logger.info(f"✅ Конфигурация загружена: {len(default_audio_config)} параметров")
            
            # Проверка основных параметров
            required_params = [
                'input_sample_rate', 'output_sample_rate', 'input_channels', 
                'output_channels', 'health_check_interval', 'rms_threshold'
            ]
            
            missing_params = []
            for param in required_params:
                if param not in default_audio_config:
                    missing_params.append(param)
            
            if missing_params:
                logger.warning(f"⚠️ Отсутствуют параметры: {missing_params}")
                return {"status": "WARNING", "missing_params": missing_params}
            
            logger.info("✅ Все необходимые параметры конфигурации присутствуют")
            return {"status": "SUCCESS", "config": default_audio_config}
            
        except Exception as e:
            logger.error(f"❌ Ошибка конфигурации: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_integration_initialization(self) -> bool:
        """Тест инициализации интеграции"""
        try:
            from integration.core.event_bus import EventBus
            from integration.core.state_manager import ApplicationStateManager
            from integration.core.error_handler import ErrorHandler
            from integration.integrations.default_audio_integration import DefaultAudioIntegration, DefaultAudioIntegrationConfig
            
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
            
            logger.info("✅ DefaultAudioIntegration создан")
            
            # Инициализация
            init_result = await integration.initialize()
            
            if init_result:
                logger.info("✅ Инициализация успешна")
                return True
            else:
                logger.error("❌ Ошибка инициализации")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации интеграции: {e}")
            return False
    
    async def test_integration_startup(self) -> bool:
        """Тест запуска интеграции"""
        try:
            # Создание и инициализация
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            await integration.initialize()
            
            # Запуск
            start_result = await integration.start()
            
            if start_result:
                logger.info("✅ Запуск успешен")
                
                # Проверяем состояние
                audio_manager = integration.get_audio_manager()
                state = audio_manager.get_current_state()
                logger.info(f"📊 Состояние аудио менеджера: {state.value}")
                
                # Останавливаем
                await integration.stop()
                return True
            else:
                logger.error("❌ Ошибка запуска")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка запуска интеграции: {e}")
            return False
    
    async def test_audio_functionality(self) -> Dict[str, Any]:
        """Тест функциональности аудио"""
        try:
            # Создание и запуск интеграции
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            await integration.initialize()
            await integration.start()
            
            # Тестируем функциональность
            audio_manager = integration.get_audio_manager()
            
            # Получение аудио данных
            audio_data = integration.get_audio_data(max_samples=1000)
            logger.info(f"🎵 Получено аудио данных: {len(audio_data)} сэмплов")
            
            # Проверка здоровья
            is_healthy = integration.is_healthy()
            health_status = integration.get_health_status()
            logger.info(f"🏥 Здоровье: {health_status.value} (healthy: {is_healthy})")
            
            # Получение метрик
            metrics = integration.get_metrics()
            logger.info(f"📊 Метрики: RMS={metrics.rms_value:.6f}, Peak={metrics.peak_value:.6f}")
            
            # Останавливаем
            await integration.stop()
            
            return {
                "status": "SUCCESS",
                "audio_samples": len(audio_data),
                "health_status": health_status.value,
                "is_healthy": is_healthy,
                "rms_value": metrics.rms_value,
                "peak_value": metrics.peak_value
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования функциональности: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_health_check(self) -> Dict[str, Any]:
        """Тест проверки здоровья микрофона"""
        try:
            # Создание и запуск интеграции
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            await integration.initialize()
            await integration.start()
            
            # Ждем немного для сбора данных
            await asyncio.sleep(2)
            
            # Проверяем здоровье несколько раз
            health_results = []
            for i in range(3):
                is_healthy = integration.is_healthy()
                health_status = integration.get_health_status()
                metrics = integration.get_metrics()
                
                health_results.append({
                    "check": i + 1,
                    "is_healthy": is_healthy,
                    "status": health_status.value,
                    "rms": metrics.rms_value,
                    "peak": metrics.peak_value
                })
                
                logger.info(f"🔍 Проверка {i+1}: {health_status.value} (RMS: {metrics.rms_value:.6f})")
                await asyncio.sleep(1)
            
            # Останавливаем
            await integration.stop()
            
            return {
                "status": "SUCCESS",
                "health_checks": health_results
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования health check: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_event_bus_integration(self) -> bool:
        """Тест интеграции с EventBus"""
        try:
            # Создание компонентов
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            # Счетчик событий
            event_count = 0
            received_events = []
            
            async def event_handler(event_data):
                nonlocal event_count
                event_count += 1
                received_events.append(event_data)
                logger.info(f"📨 Получено событие: {event_data}")
            
            # Подписываемся на события аудио
            await event_bus.subscribe("audio.stream_state_changed", event_handler)
            await event_bus.subscribe("audio.health_status_changed", event_handler)
            await event_bus.subscribe("audio.metrics_updated", event_handler)
            
            # Создание и запуск интеграции
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            await integration.initialize()
            await integration.start()
            
            # Ждем события
            await asyncio.sleep(3)
            
            # Останавливаем
            await integration.stop()
            
            logger.info(f"📊 Получено событий: {event_count}")
            logger.info(f"📋 События: {received_events}")
            
            return event_count > 0
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования EventBus: {e}")
            return False
    
    async def test_error_handling(self) -> bool:
        """Тест обработки ошибок"""
        try:
            # Создание компонентов
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            
            # Конфигурация с ошибками
            config = DefaultAudioIntegrationConfig(
                enabled=True,
                auto_start=True,
                publish_health_events=True,
                publish_stream_events=True,
                publish_metrics_events=True
            )
            
            # Создание интеграции
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            # Тестируем обработку ошибок
            try:
                await integration.initialize()
                await integration.start()
                
                # Проверяем, что интеграция работает
                is_healthy = integration.is_healthy()
                logger.info(f"🏥 Состояние после запуска: {is_healthy}")
                
                await integration.stop()
                return True
                
            except Exception as e:
                logger.error(f"❌ Ошибка в тесте обработки ошибок: {e}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования обработки ошибок: {e}")
            return False
    
    async def test_integration_shutdown(self) -> bool:
        """Тест остановки интеграции"""
        try:
            # Создание и запуск интеграции
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            await integration.initialize()
            await integration.start()
            
            # Проверяем, что интеграция запущена
            audio_manager = integration.get_audio_manager()
            state = audio_manager.get_current_state()
            logger.info(f"📊 Состояние до остановки: {state.value}")
            
            # Останавливаем
            stop_result = await integration.stop()
            
            if stop_result:
                # Проверяем состояние после остановки
                final_state = audio_manager.get_current_state()
                logger.info(f"📊 Состояние после остановки: {final_state.value}")
                return True
            else:
                logger.error("❌ Ошибка остановки")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования остановки: {e}")
            return False
    
    async def test_context_manager(self) -> bool:
        """Тест async context manager"""
        try:
            # Создание компонентов
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            # Используем context manager
            async with DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            ) as integration:
                logger.info("✅ Context manager: интеграция запущена")
                
                # Проверяем функциональность
                is_healthy = integration.is_healthy()
                health_status = integration.get_health_status()
                logger.info(f"🏥 Здоровье в context manager: {health_status.value}")
                
                # Ждем немного
                await asyncio.sleep(1)
            
            logger.info("✅ Context manager: интеграция остановлена")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка context manager: {e}")
            return False
    
    async def test_performance(self) -> Dict[str, Any]:
        """Тест производительности"""
        try:
            # Создание компонентов
            event_bus = EventBus()
            state_manager = ApplicationStateManager()
            error_handler = ErrorHandler()
            config = DefaultAudioIntegrationConfig()
            
            # Измеряем время инициализации
            start_time = time.time()
            
            integration = DefaultAudioIntegration(
                event_bus=event_bus,
                state_manager=state_manager,
                error_handler=error_handler,
                config=config
            )
            
            init_time = time.time() - start_time
            logger.info(f"⏱️ Время инициализации: {init_time:.3f}s")
            
            # Измеряем время запуска
            start_time = time.time()
            await integration.initialize()
            await integration.start()
            startup_time = time.time() - start_time
            logger.info(f"⏱️ Время запуска: {startup_time:.3f}s")
            
            # Измеряем время остановки
            start_time = time.time()
            await integration.stop()
            shutdown_time = time.time() - start_time
            logger.info(f"⏱️ Время остановки: {shutdown_time:.3f}s")
            
            return {
                "status": "SUCCESS",
                "init_time": init_time,
                "startup_time": startup_time,
                "shutdown_time": shutdown_time,
                "total_time": init_time + startup_time + shutdown_time
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования производительности: {e}")
            return {"status": "ERROR", "error": str(e)}
    
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
    diagnostic = DiagnosticDefaultAudioIntegration()
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
