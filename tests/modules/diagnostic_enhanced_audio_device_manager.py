#!/usr/bin/env python3
"""
Улучшенный диагностический тест для AudioDeviceManager с исправлениями
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from modules.audio_device_manager.core.device_manager import AudioDeviceManager
from modules.audio_device_manager.core.types import AudioDeviceManagerConfig
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class EnhancedAudioDeviceManagerDiagnostic:
    """Улучшенная диагностика AudioDeviceManager с исправлениями"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск улучшенной диагностики AudioDeviceManager"""
        logger.info("🔍 Улучшенная диагностика AudioDeviceManager...")
        
        # 1. Тест инициализации с исправлениями
        await self._test_enhanced_initialization()
        
        # 2. Тест конфигурации с валидацией
        await self._test_enhanced_configuration()
        
        # 3. Тест обнаружения устройств
        await self._test_device_discovery()
        
        # 4. Тест приоритетов устройств
        await self._test_device_priorities()
        
        # 5. Тест переключения устройств
        await self._test_device_switching()
        
        # 6. Тест мониторинга устройств
        await self._test_device_monitoring()
        
        return self._analyze_results()
    
    async def _test_enhanced_initialization(self):
        """Улучшенный тест инициализации с исправлениями"""
        logger.info("1️⃣ Улучшенный тест инициализации...")
        
        try:
            # Загружаем конфигурацию с исправлениями
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            audio_config = config.get('audio_device_manager', {})
            
            # Создаем конфигурационный объект с исправлениями
            if isinstance(audio_config, dict):
                # Применяем исправления конфигурации
                fixed_config = self._fix_audio_config(audio_config)
                self.manager_config = AudioDeviceManagerConfig(**fixed_config)
            else:
                self.manager_config = audio_config
            
            # Создаем AudioDeviceManager с исправленной конфигурацией
            self.manager = AudioDeviceManager(self.manager_config)
            
            # Запускаем менеджер (вместо initialize)
            result = await self.manager.start()
            
            if result:
                self._add_result("enhanced_initialization", True, "AudioDeviceManager инициализирован с исправлениями", 
                               "Инициализация прошла успешно", "Продолжить", {})
            else:
                self._add_result("enhanced_initialization", False, "Ошибка инициализации AudioDeviceManager",
                               "Проблема с инициализацией", "Проверить конфигурацию и зависимости", {})
            
        except Exception as e:
            self._add_result("enhanced_initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить AudioDeviceManager конфигурацию и зависимости", {"error": str(e)})
    
    def _fix_audio_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации AudioDeviceManager"""
        # Применяем исправления конфигурации согласно реальной структуре AudioDeviceManagerConfig
        fixed_config = {
            'auto_switch_enabled': raw_config.get('auto_switch_enabled', True),
            'monitoring_interval': raw_config.get('monitoring_interval', 1.0),
            'switch_delay': raw_config.get('switch_delay', 0.5),
            'separate_input_output_management': raw_config.get('separate_input_output_management', True),
            'input_device_priorities': raw_config.get('input_device_priorities', {}),
            'output_device_priorities': raw_config.get('output_device_priorities', {}),
            'user_preferences': raw_config.get('user_preferences', {}),
            'macos_settings': raw_config.get('macos_settings', {})
        }
        
        logger.info("🔧 Конфигурация AudioDeviceManager исправлена")
        return fixed_config
    
    async def _test_enhanced_configuration(self):
        """Улучшенный тест конфигурации с валидацией"""
        logger.info("2️⃣ Улучшенный тест конфигурации...")
        
        if not hasattr(self, 'manager_config'):
            self._add_result("enhanced_configuration", False, "AudioDeviceManager не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем исправленную конфигурацию
            config = self.manager_config
            
            required_params = [
                ('auto_switch_enabled', 'Автоматическое переключение включено'),
                ('monitoring_interval', 'Интервал мониторинга'),
                ('switch_delay', 'Задержка переключения'),
                ('separate_input_output_management', 'Раздельное управление входом/выходом')
            ]
            
            for param_name, description in required_params:
                if hasattr(config, param_name):
                    value = getattr(config, param_name)
                    self._add_result(f"enhanced_config_{param_name}", True, f"{description}: {value}",
                                   "Параметр настроен и исправлен", "Продолжить", {"parameter": param_name, "value": value})
                else:
                    self._add_result(f"enhanced_config_{param_name}", False, f"{description} не настроен",
                                   "Параметр отсутствует", f"Настроить {param_name} в конфигурации", 
                                   {"parameter": param_name})
            
        except Exception as e:
            self._add_result("enhanced_configuration", False, f"Ошибка проверки конфигурации: {e}",
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
            # Менеджер уже запущен в предыдущем тесте
            
            # Проверяем обнаруженные устройства
            input_devices = list(self.manager.input_devices.values())
            output_devices = list(self.manager.output_devices.values())
            
            if input_devices:
                self._add_result("input_devices", True, f"Найдено {len(input_devices)} входных устройств",
                               "Входные устройства обнаружены", "Продолжить", {"count": len(input_devices)})
            else:
                self._add_result("input_devices", False, "Входные устройства не обнаружены",
                               "Нет входных устройств", "Проверить подключение микрофонов", {})
            
            if output_devices:
                self._add_result("output_devices", True, f"Найдено {len(output_devices)} выходных устройств",
                               "Выходные устройства обнаружены", "Продолжить", {"count": len(output_devices)})
            else:
                self._add_result("output_devices", False, "Выходные устройства не обнаружены",
                               "Нет выходных устройств", "Проверить подключение динамиков", {})
            
        except Exception as e:
            self._add_result("device_discovery", False, f"Ошибка обнаружения устройств: {e}",
                           "Проблема с обнаружением устройств", "Проверить аудио драйверы", 
                           {"error": str(e)})
    
    async def _test_device_priorities(self):
        """Тест приоритетов устройств"""
        logger.info("4️⃣ Тест приоритетов устройств...")
        
        if not hasattr(self, 'manager'):
            self._add_result("device_priorities", False, "AudioDeviceManager не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем лучшее входное устройство
            best_input = await self.manager.get_best_input_device()
            if best_input:
                self._add_result("best_input_device", True, f"Лучшее входное устройство: {best_input.name}",
                               "Лучшее входное устройство найдено", "Продолжить", {"device": best_input.name})
            else:
                self._add_result("best_input_device", False, "Лучшее входное устройство не найдено",
                               "Нет доступных входных устройств", "Проверить подключение микрофонов", {})
            
            # Проверяем лучшее выходное устройство
            best_output = await self.manager.get_best_output_device()
            if best_output:
                self._add_result("best_output_device", True, f"Лучшее выходное устройство: {best_output.name}",
                               "Лучшее выходное устройство найдено", "Продолжить", {"device": best_output.name})
            else:
                self._add_result("best_output_device", False, "Лучшее выходное устройство не найдено",
                               "Нет доступных выходных устройств", "Проверить подключение динамиков", {})
            
        except Exception as e:
            self._add_result("device_priorities", False, f"Ошибка проверки приоритетов: {e}",
                           "Проблема с приоритетами устройств", "Проверить конфигурацию приоритетов", 
                           {"error": str(e)})
    
    async def _test_device_switching(self):
        """Тест переключения устройств"""
        logger.info("5️⃣ Тест переключения устройств...")
        
        if not hasattr(self, 'manager'):
            self._add_result("device_switching", False, "AudioDeviceManager не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Получаем лучшее входное устройство
            best_input = await self.manager.get_best_input_device()
            if best_input:
                # Переключаемся на лучшее входное устройство
                result = await self.manager.switch_to_input_device(best_input.id)
                if result:
                    self._add_result("input_switching", True, f"Переключение на входное устройство: {best_input.name}",
                                   "Переключение входного устройства работает", "Продолжить", {"device": best_input.name})
                else:
                    self._add_result("input_switching", False, f"Не удалось переключиться на: {best_input.name}",
                                   "Проблема с переключением входного устройства", "Проверить права доступа", {})
            
            # Получаем лучшее выходное устройство
            best_output = await self.manager.get_best_output_device()
            if best_output:
                # Переключаемся на лучшее выходное устройство
                result = await self.manager.switch_to_output_device(best_output.id)
                if result:
                    self._add_result("output_switching", True, f"Переключение на выходное устройство: {best_output.name}",
                                   "Переключение выходного устройства работает", "Продолжить", {"device": best_output.name})
                else:
                    self._add_result("output_switching", False, f"Не удалось переключиться на: {best_output.name}",
                                   "Проблема с переключением выходного устройства", "Проверить права доступа", {})
            
        except Exception as e:
            self._add_result("device_switching", False, f"Ошибка переключения устройств: {e}",
                           "Проблема с переключением устройств", "Проверить права доступа к аудио", 
                           {"error": str(e)})
    
    async def _test_device_monitoring(self):
        """Тест мониторинга устройств"""
        logger.info("6️⃣ Тест мониторинга устройств...")
        
        if not hasattr(self, 'manager'):
            self._add_result("device_monitoring", False, "AudioDeviceManager не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем мониторинг устройств
            monitor = getattr(self.manager, 'device_monitor', None)
            if monitor:
                is_monitoring = getattr(monitor, 'is_monitoring', False)
                if is_monitoring:
                    self._add_result("device_monitoring", True, "Мониторинг устройств активен",
                                   "Мониторинг устройств работает", "Продолжить", {})
                else:
                    self._add_result("device_monitoring", False, "Мониторинг устройств не активен",
                                   "Мониторинг устройств не работает", "Проверить настройки мониторинга", {})
            else:
                self._add_result("device_monitoring", False, "Мониторинг устройств не найден",
                               "Компонент мониторинга отсутствует", "Проверить инициализацию мониторинга", {})
            
        except Exception as e:
            self._add_result("device_monitoring", False, f"Ошибка мониторинга устройств: {e}",
                           "Проблема с мониторингом устройств", "Проверить настройки мониторинга", 
                           {"error": str(e)})
    
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
        
        print(f"\n📊 РЕЗУЛЬТАТЫ УЛУЧШЕННОЙ ДИАГНОСТИКИ AUDIODEVICEMANAGER:")
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
    diagnostic = EnhancedAudioDeviceManagerDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
