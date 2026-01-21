#!/usr/bin/env python3
"""
Скрипт для исправления порядка location блоков в Nginx конфигурации
Перемещает location /health и /status ПЕРЕД location /
"""
import sys
import re

def fix_nginx_config(content: str) -> str:
    """Исправляет порядок location блоков"""
    
    # Находим все location блоки
    location_pattern = r'(location\s+[^{]+)\s*\{[^}]*\}'
    
    # Разделяем на части: до location /, location /, после location /
    lines = content.split('\n')
    
    # Находим индексы location блоков
    locations = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r'\s*location\s+', line):
            # Находим начало блока
            start = i
            brace_count = 0
            j = i
            while j < len(lines):
                brace_count += lines[j].count('{')
                brace_count -= lines[j].count('}')
                if brace_count == 0 and j > start:
                    break
                j += 1
            locations.append((start, j + 1, line.strip()))
            i = j + 1
        else:
            i += 1
    
    # Разделяем на группы
    grpc_location = None
    http_locations = []
    other_locations = []
    
    for start, end, line in locations:
        if line == 'location / {':
            grpc_location = (start, end, lines[start:end])
        elif '/health' in line or '/status' in line:
            http_locations.append((start, end, lines[start:end]))
        else:
            other_locations.append((start, end, lines[start:end]))
    
    if not grpc_location:
        print("❌ Не найден location / блок")
        return content
    
    # Собираем новый конфиг
    result_lines = []
    i = 0
    
    # До первого location
    first_location = min([loc[0] for loc in locations])
    result_lines.extend(lines[:first_location])
    
    # HTTP locations (health, status) ПЕРЕД gRPC
    for start, end, block_lines in http_locations:
        result_lines.extend(block_lines)
        result_lines.append('')
    
    # gRPC location
    result_lines.extend(grpc_location[2])
    result_lines.append('')
    
    # Остальные locations
    for start, end, block_lines in other_locations:
        result_lines.extend(block_lines)
        result_lines.append('')
    
    # Остаток файла
    last_location_end = max([loc[1] for loc in locations])
    result_lines.extend(lines[last_location_end:])
    
    return '\n'.join(result_lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Использование: python3 fix_nginx_location_order.py <input_file> [output_file]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file + '.fixed'
    
    with open(input_file, 'r') as f:
        content = f.read()
    
    fixed = fix_nginx_config(content)
    
    with open(output_file, 'w') as f:
        f.write(fixed)
    
    print(f"✅ Исправленная конфигурация сохранена в: {output_file}")
