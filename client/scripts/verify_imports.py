#!/usr/bin/env python3
"""
Проверка синтаксиса Python и критических импортов перед упаковкой.

Этот скрипт проверяет (14 проверок):
1. Синтаксис всех критических .py файлов
2. Существование критических ресурсов (ffmpeg, flac, icons)
3. Существование конфигурационных файлов
4. Существование packaging файлов (Nexy.spec, entitlements.plist, etc.)
5. Импорт core компонентов
6. Импорт gateways (9 модулей)
7. Импорт workflows (4 модуля)
8. Импорт модулей из modules/ (20 модулей)
9. Импорт интеграций (21 интеграция)
10. Импорт PyObjC модулей
11. Импорт utils (4 модуля)
12. Доступность системных инструментов (codesign, xcrun, pkgbuild и т.д.)
13. Права на исполнение бинарников (ffmpeg, flac)
14. Proto файлы и pb2.py

Exit codes:
    0 - все проверки пройдены
    1 - есть ошибки синтаксиса, импортов или отсутствуют файлы
"""

from __future__ import annotations

import ast
import py_compile
import sys
from pathlib import Path
from typing import List, Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Добавляем пути к PYTHONPATH (как в main.py)
CLIENT_ROOT = PROJECT_ROOT
ROOT_DIR = CLIENT_ROOT.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))            # Для доступа к корневому 'integration'
if str(CLIENT_ROOT) not in sys.path:
    sys.path.insert(0, str(CLIENT_ROOT))         # Для доступа к локальным модулям
if str(CLIENT_ROOT / "modules") not in sys.path:
    sys.path.insert(0, str(CLIENT_ROOT / "modules"))

# Критические файлы для проверки синтаксиса
CRITICAL_FILES = [
    "main.py",
    "integration/core/simple_module_coordinator.py",
    "integration/core/event_bus.py",
    "integration/core/state_manager.py",
    "integration/core/error_handler.py",
]

# Core компоненты для проверки импорта
CORE_IMPORTS = [
    "integration.core.event_bus",
    "integration.core.state_manager",
    "integration.core.error_handler",
    "integration.core.simple_module_coordinator",
]

# Все интеграции (21 штука)
INTEGRATIONS = [
    "integration.integrations.action_execution_integration",
    "integration.integrations.autostart_manager_integration",
    "integration.integrations.first_run_permissions_integration",
    "integration.integrations.grpc_client_integration",
    "integration.integrations.hardware_id_integration",
    "integration.integrations.input_processing_integration",
    "integration.integrations.instance_manager_integration",
    "integration.integrations.interrupt_management_integration",
    "integration.integrations.mode_management_integration",
    "integration.integrations.network_manager_integration",
    "integration.integrations.permission_restart_integration",
    "integration.integrations.screenshot_capture_integration",
    "integration.integrations.signal_integration",
    "integration.integrations.speech_playback_integration",
    "integration.integrations.tray_controller_integration",
    "integration.integrations.tts_integration",
    "integration.integrations.update_notification_integration",
    "integration.integrations.updater_integration",
    "integration.integrations.voice_recognition_integration",
    "integration.integrations.voiceover_ducking_integration",
    "integration.integrations.welcome_message_integration",
]

# Модули из modules/ (21 модуль)
MODULES = [
    "modules.action_errors",
    "modules.autostart_manager",
    "modules.grpc_client",
    "modules.hardware_id",
    "modules.input_processing",
    "modules.instance_manager",
    "modules.interrupt_management",
    "modules.mcp_action",
    "modules.mode_management",
    "modules.network_manager",
    "modules.permission_restart",
    "modules.permissions",
    "modules.screenshot_capture",
    "modules.signals",
    "modules.speech_playback",
    "modules.tray_controller",
    "modules.updater",
    "modules.voice_recognition",
    "modules.voiceover_control",
    "modules.welcome_message",
]

# Workflows
WORKFLOWS = [
    "integration.workflows.base_workflow",
    "integration.workflows.listening_workflow",
    "integration.workflows.processing_workflow",
    "integration.workflows.workflow_config",
]

# Gateways (все модули)
GATEWAYS = [
    "integration.core.gateways",
    "integration.core.gateways.base",
    "integration.core.gateways.common",
    "integration.core.gateways.decision_engine",
    "integration.core.gateways.engine_loader",
    "integration.core.gateways.permission_gateways",
    "integration.core.gateways.predicates",
    "integration.core.gateways.rule_loader",
    "integration.core.gateways.types",
]

