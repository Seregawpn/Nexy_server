#!/usr/bin/env python3
"""
Скрипт для проверки состояния first_run через state_manager.
Используется для интеграционных проверок.
"""

import sys
import os
from pathlib import Path

# Добавляем путь к клиенту
client_path = Path(__file__).parent.parent
sys.path.insert(0, str(client_path))

from integration.core.state_manager import ApplicationStateManager

def main():
    state_manager = ApplicationStateManager()
    
    print("=== First Run State Check ===")
    print(f"first_run_required: {state_manager.get_state_data('first_run_required', None)}")
    print(f"first_run_completed: {state_manager.get_state_data('first_run_completed', False)}")
    print(f"permissions_restart_pending: {state_manager.get_state_data('permissions_restart_pending', False)}")
    print(f"update_in_progress: {state_manager.get_state_data('update_in_progress', False)}")
    
    # Проверяем флаг файла
    flag_file = Path.home() / "Library/Application Support/Nexy/permissions_first_run_completed.flag"
    print(f"\nFlag file exists: {flag_file.exists()}")
    if flag_file.exists():
        print(f"Flag file path: {flag_file}")
        print(f"Flag file size: {flag_file.stat().st_size} bytes")

if __name__ == "__main__":
    main()

