#!/usr/bin/env python3
"""
Проверка: Все проверки состояния микрофона используют state_manager.
Запрещено: Использование локальных флагов для проверок состояния.

Использование:
    python scripts/validate_microphone_state_source.py [--file <file>] [--fix]

Выход:
    0 - все проверки пройдены
    1 - найдены нарушения
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# Цвета для вывода
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Паттерны запрещенных проверок (локальные флаги для проверки состояния)
FORBIDDEN_PATTERNS = [
    (r'if\s+self\._recording_started\s*:', 'Использование _recording_started для проверки состояния'),
    (r'if\s+self\._google_recording_active\s*:', 'Использование _google_recording_active для проверки состояния'),
    (r'if\s+self\._playback_active\s*:', 'Использование _playback_active для проверки состояния'),
    (r'if\s+mic_active\s+and\s+self\._recording_started\s*:', 'Смешанная проверка (mic_active + локальный флаг)'),
    (r'if\s+.*_recording_started\s+and\s+.*mic_active', 'Смешанная проверка (локальный флаг + mic_active)'),
]

# Паттерны разрешенных проверок (state_manager)
ALLOWED_PATTERNS = [
    r'state_manager\.is_microphone_active\(\)',
    r'state_manager\.get_microphone_state\(\)',
    r'self\.state_manager\.is_microphone_active\(\)',
    r'self\.state_manager\.get_microphone_state\(\)',
]

# Исключения (файлы, где разрешены локальные флаги для внутренней логики)
EXCLUDED_FILES = [
    'integration/core/selectors.py',  # Selectors могут использовать локальные проверки
    'integration/core/gateways/',  # Gateways могут использовать локальные проверки
    'tests/',  # Тесты могут использовать локальные флаги
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
        description='Проверка использования единого источника истины для состояния микрофона'
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
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Автоматически исправить нарушения (не реализовано)'
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
        print("  ✅ Используйте state_manager.is_microphone_active() для проверок состояния")
        print("  ✅ Локальные флаги (_recording_started, _google_recording_active) только для внутренней логики")
        print()
        
        sys.exit(1)
    else:
        print(f"{GREEN}✅ Все проверки пройдены: единый источник истины используется правильно{RESET}")
        sys.exit(0)


if __name__ == '__main__':
    main()

