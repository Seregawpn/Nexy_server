#!/usr/bin/env python3
"""
Скрипт для проверки TAL hold после перезапуска приложения.

Проверяет логи на наличие:
1. TAL=hold после перезапуска
2. TAL=refresh (периодическое обновление)
3. TAL=released (после tray.ready)
4. Assertion did invalidate due to timeout (не должно быть до tray.ready)
5. Entering exit handler (не должно быть до tray.ready)
"""

import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Результаты проверки
results = {
    "tal_hold_found": False,
    "tal_refresh_found": False,
    "tal_released_found": False,
    "tray_ready_found": False,
    "assertion_timeout_found": False,
    "exit_handler_found": False,
    "restart_detected": False,
    "timeline": []
}

def parse_log_line(line: str) -> Optional[Dict]:
    """Парсит строку лога и извлекает события"""
    if not line.strip():
        return None
    
    # Извлекаем время и процесс
    time_match = re.search(r'(\d{2}:\d{2}:\d{2}\.\d+)', line)
    timestamp = time_match.group(1) if time_match else None
    
    # Проверяем процесс
    is_nexy = "Nexy" in line and "default" in line
    is_runningboardd = "runningboardd" in line and "default" in line
    
    event = None
    
    # TAL=hold
    if "TAL=hold" in line:
        event = {
            "type": "tal_hold",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["tal_hold_found"] = True
    
    # TAL=refresh
    elif "TAL=refresh" in line:
        event = {
            "type": "tal_refresh",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["tal_refresh_found"] = True
    
    # TAL=released
    elif "TAL=released" in line:
        event = {
            "type": "tal_released",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["tal_released_found"] = True
        # Извлекаем duration из лога
        duration_match = re.search(r'duration=([\d.]+)s', line)
        if duration_match:
            event["duration"] = float(duration_match.group(1))
    
    # tray.ready или TRAY_READY
    elif ("tray.ready" in line.lower() or "tray ready" in line.lower() or 
          "TRAY_READY" in line or "TrayControllerIntegration запущен" in line):
        event = {
            "type": "tray_ready",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["tray_ready_found"] = True
    
    # Перезапуск
    elif "launching:" in line and "Nexy.app" in line:
        event = {
            "type": "restart",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["restart_detected"] = True
    
    # Assertion timeout
    elif "Assertion did invalidate due to timeout" in line and "com.nexy.assistant" in line:
        event = {
            "type": "assertion_timeout",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["assertion_timeout_found"] = True
    
    # Exit handler
    elif "Entering exit handler" in line:
        event = {
            "type": "exit_handler",
            "timestamp": timestamp,
            "line": line.strip()
        }
        results["exit_handler_found"] = True
    
    # App is holding power assertion
    elif "App is holding power assertion" in line and "com.nexy.assistant" in line:
        event = {
            "type": "power_assertion",
            "timestamp": timestamp,
            "line": line.strip()
        }
    
    # Termination reported
    elif "termination reported by launchd" in line and "com.nexy.assistant" in line:
        event = {
            "type": "termination",
            "timestamp": timestamp,
            "line": line.strip()
        }
    
    if event:
        event["source"] = "nexy" if is_nexy else "runningboardd" if is_runningboardd else "other"
        return event
    
    return None

def analyze_log_file(log_file: str) -> Dict:
    """Анализирует лог-файл и возвращает результаты"""
    print("="*80)
    print("АНАЛИЗ ЛОГОВ: TAL HOLD ПОСЛЕ ПЕРЕЗАПУСКА")
    print("="*80)
    print(f"\nАнализирую файл: {log_file}\n")
    
    if not Path(log_file).exists():
        print(f"❌ Файл не найден: {log_file}")
        return results
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            event = parse_log_line(line)
            if event:
                results["timeline"].append(event)
    
    return results

def print_analysis(results: Dict):
    """Выводит результаты анализа"""
    print("\n" + "="*80)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА")
    print("="*80)
    
    # Проверка перезапуска
    if results["restart_detected"]:
        print("✅ Перезапуск обнаружен")
    else:
        print("⚠️ Перезапуск не обнаружен (возможно, лог не содержит перезапуск)")
    
    # Проверка TAL hold
    print(f"\n📊 TAL HOLD:")
    print(f"  TAL=hold: {'✅ НАЙДЕН' if results['tal_hold_found'] else '❌ НЕ НАЙДЕН'}")
    print(f"  TAL=refresh: {'✅ НАЙДЕН' if results['tal_refresh_found'] else '❌ НЕ НАЙДЕН'}")
    print(f"  TAL=released: {'✅ НАЙДЕН' if results['tal_released_found'] else '⚠️ НЕ НАЙДЕН (возможно, tray ещё не готов)'}")
    
    # Проверка tray ready
    print(f"\n📊 TRAY READY:")
    print(f"  tray.ready: {'✅ НАЙДЕН' if results['tray_ready_found'] else '❌ НЕ НАЙДЕН'}")
    
    # Проверка проблем
    print(f"\n📊 ПРОБЛЕМЫ:")
    print(f"  Assertion timeout: {'❌ НАЙДЕН (ПРОБЛЕМА!)' if results['assertion_timeout_found'] else '✅ НЕ НАЙДЕН'}")
    print(f"  Exit handler: {'❌ НАЙДЕН (ПРОБЛЕМА!)' if results['exit_handler_found'] else '✅ НЕ НАЙДЕН'}")
    
    # Временная шкала
    if results["timeline"]:
        print(f"\n📊 ВРЕМЕННАЯ ШКАЛА (первые 30 событий):")
        for i, event in enumerate(results["timeline"][:30]):
            timestamp = event.get("timestamp", "??:??:??")
            event_type = event.get("type", "unknown")
            source = event.get("source", "unknown")
            extra = ""
            if event_type == "tal_released" and "duration" in event:
                extra = f" (duration={event['duration']:.1f}s)"
            elif event_type == "tal_refresh" and "elapsed" in event.get("line", ""):
                elapsed_match = re.search(r'elapsed=([\d.]+)s', event.get("line", ""))
                if elapsed_match:
                    extra = f" (elapsed={elapsed_match.group(1)}s)"
            print(f"  {i+1:2d}. [{timestamp}] {event_type:20s} ({source}){extra}")
        
        if len(results["timeline"]) > 30:
            print(f"  ... и ещё {len(results['timeline']) - 30} событий")
        
        # Анализ временных интервалов
        restart_events = [e for e in results["timeline"] if e.get("type") == "restart"]
        tal_hold_events = [e for e in results["timeline"] if e.get("type") == "tal_hold"]
        tal_refresh_events = [e for e in results["timeline"] if e.get("type") == "tal_refresh"]
        tray_ready_events = [e for e in results["timeline"] if e.get("type") == "tray_ready"]
        timeout_events = [e for e in results["timeline"] if e.get("type") == "assertion_timeout"]
        
        if restart_events and tal_hold_events:
            print(f"\n📊 АНАЛИЗ ВРЕМЕННЫХ ИНТЕРВАЛОВ:")
            restart_time = restart_events[0].get("timestamp", "")
            tal_hold_time = tal_hold_events[0].get("timestamp", "")
            print(f"  Перезапуск → TAL=hold: {restart_time} → {tal_hold_time}")
            
            if tal_refresh_events:
                print(f"  TAL=refresh событий: {len(tal_refresh_events)}")
                if len(tal_refresh_events) > 1:
                    print(f"  Первый refresh: {tal_refresh_events[0].get('timestamp', '')}")
                    print(f"  Последний refresh: {tal_refresh_events[-1].get('timestamp', '')}")
            
            if tray_ready_events:
                tray_ready_time = tray_ready_events[0].get("timestamp", "")
                print(f"  TAL=hold → tray.ready: {tal_hold_time} → {tray_ready_time}")
            
            if timeout_events:
                timeout_time = timeout_events[0].get("timestamp", "")
                print(f"  ⚠️ Assertion timeout: {timeout_time}")
                if tal_hold_events:
                    print(f"  ⚠️ TAL=hold → timeout: {tal_hold_time} → {timeout_time}")
    
    # Вывод
    print("\n" + "="*80)
    print("ВЫВОД")
    print("="*80)
    
    if results["restart_detected"]:
        if results["tal_hold_found"]:
            if results["assertion_timeout_found"]:
                print("❌ ПРОБЛЕМА: TAL hold установлен, но assertion всё равно истёк")
                print("   Возможно, периодическое обновление не работает")
            elif results["exit_handler_found"] and not results["tray_ready_found"]:
                print("❌ ПРОБЛЕМА: Приложение завершилось до tray.ready")
                print("   TAL hold установлен, но приложение всё равно завершилось")
            elif results["tray_ready_found"]:
                print("✅ ИСПРАВЛЕНИЕ РАБОТАЕТ:")
                print("   - TAL hold установлен после перезапуска")
                print("   - Tray icon готов")
                print("   - Нет assertion timeout до tray.ready")
                if results["tal_refresh_found"]:
                    print("   - Периодическое обновление работает")
            else:
                print("⚠️ ЧАСТИЧНО РАБОТАЕТ:")
                print("   - TAL hold установлен")
                print("   - Tray icon ещё не готов (возможно, лог обрезан)")
        else:
            print("❌ КРИТИЧЕСКАЯ ПРОБЛЕМА:")
            print("   - TAL hold НЕ установлен после перезапуска")
            print("   - Это причина завершения приложения")
            if results["assertion_timeout_found"]:
                print("   - Assertion истёк (подтверждает проблему)")
    else:
        print("⚠️ Перезапуск не обнаружен в логах")
        print("   Запустите приложение и дождитесь перезапуска после получения разрешений")
    
    print("\n" + "="*80)

def main():
    """Главная функция"""
    if len(sys.argv) < 2:
        print("Использование: python3 check_tal_after_restart.py <log_file>")
        print("\nПример:")
        print("  python3 check_tal_after_restart.py log.md")
        print("  python3 check_tal_after_restart.py /path/to/log.md")
        sys.exit(1)
    
    log_file = sys.argv[1]
    results = analyze_log_file(log_file)
    print_analysis(results)
    
    # Возвращаем код выхода
    if results["restart_detected"]:
        if results["tal_hold_found"] and not results["assertion_timeout_found"]:
            sys.exit(0)  # Всё хорошо
        else:
            sys.exit(1)  # Есть проблемы
    else:
        sys.exit(2)  # Перезапуск не обнаружен

if __name__ == "__main__":
    main()

