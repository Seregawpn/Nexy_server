#!/usr/bin/env python3
"""
Централизованное управление версией сервера

Использование:
    python scripts/update_version.py 1.6.0.36
    
    или для чтения текущей версии:
    python scripts/update_version.py --read
"""
import sys
import os
import re
import json
from pathlib import Path
from datetime import datetime, timezone

# Путь к корню проекта
PROJECT_ROOT = Path(__file__).parent.parent.parent
VERSION_FILE = PROJECT_ROOT / "VERSION"
SERVER_ROOT = PROJECT_ROOT / "server"

def read_version() -> str:
    """Читает версию из VERSION файла"""
    if not VERSION_FILE.exists():
        raise FileNotFoundError(f"VERSION файл не найден: {VERSION_FILE}")
    
    version = VERSION_FILE.read_text().strip()
    if not re.match(r'^\d+\.\d+\.\d+\.\d+$', version):
        raise ValueError(f"Неверный формат версии: {version}. Ожидается формат: X.Y.Z.W")
    
    return version

def write_version(version: str):
    """Записывает версию в VERSION файл"""
    if not re.match(r'^\d+\.\d+\.\d+\.\d+$', version):
        raise ValueError(f"Неверный формат версии: {version}. Ожидается формат: X.Y.Z.W")
    
    VERSION_FILE.write_text(f"{version}\n")
    print(f"✅ Версия {version} записана в {VERSION_FILE}")

def update_unified_config_yaml(version: str):
    """Обновляет unified_config.yaml"""
    yaml_file = SERVER_ROOT / "config" / "unified_config.yaml"
    
    if not yaml_file.exists():
        print(f"⚠️ Файл не найден: {yaml_file}")
        return
    
    content = yaml_file.read_text()
    
    # Обновляем default_version и default_build
    content = re.sub(
        r'default_version:\s*[\d.]+',
        f'default_version: {version}',
        content
    )
    content = re.sub(
        r'default_build:\s*[\d.]+',
        f'default_build: {version}',
        content
    )
    
    # Обновляем server.version и server.build
    content = re.sub(
        r'version:\s*[\d.]+',
        f'version: {version}',
        content
    )
    content = re.sub(
        r'build:\s*[\d.]+',
        f'build: {version}',
        content
    )
    
    yaml_file.write_text(content)
    print(f"✅ Обновлен {yaml_file}")

def update_unified_config_py(version: str):
    """Обновляет unified_config.py"""
    py_file = SERVER_ROOT / "config" / "unified_config.py"
    
    if not py_file.exists():
        print(f"⚠️ Файл не найден: {py_file}")
        return
    
    content = py_file.read_text()
    
    # Обновляем дефолтные значения в UpdateServiceConfig
    content = re.sub(
        r"default_version:\s*str\s*=\s*'[\d.]+'",
        f"default_version: str = '{version}'",
        content
    )
    content = re.sub(
        r"default_build:\s*str\s*=\s*'[\d.]+'",
        f"default_build: str = '{version}'",
        content
    )
    
    # Обновляем в from_env методе
    content = re.sub(
        r"os\.getenv\('SERVER_VERSION',\s*'[\d.]+'\)",
        f"os.getenv('SERVER_VERSION', '{version}')",
        content
    )
    content = re.sub(
        r"os\.getenv\('SERVER_BUILD',\s*os\.getenv\('SERVER_VERSION',\s*'[\d.]+'\)\)",
        f"os.getenv('SERVER_BUILD', os.getenv('SERVER_VERSION', '{version}'))",
        content
    )
    
    # Обновляем ServerMetadataConfig
    content = re.sub(
        r"version:\s*str\s*=\s*'[\d.]+'",
        f"version: str = '{version}'",
        content
    )
    content = re.sub(
        r"build:\s*str\s*=\s*'[\d.]+'",
        f"build: str = '{version}'",
        content
    )
    
    py_file.write_text(content)
    print(f"✅ Обновлен {py_file}")

def update_config_env_example(version: str):
    """Обновляет config.env.example"""
    env_file = SERVER_ROOT / "config.env.example"
    
    if not env_file.exists():
        print(f"⚠️ Файл не найден: {env_file}")
        return
    
    content = env_file.read_text()
    
    # Обновляем SERVER_VERSION и SERVER_BUILD
    content = re.sub(
        r'SERVER_VERSION=[\d.]+',
        f'SERVER_VERSION={version}',
        content
    )
    content = re.sub(
        r'SERVER_BUILD=[\d.]+',
        f'SERVER_BUILD={version}',
        content
    )
    
    env_file.write_text(content)
    print(f"✅ Обновлен {env_file}")

