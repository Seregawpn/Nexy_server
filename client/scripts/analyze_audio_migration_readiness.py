#!/usr/bin/env python3
"""
Диагностический скрипт для анализа готовности к миграции аудиосистемы.

Анализирует:
- Все feature flags и их использование
- Все модули и интеграции, взаимодействующие с аудио
- Все события EventBus, связанные с аудио
- Все зависимости и потенциальные конфликты
- Конфигурацию и настройки
- Порядок инициализации

БЕЗ фактического внедрения новой системы.
"""

import os
import sys
import json
import re
import ast
import yaml
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
from dataclasses import dataclass, asdict
from collections import defaultdict

# Добавляем пути для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

@dataclass
class FeatureFlag:
    """Информация о feature flag"""
    name: str
    config_path: str
    code_locations: List[str]
    default_value: Any
    purpose: str
    type: str  # "feature_flag" | "kill_switch"

@dataclass
class EventInfo:
    """Информация о событии EventBus"""
    name: str
    publishers: List[str]
    subscribers: List[str]
    priority: Optional[str] = None

@dataclass
class ModuleInfo:
    """Информация о модуле"""
    name: str
    path: str
    audio_related: bool
    dependencies: List[str]
    events_published: List[str]
    events_subscribed: List[str]

@dataclass
class IntegrationInfo:
    """Информация об интеграции"""
    name: str
    path: str
    audio_related: bool
    dependencies: List[str]
    events_published: List[str]
    events_subscribed: List[str]
    initialization_order: Optional[int] = None

@dataclass
class AnalysisResult:
    """Результат анализа"""
    feature_flags: List[FeatureFlag]
    events: List[EventInfo]
    modules: List[ModuleInfo]
    integrations: List[IntegrationInfo]
    config_entries: Dict[str, Any]
    initialization_order: List[str]
    potential_conflicts: List[str]
    readiness_score: float
    recommendations: List[str]


