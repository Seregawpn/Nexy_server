#!/usr/bin/env python3
"""
Проверка: Все операции с состоянием микрофона thread-safe.
Запрещено: Прямое изменение _microphone_state без блокировок.

Использование:
    python scripts/validate_microphone_thread_safety.py [--file <file>]

Выход:
    0 - все проверки пройдены
    1 - найдены нарушения
"""

import re
import sys
from pathlib import Path
from typing import List, Dict

# Цвета для вывода
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Паттерны запрещенных операций (прямое изменение без блокировок)
FORBIDDEN_PATTERNS = [
    (r'self\._microphone_state\s*=', 'Прямое изменение _microphone_state без блокировок'),
    (r'state_manager\._microphone_state\s*=', 'Прямое изменение state_manager._microphone_state без блокировок'),
    (r'self\._microphone_session_id\s*=', 'Прямое изменение _microphone_session_id без блокировок'),
    (r'state_manager\._microphone_session_id\s*=', 'Прямое изменение state_manager._microphone_session_id без блокировок'),
]

# Паттерны разрешенных операций (thread-safe методы)
ALLOWED_PATTERNS = [
    r'state_manager\.set_microphone_state\(',
    r'state_manager\.force_close_microphone\(',
    r'self\.state_manager\.set_microphone_state\(',
    r'self\.state_manager\.force_close_microphone\(',
    r'with\s+self\._microphone_lock:',
    r'with\s+.*_microphone_lock:',
    r'with\s+.*lock:',
]

# Исключения (файлы, где разрешены прямые изменения)
EXCLUDED_FILES = [
    'integration/core/state_manager.py',  # state_manager сам управляет состоянием
    'tests/',  # Тесты могут использовать прямые изменения
]


def is_excluded_file(file_path: Path) -> bool:
    """Проверяет, исключен ли файл из проверки."""
    file_str = str(file_path)
    return any(excluded in file_str for excluded in EXCLUDED_FILES)


def check_line(line: str, line_num: int, file_path: Path) -> List[Dict]:
    """Проверяет одну строку на нарушения."""
    violations = []
    
    for pattern, description in FORBIDDEN_PATTERNS:
        if re.search(pattern, line):
            # Проверяем, не является ли это частью разрешенного паттерна
            is_allowed = any(re.search(allowed, line) for allowed in ALLOWED_PATTERNS)
            
            # Проверяем, не является ли это комментарием
            is_comment = line.strip().startswith('#')
            
            if not is_allowed and not is_comment:
                violations.append({
                    'file': str(file_path),
                    'line': line_num,
                    'pattern': pattern,
                    'description': description,
                    'code': line.strip()
                })
    
    return violations


def validate_file(file_path: Path) -> List[Dict]:
    """Проверяет файл на нарушения."""
    violations = []
    
    if is_excluded_file(file_path):
        return violations
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines, 1):
            line_violations = check_line(line, i, file_path)
            violations.extend(line_violations)
    
    except Exception as e:
        print(f"{RED}Ошибка при чтении файла {file_path}: {e}{RESET}", file=sys.stderr)
    
    return violations


def validate_directory(directory: Path) -> List[Dict]:
    """Проверяет директорию на нарушения."""
    violations = []
    
    for py_file in directory.rglob('*.py'):
        if py_file.is_file():
            file_violations = validate_file(py_file)
            violations.extend(file_violations)
    
    return violations


def main():
    """Главная функция."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Проверка thread-safety операций с состоянием микрофона'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='Проверить конкретный файл'
    )
    parser.add_argument(
        '--directory',
        type=str,
        default='integration/integrations',
        help='Проверить директорию (по умолчанию: integration/integrations)'
    )
    
    args = parser.parse_args()
    
    violations = []
    
    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"{RED}Файл не найден: {file_path}{RESET}", file=sys.stderr)
            sys.exit(1)
        violations = validate_file(file_path)
    else:
        directory = Path(args.directory)
        if not directory.exists():
            print(f"{RED}Директория не найдена: {directory}{RESET}", file=sys.stderr)
            sys.exit(1)
        violations = validate_directory(directory)
    
    if violations:
        print(f"{RED}Найдено {len(violations)} нарушений:{RESET}\n")
        
        for violation in violations:
            print(f"{YELLOW}{violation['file']}:{violation['line']}{RESET}")
            print(f"  {RED}❌ {violation['description']}{RESET}")
            print(f"  Код: {violation['code']}")
            print()
        
        print(f"{RED}Исправление:{RESET}")
        print("  ✅ Используйте state_manager.set_microphone_state() для изменения состояния")
        print("  ✅ Используйте блокировки (with self._microphone_lock:) для критических секций")
        print()
        
        sys.exit(1)
    else:
        print(f"{GREEN}✅ Все проверки пройдены: все операции thread-safe{RESET}")
        sys.exit(0)


if __name__ == '__main__':
    main()

