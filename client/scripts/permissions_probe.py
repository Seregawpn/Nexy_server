#!/usr/bin/env python3
"""
Диагностический скрипт для проверки надёжности методов проверки разрешений.

Цель: верифицировать корректность методов проверки (tccutil/AX/IOHID) до внедрения изменений.

Использование:
    python scripts/permissions_probe.py

Перед запуском:
    1. Убедитесь, что разрешения НЕ выданы (или выданы для сравнения)
    2. Запустите скрипт для получения baseline
    3. Выдайте разрешения в System Settings
    4. Запустите скрипт повторно для сравнения

После верификации:
    Удалите этот скрипт (временный диагностический инструмент).
"""

import sys
import os
import subprocess
import logging
from typing import Dict, Any, Optional
from datetime import datetime

# Добавляем путь к клиенту для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from modules.permissions.first_run.status_checker import (
    check_microphone_status,
    check_accessibility_status,
    check_input_monitoring_status,
    check_screen_capture_status,
    get_bundle_id,
    PermissionStatus,
)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


def run_tccutil_check(permission_type: str, bundle_id: str) -> Optional[bool]:
    """
    Проверить разрешение через tccutil check.
    
    Args:
        permission_type: тип разрешения (Microphone, ScreenCapture, Accessibility, ListenEvent)
        bundle_id: bundle identifier приложения
        
    Returns:
        True если разрешение выдано, False если нет, None если ошибка
    """
    try:
        result = subprocess.run(
            ['tccutil', 'check', permission_type, bundle_id],
            capture_output=True,
            text=True,
            timeout=5,
        )
        
        # tccutil check возвращает 0 если разрешение выдано, не-0 если нет
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        logger.warning(f"⚠️  tccutil check для {permission_type} превысил таймаут")
        return None
    except FileNotFoundError:
        logger.warning("⚠️  tccutil не найден (требуется macOS)")
        return None
    except Exception as e:
        logger.error(f"❌ Ошибка tccutil check для {permission_type}: {e}")
        return None


def format_status(status: PermissionStatus) -> str:
    """Форматировать статус для вывода."""
    status_map = {
        PermissionStatus.GRANTED: "✅ GRANTED",
        PermissionStatus.DENIED: "❌ DENIED",
        PermissionStatus.NOT_DETERMINED: "⚠️  NOT_DETERMINED",
        PermissionStatus.ERROR: "🔴 ERROR",
    }
    return status_map.get(status, f"❓ {status.value}")


def format_tccutil_result(result: Optional[bool]) -> str:
    """Форматировать результат tccutil для вывода."""
    if result is None:
        return "❓ ERROR/UNKNOWN"
    return "✅ GRANTED" if result else "❌ DENIED"


def check_all_permissions() -> Dict[str, Dict[str, Any]]:
    """
    Проверить все разрешения через все доступные методы.
    
    Returns:
        Словарь с результатами проверок для каждого разрешения
    """
    # Пытаемся получить bundle_id из окружения или конфига, иначе используем дефолтный
    bundle_id = os.environ.get("NEXY_BUNDLE_ID")
    if not bundle_id:
        try:
            from config.unified_config_loader import UnifiedConfigLoader
            config_loader = UnifiedConfigLoader.get_instance()
            config_data = config_loader._load_config()
            bundle_id = config_data.get("app", {}).get("bundle_id")
            if bundle_id:
                logger.info(f"📦 Bundle ID загружен из конфига: {bundle_id}")
        except Exception as e:
            logger.debug(f"Не удалось загрузить bundle_id из конфига: {e}")
    
    if not bundle_id:
        bundle_id = get_bundle_id()
        # Если bundle_id определяется как Python процесс, используем дефолтный для Nexy
        if bundle_id in ("org.python.python", "com.apple.python", "org.python3.python"):
            bundle_id = "com.nexy.assistant"
            logger.warning(f"⚠️  Bundle ID определён как Python процесс, используем дефолтный: {bundle_id}")
    
    logger.info(f"📦 Bundle ID: {bundle_id}")
    logger.info("")
    
    results = {}
    
    # 1. Microphone
    logger.info("🎙️  Проверка Microphone...")
    mic_status_checker = check_microphone_status()
    mic_tccutil = run_tccutil_check("Microphone", bundle_id)
    
    results["microphone"] = {
        "status_checker": mic_status_checker,
        "tccutil": mic_tccutil,
        "match": (
            mic_tccutil is not None and
            ((mic_status_checker == PermissionStatus.GRANTED and mic_tccutil) or
             (mic_status_checker != PermissionStatus.GRANTED and not mic_tccutil))
        ) if mic_tccutil is not None else None,
    }
    
    # 2. Accessibility
    logger.info("♿  Проверка Accessibility...")
    acc_status_checker = check_accessibility_status()
    acc_tccutil = run_tccutil_check("Accessibility", bundle_id)
    
    results["accessibility"] = {
        "status_checker": acc_status_checker,
        "tccutil": acc_tccutil,
        "match": (
            acc_tccutil is not None and
            ((acc_status_checker == PermissionStatus.GRANTED and acc_tccutil) or
             (acc_status_checker != PermissionStatus.GRANTED and not acc_tccutil))
        ) if acc_tccutil is not None else None,
    }
    
    # 3. Input Monitoring
    logger.info("⌨️  Проверка Input Monitoring...")
    input_status_checker = check_input_monitoring_status()
    input_tccutil = run_tccutil_check("ListenEvent", bundle_id)  # tccutil использует ListenEvent
    
    results["input_monitoring"] = {
        "status_checker": input_status_checker,
        "tccutil": input_tccutil,
        "match": (
            input_tccutil is not None and
            ((input_status_checker == PermissionStatus.GRANTED and input_tccutil) or
             (input_status_checker != PermissionStatus.GRANTED and not input_tccutil))
        ) if input_tccutil is not None else None,
    }
    
    # 4. Screen Capture
    logger.info("📺 Проверка Screen Capture...")
    screen_status_checker = check_screen_capture_status()
    screen_tccutil = run_tccutil_check("ScreenCapture", bundle_id)
    
    results["screen_capture"] = {
        "status_checker": screen_status_checker,
        "tccutil": screen_tccutil,
        "match": (
            screen_tccutil is not None and
            ((screen_status_checker == PermissionStatus.GRANTED and screen_tccutil) or
             (screen_status_checker != PermissionStatus.GRANTED and not screen_tccutil))
        ) if screen_tccutil is not None else None,
    }
    
    return results


