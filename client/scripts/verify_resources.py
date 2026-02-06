#!/usr/bin/env python3
"""
verify_resources.py — Preflight проверки ресурсов

Проверяет:
1. Наличие критических ресурсов (иконки, звуки, сертификаты)
2. Валидность файлов (не пустые, правильный формат)
3. Universal бинарники для macOS
"""

import os
import struct
import sys

# Цвета для вывода
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
NC = "\033[0m"


class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.errors = []

    def ok(self, name: str):
        self.passed += 1
        print(f"  {GREEN}✓{NC} {name}")

    def warn(self, name: str, reason: str):
        self.warnings += 1
        print(f"  {YELLOW}⚠{NC} {name}: {reason}")

    def fail(self, name: str, reason: str):
        self.failed += 1
        self.errors.append(f"{name}: {reason}")
        print(f"  {RED}✗{NC} {name}: {reason}")

    def summary(self) -> bool:
        total = self.passed + self.failed
        if self.failed == 0:
            msg = f"Все {total} проверок пройдены"
            if self.warnings > 0:
                msg += f" ({self.warnings} предупреждений)"
            print(f"\n{GREEN}✅ {msg}{NC}")
            return True
        else:
            print(f"\n{RED}❌ Провалено {self.failed} из {total} проверок{NC}")
            for err in self.errors:
                print(f"   • {err}")
            return False


