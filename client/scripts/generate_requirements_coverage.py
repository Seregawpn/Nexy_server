#!/usr/bin/env python3
"""
Генерация отчёта о покрытии требований

Анализирует PROJECT_REQUIREMENTS.md и проверяет, какие требования имеют
реализацию и тесты, а какие нет.

Использование:
    python scripts/generate_requirements_coverage.py [--output <file.json>]

Возвращает JSON-отчёт с покрытием требований.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color


class RequirementsCoverageAnalyzer:
    """Анализатор покрытия требований"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.requirements_file = project_root / 'Docs' / 'PROJECT_REQUIREMENTS.md'
        self.coverage: Dict[str, Any] = {
            'timestamp': datetime.now().isoformat(),
            'total_requirements': 0,
            'with_implementation': 0,
            'with_verification': 0,
            'with_both': 0,
            'without_implementation': 0,
            'without_verification': 0,
            'gaps': [],
            'requirements': []
        }
        
    def log_info(self, message: str):
        """Логирует информационное сообщение"""
        print(f"{GREEN}[INFO]{NC} {message}")
    
    def log_warn(self, message: str):
        """Логирует предупреждение"""
        print(f"{YELLOW}[WARN]{NC} {message}")
    
    def extract_requirements(self) -> List[Dict[str, Any]]:
        """Извлекает все требования из PROJECT_REQUIREMENTS.md"""
        if not self.requirements_file.exists():
            self.log_warn(f"PROJECT_REQUIREMENTS.md не найден: {self.requirements_file}")
            return []
        
        with open(self.requirements_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        requirements = []
        
        # Паттерн для поиска требований
        req_pattern = r'### (REQ-\d{3}):\s*(.+?)(?=### REQ-|\Z)'
        matches = re.finditer(req_pattern, content, re.DOTALL)
        
        for match in matches:
            req_id = match.group(1)
            req_content = match.group(2)
            
            # Извлекаем поля
            domain_match = re.search(r'- \*\*Домен\*\*:\s*(.+)', req_content)
            criticality_match = re.search(r'- \*\*Критичность\*\*:\s*(.+)', req_content)
            description_match = re.search(r'- \*\*Описание\*\*:\s*(.+)', req_content)
            implementation_match = re.search(r'- \*\*Implementation\*\*:\s*(.+)', req_content)
            verification_match = re.search(r'- \*\*Verification\*\*:\s*(.+)', req_content)
            
            req = {
                'id': req_id,
                'domain': domain_match.group(1).strip() if domain_match else None,
                'criticality': criticality_match.group(1).strip() if criticality_match else None,
                'description': description_match.group(1).strip() if description_match else None,
                'implementation': implementation_match.group(1).strip() if implementation_match else None,
                'verification': verification_match.group(1).strip() if verification_match else None,
                'has_implementation': bool(implementation_match),
                'has_verification': bool(verification_match),
            }
            
            requirements.append(req)
        
        return requirements
    
    def check_file_exists(self, file_path_str: str) -> bool:
        """Проверяет существование файла (упрощённая версия)"""
        if not file_path_str:
            return False
        
        # Очищаем путь от markdown форматирования
        file_path_str = file_path_str.strip().replace('`', '')
        
        # Пропускаем описательные тексты
        if any(skip in file_path_str.lower() for skip in ['см.', 'см', 'reference', 'ссылка', 'например', 'если есть', 'логи', 'ревью', 'проверка']):
            return False
        
        # Если путь относительный, делаем его абсолютным
        if not file_path_str.startswith('/'):
            full_path = self.project_root / file_path_str
        else:
            full_path = Path(file_path_str)
        
        return full_path.exists()
    
    def analyze_coverage(self):
        """Анализирует покрытие требований"""
        self.log_info("Анализ покрытия требований...")
        
        requirements = self.extract_requirements()
        self.coverage['total_requirements'] = len(requirements)
        
        for req in requirements:
            has_impl = req['has_implementation']
            has_verif = req['has_verification']
            
            # Проверяем существование файлов (упрощённо)
            impl_exists = False
            verif_exists = False
            
            if has_impl and req['implementation']:
                # Разбиваем на отдельные пути
                impl_paths = re.split(r'[,;]', req['implementation'])
                impl_exists = any(self.check_file_exists(p.strip()) for p in impl_paths if p.strip())
            
            if has_verif and req['verification']:
                # Разбиваем на отдельные пути
                verif_paths = re.split(r'[,;]', req['verification'])
                verif_exists = any(self.check_file_exists(p.strip()) for p in verif_paths if p.strip())
            
            req['implementation_exists'] = impl_exists
            req['verification_exists'] = verif_exists
            
            # Подсчитываем статистику
            if has_impl:
                self.coverage['with_implementation'] += 1
            else:
                self.coverage['without_implementation'] += 1
                self.coverage['gaps'].append({
                    'requirement': req['id'],
                    'type': 'missing_implementation',
                    'domain': req['domain'],
                    'criticality': req['criticality']
                })
            
            if has_verif:
                self.coverage['with_verification'] += 1
            else:
                self.coverage['without_verification'] += 1
                if req['id'] not in [g['requirement'] for g in self.coverage['gaps']]:
                    self.coverage['gaps'].append({
                        'requirement': req['id'],
                        'type': 'missing_verification',
                        'domain': req['domain'],
                        'criticality': req['criticality']
                    })
            
            if has_impl and has_verif:
                self.coverage['with_both'] += 1
            
            self.coverage['requirements'].append(req)
        
        # Вычисляем проценты
        total = self.coverage['total_requirements']
        if total > 0:
            self.coverage['implementation_coverage_percent'] = round(
                (self.coverage['with_implementation'] / total) * 100, 2
            )
            self.coverage['verification_coverage_percent'] = round(
                (self.coverage['with_verification'] / total) * 100, 2
            )
            self.coverage['both_coverage_percent'] = round(
                (self.coverage['with_both'] / total) * 100, 2
            )
        else:
            self.coverage['implementation_coverage_percent'] = 0
            self.coverage['verification_coverage_percent'] = 0
            self.coverage['both_coverage_percent'] = 0
    
    def print_summary(self):
        """Выводит сводку покрытия"""
        print()
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{GREEN}📊 ОТЧЁТ О ПОКРЫТИИ ТРЕБОВАНИЙ{NC}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print()
        
        total = self.coverage['total_requirements']
        print(f"Всего требований: {total}")
        print()
        
        print(f"Покрытие Implementation:")
        print(f"  ✅ С Implementation: {self.coverage['with_implementation']} ({self.coverage.get('implementation_coverage_percent', 0)}%)")
        print(f"  ❌ Без Implementation: {self.coverage['without_implementation']}")
        print()
        
        print(f"Покрытие Verification:")
        print(f"  ✅ С Verification: {self.coverage['with_verification']} ({self.coverage.get('verification_coverage_percent', 0)}%)")
        print(f"  ❌ Без Verification: {self.coverage['without_verification']}")
        print()
        
        print(f"Полное покрытие (Implementation + Verification):")
        print(f"  ✅ С обоими: {self.coverage['with_both']} ({self.coverage.get('both_coverage_percent', 0)}%)")
        print()
        
        if self.coverage['gaps']:
            print(f"{YELLOW}⚠️  Обнаружены GAP'ы ({len(self.coverage['gaps'])}):{NC}")
            for gap in self.coverage['gaps']:
                print(f"  • {gap['requirement']}: {gap['type']} ({gap['domain']}, {gap['criticality']})")
            print()
        else:
            print(f"{GREEN}✅ Все требования имеют Implementation и Verification{NC}")
            print()
    
    def save_report(self, output_file: Optional[Path] = None):
        """Сохраняет JSON-отчёт"""
        if output_file is None:
            output_file = self.project_root / 'requirements_coverage_report.json'
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.coverage, f, indent=2, ensure_ascii=False)
            self.log_info(f"📄 Отчёт сохранён: {output_file}")
        except Exception as e:
            print(f"{RED}[ERROR]{NC} Ошибка сохранения отчёта: {e}")


def main():
    parser = argparse.ArgumentParser(description='Генерация отчёта о покрытии требований')
    parser.add_argument('--output', type=str, help='Путь к файлу для сохранения JSON-отчёта')
    args = parser.parse_args()
    
    # Определяем корень проекта
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Создаём анализатор
    analyzer = RequirementsCoverageAnalyzer(project_root)
    
    # Анализируем покрытие
    analyzer.analyze_coverage()
    
    # Выводим сводку
    analyzer.print_summary()
    
    # Сохраняем отчёт
    output_file = Path(args.output) if args.output else None
    analyzer.save_report(output_file)
    
    sys.exit(0)


if __name__ == '__main__':
    main()

