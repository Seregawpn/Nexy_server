#!/usr/bin/env python3
"""
Мониторинг метрик и SLO для Nexy Client

Анализирует логи и метрики, проверяет соответствие SLO порогам,
генерирует отчёты о производительности.

Использование:
    python scripts/monitor_metrics.py [--log-file <file>] [--output <report.json>] [--check-slo]
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from collections import defaultdict

# Цвета для вывода
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color


class MetricsMonitor:
    """Монитор метрик и SLO"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.registry_file = project_root / 'client' / 'metrics' / 'registry.md'
        self.slo_thresholds: Dict[str, Dict[str, Any]] = {}
        self.metrics: Dict[str, List[float]] = defaultdict(list)
        self.report: Dict[str, Any] = {
            'timestamp': datetime.now().isoformat(),
            'metrics': {},
            'slo_violations': [],
            'summary': {}
        }
        
    def load_slo_thresholds(self):
        """Загружает SLO пороги из registry.md"""
        if not self.registry_file.exists():
            print(f"{YELLOW}[WARN]{NC} Metrics registry не найден: {self.registry_file}")
            return
        
        with open(self.registry_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Парсим SLO пороги из таблиц
        # Формат: | `metric_name` | Type | Semantics | Порог SLO (p95) | Source |
        # Используем построчный разбор с regex для надёжного извлечения метрик и порогов
        for line in content.split('\n'):
            # Пропускаем разделители таблицы и заголовки
            if not line.strip() or line.strip().startswith('|---') or ('Метрика' in line and 'Тип' in line):
                continue
            
            # Ищем строки с метриками в обратных кавычках
            # Поддерживаем метрики с дополнительными символами для универсальности:
            # - Фигурные скобки {}: decision_rate{type} (используется в registry.md)
            # - Двоеточия ::
            # - Дефисы -:
            # - Цифры: metric_name_v2
            # Regex паттерн: [a-z0-9_{}:-]+ (буквы, цифры, подчёркивания, фигурные скобки, двоеточия, дефисы)
            metric_match = re.search(r'`([a-z0-9_{}:-]+)`', line)
            if not metric_match:
                continue
            
            metric_name = metric_match.group(1)
            
            # Ищем порог SLO в строке через regex (независимо от разбиения по |)
            # Форматы порогов:
            # - ≤X сек/ms/%/MB
            # - ~X сек (target), ≤Y сек (допустимо)
            # - 0 (в idle-режиме)
            # - 0
            
            threshold_str = None
            
            # Находим позицию метрики для поиска порога после неё
            metric_pos = metric_match.end()
            line_after_metric = line[metric_pos:]
            
            # Паттерн 1: ~X сек (target), ≤Y сек (допустимо) - берём максимальное значение
            # Проверяем сначала сложные пороги
            complex_match = re.search(r'~(\d+(?:\.\d+)?)\s*сек.*?≤\s*(\d+(?:\.\d+)?)\s*сек', line_after_metric, re.IGNORECASE)
            if complex_match:
                # Берём максимальное значение (второе, после ≤)
                max_value = max(float(complex_match.group(1)), float(complex_match.group(2)))
                threshold_str = f"≤{max_value} сек"
            
            # Паттерн 2: ≤X сек/ms/%/MB (простой случай)
            if not threshold_str:
                threshold_match = re.search(r'≤\s*(\d+(?:\.\d+)?)\s*(сек|sec|s|ms|mb|MB|%)', line_after_metric, re.IGNORECASE)
                if threshold_match:
                    threshold_str = f"≤{threshold_match.group(1)} {threshold_match.group(2)}"
            
            # Паттерн 3: 0 (в idle-режиме) или просто 0
            if not threshold_str:
                # Ищем 0 в колонке порога (после третьего |, но ищем в полной строке)
                zero_match = re.search(r'\|[^|]*\|[^|]*\|[^|]*\|\s*0\s*(?:\([^)]+\))?\s*\|', line)
                if zero_match:
                    threshold_str = '0'
            
            if not threshold_str or 'N/A' in threshold_str:
                continue
            
            # Парсим порог
            threshold = self._parse_threshold(threshold_str)
            if threshold:
                self.slo_thresholds[metric_name] = threshold
    
    def _parse_threshold(self, threshold_str: str) -> Optional[Dict[str, Any]]:
        """Парсит строку порога в структуру"""
        threshold_str = threshold_str.lower()
        
        # p95 ≤ X ms/sec
        p95_match = re.search(r'p95\s*≤\s*(\d+(?:\.\d+)?)\s*(ms|sec|s|%)', threshold_str)
        if p95_match:
            value = float(p95_match.group(1))
            unit = p95_match.group(2)
            # Конвертируем в ms
            if unit in ['sec', 's']:
                value *= 1000
            return {'type': 'p95_max', 'value': value, 'unit': 'ms'}
        
        # ≥ X%
        min_match = re.search(r'≥\s*(\d+(?:\.\d+)?)\s*%', threshold_str)
        if min_match:
            value = float(min_match.group(1)) / 100.0
            return {'type': 'min', 'value': value, 'unit': 'rate'}
        
        # Для сложных порогов (например: "~30 сек (target), ≤35 сек (допустимо)") берём максимальное значение
        # Ищем все значения ≤ X (поддерживаем кириллицу "сек" и латиницу "sec"/"s")
        all_max_matches = re.findall(r'≤\s*(\d+(?:\.\d+)?)\s*(ms|sec|s|сек|mb|MB|%)', threshold_str, re.IGNORECASE)
        if all_max_matches:
            # Берём максимальное значение
            max_value = 0
            max_unit = 'ms'
            for value_str, unit_str in all_max_matches:
                value = float(value_str)
                unit = unit_str.lower()
                if unit in ['sec', 's', 'сек']:
                    value *= 1000  # Конвертируем секунды в миллисекунды
                    unit = 'ms'
                if value > max_value:
                    max_value = value
                    max_unit = unit
            
            if max_unit == 'mb':
                return {'type': 'max', 'value': max_value, 'unit': 'mb'}
            elif max_unit == '%':
                return {'type': 'max', 'value': max_value, 'unit': '%'}
            else:
                return {'type': 'max', 'value': max_value, 'unit': 'ms'}
        
        # ≤ X ms/sec/MB (простой случай)
        # Поддерживаем кириллицу "сек" и латиницу "sec"/"s"
        max_match = re.search(r'≤\s*(\d+(?:\.\d+)?)\s*(ms|sec|s|сек|mb|MB|%)', threshold_str, re.IGNORECASE)
        if max_match:
            value = float(max_match.group(1))
            unit = max_match.group(2).lower()
            if unit in ['sec', 's', 'сек']:
                value *= 1000  # Конвертируем секунды в миллисекунды
                return {'type': 'max', 'value': value, 'unit': 'ms'}
            elif unit == 'mb':
                return {'type': 'max', 'value': value, 'unit': 'mb'}
            elif unit == '%':
                return {'type': 'max', 'value': value, 'unit': '%'}
            else:
                return {'type': 'max', 'value': value, 'unit': 'ms'}
        
        # ≤ X% (для процентов без явного указания единицы)
        percent_match = re.search(r'≤\s*(\d+(?:\.\d+)?)\s*%', threshold_str)
        if percent_match:
            value = float(percent_match.group(1))
            return {'type': 'max', 'value': value, 'unit': '%'}
        
        # 0 (для power_assertion_active_count и других строгих нулевых порогов)
        zero_match = re.search(r'^0\s*(?:\([^)]+\))?\s*$', threshold_str.strip())
        if zero_match:
            return {'type': 'max', 'value': 0, 'unit': 'count'}
        
        return None
    
    def parse_log_file(self, log_file: Path):
        """Парсит лог-файл и извлекает метрики"""
        if not log_file.exists():
            print(f"{RED}[ERROR]{NC} Лог-файл не найден: {log_file}")
            return
        
        with open(log_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ищем метрики в формате: metric_name=value или metric_name: value
        for metric_name in self.slo_thresholds.keys():
            # Паттерны для поиска метрик
            # ВАЖНО: Используем только прямые логи метрик (например, tal_hold_duration_ms=1234.56)
            # TAL=refresh/released паттерны удалены, так как теперь есть прямые логи tal_* метрик
            patterns = [
                rf'{metric_name}=(\d+(?:\.\d+)?)',
                rf'{metric_name}:(\d+(?:\.\d+)?)',
                rf'{metric_name}\s*=\s*(\d+(?:\.\d+)?)',
                rf'{metric_name}_ms=(\d+(?:\.\d+)?)',
                rf'{metric_name}_ms:(\d+(?:\.\d+)?)',
            ]
            
            for pattern in patterns:
                matches = re.finditer(pattern, content, re.IGNORECASE)
                for match in matches:
                    try:
                        value = float(match.group(1))
                        self.metrics[metric_name].append(value)
                    except ValueError:
                        continue
    
    def calculate_percentile(self, values: List[float], percentile: int) -> float:
        """Вычисляет перцентиль"""
        if not values:
            return 0.0
        sorted_values = sorted(values)
        index = int(len(sorted_values) * (percentile / 100.0))
        if index >= len(sorted_values):
            index = len(sorted_values) - 1
        return sorted_values[index]
    
    def check_slo(self) -> List[Dict[str, Any]]:
        """Проверяет соответствие метрик SLO порогам"""
        violations = []
        
        for metric_name, threshold in self.slo_thresholds.items():
            values = self.metrics.get(metric_name, [])
            if not values:
                continue
            
            threshold_type = threshold['type']
            threshold_value = threshold['value']
            
            violation = None
            
            if threshold_type == 'p95_max':
                p95 = self.calculate_percentile(values, 95)
                if p95 > threshold_value:
                    violation = {
                        'metric': metric_name,
                        'threshold_type': 'p95_max',
                        'threshold_value': threshold_value,
                        'actual_value': p95,
                        'violation': p95 - threshold_value,
                        'unit': 'ms'
                    }
            elif threshold_type == 'min':
                rate = sum(1 for v in values if v >= 1.0) / len(values) if values else 0.0
                if rate < threshold_value:
                    violation = {
                        'metric': metric_name,
                        'threshold_type': 'min',
                        'threshold_value': threshold_value,
                        'actual_value': rate,
                        'violation': threshold_value - rate,
                        'unit': 'rate'
                    }
            elif threshold_type == 'max':
                max_value = max(values)
                if max_value > threshold_value:
                    violation = {
                        'metric': metric_name,
                        'threshold_type': 'max',
                        'threshold_value': threshold_value,
                        'actual_value': max_value,
                        'violation': max_value - threshold_value,
                        'unit': 'ms'
                    }
            
            if violation:
                violations.append(violation)
        
        return violations
    
    def generate_report(self) -> Dict[str, Any]:
        """Генерирует отчёт о метриках"""
        # Собираем статистику по метрикам
        metrics_stats = {}
        for metric_name, values in self.metrics.items():
            if not values:
                continue
            
            metrics_stats[metric_name] = {
                'count': len(values),
                'min': min(values),
                'max': max(values),
                'avg': sum(values) / len(values),
                'p50': self.calculate_percentile(values, 50),
                'p95': self.calculate_percentile(values, 95),
                'p99': self.calculate_percentile(values, 99),
            }
        
        # Проверяем SLO
        violations = self.check_slo()
        
        self.report['metrics'] = metrics_stats
        self.report['slo_violations'] = violations
        self.report['summary'] = {
            'total_metrics': len(metrics_stats),
            'metrics_with_data': len([m for m in metrics_stats.values() if m['count'] > 0]),
            'slo_violations_count': len(violations),
            'slo_compliance': len(violations) == 0
        }
        
        return self.report
    
    def print_report(self):
        """Выводит отчёт в консоль"""
        print()
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print(f"{GREEN}📊 ОТЧЁТ О МЕТРИКАХ И SLO{NC}")
        print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
        print()
        
        summary = self.report['summary']
        print(f"Всего метрик: {summary['total_metrics']}")
        print(f"Метрик с данными: {summary['metrics_with_data']}")
        print()
        
        # Выводим статистику по метрикам
        if self.report['metrics']:
            print(f"{BLUE}Статистика метрик:{NC}")
            for metric_name, stats in self.report['metrics'].items():
                # Определяем единицу измерения из SLO порога
                unit = 'ms'  # По умолчанию миллисекунды
                if metric_name in self.slo_thresholds:
                    unit = self.slo_thresholds[metric_name].get('unit', 'ms')
                
                print(f"  {metric_name}:")
                print(f"    Количество: {stats['count']}")
                print(f"    Min: {stats['min']:.2f}{unit}")
                print(f"    Max: {stats['max']:.2f}{unit}")
                print(f"    Avg: {stats['avg']:.2f}{unit}")
                print(f"    p50: {stats['p50']:.2f}{unit}")
                print(f"    p95: {stats['p95']:.2f}{unit}")
                print(f"    p99: {stats['p99']:.2f}{unit}")
                print()
        
        # Выводим нарушения SLO
        violations = self.report['slo_violations']
        if violations:
            print(f"{RED}⚠️  Нарушения SLO ({len(violations)}):{NC}")
            for violation in violations:
                print(f"  • {violation['metric']}: {violation['actual_value']:.2f}{violation['unit']} (порог: {violation['threshold_value']:.2f}{violation['unit']}, превышение: {violation['violation']:.2f}{violation['unit']})")
            print()
        else:
            print(f"{GREEN}✅ Все метрики соответствуют SLO порогам{NC}")
            print()
    
    def save_report(self, output_file: Optional[Path] = None):
        """Сохраняет JSON-отчёт"""
        if output_file is None:
            output_file = self.project_root / 'metrics_report.json'
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.report, f, indent=2, ensure_ascii=False)
            print(f"{GREEN}[INFO]{NC} Отчёт сохранён: {output_file}")
        except Exception as e:
            print(f"{RED}[ERROR]{NC} Ошибка сохранения отчёта: {e}")


def main():
    parser = argparse.ArgumentParser(description='Мониторинг метрик и SLO для Nexy Client')
    parser.add_argument('--log-file', type=str, help='Путь к лог-файлу для анализа')
    parser.add_argument('--output', type=str, help='Путь к файлу для сохранения JSON-отчёта')
    parser.add_argument('--check-slo', action='store_true', help='Проверить соответствие SLO и выйти с кодом ошибки при нарушениях')
    args = parser.parse_args()
    
    # Определяем корень проекта
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Создаём монитор
    monitor = MetricsMonitor(project_root)
    
    # Загружаем SLO пороги
    monitor.load_slo_thresholds()
    
    # Парсим лог-файл если указан
    if args.log_file:
        log_file = Path(args.log_file)
        monitor.parse_log_file(log_file)
    else:
        # Пробуем найти последний лог
        log_files = list(project_root.glob('log*.md'))
        if log_files:
            latest_log = max(log_files, key=lambda p: p.stat().st_mtime)
            print(f"{BLUE}[INFO]{NC} Используется последний лог: {latest_log}")
            monitor.parse_log_file(latest_log)
        else:
            print(f"{YELLOW}[WARN]{NC} Лог-файлы не найдены, метрики не будут извлечены")
    
    # Генерируем отчёт
    report = monitor.generate_report()
    
    # Выводим отчёт
    monitor.print_report()
    
    # Сохраняем отчёт
    output_file = Path(args.output) if args.output else None
    monitor.save_report(output_file)
    
    # Проверяем SLO если требуется
    if args.check_slo:
        if not report['summary']['slo_compliance']:
            print(f"{RED}[ERROR]{NC} Обнаружены нарушения SLO!")
            sys.exit(1)
        else:
            print(f"{GREEN}[INFO]{NC} Все метрики соответствуют SLO порогам")
            sys.exit(0)
    
    sys.exit(0)


if __name__ == '__main__':
    main()