# Utils
UTILS = [
    "integration.utils",
    "integration.utils.logging_setup",
    "integration.utils.macos_pyobjc_fix",
    "integration.utils.resource_path",
]

# Системные инструменты (должны быть доступны)
SYSTEM_TOOLS = [
    "codesign",
    "xcrun",
    "pkgbuild",
    "productbuild",
    "lipo",
    "python3",
]

# Критические файлы ресурсов (должны существовать)
CRITICAL_RESOURCES = [
    "resources/ffmpeg/ffmpeg",
    "resources/audio/flac",
    "resources/audio/SwitchAudioSource",
    "assets/icons/app_icon.icns",
]

# Бинарники которые должны иметь права на исполнение
EXECUTABLE_BINARIES = [
    "resources/ffmpeg/ffmpeg",
    "resources/audio/flac",
    "resources/audio/SwitchAudioSource",
]

# Критические конфигурационные файлы
CRITICAL_CONFIGS = [
    "config/unified_config.yaml",
    "config/interaction_matrix.yaml",
    "config/tray_config.yaml",
]

# Критические packaging файлы
CRITICAL_PACKAGING = [
    "packaging/Nexy.spec",
    "packaging/entitlements.plist",
    "packaging/runtime_hook_pyobjc_fix.py",
    "packaging/distribution.xml",
    "client/VERSION_INFO.json",
]

# PyObjC модули для проверки
PYOBJC_IMPORTS = [
    "AppKit",
    "Foundation",
    "Quartz",
    "AVFoundation",
]


class CheckError(Exception):
    """Ошибка проверки."""


def check_syntax(file_path: Path) -> Tuple[bool, str]:
    """
    Проверяет синтаксис Python файла.
    
    Returns:
        (success, error_message)
    """
    try:
        # Проверяем синтаксис через py_compile
        py_compile.compile(str(file_path), doraise=True)
        
        # Дополнительная проверка через AST
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        ast.parse(source, filename=str(file_path))
        
        return True, ""
    except py_compile.PyCompileError as e:
        return False, f"PyCompileError: {e}"
    except SyntaxError as e:
        return False, f"SyntaxError: {e.filename}:{e.lineno}: {e.msg}"
    except Exception as e:
        return False, f"Unexpected error: {type(e).__name__}: {e}"


def check_import(module_name: str) -> Tuple[bool, str]:
    """
    Проверяет возможность импорта модуля.
    
    Returns:
        (success, error_message)
    """
    try:
        __import__(module_name)
        return True, ""
    except ImportError as e:
        return False, f"ImportError: {e}"
    except SyntaxError as e:
        return False, f"SyntaxError in {module_name}: {e.filename}:{e.lineno}: {e.msg}"
    except Exception as e:
        return False, f"Unexpected error importing {module_name}: {type(e).__name__}: {e}"


def check_all_syntax() -> List[str]:
    """Проверяет синтаксис всех критических файлов."""
    errors = []
    
    for rel_path in CRITICAL_FILES:
        file_path = PROJECT_ROOT / rel_path
        if not file_path.exists():
            errors.append(f"{rel_path}: файл не найден")
            continue
        
        success, error_msg = check_syntax(file_path)
        if not success:
            errors.append(f"{rel_path}: {error_msg}")
    
    return errors


def check_all_integrations() -> List[str]:
    """Проверяет импорт всех интеграций."""
    errors = []
    
    for integration in INTEGRATIONS:
        success, error_msg = check_import(integration)
        if not success:
            errors.append(f"{integration}: {error_msg}")
    
    return errors


def check_core_imports() -> List[str]:
    """Проверяет импорт core компонентов."""
    errors = []
    
    for module in CORE_IMPORTS:
        success, error_msg = check_import(module)
        if not success:
            errors.append(f"{module}: {error_msg}")
    
    return errors


def check_pyobjc_imports() -> List[str]:
    """Проверяет импорт PyObjC модулей."""
    errors = []
    
    for module in PYOBJC_IMPORTS:
        success, error_msg = check_import(module)
        if not success:
            errors.append(f"{module}: {error_msg}")
    
    return errors


def check_all_modules() -> List[str]:
    """Проверяет импорт всех модулей из modules/."""
    errors = []
    
    for module in MODULES:
        success, error_msg = check_import(module)
        if not success:
            errors.append(f"{module}: {error_msg}")
    
    return errors


