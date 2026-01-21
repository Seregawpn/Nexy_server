#!/usr/bin/env python3
"""
Скрипт для проверки состояния first_run (offline и runtime режимы).

ВАЖНО: ApplicationStateManager хранит состояние в памяти.
- Offline режим: проверяет только флаг и логи (единственный источник истины без приложения)
- Runtime режим: проверяет state_manager только в работающем приложении

Использование:
  python3 scripts/check_first_run_state.py          # Offline режим (по умолчанию)
  python3 scripts/check_first_run_state.py --runtime # Runtime режим (требует работающее приложение)
"""

import sys
import os
import re
from pathlib import Path
from typing import Optional

# Добавляем путь к клиенту
client_path = Path(__file__).parent.parent
sys.path.insert(0, str(client_path))

from integration.utils.resource_path import get_user_data_dir


def check_offline_state():
    """Проверка offline состояния (флаг и логи)"""
    print("=== First Run State Check (OFFLINE MODE) ===")
    print("ℹ️  StateManager не проверяется в offline режиме (создаёт новый экземпляр)")
    print("    Единственный источник истины: флаг и логи\n")
    
    # Проверяем флаг файла (канонический)
    data_dir = get_user_data_dir("Nexy")
    flag_file = data_dir / "permissions_first_run_completed.flag"
    
    print("📋 Флаг first-run:")
    print(f"   exists: {flag_file.exists()}")
    if flag_file.exists():
        print(f"   path: {flag_file}")
        print(f"   size: {flag_file.stat().st_size} bytes")
        print("   ✅ First-run завершён (флаг существует)")
    else:
        print("   ⚠️  First-run не завершён (флаг отсутствует)")
    
    # Проверяем restart_completed.flag
    restart_flag_file = data_dir / "restart_completed.flag"
    print(f"\n📋 Флаг restart:")
    print(f"   exists: {restart_flag_file.exists()}")
    if restart_flag_file.exists():
        print(f"   path: {restart_flag_file}")
        print(f"   size: {restart_flag_file.stat().st_size} bytes")
    
    # Проверяем логи на события permissions.*
    log_paths = [
        Path("logs/nexy.log"),
        Path.home() / "nexy_first_run.log",
    ]
    
    print(f"\n📋 События в логах:")
    log_file = None
    for path in log_paths:
        if path.exists():
            log_file = path
            break
    
    if log_file:
        print(f"   log_file: {log_file}")
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                log_content = f.read()
            
            # Ищем события permissions.*
            events = {
                "permissions.first_run_started": len(re.findall(r"permissions\.first_run_started", log_content, re.IGNORECASE)),
                "permissions.first_run_completed": len(re.findall(r"permissions\.first_run_completed", log_content, re.IGNORECASE)),
                "permissions.first_run_restart_pending": len(re.findall(r"permissions\.first_run_restart_pending", log_content, re.IGNORECASE)),
                "permissions.status_checked": len(re.findall(r"📢 Событие опубликовано: permissions\.status_checked", log_content, re.IGNORECASE)),
                "permissions.changed": len(re.findall(r"permissions\.changed", log_content, re.IGNORECASE)),
            }
            
            for event_name, count in events.items():
                if count > 0:
                    print(f"   ✅ {event_name}: {count} вхождений")
                else:
                    print(f"   ⚠️  {event_name}: не найдено")
        except Exception as e:
            print(f"   ❌ Ошибка чтения лога: {e}")
    else:
        print("   ⚠️  Лог-файл не найден")
    
    print("\n" + "="*60)
    print("📝 Примечание:")
    print("   Для проверки runtime state запустите приложение и используйте --runtime")
    print("   или проверьте логи на события permissions.first_run_completed")


def check_runtime_state():
    """Проверка runtime состояния (требует работающее приложение)"""
    print("=== First Run State Check (RUNTIME MODE) ===")
    print("⚠️  Runtime режим требует работающее приложение")
    print("    StateManager проверяется только если интеграции инициализированы\n")
    
    try:
        from integration.core.state_manager import ApplicationStateManager
        
        state_manager = ApplicationStateManager()
        
        print("📋 StateManager состояние:")
        print(f"   first_run_in_progress: {state_manager.get_state_data('first_run_in_progress', False)}")
        print(f"   first_run_required: {state_manager.get_state_data('first_run_required', None)}")
        print(f"   first_run_completed: {state_manager.get_state_data('first_run_completed', False)}")
        print(f"   permissions_restart_pending: {state_manager.get_state_data('permissions_restart_pending', False)}")
        print(f"   update_in_progress: {state_manager.get_state_data('update_in_progress', False)}")
        
        print("\n⚠️  ВАЖНО: State валиден только при активном приложении")
        print("    Это состояние из нового ApplicationStateManager, созданного скриптом")
        print("    Оно отражает runtime-состояние только если интеграции инициализированы в работающем приложении")
        print("    Для проверки фактического состояния используйте offline режим (флаг + логи)")
        
    except Exception as e:
        print(f"❌ Ошибка проверки runtime state: {e}")
        print("   Убедитесь, что приложение запущено и интеграции инициализированы")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Проверка состояния first-run")
    parser.add_argument(
        "--runtime",
        action="store_true",
        help="Runtime режим (проверяет StateManager, требует работающее приложение)"
    )
    
    args = parser.parse_args()
    
    if args.runtime:
        check_runtime_state()
    else:
        check_offline_state()


if __name__ == "__main__":
    main()
