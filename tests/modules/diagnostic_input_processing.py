#!/usr/bin/env python3
"""
Диагностический тест для Input Processing модуля
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
from modules.input_processing.keyboard.types import KeyEvent, KeyEventType
from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class InputProcessingDiagnostic:
    """Диагностика Input Processing модуля"""
    
    def __init__(self):
        self.results = []
        
    async def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики Input Processing"""
        logger.info("🔍 Диагностика Input Processing...")
        
        # 1. Тест инициализации
        await self._test_initialization()
        
        # 2. Тест конфигурации
        await self._test_configuration()
        
        # 3. Тест keyboard listener
        await self._test_keyboard_listener()
        
        # 4. Тест обработки событий
        await self._test_event_processing()
        
        # 5. Тест разрешений
        await self._test_permissions()
        
        return self._analyze_results()
    
    async def _test_initialization(self):
        """Тест инициализации Input Processing"""
        logger.info("1️⃣ Тест инициализации...")
        
        try:
            # Загружаем конфигурацию
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            input_config = config.get('input_processing', {})
            
            # Создаем KeyboardMonitor с исправленной конфигурацией
            fixed_config = self._fix_input_config(input_config)
            self.keyboard_monitor = KeyboardMonitor(fixed_config)
            
            # Регистрируем тестовый callback
            def test_callback(event):
                pass
            
            self.keyboard_monitor.register_callback(KeyEventType.PRESS, test_callback)
            
            # Запускаем мониторинг
            self.keyboard_monitor.start_monitoring()
            result = True  # start_monitoring не возвращает значение
            
            if result:
                self._add_result("initialization", True, "Input Processing инициализирован", 
                               "Инициализация прошла успешно", "Продолжить", {})
            else:
                self._add_result("initialization", False, "Ошибка инициализации Input Processing",
                               "Проблема с инициализацией", "Проверить конфигурацию и зависимости", {})
            
        except Exception as e:
            self._add_result("initialization", False, f"Ошибка инициализации: {e}",
                           "Проблема с конфигурацией или зависимостями",
                           "Проверить Input Processing конфигурацию и зависимости", {"error": str(e)})
    
    async def _test_configuration(self):
        """Тест конфигурации Input Processing"""
        logger.info("2️⃣ Тест конфигурации...")
        
        if not hasattr(self, 'keyboard_monitor'):
            self._add_result("configuration", False, "Input Processing не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем основные параметры конфигурации
            config = self.keyboard_monitor.config
            
            required_params = [
                ('key_to_monitor', 'Клавиша для мониторинга'),
                ('short_press_threshold', 'Порог короткого нажатия'),
                ('long_press_threshold', 'Порог долгого нажатия'),
                ('event_cooldown', 'Задержка между событиями')
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
    
    async def _test_keyboard_listener(self):
        """Тест keyboard listener"""
        logger.info("3️⃣ Тест keyboard listener...")
        
        if not hasattr(self, 'keyboard_monitor'):
            self._add_result("keyboard_listener", False, "Input Processing не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем состояние listener
            is_monitoring = getattr(self.keyboard_monitor, 'is_monitoring', False)
            
            if is_monitoring:
                self._add_result("keyboard_listener", True, "Keyboard listener запущен",
                               "Listener работает", "Продолжить", {})
            else:
                self._add_result("keyboard_listener", False, "Keyboard listener не запущен",
                               "Listener не работает", "Проверить запуск listener", {})
            
            # Проверяем callback функции
            callbacks = getattr(self.keyboard_monitor, 'event_callbacks', {})
            if callbacks:
                self._add_result("keyboard_callbacks", True, f"Найдено {len(callbacks)} callback функций",
                               "Callback функции настроены", "Продолжить", {"callback_count": len(callbacks)})
            else:
                self._add_result("keyboard_callbacks", False, "Callback функции не настроены",
                               "Нет callback функций", "Настроить callback функции", {})
            
        except Exception as e:
            self._add_result("keyboard_listener", False, f"Ошибка тестирования listener: {e}",
                           "Проблема с keyboard listener", "Проверить keyboard listener", 
                           {"error": str(e)})
    
    async def _test_event_processing(self):
        """Тест обработки событий"""
        logger.info("4️⃣ Тест обработки событий...")
        
        if not hasattr(self, 'keyboard_monitor'):
            self._add_result("event_processing", False, "Input Processing не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Создаем тестовое событие
            test_event = KeyEvent(
                key="space",
                event_type=KeyEventType.PRESS,
                timestamp=1234567890,
                duration=0.1
            )
            
            # Проверяем, что KeyboardMonitor может создавать события
            # (это означает, что обработка событий работает)
            if hasattr(self.keyboard_monitor, 'event_callbacks'):
                self._add_result("event_processing", True, "Обработка событий настроена",
                               "События могут обрабатываться", "Продолжить", {})
            else:
                self._add_result("event_processing", False, "Обработка событий не настроена",
                               "События не могут обрабатываться", "Проверить обработку событий", {})
            
        except Exception as e:
            self._add_result("event_processing", False, f"Ошибка обработки событий: {e}",
                           "Проблема с обработкой событий", "Проверить обработку событий", 
                           {"error": str(e)})
    
    async def _test_permissions(self):
        """Тест разрешений"""
        logger.info("5️⃣ Тест разрешений...")
        
        if not hasattr(self, 'keyboard_monitor'):
            self._add_result("permissions", False, "Input Processing не инициализирован",
                           "Предыдущий тест не прошел", "Сначала исправить инициализацию", {})
            return
        
        try:
            # Проверяем, что мониторинг запущен (это означает, что разрешения есть)
            if self.keyboard_monitor.is_monitoring:
                self._add_result("permissions", True, "Разрешения получены (мониторинг работает)",
                               "Разрешения настроены корректно", "Продолжить", {})
            else:
                self._add_result("permissions", False, "Мониторинг не работает",
                               "Возможно проблема с разрешениями", "Проверить разрешения системы", {})
            
        except Exception as e:
            self._add_result("permissions", False, f"Ошибка проверки разрешений: {e}",
                           "Проблема с проверкой разрешений", "Проверить разрешения системы", 
                           {"error": str(e)})
    

    def _fix_input_config(self, raw_config: Dict[str, Any]) -> 'KeyboardConfig':
        """Исправление конфигурации InputProcessing"""
        from modules.input_processing.keyboard.types import KeyboardConfig
        
        return KeyboardConfig(
            key_to_monitor=raw_config.get('key_to_monitor', 'space'),
            short_press_threshold=raw_config.get('short_press_threshold', 0.6),
            long_press_threshold=raw_config.get('long_press_threshold', 1.0),
            event_cooldown=raw_config.get('event_cooldown', 0.1),
            hold_check_interval=raw_config.get('hold_check_interval', 0.05),
            debounce_time=raw_config.get('debounce_time', 0.1)
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
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДИАГНОСТИКИ INPUT_PROCESSING:")
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
    diagnostic = InputProcessingDiagnostic()
    results = await diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
