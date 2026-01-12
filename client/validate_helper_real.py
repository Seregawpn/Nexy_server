#!/usr/bin/env python3
"""
Реальная валидация helper'а на машине пользователя.
Выполняет все шаги из Verification (DoD).
"""

import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from modules.permissions.first_run.status_checker import check_accessibility_status, PermissionStatus


def step_reset():
    """ШАГ 1: Сброс разрешения."""
    print("\n" + "="*60)
    print("ШАГ 1: Сброс разрешения Accessibility")
    print("="*60)
    
    cmd = ["sudo", "tccutil", "reset", "Accessibility", "com.nexy.assistant"]
    print(f"Выполняю: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка: {e.stderr.strip()}")
        return False


def step_check_status_before():
    """ШАГ 2: Проверка статуса ДО."""
    print("\n" + "="*60)
    print("ШАГ 2: Проверка статуса ДО запуска helper'а")
    print("="*60)
    
    status = check_accessibility_status()
    print(f"Статус: {status.value}")
    
    # Функциональный тест
    try:
        result = subprocess.run(
            ['osascript', '-e', 'tell application "System Events" to get name of first application process whose frontmost is true'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            print(f"✅ Функциональный тест: GRANTED (AppleScript работает)")
        else:
            print(f"❌ Функциональный тест: NOT GRANTED (AppleScript не работает)")
    except Exception as e:
        print(f"⚠️  Функциональный тест ошибка: {e}")
    
    return status


def step_run_helper():
    """ШАГ 3: Запуск helper'а напрямую."""
    print("\n" + "="*60)
    print("ШАГ 3: Запуск trigger_accessibility_prompt.py")
    print("="*60)
    
    script_path = Path(__file__).parent / "modules" / "permissions" / "first_run" / "trigger_accessibility_prompt.py"
    
    if not script_path.exists():
        print(f"❌ Файл не найден: {script_path}")
        return None
    
    print(f"Запускаю: {sys.executable} {script_path}")
    print("⏳ Ожидание завершения helper'а...")
    
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


def step_check_tccd_logs():
    """ШАГ 4: Проверка tccd логов."""
    print("\n" + "="*60)
    print("ШАГ 4: Проверка tccd логов")
    print("="*60)
    
    print("Выполняю: log show --last 2m --predicate 'process == \"tccd\"' | grep -i accessibility")
    
    try:
        result = subprocess.run(
            ["log", "show", "--last", "2m", "--predicate", 'process == "tccd"'],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            accessibility_lines = [line for line in lines if 'accessibility' in line.lower() or 'nexy' in line.lower()]
            
            if accessibility_lines:
                print(f"\nНайдено {len(accessibility_lines)} строк с 'accessibility' или 'nexy':")
                for line in accessibility_lines[:10]:  # Первые 10 строк
                    print(f"  {line[:200]}")
            else:
                print("\n⚠️  Строк с 'accessibility' или 'nexy' не найдено")
            
            # Проверка на ошибки
            error_lines = [line for line in lines if any(keyword in line.lower() for keyword in ['error', 'crash', 'fail', 'denied'])]
            if error_lines:
                print(f"\n⚠️  Найдено {len(error_lines)} строк с ошибками:")
                for line in error_lines[:5]:  # Первые 5 ошибок
                    print(f"  {line[:200]}")
            else:
                print("\n✅ Ошибок в tccd логах не найдено")
        else:
            print(f"⚠️  Команда log show завершилась с кодом {result.returncode}")
            
    except Exception as e:
        print(f"⚠️  Ошибка проверки логов: {e}")


def step_check_status_after():
    """ШАГ 5: Проверка статуса ПОСЛЕ."""
    print("\n" + "="*60)
    print("ШАГ 5: Проверка статуса ПОСЛЕ запуска helper'а")
    print("="*60)
    
    print("⏳ Ожидание 2 секунды для обработки системой...")
    time.sleep(2)
    
    status = check_accessibility_status()
    print(f"Статус: {status.value}")
    
    # Функциональный тест
    try:
        result = subprocess.run(
            ['osascript', '-e', 'tell application "System Events" to get name of first application process whose frontmost is true'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            print(f"✅ Функциональный тест: GRANTED (AppleScript работает)")
        else:
            print(f"❌ Функциональный тест: NOT GRANTED (AppleScript не работает)")
    except Exception as e:
        print(f"⚠️  Функциональный тест ошибка: {e}")
    
    return status


def main():
    """Основная функция валидации."""
    print("\n" + "="*60)
    print("РЕАЛЬНАЯ ВАЛИДАЦИЯ: trigger_accessibility_prompt.py")
    print("="*60)
    print("\nВыполняю все шаги из Verification (DoD)...")
    
    # ШАГ 1: Сброс разрешения
    if not step_reset():
        print("\n⚠️  Не удалось сбросить разрешение, продолжаю...")
    
    # ШАГ 2: Статус ДО
    status_before = step_check_status_before()
    
    # ШАГ 3: Запуск helper'а
    helper_result = step_run_helper()
    
    if helper_result is None:
        print("\n❌ Не удалось запустить helper")
        return 1
    
    # ШАГ 4: tccd логи
    step_check_tccd_logs()
    
    # ШАГ 5: Статус ПОСЛЕ
    status_after = step_check_status_after()
    
    # Итоги
    print("\n" + "="*60)
    print("ИТОГИ ВАЛИДАЦИИ")
    print("="*60)
    
    print(f"\nHelper exit code: {helper_result['exit_code']}")
    print(f"Интерпретация: {helper_result['meaning']}")
    print(f"\nСтатус ДО: {status_before.value}")
    print(f"Статус ПОСЛЕ: {status_after.value}")
    print(f"Статус изменился: {'✅ Да' if status_before != status_after else '❌ Нет'}")
    
    # Критерии успеха
    print("\n" + "="*60)
    print("КРИТЕРИИ УСПЕХА")
    print("="*60)
    
    success = []
    warnings = []
    
    if helper_result['exit_code'] in [0, 1]:
        success.append("✅ Helper завершился без ошибки (exit 0 или 1)")
    else:
        warnings.append(f"⚠️  Helper завершился с ошибкой (exit {helper_result['exit_code']})")
    
    if helper_result['exit_code'] == 0:
        if status_after == PermissionStatus.GRANTED:
            success.append("✅ Exit 0 соответствует статусу GRANTED")
        else:
            warnings.append(f"⚠️  Exit 0, но статус {status_after.value} (возможно, диалог показан)")
    elif helper_result['exit_code'] == 1:
        if status_after in [PermissionStatus.NOT_DETERMINED, PermissionStatus.DENIED]:
            success.append(f"✅ Exit 1 соответствует статусу {status_after.value}")
        else:
            warnings.append(f"⚠️  Exit 1, но статус {status_after.value} (неожиданно)")
    
    if not helper_result['stderr']:
        success.append("✅ Нет ошибок в stderr")
    else:
        warnings.append(f"⚠️  Есть ошибки в stderr: {helper_result['stderr'][:200]}")
    
    print("\nУспехи:")
    for s in success:
        print(f"  {s}")
    
    if warnings:
        print("\nПредупреждения:")
        for w in warnings:
            print(f"  {w}")
    
    print("\n" + "="*60)
    print("РЕКОМЕНДАЦИИ")
    print("="*60)
    
    if helper_result['exit_code'] == 0:
        print("\n✅ Helper вернул 0 — разрешение есть или диалог показан успешно")
        print("   Проверьте:")
        print("   1. Появился ли системный диалог Accessibility?")
        print("   2. Если диалог не появился, разрешение уже было предоставлено ранее")
    elif helper_result['exit_code'] == 1:
        print("\n⚠️  Helper вернул 1 — разрешения нет, диалог должен был появиться")
        print("   Проверьте:")
        print("   1. Появился ли системный диалог Accessibility?")
        print("   2. Есть ли ошибки в tccd логах?")
        print("   3. Проверьте tccd логи выше на наличие событий по Accessibility")
    elif helper_result['exit_code'] == 2:
        print("\n❌ Helper вернул 2 — ошибка выполнения")
        if helper_result['stderr']:
            print(f"   Ошибка: {helper_result['stderr']}")
    
    return 0 if helper_result['exit_code'] in [0, 1] else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Прервано пользователем")
        sys.exit(130)
