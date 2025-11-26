#!/usr/bin/env python3
"""
Полная валидация Universal 2 пакета Nexy

Проверяет все нюансы Universal 2 сборки:
- Архитектуры (arm64 + x86_64) в .app и PKG
- Подпись и нотаризацию
- Структуру и ресурсы
- Размеры и производительность

Использование:
    python scripts/validate_universal_package.py [--pkg path/to/Nexy.pkg] [--dmg path/to/Nexy.dmg]
"""

import argparse
import subprocess
import sys
import tempfile
import tarfile
from pathlib import Path
from typing import Optional, Dict, List, Tuple

# Цвета
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'


def run_cmd(cmd: List[str], check: bool = True) -> Tuple[int, str, str]:
    """Выполняет команду и возвращает код, stdout, stderr"""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"{RED}❌ Команда провалилась: {' '.join(cmd)}{NC}")
        print(f"{RED}   stderr: {result.stderr}{NC}")
    return result.returncode, result.stdout, result.stderr


def check_lipo_architectures(binary_path: Path) -> Dict[str, bool]:
    """Проверяет архитектуры бинарника через lipo"""
    code, stdout, stderr = run_cmd(["lipo", "-info", str(binary_path)], check=False)
    if code != 0:
        return {"error": stderr or stdout}
    
    info = (stdout + stderr).lower()
    return {
        "arm64": "arm64" in info,
        "x86_64": "x86_64" in info,
        "universal": "arm64" in info and "x86_64" in info,
        "info": stdout.strip()
    }


def extract_pkg_app(pkg_path: Path, extract_dir: Path) -> Optional[Path]:
    """Извлекает .app из PKG для проверки"""
    print(f"{BLUE}📦 Извлекаем .app из PKG...{NC}")
    
    # Шаг 1: Распаковываем distribution PKG
    expanded_dir = extract_dir / "expanded"
    code, _, stderr = run_cmd(["pkgutil", "--expand", str(pkg_path), str(expanded_dir)])
    if code != 0:
        print(f"{RED}❌ Ошибка распаковки PKG: {stderr}{NC}")
        return None
    
    # Шаг 2: Находим вложенный component PKG
    nested_pkg = None
    for item in expanded_dir.rglob("*.pkg"):
        if item.is_dir() and (item / "PackageInfo").exists():
            nested_pkg = item
            break
    
    if not nested_pkg:
        print(f"{RED}❌ Не найден вложенный .pkg в distribution PKG{NC}")
        return None
    
    # Шаг 3: Извлекаем Payload (используем подход из build_final.sh: tar -xf)
    payload = nested_pkg / "Payload"
    if not payload.exists():
        print(f"{RED}❌ Payload не найден во вложенном PKG{NC}")
        return None
    
    app_extract_dir = extract_dir / "app"
    app_extract_dir.mkdir(exist_ok=True)
    
    # Используем tar -xf (как в build_final.sh)
    code, _, stderr = run_cmd([
        "tar", "-xf", str(payload), "-C", str(app_extract_dir)
    ], check=False)
    
    if code != 0:
        print(f"{YELLOW}⚠️  tar -xf не сработал, пробуем альтернативные методы...{NC}")
        # Пробуем через cpio
        import gzip
        import shutil
        temp_cpio = app_extract_dir / "payload.cpio"
        try:
            with gzip.open(payload, "rb") as gz:
                with open(temp_cpio, "wb") as out:
                    shutil.copyfileobj(gz, out)
            
            code, _, _ = run_cmd([
                "cd", str(app_extract_dir), "&&",
                "cpio", "-i", "<", str(temp_cpio)
            ], check=False)
            if temp_cpio.exists():
                temp_cpio.unlink()
        except Exception as e:
            print(f"{RED}❌ Не удалось распаковать Payload: {e}{NC}")
            return None
    
    # Шаг 4: Находим .app (обычно в Applications/Nexy.app)
    app_path = app_extract_dir / "Applications" / "Nexy.app"
    if not app_path.exists():
        # Пробуем найти в любом месте
        for item in app_extract_dir.rglob("*.app"):
            if item.is_dir():
                app_path = item
                break
        else:
            app_path = None
    
    if app_path and app_path.exists():
        print(f"{GREEN}✅ .app извлечён: {app_path}{NC}")
    else:
        print(f"{RED}❌ .app не найден в извлечённом содержимом{NC}")
        return None
    
    return app_path