def check_all_workflows() -> List[str]:
    """Проверяет импорт всех workflows."""
    errors = []
    
    for workflow in WORKFLOWS:
        success, error_msg = check_import(workflow)
        if not success:
            errors.append(f"{workflow}: {error_msg}")
    
    return errors


def check_all_gateways() -> List[str]:
    """Проверяет импорт всех gateways."""
    errors = []
    
    for gateway in GATEWAYS:
        success, error_msg = check_import(gateway)
        if not success:
            errors.append(f"{gateway}: {error_msg}")
    
    return errors


def check_resources_exist() -> List[str]:
    """Проверяет существование критических ресурсов."""
    errors = []
    
    for resource in CRITICAL_RESOURCES:
        resource_path = PROJECT_ROOT / resource
        if not resource_path.exists():
            errors.append(f"{resource}: файл не найден")
    
    return errors


def check_configs_exist() -> List[str]:
    """Проверяет существование критических конфигурационных файлов."""
    errors = []
    
    for config in CRITICAL_CONFIGS:
        config_path = PROJECT_ROOT / config
        if not config_path.exists():
            errors.append(f"{config}: файл не найден")
    
    return errors


def check_packaging_files() -> List[str]:
    """Проверяет существование критических packaging файлов."""
    errors = []
    
    for pkg_file in CRITICAL_PACKAGING:
        pkg_path = PROJECT_ROOT / pkg_file
        if not pkg_path.exists():
            errors.append(f"{pkg_file}: файл не найден")
    
    return errors


def check_all_utils() -> List[str]:
    """Проверяет импорт всех utils."""
    errors = []
    
    for util in UTILS:
        success, error_msg = check_import(util)
        if not success:
            errors.append(f"{util}: {error_msg}")
    
    return errors


def check_system_tools() -> List[str]:
    """Проверяет доступность системных инструментов."""
    import shutil
    errors = []
    
    for tool in SYSTEM_TOOLS:
        if shutil.which(tool) is None:
            errors.append(f"{tool}: не найден в PATH")
    
    return errors


def check_binary_permissions() -> List[str]:
    """Проверяет права доступа на исполнение бинарников."""
    import os
    errors = []
    
    for binary in EXECUTABLE_BINARIES:
        binary_path = PROJECT_ROOT / binary
        if binary_path.exists():
            if not os.access(binary_path, os.X_OK):
                errors.append(f"{binary}: нет прав на исполнение (chmod +x)")
    
    return errors


def check_proto_files() -> List[str]:
    """Проверяет существование proto файлов и pb2.py."""
    errors = []
    
    proto_dir = PROJECT_ROOT / "modules" / "grpc_client" / "proto"
    
    # Проверяем существование proto файла
    proto_file = proto_dir / "streaming.proto"
    if not proto_file.exists():
        errors.append(f"modules/grpc_client/proto/streaming.proto: файл не найден")
        return errors
    
    # Проверяем существование сгенерированных pb2 файлов
    pb2_file = proto_dir / "streaming_pb2.py"
    pb2_grpc_file = proto_dir / "streaming_pb2_grpc.py"
    
    if not pb2_file.exists():
        errors.append(f"modules/grpc_client/proto/streaming_pb2.py: не найден (запустите scripts/regenerate_proto.sh)")
    if not pb2_grpc_file.exists():
        errors.append(f"modules/grpc_client/proto/streaming_pb2_grpc.py: не найден (запустите scripts/regenerate_proto.sh)")
    
    return errors