def update_server_manifest(version: str, server_ip: str = None):
    """Обновляет манифест на сервере (требует Azure CLI)"""
    if not server_ip:
        print("⚠️ IP сервера не указан, пропускаем обновление манифеста на сервере")
        return
    
    print(f"📤 Обновление манифеста на сервере {server_ip}...")
    
    # Создаем Python скрипт для выполнения на сервере
    script = f"""
import json
from datetime import datetime, timezone
from pathlib import Path

manifest_file = Path('updates/manifests/manifest.json')
new_version = '{version}'
new_build = '{version}'
new_ip = '{server_ip}'

if manifest_file.exists():
    with open(manifest_file, 'r') as f:
        manifest = json.load(f)
else:
    manifest = {{'version': '1.0.0', 'build': '1.0.0', 'artifact': {{'type': 'dmg', 'url': '', 'size': 0, 'sha256': '', 'arch': 'universal2', 'min_os': '11.0', 'ed25519': ''}}}}

manifest['version'] = new_version
manifest['build'] = new_build
manifest['release_date'] = datetime.now(timezone.utc).isoformat()

if 'artifact' in manifest and 'url' in manifest['artifact']:
    manifest['artifact']['url'] = f'https://{{new_ip}}/updates/appcast.xml'
if 'notes_url' in manifest:
    manifest['notes_url'] = f'https://{{new_ip}}/updates/appcast.xml'

with open(manifest_file, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f'✅ Манифест обновлен: version={{new_version}}, build={{new_build}}')
"""
    
    # Выполняем через Azure CLI
    import subprocess
    result = subprocess.run(
        [
            "az", "vm", "run-command", "invoke",
            "--resource-group", "NetworkWatcherRG",
            "--name", "Nexy",
            "--command-id", "RunShellScript",
            "--scripts", f"cd /home/azureuser/voice-assistant/server && python3 << 'PYEOF'\n{script}\nPYEOF"
        ],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print(f"✅ Манифест на сервере обновлен")
    else:
        print(f"⚠️ Не удалось обновить манифест на сервере: {result.stderr}")

def main():
    """Основная функция"""
    if len(sys.argv) > 1 and sys.argv[1] == "--read":
        # Режим чтения
        try:
            version = read_version()
            print(f"Текущая версия: {version}")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Ошибка: {e}")
            sys.exit(1)
    
    if len(sys.argv) < 2:
        print("Использование:")
        print("  python scripts/update_version.py <version>")
        print("  python scripts/update_version.py --read")
        print()
        print("Пример:")
        print("  python scripts/update_version.py 1.6.0.36")
        sys.exit(1)
    
    new_version = sys.argv[1]
    
    # Валидация версии
    if not re.match(r'^\d+\.\d+\.\d+\.\d+$', new_version):
        print(f"❌ Неверный формат версии: {new_version}")
        print("Ожидается формат: X.Y.Z.W (например, 1.6.0.36)")
        sys.exit(1)
    
    print(f"🔄 Обновление версии до {new_version}...")
    print()
    
    try:
        # Обновляем VERSION файл
        write_version(new_version)
        
        # Обновляем конфигурационные файлы
        update_unified_config_yaml(new_version)
        update_unified_config_py(new_version)
        update_config_env_example(new_version)
        
        print()
        print("=" * 60)
        print(f"✅ Версия успешно обновлена до {new_version}")
        print("=" * 60)
        print()
        print("📋 Следующие шаги:")
        print("1. Проверьте изменения: git diff")
        print("2. Закоммитьте изменения: git add -A && git commit -m 'Update version to {new_version}'")
        print("3. Создайте тег: git tag {new_version} -m 'Release {new_version}'")
        print("4. Отправьте на GitHub: git push origin main && git push origin {new_version}")
        print("5. Обновите сервер: скрипт обновит манифест автоматически при деплое")
        print()
        
        # Опционально: обновить манифест на сервере
        server_ip = os.getenv("SERVER_IP", "nexy-server.canadacentral.cloudapp.azure.com")
        update_remote = os.getenv("UPDATE_REMOTE_MANIFEST", "false").lower() == "true"
        
        if update_remote:
            update_server_manifest(new_version, server_ip)
        
    except Exception as e:
        print(f"❌ Ошибка при обновлении версии: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
