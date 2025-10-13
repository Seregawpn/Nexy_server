#!/usr/bin/env python3
"""
Специализированный тест для unified_config.yaml
Диагностирует проблемы в конфигурации
"""

import os
import sys
import yaml
import logging
from typing import Dict, Any, List, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from config.unified_config_loader import UnifiedConfigLoader

logger = logging.getLogger(__name__)

class UnifiedConfigDiagnostic:
    """Диагностика unified_config.yaml"""
    
    def __init__(self):
        self.results = []
        self.config_path = os.path.join(os.path.dirname(__file__), '../../config/unified_config.yaml')
        
    def run_diagnostic(self) -> Dict[str, Any]:
        """Запуск диагностики unified_config.yaml"""
        logger.info("🔍 Диагностика unified_config.yaml...")
        
        # 1. Тест существования файла
        self._test_file_existence()
        
        # 2. Тест валидности YAML
        self._test_yaml_validity()
        
        # 3. Тест структуры конфигурации
        self._test_config_structure()
        
        # 4. Тест аудио конфигурации
        self._test_audio_config()
        
        # 5. Тест приоритетов устройств
        self._test_device_priorities()
        
        # 6. Тест загрузки через UnifiedConfigLoader
        self._test_config_loader()
        
        return self._analyze_results()
    
    def _test_file_existence(self):
        """Тест существования файла конфигурации"""
        logger.info("1️⃣ Тест существования файла...")
        
        if os.path.exists(self.config_path):
            self._add_result("file_existence", True, "Файл unified_config.yaml существует",
                           "Файл конфигурации найден", "Продолжить", {"path": self.config_path})
        else:
            self._add_result("file_existence", False, "Файл unified_config.yaml не найден",
                           "Файл конфигурации отсутствует", "Создать unified_config.yaml", 
                           {"path": self.config_path})
    
    def _test_yaml_validity(self):
        """Тест валидности YAML"""
        logger.info("2️⃣ Тест валидности YAML...")
        
        if not os.path.exists(self.config_path):
            self._add_result("yaml_validity", False, "Файл не существует",
                           "Предыдущий тест не прошел", "Сначала создать файл", {})
            return
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                yaml.safe_load(f)
            
            self._add_result("yaml_validity", True, "YAML синтаксис валиден",
                           "Файл корректно парсится", "Продолжить", {})
            
        except yaml.YAMLError as e:
            self._add_result("yaml_validity", False, f"Ошибка YAML синтаксиса: {e}",
                           "Некорректный YAML синтаксис", "Исправить синтаксис YAML", 
                           {"error": str(e)})
        except Exception as e:
            self._add_result("yaml_validity", False, f"Ошибка чтения файла: {e}",
                           "Проблема с чтением файла", "Проверить права доступа", 
                           {"error": str(e)})
    
    def _test_config_structure(self):
        """Тест структуры конфигурации"""
        logger.info("3️⃣ Тест структуры конфигурации...")
        
        if not os.path.exists(self.config_path):
            self._add_result("config_structure", False, "Файл не существует",
                           "Предыдущий тест не прошел", "Сначала создать файл", {})
            return
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            # Проверяем основные секции
            required_sections = ['app', 'audio', 'integrations']
            
            for section in required_sections:
                if section in config:
                    self._add_result(f"section_{section}", True, f"Секция {section} присутствует",
                                   "Секция конфигурации найдена", "Продолжить", {"section": section})
                else:
                    self._add_result(f"section_{section}", False, f"Секция {section} отсутствует",
                                   "Обязательная секция отсутствует", f"Добавить секцию {section}", 
                                   {"section": section})
            
        except Exception as e:
            self._add_result("config_structure", False, f"Ошибка проверки структуры: {e}",
                           "Проблема с анализом структуры", "Проверить формат конфигурации", 
                           {"error": str(e)})
    
    def _test_audio_config(self):
        """Тест аудио конфигурации"""
        logger.info("4️⃣ Тест аудио конфигурации...")
        
        if not os.path.exists(self.config_path):
            self._add_result("audio_config", False, "Файл не существует",
                           "Предыдущий тест не прошел", "Сначала создать файл", {})
            return
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            audio_config = config.get('audio', {})
            
            # Проверяем секцию device_manager
            device_manager = audio_config.get('device_manager', {})
            if device_manager:
                self._add_result("audio_device_manager", True, "Секция audio.device_manager присутствует",
                               "Конфигурация device_manager найдена", "Продолжить", {})
                
                # Проверяем ключевые параметры
                required_params = ['auto_switch_to_best', 'auto_switch_to_headphones', 'device_priorities']
                for param in required_params:
                    if param in device_manager:
                        self._add_result(f"audio_param_{param}", True, f"Параметр {param} присутствует",
                                       "Параметр конфигурации найден", "Продолжить", {"param": param})
                    else:
                        self._add_result(f"audio_param_{param}", False, f"Параметр {param} отсутствует",
                                       "Обязательный параметр отсутствует", f"Добавить параметр {param}", 
                                       {"param": param})
            else:
                self._add_result("audio_device_manager", False, "Секция audio.device_manager отсутствует",
                               "Конфигурация device_manager не найдена", "Добавить секцию device_manager", {})
            
        except Exception as e:
            self._add_result("audio_config", False, f"Ошибка проверки аудио конфигурации: {e}",
                           "Проблема с анализом аудио конфигурации", "Проверить секцию audio", 
                           {"error": str(e)})
    
    def _test_device_priorities(self):
        """Тест приоритетов устройств"""
        logger.info("5️⃣ Тест приоритетов устройств...")
        
        if not os.path.exists(self.config_path):
            self._add_result("device_priorities", False, "Файл не существует",
                           "Предыдущий тест не прошел", "Сначала создать файл", {})
            return
        
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            device_priorities = config.get('audio', {}).get('device_manager', {}).get('device_priorities', {})
            
            if device_priorities:
                self._add_result("device_priorities_exist", True, "Приоритеты устройств настроены",
                               "Конфигурация приоритетов найдена", "Продолжить", {})
                
                # Проверяем ключевые устройства
                expected_devices = ['airpods', 'bluetooth_headphones', 'built_in', 'microphone', 'iphone_microphone']
                for device in expected_devices:
                    if device in device_priorities:
                        priority = device_priorities[device]
                        if isinstance(priority, int) and 1 <= priority <= 20:
                            self._add_result(f"device_priority_{device}", True, 
                                           f"Приоритет {device} настроен корректно ({priority})",
                                           "Приоритет устройства валиден", "Продолжить", 
                                           {"device": device, "priority": priority})
                        else:
                            self._add_result(f"device_priority_{device}", False, 
                                           f"Приоритет {device} некорректен ({priority})",
                                           "Приоритет должен быть числом от 1 до 20", 
                                           f"Исправить приоритет {device}", 
                                           {"device": device, "priority": priority})
                    else:
                        self._add_result(f"device_priority_{device}", False, 
                                       f"Приоритет {device} не настроен",
                                       "Приоритет устройства отсутствует", 
                                       f"Добавить приоритет для {device}", 
                                       {"device": device})
            else:
                self._add_result("device_priorities_exist", False, "Приоритеты устройств не настроены",
                               "Конфигурация приоритетов отсутствует", "Добавить device_priorities", {})
            
        except Exception as e:
            self._add_result("device_priorities", False, f"Ошибка проверки приоритетов: {e}",
                           "Проблема с анализом приоритетов", "Проверить device_priorities", 
                           {"error": str(e)})
    
    def _test_config_loader(self):
        """Тест загрузки через UnifiedConfigLoader"""
        logger.info("6️⃣ Тест загрузки через UnifiedConfigLoader...")
        
        try:
            loader = UnifiedConfigLoader()
            
            # Тестируем загрузку аудио конфигурации
            audio_config = loader.get_audio_config()
            
            if audio_config:
                self._add_result("config_loader_audio", True, "UnifiedConfigLoader загружает аудио конфигурацию",
                               "Загрузка конфигурации работает", "Продолжить", {})
                
                # Проверяем что приоритеты загружены
                if hasattr(audio_config, 'input_device_priorities') and audio_config.input_device_priorities:
                    self._add_result("config_loader_input_priorities", True, 
                                   "input_device_priorities загружены",
                                   "Приоритеты INPUT устройств загружены", "Продолжить", {})
                else:
                    self._add_result("config_loader_input_priorities", False, 
                                   "input_device_priorities не загружены",
                                   "Приоритеты INPUT устройств не загружены", 
                                   "Проверить загрузку приоритетов", {})
                
                if hasattr(audio_config, 'output_device_priorities') and audio_config.output_device_priorities:
                    self._add_result("config_loader_output_priorities", True, 
                                   "output_device_priorities загружены",
                                   "Приоритеты OUTPUT устройств загружены", "Продолжить", {})
                else:
                    self._add_result("config_loader_output_priorities", False, 
                                   "output_device_priorities не загружены",
                                   "Приоритеты OUTPUT устройств не загружены", 
                                   "Проверить загрузку приоритетов", {})
            else:
                self._add_result("config_loader_audio", False, "UnifiedConfigLoader не загружает аудио конфигурацию",
                               "Проблема с загрузкой конфигурации", "Проверить UnifiedConfigLoader", {})
            
        except Exception as e:
            self._add_result("config_loader", False, f"Ошибка UnifiedConfigLoader: {e}",
                           "Проблема с UnifiedConfigLoader", "Проверить UnifiedConfigLoader", 
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
        
        print(f"\n📊 РЕЗУЛЬТАТЫ ДИАГНОСТИКИ UNIFIED_CONFIG:")
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

def main():
    """Основная функция"""
    diagnostic = UnifiedConfigDiagnostic()
    results = diagnostic.run_diagnostic()
    
    # Возвращаем код выхода
    return 1 if results["failed_tests"] > 0 else 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