def main() -> int:
    """Главная функция."""
    print("🔍 Проверка синтаксиса и импортов...")
    print()
    
    all_errors = []
    check_num = 0
    
    # 1. Проверка синтаксиса
    check_num += 1
    print(f"{check_num}. Проверка синтаксиса критических файлов...")
    syntax_errors = check_all_syntax()
    if syntax_errors:
        all_errors.extend(syntax_errors)
        for err in syntax_errors:
            print(f"   ❌ {err}")
    else:
        print("   ✅ Синтаксис всех файлов корректен")
    print()
    
    # 2. Проверка существования ресурсов
    check_num += 1
    print(f"{check_num}. Проверка существования критических ресурсов...")
    resource_errors = check_resources_exist()
    if resource_errors:
        all_errors.extend(resource_errors)
        for err in resource_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(CRITICAL_RESOURCES)} ресурсов найдены")
    print()
    
    # 3. Проверка существования конфигов
    check_num += 1
    print(f"{check_num}. Проверка существования конфигурационных файлов...")
    config_errors = check_configs_exist()
    if config_errors:
        all_errors.extend(config_errors)
        for err in config_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(CRITICAL_CONFIGS)} конфигурационных файлов найдены")
    print()
    
    # 4. Проверка существования packaging файлов
    check_num += 1
    print(f"{check_num}. Проверка существования packaging файлов...")
    packaging_errors = check_packaging_files()
    if packaging_errors:
        all_errors.extend(packaging_errors)
        for err in packaging_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(CRITICAL_PACKAGING)} packaging файлов найдены")
    print()
    
    # 5. Проверка core импортов
    check_num += 1
    print(f"{check_num}. Проверка импорта core компонентов...")
    core_errors = check_core_imports()
    if core_errors:
        all_errors.extend(core_errors)
        for err in core_errors:
            print(f"   ❌ {err}")
    else:
        print("   ✅ Все core компоненты импортируются")
    print()
    
    # 6. Проверка gateways
    check_num += 1
    print(f"{check_num}. Проверка импорта gateways...")
    gateway_errors = check_all_gateways()
    if gateway_errors:
        all_errors.extend(gateway_errors)
        for err in gateway_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(GATEWAYS)} gateways импортируются")
    print()
    
    # 7. Проверка workflows
    check_num += 1
    print(f"{check_num}. Проверка импорта workflows...")
    workflow_errors = check_all_workflows()
    if workflow_errors:
        all_errors.extend(workflow_errors)
        for err in workflow_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(WORKFLOWS)} workflows импортируются")
    print()
    
    # 8. Проверка модулей
    check_num += 1
    print(f"{check_num}. Проверка импорта модулей...")
    module_errors = check_all_modules()
    if module_errors:
        all_errors.extend(module_errors)
        for err in module_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(MODULES)} модулей импортируются")
    print()
    
    # 9. Проверка интеграций
    check_num += 1
    print(f"{check_num}. Проверка импорта интеграций...")
    integration_errors = check_all_integrations()
    if integration_errors:
        all_errors.extend(integration_errors)
        for err in integration_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(INTEGRATIONS)} интеграций импортируются")
    print()
    
    # 10. Проверка PyObjC
    check_num += 1
    print(f"{check_num}. Проверка импорта PyObjC модулей...")
    pyobjc_errors = check_pyobjc_imports()
    if pyobjc_errors:
        all_errors.extend(pyobjc_errors)
        for err in pyobjc_errors:
            print(f"   ❌ {err}")
    else:
        print("   ✅ Все PyObjC модули импортируются")
    print()
    
    # 11. Проверка utils
    check_num += 1
    print(f"{check_num}. Проверка импорта utils...")
    utils_errors = check_all_utils()
    if utils_errors:
        all_errors.extend(utils_errors)
        for err in utils_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(UTILS)} utils импортируются")
    print()
    
    # 12. Проверка системных инструментов
    check_num += 1
    print(f"{check_num}. Проверка системных инструментов...")
    tools_errors = check_system_tools()
    if tools_errors:
        all_errors.extend(tools_errors)
        for err in tools_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все {len(SYSTEM_TOOLS)} системных инструментов доступны")
    print()
    
    # 13. Проверка прав на бинарники
    check_num += 1
    print(f"{check_num}. Проверка прав на исполнение бинарников...")
    perm_errors = check_binary_permissions()
    if perm_errors:
        all_errors.extend(perm_errors)
        for err in perm_errors:
            print(f"   ❌ {err}")
    else:
        print("   ✅ Все бинарники имеют права на исполнение")
    print()
    
    # 14. Проверка proto файлов
    check_num += 1
    print(f"{check_num}. Проверка proto файлов...")
    proto_errors = check_proto_files()
    if proto_errors:
        all_errors.extend(proto_errors)
        for err in proto_errors:
            print(f"   ❌ {err}")
    else:
        print("   ✅ Все proto файлы и pb2.py найдены")
    print()
    
    # Итоги
    if all_errors:
        print("❌ Проверка завершена с ошибками:")
        print()
        for err in all_errors:
            print(f"   - {err}")
        return 1
    
    print("✅ Все проверки пройдены успешно!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
