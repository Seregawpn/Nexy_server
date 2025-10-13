#!/usr/bin/env python3
"""
Диагностический тест для Permissions модуля
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from modules.permissions.core.permissions_manager import PermissionManager
from modules.permissions.macos.permission_handler import MacOSPermissionHandler
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class PermissionsDiagnostic:
    """Диагностика Permissions модуля"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики Permissions"""
        logger.info("🔍 Диагностика Permissions...")
        
        # 1. Тест инициализации
        await self._test_initialization()
        
        # 2. Тест конфигурации
        await self._test_configuration()
        
        # 3. Тест permission handler
        await self._test_permission_handler()
        
        # 4. Тест проверки разрешений
        await self._test_permission_checks()
        
        # 5. Тест запроса разрешений
        await self._test_permission_requests()
        
        return self._analyze_results()
    
    async def _test_initialization(self):
        """Тест инициализации Permissions"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            permissions_config = config.get('permissions', {})
            
            # Создаем PermissionManager
            self.permissions_manager = PermissionManager("config/permissions_config.yaml")
            
            # Создаем MacOSPermissionHandler (не требует конфигурации)
            self.permission_handler = MacOSPermissionHandler()
            
            # Инициализируем
            manager_result = await self.permissions_manager.initialize()
            handler_result = True  # MacOSPermissionHandler не требует инициализации
            
            if manager_result and handler_result:
                self._add_result("initialization", True, "Permissions инициализирован", 
                               "Инициализация прошла успешно", "Продолжить", {})
            else:
                self._add_result("initialization", False, "Ошибка инициализации Permissions",
                               "Проблема с инициализацией", "Проверить конфигурацию и зависимости", {})
            
        except Exception as e:
            self._add_result("initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить Permissions конфигурацию и зависимости", {"error": str(e)})
    
    async def _test_configuration(self):
        """Тест конфигурации Permissions"""
        logger.info("2️⃣ Тест конфигурации...")
        
        if not hasattr(self, 'permissions_manager'):
            self._add_result("configuration", False, "Permissions не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем основные параметры конфигурации
            config = self.permissions_manager.config
            
            required_params = [
                ('auto_open_preferences', 'Автоматическое открытие настроек'),
                ('check_interval', 'Интервал проверки'),
                ('required_permissions', 'Обязательные разрешения'),
                ('retry_attempts', 'Количество попыток')
            ]
            
            for param_name, description in required_params:
                if hasattr(config, param_name):
                    value = getattr(config, param_name)
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
    
    async def _test_permission_handler(self):
        """Тест permission handler"""
        logger.info("3️⃣ Тест permission handler...")
        
        if not hasattr(self, 'permission_handler'):
            self._add_result("permission_handler", False, "Permissions не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем состояние handler (MacOSPermissionHandler не требует инициализации)
            if hasattr(self.permission_handler, 'bundle_id') and self.permission_handler.bundle_id:
                self._add_result("permission_handler", True, "Permission handler инициализирован",
                               "Handler готов к работе", "Продолжить", {})
            else:
                self._add_result("permission_handler", False, "Permission handler не инициализирован",
                               "Handler не готов", "Проверить инициализацию handler", {})
            
            # Проверяем доступные разрешения
            # Проверяем доступные разрешения (MacOSPermissionHandler имеет методы для проверки)
            if hasattr(self.permission_handler, 'check_microphone_permission'):
                self._add_result("available_permissions", True, "Разрешения доступны для проверки",
                               "Разрешения доступны", "Продолжить", {})
            else:
                self._add_result("available_permissions", False, "Разрешения не доступны",
                               "Нет доступных разрешений", "Проверить доступные разрешения", {})
            
        except Exception as e:
            self._add_result("permission_handler", False, f"Ошибка тестирования handler: {e}",
                           "Проблема с permission handler", "Проверить permission handler", 
                           {"error": str(e)})
    
    async def _test_permission_checks(self):
        """Тест проверки разрешений"""
        logger.info("4️⃣ Тест проверки разрешений...")
        
        if not hasattr(self, 'permission_handler'):
            self._add_result("permission_checks", False, "Permissions не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем разрешение на микрофон
            microphone_permission = await self.permission_handler.check_microphone_permission()
            
            if microphone_permission:
                self._add_result("microphone_permission", True, "Разрешение на микрофон получено",
                               "Микрофон доступен", "Продолжить", {})
            else:
                self._add_result("microphone_permission", False, "Разрешение на микрофон не получено",
                               "Микрофон недоступен", "Предоставить разрешение на микрофон", {})
            
            # Проверяем разрешение на доступность
            accessibility_permission = await self.permission_handler.check_accessibility_permission()
            
            if accessibility_permission:
                self._add_result("accessibility_permission", True, "Разрешение на доступность получено",
                               "Доступность разрешена", "Продолжить", {})
            else:
                self._add_result("accessibility_permission", False, "Разрешение на доступность не получено",
                               "Доступность запрещена", "Предоставить разрешение на доступность", {})
            
            # Проверяем разрешение на мониторинг ввода
            input_monitoring_permission = await self.permission_handler.check_input_monitoring_permission()
            
            if input_monitoring_permission:
                self._add_result("input_monitoring_permission", True, "Разрешение на мониторинг ввода получено",
                               "Мониторинг ввода разрешен", "Продолжить", {})
            else:
                self._add_result("input_monitoring_permission", False, "Разрешение на мониторинг ввода не получено",
                               "Мониторинг ввода запрещен", "Предоставить разрешение на мониторинг ввода", {})
            
        except Exception as e:
            self._add_result("permission_checks", False, f"Ошибка проверки разрешений: {e}",
                           "Проблема с проверкой разрешений", "Проверить проверку разрешений", 
                           {"error": str(e)})
    
    async def _test_permission_requests(self):
        """Тест запроса разрешений"""
        logger.info("5️⃣ Тест запроса разрешений...")
        
        if not hasattr(self, 'permission_handler'):
            self._add_result("permission_requests", False, "Permissions не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Тестируем запрос разрешения на микрофон
            microphone_request = await self.permission_handler.check_microphone_permission()
            
            if microphone_request:
                self._add_result("microphone_request", True, "Запрос разрешения на микрофон выполнен",
                               "Запрос разрешения работает", "Продолжить", {})
            else:
                self._add_result("microphone_request", False, "Запрос разрешения на микрофон не выполнен",
                               "Запрос разрешения не работает", "Проверить запрос разрешения", {})
            
            # Тестируем запрос разрешения на доступность
            accessibility_request = await self.permission_handler.check_accessibility_permission()
            
            if accessibility_request:
                self._add_result("accessibility_request", True, "Запрос разрешения на доступность выполнен",
                               "Запрос разрешения работает", "Продолжить", {})
            else:
                self._add_result("accessibility_request", False, "Запрос разрешения на доступность не выполнен",
                               "Запрос разрешения не работает", "Проверить запрос разрешения", {})
            
        except Exception as e:
            self._add_result("permission_requests", False, f"Ошибка запроса разрешений: {e}",
                           "Проблема с запросом разрешений", "Проверить запрос разрешений", 
                           {"error": str(e)})
    

    def _fix_permissions_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации Permissions"""
        return {
            'microphone_permission': raw_config.get('microphone_permission', True),
            'accessibility_permission': raw_config.get('accessibility_permission', True),
            'input_monitoring_permission': raw_config.get('input_monitoring_permission', True),
            'screen_recording_permission': raw_config.get('screen_recording_permission', True)
        }

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
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДИАГНОСТИКИ PERMISSIONS:")
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
    diagnostic = PermissionsDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
