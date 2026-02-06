#!/usr/bin/env python3
"""
Валидация релизного бандла Nexy Client

Проверяет метаданные артефакта и убедительность отчётов перед загрузкой на сервер.

Использование:
    python scripts/validate_release_bundle.py <path_to_app> [path_to_pkg]

Проверяет:
- Наличие VERSION_INFO.json и release_suite_report.json в .app
- Валидность метаданных (версия, req_version, checksum)
- Статус подписи и нотарификации
- Структуру .app и .pkg
"""

import argparse
import json
from pathlib import Path
import plistlib
import subprocess
import sys

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color


class BundleValidator:
    """Валидатор релизного бандла"""
    
    def __init__(self, app_path: Path, pkg_path: Path | None = None):
        self.app_path = app_path
        self.pkg_path = pkg_path
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []
        
    def log_info(self, message: str):
        """Логирует информационное сообщение"""
        self.info.append(message)
        print(f"{GREEN}[INFO]{NC} {message}")
    
    def log_error(self, message: str):
        """Логирует сообщение об ошибке"""
        self.errors.append(message)
        print(f"{RED}[ERROR]{NC} {message}")
    
    def log_warn(self, message: str):
        """Логирует предупреждение"""
        self.warnings.append(message)
        print(f"{YELLOW}[WARN]{NC} {message}")
    
    def check_app_exists(self) -> bool:
        """Проверка 1: .app существует"""
        if not self.app_path.exists():
            self.log_error(f".app не найден: {self.app_path}")
            return False
        
        if not self.app_path.is_dir():
            self.log_error(f".app не является директорией: {self.app_path}")
            return False
        
        self.log_info(f"✅ .app найден: {self.app_path}")
        return True
    
    def check_app_structure(self) -> bool:
        """Проверка 2: Структура .app"""
        required_paths = [
            'Contents/Info.plist',
            'Contents/MacOS/Nexy',
            'Contents/Resources',
        ]
        
        all_ok = True
        for rel_path in required_paths:
            full_path = self.app_path / rel_path
            if not full_path.exists():
                self.log_error(f"Отсутствует обязательный путь: {rel_path}")
                all_ok = False
            else:
                self.log_info(f"✅ Найден: {rel_path}")
        
        return all_ok
    
    def check_info_plist(self) -> bool:
        """Проверка 3: Info.plist"""
        plist_path = self.app_path / 'Contents' / 'Info.plist'
        if not plist_path.exists():
            self.log_error("Info.plist не найден")
            return False
        
        try:
            with open(plist_path, 'rb') as f:
                plist = plistlib.load(f)
            
            # Проверяем обязательные поля
            required_keys = ['CFBundleIdentifier', 'CFBundleVersion', 'CFBundleShortVersionString']
            all_ok = True
            
            for key in required_keys:
                if key not in plist:
                    self.log_error(f"Info.plist: отсутствует ключ {key}")
                    all_ok = False
                else:
                    self.log_info(f"✅ Info.plist: {key} = {plist[key]}")
            
            # Проверяем CFBundleIdentifier
            if 'CFBundleIdentifier' in plist:
                bundle_id = plist['CFBundleIdentifier']
                if bundle_id != 'com.nexy.assistant':
                    self.log_warn(f"CFBundleIdentifier: {bundle_id} (ожидается com.nexy.assistant)")
            
            return all_ok
            
        except Exception as e:
            self.log_error(f"Ошибка чтения Info.plist: {e}")
            return False
    
    def check_version_info(self) -> bool:
        """Проверка 4: VERSION_INFO.json"""
        version_info_path = self.app_path / 'Contents' / 'Resources' / 'VERSION_INFO.json'
        
        if not version_info_path.exists():
            self.log_warn("VERSION_INFO.json не найден в .app (не критично)")
            return True  # Не критично
        
        try:
            with open(version_info_path, 'r', encoding='utf-8') as f:
                version_info = json.load(f)
            
            # Проверяем обязательные поля
            if 'version' not in version_info:
                self.log_error("VERSION_INFO.json: отсутствует поле 'version'")
                return False
            
            if 'requirements' not in version_info:
                self.log_warn("VERSION_INFO.json: отсутствует поле 'requirements'")
            else:
                req = version_info['requirements']
                if 'req_version' not in req:
                    self.log_warn("VERSION_INFO.json: отсутствует req_version")
                else:
                    self.log_info(f"✅ req_version: {req['req_version']}")
                
                if 'req_checksum' not in req:
                    self.log_warn("VERSION_INFO.json: отсутствует req_checksum")
                else:
                    checksum = req['req_checksum']
                    self.log_info(f"✅ req_checksum: {checksum[:16]}...")
            
            self.log_info(f"✅ VERSION_INFO.json валиден: version={version_info.get('version', 'unknown')}")
            return True
            
        except Exception as e:
            self.log_error(f"Ошибка чтения VERSION_INFO.json: {e}")
            return False
    
    def check_release_suite_report(self) -> bool:
        """Проверка 5: release_suite_report.json"""
        report_path = self.app_path / 'Contents' / 'Resources' / 'release_suite_report.json'
        
        if not report_path.exists():
            self.log_warn("release_suite_report.json не найден в .app (не критично)")
            return True  # Не критично
        
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            
            # Проверяем структуру отчёта
            if 'summary' not in report:
                self.log_warn("release_suite_report.json: отсутствует поле 'summary'")
                return True  # Не критично
            
            summary = report['summary']
            total = summary.get('total', 0)
            passed = summary.get('passed', 0)
            failed = summary.get('failed', 0)
            errors = summary.get('errors', 0)
            success = summary.get('success', False)
            
            self.log_info(f"Release Suite: {passed}/{total} проверок пройдено")
            
            if not success:
                self.log_warn(f"Release Suite: есть проваленные проверки (failed={failed}, errors={errors})")
            else:
                self.log_info("✅ Release Suite: все проверки пройдены")
            
            return True  # Не критично, только предупреждение
            
        except Exception as e:
            self.log_warn(f"Ошибка чтения release_suite_report.json: {e}")
            return True  # Не критично
    
    def check_code_signature(self) -> bool:
        """Проверка 6: Подпись кода"""
        try:
            result = subprocess.run(
                ['codesign', '--verify', '--deep', '--strict', '--verbose=2', str(self.app_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                self.log_info("✅ Подпись кода валидна")
                return True
            else:
                self.log_error(f"Подпись кода невалидна:\n{result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            self.log_error("Проверка подписи превысила таймаут")
            return False
        except Exception as e:
            self.log_error(f"Ошибка проверки подписи: {e}")
            return False
    
    def check_notarization(self) -> bool:
        """Проверка 7: Нотарификация"""
        try:
            result = subprocess.run(
                ['xcrun', 'stapler', 'validate', str(self.app_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                self.log_info("✅ Нотарификация валидна")
                return True
            else:
                self.log_warn(f"Нотарификация может быть невалидна:\n{result.stderr}")
                return True  # Не критично, может быть не нотарифицирован
            
        except subprocess.TimeoutExpired:
            self.log_warn("Проверка нотарификации превысила таймаут")
            return True  # Не критично
        except Exception as e:
            self.log_warn(f"Ошибка проверки нотарификации: {e}")
            return True  # Не критично
    
    def check_pkg(self) -> bool:
        """Проверка 8: .pkg (если указан)"""
        if not self.pkg_path:
            return True  # Не указан, пропускаем
        
        if not self.pkg_path.exists():
            self.log_warn(f".pkg не найден: {self.pkg_path}")
            return True  # Не критично
        
        try:
            # Проверяем подпись PKG
            result = subprocess.run(
                ['pkgutil', '--check-signature', str(self.pkg_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                self.log_info("✅ Подпись PKG валидна")
            else:
                self.log_warn(f"Подпись PKG может быть невалидна:\n{result.stderr}")
            
            # Проверяем нотарификацию PKG
            result = subprocess.run(
                ['xcrun', 'stapler', 'validate', str(self.pkg_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                self.log_info("✅ Нотарификация PKG валидна")
            else:
                self.log_warn(f"Нотарификация PKG может быть невалидна")
            
            return True  # Не критично
            
        except Exception as e:
            self.log_warn(f"Ошибка проверки PKG: {e}")
            return True  # Не критично
    
    def validate(self) -> bool:
        """Выполняет все проверки"""
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{GREEN}🔍 ВАЛИДАЦИЯ РЕЛИЗНОГО БАНДЛА{NC}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print()
        
        checks = [
            ('Существование .app', self.check_app_exists),
            ('Структура .app', self.check_app_structure),
            ('Info.plist', self.check_info_plist),
            ('VERSION_INFO.json', self.check_version_info),
            ('release_suite_report.json', self.check_release_suite_report),
            ('Подпись кода', self.check_code_signature),
            ('Нотарификация', self.check_notarization),
            ('PKG (если указан)', self.check_pkg),
        ]
        
        all_passed = True
        for name, check_func in checks:
            print(f"{BLUE}Проверка: {name}{NC}")
            if not check_func():
                all_passed = False
            print()
        
        # Итоги
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{GREEN}ИТОГИ ВАЛИДАЦИИ{NC}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print()
        
        print(f"Информаций: {len(self.info)}")
        if self.warnings:
            print(f"{YELLOW}Предупреждений: {len(self.warnings)}{NC}")
        if self.errors:
            print(f"{RED}Ошибок: {len(self.errors)}{NC}")
        print()
        
        if all_passed and not self.errors:
            print(f"{GREEN}✅ ВАЛИДАЦИЯ: ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ{NC}")
            return True
        else:
            print(f"{RED}❌ ВАЛИДАЦИЯ: ЕСТЬ ОШИБКИ{NC}")
            if self.errors:
                print(f"\n{RED}Ошибки:{NC}")
                for error in self.errors:
                    print(f"  • {error}")
            return False


def main():
    parser = argparse.ArgumentParser(description='Валидация релизного бандла Nexy Client')
    parser.add_argument('app_path', type=str, help='Путь к Nexy.app')
    parser.add_argument('pkg_path', type=str, nargs='?', help='Путь к Nexy.pkg (опционально)')
    args = parser.parse_args()
    
    app_path = Path(args.app_path).resolve()
    pkg_path = Path(args.pkg_path).resolve() if args.pkg_path else None
    
    validator = BundleValidator(app_path, pkg_path)
    success = validator.validate()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

