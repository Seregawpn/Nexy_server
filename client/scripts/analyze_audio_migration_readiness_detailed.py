#!/usr/bin/env python3
"""
Расширенный диагностический скрипт для детального анализа готовности к миграции аудиосистемы.

Анализирует:
- Все файлы, которые нужно создать/изменить
- Все EventBus события с детальной информацией
- Зависимости PyObjC и их доступность
- Entitlements и разрешения
- Тесты и их покрытие
- CI/CD интеграцию
- Блокировки (first_run, permission_restart, update_in_progress)
- Порядок инициализации с зависимостями
- Конфигурацию с валидацией
- Документацию

БЕЗ фактического внедрения новой системы.
"""

import os
import sys
import json
import re
import ast
import yaml
from pathlib import Path
from typing import Dict, List, Set, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@dataclass
class FileStatus:
    """Статус файла"""
    path: str
    exists: bool
    needs_create: bool
    needs_modify: bool
    lines_of_code: Optional[int] = None
    dependencies: List[str] = None
    tests_exist: bool = False

@dataclass
class EventDetail:
    """Детальная информация о событии EventBus"""
    name: str
    publishers: List[str]
    subscribers: List[str]
    priority: Optional[str] = None
    payload_schema: Optional[Dict[str, Any]] = None
    audio_related: bool = False
    used_by_route_manager: bool = False

@dataclass
class DependencyCheck:
    """Проверка зависимости"""
    name: str
    required: bool
    available: bool
    version: Optional[str] = None
    location: Optional[str] = None

@dataclass
class BlockingCondition:
    """Условие блокировки"""
    name: str
    event: str
    integration: str
    checked: bool = False

@dataclass
class DetailedAnalysisResult:
    """Детальный результат анализа"""
    # Файлы
    files_to_create: List[FileStatus]
    files_to_modify: List[FileStatus]
    files_existing: List[FileStatus]
    
    # События
    events_detailed: List[EventDetail]
    events_missing: List[str]
    
    # Зависимости
    dependencies: List[DependencyCheck]
    
    # Блокировки
    blocking_conditions: List[BlockingCondition]
    
    # Конфигурация
    config_sections: Dict[str, Any]
    config_missing: List[str]
    
    # Тесты
    tests_existing: List[str]
    tests_missing: List[str]
    
    # CI/CD
    ci_integration: Dict[str, bool]
    
    # Порядок инициализации
    init_order: List[str]
    init_order_issues: List[str]
    
    # Готовность
    readiness_score: float
    readiness_breakdown: Dict[str, float]
    recommendations: List[str]
    critical_issues: List[str]
    warnings: List[str]


