#!/usr/bin/env python3
"""
Проверка: Все изменения состояния микрофона синхронизированы.
Обязательно: state_manager.set_microphone_state() вызывается при каждом изменении.

Использование:
    python scripts/validate_microphone_sync.py [--file <file>]

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

# События, которые должны обновлять состояние микрофона
STATE_CHANGE_EVENTS = [
    (r'microphone\.opened', 'microphone.opened'),
    (r'microphone\.closed', 'microphone.closed'),
    (r'voice\.recording_start', 'voice.recording_start'),
    (r'voice\.recording_stop', 'voice.recording_stop'),
]

# Паттерны обновления состояния
STATE_UPDATE_PATTERNS = [
    r'state_manager\.set_microphone_state\(',
    r'self\.state_manager\.set_microphone_state\(',
    r'state_manager\.force_close_microphone\(',
    r'self\.state_manager\.force_close_microphone\(',
]

# Исключения (файлы, где не требуется проверка синхронизации)
EXCLUDED_FILES = [
    'tests/',  # Тесты могут не требовать синхронизации
    'scripts/',  # Скрипты могут не требовать синхронизации
]


def is_excluded_file(file_path: Path) -> bool:
    """Проверяет, исключен ли файл из проверки."""
    file_str = str(file_path)
    return any(excluded in file_str for excluded in EXCLUDED_FILES)


def find_state_updates_in_range(lines: List[str], start_line: int, end_line: int) -> bool:
    """Проверяет, есть ли обновление состояния в указанном диапазоне строк."""
    for i in range(start_line, min(end_line, len(lines))):
        line = lines[i]
        for pattern in STATE_UPDATE_PATTERNS:
            if re.search(pattern, line):
                return True
    return False


def validate_file(file_path: Path) -> List[Dict]:
    """Проверяет файл на нарушения синхронизации."""
    violations = []
    
    if is_excluded_file(file_path):
        return violations
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Ищем события, которые должны обновлять состояние
        for i, line in enumerate(lines):
            for event_pattern, event_name in STATE_CHANGE_EVENTS:
                if re.search(event_pattern, line):
                    # Проверяем, есть ли обновление состояния в следующих 15 строках
                    found_update = find_state_updates_in_range(lines, i, i + 15)
                    
                    if not found_update:
                        # Проверяем, не является ли это комментарием или строкой документации
                        is_comment = line.strip().startswith('#')
                        is_docstring = '"""' in line or "'''" in line
                        
                        if not is_comment and not is_docstring:
                            violations.append({
                                'file': str(file_path),
                                'line': i + 1,
                                'event': event_name,
                                'code': line.strip(),
                                'message': f'Событие {event_name} должно обновлять state_manager в следующих 15 строках'
                            })
    
    except Exception as e:
        print(f"{RED}Ошибка при чтении файла {file_path}: {e}{RESET}", file=sys.stderr)
    
    return violations


def validate_directory(directory: Path) -> List[Dict]:
    """Проверяет директорию на нарушения синхронизации."""
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
        description='Проверка синхронизации изменений состояния микрофона'
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
        print(f"{RED}Найдено {len(violations)} нарушений синхронизации:{RESET}\n")
        
        for violation in violations:
            print(f"{YELLOW}{violation['file']}:{violation['line']}{RESET}")
            print(f"  {RED}❌ {violation['message']}{RESET}")
            print(f"  Событие: {violation['event']}")
            print(f"  Код: {violation['code']}")
            print()
        
        print(f"{RED}Исправление:{RESET}")
        print("  ✅ После публикации события microphone.opened/closed обновляйте state_manager")
        print("  ✅ После обработки voice.recording_start/stop обновляйте state_manager")
        print("  ✅ Используйте state_manager.set_microphone_state() для синхронизации")
        print()
        
        sys.exit(1)
    else:
        print(f"{GREEN}✅ Все проверки пройдены: все изменения состояния синхронизированы{RESET}")
        sys.exit(0)


if __name__ == '__main__':
    main()

