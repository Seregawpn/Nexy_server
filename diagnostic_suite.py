#!/usr/bin/env python3
"""
Комплексная диагностическая система для Nexy Client
Автоматически определяет локацию, причину и решение проблем
"""

import asyncio
import logging
import sys
import os
import time
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ProblemSeverity(Enum):
    """Уровни серьезности проблем"""
    CRITICAL = "CRITICAL"      # Система не работает
    HIGH = "HIGH"              # Основная функциональность нарушена
    MEDIUM = "MEDIUM"          # Частичная функциональность
    LOW = "LOW"                # Незначительные проблемы
    INFO = "INFO"              # Информационные сообщения

class ProblemCategory(Enum):
    """Категории проблем"""
    MODULE = "MODULE"          # Проблема в модуле
    INTEGRATION = "INTEGRATION" # Проблема в интеграции
    CONFIG = "CONFIG"          # Проблема в конфигурации
    SYSTEM = "SYSTEM"          # Системная проблема
    NETWORK = "NETWORK"        # Сетевая проблема
    PERMISSIONS = "PERMISSIONS" # Проблемы с разрешениями

@dataclass
class DiagnosticResult:
    """Результат диагностики"""
    test_name: str
    success: bool
    severity: ProblemSeverity
    category: ProblemCategory
    location: str
    problem: str
    cause: str
    solution: str
    details: Dict[str, Any]
    execution_time: float