class DetailedAudioMigrationAnalyzer:
    """Расширенный анализатор готовности к миграции аудиосистемы"""
    
    def __init__(self, project_root: str):
        project_root_path = Path(project_root).resolve()
        
        # Определяем client_root
        if (project_root_path / "client").exists() and (project_root_path / "client" / "integration").exists():
            self.client_root = project_root_path / "client"
            self.project_root = project_root_path
        elif (project_root_path / "integration").exists():
            self.client_root = project_root_path
            current = project_root_path
            while current != current.parent:
                if (current / "Docs").exists():
                    self.project_root = current
                    break
                current = current.parent
            else:
                self.project_root = project_root_path.parent
        else:
            self.client_root = project_root_path
            self.project_root = project_root_path.parent if (project_root_path.parent / "Docs").exists() else project_root_path
        
        # Пути
        self.config_path = self.client_root / "config" / "unified_config.yaml"
        self.feature_flags_path = self.project_root / "Docs" / "FEATURE_FLAGS.md"
        self.migration_plan_path = self.project_root / "Docs" / "AUDIO_MIGRATION_STEP_BY_STEP_PLAN.md"
        self.requirements_path = self.client_root / "requirements.txt"
        self.ci_workflow_path = self.project_root / ".github" / "workflows" / "ci.yml"
        
        # Файлы для создания (из плана миграции)
        self.files_to_create = {
            # Этап 1: Подготовка инфраструктуры
            "modules/voice_recognition/core/avfoundation/__init__.py": "Экспорт основных классов",
            "modules/voice_recognition/core/avfoundation/contracts.py": "Типы данных и контракты",
            "modules/voice_recognition/core/avfoundation/mapping.py": "AVFoundation → PortAudio маппинг",
            "modules/voice_recognition/core/avfoundation/state_machines.py": "InputSM и OutputSM",
            "modules/voice_recognition/core/avfoundation/route_manager.py": "AudioRouteManager (reconcile)",
            "modules/voice_recognition/core/avfoundation/adapters/__init__.py": "Экспорт адаптеров",
            "modules/voice_recognition/core/avfoundation/adapters/avf_monitor.py": "AVFoundationDeviceMonitor",
            "modules/voice_recognition/core/avfoundation/adapters/avf_output.py": "AVFoundationAudioPlayback",
            "modules/voice_recognition/core/avfoundation/adapters/google_input.py": "GoogleInputController",
            
            # Этап 2: Интеграция RouteManager
            "integration/integrations/audio_route_manager_integration.py": "AudioRouteManagerIntegration",
            
            # Тесты
            "tests/test_avfoundation_contracts.py": "Тесты contracts.py",
            "tests/test_avfoundation_mapping.py": "Тесты mapping.py",
            "tests/test_avfoundation_state_machines.py": "Тесты state_machines.py",
            "tests/test_avfoundation_route_manager.py": "Тесты route_manager.py",
            "tests/test_avfoundation_monitor.py": "Тесты avf_monitor.py",
            "tests/test_avfoundation_output.py": "Тесты avf_output.py",
            "tests/test_avfoundation_google_input.py": "Тесты google_input.py",
            "tests/integration/test_audio_route_manager.py": "Интеграционные тесты RouteManager",
            "tests/integration/test_device_switching.py": "Тесты переключения устройств",
            "tests/integration/test_heartbeat_watchdog.py": "Тесты heartbeat и watchdog",
        }
        
        # Файлы для изменения
        self.files_to_modify = {
            "integration/integrations/voice_recognition_integration.py": "Добавить RouteManager логику",
            "integration/integrations/speech_playback_integration.py": "Добавить AVFoundation output",
            "integration/core/simple_module_coordinator.py": "Добавить AudioRouteManagerIntegration",
            "config/unified_config.yaml": "Добавить секцию audio_system",
            "Docs/FEATURE_FLAGS.md": "Зарегистрировать feature flags",
        }
        
        # События, которые должен использовать RouteManager
        self.route_manager_events = {
            "audio.route.snapshot": "Snapshot состояния маршрутизации",
            "audio.input.active": "Input активирован",
            "audio.input.failed": "Input не удалось активировать",
            "audio.output.ready": "Output готов",
            "audio.output.error": "Ошибка output",
            "audio.device.changed": "Устройство изменилось",
        }
        
        # Блокировки
        self.blocking_events = {
            "permissions.first_run_started": "VoiceRecognitionIntegration",
            "permissions.first_run_completed": "VoiceRecognitionIntegration",
            "permission_restart.scheduled": "PermissionRestartIntegration",
            "update.started": "UpdaterIntegration",
        }
        
        # Зависимости PyObjC
        self.required_pyobjc = [
            "pyobjc-core",
            "pyobjc-framework-AVFoundation",
            "pyobjc-framework-CoreAudio",
        ]
        
    def analyze(self) -> DetailedAnalysisResult:
        """Выполнить детальный анализ"""
        print("🔍 Начинаем детальный анализ готовности к миграции аудиосистемы...")
        print("=" * 80)
        
        # 1. Анализ файлов
        print("\n📁 Анализ файлов...")
        files_to_create = self._analyze_files_to_create()
        files_to_modify = self._analyze_files_to_modify()
        files_existing = self._analyze_existing_files()
        
        # 2. Детальный анализ событий
        print("\n📡 Детальный анализ событий EventBus...")
        events_detailed = self._analyze_events_detailed()
        events_missing = self._find_missing_events(events_detailed)
        
        # 3. Проверка зависимостей
        print("\n📦 Проверка зависимостей...")
        dependencies = self._check_dependencies()
        
        # 4. Проверка блокировок
        print("\n🔒 Проверка блокировок...")
        blocking_conditions = self._check_blocking_conditions()
        
        # 5. Анализ конфигурации
        print("\n⚙️ Анализ конфигурации...")
        config_sections, config_missing = self._analyze_config_detailed()
        
        # 6. Анализ тестов
        print("\n🧪 Анализ тестов...")
        tests_existing, tests_missing = self._analyze_tests()
        
        # 7. Проверка CI/CD
        print("\n🔄 Проверка CI/CD...")
        ci_integration = self._check_ci_integration()
        
        # 8. Анализ порядка инициализации
        print("\n🔄 Анализ порядка инициализации...")
        init_order, init_order_issues = self._analyze_init_order_detailed()
        
        # 9. Расчет готовности
        print("\n📊 Расчет готовности...")
        readiness_score, readiness_breakdown, recommendations, critical_issues, warnings = self._calculate_readiness_detailed(
            files_to_create, files_to_modify, events_detailed, events_missing,
            dependencies, blocking_conditions, config_sections, config_missing,
            tests_existing, tests_missing, ci_integration, init_order_issues
        )
        
        return DetailedAnalysisResult(
            files_to_create=files_to_create,
            files_to_modify=files_to_modify,
            files_existing=files_existing,
            events_detailed=events_detailed,
            events_missing=events_missing,
            dependencies=dependencies,
            blocking_conditions=blocking_conditions,
            config_sections=config_sections,
            config_missing=config_missing,
            tests_existing=tests_existing,
            tests_missing=tests_missing,
            ci_integration=ci_integration,
            init_order=init_order,
            init_order_issues=init_order_issues,
            readiness_score=readiness_score,
            readiness_breakdown=readiness_breakdown,
            recommendations=recommendations,
            critical_issues=critical_issues,
            warnings=warnings
        )
    
    def _analyze_files_to_create(self) -> List[FileStatus]:
        """Анализ файлов для создания"""
        files = []
        for rel_path, description in self.files_to_create.items():
            full_path = self.client_root / rel_path
            files.append(FileStatus(
                path=rel_path,
                exists=full_path.exists(),
                needs_create=not full_path.exists(),
                needs_modify=False,
                lines_of_code=self._count_lines(full_path) if full_path.exists() else None,
                dependencies=self._extract_dependencies(full_path) if full_path.exists() else [],
                tests_exist=self._check_tests_exist(rel_path)
            ))
        return files
    
    def _analyze_files_to_modify(self) -> List[FileStatus]:
        """Анализ файлов для изменения"""
        files = []
        for rel_path, description in self.files_to_modify.items():
            full_path = self.client_root / rel_path if not rel_path.startswith("Docs/") else self.project_root / rel_path
            if full_path.exists():
                files.append(FileStatus(
                    path=rel_path,
                    exists=True,
                    needs_create=False,
                    needs_modify=True,
                    lines_of_code=self._count_lines(full_path),
                    dependencies=self._extract_dependencies(full_path),
                    tests_exist=self._check_tests_exist(rel_path)
                ))
            else:
                files.append(FileStatus(
                    path=rel_path,
                    exists=False,
                    needs_create=True,
                    needs_modify=False,
                    lines_of_code=None,
                    dependencies=[],
                    tests_exist=False
                ))
        return files
    
    def _analyze_existing_files(self) -> List[FileStatus]:
        """Анализ существующих файлов, связанных с аудио"""
        files = []
        audio_modules = ["voice_recognition", "speech_playback", "input_processing"]
        
        for module_name in audio_modules:
            module_path = self.client_root / "modules" / module_name
            if module_path.exists():
                for py_file in module_path.rglob("*.py"):
                    if "test" in str(py_file) or "__pycache__" in str(py_file):
                        continue
                    rel_path = py_file.relative_to(self.client_root)
                    files.append(FileStatus(
                        path=str(rel_path),
                        exists=True,
                        needs_create=False,
                        needs_modify=False,
                        lines_of_code=self._count_lines(py_file),
                        dependencies=self._extract_dependencies(py_file),
                        tests_exist=self._check_tests_exist(str(rel_path))
                    ))
        
        return files
    
    def _analyze_events_detailed(self) -> List[EventDetail]:
        """Детальный анализ событий EventBus"""
        events_dict: Dict[str, EventDetail] = {}
        
        # Паттерны для поиска
        publish_pattern = re.compile(r'publish\(["\']([^"\']+)["\']')
        subscribe_pattern = re.compile(r'subscribe\(["\']([^"\']+)["\']')
        priority_pattern = re.compile(r'EventPriority\.(\w+)')
        
        # Анализируем интеграции
        integrations_path = self.client_root / "integration" / "integrations"
        if integrations_path.exists():
            for py_file in integrations_path.glob("*.py"):
                if py_file.name == "__init__.py":
                    continue
                
                try:
                    content = py_file.read_text()
                    module_name = py_file.stem.replace("_integration", "")
                    
                    # Ищем publish с приоритетом
                    for match in publish_pattern.finditer(content):
                        event_name = match.group(1)
                        if event_name not in events_dict:
                            events_dict[event_name] = EventDetail(
                                name=event_name,
                                publishers=[],
                                subscribers=[],
                                audio_related=any(kw in event_name.lower() for kw in ["voice", "audio", "mic", "playback", "recording", "speech", "sound", "device"]),
                                used_by_route_manager=event_name in self.route_manager_events
                            )
                        if module_name not in events_dict[event_name].publishers:
                            events_dict[event_name].publishers.append(module_name)
                    
                    # Ищем subscribe с приоритетом
                    for match in subscribe_pattern.finditer(content):
                        event_name = match.group(1)
                        # Ищем приоритет перед subscribe
                        context_start = max(0, match.start() - 200)
                        context = content[context_start:match.start()]
                        priority_match = priority_pattern.search(context)
                        priority = priority_match.group(1) if priority_match else None
                        
                        if event_name not in events_dict:
                            events_dict[event_name] = EventDetail(
                                name=event_name,
                                publishers=[],
                                subscribers=[],
                                priority=priority,
                                audio_related=any(kw in event_name.lower() for kw in ["voice", "audio", "mic", "playback", "recording", "speech", "sound", "device"]),
                                used_by_route_manager=event_name in self.route_manager_events
                            )
                        if module_name not in events_dict[event_name].subscribers:
                            events_dict[event_name].subscribers.append(module_name)
                        if priority and not events_dict[event_name].priority:
                            events_dict[event_name].priority = priority
                except Exception as e:
                    print(f"⚠️ Ошибка анализа {py_file}: {e}")
        
        return list(events_dict.values())
    
    def _find_missing_events(self, events: List[EventDetail]) -> List[str]:
        """Найти отсутствующие события"""
        existing_names = {e.name for e in events}
        missing = []
        for event_name in self.route_manager_events:
            if event_name not in existing_names:
                missing.append(event_name)
        return missing
    
    def _check_dependencies(self) -> List[DependencyCheck]:
        """Проверка зависимостей"""
        dependencies = []
        
        # Проверяем requirements.txt
        if self.requirements_path.exists():
            content = self.requirements_path.read_text()
            for dep_name in self.required_pyobjc:
                version_match = re.search(rf'{re.escape(dep_name)}==([\d.]+)', content)
                version = version_match.group(1) if version_match else None
                available = dep_name in content
                dependencies.append(DependencyCheck(
                    name=dep_name,
                    required=True,
                    available=available,
                    version=version,
                    location="requirements.txt"
                ))
        
        return dependencies
    
    def _check_blocking_conditions(self) -> List[BlockingCondition]:
        """Проверка условий блокировки"""
        conditions = []
        
        for event_name, integration_name in self.blocking_events.items():
            # Проверяем, подписывается ли интеграция на событие
            integration_path = self.client_root / "integration" / "integrations" / f"{integration_name.lower()}_integration.py"
            checked = False
            if integration_path.exists():
                content = integration_path.read_text()
                checked = event_name in content
            
            conditions.append(BlockingCondition(
                name=f"{integration_name} блокирует при {event_name}",
                event=event_name,
                integration=integration_name,
                checked=checked
            ))
        
        return conditions
    
    def _analyze_config_detailed(self) -> Tuple[Dict[str, Any], List[str]]:
        """Детальный анализ конфигурации"""
        config_sections = {}
        config_missing = []
        
        if not self.config_path.exists():
            config_missing.append("unified_config.yaml не существует")
            return config_sections, config_missing
        
        try:
            with open(self.config_path, 'r') as f:
                config_data = yaml.safe_load(f) or {}
            
            # Проверяем необходимые секции
            required_sections = {
                "audio_system": "Секция для новой аудиосистемы",
                "voice_recognition": "Конфигурация распознавания речи",
                "speech_playback": "Конфигурация воспроизведения",
                "default_audio": "Конфигурация аудио по умолчанию",
            }
            
            for section, description in required_sections.items():
                if section in config_data:
                    config_sections[section] = config_data[section]
                else:
                    config_missing.append(f"{section} ({description})")
            
            # Проверяем audio_system детально
            if "audio_system" in config_data:
                audio_system = config_data["audio_system"]
                required_flags = [
                    "avfoundation_enabled",
                    "avfoundation_input_monitor_enabled",
                    "avfoundation_output_enabled",
                    "avfoundation_route_manager_enabled",
                ]
                for flag in required_flags:
                    if flag not in audio_system:
                        config_missing.append(f"audio_system.{flag}")
        except Exception as e:
            config_missing.append(f"Ошибка чтения конфигурации: {e}")
        
        return config_sections, config_missing
    
    def _analyze_tests(self) -> Tuple[List[str], List[str]]:
        """Анализ тестов"""
        tests_existing = []
        tests_missing = []
        
        tests_path = self.client_root / "tests"
        if not tests_path.exists():
            return tests_existing, list(self.files_to_create.keys())
        
        # Ищем существующие тесты
        for test_file in tests_path.rglob("test_*.py"):
            rel_path = str(test_file.relative_to(self.client_root))
            tests_existing.append(rel_path)
        
        # Проверяем отсутствующие тесты
        for rel_path in self.files_to_create.keys():
            if "test_" in rel_path or "integration" in rel_path:
                test_path = self.client_root / rel_path
                if not test_path.exists():
                    tests_missing.append(rel_path)
        
        return tests_existing, tests_missing
    
    def _check_ci_integration(self) -> Dict[str, bool]:
        """Проверка CI/CD интеграции"""
        ci_checks = {
            "pre_build_gate_exists": False,
            "release_suite_exists": False,
            "audio_tests_in_ci": False,
            "feature_flags_validation": False,
        }
        
        # Проверяем pre_build_gate.sh
        pre_build_gate = self.client_root / "scripts" / "pre_build_gate.sh"
        ci_checks["pre_build_gate_exists"] = pre_build_gate.exists()
        
        # Проверяем run_release_suite.py
        release_suite = self.client_root / "scripts" / "run_release_suite.py"
        ci_checks["release_suite_exists"] = release_suite.exists()
        
        # Проверяем CI workflow
        if self.ci_workflow_path.exists():
            content = self.ci_workflow_path.read_text()
            ci_checks["audio_tests_in_ci"] = "test_avfoundation" in content or "audio" in content.lower()
            ci_checks["feature_flags_validation"] = "feature_flag" in content.lower() or "FEATURE_FLAGS" in content
        
        return ci_checks
    
    def _analyze_init_order_detailed(self) -> Tuple[List[str], List[str]]:
        """Детальный анализ порядка инициализации"""
        init_order = []
        issues = []
        
        coordinator_path = self.client_root / "integration" / "core" / "simple_module_coordinator.py"
        if not coordinator_path.exists():
            issues.append("SimpleModuleCoordinator не найден")
            return init_order, issues
        
        try:
            content = coordinator_path.read_text()
            # Ищем порядок инициализации
            order_match = re.search(r'startup_order\s*=\s*\[(.*?)\]', content, re.DOTALL)
            if order_match:
                order_str = order_match.group(1)
                modules = re.findall(r"['\"]([^'\"]+)['\"]", order_str)
                init_order = [m.strip() for m in modules if m.strip() and not m.strip().startswith('#')]
            
            # Проверяем наличие audio_route_manager
            if "audio_route_manager" not in init_order:
                issues.append("audio_route_manager отсутствует в порядке инициализации")
            
            # Проверяем порядок (voice_recognition должен быть до audio_route_manager)
            if "voice_recognition" in init_order and "audio_route_manager" in init_order:
                voice_idx = init_order.index("voice_recognition")
                route_idx = init_order.index("audio_route_manager")
                if route_idx <= voice_idx:
                    issues.append("audio_route_manager должен инициализироваться после voice_recognition")
        except Exception as e:
            issues.append(f"Ошибка анализа порядка инициализации: {e}")
        
        return init_order, issues
    
    def _calculate_readiness_detailed(
        self,
        files_to_create: List[FileStatus],
        files_to_modify: List[FileStatus],
        events_detailed: List[EventDetail],
        events_missing: List[str],
        dependencies: List[DependencyCheck],
        blocking_conditions: List[BlockingCondition],
        config_sections: Dict[str, Any],
        config_missing: List[str],
        tests_existing: List[str],
        tests_missing: List[str],
        ci_integration: Dict[str, bool],
        init_order_issues: List[str]
    ) -> Tuple[float, Dict[str, float], List[str], List[str], List[str]]:
        """Детальный расчет готовности"""
        score = 100.0
        breakdown = {}
        recommendations = []
        critical_issues = []
        warnings = []
        
        # 1. Файлы для создания (30%)
        files_score = 100.0
        files_created = sum(1 for f in files_to_create if f.exists)
        files_total = len(files_to_create)
        if files_total > 0:
            files_score = (files_created / files_total) * 100.0
        breakdown["files_to_create"] = files_score
        score = score * 0.3 * (files_score / 100.0) + score * 0.7
        
        if files_score < 100:
            critical_issues.append(f"Создано только {files_created}/{files_total} файлов ({files_score:.1f}%)")
        
        # 2. Файлы для изменения (10%)
        modify_score = 100.0
        files_modified = sum(1 for f in files_to_modify if f.exists and not f.needs_modify)
        files_modify_total = len(files_to_modify)
        if files_modify_total > 0:
            modify_score = (files_modified / files_modify_total) * 100.0
        breakdown["files_to_modify"] = modify_score
        score = score * 0.1 * (modify_score / 100.0) + score * 0.9
        
        if modify_score < 100:
            warnings.append(f"Изменено только {files_modified}/{files_modify_total} файлов")
        
        # 3. События (15%)
        events_score = 100.0
        audio_events = [e for e in events_detailed if e.audio_related]
        if len(events_missing) > 0:
            events_score -= len(events_missing) * 10
        breakdown["events"] = max(0, events_score)
        score = score * 0.15 * (events_score / 100.0) + score * 0.85
        
        if events_missing:
            critical_issues.append(f"Отсутствуют события: {', '.join(events_missing)}")
        
        # 4. Зависимости (10%)
        deps_score = 100.0
        missing_deps = [d for d in dependencies if d.required and not d.available]
        if missing_deps:
            deps_score -= len(missing_deps) * 20
        breakdown["dependencies"] = max(0, deps_score)
        score = score * 0.1 * (deps_score / 100.0) + score * 0.9
        
        if missing_deps:
            critical_issues.append(f"Отсутствуют зависимости: {', '.join(d.name for d in missing_deps)}")
        
        # 5. Блокировки (5%)
        blocking_score = 100.0
        unchecked_blocking = [b for b in blocking_conditions if not b.checked]
        if unchecked_blocking:
            blocking_score -= len(unchecked_blocking) * 15
        breakdown["blocking_conditions"] = max(0, blocking_score)
        score = score * 0.05 * (blocking_score / 100.0) + score * 0.95
        
        if unchecked_blocking:
            warnings.append(f"Не проверены блокировки: {len(unchecked_blocking)}")
        
        # 6. Конфигурация (10%)
        config_score = 100.0
        if config_missing:
            config_score -= len(config_missing) * 10
        breakdown["configuration"] = max(0, config_score)
        score = score * 0.1 * (config_score / 100.0) + score * 0.9
        
        if config_missing:
            critical_issues.append(f"Отсутствуют секции конфигурации: {len(config_missing)}")
        
        # 7. Тесты (10%)
        tests_score = 100.0
        if tests_missing:
            tests_score -= len(tests_missing) * 5
        breakdown["tests"] = max(0, tests_score)
        score = score * 0.1 * (tests_score / 100.0) + score * 0.9
        
        if tests_missing:
            warnings.append(f"Отсутствуют тесты: {len(tests_missing)}")
        
        # 8. CI/CD (5%)
        ci_score = sum(ci_integration.values()) / len(ci_integration) * 100.0 if ci_integration else 0
        breakdown["ci_cd"] = ci_score
        score = score * 0.05 * (ci_score / 100.0) + score * 0.95
        
        if ci_score < 100:
            warnings.append("CI/CD интеграция неполная")
        
        # 9. Порядок инициализации (5%)
        init_score = 100.0
        if init_order_issues:
            init_score -= len(init_order_issues) * 20
        breakdown["initialization_order"] = max(0, init_score)
        score = score * 0.05 * (init_score / 100.0) + score * 0.95
        
        if init_order_issues:
            critical_issues.extend(init_order_issues)
        
        # Рекомендации
        if score < 50:
            recommendations.append("🔴 Критический уровень - требуется немедленная доработка")
        elif score < 70:
            recommendations.append("🟡 Низкий уровень - требуется доработка перед началом миграции")
        elif score < 85:
            recommendations.append("🟠 Средний уровень - рекомендуется доработка")
        else:
            recommendations.append("🟢 Высокий уровень - можно начинать миграцию")
        
        return max(0.0, min(100.0, score)), breakdown, recommendations, critical_issues, warnings
    
    # Вспомогательные методы
    def _count_lines(self, file_path: Path) -> Optional[int]:
        """Подсчет строк в файле"""
        if not file_path.exists():
            return None
        try:
            return len(file_path.read_text().splitlines())
        except Exception:
            return None
    
    def _extract_dependencies(self, file_path: Path) -> List[str]:
        """Извлечение зависимостей из файла"""
        if not file_path.exists():
            return []
        try:
            content = file_path.read_text()
            tree = ast.parse(content)
            deps = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        deps.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        deps.append(node.module)
            return list(set(deps))
        except Exception:
            return []
    
    def _check_tests_exist(self, file_path: str) -> bool:
        """Проверка существования тестов для файла"""
        # Простая проверка: ищем test_ файлы с похожим именем
        test_name = Path(file_path).stem
        tests_path = self.client_root / "tests"
        if not tests_path.exists():
            return False
        
        # Ищем тесты с похожим именем
        for test_file in tests_path.rglob(f"test_*{test_name}*.py"):
            return True
        
        return False


