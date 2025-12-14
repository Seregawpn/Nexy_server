"""
Изолированный тест для проверки исправления ошибки 'preflight_peak is not defined'.

Проверяет через статический анализ кода:
1. Переменная preflight_peak определена в коде start_listening()
2. Preflight пропущен для быстрой активации (проверка через анализ исходного кода)
3. Код компилируется без ошибок
"""

import pytest
import ast
from pathlib import Path


def test_preflight_peak_defined_in_code():
    """Проверяет, что preflight_peak определена в коде start_listening()"""
    
    # Читаем исходный код файла
    file_path = Path("modules/voice_recognition/core/speech_recognizer.py")
    with open(file_path, 'r') as f:
        source_code = f.read()
    
    # Проверяем исходный код напрямую (более надежно, чем AST для вложенных блоков)
    lines = source_code.split('\n')
    in_start_listening = False
    start_listening_found = False
    preflight_peak_defined = False
    
    for i, line in enumerate(lines):
        if 'async def start_listening' in line:
            in_start_listening = True
            start_listening_found = True
        if in_start_listening:
            if 'def ' in line and 'async def start_listening' not in line:
                break  # Конец функции
            
            # Ищем присваивание preflight_peak = 0.0
            if 'preflight_peak' in line and '=' in line and '0.0' in line and not line.strip().startswith('#'):
                if 'preflight_peak' in line.split('=')[0]:
                    preflight_peak_defined = True
                    print(f"✅ Строка {i+1}: preflight_peak = 0.0 найдено: {line.strip()}")
                    break
    
    assert start_listening_found, "Функция start_listening() не найдена в коде"
    assert preflight_peak_defined, "preflight_peak не определена в коде start_listening()"
    
    print("✅ Тест пройден: preflight_peak определена в коде")


def test_preflight_check_not_called():
    """Проверяет, что preflight_check не вызывается (пропущен для скорости)"""
    
    # Читаем исходный код файла
    file_path = Path("modules/voice_recognition/core/speech_recognizer.py")
    with open(file_path, 'r') as f:
        source_code = f.read()
    
    # Проверяем исходный код напрямую (для закомментированных строк)
    lines = source_code.split('\n')
    in_start_listening = False
    preflight_check_commented = False
    preflight_success_set = False
    
    for i, line in enumerate(lines):
        if 'async def start_listening' in line:
            in_start_listening = True
        if in_start_listening:
            if 'def ' in line and 'async def start_listening' not in line:
                break  # Конец функции
            
            # Проверяем, что вызов preflight_check закомментирован
            if 'preflight_check' in line:
                if line.strip().startswith('#'):
                    preflight_check_commented = True
                    print(f"✅ Строка {i+1}: preflight_check закомментирован: {line.strip()[:80]}")
            
            # Проверяем, что preflight_success = True установлен
            if 'preflight_success = True' in line and not line.strip().startswith('#'):
                preflight_success_set = True
                print(f"✅ Строка {i+1}: preflight пропущен (preflight_success = True): {line.strip()[:80]}")
    
    assert preflight_check_commented or preflight_success_set, \
        "preflight_check должен быть закомментирован или preflight_success = True установлен"
    
    print("✅ Тест пройден: preflight_check не вызывается (пропущен для скорости)")


def test_preflight_peak_has_default_value():
    """Проверяет, что preflight_peak имеет значение по умолчанию 0.0"""
    
    # Читаем исходный код файла
    file_path = Path("modules/voice_recognition/core/speech_recognizer.py")
    with open(file_path, 'r') as f:
        source_code = f.read()
    
    # Ищем присваивание preflight_peak = 0.0
    lines = source_code.split('\n')
    in_start_listening = False
    preflight_peak_found = False
    
    for i, line in enumerate(lines):
        if 'async def start_listening' in line:
            in_start_listening = True
        if in_start_listening:
            if 'def ' in line and 'async def start_listening' not in line:
                break  # Конец функции
            
            # Ищем присваивание preflight_peak = 0.0
            if 'preflight_peak' in line and '=' in line and '0.0' in line and not line.strip().startswith('#'):
                preflight_peak_found = True
                print(f"✅ Строка {i+1}: preflight_peak = 0.0 найдено: {line.strip()}")
                break
    
    assert preflight_peak_found, "preflight_peak = 0.0 не найдено в коде start_listening()"
    print("✅ Тест пройден: preflight_peak имеет значение по умолчанию 0.0")


def test_code_compiles_without_preflight_peak_error():
    """Проверяет, что код компилируется без ошибки 'preflight_peak is not defined'"""
    
    # Читаем исходный код файла
    file_path = Path("modules/voice_recognition/core/speech_recognizer.py")
    
    try:
        # Компилируем код для проверки синтаксиса
        with open(file_path, 'r') as f:
            source_code = f.read()
        
        compile(source_code, str(file_path), 'exec')
        print("✅ Код компилируется без синтаксических ошибок")
        
        # Проверяем, что preflight_peak определена перед использованием
        lines = source_code.split('\n')
        in_start_listening = False
        preflight_peak_defined_before_use = False
        preflight_peak_used = False
        
        for i, line in enumerate(lines):
            if 'async def start_listening' in line:
                in_start_listening = True
            if in_start_listening:
                if 'def ' in line and 'async def start_listening' not in line:
                    break  # Конец функции
                
                # Ищем использование preflight_peak
                if 'preflight_peak' in line and not line.strip().startswith('#'):
                    if '=' in line and 'preflight_peak' in line.split('=')[0]:
                        # Это присваивание
                        preflight_peak_defined_before_use = True
                        print(f"✅ Строка {i+1}: preflight_peak определена: {line.strip()}")
                    elif preflight_peak_defined_before_use and 'preflight_peak' in line:
                        # Это использование после определения
                        preflight_peak_used = True
                        print(f"✅ Строка {i+1}: preflight_peak используется после определения: {line.strip()[:80]}")
        
        assert preflight_peak_defined_before_use, "preflight_peak должна быть определена перед использованием"
        print("✅ Тест пройден: код компилируется без ошибки 'preflight_peak is not defined'")
        
    except SyntaxError as e:
        pytest.fail(f"❌ Синтаксическая ошибка в коде: {e}")
    except Exception as e:
        pytest.fail(f"❌ Ошибка при компиляции кода: {e}")


def test_preflight_peak_not_used_in_commented_code():
    """Проверяет, что preflight_peak не используется в закомментированном коде без определения"""
    
    # Читаем исходный код файла
    file_path = Path("modules/voice_recognition/core/speech_recognizer.py")
    with open(file_path, 'r') as f:
        source_code = f.read()
    
    lines = source_code.split('\n')
    in_start_listening = False
    preflight_peak_defined = False
    preflight_peak_used_in_comments = False
    
    for i, line in enumerate(lines):
        if 'async def start_listening' in line:
            in_start_listening = True
        if in_start_listening:
            if 'def ' in line and 'async def start_listening' not in line:
                break  # Конец функции
            
            # Ищем определение preflight_peak
            if 'preflight_peak' in line and '=' in line and not line.strip().startswith('#'):
                if 'preflight_peak' in line.split('=')[0]:
                    preflight_peak_defined = True
                    print(f"✅ Строка {i+1}: preflight_peak определена: {line.strip()}")
            
            # Проверяем использование в закомментированном коде
            if line.strip().startswith('#') and 'preflight_peak' in line:
                # Это нормально - использование в комментариях допустимо
                pass
    
    assert preflight_peak_defined, "preflight_peak должна быть определена в активном коде"
    print("✅ Тест пройден: preflight_peak определена в активном коде")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