class DiagnosticSuite:
    """Главный класс диагностической системы"""
    
    def __init__(self):
        self.results: List[DiagnosticResult] = []
        self.start_time = time.time()
        
    async def run_full_diagnostic(self) -> Dict[str, Any]:
        """Запуск полной диагностики системы"""
        logger.info("🔍 Запуск комплексной диагностики Nexy Client...")
        
        # 1. Системная диагностика
        await self._test_system_requirements()
        
        # 2. Конфигурационная диагностика
        await self._test_configuration()
        
        # 3. Модульная диагностика
        await self._test_modules()
        
        # 4. Интеграционная диагностика
        await self._test_integrations()
        
        # 5. Функциональная диагностика
        await self._test_functionality()
        
        # Анализ результатов
        return self._analyze_results()
    
    async def _test_system_requirements(self):
        """Тестирование системных требований"""
        logger.info("1️⃣ Тестирование системных требований...")
        
        # Python версия
        python_version = sys.version_info
        if python_version >= (3, 11):
            self._add_result("python_version", True, ProblemSeverity.INFO, 
                           ProblemCategory.SYSTEM, "Python", 
                           f"Python {python_version.major}.{python_version.minor}.{python_version.micro}",
                           "Версия Python соответствует требованиям", 
                           "Продолжить", {"version": f"{python_version.major}.{python_version.minor}.{python_version.micro}"})
        else:
            self._add_result("python_version", False, ProblemSeverity.CRITICAL,
                           ProblemCategory.SYSTEM, "Python",
                           f"Python {python_version.major}.{python_version.minor}.{python_version.micro}",
                           "Версия Python ниже требуемой (3.11+)",
                           "Обновить Python до версии 3.11 или выше", {"version": f"{python_version.major}.{python_version.minor}.{python_version.micro}"})
        
        # Проверка зависимостей
        await self._test_dependencies()
        
        # Проверка разрешений
        await self._test_permissions()
    
    async def _test_dependencies(self):
        """Тестирование зависимостей"""
        dependencies = [
            ("sounddevice", "Аудио устройства"),
            ("speech_recognition", "Распознавание речи"),
            ("numpy", "Обработка аудио"),
            ("asyncio", "Асинхронное программирование"),
        ]
        
        for dep_name, description in dependencies:
            try:
                __import__(dep_name)
                self._add_result(f"dependency_{dep_name}", True, ProblemSeverity.INFO,
                               ProblemCategory.SYSTEM, f"Зависимость: {dep_name}",
                               f"{description} доступно", "Зависимость установлена",
                               "Продолжить", {"dependency": dep_name})
            except ImportError:
                self._add_result(f"dependency_{dep_name}", False, ProblemSeverity.CRITICAL,
                               ProblemCategory.SYSTEM, f"Зависимость: {dep_name}",
                               f"{description} недоступно", "Зависимость не установлена",
                               f"Установить: pip install {dep_name}", {"dependency": dep_name})
    
    async def _test_permissions(self):
        """Тестирование разрешений"""
        logger.info("🔐 Тестирование разрешений...")
        
        # Проверка разрешений микрофона
        try:
            import sounddevice as sd
            devices = sd.query_devices()
            if devices:
                self._add_result("microphone_permissions", True, ProblemSeverity.INFO,
                               ProblemCategory.PERMISSIONS, "Разрешения микрофона",
                               "Доступ к микрофону есть", "Разрешения настроены",
                               "Продолжить", {"devices_count": len(devices)})
            else:
                self._add_result("microphone_permissions", False, ProblemSeverity.HIGH,
                               ProblemCategory.PERMISSIONS, "Разрешения микрофона",
                               "Нет доступа к микрофону", "Разрешения не предоставлены",
                               "Предоставить разрешения в Системных настройках", {})
        except Exception as e:
            self._add_result("microphone_permissions", False, ProblemSeverity.HIGH,
                           ProblemCategory.PERMISSIONS, "Разрешения микрофона",
                           f"Ошибка проверки разрешений: {e}", "Проблема с доступом к микрофону",
                           "Проверить разрешения в Системных настройках", {"error": str(e)})
    
    async def _test_configuration(self):
        """Тестирование конфигурации"""
        logger.info("2️⃣ Тестирование конфигурации...")
        
        try:
            from config.unified_config_loader import UnifiedConfigLoader
            config_loader = UnifiedConfigLoader()
            config = config_loader._load_config()
            
            # Проверка структуры конфигурации
            required_sections = ['audio', 'integrations', 'app']
            for section in required_sections:
                if section in config:
                    self._add_result(f"config_section_{section}", True, ProblemSeverity.INFO,
                                   ProblemCategory.CONFIG, f"Конфигурация: {section}",
                                   f"Секция {section} найдена", "Конфигурация корректна",
                                   "Продолжить", {"section": section})
                else:
                    self._add_result(f"config_section_{section}", False, ProblemSeverity.HIGH,
                                   ProblemCategory.CONFIG, f"Конфигурация: {section}",
                                   f"Секция {section} отсутствует", "Неполная конфигурация",
                                   f"Добавить секцию {section} в unified_config.yaml", {"section": section})
            
            # Проверка аудио конфигурации
            await self._test_audio_config(config.get('audio', {}))
            
        except Exception as e:
            self._add_result("config_loading", False, ProblemSeverity.CRITICAL,
                           ProblemCategory.CONFIG, "Загрузка конфигурации",
                           f"Ошибка загрузки конфигурации: {e}", "Проблема с файлом конфигурации",
                           "Проверить unified_config.yaml", {"error": str(e)})
    
    async def _test_audio_config(self, audio_config: Dict[str, Any]):
        """Тестирование аудио конфигурации"""
        device_manager_config = audio_config.get('device_manager', {})
        
        # Проверка приоритетов устройств
        device_priorities = device_manager_config.get('device_priorities', {})
        if device_priorities:
            self._add_result("device_priorities", True, ProblemSeverity.INFO,
                           ProblemCategory.CONFIG, "Приоритеты устройств",
                           f"Настроено {len(device_priorities)} приоритетов", "Приоритеты настроены",
                           "Продолжить", {"priorities_count": len(device_priorities)})
        else:
            self._add_result("device_priorities", False, ProblemSeverity.MEDIUM,
                           ProblemCategory.CONFIG, "Приоритеты устройств",
                           "Приоритеты устройств не настроены", "Отсутствует конфигурация приоритетов",
                           "Добавить device_priorities в unified_config.yaml", {})
    
    async def _test_modules(self):
        """Тестирование модулей"""
        logger.info("3️⃣ Тестирование модулей...")
        
        modules_to_test = [
            ("modules.audio_device_manager.core.device_manager", "AudioDeviceManager"),
            ("modules.voice_recognition.core.speech_recognizer", "SpeechRecognizer"),
            ("modules.speech_playback.core.player", "SpeechPlayback"),
        ]
        
        for module_path, module_name in modules_to_test:
            try:
                module = __import__(module_path, fromlist=[''])
                self._add_result(f"module_{module_name.lower()}", True, ProblemSeverity.INFO,
                               ProblemCategory.MODULE, f"Модуль: {module_name}",
                               f"Модуль {module_name} загружен", "Модуль доступен",
                               "Продолжить", {"module": module_name})
            except Exception as e:
                self._add_result(f"module_{module_name.lower()}", False, ProblemSeverity.HIGH,
                               ProblemCategory.MODULE, f"Модуль: {module_name}",
                               f"Ошибка загрузки модуля: {e}", "Проблема с модулем",
                               f"Проверить модуль {module_name}", {"error": str(e), "module": module_name})
    
    async def _test_integrations(self):
        """Тестирование интеграций"""
        logger.info("4️⃣ Тестирование интеграций...")
        
        integrations_to_test = [
            ("integration.integrations.audio_device_integration", "AudioDeviceIntegration"),
            ("integration.integrations.voice_recognition_integration", "VoiceRecognitionIntegration"),
            ("integration.integrations.speech_playback_integration", "SpeechPlaybackIntegration"),
        ]
        
        for integration_path, integration_name in integrations_to_test:
            try:
                integration = __import__(integration_path, fromlist=[''])
                self._add_result(f"integration_{integration_name.lower()}", True, ProblemSeverity.INFO,
                               ProblemCategory.INTEGRATION, f"Интеграция: {integration_name}",
                               f"Интеграция {integration_name} загружена", "Интеграция доступна",
                               "Продолжить", {"integration": integration_name})
            except Exception as e:
                self._add_result(f"integration_{integration_name.lower()}", False, ProblemSeverity.HIGH,
                               ProblemCategory.INTEGRATION, f"Интеграция: {integration_name}",
                               f"Ошибка загрузки интеграции: {e}", "Проблема с интеграцией",
                               f"Проверить интеграцию {integration_name}", {"error": str(e), "integration": integration_name})
    
    async def _test_functionality(self):
        """Тестирование функциональности"""
        logger.info("5️⃣ Тестирование функциональности...")
        
        # Тест инициализации EventBus
        try:
            from integration.core.event_bus import EventBus
            event_bus = EventBus()
            self._add_result("eventbus_init", True, ProblemSeverity.INFO,
                           ProblemCategory.SYSTEM, "EventBus",
                           "EventBus инициализирован", "EventBus работает",
                           "Продолжить", {})
        except Exception as e:
            self._add_result("eventbus_init", False, ProblemSeverity.CRITICAL,
                           ProblemCategory.SYSTEM, "EventBus",
                           f"Ошибка инициализации EventBus: {e}", "Проблема с EventBus",
                           "Проверить EventBus", {"error": str(e)})
    
    def _add_result(self, test_name: str, success: bool, severity: ProblemSeverity,
                   category: ProblemCategory, location: str, problem: str,
                   cause: str, solution: str, details: Dict[str, Any]):
        """Добавление результата диагностики"""
        execution_time = time.time() - self.start_time
        result = DiagnosticResult(
            test_name=test_name,
            success=success,
            severity=severity,
            category=category,
            location=location,
            problem=problem,
            cause=cause,
            solution=solution,
            details=details,
            execution_time=execution_time
        )
        self.results.append(result)
    
    def _analyze_results(self) -> Dict[str, Any]:
        """Анализ результатов диагностики"""
        logger.info("📊 Анализ результатов диагностики...")
        
        # Статистика по результатам
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results if r.success])
        failed_tests = total_tests - successful_tests
        
        # Группировка по категориям
        by_category = {}
        by_severity = {}
        
        for result in self.results:
            # По категориям
            if result.category not in by_category:
                by_category[result.category] = {"total": 0, "failed": 0, "problems": []}
            by_category[result.category]["total"] += 1
            if not result.success:
                by_category[result.category]["failed"] += 1
                by_category[result.category]["problems"].append(result)
            
            # По серьезности
            if result.severity not in by_severity:
                by_severity[result.severity] = {"total": 0, "failed": 0, "problems": []}
            by_severity[result.severity]["total"] += 1
            if not result.success:
                by_severity[result.severity]["failed"] += 1
                by_severity[result.severity]["problems"].append(result)
        
        # Определение основной проблемы
        critical_problems = [r for r in self.results if r.severity == ProblemSeverity.CRITICAL and not r.success]
        high_problems = [r for r in self.results if r.severity == ProblemSeverity.HIGH and not r.success]
        
        # Рекомендации
        recommendations = []
        if critical_problems:
            recommendations.append("🚨 КРИТИЧЕСКИЕ ПРОБЛЕМЫ требуют немедленного решения!")
            for problem in critical_problems:
                recommendations.append(f"   • {problem.location}: {problem.solution}")
        
        if high_problems:
            recommendations.append("⚠️ ВЫСОКИЕ ПРИОРИТЕТЫ требуют внимания:")
            for problem in high_problems:
                recommendations.append(f"   • {problem.location}: {problem.solution}")
        
        # Вывод результатов
        self._print_summary(total_tests, successful_tests, failed_tests, by_category, by_severity, recommendations)
        
        return {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "failed_tests": failed_tests,
            "success_rate": (successful_tests / total_tests * 100) if total_tests > 0 else 0,
            "by_category": by_category,
            "by_severity": by_severity,
            "critical_problems": critical_problems,
            "high_problems": high_problems,
            "recommendations": recommendations,
            "execution_time": time.time() - self.start_time
        }
    
    def _print_summary(self, total_tests: int, successful_tests: int, failed_tests: int,
                      by_category: Dict, by_severity: Dict, recommendations: List[str]):
        """Вывод сводки результатов"""
        print("\n" + "="*80)
        print("🔍 ДИАГНОСТИЧЕСКАЯ СВОДКА NEXY CLIENT")
        print("="*80)
        
        print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
        print(f"   Всего тестов: {total_tests}")
        print(f"   ✅ Успешных: {successful_tests}")
        print(f"   ❌ Неудачных: {failed_tests}")
        print(f"   📈 Успешность: {(successful_tests / total_tests * 100):.1f}%")
        
        print(f"\n📂 ПО КАТЕГОРИЯМ:")
        for category, stats in by_category.items():
            status = "✅" if stats["failed"] == 0 else "❌"
            print(f"   {status} {category.value}: {stats['total'] - stats['failed']}/{stats['total']}")
        
        print(f"\n🚨 ПО СЕРЬЕЗНОСТИ:")
        for severity, stats in by_severity.items():
            if stats["failed"] > 0:
                status = "🚨" if severity == ProblemSeverity.CRITICAL else "⚠️" if severity == ProblemSeverity.HIGH else "ℹ️"
                print(f"   {status} {severity.value}: {stats['failed']} проблем")
        
        if recommendations:
            print(f"\n💡 РЕКОМЕНДАЦИИ:")
            for rec in recommendations:
                print(f"   {rec}")
        
        print("\n" + "="*80)

async def main():
    """Основная функция"""
    diagnostic = DiagnosticSuite()
    results = await diagnostic.run_full_diagnostic()
    
    # Возвращаем код выхода на основе результатов
    if results["critical_problems"]:
        return 1  # Критические проблемы
    elif results["high_problems"]:
        return 2  # Высокие приоритеты
    else:
        return 0  # Все в порядке

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
