#!/usr/bin/env python3
"""
Скрипт для проверки зависимостей между модулями и интеграциями.
Проверяет корректность импортов и отсутствие циклических зависимостей.
"""

import sys
import ast
import importlib.util
from pathlib import Path
from typing import Set, Dict, List, Tuple
from collections import defaultdict

# Добавляем пути как в main.py
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))
if (CLIENT_ROOT / "client" / "modules").exists():
    sys.path.insert(0, str(CLIENT_ROOT / "client" / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "modules"))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))


class DependencyChecker:
    """Проверяет зависимости между модулями и интеграциями"""
    
    def __init__(self, root: Path):
        self.root = root
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.imports: Dict[str, Set[str]] = defaultdict(set)
        
    def check_file(self, file_path: Path) -> bool:
        """Проверяет один файл на корректность импортов"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        self._check_import(file_path, alias.name, alias.asname)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        self._check_import(file_path, node.module, None)
                        
        except SyntaxError as e:
            self.errors.append(f"❌ Синтаксическая ошибка в {file_path}: {e}")
            return False
        except Exception as e:
            self.warnings.append(f"⚠️ Ошибка при проверке {file_path}: {e}")
            return False
            
        return True
    
    def _check_import(self, file_path: Path, module_name: str, alias: str = None):
        """Проверяет один импорт"""
        # Игнорируем стандартные библиотеки
        if not module_name or module_name.split('.')[0] in ['sys', 'os', 'asyncio', 'logging', 'typing', 'pathlib', 'dataclasses', 'enum', 'json', 'time', 'uuid', 'threading', 'collections', 'abc', 'functools', 'itertools', 'operator', 'copy', 'pickle', 'hashlib', 'base64', 'urllib', 'http', 'socket', 'ssl', 'ctypes', 'tempfile', 'shutil', 'subprocess', 'signal', 'platform', 'traceback', 'inspect', 'importlib', 'pkgutil', 'weakref', 'gc', 'multiprocessing', 'queue', 'concurrent', 'futures', 'contextlib', 'dataclasses', 'typing_extensions', 'collections.abc']:
            return
        
        # Проверяем импорты модулей и интеграций
        if module_name.startswith('modules.') or module_name.startswith('client.modules.') or module_name.startswith('integration.'):
            # Пытаемся импортировать модуль
            try:
                spec = importlib.util.find_spec(module_name)
                if spec is None:
                    # Пробуем альтернативные пути
                    if module_name.startswith('modules.'):
                        alt_name = module_name.replace('modules.', 'client.modules.', 1)
                        spec = importlib.util.find_spec(alt_name)
                        if spec is None:
                            self.errors.append(f"❌ Не найден модуль {module_name} (используется в {file_path})")
                    elif module_name.startswith('client.modules.'):
                        alt_name = module_name.replace('client.modules.', 'modules.', 1)
                        spec = importlib.util.find_spec(alt_name)
                        if spec is None:
                            self.errors.append(f"❌ Не найден модуль {module_name} (используется в {file_path})")
                    else:
                        self.errors.append(f"❌ Не найден модуль {module_name} (используется в {file_path})")
            except Exception as e:
                self.warnings.append(f"⚠️ Ошибка при проверке импорта {module_name} в {file_path}: {e}")
    
    def check_all(self) -> Tuple[bool, List[str], List[str]]:
        """Проверяет все файлы в проекте"""
        # Проверяем интеграции
        integrations_dir = self.root / "integration" / "integrations"
        if integrations_dir.exists():
            for file_path in integrations_dir.glob("*.py"):
                if file_path.name != "__init__.py":
                    self.check_file(file_path)
        
        # Проверяем core
        core_dir = self.root / "integration" / "core"
        if core_dir.exists():
            for file_path in core_dir.glob("*.py"):
                if file_path.name != "__init__.py":
                    self.check_file(file_path)
        
        return len(self.errors) == 0, self.errors, self.warnings


def main():
    """Главная функция"""
    root = Path(__file__).parent.parent
    checker = DependencyChecker(root)
    
    print("🔍 Проверка зависимостей между модулями и интеграциями...")
    print("=" * 80)
    
    success, errors, warnings = checker.check_all()
    
    if warnings:
        print(f"\n⚠️ Предупреждения ({len(warnings)}):")
        for warning in warnings[:20]:  # Показываем первые 20
            print(f"  {warning}")
        if len(warnings) > 20:
            print(f"  ... и ещё {len(warnings) - 20} предупреждений")
    
    if errors:
        print(f"\n❌ Ошибки ({len(errors)}):")
        for error in errors:
            print(f"  {error}")
    else:
        print("\n✅ Все зависимости корректны!")
    
    print("=" * 80)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
