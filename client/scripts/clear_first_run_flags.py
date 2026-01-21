#!/usr/bin/env python3
"""
Скрипт для очистки флагов первого запуска приложения Nexy.

Удаляет все флаги, связанные с permissions, чтобы можно было заново пройти процедуру первого запуска.
"""

import sys
import os
from pathlib import Path

# Добавляем пути к модулям
CLIENT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(CLIENT_ROOT))
sys.path.insert(0, str(CLIENT_ROOT / "integration"))

from integration.utils.resource_path import get_user_data_dir

def clear_flags():
    """Очищает все флаги первого запуска"""
    print("🧹 Очистка флагов первого запуска...")
    print("=" * 60)
    
    cleared_count = 0
    checked_paths = []
    
    # Стандартный путь
    data_dir = get_user_data_dir("Nexy")
    
    # 1. Очистка permissions_first_run_completed.flag (канонический флаг)
    print("\n📋 Проверка permissions_first_run_completed.flag:")
    
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
    
    # 2. Очистка старого флага (для миграции)
    print("\n📋 Проверка permissions_granted.flag (legacy, для миграции):")
    
    old_flag_file = data_dir / "permissions_granted.flag"
    checked_paths.append(old_flag_file)
    
    if old_flag_file.exists():
        try:
            old_flag_file.unlink()
            print(f"  ✅ Удалён: {old_flag_file}")
            cleared_count += 1
        except Exception as e:
            print(f"  ❌ Ошибка удаления {old_flag_file}: {e}")
    else:
        print(f"  ℹ️  Не найден: {old_flag_file}")
    
    # 3. Очистка restart_completed.flag (legacy, больше не используется)
    print("\n📋 Проверка restart_completed.flag (legacy, deprecated):")
    
    restart_flag_file = data_dir / "restart_completed.flag"
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
    
    # 4. Sandbox пути (если отличаются)
    bundle_id = os.environ.get("APP_BUNDLE_ID", "com.nexy.assistant")
    sandbox_data_dir = Path.home() / "Library" / "Containers" / bundle_id / "Data" / "Library" / "Application Support" / "Nexy"
    
    for flag_name in ["permissions_first_run_completed.flag", "permissions_granted.flag", "restart_completed.flag"]:
        sandbox_flag = sandbox_data_dir / flag_name
        if sandbox_flag.exists() and sandbox_flag not in checked_paths:
            checked_paths.append(sandbox_flag)
            try:
                sandbox_flag.unlink()
                print(f"  ✅ Удалён (sandbox): {sandbox_flag}")
                cleared_count += 1
            except Exception as e:
                print(f"  ❌ Ошибка удаления {sandbox_flag}: {e}")
    
    # 5. /tmp fallback
    for flag_name in ["permissions_first_run_completed.flag", "permissions_granted.flag", "restart_completed.flag"]:
        tmp_flag = Path("/tmp") / "Nexy" / flag_name
        if tmp_flag.exists() and tmp_flag not in checked_paths:
            checked_paths.append(tmp_flag)
            try:
                tmp_flag.unlink()
                print(f"  ✅ Удалён (/tmp): {tmp_flag}")
                cleared_count += 1
            except Exception as e:
                print(f"  ❌ Ошибка удаления {tmp_flag}: {e}")
    
    # 6. Очистка env переменной (если установлена)
    print("\n📋 Проверка environment переменных:")
    if os.environ.get("NEXY_TEST_SKIP_PERMISSIONS") == "1":
        print("  ⚠️  NEXY_TEST_SKIP_PERMISSIONS=1 установлена (тестовый режим)")
        print("     Для очистки выполните: unset NEXY_TEST_SKIP_PERMISSIONS")
    else:
        print("  ℹ️  NEXY_TEST_SKIP_PERMISSIONS не установлена")
    
    # Итоги
    print("\n" + "=" * 60)
    print(f"✅ Очищено флагов: {cleared_count}")
    print(f"📁 Проверено путей: {len(checked_paths)}")
    
    if cleared_count > 0:
        print("\n🎉 Флаги успешно очищены! При следующем запуске приложение запросит разрешения заново.")
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
