#!/usr/bin/env python3
"""
Wrapper script that automatically redirects to venv Python
This allows running: python3 server/main_wrapper.py
"""

import sys
import os

# Определяем путь к main.py
main_py_path = os.path.join(os.path.dirname(__file__), 'main.py')
server_dir = os.path.dirname(os.path.dirname(__file__))  # server(Messages)
venv_python = os.path.join(server_dir, '.venv', 'bin', 'python')

# Проверяем, запущены ли мы из venv
python_path = sys.executable
venv_indicators = ['.venv', 'venv', 'env']
is_venv = any(indicator in python_path for indicator in venv_indicators)

# Если не в venv и venv существует - перезапускаем
if not is_venv and os.path.exists(venv_python) and os.path.isfile(venv_python):
    print("\n" + "="*80)
    print("🔄 Автоматическое перенаправление на виртуальное окружение...")
    print("="*80)
    print(f"Текущий Python: {python_path}")
    print(f"Перезапуск через: {venv_python}")
    print("="*80 + "\n")
    
    # Перезапускаем через venv Python
    os.execv(venv_python, [venv_python, main_py_path] + sys.argv[1:])
    # execv не возвращается, если успешно

# Если venv не найден или уже в venv - импортируем main
if __name__ == '__main__':
    # Импортируем и запускаем main
    import importlib.util
    spec = importlib.util.spec_from_file_location("main", main_py_path)
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)







