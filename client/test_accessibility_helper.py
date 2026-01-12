#!/usr/bin/env python3
"""
Тестовый скрипт для проверки trigger_accessibility_prompt.py helper.

Проверяет:
1. Exit code helper'а
2. Статус до/после вызова
3. Мониторинг tccd логов (опционально)

Использование:
    python3 test_accessibility_helper.py
"""

import asyncio
import subprocess
import sys
import os
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent))

from modules.permissions.first_run.status_checker import (
    check_accessibility_status,
    PermissionStatus
)


def reset_accessibility_permission():
    """Сбросить разрешение Accessibility через tccutil."""
    print("\n" + "="*60)
    print("ШАГ 1: Сброс разрешения Accessibility")
    print("="*60)
    
    bundle_id = "com.nexy.assistant"
    cmd = ["sudo", "tccutil", "reset", "Accessibility", bundle_id]
    
    print(f"Выполняю: {' '.join(cmd)}")
    print("⚠️  Требуется пароль администратора")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ Разрешение сброшено: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка сброса: {e.stderr.strip()}")
        return False
    except KeyboardInterrupt:
        print("\n⚠️  Прервано пользователем")
        return False


def run_helper_directly():
    """Запустить helper напрямую и получить exit code."""
    print("\n" + "="*60)
    print("ШАГ 2: Прямой запуск trigger_accessibility_prompt.py")
    print("="*60)
    
    script_path = Path(__file__).parent / "modules" / "permissions" / "first_run" / "trigger_accessibility_prompt.py"
    
    if not script_path.exists():
        print(f"❌ Файл не найден: {script_path}")
        return None
    
    print(f"Запускаю: {sys.executable} {script_path}")
    
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
        
        # Интерпретация exit code
        exit_code_meaning = {
            0: "✅ Разрешение уже есть (trusted=True) или диалог показан успешно",
            1: "⚠️  Разрешения нет (trusted=False) — диалог должен был появиться",
            2: "❌ Ошибка выполнения"
        }.get(exit_code, f"❓ Неизвестный exit code: {exit_code}")
        
        print(f"\nExit code: {exit_code}")
        print(f"Интерпретация: {exit_code_meaning}")
        
        if stdout:
            print(f"\nSTDOUT:\n{stdout}")
        if stderr:
            print(f"\nSTDERR:\n{stderr}")
        
        return {
            "exit_code": exit_code,
            "meaning": exit_code_meaning,
            "stdout": stdout,
            "stderr": stderr
        }
        
    except subprocess.TimeoutExpired:
        print("❌ Timeout (10s) — helper не завершился")
        return {"exit_code": -1, "meaning": "Timeout", "stdout": None, "stderr": None}
    except Exception as e:
        print(f"❌ Ошибка запуска: {e}")
        return {"exit_code": -2, "meaning": f"Exception: {e}", "stdout": None, "stderr": None}


def check_status_before_after():
    """Проверить статус до и после вызова helper'а."""
    print("\n" + "="*60)
    print("ШАГ 3: Проверка статуса до/после")
    print("="*60)
    
    print("\nСтатус ДО вызова helper'а:")
    status_before = check_accessibility_status()
    print(f"  → {status_before.value}")
    
    print("\n⏳ Ожидание 1 секунда для обработки системой...")
    import time
    time.sleep(1.0)
    
    print("\nСтатус ПОСЛЕ вызова helper'а:")
    status_after = check_accessibility_status()
    print(f"  → {status_after.value}")
    
    if status_before != status_after:
        print(f"\n✅ Статус изменился: {status_before.value} → {status_after.value}")
    else:
        print(f"\n⚠️  Статус не изменился: {status_before.value}")
    
    return {
        "before": status_before,
        "after": status_after,
        "changed": status_before != status_after
    }


