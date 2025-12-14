#!/usr/bin/env python3
"""
Скрипт для проверки логов запуска приложения
Цель: найти логи инициализации AVF в логах запуска
"""
import sys
import re
from pathlib import Path

def check_log_file(log_file_path: str):
    """Проверяет лог-файл на наличие логов инициализации"""
    log_path = Path(log_file_path)
    
    if not log_path.exists():
        print(f"❌ Файл не найден: {log_file_path}")
        return
    
    print(f"\n{'='*80}")
    print(f"🔍 ПРОВЕРКА ЛОГОВ: {log_file_path}")
    print(f"{'='*80}")
    
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    print(f"\n📊 Общая информация:")
    print(f"   - Всего строк: {len(lines)}")
    print(f"   - Первые 50 строк будут проверены на логи инициализации")
    
    # Ключевые логи для поиска
    expected_logs = [
        ("🔍 [AUDIO_DEBUG] VoiceRecognitionIntegration.initialize() ВЫЗВАН", "Вызов initialize()"),
        ("🔧 Инициализация voice_recognition", "Инициализация voice_recognition в Coordinator"),
        ("✅ voice_recognition инициализирован", "voice_recognition инициализирован"),
        ("🔍 [AVF] Начало инициализации AVF", "Начало инициализации AVF"),
        ("🔍 [AVF] UnifiedConfigLoader создан", "UnifiedConfigLoader создан"),
        ("🔍 [AVF] audio_config загружен", "audio_config загружен"),
        ("🔍 [AVF] avf_config загружен", "avf_config загружен"),
        ("🔍 [AVF] avf.enabled=", "avf.enabled проверка"),
        ("🔍 [AVF] _use_avf вычислен", "_use_avf вычислен"),
        ("✅ [AVF] AVFAudioEngine инициализирован", "AVFAudioEngine инициализирован (успех)"),
        ("❌ [AVF] Ошибка создания AVFAudioEngine", "AVFAudioEngine ошибка"),
        ("ℹ️ [AVF] AVFoundation аудиосистема отключена", "AVF отключен"),
        ("✅ AVFAudioEngine получен из VoiceRecognitionIntegration", "AVFAudioEngine получен в Coordinator"),
        ("⚠️ VoiceRecognitionIntegration._avf_engine = None", "AVFAudioEngine не создан"),
    ]
    
    # Проверяем первые 100 строк (логи инициализации должны быть в начале)
    search_lines = lines[:100]
    
    print(f"\n📋 Проверка логов инициализации (первые 100 строк):")
    found_logs = []
    missing_logs = []
    
    for log_pattern, description in expected_logs:
        found = False
        found_line = None
        for i, line in enumerate(search_lines):
            if log_pattern in line:
                found = True
                found_line = i + 1
                break
        
        if found:
            found_logs.append((description, found_line))
            print(f"   ✅ {description} (строка {found_line})")
        else:
            missing_logs.append(description)
            print(f"   ❌ {description} - НЕ НАЙДЕН")
    
    print(f"\n📊 ИТОГИ:")
    print(f"   - Найдено логов: {len(found_logs)}/{len(expected_logs)}")
    print(f"   - Отсутствует логов: {len(missing_logs)}/{len(expected_logs)}")
    
    if missing_logs:
        print(f"\n   ⚠️ Отсутствующие логи:")
        for log in missing_logs:
            print(f"      - {log}")
    
    # Проверяем критичные логи
    critical_missing = []
    if "🔍 [AUDIO_DEBUG] VoiceRecognitionIntegration.initialize() ВЫЗВАН" not in ''.join(search_lines):
        critical_missing.append("Вызов initialize()")
    if "🔍 [AVF] Начало инициализации AVF" not in ''.join(search_lines):
        critical_missing.append("Начало инициализации AVF")
    
    if critical_missing:
        print(f"\n   ❌ КРИТИЧНО: Отсутствуют критичные логи:")
        for log in critical_missing:
            print(f"      - {log}")
        print(f"\n   ⚠️ ВОЗМОЖНЫЕ ПРИЧИНЫ:")
        print(f"      1. initialize() не вызывается при запуске приложения")
        print(f"      2. Логи инициализации находятся после строки 100")
        print(f"      3. Логирование не работает или фильтруется")
    
    # Показываем первые 20 строк для контекста
    print(f"\n📋 Первые 20 строк логов (для контекста):")
    for i, line in enumerate(lines[:20], 1):
        print(f"   {i:3d}: {line.rstrip()}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        log_file = sys.argv[1]
    else:
        # Пробуем найти последний лог-файл
        log_dir = Path.home() / "Library/Logs/Nexy"
        if log_dir.exists():
            log_files = sorted(log_dir.glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
            if log_files:
                log_file = str(log_files[0])
                print(f"📁 Найден последний лог-файл: {log_file}")
            else:
                print("❌ Лог-файлы не найдены")
                print("Использование: python scripts/check_startup_logs.py <путь_к_лог_файлу>")
                sys.exit(1)
        else:
            print("❌ Директория логов не найдена")
            print("Использование: python scripts/check_startup_logs.py <путь_к_лог_файлу>")
            sys.exit(1)
    
    check_log_file(log_file)