class AudioMigrationAnalyzer:
    """Анализатор готовности к миграции аудиосистемы"""
    
    def __init__(self, project_root: str):
        project_root_path = Path(project_root).resolve()
        
        # Определяем client_root: если есть client/ - используем его, иначе текущая директория
        if (project_root_path / "client").exists() and (project_root_path / "client" / "integration").exists():
            self.client_root = project_root_path / "client"
            self.project_root = project_root_path
        elif (project_root_path / "integration").exists():
            # Мы уже в client/
            self.client_root = project_root_path
            # Ищем project root (где есть Docs/)
            current = project_root_path
            while current != current.parent:
                if (current / "Docs").exists():
                    self.project_root = current
                    break
                current = current.parent
            else:
                self.project_root = project_root_path.parent
        else:
            # Fallback: используем переданный путь
            self.client_root = project_root_path
            self.project_root = project_root_path.parent if (project_root_path.parent / "Docs").exists() else project_root_path
        
        self.config_path = self.client_root / "config" / "unified_config.yaml"
        self.feature_flags_path = self.project_root / "Docs" / "FEATURE_FLAGS.md"
        
        # Паттерны для поиска
        self.event_patterns = {
            "publish": re.compile(r'await\s+self\.event_bus\.publish\(["\']([^"\']+)["\']'),
            "subscribe": re.compile(r'await\s+self\.event_bus\.subscribe\(["\']([^"\']+)["\']'),
        }
        
        self.audio_related_keywords = {
            "voice", "audio", "mic", "microphone", "recording", 
            "playback", "speech", "sound", "device", "input", "output",
            "recogn", "listening", "stream"
        }
        
        self.audio_event_prefixes = {
            "voice.", "audio.", "playback.", "recording.", "mic", "speech."
        }
        
    def analyze(self) -> AnalysisResult:
        """Выполнить полный анализ"""
        print("🔍 Начинаем анализ готовности к миграции аудиосистемы...")
        
        # 1. Анализ feature flags
        print("📋 Анализ feature flags...")
        feature_flags = self._analyze_feature_flags()
        
        # 2. Анализ событий EventBus
        print("📡 Анализ событий EventBus...")
        events = self._analyze_events()
        
        # 3. Анализ модулей
        print("🧩 Анализ модулей...")
        modules = self._analyze_modules()
        
        # 4. Анализ интеграций
        print("🔗 Анализ интеграций...")
        integrations = self._analyze_integrations()
        
        # 5. Анализ конфигурации
        print("⚙️ Анализ конфигурации...")
        config_entries = self._analyze_config()
        
        # 6. Анализ порядка инициализации
        print("🔄 Анализ порядка инициализации...")
        initialization_order = self._analyze_initialization_order()
        
        # 7. Поиск потенциальных конфликтов
        print("⚠️ Поиск потенциальных конфликтов...")
        potential_conflicts = self._find_potential_conflicts(
            feature_flags, events, modules, integrations
        )
        
        # 8. Расчет готовности
        print("📊 Расчет готовности...")
        readiness_score, recommendations = self._calculate_readiness(
            feature_flags, events, modules, integrations, potential_conflicts
        )
        
        return AnalysisResult(
            feature_flags=feature_flags,
            events=events,
            modules=modules,
            integrations=integrations,
            config_entries=config_entries,
            initialization_order=initialization_order,
            potential_conflicts=potential_conflicts,
            readiness_score=readiness_score,
            recommendations=recommendations
        )
    
    def _analyze_feature_flags(self) -> List[FeatureFlag]:
        """Анализ feature flags из FEATURE_FLAGS.md и кода"""
        flags = []
        
        # Читаем FEATURE_FLAGS.md
        if self.feature_flags_path.exists():
            content = self.feature_flags_path.read_text()
            # Парсим таблицу feature flags
            for line in content.split('\n'):
                if '|' in line and 'NEXY_' in line and not line.strip().startswith('|--'):
                    parts = [p.strip() for p in line.split('|')]
                    # Убираем пустые элементы в начале/конце
                    parts = [p for p in parts if p]
                    if len(parts) >= 7:
                        name = parts[0].strip().strip('`')
                        flag_type = parts[1].strip()
                        config_path = parts[2].strip().strip('`')
                        code_location = parts[3].strip().strip('`')
                        default = parts[5].strip()
                        purpose = parts[6].strip() if len(parts) > 6 else ""
                        
                        flags.append(FeatureFlag(
                            name=name,
                            config_path=config_path,
                            code_locations=[code_location] if code_location and code_location != "Pending wiring" else [],
                            default_value=default,
                            purpose=purpose,
                            type=flag_type.lower().replace("-", "_")
                        ))
        
        # Ищем feature flags в коде
        for py_file in self.client_root.rglob("*.py"):
            if "test" in str(py_file) or "__pycache__" in str(py_file):
                continue
            
            try:
                content = py_file.read_text()
                # Ищем упоминания feature flags
                for flag in flags:
                    if flag.name in content:
                        if str(py_file) not in flag.code_locations:
                            flag.code_locations.append(str(py_file))
            except Exception:
                pass
        
        return flags
    
    def _analyze_events(self) -> List[EventInfo]:
        """Анализ событий EventBus"""
        events_dict: Dict[str, EventInfo] = {}
        
        # Паттерны для поиска событий
        publish_pattern = re.compile(r'publish\(["\']([^"\']+)["\']')
        subscribe_pattern = re.compile(r'subscribe\(["\']([^"\']+)["\']')
        
        # Анализируем интеграции
        integrations_path = self.client_root / "integration" / "integrations"
        if integrations_path.exists():
            for py_file in integrations_path.glob("*.py"):
                if py_file.name == "__init__.py":
                    continue
                
                try:
                    content = py_file.read_text()
                    module_name = py_file.stem.replace("_integration", "")
                    
                    # Ищем publish
                    for match in publish_pattern.finditer(content):
                        event_name = match.group(1)
                        if event_name not in events_dict:
                            events_dict[event_name] = EventInfo(
                                name=event_name,
                                publishers=[],
                                subscribers=[]
                            )
                        if module_name not in events_dict[event_name].publishers:
                            events_dict[event_name].publishers.append(module_name)
                    
                    # Ищем subscribe
                    for match in subscribe_pattern.finditer(content):
                        event_name = match.group(1)
                        if event_name not in events_dict:
                            events_dict[event_name] = EventInfo(
                                name=event_name,
                                publishers=[],
                                subscribers=[]
                            )
                        if module_name not in events_dict[event_name].subscribers:
                            events_dict[event_name].subscribers.append(module_name)
                except Exception as e:
                    print(f"⚠️ Ошибка анализа {py_file}: {e}")
        
        # Анализируем workflows
        workflows_path = self.client_root / "integration" / "workflows"
        if workflows_path.exists():
            for py_file in workflows_path.glob("*.py"):
                if py_file.name == "__init__.py" or "base" in py_file.name:
                    continue
                
                try:
                    content = py_file.read_text()
                    module_name = py_file.stem.replace("_workflow", "")
                    
                    # Ищем subscribe в workflows
                    for match in subscribe_pattern.finditer(content):
                        event_name = match.group(1)
                        if event_name not in events_dict:
                            events_dict[event_name] = EventInfo(
                                name=event_name,
                                publishers=[],
                                subscribers=[]
                            )
                        if module_name not in events_dict[event_name].subscribers:
                            events_dict[event_name].subscribers.append(module_name)
                except Exception:
                    pass
        
        return list(events_dict.values())
    
    def _analyze_modules(self) -> List[ModuleInfo]:
        """Анализ модулей"""
        modules = []
        modules_path = self.client_root / "modules"
        
        if not modules_path.exists():
            return modules
        
        for module_dir in modules_path.iterdir():
            if not module_dir.is_dir() or module_dir.name.startswith('_'):
                continue
            
            # Проверяем, связан ли модуль с аудио
            module_name_lower = module_dir.name.lower()
            audio_related = any(
                keyword in module_name_lower 
                for keyword in self.audio_related_keywords
            )
            
            # Дополнительная проверка по содержимому файлов
            if not audio_related:
                for py_file in module_dir.rglob("*.py"):
                    if "test" in str(py_file) or "__pycache__" in str(py_file):
                        continue
                    try:
                        content = py_file.read_text().lower()
                        if any(keyword in content for keyword in self.audio_related_keywords):
                            audio_related = True
                            break
                    except Exception:
                        pass
            
            # Анализируем файлы модуля
            events_published = []
            events_subscribed = []
            dependencies = []
            
            for py_file in module_dir.rglob("*.py"):
                if "test" in str(py_file) or "__pycache__" in str(py_file):
                    continue
                
                try:
                    content = py_file.read_text()
                    
                    # Ищем события
                    for match in self.event_patterns["publish"].finditer(content):
                        event_name = match.group(1)
                        if event_name not in events_published:
                            events_published.append(event_name)
                    
                    for match in self.event_patterns["subscribe"].finditer(content):
                        event_name = match.group(1)
                        if event_name not in events_subscribed:
                            events_subscribed.append(event_name)
                    
                    # Ищем импорты (зависимости)
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                dependencies.append(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                dependencies.append(node.module)
                except Exception:
                    pass
            
            modules.append(ModuleInfo(
                name=module_dir.name,
                path=str(module_dir),
                audio_related=audio_related,
                dependencies=list(set(dependencies)),
                events_published=events_published,
                events_subscribed=events_subscribed
            ))
        
        return modules
    
    def _analyze_integrations(self) -> List[IntegrationInfo]:
        """Анализ интеграций"""
        integrations = []
        integrations_path = self.client_root / "integration" / "integrations"
        
        if not integrations_path.exists():
            return integrations
        
        # Читаем порядок инициализации из SimpleModuleCoordinator
        initialization_order = self._get_initialization_order()
        
        for py_file in integrations_path.glob("*.py"):
            if py_file.name == "__init__.py":
                continue
            
            try:
                content = py_file.read_text()
                module_name = py_file.stem.replace("_integration", "")
                
                # Проверяем, связана ли интеграция с аудио
                module_name_lower = module_name.lower()
                content_lower = content.lower()
                audio_related = any(
                    keyword in module_name_lower or keyword in content_lower
                    for keyword in self.audio_related_keywords
                )
                
                # Дополнительная проверка по событиям
                if not audio_related:
                    # Проверяем события в коде
                    for event_name in events_published + events_subscribed:
                        if any(prefix in event_name.lower() for prefix in self.audio_event_prefixes):
                            audio_related = True
                            break
                
                # Анализируем события
                events_published = []
                events_subscribed = []
                dependencies = []
                
                # Ищем publish
                publish_pattern = re.compile(r'publish\(["\']([^"\']+)["\']')
                for match in publish_pattern.finditer(content):
                    event_name = match.group(1)
                    if event_name not in events_published:
                        events_published.append(event_name)
                
                # Ищем subscribe
                subscribe_pattern = re.compile(r'subscribe\(["\']([^"\']+)["\']')
                for match in subscribe_pattern.finditer(content):
                    event_name = match.group(1)
                    if event_name not in events_subscribed:
                        events_subscribed.append(event_name)
                
                # Ищем зависимости
                try:
                    tree = ast.parse(content)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                dependencies.append(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                dependencies.append(node.module)
                except Exception:
                    pass
                
                # Определяем порядок инициализации
                init_order = None
                if module_name in initialization_order:
                    init_order = initialization_order.index(module_name)
                
                # Дополнительная проверка по событиям для audio_related
                if not audio_related:
                    for event_name in events_published + events_subscribed:
                        if any(prefix in event_name.lower() for prefix in self.audio_event_prefixes):
                            audio_related = True
                            break
                
                integrations.append(IntegrationInfo(
                    name=module_name,
                    path=str(py_file),
                    audio_related=audio_related,
                    dependencies=list(set(dependencies)),
                    events_published=events_published,
                    events_subscribed=events_subscribed,
                    initialization_order=init_order
                ))
            except Exception as e:
                print(f"⚠️ Ошибка анализа {py_file}: {e}")
        
        return integrations
    
    def _get_initialization_order(self) -> List[str]:
        """Получить порядок инициализации из SimpleModuleCoordinator"""
        coordinator_path = self.client_root / "integration" / "core" / "simple_module_coordinator.py"
        
        if not coordinator_path.exists():
            return []
        
        try:
            content = coordinator_path.read_text()
            # Ищем startup_order (может быть многострочным)
            order_match = re.search(r'startup_order\s*=\s*\[(.*?)\]', content, re.DOTALL)
            if order_match:
                order_str = order_match.group(1)
                # Извлекаем имена модулей (поддерживаем и ' и ")
                modules = re.findall(r"['\"]([^'\"]+)['\"]", order_str)
                # Убираем комментарии и пустые строки
                modules = [m.strip() for m in modules if m.strip() and not m.strip().startswith('#')]
                return modules
            
            # Альтернативный поиск: ищем строки с порядком
            lines = content.split('\n')
            in_startup_order = False
            modules = []
            for line in lines:
                if 'startup_order' in line and '=' in line:
                    in_startup_order = True
                if in_startup_order:
                    # Ищем строки с именами модулей
                    matches = re.findall(r"['\"]([^'\"]+)['\"]", line)
                    modules.extend(matches)
                    if ']' in line:
                        break
            return modules
        except Exception as e:
            print(f"⚠️ Ошибка чтения порядка инициализации: {e}")
        
        return []
    
    def _analyze_config(self) -> Dict[str, Any]:
        """Анализ конфигурации"""
        config = {}
        
        if not self.config_path.exists():
            return config
        
        try:
            with open(self.config_path, 'r') as f:
                config_data = yaml.safe_load(f)
            
            # Извлекаем аудио-связанные секции
            audio_sections = [
                "voice_recognition", "speech_playback", "input_processing",
                "permission_restart", "first_run_permissions", "default_audio"
            ]
            
            for section in audio_sections:
                if section in config_data:
                    config[section] = config_data[section]
            
            # Проверяем integrations секцию
            if "integrations" in config_data:
                for name, integration_config in config_data["integrations"].items():
                    if any(keyword in name.lower() for keyword in self.audio_related_keywords):
                        config[f"integrations.{name}"] = integration_config
        except Exception as e:
            print(f"⚠️ Ошибка чтения конфигурации: {e}")
        
        return config
    
    def _analyze_initialization_order(self) -> List[str]:
        """Анализ порядка инициализации"""
        return self._get_initialization_order()
    
    def _find_potential_conflicts(
        self,
        feature_flags: List[FeatureFlag],
        events: List[EventInfo],
        modules: List[ModuleInfo],
        integrations: List[IntegrationInfo]
    ) -> List[str]:
        """Поиск потенциальных конфликтов"""
        conflicts = []
        
        # 1. Проверка дублирования событий
        event_publishers = defaultdict(list)
        for event in events:
            if len(event.publishers) > 1:
                conflicts.append(
                    f"⚠️ Событие '{event.name}' публикуется несколькими компонентами: {', '.join(event.publishers)}"
                )
        
        # 2. Проверка отсутствующих feature flags в конфигурации
        for flag in feature_flags:
            if flag.config_path and "unified_config.yaml" in flag.config_path:
                # Проверяем наличие в конфигурации
                config_path = flag.config_path.split(":")[-1] if ":" in flag.config_path else flag.config_path
                if not self._check_config_path_exists(config_path):
                    conflicts.append(
                        f"⚠️ Feature flag '{flag.name}' указан в конфигурации, но путь '{config_path}' может отсутствовать"
                    )
        
        # 3. Проверка циклических зависимостей
        # (упрощенная проверка)
        for integration in integrations:
            for dep in integration.dependencies:
                if "integration" in dep.lower():
                    dep_name = dep.split(".")[-1].replace("_integration", "").replace("Integration", "")
                    # Проверяем обратную зависимость
                    for other_integration in integrations:
                        if other_integration.name == dep_name:
                            if integration.name in other_integration.dependencies:
                                conflicts.append(
                                    f"⚠️ Возможная циклическая зависимость между '{integration.name}' и '{dep_name}'"
                                )
        
        # 4. Проверка аудио-связанных модулей без feature flags
        audio_modules = [m for m in modules if m.audio_related]
        for module in audio_modules:
            # Проверяем, есть ли feature flags для этого модуля
            module_flags = [f for f in feature_flags if module.name.lower() in f.name.lower()]
            if not module_flags:
                conflicts.append(
                    f"ℹ️ Аудио-модуль '{module.name}' не имеет feature flags для управления"
                )
        
        return conflicts
    
    def _check_config_path_exists(self, config_path: str) -> bool:
        """Проверить существование пути в конфигурации"""
        if not self.config_path.exists():
            return False
        
        try:
            with open(self.config_path, 'r') as f:
                config_data = yaml.safe_load(f)
            
            # Очищаем путь от лишних символов и пробелов
            config_path = config_path.strip().strip('`').strip()
            
            # Убираем префикс "unified_config.yaml:" если есть
            if ":" in config_path:
                config_path = config_path.split(":", 1)[1].strip()
            
            # Разбираем путь (например, "permission_restart.enabled")
            parts = [p.strip() for p in config_path.split(".") if p.strip()]
            current = config_data
            
            for part in parts:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    return False
            
            return True
        except Exception:
            return False
    
    def _calculate_readiness(
        self,
        feature_flags: List[FeatureFlag],
        events: List[EventInfo],
        modules: List[ModuleInfo],
        integrations: List[IntegrationInfo],
        conflicts: List[str]
    ) -> tuple[float, List[str]]:
        """Рассчитать готовность к миграции"""
        score = 100.0
        recommendations = []
        
        # Штрафы за проблемы
        critical_conflicts = [c for c in conflicts if "⚠️" in c]
        info_conflicts = [c for c in conflicts if "ℹ️" in c]
        
        score -= len(critical_conflicts) * 5
        score -= len(info_conflicts) * 1
        
        # Проверка наличия необходимых feature flags
        required_flags = [
            "NEXY_FEATURE_AVFOUNDATION_AUDIO_V2",
            "NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2",
            "NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2",
            "NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2"
        ]
        
        existing_flag_names = [f.name for f in feature_flags]
        missing_flags = [f for f in required_flags if f not in existing_flag_names]
        
        if missing_flags:
            score -= len(missing_flags) * 10
            recommendations.append(
                f"❌ Отсутствуют необходимые feature flags: {', '.join(missing_flags)}"
            )
        
        # Проверка аудио-связанных интеграций
        audio_integrations = [i for i in integrations if i.audio_related]
        if len(audio_integrations) < 2:
            score -= 10
            recommendations.append("⚠️ Обнаружено менее 2 аудио-связанных интеграций")
        
        # Проверка событий
        audio_events = [e for e in events if any(kw in e.name.lower() for kw in self.audio_related_keywords)]
        if len(audio_events) < 5:
            score -= 5
            recommendations.append("⚠️ Обнаружено менее 5 аудио-связанных событий")
        
        # Рекомендации
        if score < 70:
            recommendations.append("🔴 Критический уровень готовности - требуется доработка")
        elif score < 85:
            recommendations.append("🟡 Средний уровень готовности - рекомендуется доработка")
        else:
            recommendations.append("🟢 Высокий уровень готовности - можно начинать миграцию")
        
        return max(0.0, min(100.0, score)), recommendations


def print_report(result: AnalysisResult):
    """Вывести отчет в консоль"""
    print("\n" + "="*80)
    print("📊 ОТЧЕТ О ГОТОВНОСТИ К МИГРАЦИИ АУДИОСИСТЕМЫ")
    print("="*80)
    
    print(f"\n🎯 Общая готовность: {result.readiness_score:.1f}%")
    
    print("\n📋 FEATURE FLAGS:")
    print("-" * 80)
    for flag in result.feature_flags:
        print(f"  • {flag.name} ({flag.type})")
        print(f"    Config: {flag.config_path}")
        print(f"    Locations: {', '.join(flag.code_locations[:3])}")
        if len(flag.code_locations) > 3:
            print(f"    ... и еще {len(flag.code_locations) - 3}")
    
    print("\n📡 СОБЫТИЯ EVENTBUS (аудио-связанные):")
    print("-" * 80)
    audio_keywords = ["voice", "audio", "mic", "playback", "recording", "speech", "sound", "device"]
    audio_events = [e for e in result.events if any(
        kw in e.name.lower() for kw in audio_keywords
    )]
    if not audio_events:
        print("  ⚠️ Аудио-связанные события не найдены")
    else:
        for event in audio_events[:20]:  # Показываем первые 20
            print(f"  • {event.name}")
            if event.publishers:
                print(f"    Публикуют: {', '.join(event.publishers)}")
            if event.subscribers:
                print(f"    Подписываются: {', '.join(event.subscribers[:5])}")
                if len(event.subscribers) > 5:
                    print(f"    ... и еще {len(event.subscribers) - 5}")
    
    print("\n🧩 МОДУЛИ (аудио-связанные):")
    print("-" * 80)
    audio_modules = [m for m in result.modules if m.audio_related]
    for module in audio_modules:
        print(f"  • {module.name}")
        print(f"    События: {len(module.events_published)} публикует, {len(module.events_subscribed)} подписывается")
    
    print("\n🔗 ИНТЕГРАЦИИ (аудио-связанные):")
    print("-" * 80)
    audio_integrations = [i for i in result.integrations if i.audio_related]
    for integration in sorted(audio_integrations, key=lambda x: x.initialization_order or 999):
        order_str = f"#{integration.initialization_order}" if integration.initialization_order is not None else "?"
        print(f"  • {integration.name} (порядок: {order_str})")
        print(f"    События: {len(integration.events_published)} публикует, {len(integration.events_subscribed)} подписывается")
    
    print("\n🔄 ПОРЯДОК ИНИЦИАЛИЗАЦИИ:")
    print("-" * 80)
    for i, module_name in enumerate(result.initialization_order, 1):
        marker = "🎤" if any(kw in module_name.lower() for kw in ["voice", "audio", "speech", "input"]) else "  "
        print(f"  {marker} {i}. {module_name}")
    
    print("\n⚠️ ПОТЕНЦИАЛЬНЫЕ КОНФЛИКТЫ:")
    print("-" * 80)
    if result.potential_conflicts:
        for conflict in result.potential_conflicts:
            print(f"  {conflict}")
    else:
        print("  ✅ Конфликтов не обнаружено")
    
    print("\n💡 РЕКОМЕНДАЦИИ:")
    print("-" * 80)
    for rec in result.recommendations:
        print(f"  {rec}")
    
    print("\n" + "="*80)


def save_json_report(result: AnalysisResult, output_path: str):
    """Сохранить отчет в JSON"""
    report = {
        "readiness_score": result.readiness_score,
        "feature_flags": [asdict(f) for f in result.feature_flags],
        "events": [asdict(e) for e in result.events],
        "modules": [asdict(m) for m in result.modules],
        "integrations": [asdict(i) for i in result.integrations],
        "config_entries": result.config_entries,
        "initialization_order": result.initialization_order,
        "potential_conflicts": result.potential_conflicts,
        "recommendations": result.recommendations
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Отчет сохранен в: {output_path}")


def main():
    """Главная функция"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Анализ готовности к миграции аудиосистемы"
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
        default="audio_migration_readiness_report.json",
        help="Путь для сохранения JSON отчета"
    )
    parser.add_argument(
        "--json-only",
        action="store_true",
        help="Только JSON отчет, без вывода в консоль"
    )
    
    args = parser.parse_args()
    
    analyzer = AudioMigrationAnalyzer(args.project_root)
    result = analyzer.analyze()
    
    if not args.json_only:
        print_report(result)
    
    save_json_report(result, args.output)
    
    # Exit code на основе готовности
    if result.readiness_score < 70:
        sys.exit(1)
    elif result.readiness_score < 85:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

