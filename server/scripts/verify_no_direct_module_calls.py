#!/usr/bin/env python3
"""
Скрипт проверки отсутствия прямых межмодульных вызовов
Фейлит PR, если в server/modules/* импортируется другой server/modules/*
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color


def find_direct_module_imports(modules_dir: Path) -> List[Tuple[str, str, int]]:
    """
    Поиск прямых импортов между модулями
    
    Args:
        modules_dir: Директория с модулями
        
    Returns:
        Список кортежей (файл, импорт, строка)
    """
    issues = []
    
    # Паттерн для поиска импортов модулей
    module_import_pattern = re.compile(
        r'^from\s+modules\.(\w+)|^import\s+modules\.(\w+)'
    )
    
    for py_file in modules_dir.rglob("*.py"):
        # Пропускаем __init__.py и __pycache__
        if py_file.name == "__init__.py" or "__pycache__" in str(py_file):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    
                    # Проверяем импорты модулей
                    match = module_import_pattern.match(line)
                    if match:
                        imported_module = match.group(1) or match.group(2)
                        
                        # Определяем текущий модуль (берем имя родительской директории)
                        current_module = None
                        for part in py_file.parts:
                            if part == "modules":
                                # Находим следующий элемент после "modules"
                                idx = py_file.parts.index(part)
                                if idx + 1 < len(py_file.parts):
                                    current_module = py_file.parts[idx + 1]
                                    break
                        
                        # Если импортируется другой модуль - это проблема
                        # Но импорты внутри одного модуля (например, config, providers) - OK
                        if current_module and imported_module != current_module:
                            issues.append((
                                str(py_file.relative_to(modules_dir.parent.parent)),
                                f"modules.{imported_module}",
                                line_num
                            ))
        
        except Exception as e:
            print(f"{YELLOW}⚠️ Ошибка чтения файла {py_file}: {e}{NC}")
    
    return issues


def main():
    """Основная функция проверки"""
    project_root = Path(__file__).parent.parent
    modules_dir = project_root / "modules"
    
    if not modules_dir.exists():
        print(f"{RED}❌ Директория modules не найдена: {modules_dir}{NC}")
        sys.exit(1)
    
    print("🔍 Проверка прямых межмодульных вызовов...")
    print()
    
    issues = find_direct_module_imports(modules_dir)
    
    if issues:
        print(f"{RED}❌ Найдено {len(issues)} прямых межмодульных импортов:{NC}")
        print()
        
        for file_path, import_name, line_num in issues:
            print(f"  {RED}✗{NC} {file_path}:{line_num}")
            print(f"    Импорт: {import_name}")
            print()
        
        print(f"{RED}❌ Прямые вызовы между модулями запрещены!{NC}")
        print(f"{YELLOW}Используйте координатор модулей (ModuleCoordinator) для взаимодействия.{NC}")
        sys.exit(1)
    else:
        print(f"{GREEN}✅ Прямых межмодульных импортов не найдено{NC}")
        sys.exit(0)


if __name__ == "__main__":
    main()

