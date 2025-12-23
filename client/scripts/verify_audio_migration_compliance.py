#!/usr/bin/env python3
"""
Комплексная проверка соответствия миграции аудиосистемы всем требованиям.

Проверяет:
1. Соответствие .cursorrules требованиям
2. Соответствие документации требованиям
3. Соответствие конфигурации требованиям
4. Соответствие feature flags требованиям
5. Соответствие метрик требованиям
6. Соответствие правил interaction_matrix требованиям
7. Соответствие ADR и Change Impact требованиям
8. Соответствие структуры файлов требованиям
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any
import yaml

# Цвета для вывода
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

class ComplianceChecker:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
        self.checks_passed = 0
        self.checks_failed = 0
        
    def log_error(self, msg: str):
        self.errors.append(msg)
        self.checks_failed += 1
        print(f"{RED}❌{NC} {msg}")
    
    def log_warning(self, msg: str):
        self.warnings.append(msg)
        print(f"{YELLOW}⚠️{NC} {msg}")
    
    def log_info(self, msg: str):
        self.info.append(msg)
        print(f"{BLUE}ℹ️{NC} {msg}")
    
    def log_success(self, msg: str):
        self.checks_passed += 1
        print(f"{GREEN}✅{NC} {msg}")
    
    def check_file_exists(self, file_path: Path, description: str) -> bool:
        """Проверка существования файла"""
        if file_path.exists():
            self.log_success(f"{description}: {file_path}")
            return True
        else:
            self.log_error(f"{description} отсутствует: {file_path}")
            return False
    
    def check_yaml_valid(self, file_path: Path, description: str) -> bool:
        """Проверка валидности YAML файла"""
        if not file_path.exists():
            self.log_error(f"{description} отсутствует: {file_path}")
            return False
        
        try:
            with open(file_path, 'r') as f:
                yaml.safe_load(f)
            self.log_success(f"{description} валиден: {file_path}")
            return True
        except yaml.YAMLError as e:
            self.log_error(f"{description} содержит ошибки YAML: {e}")
            return False
    
    def check_feature_flags_registered(self) -> bool:
        """Проверка регистрации feature flags в FEATURE_FLAGS.md"""
        flags_file = self.project_root / "Docs" / "FEATURE_FLAGS.md"
        if not flags_file.exists():
            self.log_error("FEATURE_FLAGS.md отсутствует")
            return False
        
        content = flags_file.read_text()
        
        required_flags = [
            "NEXY_FEATURE_AVFOUNDATION_AUDIO_V2",
            "NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2",
            "NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2",
            "NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2",
            "NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2",
            "NEXY_KS_AVFOUNDATION_OUTPUT_V2",
            "NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2",
        ]
        
        missing_flags = []
        for flag in required_flags:
            if flag not in content:
                missing_flags.append(flag)
        
        if missing_flags:
            self.log_error(f"Feature flags не зарегистрированы: {', '.join(missing_flags)}")
            return False
        
        self.log_success("Все feature flags зарегистрированы в FEATURE_FLAGS.md")
        return True
    
    def check_unified_config_audio_system(self) -> bool:
        """Проверка секции audio_system в unified_config.yaml"""
        config_file = self.project_root / "config" / "unified_config.yaml"
        if not config_file.exists():
            self.log_error("unified_config.yaml отсутствует")
            return False
        
        try:
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
            
            if 'audio_system' not in config:
                self.log_error("Секция audio_system отсутствует в unified_config.yaml")
                return False
            
            audio_system = config['audio_system']
            
            # Проверка обязательных полей
            required_fields = [
                'avfoundation_enabled',
                'avfoundation_input_monitor_enabled',
                'avfoundation_output_enabled',
                'avfoundation_route_manager_enabled',
                'ks_avfoundation_input_monitor',
                'ks_avfoundation_output',
                'ks_avfoundation_route_manager',
            ]
            
            missing_fields = []
            for field in required_fields:
                if field not in audio_system:
                    missing_fields.append(field)
            
            if missing_fields:
                self.log_error(f"Отсутствуют обязательные поля в audio_system: {', '.join(missing_fields)}")
                return False
            
            # Проверка значений по умолчанию (должны быть false)
            default_false_fields = [
                'avfoundation_enabled',
                'avfoundation_input_monitor_enabled',
                'avfoundation_output_enabled',
                'avfoundation_route_manager_enabled',
                'ks_avfoundation_input_monitor',
                'ks_avfoundation_output',
                'ks_avfoundation_route_manager',
            ]
            
            wrong_defaults = []
            for field in default_false_fields:
                if audio_system.get(field) is not False:
                    wrong_defaults.append(f"{field} (ожидается False, получено {audio_system.get(field)})")
            
            if wrong_defaults:
                self.log_warning(f"Неправильные значения по умолчанию: {', '.join(wrong_defaults)}")
            
            # Проверка структуры route_manager
            if 'route_manager' in audio_system:
                route_manager = audio_system['route_manager']
                if 'debounce' in route_manager:
                    debounce = route_manager['debounce']
                    required_transports = ['bluetooth', 'usb', 'built_in']
                    missing_transports = []
                    for transport in required_transports:
                        if transport not in debounce:
                            missing_transports.append(transport)
                    
                    if missing_transports:
                        self.log_error(f"Отсутствуют транспорты в debounce: {', '.join(missing_transports)}")
                        return False
            
            self.log_success("Секция audio_system корректна в unified_config.yaml")
            return True
            
        except Exception as e:
            self.log_error(f"Ошибка проверки unified_config.yaml: {e}")
            return False
    
    def check_interaction_matrix_rules(self) -> bool:
        """Проверка правил RouteManager в interaction_matrix.yaml"""
        matrix_file = self.project_root / "config" / "interaction_matrix.yaml"
        if not matrix_file.exists():
            self.log_error("interaction_matrix.yaml отсутствует")
            return False
        
        try:
            with open(matrix_file, 'r') as f:
                content = f.read()
            
            # Проверка наличия секции с правилами RouteManager
            if "AUDIO ROUTE MANAGER RULES" not in content:
                self.log_error("Секция AUDIO ROUTE MANAGER RULES отсутствует в interaction_matrix.yaml")
                return False
            
            # Проверка обязательных правил
            required_rules = [
                "decide_route_manager_reconcile",
                "first_run",
                "restart_pending",
                "update_in_progress",
            ]
            
            missing_rules = []
            for rule_keyword in required_rules:
                if rule_keyword not in content:
                    missing_rules.append(rule_keyword)
            
            if missing_rules:
                self.log_error(f"Отсутствуют обязательные правила: {', '.join(missing_rules)}")
                return False
            
            # Проверка приоритетов (hard_stop, graceful)
            if "priority: hard_stop" not in content:
                self.log_warning("Не найдены правила с priority: hard_stop")
            
            if "priority: graceful" not in content:
                self.log_warning("Не найдены правила с priority: graceful")
            
            self.log_success("Правила RouteManager присутствуют в interaction_matrix.yaml")
            return True
            
        except Exception as e:
            self.log_error(f"Ошибка проверки interaction_matrix.yaml: {e}")
            return False
    
    def check_metrics_registry(self) -> bool:
        """Проверка метрик RouteManager в registry.md"""
        registry_file = self.project_root / "client" / "metrics" / "registry.md"
        if not registry_file.exists():
            self.log_error("registry.md отсутствует")
            return False
        
        content = registry_file.read_text()
        
        # Проверка наличия секции метрик
        if "Audio Route Manager Metrics" not in content:
            self.log_error("Секция Audio Route Manager Metrics отсутствует в registry.md")
            return False
        
        # Проверка обязательных метрик
        required_metrics = [
            "device_discovery_latency_ms",
            "input_switch_duration_ms",
            "output_recreate_duration_ms",
            "mapping_confidence_distribution",
            "reconcile_duration_ms",
            "route_manager_decision_rate",
        ]
        
        missing_metrics = []
        for metric in required_metrics:
            if metric not in content:
                missing_metrics.append(metric)
        
        if missing_metrics:
            self.log_error(f"Отсутствуют обязательные метрики: {', '.join(missing_metrics)}")
            return False
        
        # Проверка SLO порогов
        if "SLO" not in content or "p95" not in content:
            self.log_warning("SLO пороги не указаны для метрик")
        
        self.log_success("Метрики RouteManager присутствуют в registry.md")
        return True
    
    def check_adr_exists(self) -> bool:
        """Проверка наличия ADR"""
        adr_dir = self.project_root / "Docs" / "ADRs"
        if not adr_dir.exists():
            self.log_error("Директория Docs/ADRs отсутствует")
            return False
        
        # Ищем ADR файлы
        adr_files = list(adr_dir.glob("ADR_*_avfoundation_audio_migration.md"))
        
        if not adr_files:
            self.log_error("ADR для миграции аудиосистемы отсутствует")
            return False
        
        # Проверяем содержимое ADR
        adr_file = adr_files[0]
        content = adr_file.read_text()
        
        required_sections = [
            "Что",
            "Почему",
            "Альтернативы",
            "Решение",
            "Последствия",
            "Дата",
            "Откат",
        ]
        
        missing_sections = []
        for section in required_sections:
            if f"## {section}" not in content and f"### {section}" not in content:
                missing_sections.append(section)
        
        if missing_sections:
            self.log_warning(f"В ADR отсутствуют секции: {', '.join(missing_sections)}")
        
        self.log_success(f"ADR найден: {adr_file.name}")
        return True
    
    def check_change_impact_exists(self) -> bool:
        """Проверка наличия Change Impact Assessment"""
        impact_file = self.project_root / ".impact" / "change_impact_avfoundation_audio.yaml"
        if not impact_file.exists():
            self.log_error("Change Impact Assessment отсутствует")
            return False
        
        try:
            with open(impact_file, 'r') as f:
                impact = yaml.safe_load(f)
            
            # Проверка обязательных секций
            required_sections = [
                'axes_touched',
                'invariants',
                'metrics',
                'rollout',
                'test_strategy',
            ]
            
            missing_sections = []
            for section in required_sections:
                if section not in impact:
                    missing_sections.append(section)
            
            if missing_sections:
                self.log_error(f"В Change Impact отсутствуют секции: {', '.join(missing_sections)}")
                return False
            
            # Проверка rollout секции
            if 'rollout' in impact:
                rollout = impact['rollout']
                if 'flag' not in rollout:
                    self.log_error("В rollout отсутствует flag")
                    return False
                if 'kill_switch' not in rollout:
                    self.log_error("В rollout отсутствует kill_switch")
                    return False
            
            self.log_success("Change Impact Assessment корректен")
            return True
            
        except Exception as e:
            self.log_error(f"Ошибка проверки Change Impact: {e}")
            return False
    
    def check_structure_exists(self) -> bool:
        """Проверка структуры директорий"""
        required_dirs = [
            "modules/voice_recognition/core/avfoundation",
            "modules/voice_recognition/core/avfoundation/adapters",
        ]
        
        all_exist = True
        for dir_path in required_dirs:
            full_path = self.project_root / dir_path
            if not full_path.exists():
                self.log_error(f"Директория отсутствует: {dir_path}")
                all_exist = False
            else:
                self.log_success(f"Директория существует: {dir_path}")
        
        # Проверка __init__.py файлов
        required_init_files = [
            "modules/voice_recognition/core/avfoundation/__init__.py",
            "modules/voice_recognition/core/avfoundation/adapters/__init__.py",
        ]
        
        for init_file in required_init_files:
            full_path = self.project_root / init_file
            if not full_path.exists():
                self.log_error(f"__init__.py отсутствует: {init_file}")
                all_exist = False
            else:
                self.log_success(f"__init__.py существует: {init_file}")
        
        return all_exist
    
    def check_cursorrules_compliance(self) -> bool:
        """Проверка соответствия .cursorrules требованиям"""
        cursorrules_file = self.project_root / ".cursorrules"
        if not cursorrules_file.exists():
            self.log_warning(".cursorrules отсутствует (может быть в родительской директории)")
            return True
        
        content = cursorrules_file.read_text()
        
        # Проверка упоминания feature flags
        if "FEATURE_FLAGS.md" not in content:
            self.log_warning(".cursorrules не упоминает FEATURE_FLAGS.md")
        
        # Проверка упоминания interaction_matrix
        if "interaction_matrix.yaml" not in content:
            self.log_warning(".cursorrules не упоминает interaction_matrix.yaml")
        
        # Проверка упоминания STATE_CATALOG
        if "STATE_CATALOG.md" not in content:
            self.log_warning(".cursorrules не упоминает STATE_CATALOG.md")
        
        self.log_success("Проверка .cursorrules завершена")
        return True
    
    def check_state_catalog_compliance(self) -> bool:
        """Проверка соответствия STATE_CATALOG.md требованиям"""
        state_catalog_file = self.project_root / "Docs" / "STATE_CATALOG.md"
        if not state_catalog_file.exists():
            self.log_warning("STATE_CATALOG.md отсутствует")
            return True
        
        content = state_catalog_file.read_text()
        
        # Проверка упоминания audio осей (если должны быть добавлены)
        # Это предупреждение, так как оси могут быть добавлены позже
        if "audio.input.device" not in content and "audio.output.device" not in content:
            self.log_info("В STATE_CATALOG.md не найдены оси audio.input.device и audio.output.device (могут быть добавлены позже)")
        
        return True
    
    def run_all_checks(self) -> Dict[str, Any]:
        """Запуск всех проверок"""
        print(f"{BLUE}{'='*80}{NC}")
        print(f"{BLUE}Комплексная проверка соответствия миграции аудиосистемы требованиям{NC}")
        print(f"{BLUE}{'='*80}{NC}\n")
        
        results = {
            'feature_flags': self.check_feature_flags_registered(),
            'unified_config': self.check_unified_config_audio_system(),
            'interaction_matrix': self.check_interaction_matrix_rules(),
            'metrics': self.check_metrics_registry(),
            'adr': self.check_adr_exists(),
            'change_impact': self.check_change_impact_exists(),
            'structure': self.check_structure_exists(),
            'cursorrules': self.check_cursorrules_compliance(),
            'state_catalog': self.check_state_catalog_compliance(),
        }
        
        print(f"\n{BLUE}{'='*80}{NC}")
        print(f"{BLUE}Итоги проверки{NC}")
        print(f"{BLUE}{'='*80}{NC}\n")
        
        print(f"{GREEN}✅ Проверок пройдено: {self.checks_passed}{NC}")
        print(f"{RED}❌ Проверок провалено: {self.checks_failed}{NC}")
        print(f"{YELLOW}⚠️ Предупреждений: {len(self.warnings)}{NC}")
        print(f"{BLUE}ℹ️ Информационных сообщений: {len(self.info)}{NC}\n")
        
        if self.errors:
            print(f"{RED}Ошибки:{NC}")
            for error in self.errors:
                print(f"  {RED}❌{NC} {error}")
            print()
        
        if self.warnings:
            print(f"{YELLOW}Предупреждения:{NC}")
            for warning in self.warnings:
                print(f"  {YELLOW}⚠️{NC} {warning}")
            print()
        
        # Расчет готовности
        total_checks = self.checks_passed + self.checks_failed
        if total_checks > 0:
            readiness = (self.checks_passed / total_checks) * 100
            print(f"{BLUE}Готовность: {readiness:.1f}%{NC}\n")
        
        return {
            'results': results,
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info,
            'checks_passed': self.checks_passed,
            'checks_failed': self.checks_failed,
            'readiness': (self.checks_passed / total_checks * 100) if total_checks > 0 else 0,
        }

def main():
    project_root = Path(__file__).parent.parent
    checker = ComplianceChecker(project_root)
    results = checker.run_all_checks()
    
    # Exit code: 0 если все проверки пройдены, 1 если есть ошибки
    exit_code = 0 if checker.checks_failed == 0 else 1
    
    # Сохраняем результаты в JSON
    output_file = project_root / "audio_migration_compliance_report.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{BLUE}Отчет сохранен в: {output_file}{NC}\n")
    
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

