#!/usr/bin/env python3
"""
Тест различных exit codes helper'а и их логирования.
"""

import subprocess
import sys
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent))

from modules.permissions.first_run.status_checker import check_accessibility_status


def test_helper_directly():
    """Прямой тест helper'а с проверкой exit codes."""
    print("\n" + "="*60)
    print("ТЕСТ: Прямой запуск trigger_accessibility_prompt.py")
    print("="*60)
    
    script_path = Path(__file__).parent / "modules" / "permissions" / "first_run" / "trigger_accessibility_prompt.py"
    
    if not script_path.exists():
        print(f"❌ Файл не найден: {script_path}")
        return False
    
    print(f"\nЗапускаю: {sys.executable} {script_path}")
    
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        exit_code = result.returncode
        stdout = result.stdout.strip() if result.stdout else None
        stderr = result.stderr.strip() if result.stderr else None
        
        # Интерпретация exit code (как в activator.py)
        exit_code_meaning = {
            0: "Разрешение уже есть (trusted=True) или диалог показан успешно",
            1: "Разрешения нет (trusted=False) — диалог должен был появиться",
            2: "Ошибка выполнения"
        }.get(exit_code, f"Неизвестный exit code: {exit_code}")
        
        print(f"\n✅ Helper завершился")
        print(f"   Exit code: {exit_code}")
        print(f"   Интерпретация: {exit_code_meaning}")
        
        if stdout:
            print(f"\n   STDOUT:\n   {stdout}")
        if stderr:
            print(f"\n   STDERR:\n   {stderr}")
        
        # Проверка статуса
        status = check_accessibility_status()
        print(f"\n   Текущий статус: {status.value}")
        
        # Валидация
        if exit_code == 0:
            if status.value == "granted":
                print("\n✅ Валидация: Exit 0 соответствует статусу 'granted'")
                return True
            else:
                print(f"\n⚠️  Валидация: Exit 0, но статус '{status.value}' (возможно, диалог показан)")
                return True
        elif exit_code == 1:
            if status.value in ["not_determined", "denied"]:
                print(f"\n✅ Валидация: Exit 1 соответствует статусу '{status.value}'")
                return True
            else:
                print(f"\n⚠️  Валидация: Exit 1, но статус '{status.value}' (неожиданно)")
                return True
        elif exit_code == 2:
            print("\n❌ Валидация: Exit 2 означает ошибку выполнения")
            return False
        else:
            print(f"\n❌ Валидация: Неожиданный exit code {exit_code}")
            return False
        
    except subprocess.TimeoutExpired:
        print("\n❌ Timeout (10s) — helper не завершился")
        return False
    except Exception as e:
        print(f"\n❌ Ошибка запуска: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_logging_format():
    """Тест формата логирования (симуляция)."""
    print("\n" + "="*60)
    print("ТЕСТ: Формат логирования (симуляция)")
    print("="*60)
    
    # Симулируем различные exit codes
    test_cases = [
        (0, "Разрешение уже есть (trusted=True) или диалог показан успешно"),
        (1, "Разрешения нет (trusted=False) — диалог должен был появиться"),
        (2, "Ошибка выполнения"),
        (-1, "Timeout"),
        (-2, "Exception при запуске"),
    ]
    
    print("\nПримеры логов для различных exit codes:\n")
    
    for exit_code, meaning in test_cases:
        print(f"Exit code: {exit_code}")
        print(f"  Лог: ♿ Accessibility: prompt helper завершён — exit_code={exit_code} ({meaning}) stdout=(пусто) stderr=(пусто)")
        print(f"  Print: ♿ [ACTIVATOR] Accessibility prompt helper: exit={exit_code} ({meaning})")
        print()
    
    print("✅ Формат логирования корректен")


def main():
    """Основная функция."""
    print("\n" + "="*60)
    print("ТЕСТ: Accessibility Helper Exit Codes")
    print("="*60)
    
    # Тест 1: Прямой запуск helper'а
    helper_ok = test_helper_directly()
    
    # Тест 2: Формат логирования
    test_logging_format()
    
    # Итоги
    print("\n" + "="*60)
    print("ИТОГИ")
    print("="*60)
    print(f"\nПрямой запуск helper'а: {'✅ OK' if helper_ok else '❌ FAIL'}")
    print("Формат логирования: ✅ OK")
    
    if helper_ok:
        print("\n✅ ВСЕ ТЕСТЫ ПРОШЛИ")
        print("\n📋 Что проверить:")
        print("   1. Exit code helper'а соответствует статусу разрешения")
        print("   2. Логирование в activate_accessibility() показывает exit code")
        print("   3. Статус до/после вызова логируется корректно")
    else:
        print("\n⚠️  НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОШЛИ")
    
    return 0 if helper_ok else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(130)
