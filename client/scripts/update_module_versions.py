#!/usr/bin/env python3
"""
Обновление версий в Info.plist файлах модулей
Читает версию из unified_config.yaml и обновляет все модули
"""

from pathlib import Path
import re

import yaml


def get_version_from_config() -> str:
    """Получает версию из unified_config.yaml"""
    config_path = Path(__file__).parent.parent / "config" / "unified_config.yaml"
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['app']['version']


def update_plist_version(plist_path: Path, version: str) -> bool:
    """Обновляет версию в Info.plist файле"""
    if not plist_path.exists():
        print(f"⚠ Пропущен {plist_path}: файл не найден")
        return False

    with open(plist_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Обновляем CFBundleShortVersionString
    new_content = re.sub(
        r'(<key>CFBundleShortVersionString</key>\s*<string>)[^<]*(</string>)',
        rf'\g<1>{version}\g<2>',
        content
    )

    # Обновляем CFBundleVersion
    new_content = re.sub(
        r'(<key>CFBundleVersion</key>\s*<string>)[^<]*(</string>)',
        rf'\g<1>{version}\g<2>',
        new_content
    )

    if new_content == content:
        print(f"• {plist_path.name}: версия уже актуальна")
        return False

    with open(plist_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ {plist_path.name}: обновлено до {version}")
    return True


def update_python_version(init_path: Path, version: str) -> bool:
    """Обновляет __version__ в __init__.py файле"""
    if not init_path.exists():
        print(f"⚠ Пропущен {init_path}: файл не найден")
        return False

    with open(init_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Обновляем __version__
    new_content = re.sub(
        r'(__version__\s*=\s*["\'])[^"\']*(["\'])',
        rf'\g<1>{version}\g<2>',
        content
    )

    if new_content == content:
        print(f"• {init_path.parent.name}/{init_path.name}: версия уже актуальна")
        return False

    with open(init_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✓ {init_path.parent.name}/{init_path.name}: обновлено до {version}")
    return True


def main():
    """Главная функция"""
    # Получаем версию из конфига
    version = get_version_from_config()
    print(f"\nВерсия из unified_config.yaml: {version}\n")

    client_dir = Path(__file__).parent.parent

    # Список Info.plist файлов модулей
    plist_files = [
        client_dir / "modules/grpc_client/macos/info/Info.plist",
        client_dir / "modules/hardware_id/macos/info/Info.plist",
        client_dir / "modules/input_processing/macos/info/Info.plist",
    ]

    # Список __init__.py файлов с __version__
    python_init_files = [
        client_dir / "integration/__init__.py",
        client_dir / "integration/workflows/__init__.py",
        client_dir / "integration/integrations/__init__.py",
        client_dir / "modules/voice_recognition/__init__.py",
        client_dir / "modules/permissions/__init__.py",
        client_dir / "modules/mode_management/__init__.py",
        client_dir / "modules/speech_playback/__init__.py",
        client_dir / "modules/input_processing/__init__.py",
        client_dir / "modules/tray_controller/__init__.py",
        client_dir / "modules/screenshot_capture/__init__.py",
        client_dir / "modules/interrupt_management/__init__.py",
        client_dir / "modules/grpc_client/__init__.py",
        client_dir / "modules/welcome_message/__init__.py",
    ]

    # Обновляем Info.plist файлы
    print("=== Info.plist файлы ===")
    plist_updated = 0
    for plist_path in plist_files:
        if update_plist_version(plist_path, version):
            plist_updated += 1

    # Обновляем Python __init__.py файлы
    print("\n=== Python __init__.py файлы ===")
    python_updated = 0
    for init_path in python_init_files:
        if update_python_version(init_path, version):
            python_updated += 1

    print(f"\n{'='*50}")
    print(f"Обновлено Info.plist: {plist_updated}/{len(plist_files)}")
    print(f"Обновлено __init__.py: {python_updated}/{len(python_init_files)}")
    print(f"Всего обновлено: {plist_updated + python_updated}/{len(plist_files) + len(python_init_files)}")
    print(f"{'='*50}\n")


if __name__ == '__main__':
    main()
