#!/usr/bin/env python3
"""
Скрипт для валидации и обновления snapshot требований PROJECT_REQUIREMENTS.md.

Использование:
    python scripts/update_requirements_snapshot.py --check    # Только проверка
    python scripts/update_requirements_snapshot.py --update    # Обновление checksum в VERSION_INFO.json
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# Пути к файлам
PROJECT_ROOT = Path(__file__).parent.parent
REQUIREMENTS_FILE = PROJECT_ROOT / "Docs" / "PROJECT_REQUIREMENTS.md"
VERSION_INFO_FILE = PROJECT_ROOT / "client" / "VERSION_INFO.json"


def extract_requirements_version(content: str) -> str:
    """Извлекает req_version из PROJECT_REQUIREMENTS.md."""
    match = re.search(r'\*\*Версия snapshot\'а\*\*:\s*`req_version\s*=\s*([^`]+)`', content)
    if match:
        return match.group(1).strip()
    return None


def extract_requirements_date(content: str) -> str:
    """Извлекает дату выпуска из PROJECT_REQUIREMENTS.md."""
    match = re.search(r'\*\*Дата выпуска\*\*:\s*(\d{4}-\d{2}-\d{2})', content)
    if match:
        return match.group(1)
    return None


def calculate_checksum(content: str) -> str:
    """Вычисляет SHA256 checksum содержимого файла."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def validate_requirements_structure(content: str) -> list:
    """Проверяет структуру PROJECT_REQUIREMENTS.md и возвращает список ошибок."""
    errors = []
    
    # Проверка наличия обязательных разделов
    required_sections = [
        "## Назначение",
        "## Структура требований",
        "## 1. Client Runtime",
        "## Implementation Map",
        "## Процесс обновления требований",
    ]
    
    for section in required_sections:
        if section not in content:
            errors.append(f"Отсутствует обязательный раздел: {section}")
    
    # Проверка наличия req_version
    if not extract_requirements_version(content):
        errors.append("Отсутствует req_version в заголовке")
    
    # Проверка наличия даты выпуска
    if not extract_requirements_date(content):
        errors.append("Отсутствует дата выпуска в заголовке")
    
    # Проверка формата требований (REQ-XXX)
    req_pattern = r'### REQ-\d{3}:'
    requirements = re.findall(req_pattern, content)
    if not requirements:
        errors.append("Не найдено ни одного требования в формате REQ-XXX")
    
    # Проверка наличия полей в требованиях
    req_sections = re.split(r'### REQ-\d{3}:', content)
    for i, section in enumerate(req_sections[1:], 1):
        req_id = f"REQ-{i:03d}"
        required_fields = [
            "- **Домен**:",
            "- **Критичность**:",
            "- **Описание**:",
            "- **Источник**:",
            "- **Owner**:",
            "- **Ожидаемый результат**:",
            "- **Implementation**:",
            "- **Verification**:",
        ]
        
        for field in required_fields:
            if field not in section:
                errors.append(f"{req_id}: отсутствует поле {field}")
    
    # Проверка Implementation Map
    if "## Implementation Map" in content:
        impl_map_section = content.split("## Implementation Map")[1].split("##")[0]
        if "| Requirement ID |" not in impl_map_section:
            errors.append("Implementation Map не содержит таблицу")
    
    return errors


def update_version_info(req_version: str, req_date: str, checksum: str):
    """Обновляет VERSION_INFO.json с req_version и checksum."""
    if not VERSION_INFO_FILE.exists():
        # Создаём файл, если его нет
        data = {
            "version": "0.0.0",
            "build_date": "",
            "git_sha": "",
            "requirements": {
                "req_version": req_version,
                "req_date": req_date,
                "req_checksum": checksum
            }
        }
    else:
        with open(VERSION_INFO_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "requirements" not in data:
            data["requirements"] = {}
        
        data["requirements"]["req_version"] = req_version
        data["requirements"]["req_date"] = req_date
        data["requirements"]["req_checksum"] = checksum
    
    with open(VERSION_INFO_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Обновлён {VERSION_INFO_FILE}")
    print(f"   req_version: {req_version}")
    print(f"   req_date: {req_date}")
    print(f"   req_checksum: {checksum}")


def main():
    parser = argparse.ArgumentParser(description='Валидация и обновление snapshot требований')
    parser.add_argument('--check', action='store_true', help='Только проверка структуры')
    parser.add_argument('--update', action='store_true', help='Обновить checksum в VERSION_INFO.json')
    args = parser.parse_args()
    
    if not args.check and not args.update:
        parser.print_help()
        sys.exit(1)
    
    # Читаем PROJECT_REQUIREMENTS.md
    if not REQUIREMENTS_FILE.exists():
        print(f"❌ Файл не найден: {REQUIREMENTS_FILE}")
        sys.exit(1)
    
    with open(REQUIREMENTS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Валидация структуры
    errors = validate_requirements_structure(content)
    
    if errors:
        print("❌ Ошибки валидации структуры:")
        for error in errors:
            print(f"   - {error}")
        sys.exit(1)
    
    print("✅ Структура PROJECT_REQUIREMENTS.md валидна")
    
    # Извлекаем метаданные
    req_version = extract_requirements_version(content)
    req_date = extract_requirements_date(content)
    checksum = calculate_checksum(content)
    
    if req_version:
        print(f"   req_version: {req_version}")
    if req_date:
        print(f"   req_date: {req_date}")
    print(f"   checksum: {checksum[:16]}...")
    
    # Обновление VERSION_INFO.json
    if args.update:
        if not req_version or not req_date:
            print("❌ Не удалось извлечь req_version или req_date")
            sys.exit(1)
        
        update_version_info(req_version, req_date, checksum)
        print("\n✅ Snapshot обновлён успешно")
    
    sys.exit(0)


if __name__ == '__main__':
    main()