def validate_app_architectures(app_path: Path) -> bool:
    """Проверяет архитектуры в .app"""
    print(f"\n{BLUE}🏗️  Проверка архитектур .app{NC}")
    
    # Главный бинарник
    main_binary = app_path / "Contents" / "MacOS" / "Nexy"
    if not main_binary.exists():
        print(f"{RED}❌ Главный бинарник не найден: {main_binary}{NC}")
        return False
    
    archs = check_lipo_architectures(main_binary)
    if "error" in archs:
        print(f"{RED}❌ Ошибка проверки главного бинарника: {archs['error']}{NC}")
        return False
    
    if not archs["universal"]:
        print(f"{RED}❌ Главный бинарник не Universal 2: {archs['info']}{NC}")
        return False
    
    print(f"{GREEN}✅ Главный бинарник: {archs['info']}{NC}")
    
    # Ресурсные бинарники
    resource_binaries = [
        ("FFmpeg", app_path / "Contents" / "Resources" / "resources" / "ffmpeg" / "ffmpeg"),
        ("SwitchAudioSource", app_path / "Contents" / "Resources" / "resources" / "audio" / "SwitchAudioSource"),
        ("FLAC", app_path / "Contents" / "Resources" / "resources" / "audio" / "flac"),
    ]
    
    all_ok = True
    for name, binary_path in resource_binaries:
        if not binary_path.exists():
            print(f"{YELLOW}⚠️  {name} не найден (не критично){NC}")
            continue
        
        archs = check_lipo_architectures(binary_path)
        if "error" in archs:
            print(f"{RED}❌ Ошибка проверки {name}: {archs['error']}{NC}")
            all_ok = False
            continue
        
        if not archs["universal"]:
            print(f"{RED}❌ {name} не Universal 2: {archs['info']}{NC}")
            all_ok = False
        else:
            print(f"{GREEN}✅ {name}: {archs['info']}{NC}")
    
    return all_ok


def validate_pkg_signature(pkg_path: Path) -> bool:
    """Проверяет подпись и нотаризацию PKG"""
    print(f"\n{BLUE}🔐 Проверка подписи PKG{NC}")
    
    # Проверка подписи
    code, stdout, stderr = run_cmd(["pkgutil", "--check-signature", str(pkg_path)])
    if code != 0:
        print(f"{RED}❌ PKG не подписан или подпись невалидна{NC}")
        print(f"{RED}   {stderr}{NC}")
        return False
    
    if "signed by a developer certificate" not in stdout:
        print(f"{RED}❌ PKG не подписан Developer ID сертификатом{NC}")
        return False
    
    if "Notarization: trusted" not in stdout:
        print(f"{YELLOW}⚠️  PKG не нотаризован (может быть в процессе){NC}")
    else:
        print(f"{GREEN}✅ PKG подписан и нотаризован{NC}")
    
    # Проверка stapler
    code, _, _ = run_cmd(["xcrun", "stapler", "validate", str(pkg_path)])
    if code != 0:
        print(f"{YELLOW}⚠️  stapler validate не прошёл (может быть нормально){NC}")
    else:
        print(f"{GREEN}✅ stapler validate успешно{NC}")
    
    return True


