#!/usr/bin/env python3
"""
Валидация Nexy.spec на полноту конфигурации.

Этот скрипт проверяет:
- Все модули из modules/ присутствуют в hiddenimports
- Все интеграции из integration/integrations/ присутствуют в hiddenimports
- PyObjC модули присутствуют в hiddenimports
- gRPC и protobuf присутствуют в hiddenimports
- Все необходимые ресурсы присутствуют в datas
- runtime_hooks настроены корректно
- Info.plist содержит обязательные ключи

Exit codes:
    0 - все проверки пройдены
    1 - есть отсутствующие imports/data/hooks
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SPEC_FILE = PROJECT_ROOT / "packaging" / "Nexy.spec"

# Ожидаемые интеграции в hiddenimports
EXPECTED_INTEGRATIONS = [
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

# Ожидаемые core модули
EXPECTED_CORE = [
    "integration.core",
    "integration.core.base_integration",
    "integration.core.error_handler",
    "integration.core.event_bus",
    "integration.core.event_utils",
    "integration.core.integration_factory",
    "integration.core.selectors",
    "integration.core.simple_module_coordinator",
    "integration.core.state_manager",
]

# Ожидаемые PyObjC модули
EXPECTED_PYOBJC = [
    "AppKit",
    "Foundation",
    "Quartz",
    "AVFoundation",
]

# Ожидаемые gRPC модули
EXPECTED_GRPC = [
    "grpc",
    "grpc.aio",
    "modules.grpc_client.proto.streaming_pb2",
    "modules.grpc_client.proto.streaming_pb2_grpc",
    "google.protobuf",
]

# Ожидаемые ресурсы в datas
EXPECTED_DATA_PATTERNS = [
    ("config", "config"),
    ("assets", "assets"),
    ("resources", "resources"),
    ("integration", "integration"),
]

# Ожидаемый runtime hook
EXPECTED_RUNTIME_HOOK = "packaging/runtime_hook_pyobjc_fix.py"

# Обязательные ключи Info.plist
# Примечание: CFBundleIdentifier может быть задан в bundle_identifier параметре BUNDLE
REQUIRED_INFO_PLIST_KEYS = [
    "CFBundleVersion",
    "CFBundleShortVersionString",
    "NSMicrophoneUsageDescription",
    "NSScreenCaptureUsageDescription",
    "NSAppleEventsUsageDescription",
    "NSAccessibilityUsageDescription",
    "NSContactsUsageDescription",
    "NSInputMonitoringUsageDescription",
    "NSFullDiskAccessUsageDescription",
    "LSUIElement",
]

# Дополнительная проверка bundle_identifier
REQUIRED_BUNDLE_IDENTIFIER = "bundle_identifier"


class CheckError(Exception):
    """Ошибка проверки."""


def parse_spec_file() -> dict[str, Any]:
    """Парсит Nexy.spec и извлекает конфигурацию."""
    if not SPEC_FILE.exists():
        raise CheckError(f"Файл {SPEC_FILE} не найден")
    
    with open(SPEC_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Извлекаем hiddenimports
    hiddenimports_match = re.search(
        r'hiddenimports=\[(.*?)\]', content, re.DOTALL
    )
    hiddenimports = []
    if hiddenimports_match:
        imports_text = hiddenimports_match.group(1)
        # Извлекаем строки в кавычках
        imports = re.findall(r'["\']([^"\']+)["\']', imports_text)
        hiddenimports = imports
    
    # Извлекаем datas
    datas_match = re.search(r'datas=\[(.*?)\]', content, re.DOTALL)
    datas = []
    if datas_match:
        datas_text = datas_match.group(1)
        # Извлекаем кортежи (source, dest) - учитываем многострочные кортежи
        # Ищем паттерн (str(...), "dest")
        tuple_pattern = r'\([^)]*(?:\([^)]*\)[^)]*)*\)'
        datas_tuples = re.findall(tuple_pattern, datas_text, re.DOTALL)
        for tuple_str in datas_tuples:
            # Извлекаем пути из кортежа
            # Может быть str(client_dir / "config") или просто "config"
            paths = re.findall(r'["\']([^"\']+)["\']', tuple_str)
            if len(paths) >= 2:
                # Берем последние два пути (source и dest)
                source = paths[-2] if len(paths) >= 2 else paths[0]
                dest = paths[-1]
                datas.append((source, dest))
            elif len(paths) == 1:
                # Если только один путь, это может быть dest, source вычисляется из контекста
                # Проверяем, есть ли в tuple_str упоминание config/assets/resources/integration
                for pattern in ["config", "assets", "resources", "integration"]:
                    if pattern in tuple_str.lower():
                        datas.append((pattern, paths[0]))
                        break
    
    # Извлекаем runtime_hooks
    runtime_hooks_match = re.search(
        r'runtime_hooks=\[(.*?)\]', content, re.DOTALL
    )
    runtime_hooks = []
    if runtime_hooks_match:
        hooks_text = runtime_hooks_match.group(1)
        hooks = re.findall(r'["\']([^"\']+)["\']', hooks_text)
        runtime_hooks = hooks
    
    # Извлекаем info_plist
    # Ищем info_plist={...} - может быть многострочным, нужно найти закрывающую скобку
    # Используем более сложный паттерн для поиска вложенных словарей
    info_plist_match = re.search(
        r'info_plist=\{(.*?)\n\s*\}', content, re.DOTALL
    )
    info_plist = {}
    if info_plist_match:
        plist_text = info_plist_match.group(1)
        # Проверяем наличие ключей через поиск
        # Ключи могут быть в формате "key": value или 'key': value
        for key in REQUIRED_INFO_PLIST_KEYS:
            # Ищем ключ в формате "key" или 'key' (может быть с двоеточием после)
            pattern = rf'["\']{re.escape(key)}["\']\s*:'
            if re.search(pattern, plist_text):
                info_plist[key] = True
    
    # Проверяем bundle_identifier в BUNDLE
    bundle_identifier_match = re.search(
        r'bundle_identifier\s*=\s*["\']([^"\']+)["\']', content
    )
    if bundle_identifier_match:
        info_plist["CFBundleIdentifier"] = True  # Считаем, что есть через bundle_identifier
    
    return {
        "hiddenimports": hiddenimports,
        "datas": datas,
        "runtime_hooks": runtime_hooks,
        "info_plist": info_plist,
        "content": content,
    }


def check_hidden_imports(config: dict[str, Any]) -> list[str]:
    """Проверяет полноту hiddenimports."""
    errors = []
    hiddenimports = set(config["hiddenimports"])
    
    # Проверка интеграций
    for integration in EXPECTED_INTEGRATIONS:
        if integration not in hiddenimports:
            errors.append(f"Отсутствует интеграция в hiddenimports: {integration}")
    
    # Проверка core модулей
    for core in EXPECTED_CORE:
        if core not in hiddenimports:
            errors.append(f"Отсутствует core модуль в hiddenimports: {core}")
    
    # Проверка PyObjC (хотя бы базовые)
    found_pyobjc = sum(1 for pyobjc in EXPECTED_PYOBJC if pyobjc in hiddenimports)
    if found_pyobjc < len(EXPECTED_PYOBJC):
        missing = [p for p in EXPECTED_PYOBJC if p not in hiddenimports]
        errors.append(f"Отсутствуют PyObjC модули в hiddenimports: {', '.join(missing)}")
    
    # Проверка gRPC (хотя бы базовые)
    found_grpc = sum(1 for grpc in EXPECTED_GRPC if grpc in hiddenimports)
    if found_grpc < 2:  # Минимум grpc и grpc.aio
        missing = [g for g in EXPECTED_GRPC[:2] if g not in hiddenimports]
        errors.append(f"Отсутствуют gRPC модули в hiddenimports: {', '.join(missing)}")
    
    return errors


def check_data_files(config: dict[str, Any]) -> list[str]:
    """Проверяет наличие необходимых ресурсов в datas."""
    errors = []
    datas = config["datas"]
    
    # Проверяем наличие ожидаемых паттернов
    for source_pattern, dest_pattern in EXPECTED_DATA_PATTERNS:
        found = False
        for source, dest in datas:
            if source_pattern in source and dest_pattern in dest:
                found = True
                break
        if not found:
            errors.append(
                f"Отсутствует ресурс в datas: {source_pattern} -> {dest_pattern}"
            )
    
    return errors


def check_runtime_hooks(config: dict[str, Any]) -> list[str]:
    """Проверяет наличие runtime hooks."""
    errors = []
    runtime_hooks = config["runtime_hooks"]
    
    if EXPECTED_RUNTIME_HOOK not in runtime_hooks:
        # Проверяем, есть ли хотя бы часть пути
        found = any(EXPECTED_RUNTIME_HOOK.rsplit("/", maxsplit=1)[-1] in hook for hook in runtime_hooks)
        if not found:
            errors.append(f"Отсутствует runtime hook: {EXPECTED_RUNTIME_HOOK}")
    
    return errors


def check_info_plist(config: dict[str, Any]) -> list[str]:
    """Проверяет наличие обязательных ключей в Info.plist."""
    errors = []
    info_plist = config["info_plist"]
    
    for key in REQUIRED_INFO_PLIST_KEYS:
        if key not in info_plist:
            errors.append(f"Отсутствует обязательный ключ в info_plist: {key}")
    
    return errors


def main() -> int:
    """Главная функция."""
    print("🔍 Валидация Nexy.spec...")
    print()
    
    try:
        config = parse_spec_file()
    except CheckError as e:
        print(f"❌ Ошибка чтения spec файла: {e}")
        return 1
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {type(e).__name__}: {e}")
        return 1
    
    all_errors = []
    all_warnings = []
    
    # 1. Проверка hiddenimports
    print("1. Проверка hiddenimports...")
    import_errors = check_hidden_imports(config)
    if import_errors:
        all_errors.extend(import_errors)
        for err in import_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все необходимые модули присутствуют в hiddenimports ({len(config['hiddenimports'])} модулей)")
    print()
    
    # 2. Проверка datas
    print("2. Проверка datas...")
    data_errors = check_data_files(config)
    if data_errors:
        all_errors.extend(data_errors)
        for err in data_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все необходимые ресурсы присутствуют в datas ({len(config['datas'])} ресурсов)")
    print()
    
    # 3. Проверка runtime_hooks
    print("3. Проверка runtime_hooks...")
    hook_errors = check_runtime_hooks(config)
    if hook_errors:
        all_errors.extend(hook_errors)
        for err in hook_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Runtime hooks настроены корректно ({len(config['runtime_hooks'])} hooks)")
    print()
    
    # 4. Проверка info_plist
    print("4. Проверка info_plist...")
    plist_errors = check_info_plist(config)
    if plist_errors:
        all_errors.extend(plist_errors)
        for err in plist_errors:
            print(f"   ❌ {err}")
    else:
        print(f"   ✅ Все обязательные ключи присутствуют в info_plist ({len(config['info_plist'])} ключей)")
    print()

    # 5. Playwright driver hints (warning-only)
    print("5. Проверка Playwright driver (warning-only)...")
    content = config.get("content", "")
    if "playwright/driver" not in content:
        all_warnings.append("Playwright driver не упомянут в Nexy.spec (playwright/driver)")
        print("   ⚠ Playwright driver не упомянут в Nexy.spec (playwright/driver)")
    else:
        print("   ✅ Nexy.spec содержит упоминание playwright/driver")
    print()
    
    # Итоги
    if all_errors:
        print("❌ Валидация завершена с ошибками:")
        print()
        for err in all_errors:
            print(f"   - {err}")
        return 1

    if all_warnings:
        print("⚠ Валидация завершена с предупреждениями:")
        for warn_msg in all_warnings:
            print(f"   - {warn_msg}")
        print()

    print("✅ Все проверки пройдены успешно!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