def print_results(results: Dict[str, Dict[str, Any]]):
    """Вывести результаты проверок в удобном формате."""
    print("\n" + "=" * 80)
    print(f"📊 РЕЗУЛЬТАТЫ ПРОВЕРКИ РАЗРЕШЕНИЙ - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    print()
    
    for perm_name, perm_results in results.items():
        print(f"🔍 {perm_name.upper().replace('_', ' ')}")
        print("-" * 80)
        
        # Status Checker результат
        status_checker = perm_results.get("status_checker")
        print(f"  Status Checker:     {format_status(status_checker)}")
        
        # tccutil результат
        tccutil = perm_results.get("tccutil")
        print(f"  tccutil check:      {format_tccutil_result(tccutil)}")
        
        # Совпадение результатов
        match = perm_results.get("match")
        if match is not None:
            match_str = "✅ СОВПАДАЕТ" if match else "⚠️  НЕ СОВПАДАЕТ"
            print(f"  Совпадение:         {match_str}")
        else:
            print(f"  Совпадение:         ❓ НЕВОЗМОЖНО ПРОВЕРИТЬ (tccutil error)")
        
        print()
    
    # Итоговая статистика
    print("=" * 80)
    print("📈 ИТОГОВАЯ СТАТИСТИКА")
    print("-" * 80)
    
    total = len(results)
    matches = sum(1 for r in results.values() if r.get("match") is True)
    mismatches = sum(1 for r in results.values() if r.get("match") is False)
    errors = sum(1 for r in results.values() if r.get("match") is None)
    
    print(f"  Всего проверок:      {total}")
    print(f"  ✅ Совпадает:        {matches}")
    print(f"  ⚠️  Не совпадает:     {mismatches}")
    print(f"  ❓ Ошибки проверки:  {errors}")
    print()
    
    if matches == total:
        print("✅ ВСЕ ПРОВЕРКИ СОВПАДАЮТ - методы проверки надёжны")
    elif mismatches > 0:
        print("⚠️  ОБНАРУЖЕНЫ РАСХОЖДЕНИЯ - требуется анализ методов проверки")
    else:
        print("❓ ЕСТЬ ОШИБКИ ПРОВЕРКИ - требуется диагностика")
    
    print("=" * 80)
    print()


def main():
    """Главная функция."""
    import time
    
    watch_mode = "--watch" in sys.argv
    
    print("\n" + "=" * 80)
    print("🔬 ДИАГНОСТИЧЕСКАЯ ПРОВЕРКА РАЗРЕШЕНИЙ")
    if watch_mode:
        print("   [WATCH MODE - Continuous polling, Ctrl+C для выхода]")
    print("=" * 80)
    print()
    print("Этот скрипт проверяет надёжность методов проверки разрешений.")
    print("Сравнивает результаты status_checker.py с tccutil check.")
    print()
    if not watch_mode:
        print("Инструкция:")
        print("  1. Запустите скрипт ДО выдачи разрешений (baseline)")
        print("  2. Выдайте разрешения в System Settings")
        print("  3. Запустите скрипт повторно (после выдачи)")
        print("  4. Сравните результаты и убедитесь, что методы надёжны")
        print()
        print("Опции:")
        print("  --watch    Continuous polling каждую секунду")
    print()
    print("-" * 80)
    print()
    
    try:
        if watch_mode:
            # Watch mode: continuous polling
            iteration = 0
            prev_statuses = {}
            
            while True:
                iteration += 1
                results = check_all_permissions()
                
                # Собираем текущие статусы
                current_statuses = {
                    perm: str(res.get("status_checker", "?"))
                    for perm, res in results.items()
                }
                
                # Проверяем изменения
                changes = []
                for perm, status in current_statuses.items():
                    prev = prev_statuses.get(perm)
                    if prev and prev != status:
                        changes.append(f"{perm}: {prev} → {status}")
                
                # Выводим компактный статус
                print(f"\r[{iteration:4d}] ", end="")
                for perm, status in current_statuses.items():
                    short_perm = perm[:3].upper()
                    short_status = "✅" if "GRANTED" in status else "❌" if "DENIED" in status else "⚠️"
                    print(f"{short_perm}:{short_status} ", end="")
                
                if changes:
                    print(f" ← ИЗМЕНЕНИЯ: {', '.join(changes)}", end="")
                
                print("", flush=True)
                
                prev_statuses = current_statuses
                time.sleep(1.0)
        else:
            # Single check mode
            results = check_all_permissions()
            print_results(results)
            
            # Возвращаем код выхода в зависимости от результатов
            matches = sum(1 for r in results.values() if r.get("match") is True)
            total = len(results)
            
            if matches == total:
                return 0  # Все совпадает
            else:
                return 1  # Есть расхождения или ошибки
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        return 130
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
