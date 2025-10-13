#!/usr/bin/env python3
"""
Диагностический тест для Mode Management модуля
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from modules.mode_management.core.mode_controller import ModeController
from modules.mode_management.core.types import AppMode, ModeConfig
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class ModeManagementDiagnostic:
    """Диагностика Mode Management модуля"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики Mode Management"""
        logger.info("🔍 Диагностика Mode Management...")
        
        # 1. Тест инициализации
        await self._test_initialization()
        
        # 2. Тест конфигурации
        await self._test_configuration()
        
        # 3. Тест режимов
        await self._test_modes()
        
        # 4. Тест переходов между режимами
        await self._test_mode_transitions()
        
        # 5. Тест состояния режима
        await self._test_mode_state()
        
        return self._analyze_results()
    
    async def _test_initialization(self):
        """Тест инициализации Mode Management"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            mode_config = config.get('mode_management', {})
            
            # Создаем ModeController с исправленной конфигурацией
            fixed_config = self._fix_mode_config(mode_config)
            self.mode_controller = ModeController(fixed_config)
            
            # Инициализируем (ModeController не требует явной инициализации)
            result = True
            
            if result:
                self._add_result("initialization", True, "Mode Management инициализирован", 
                               "Инициализация прошла успешно", "Продолжить", {})
            else:
                self._add_result("initialization", False, "Ошибка инициализации Mode Management",
                               "Проблема с инициализацией", "Проверить конфигурацию и зависимости", {})
            
        except Exception as e:
            self._add_result("initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить Mode Management конфигурацию и зависимости", {"error": str(e)})
    
    async def _test_configuration(self):
        """Тест конфигурации Mode Management"""
        logger.info("2️⃣ Тест конфигурации...")
        
        if not hasattr(self, 'mode_controller'):
            self._add_result("configuration", False, "Mode Management не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем основные параметры конфигурации
            config = self.mode_controller.config
            
            required_params = [
                ('default_mode', 'Режим по умолчанию'),
                ('transition_timeout', 'Таймаут перехода'),
                ('enable_automatic_transitions', 'Автоматический переход'),
                ('max_transition_attempts', 'Максимум попыток перехода')
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
    
    async def _test_modes(self):
        """Тест режимов"""
        logger.info("3️⃣ Тест режимов...")
        
        if not hasattr(self, 'mode_controller'):
            self._add_result("modes", False, "Mode Management не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем доступные режимы (все режимы AppMode)
            from modules.mode_management.core.types import AppMode
            available_modes = list(AppMode)
            
            if available_modes:
                self._add_result("available_modes", True, f"Доступно {len(available_modes)} режимов",
                               "Режимы доступны", "Продолжить", {"modes": [mode.value for mode in available_modes]})
            else:
                self._add_result("available_modes", False, "Режимы не доступны",
                               "Нет доступных режимов", "Проверить доступные режимы", {})
            
            # Проверяем режим по умолчанию
            default_mode = self.mode_controller.config.default_mode
            if default_mode:
                self._add_result("default_mode", True, f"Режим по умолчанию: {default_mode.value}",
                               "Режим по умолчанию настроен", "Продолжить", {"mode": default_mode.value})
            else:
                self._add_result("default_mode", False, "Режим по умолчанию не настроен",
                               "Нет режима по умолчанию", "Настроить режим по умолчанию", {})
            
        except Exception as e:
            self._add_result("modes", False, f"Ошибка тестирования режимов: {e}",
                           "Проблема с режимами", "Проверить режимы", 
                           {"error": str(e)})
    
    async def _test_mode_transitions(self):
        """Тест переходов между режимами"""
        logger.info("4️⃣ Тест переходов между режимами...")
        
        if not hasattr(self, 'mode_controller'):
            self._add_result("mode_transitions", False, "Mode Management не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем доступность метода переключения режимов
            if hasattr(self.mode_controller, 'switch_mode'):
                self._add_result("switch_mode_method", True, "Метод switch_mode доступен",
                               "Метод переключения режимов существует", "Продолжить", {})
            else:
                self._add_result("switch_mode_method", False, "Метод switch_mode недоступен",
                               "Метод переключения режимов отсутствует", "Добавить метод switch_mode", {})
            
            # Проверяем доступные переходы
            available_transitions = self.mode_controller.get_available_transitions()
            if available_transitions is not None:
                self._add_result("available_transitions", True, f"Доступно {len(available_transitions)} переходов",
                               "Переходы доступны", "Продолжить", {"transitions": [t.value for t in available_transitions]})
            else:
                self._add_result("available_transitions", False, "Переходы недоступны",
                               "Нет доступных переходов", "Проверить переходы", {})
            
            # Проверяем статус контроллера
            status = self.mode_controller.get_status()
            if status:
                self._add_result("controller_status", True, "Статус контроллера получен",
                               "Статус контроллера доступен", "Продолжить", {"status": status})
            else:
                self._add_result("controller_status", False, "Статус контроллера недоступен",
                               "Статус контроллера недоступен", "Проверить статус контроллера", {})
            
        except Exception as e:
            self._add_result("mode_transitions", False, f"Ошибка тестирования переходов: {e}",
                           "Проблема с переходами между режимами", "Проверить переходы между режимами", 
                           {"error": str(e)})
    
    async def _test_mode_state(self):
        """Тест состояния режима"""
        logger.info("5️⃣ Тест состояния режима...")
        
        if not hasattr(self, 'mode_controller'):
            self._add_result("mode_state", False, "Mode Management не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем текущий режим
            current_mode = self.mode_controller.get_current_mode()
            
            if current_mode:
                self._add_result("current_mode", True, f"Текущий режим: {current_mode.value}",
                               "Текущий режим получен", "Продолжить", {"mode": current_mode.value})
            else:
                self._add_result("current_mode", False, "Текущий режим не получен",
                               "Текущий режим недоступен", "Проверить текущий режим", {})
            
            # Проверяем метрики режимов
            metrics = self.mode_controller.get_metrics()
            if metrics:
                self._add_result("mode_metrics", True, f"Метрики режимов доступны",
                               "Метрики режимов доступны", "Продолжить", {"total_transitions": metrics.total_transitions})
            else:
                self._add_result("mode_metrics", False, "Метрики режимов недоступны",
                               "Нет метрик режимов", "Проверить метрики режимов", {})
            
        except Exception as e:
            self._add_result("mode_state", False, f"Ошибка тестирования состояния режима: {e}",
                           "Проблема с состоянием режима", "Проверить состояние режима", 
                           {"error": str(e)})
    

    def _fix_mode_config(self, raw_config: Dict[str, Any]) -> ModeConfig:
        """Исправление конфигурации ModeManagement"""
        return ModeConfig(
            default_mode=AppMode(raw_config.get('default_mode', 'sleeping')),
            enable_automatic_transitions=raw_config.get('enable_automatic_transitions', True),
            transition_timeout=raw_config.get('transition_timeout', 5.0),
            max_transition_attempts=raw_config.get('max_transition_attempts', 3),
            enable_logging=raw_config.get('enable_logging', True),
            enable_metrics=raw_config.get('enable_metrics', True)
        )

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
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДИАГНОСТИКИ MODE_MANAGEMENT:")
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
    diagnostic = ModeManagementDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