def monitor_tccd_logs():
    """Мониторинг tccd логов (опционально, требует ручного запуска)."""
    print("\n" + "="*60)
    print("ШАГ 4: Мониторинг tccd логов (опционально)")
    print("="*60)
    
    print("\nДля мониторинга tccd логов выполните в отдельном терминале:")
    print("  log show --last 2m --predicate 'process == \"tccd\"' | grep -i accessibility")
    print("\nИли для более детального вывода:")
    print("  log show --last 2m --predicate 'process == \"tccd\"' | grep -i 'com.nexy.assistant'")
    
    print("\nНажмите Enter когда закончите проверку логов...")
    try:
        input()
    except KeyboardInterrupt:
        print("\n⚠️  Прервано пользователем")


def main():
    """Основная функция теста."""
    print("\n" + "="*60)
    print("ТЕСТ: trigger_accessibility_prompt.py helper")
    print("="*60)
    
    # Проверка статуса до сброса
    print("\n📊 Текущий статус Accessibility:")
    initial_status = check_accessibility_status()
    print(f"  → {initial_status.value}")
    
    if initial_status == PermissionStatus.GRANTED:
        print("\n⚠️  Разрешение уже предоставлено.")
        print("Для полного теста нужно сбросить разрешение.")
        reset_choice = input("\nСбросить разрешение? (y/N): ").strip().lower()
        if reset_choice != 'y':
            print("Продолжаем без сброса...")
        else:
            if not reset_accessibility_permission():
                print("⚠️  Не удалось сбросить разрешение, продолжаем...")
    else:
        print("\n✅ Разрешение не предоставлено — можно тестировать без сброса")
        reset_choice = input("\nВсё равно сбросить разрешение? (y/N): ").strip().lower()
        if reset_choice == 'y':
            reset_accessibility_permission()
    
    # Запуск helper'а
    helper_result = run_helper_directly()
    
    if helper_result is None:
        print("\n❌ Не удалось запустить helper")
        return 1
    
    # Проверка статуса
    status_result = check_status_before_after()
    
    # Мониторинг логов (опционально)
    monitor_tccd_logs()
    
    # Итоги
    print("\n" + "="*60)
    print("ИТОГИ ТЕСТА")
    print("="*60)
    print(f"\nHelper exit code: {helper_result['exit_code']}")
    print(f"Интерпретация: {helper_result['meaning']}")
    print(f"\nСтатус до: {status_result['before'].value}")
    print(f"Статус после: {status_result['after'].value}")
    print(f"Статус изменился: {'✅ Да' if status_result['changed'] else '❌ Нет'}")
    
    # Критерии успеха
    success_criteria = []
    
    if helper_result['exit_code'] in [0, 1]:
        success_criteria.append("✅ Helper завершился без ошибки (exit 0 или 1)")
    else:
        success_criteria.append(f"❌ Helper завершился с ошибкой (exit {helper_result['exit_code']})")
    
    if status_result['changed']:
        success_criteria.append("✅ Статус изменился после вызова helper'а")
    else:
        success_criteria.append("⚠️  Статус не изменился (возможно, диалог не показан или пользователь не ответил)")
    
    print("\n" + "\n".join(success_criteria))
    
    # Рекомендации
    print("\n" + "="*60)
    print("РЕКОМЕНДАЦИИ")
    print("="*60)
    
    if helper_result['exit_code'] == 0:
        print("\n✅ Helper вернул 0 — разрешение уже есть или диалог показан успешно")
    elif helper_result['exit_code'] == 1:
        print("\n⚠️  Helper вернул 1 — разрешения нет, диалог должен был появиться")
        print("   Проверьте:")
        print("   1. Появился ли системный диалог Accessibility?")
        print("   2. Есть ли ошибки в tccd логах?")
    elif helper_result['exit_code'] == 2:
        print("\n❌ Helper вернул 2 — ошибка выполнения")
        if helper_result['stderr']:
            print(f"   Ошибка: {helper_result['stderr']}")
    else:
        print(f"\n❌ Helper вернул неожиданный код: {helper_result['exit_code']}")
    
    return 0 if helper_result['exit_code'] in [0, 1] else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(130)
