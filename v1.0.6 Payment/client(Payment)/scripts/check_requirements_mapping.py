#!/usr/bin/env python3
"""
Скрипт для проверки соответствия требований из PROJECT_REQUIREMENTS.md
реализации (Implementation) и тестам (Verification).

Использование:
    python scripts/check_requirements_mapping.py
"""

import re
import sys
from pathlib import Path

# Пути к файлам
PROJECT_ROOT = Path(__file__).parent.parent
REQUIREMENTS_FILE = PROJECT_ROOT / "Docs" / "PROJECT_REQUIREMENTS.md"


def extract_requirements(content: str) -> list:
    """Извлекает все требования из PROJECT_REQUIREMENTS.md."""
    requirements = []
    
    # Паттерн для поиска требований
    req_pattern = r'### (REQ-\d{3}):\s*(.+?)(?=### REQ-|\Z)'
    matches = re.finditer(req_pattern, content, re.DOTALL)
    
    for match in matches:
        req_id = match.group(1)
        req_content = match.group(2)
        
        # Извлекаем поля
        domain_match = re.search(r'- \*\*Домен\*\*:\s*(.+)', req_content)
        implementation_match = re.search(r'- \*\*Implementation\*\*:\s*(.+)', req_content)
        verification_match = re.search(r'- \*\*Verification\*\*:\s*(.+)', req_content)
        
        req = {
            'id': req_id,
            'domain': domain_match.group(1).strip() if domain_match else None,
            'implementation': implementation_match.group(1).strip() if implementation_match else None,
            'verification': verification_match.group(1).strip() if verification_match else None,
        }
        
        requirements.append(req)
    
    return requirements


def check_file_exists(file_path_str: str, project_root: Path) -> tuple[bool, str]:
    """Проверяет существование файла или директории."""
    # Очищаем путь от markdown форматирования и лишних символов
    file_path_str = file_path_str.strip()
    # Убираем обратные кавычки
    file_path_str = file_path_str.replace('`', '')
    
    # Разбиваем на несколько путей (могут быть перечислены через запятую)
    paths = [p.strip() for p in file_path_str.split(',')]
    
    results = []
    for path_str in paths:
        # Убираем возможные префиксы типа "см. " или "ссылка на "
        path_str = re.sub(r'^(см\.|ссылка на|см|reference to)\s+', '', path_str, flags=re.IGNORECASE)
        path_str = path_str.strip()
        
        # Если путь относительный, делаем его абсолютным
        if not path_str.startswith('/'):
            full_path = project_root / path_str
        else:
            full_path = Path(path_str)
        
        exists = full_path.exists()
        results.append((exists, str(full_path)))
    
    # Возвращаем True, если хотя бы один путь существует
    return any(r[0] for r in results), ', '.join(r[1] for r in results)


def check_implementation_files(implementation: str, project_root: Path) -> list:
    """Проверяет существование файлов из Implementation."""
    errors = []
    
    if not implementation:
        return errors
    
    # Разбиваем на отдельные пути (могут быть перечислены через запятую или точку с запятой)
    paths = re.split(r'[,;]', implementation)
    
    for path_str in paths:
        path_str = path_str.strip()
        if not path_str:
            continue
        
        # Убираем markdown форматирование
        path_str = path_str.replace('`', '').strip()
        
        # Пропускаем описательные тексты
        if any(skip in path_str.lower() for skip in ['см.', 'см', 'reference', 'ссылка', 'например']):
            continue
        
        exists, full_path = check_file_exists(path_str, project_root)
        if not exists:
            errors.append(f"   - {path_str} (путь: {full_path})")
    
    return errors


def check_verification_files(verification: str, project_root: Path) -> list:
    """Проверяет существование файлов/тестов из Verification."""
    errors = []
    
    if not verification:
        return errors
    
    # Разбиваем на отдельные пути
    paths = re.split(r'[,;]', verification)
    
    for path_str in paths:
        path_str = path_str.strip()
        if not path_str:
            continue
        
        # Убираем markdown форматирование
        path_str = path_str.replace('`', '').strip()
        
        # Пропускаем описательные тексты
        if any(skip in path_str.lower() for skip in ['см.', 'см', 'reference', 'ссылка', 'например', 'если есть']):
            continue
        
        # Пропускаем общие описания типа "Логи ошибок", "Ревью кода"
        if any(skip in path_str.lower() for skip in ['логи', 'ревью', 'проверка', 'logs', 'review']):
            continue
        
        exists, full_path = check_file_exists(path_str, project_root)
        if not exists:
            errors.append(f"   - {path_str} (путь: {full_path})")
    
    return errors


def main():
    # Читаем PROJECT_REQUIREMENTS.md
    if not REQUIREMENTS_FILE.exists():
        print(f"❌ Файл не найден: {REQUIREMENTS_FILE}")
        sys.exit(1)
    
    with open(REQUIREMENTS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Извлекаем требования
    requirements = extract_requirements(content)
    
    if not requirements:
        print("❌ Не найдено ни одного требования в PROJECT_REQUIREMENTS.md")
        sys.exit(1)
    
    print(f"📋 Найдено требований: {len(requirements)}\n")
    
    # Проверяем каждое требование
    all_errors = []
    missing_impl = []
    missing_verif = []
    
    for req in requirements:
        req_id = req['id']
        impl = req['implementation']
        verif = req['verification']
        
        impl_errors = check_implementation_files(impl, PROJECT_ROOT) if impl else []
        verif_errors = check_verification_files(verif, PROJECT_ROOT) if verif else []
        
        if impl_errors:
            missing_impl.append(req_id)
            all_errors.append(f"\n{req_id} (Implementation):")
            all_errors.extend(impl_errors)
        
        if verif_errors:
            missing_verif.append(req_id)
            all_errors.append(f"\n{req_id} (Verification):")
            all_errors.extend(verif_errors)
    
    # Выводим результаты
    if all_errors:
        print("❌ Найдены отсутствующие файлы/тесты:\n")
        for error in all_errors:
            print(error)
        
        print(f"\n📊 Статистика:")
        print(f"   Требований с отсутствующими Implementation: {len(missing_impl)}")
        print(f"   Требований с отсутствующими Verification: {len(missing_verif)}")
        print(f"\n⚠️  Некоторые файлы могут быть описательными ссылками или опциональными.")
        print(f"    Проверьте вручную требования с ошибками.")
        
        sys.exit(1)
    else:
        print("✅ Все файлы из Implementation и Verification существуют")
        print(f"   Проверено требований: {len(requirements)}")
        sys.exit(0)


if __name__ == '__main__':
    main()