def print_detailed_report(result: DetailedAnalysisResult):
    """Вывести детальный отчет"""
    print("\n" + "="*80)
    print("📊 ДЕТАЛЬНЫЙ ОТЧЕТ О ГОТОВНОСТИ К МИГРАЦИИ АУДИОСИСТЕМЫ")
    print("="*80)
    
    print(f"\n🎯 Общая готовность: {result.readiness_score:.1f}%")
    
    print("\n📊 Разбивка по категориям:")
    print("-" * 80)
    for category, score in result.readiness_breakdown.items():
        bar_length = int(score / 5)
        bar = "█" * bar_length + "░" * (20 - bar_length)
        print(f"  {category:25s} {bar} {score:5.1f}%")
    
    print("\n📁 ФАЙЛЫ ДЛЯ СОЗДАНИЯ:")
    print("-" * 80)
    created = sum(1 for f in result.files_to_create if f.exists)
    total = len(result.files_to_create)
    print(f"  Создано: {created}/{total}")
    for file in result.files_to_create[:10]:
        status = "✅" if file.exists else "❌"
        print(f"  {status} {file.path}")
    if len(result.files_to_create) > 10:
        print(f"  ... и еще {len(result.files_to_create) - 10} файлов")
    
    print("\n📝 ФАЙЛЫ ДЛЯ ИЗМЕНЕНИЯ:")
    print("-" * 80)
    for file in result.files_to_modify:
        status = "✅" if file.exists and not file.needs_modify else "⚠️" if file.exists else "❌"
        print(f"  {status} {file.path}")
    
    print("\n📡 СОБЫТИЯ EVENTBUS:")
    print("-" * 80)
    audio_events = [e for e in result.events_detailed if e.audio_related]
    print(f"  Всего аудио-событий: {len(audio_events)}")
    route_manager_events = [e for e in result.events_detailed if e.used_by_route_manager]
    print(f"  События для RouteManager: {len(route_manager_events)}")
    if result.events_missing:
        print(f"  ❌ Отсутствующие события: {', '.join(result.events_missing)}")
    
    print("\n📦 ЗАВИСИМОСТИ:")
    print("-" * 80)
    for dep in result.dependencies:
        status = "✅" if dep.available else "❌"
        version_str = f" (v{dep.version})" if dep.version else ""
        print(f"  {status} {dep.name}{version_str}")
    
    print("\n🔒 БЛОКИРОВКИ:")
    print("-" * 80)
    for blocking in result.blocking_conditions:
        status = "✅" if blocking.checked else "⚠️"
        print(f"  {status} {blocking.name}")
    
    print("\n⚙️ КОНФИГУРАЦИЯ:")
    print("-" * 80)
    print(f"  Секции найдены: {len(result.config_sections)}")
    if result.config_missing:
        print(f"  ❌ Отсутствующие секции: {len(result.config_missing)}")
        for missing in result.config_missing[:5]:
            print(f"    - {missing}")
    
    print("\n🧪 ТЕСТЫ:")
    print("-" * 80)
    print(f"  Существующие: {len(result.tests_existing)}")
    if result.tests_missing:
        print(f"  ❌ Отсутствующие: {len(result.tests_missing)}")
    
    print("\n🔄 CI/CD:")
    print("-" * 80)
    for check, status in result.ci_integration.items():
        status_icon = "✅" if status else "❌"
        print(f"  {status_icon} {check}")
    
    print("\n🔄 ПОРЯДОК ИНИЦИАЛИЗАЦИИ:")
    print("-" * 80)
    for i, module in enumerate(result.init_order[:15], 1):
        marker = "🎤" if any(kw in module.lower() for kw in ["voice", "audio", "speech", "input"]) else "  "
        print(f"  {marker} {i}. {module}")
    if len(result.init_order) > 15:
        print(f"  ... и еще {len(result.init_order) - 15} модулей")
    
    if result.init_order_issues:
        print(f"  ⚠️ Проблемы: {', '.join(result.init_order_issues)}")
    
    print("\n❌ КРИТИЧЕСКИЕ ПРОБЛЕМЫ:")
    print("-" * 80)
    if result.critical_issues:
        for issue in result.critical_issues:
            print(f"  ❌ {issue}")
    else:
        print("  ✅ Критических проблем не обнаружено")
    
    print("\n⚠️ ПРЕДУПРЕЖДЕНИЯ:")
    print("-" * 80)
    if result.warnings:
        for warning in result.warnings:
            print(f"  ⚠️ {warning}")
    else:
        print("  ✅ Предупреждений нет")
    
    print("\n💡 РЕКОМЕНДАЦИИ:")
    print("-" * 80)
    for rec in result.recommendations:
        print(f"  {rec}")
    
    print("\n" + "="*80)


