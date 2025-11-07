#!/usr/bin/env python3
"""
Скрипт для удаления флагов первого запуска приложения.
Удаляет:
- permissions_first_run_completed.flag (из Application Support)
- restart_completed.flag (из Caches)
"""

import sys
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

from integration.utils.resource_path import get_user_data_dir, get_user_cache_dir

def clear_first_run_flags():
    """Удаляет все флаги первого запуска"""
    print("🧹 Удаление флагов первого запуска...")
    
    # Флаг завершения первого запуска
    data_dir = get_user_data_dir("Nexy")
    flag_file = data_dir / "permissions_first_run_completed.flag"
    
    # Флаг завершения перезапуска
    cache_dir = get_user_cache_dir("Nexy")
    restart_flag = cache_dir / "restart_completed.flag"
    
    removed_count = 0
    
    # Удаляем permissions_first_run_completed.flag
    if flag_file.exists():
        try:
            flag_file.unlink()
            print(f"✅ Удалён: {flag_file}")
            removed_count += 1
        except Exception as e:
            print(f"❌ Ошибка удаления {flag_file}: {e}")
    else:
        print(f"ℹ️  Файл не найден: {flag_file}")
    
    # Удаляем restart_completed.flag
    if restart_flag.exists():
        try:
            restart_flag.unlink()
            print(f"✅ Удалён: {restart_flag}")
            removed_count += 1
        except Exception as e:
            print(f"❌ Ошибка удаления {restart_flag}: {e}")
    else:
        print(f"ℹ️  Файл не найден: {restart_flag}")
    
    if removed_count > 0:
        print(f"\n✅ Удалено флагов: {removed_count}")
        print("ℹ️  При следующем запуске приложение будет работать как при первом запуске")
    else:
        print("\nℹ️  Флаги первого запуска не найдены (возможно, уже были удалены)")
    
    return removed_count

if __name__ == "__main__":
    try:
        clear_first_run_flags()
    except Exception as e:
        print(f"❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

