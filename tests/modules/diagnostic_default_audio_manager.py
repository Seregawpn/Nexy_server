"""
Диагностический тест для DefaultAudioManager
Проверяет все аспекты работы нового аудио модуля
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

class DiagnosticDefaultAudioManager:
    """Диагностический класс для DefaultAudioManager"""
    
    def __init__(self):
        self.results = {}
        self.errors = []
        self.warnings = []
        self.start_time = time.time()
        
    async def run_all_tests(self) -> Dict[str, Any]:
        """Запуск всех диагностических тестов"""
        logger.info("🚀 ЗАПУСК ДИАГНОСТИКИ DEFAULT AUDIO MANAGER")
        logger.info("=" * 60)
        
        # Список тестов
        tests = [
            ("Импорт модулей", self.test_imports),
            ("Создание конфигурации", self.test_config_creation),
            ("Загрузка конфигурации", self.test_config_loading),
            ("Создание менеджера", self.test_manager_creation),
            ("Запуск менеджера", self.test_manager_startup),
            ("Аудио потоки", self.test_audio_streams),
            ("Health Checker", self.test_health_checker),
            ("Метрики аудио", self.test_audio_metrics),
            ("Обработка ошибок", self.test_error_handling),
            ("Переоткрытие потоков", self.test_stream_reopening),
            ("Остановка менеджера", self.test_manager_shutdown),
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
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            from modules.default_audio_manager.core.types import (
                AudioStreamState, HealthStatus, StreamError, AudioMetrics
            )
            from modules.default_audio_manager.core.health_checker import HealthChecker
            from modules.default_audio_manager.config.default_config import DefaultAudioConfigLoader
            
            logger.info("✅ Все модули DefaultAudioManager импортированы успешно")
            return True
            
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта: {e}")
            return False
    
    async def test_config_creation(self) -> bool:
        """Тест создания конфигурации"""
        try:
            from modules.default_audio_manager.core.types import DefaultAudioConfig
            
            # Создание конфигурации по умолчанию
            config = DefaultAudioConfig()
            logger.info("✅ DefaultAudioConfig создан с параметрами по умолчанию")
            
            # Проверка основных параметров
            assert config.input_sample_rate == 16000
            assert config.output_sample_rate == 48000
            assert config.input_channels == 1
            assert config.output_channels == 1
            assert config.dtype == "int16"
            assert config.health_check_interval == 1.0
            assert config.rms_threshold == 1e-4
            
            logger.info("✅ Все параметры конфигурации корректны")
            
            # Создание кастомной конфигурации
            custom_config = DefaultAudioConfig(
                input_sample_rate=24000,
                health_check_interval=2.0,
                rms_threshold=1e-3
            )
            
            assert custom_config.input_sample_rate == 24000
            assert custom_config.health_check_interval == 2.0
            assert custom_config.rms_threshold == 1e-3
            
            logger.info("✅ Кастомная конфигурация создана корректно")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания конфигурации: {e}")
            return False
    
    async def test_config_loading(self) -> bool:
        """Тест загрузки конфигурации из unified_config.yaml"""
        try:
            from modules.default_audio_manager.config.default_config import DefaultAudioConfigLoader
            from config.unified_config_loader import UnifiedConfigLoader
            
            # Загрузка конфигурации
            unified_config = UnifiedConfigLoader()
            default_audio_config = unified_config.get_default_audio_config()
            
            logger.info(f"✅ Конфигурация загружена из unified_config.yaml: {len(default_audio_config)} параметров")
            
            # Создание конфигурации через loader
            config = DefaultAudioConfigLoader.load_from_unified_config(default_audio_config)
            
            logger.info("✅ DefaultAudioConfig создан через loader")
            
            # Проверка, что конфигурация загружена
            assert config is not None
            assert hasattr(config, 'input_sample_rate')
            assert hasattr(config, 'output_sample_rate')
            
            logger.info(f"📊 Загруженные параметры: input_rate={config.input_sample_rate}, output_rate={config.output_sample_rate}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки конфигурации: {e}")
            return False
    
    async def test_manager_creation(self) -> bool:
        """Тест создания DefaultAudioManager"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание конфигурации
            config = DefaultAudioConfig()
            
            # Создание менеджера
            manager = DefaultAudioManager(config)
            
            logger.info("✅ DefaultAudioManager создан успешно")
            
            # Проверка состояния
            state = manager.get_current_state()
            logger.info(f"📊 Начальное состояние: {state.value}")
            
            # Проверка health checker
            health_checker = manager.health_checker
            assert health_checker is not None
            logger.info("✅ HealthChecker создан")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка создания менеджера: {e}")
            return False
    
    async def test_manager_startup(self) -> bool:
        """Тест запуска DefaultAudioManager"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание и запуск менеджера
            config = DefaultAudioConfig()
            manager = DefaultAudioManager(config)
            
            # Запуск
            start_result = await manager.start()
            
            if start_result:
                logger.info("✅ DefaultAudioManager запущен успешно")
                
                # Проверяем состояние
                state = manager.get_current_state()
                logger.info(f"📊 Состояние после запуска: {state.value}")
                
                # Останавливаем
                await manager.stop()
                return True
            else:
                logger.error("❌ Ошибка запуска DefaultAudioManager")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка запуска менеджера: {e}")
            return False
    
    async def test_audio_streams(self) -> Dict[str, Any]:
        """Тест аудио потоков"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание и запуск менеджера
            config = DefaultAudioConfig()
            manager = DefaultAudioManager(config)
            
            await manager.start()
            
            # Проверяем потоки
            input_stream = manager.input_stream
            output_stream = manager.output_stream
            
            logger.info(f"📊 Input stream: {'✅' if input_stream else '❌'}")
            logger.info(f"📊 Output stream: {'✅' if output_stream else '❌'}")
            
            # Получаем аудио данные
            audio_data = manager.get_audio_data(max_samples=1000)
            logger.info(f"🎵 Получено аудио данных: {len(audio_data)} сэмплов")
            
            # Ждем немного для сбора данных
            await asyncio.sleep(2)
            
            # Получаем обновленные данные
            updated_audio_data = manager.get_audio_data(max_samples=1000)
            logger.info(f"🎵 Обновленные аудио данные: {len(updated_audio_data)} сэмплов")
            
            # Останавливаем
            await manager.stop()
            
            return {
                "status": "SUCCESS",
                "input_stream_active": input_stream is not None,
                "output_stream_active": output_stream is not None,
                "initial_audio_samples": len(audio_data),
                "updated_audio_samples": len(updated_audio_data)
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования аудио потоков: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_health_checker(self) -> Dict[str, Any]:
        """Тест HealthChecker"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание и запуск менеджера
            config = DefaultAudioConfig()
            manager = DefaultAudioManager(config)
            
            await manager.start()
            
            # Тестируем health checker
            health_checker = manager.health_checker
            
            # Проверяем здоровье несколько раз
            health_results = []
            for i in range(3):
                health_status, metrics = health_checker.check_health()
                
                health_results.append({
                    "check": i + 1,
                    "status": health_status.value,
                    "rms": metrics.rms_value,
                    "peak": metrics.peak_value,
                    "samples": metrics.sample_count
                })
                
                logger.info(f"🔍 Health check {i+1}: {health_status.value} (RMS: {metrics.rms_value:.6f})")
                await asyncio.sleep(1)
            
            # Тестируем quick check
            is_healthy = health_checker.quick_check()
            logger.info(f"⚡ Quick check: {is_healthy}")
            
            # Получаем последний статус
            last_status = health_checker.get_last_status()
            last_metrics = health_checker.get_last_metrics()
            
            logger.info(f"📊 Последний статус: {last_status.value}")
            logger.info(f"📊 Последние метрики: RMS={last_metrics.rms_value:.6f}")
            
            # Останавливаем
            await manager.stop()
            
            return {
                "status": "SUCCESS",
                "health_checks": health_results,
                "quick_check": is_healthy,
                "last_status": last_status.value,
                "last_rms": last_metrics.rms_value
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования HealthChecker: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_audio_metrics(self) -> Dict[str, Any]:
        """Тест метрик аудио"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание и запуск менеджера
            config = DefaultAudioConfig()
            manager = DefaultAudioManager(config)
            
            await manager.start()
            
            # Ждем для сбора данных
            await asyncio.sleep(2)
            
            # Получаем метрики
            metrics = manager.get_metrics()
            
            logger.info(f"📊 Метрики аудио:")
            logger.info(f"   RMS: {metrics.rms_value:.6f}")
            logger.info(f"   Peak: {metrics.peak_value:.6f}")
            logger.info(f"   Samples: {metrics.sample_count}")
            logger.info(f"   Errors: {metrics.error_count}")
            logger.info(f"   Last health check: {metrics.last_health_check}")
            logger.info(f"   Stream uptime: {metrics.stream_uptime}")
            
            # Проверяем, что метрики обновляются
            await asyncio.sleep(1)
            updated_metrics = manager.get_metrics()
            
            logger.info(f"📊 Обновленные метрики:")
            logger.info(f"   RMS: {updated_metrics.rms_value:.6f}")
            logger.info(f"   Peak: {updated_metrics.peak_value:.6f}")
            
            # Останавливаем
            await manager.stop()
            
            return {
                "status": "SUCCESS",
                "initial_metrics": {
                    "rms": metrics.rms_value,
                    "peak": metrics.peak_value,
                    "samples": metrics.sample_count,
                    "errors": metrics.error_count
                },
                "updated_metrics": {
                    "rms": updated_metrics.rms_value,
                    "peak": updated_metrics.peak_value
                }
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования метрик: {e}")
            return {"status": "ERROR", "error": str(e)}
    
    async def test_error_handling(self) -> bool:
        """Тест обработки ошибок"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание конфигурации с обработкой ошибок
            config = DefaultAudioConfig(
                auto_reopen_on_error=True,
                max_retry_attempts=2,
                retry_delay=0.5,
                error_cooldown=1.0
            )
            
            # Создание менеджера
            manager = DefaultAudioManager(config)
            
            # Запуск
            await manager.start()
            
            # Проверяем, что менеджер работает
            state = manager.get_current_state()
            logger.info(f"📊 Состояние после запуска: {state.value}")
            
            # Проверяем обработку ошибок
            is_healthy = manager.is_healthy()
            logger.info(f"🏥 Здоровье: {is_healthy}")
            
            # Останавливаем
            await manager.stop()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования обработки ошибок: {e}")
            return False
    
    async def test_stream_reopening(self) -> bool:
        """Тест переоткрытия потоков"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание конфигурации с авто-переоткрытием
            config = DefaultAudioConfig(
                auto_reopen_on_error=True,
                max_retry_attempts=3,
                retry_delay=0.2,
                error_cooldown=0.5
            )
            
            # Создание менеджера
            manager = DefaultAudioManager(config)
            
            # Запуск
            await manager.start()
            
            # Проверяем начальное состояние
            initial_state = manager.get_current_state()
            logger.info(f"📊 Начальное состояние: {initial_state.value}")
            
            # Ждем немного
            await asyncio.sleep(2)
            
            # Проверяем состояние после работы
            final_state = manager.get_current_state()
            logger.info(f"📊 Финальное состояние: {final_state.value}")
            
            # Останавливаем
            await manager.stop()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования переоткрытия потоков: {e}")
            return False
    
    async def test_manager_shutdown(self) -> bool:
        """Тест остановки DefaultAudioManager"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание и запуск менеджера
            config = DefaultAudioConfig()
            manager = DefaultAudioManager(config)
            
            await manager.start()
            
            # Проверяем, что менеджер запущен
            state = manager.get_current_state()
            logger.info(f"📊 Состояние до остановки: {state.value}")
            
            # Останавливаем
            stop_result = await manager.stop()
            
            if stop_result:
                # Проверяем состояние после остановки
                final_state = manager.get_current_state()
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
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание конфигурации
            config = DefaultAudioConfig()
            
            # Используем context manager
            async with DefaultAudioManager(config) as manager:
                logger.info("✅ Context manager: менеджер запущен")
                
                # Проверяем функциональность
                state = manager.get_current_state()
                is_healthy = manager.is_healthy()
                metrics = manager.get_metrics()
                
                logger.info(f"📊 Состояние: {state.value}")
                logger.info(f"🏥 Здоровье: {is_healthy}")
                logger.info(f"📊 Метрики: RMS={metrics.rms_value:.6f}")
                
                # Ждем немного
                await asyncio.sleep(1)
            
            logger.info("✅ Context manager: менеджер остановлен")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка context manager: {e}")
            return False
    
    async def test_performance(self) -> Dict[str, Any]:
        """Тест производительности"""
        try:
            from modules.default_audio_manager import DefaultAudioManager, DefaultAudioConfig
            
            # Создание конфигурации
            config = DefaultAudioConfig()
            
            # Измеряем время создания
            start_time = time.time()
            manager = DefaultAudioManager(config)
            creation_time = time.time() - start_time
            logger.info(f"⏱️ Время создания: {creation_time:.3f}s")
            
            # Измеряем время запуска
            start_time = time.time()
            await manager.start()
            startup_time = time.time() - start_time
            logger.info(f"⏱️ Время запуска: {startup_time:.3f}s")
            
            # Измеряем время работы
            start_time = time.time()
            await asyncio.sleep(2)
            work_time = time.time() - start_time
            logger.info(f"⏱️ Время работы: {work_time:.3f}s")
            
            # Измеряем время остановки
            start_time = time.time()
            await manager.stop()
            shutdown_time = time.time() - start_time
            logger.info(f"⏱️ Время остановки: {shutdown_time:.3f}s")
            
            return {
                "status": "SUCCESS",
                "creation_time": creation_time,
                "startup_time": startup_time,
                "work_time": work_time,
                "shutdown_time": shutdown_time,
                "total_time": creation_time + startup_time + work_time + shutdown_time
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
    diagnostic = DiagnosticDefaultAudioManager()
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