def save_detailed_json_report(result: DetailedAnalysisResult, output_path: str):
    """Сохранить детальный отчет в JSON"""
    report = {
        "readiness_score": result.readiness_score,
        "readiness_breakdown": result.readiness_breakdown,
        "files_to_create": [asdict(f) for f in result.files_to_create],
        "files_to_modify": [asdict(f) for f in result.files_to_modify],
        "files_existing": [asdict(f) for f in result.files_existing],
        "events_detailed": [asdict(e) for e in result.events_detailed],
        "events_missing": result.events_missing,
        "dependencies": [asdict(d) for d in result.dependencies],
        "blocking_conditions": [asdict(b) for b in result.blocking_conditions],
        "config_sections": result.config_sections,
        "config_missing": result.config_missing,
        "tests_existing": result.tests_existing,
        "tests_missing": result.tests_missing,
        "ci_integration": result.ci_integration,
        "init_order": result.init_order,
        "init_order_issues": result.init_order_issues,
        "recommendations": result.recommendations,
        "critical_issues": result.critical_issues,
        "warnings": result.warnings
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Детальный отчет сохранен в: {output_path}")


def main():
    """Главная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Детальный анализ готовности к миграции аудиосистемы"
    )
    parser.add_argument(
        "--project-root",
        type=str,
        default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        help="Корневая директория проекта"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="audio_migration_readiness_detailed_report.json",
        help="Путь для сохранения JSON отчета"
    )
    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Только JSON отчет, без вывода в консоль"
    )
    
    args = parser.parse_args()
    
    analyzer = DetailedAudioMigrationAnalyzer(args.project_root)
    result = analyzer.analyze()
    
    if not args.json_only:
        print_detailed_report(result)
    
    save_detailed_json_report(result, args.output)
    
    # Exit code на основе готовности
    if result.readiness_score < 50:
        sys.exit(1)
    elif result.readiness_score < 70:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