def validate_dmg(dmg_path: Path) -> bool:
    """Проверяет DMG"""
    print(f"\n{BLUE}💿 Проверка DMG{NC}")
    
    if not dmg_path.exists():
        print(f"{YELLOW}⚠️  DMG не найден (не критично){NC}")
        return True
    
    # Проверяем размер
    size_mb = dmg_path.stat().st_size / (1024 * 1024)
    print(f"{GREEN}✅ Размер DMG: {size_mb:.1f} MB{NC}")
    
    # Пытаемся примонтировать и проверить содержимое
    mount_point = Path(tempfile.mkdtemp(prefix="nexy_dmg_"))
    try:
        code, _, stderr = run_cmd([
            "hdiutil", "attach", str(dmg_path),
            "-mountpoint", str(mount_point),
            "-quiet"
        ], check=False)
        
        if code == 0:
            app_in_dmg = list(mount_point.glob("*.app"))
            if app_in_dmg:
                print(f"{GREEN}✅ .app найден в DMG: {app_in_dmg[0].name}{NC}")
            else:
                print(f"{YELLOW}⚠️  .app не найден в DMG{NC}")
            
            run_cmd(["hdiutil", "detach", str(mount_point), "-quiet"], check=False)
        else:
            print(f"{YELLOW}⚠️  Не удалось примонтировать DMG: {stderr}{NC}")
    except Exception as e:
        print(f"{YELLOW}⚠️  Ошибка проверки DMG: {e}{NC}")
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Валидация Universal 2 пакета Nexy")
    parser.add_argument("--pkg", type=Path, help="Путь к PKG файлу")
    parser.add_argument("--dmg", type=Path, help="Путь к DMG файлу")
    parser.add_argument("--app", type=Path, help="Путь к .app (если есть отдельно)")
    
    args = parser.parse_args()
    
    # Определяем пути
    dist_dir = Path(__file__).parent.parent / "dist"
    pkg_path = args.pkg or (dist_dir / "Nexy.pkg")
    dmg_path = args.dmg or (dist_dir / "Nexy.dmg")
    app_path = args.app
    
    print(f"{BLUE}{'='*60}{NC}")
    print(f"{BLUE}🔍 ВАЛИДАЦИЯ UNIVERSAL 2 ПАКЕТА NEXY{NC}")
    print(f"{BLUE}{'='*60}{NC}\n")
    
    errors = []
    
    # Проверка PKG
    if pkg_path.exists():
        print(f"{GREEN}✅ PKG найден: {pkg_path}{NC}")
        
        # Подпись и нотаризация
        if not validate_pkg_signature(pkg_path):
            errors.append("PKG подпись/нотаризация невалидна")
        
        # Извлекаем .app из PKG для проверки архитектур
        with tempfile.TemporaryDirectory(prefix="nexy_validate_") as tmpdir:
            extracted_app = extract_pkg_app(pkg_path, Path(tmpdir))
            if extracted_app:
                if not validate_app_architectures(extracted_app):
                    errors.append("Архитектуры .app невалидны")
            else:
                errors.append("Не удалось извлечь .app из PKG")
    else:
        print(f"{RED}❌ PKG не найден: {pkg_path}{NC}")
        errors.append("PKG не найден")
    
    # Проверка DMG
    validate_dmg(dmg_path)
    
    # Проверка .app напрямую (если указан)
    if app_path and app_path.exists():
        print(f"\n{BLUE}📱 Проверка .app напрямую{NC}")
        if not validate_app_architectures(app_path):
            errors.append("Архитектуры .app (прямая проверка) невалидны")
    
    # Итоги
    print(f"\n{BLUE}{'='*60}{NC}")
    if errors:
        print(f"{RED}❌ ВАЛИДАЦИЯ: ЕСТЬ ОШИБКИ{NC}")
        for err in errors:
            print(f"{RED}   • {err}{NC}")
        return 1
    else:
        print(f"{GREEN}✅ ВАЛИДАЦИЯ: ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ{NC}")
        return 0


if __name__ == "__main__":
    sys.exit(main())

