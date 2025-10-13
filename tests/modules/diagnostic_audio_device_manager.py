#!/usr/bin/env python3
"""
Специализированный тест для AudioDeviceManager
Диагностирует проблемы в модуле управления аудио устройствами
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from modules.audio_device_manager.core.device_manager import AudioDeviceManager
from modules.audio_device_manager.core.types import AudioDeviceManagerConfig, DeviceType
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class AudioDeviceManagerDiagnostic:
    """Диагностика AudioDeviceManager"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики AudioDeviceManager"""
        logger.info("🔍 Диагностика AudioDeviceManager...")
        
        # 1. Тест инициализации
        await self._test_initialization()
        
        # 2. Тест конфигурации
        await self._test_configuration()
        
        # 3. Тест обнаружения устройств
        await self._test_device_discovery()
        
        # 4. Тест приоритетов
        await self._test_device_priorities()
        
        # 5. Тест переключения устройств
        await self._test_device_switching()
        
        return self._analyze_results()
    
    async def _test_initialization(self):
        """Тест инициализации AudioDeviceManager"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            audio_config_dict = config_loader.get_audio_config()
            
            # Создаем объект AudioDeviceManagerConfig
            audio_config = AudioDeviceManagerConfig(
                auto_switch_enabled=audio_config_dict.get('device_manager', {}).get('auto_switch_to_best', True),
                monitoring_interval=audio_config_dict.get('device_manager', {}).get('cache_timeout', 5.0),
                switch_delay=0.1,
                user_preferences={},
                macos_settings={},
                separate_input_output_management=True,
                input_device_priorities=audio_config_dict.get('input_device_priorities', {}),
                output_device_priorities=audio_config_dict.get('output_device_priorities', {})
            )
            
            # Создаем AudioDeviceManager
            manager = AudioDeviceManager(audio_config)
            
            self._add_result("initialization", True, "AudioDeviceManager инициализирован", 
                           "Инициализация прошла успешно", "Продолжить", {})
            
            # Сохраняем для дальнейших тестов
            self.manager = manager
            
        except Exception as e:
            self._add_result("initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить unified_config.yaml и зависимости", {"error": str(e)})
    
    async def _test_configuration(self):
        """Тест конфигурации"""
        logger.info("2️⃣ Тест конфигурации...")
        
        if not hasattr(self, 'manager'):
            self._add_result("configuration", False, "AudioDeviceManager не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            config = self.manager.config
            
            # Проверяем основные параметры
            checks = [
                ("auto_switch_enabled", config.auto_switch_enabled, "Автопереключение устройств"),
                ("monitoring_interval", config.monitoring_interval, "Интервал мониторинга"),
                ("switch_delay", config.switch_delay, "Задержка переключения"),
            ]
            
            for param_name, value, description in checks:
                if value is not None:
                    self._add_result(f"config_{param_name}", True, f"{description}: {value}",
                                   "Параметр настроен", "Продолжить", {"parameter": param_name, "value": value})
                else:
                    self._add_result(f"config_{param_name}", False, f"{description} не настроен",
                                   "Параметр отсутствует", f"Настроить {param_name} в конфигурации", 
                                   {"parameter": param_name})
            
        except Exception as e:
            self._add_result("configuration", False, f"Ошибка проверки конфигурации: {e}",
                           "Проблема с доступом к конфигурации", "Проверить структуру конфигурации", 
                           {"error": str(e)})
    
    async def _test_device_discovery(self):
        """Тест обнаружения устройств"""
        logger.info("3️⃣ Тест обнаружения устройств...")
        
        if not hasattr(self, 'manager'):
            self._add_result("device_discovery", False, "AudioDeviceManager не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Запускаем менеджер
            await self.manager.start()
            
            # Получаем устройства
            input_devices = list(self.manager.input_devices.values())
            output_devices = list(self.manager.output_devices.values())
            
            # Проверяем INPUT устройства
            if input_devices:
                self._add_result("input_devices", True, f"Найдено {len(input_devices)} INPUT устройств",
                               "INPUT устройства обнаружены", "Продолжить", 
                               {"count": len(input_devices), "devices": [d.name for d in input_devices]})
            else:
                self._add_result("input_devices", False, "INPUT устройства не найдены",
                               "Нет доступных микрофонов", "Проверить подключение микрофона", {})
            
            # Проверяем OUTPUT устройства
            if output_devices:
                self._add_result("output_devices", True, f"Найдено {len(output_devices)} OUTPUT устройств",
                               "OUTPUT устройства обнаружены", "Продолжить",
                               {"count": len(output_devices), "devices": [d.name for d in output_devices]})
            else:
                self._add_result("output_devices", False, "OUTPUT устройства не найдены",
                               "Нет доступных динамиков", "Проверить подключение динамиков", {})
            
            # Проверяем portaudio_index
            devices_with_index = [d for d in input_devices + output_devices if d.portaudio_index is not None]
            if devices_with_index:
                self._add_result("portaudio_index", True, f"{len(devices_with_index)} устройств с portaudio_index",
                               "portaudio_index настроен", "Продолжить", {"count": len(devices_with_index)})
            else:
                self._add_result("portaudio_index", False, "portaudio_index не настроен",
                               "Отсутствует маппинг на sounddevice", "Проверить SwitchAudioBridge", {})
            
        except Exception as e:
            self._add_result("device_discovery", False, f"Ошибка обнаружения устройств: {e}",
                           "Проблема с доступом к аудио устройствам", "Проверить разрешения и SwitchAudioSource", 
                           {"error": str(e)})
    
    async def _test_device_priorities(self):
        """Тест приоритетов устройств"""
        logger.info("4️⃣ Тест приоритетов устройств...")
        
        if not hasattr(self, 'manager') or not hasattr(self.manager, 'input_devices'):
            self._add_result("device_priorities", False, "AudioDeviceManager не готов",
                           "Предыдущие тесты не прошли", "Сначала исправить обнаружение устройств", {})
            return
        
        try:
            # Тестируем приоритеты INPUT устройств
            input_devices = self.manager.input_devices
            if input_devices:
                # Получаем лучшее устройство
                best_input = await self.manager.get_best_input_device()
                if best_input:
                    priority = self.manager._get_input_priority(best_input)
                    self._add_result("input_priorities", True, f"Лучшее INPUT: {best_input.name} (приоритет: {priority})",
                                   "Приоритеты INPUT работают", "Продолжить", 
                                   {"device": best_input.name, "priority": priority})
                else:
                    self._add_result("input_priorities", False, "Не удалось определить лучшее INPUT устройство",
                                   "Проблема с логикой приоритетов", "Проверить конфигурацию приоритетов", {})
            
            # Тестируем приоритеты OUTPUT устройств
            output_devices = self.manager.output_devices
            if output_devices:
                best_output = await self.manager.get_best_output_device()
                if best_output:
                    priority = self.manager._get_output_priority(best_output)
                    self._add_result("output_priorities", True, f"Лучшее OUTPUT: {best_output.name} (приоритет: {priority})",
                                   "Приоритеты OUTPUT работают", "Продолжить",
                                   {"device": best_output.name, "priority": priority})
                else:
                    self._add_result("output_priorities", False, "Не удалось определить лучшее OUTPUT устройство",
                                   "Проблема с логикой приоритетов", "Проверить конфигурацию приоритетов", {})
            
        except Exception as e:
            self._add_result("device_priorities", False, f"Ошибка тестирования приоритетов: {e}",
                           "Проблема с логикой приоритетов", "Проверить методы _get_input_priority и _get_output_priority", 
                           {"error": str(e)})
    
    async def _test_device_switching(self):
        """Тест переключения устройств"""
        logger.info("5️⃣ Тест переключения устройств...")
        
        if not hasattr(self, 'manager') or not hasattr(self.manager, 'input_devices'):
            self._add_result("device_switching", False, "AudioDeviceManager не готов",
                           "Предыдущие тесты не прошли", "Сначала исправить обнаружение устройств", {})
            return
        
        try:
            # Тестируем переключение на лучшее INPUT устройство
            input_devices = list(self.manager.input_devices.values())
            if input_devices:
                # Получаем лучшее INPUT устройство
                best_input = await self.manager.get_best_input_device()
                if best_input:
                    result = await self.manager.switch_to_input_device(best_input.id)
                    if result:
                        self._add_result("input_switching", True, "Переключение на лучшее INPUT устройство успешно",
                                       "Переключение INPUT работает", "Продолжить", {})
                    else:
                        self._add_result("input_switching", False, "Не удалось переключиться на лучшее INPUT устройство",
                                       "Проблема с переключением INPUT", "Проверить DeviceSwitcher", {})
                else:
                    self._add_result("input_switching", False, "Не удалось найти лучшее INPUT устройство",
                                   "Проблема с выбором лучшего INPUT устройства", "Проверить логику приоритетов", {})
            
            # Тестируем переключение на лучшее OUTPUT устройство
            output_devices = list(self.manager.output_devices.values())
            if output_devices:
                # Получаем лучшее OUTPUT устройство
                best_output = await self.manager.get_best_output_device()
                if best_output:
                    result = await self.manager.switch_to_output_device(best_output.id)
                    if result:
                        self._add_result("output_switching", True, "Переключение на лучшее OUTPUT устройство успешно",
                                       "Переключение OUTPUT работает", "Продолжить", {})
                    else:
                        self._add_result("output_switching", False, "Не удалось переключиться на лучшее OUTPUT устройство",
                                       "Проблема с переключением OUTPUT", "Проверить DeviceSwitcher", {})
                else:
                    self._add_result("output_switching", False, "Не удалось найти лучшее OUTPUT устройство",
                                   "Проблема с выбором лучшего OUTPUT устройства", "Проверить логику приоритетов", {})
            
        except Exception as e:
            self._add_result("device_switching", False, f"Ошибка тестирования переключения: {e}",
                           "Проблема с переключением устройств", "Проверить DeviceSwitcher и SwitchAudioBridge", 
                           {"error": str(e)})
        
        finally:
            # Останавливаем менеджер
            if hasattr(self, 'manager'):
                await self.manager.stop()
    
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
        """Анализ результатов с детальной диагностикой"""
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results if r["success"]])
        failed_tests = total_tests - successful_tests
        
        print(f"\n{'='*80}")
        print(f"📊 ДЕТАЛЬНАЯ ДИАГНОСТИКА AUDIODEVICEMANAGER")
        print(f"{'='*80}")
        print(f"📈 ОБЩАЯ СТАТИСТИКА:")
        print(f"   Всего тестов: {total_tests}")
        print(f"   ✅ Успешных: {successful_tests}")
        print(f"   ❌ Неудачных: {failed_tests}")
        print(f"   📊 Успешность: {(successful_tests / total_tests * 100):.1f}%")
        
        print(f"\n🔍 ДЕТАЛЬНЫЕ РЕЗУЛЬТАТЫ:")
        print(f"{'-'*80}")
        
        # Группируем результаты по категориям
        categories = {
            "Инициализация": [],
            "Конфигурация": [],
            "Обнаружение устройств": [],
            "Приоритеты": [],
            "Переключение": []
        }
        
        for result in self.results:
            test_name = result['test']
            if 'initialization' in test_name:
                categories["Инициализация"].append(result)
            elif 'config' in test_name:
                categories["Конфигурация"].append(result)
            elif 'device_discovery' in test_name or 'devices' in test_name:
                categories["Обнаружение устройств"].append(result)
            elif 'priorities' in test_name or 'best' in test_name:
                categories["Приоритеты"].append(result)
            elif 'switching' in test_name or 'switch' in test_name:
                categories["Переключение"].append(result)
            else:
                categories["Инициализация"].append(result)
        
        # Выводим результаты по категориям
        for category, tests in categories.items():
            if tests:
                print(f"\n📂 {category.upper()}:")
                for result in tests:
                    status = "✅" if result["success"] else "❌"
                    print(f"   {status} {result['test']}: {result['problem']}")
                    
                    # Показываем детали для успешных тестов
                    if result["success"] and result.get("details"):
                        details = result["details"]
                        for key, value in details.items():
                            if isinstance(value, (int, float, str)):
                                print(f"      📊 {key}: {value}")
                            elif isinstance(value, list) and len(value) <= 5:
                                print(f"      📋 {key}: {', '.join(map(str, value))}")
                            elif isinstance(value, dict):
                                print(f"      📋 {key}: {len(value)} элементов")
        
        # Показываем проблемы
        if failed_tests > 0:
            print(f"\n❌ ОБНАРУЖЕННЫЕ ПРОБЛЕМЫ:")
            print(f"{'-'*80}")
            for result in self.results:
                if not result["success"]:
                    print(f"   🔴 {result['test']}: {result['problem']}")
                    print(f"      💡 Причина: {result['cause']}")
                    print(f"      🛠️  Решение: {result['solution']}")
                    if result.get("details", {}).get("error"):
                        print(f"      🐛 Ошибка: {result['details']['error']}")
        
        # Показываем рекомендации
        print(f"\n💡 РЕКОМЕНДАЦИИ:")
        print(f"{'-'*80}")
        if successful_tests == total_tests:
            print("   🎉 Все тесты прошли успешно! AudioDeviceManager готов к работе.")
            print("   🚀 Система может корректно управлять аудио устройствами.")
        else:
            print(f"   ⚠️  Обнаружено {failed_tests} проблем, требующих внимания.")
            print("   🔧 Рекомендуется исправить проблемы перед использованием.")
        
        print(f"\n{'='*80}")
        
        return {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": failed_tests,
            "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0,
            "results": self.results,
            "categories": categories
        }

async def main():
    """Основная функция"""
    diagnostic = AudioDeviceManagerDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