def get_client_dir() -> str:
    """Получить путь к client директории."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)


def check_file_exists(result: TestResult, path: str, name: str, required: bool = True):
    """Проверить существование файла."""
    if os.path.exists(path):
        size = os.path.getsize(path)
        if size == 0:
            result.fail(name, f"Пустой файл: {os.path.basename(path)}")
        else:
            size_kb = size / 1024
            result.ok(f"{name} ({size_kb:.1f} KB)")
        return True
    else:
        if required:
            result.fail(name, f"Не найден: {os.path.basename(path)}")
        else:
            result.warn(name, f"Не найден: {os.path.basename(path)}")
        return False


def test_icons(result: TestResult, client_dir: str):
    """Проверка иконок приложения."""
    # Иконки могут быть в разных местах
    icons = [
        ("assets/icons/app.icns", True),       # Основная иконка
        ("assets/icons/app_icon.icns", False), # Альтернативная
        ("assets/logo.icns", False),           # Лого
        ("resources/tray_icon.png", False),    # Иконка трея
    ]
    
    for icon_rel_path, required in icons:
        path = os.path.join(client_dir, icon_rel_path)
        check_file_exists(result, path, f"Иконка {os.path.basename(icon_rel_path)}", required)


def test_sounds(result: TestResult, client_dir: str):
    """Проверка звуковых файлов."""
    sounds_dir = os.path.join(client_dir, "resources", "sounds")
    
    if not os.path.exists(sounds_dir):
        result.warn("Директория sounds", "Не найдена")
        return
    
    # Ищем звуковые файлы
    sound_extensions = (".mp3", ".wav", ".aiff", ".m4a")
    sounds_found = 0
    
    for file in os.listdir(sounds_dir):
        if file.lower().endswith(sound_extensions):
            sounds_found += 1
            path = os.path.join(sounds_dir, file)
            size = os.path.getsize(path)
            if size == 0:
                result.warn(f"Звук {file}", "Пустой файл")
    
    if sounds_found > 0:
        result.ok(f"Найдено {sounds_found} звуковых файлов")
    else:
        result.warn("Звуки", "Звуковые файлы не найдены")


def test_certificates(result: TestResult, client_dir: str):
    """Проверка SSL сертификатов."""
    certs_dir = os.path.join(client_dir, "resources", "certs")
    
    if not os.path.exists(certs_dir):
        result.warn("Директория certs", "Не найдена")
        return
    
    # Ищем .pem файлы
    pem_files = [f for f in os.listdir(certs_dir) if f.endswith(".pem")]
    
    if pem_files:
        for pem in pem_files:
            path = os.path.join(certs_dir, pem)
            check_file_exists(result, path, f"Сертификат {pem}", required=False)
    else:
        result.warn("Сертификаты", "PEM файлы не найдены")


def is_universal_binary(path: str) -> tuple[bool, str]:
    """Проверить является ли бинарник Universal (arm64 + x86_64)."""
    try:
        with open(path, 'rb') as f:
            magic = f.read(4)
            
            # Fat binary (Universal)
            if magic in (b'\xca\xfe\xba\xbe', b'\xbe\xba\xfe\xca'):
                return True, "Universal"
            
            # Mach-O 64-bit
            if magic in (b'\xcf\xfa\xed\xfe', b'\xfe\xed\xfa\xcf'):
                f.seek(4)
                cpu_type = struct.unpack('<I', f.read(4))[0]
                if cpu_type == 0x0100000c:  # ARM64
                    return False, "arm64 only"
                elif cpu_type == 0x01000007:  # x86_64
                    return False, "x86_64 only"
                return False, "unknown arch"
            
            return False, "not Mach-O"
            
    except Exception as e:
        return False, str(e)


def test_native_modules(result: TestResult, client_dir: str):
    """Проверка нативных модулей."""
    modules_dir = os.path.join(client_dir, "modules")
    
    if not os.path.exists(modules_dir):
        result.warn("Директория modules", "Не найдена")
        return
    
    # Ищем .dylib файлы
    dylibs = []
    for root, dirs, files in os.walk(modules_dir):
        for file in files:
            if file.endswith((".dylib", ".so")):
                dylibs.append(os.path.join(root, file))
    
    if not dylibs:
        result.ok("Нативные модули: нет .dylib/.so файлов")
        return
    
    universal_count = 0
    for dylib in dylibs:
        is_universal, arch = is_universal_binary(dylib)
        name = os.path.basename(dylib)
        
        if is_universal:
            universal_count += 1
            result.ok(f"{name}: {arch}")
        else:
            result.warn(f"{name}", f"Не Universal ({arch})")
    
    result.ok(f"{universal_count}/{len(dylibs)} Universal бинарников")


def test_config_files(result: TestResult, client_dir: str):
    """Проверка конфигурационных файлов."""
    config_dir = os.path.join(client_dir, "config")
    
    required_configs = [
        "unified_config.yaml",
    ]
    
    for config in required_configs:
        path = os.path.join(config_dir, config)
        check_file_exists(result, path, f"Конфиг {config}", required=True)


def test_spec_file(result: TestResult, client_dir: str):
    """Проверка PyInstaller spec файла."""
    packaging_dir = os.path.join(client_dir, "packaging")
    
    spec_files = [f for f in os.listdir(packaging_dir) if f.endswith(".spec")] if os.path.exists(packaging_dir) else []
    
    if spec_files:
        for spec in spec_files:
            path = os.path.join(packaging_dir, spec)
            check_file_exists(result, path, f"Spec {spec}", required=False)
    else:
        result.warn("PyInstaller spec", "Spec файлы не найдены")


def test_entitlements(result: TestResult, client_dir: str):
    """Проверка entitlements файла."""
    packaging_dir = os.path.join(client_dir, "packaging")
    
    entitlements_paths = [
        os.path.join(packaging_dir, "entitlements.plist"),
        os.path.join(client_dir, "entitlements.plist"),
    ]
    
    found = False
    for path in entitlements_paths:
        if os.path.exists(path):
            check_file_exists(result, path, "Entitlements", required=True)
            found = True
            break
    
    if not found:
        result.warn("Entitlements", "entitlements.plist не найден")


def main():
    print(f"\n{YELLOW}📦 РЕСУРСЫ PREFLIGHT ПРОВЕРКИ{NC}")
    print("=" * 50)
    
    result = TestResult()
    client_dir = get_client_dir()
    
    print(f"\n{YELLOW}1. Иконки{NC}")
    test_icons(result, client_dir)
    
    print(f"\n{YELLOW}2. Звуки{NC}")
    test_sounds(result, client_dir)
    
    print(f"\n{YELLOW}3. Сертификаты{NC}")
    test_certificates(result, client_dir)
    
    print(f"\n{YELLOW}4. Нативные модули{NC}")
    test_native_modules(result, client_dir)
    
    print(f"\n{YELLOW}5. Конфигурационные файлы{NC}")
    test_config_files(result, client_dir)
    
    print(f"\n{YELLOW}6. PyInstaller spec{NC}")
    test_spec_file(result, client_dir)
    
    print(f"\n{YELLOW}7. Entitlements{NC}")
    test_entitlements(result, client_dir)
    
    print("=" * 50)
    success = result.summary()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
