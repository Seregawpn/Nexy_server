#!/usr/bin/env python3
"""
Скрипт для очистки флагов первого запуска приложения Nexy.

Удаляет все флаги, связанные с first_run, чтобы можно было заново пройти процедуру первого запуска.
"""

import sys
import os
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

from integration.utils.resource_path import get_user_data_dir, get_user_cache_dir

def clear_flags():
    """Очищает все флаги первого запуска"""
    print("🧹 Очистка флагов первого запуска...")
    print("=" * 60)
    
    cleared_count = 0
    checked_paths = []
    
    # 1. Очистка permissions_first_run_completed.flag
    print("\n📋 Проверка permissions_first_run_completed.flag:")
    
    # Стандартный путь
    data_dir = get_user_data_dir("Nexy")
    flag_file = data_dir / "permissions_first_run_completed.flag"
    checked_paths.append(flag_file)
    
    if flag_file.exists():
        try:
            flag_file.unlink()
            print(f"  ✅ Удалён: {flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {flag_file}: {e}")
    else:
        print(f"  ℹ️  Не найден: {flag_file}")
    
    # Sandbox путь (если отличается)
    bundle_id = os.environ.get("APP_BUNDLE_ID", "com.nexy.assistant")
    sandbox_data_dir = Path.home() / "Library" / "Containers" / bundle_id / "Data" / "Library" / "Application Support" / "Nexy"
    sandbox_flag_file = sandbox_data_dir / "permissions_first_run_completed.flag"
    if sandbox_flag_file != flag_file and sandbox_flag_file.exists():
        checked_paths.append(sandbox_flag_file)
        try:
            sandbox_flag_file.unlink()
            print(f"  ✅ Удалён (sandbox): {sandbox_flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {sandbox_flag_file}: {e}")
    
    # /tmp fallback
    tmp_flag_file = Path("/tmp") / "Nexy" / "permissions_first_run_completed.flag"
    if tmp_flag_file.exists():
        checked_paths.append(tmp_flag_file)
        try:
            tmp_flag_file.unlink()
            print(f"  ✅ Удалён (/tmp): {tmp_flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {tmp_flag_file}: {e}")
    
    # 2. Очистка restart_completed.flag
    print("\n📋 Проверка restart_completed.flag:")
    
    # Стандартный путь (Caches)
    cache_dir = get_user_cache_dir("Nexy")
    restart_flag_file = cache_dir / "restart_completed.flag"
    checked_paths.append(restart_flag_file)
    
    if restart_flag_file.exists():
        try:
            restart_flag_file.unlink()
            print(f"  ✅ Удалён: {restart_flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {restart_flag_file}: {e}")
    else:
        print(f"  ℹ️  Не найден: {restart_flag_file}")
    
    # Sandbox путь (если отличается)
    sandbox_cache_dir = Path.home() / "Library" / "Containers" / bundle_id / "Data" / "Library" / "Caches" / "Nexy"
    sandbox_restart_flag_file = sandbox_cache_dir / "restart_completed.flag"
    if sandbox_restart_flag_file != restart_flag_file and sandbox_restart_flag_file.exists():
        checked_paths.append(sandbox_restart_flag_file)
        try:
            sandbox_restart_flag_file.unlink()
            print(f"  ✅ Удалён (sandbox): {sandbox_restart_flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {sandbox_restart_flag_file}: {e}")
    
    # /tmp fallback
    tmp_restart_flag_file = Path("/tmp") / "Nexy_cache" / "restart_completed.flag"
    if tmp_restart_flag_file.exists():
        checked_paths.append(tmp_restart_flag_file)
        try:
            tmp_restart_flag_file.unlink()
            print(f"  ✅ Удалён (/tmp): {tmp_restart_flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {tmp_restart_flag_file}: {e}")
    
    # 3. Очистка env переменной (если установлена)
    print("\n📋 Проверка environment переменных:")
    if os.environ.get("NEXY_FIRST_RUN_RESTARTED") == "1":
        print("  ⚠️  NEXY_FIRST_RUN_RESTARTED=1 установлена (не удаляется автоматически)")
        print("     Для очистки выполните: unset NEXY_FIRST_RUN_RESTARTED")
    else:
        print("  ℹ️  NEXY_FIRST_RUN_RESTARTED не установлена")
    
    # Итоги
    print("\n" + "=" * 60)
    print(f"✅ Очищено флагов: {cleared_count}")
    print(f"📁 Проверено путей: {len(checked_paths)}")
    
    if cleared_count > 0:
        print("\n🎉 Флаги успешно очищены! При следующем запуске приложение пройдёт процедуру первого запуска заново.")
    else:
        print("\nℹ️  Флаги не найдены. Возможно, они уже были очищены ранее.")
    
    return cleared_count

if __name__ == "__main__":
    try:
        cleared = clear_flags()
        sys.exit(0 if cleared >= 0 else 1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Прервано пользователем")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Критическая ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

