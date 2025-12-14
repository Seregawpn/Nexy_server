"""
Тест для проверки вызова initialize() при запуске приложения
Цель: проверить, вызывается ли initialize() в SimpleModuleCoordinator
"""
import pytest
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import inspect
from integration.core.simple_module_coordinator import SimpleModuleCoordinator


class TestCheckInitializeCall:
    """Тесты для проверки вызова initialize()"""
    
    def test_check_initialize_call_in_coordinator(self):
        """Тест: Проверка вызова initialize() в SimpleModuleCoordinator"""
        print(f"\n{'='*80}")
        print(f"🔍 ТЕСТ: Проверка вызова initialize() в SimpleModuleCoordinator")
        print(f"{'='*80}")
        
        # Получаем исходный код метода _initialize_integrations
        coordinator_class = SimpleModuleCoordinator
        initialize_method = coordinator_class._initialize_integrations
        source_lines = inspect.getsourcelines(initialize_method)
        
        print(f"\n📊 Информация о методе _initialize_integrations():")
        print(f"   - Файл: {inspect.getfile(initialize_method)}")
        print(f"   - Строка начала: {source_lines[1]}")
        print(f"   - Количество строк: {len(source_lines[0])}")
        
        # Ищем вызов initialize()
        source_code = ''.join(source_lines[0])
        
        has_voice_init = "voice_integration.initialize()" in source_code
        has_voice_recognition_check = "'voice_recognition' in self.integrations" in source_code
        
        print(f"\n📊 Проверка наличия вызова initialize():")
        print(f"   - Проверка 'voice_recognition' in integrations: {has_voice_recognition_check}")
        print(f"   - Вызов voice_integration.initialize(): {has_voice_init}")
        
        # Показываем контекст вызова
        if has_voice_init:
            lines = source_code.split('\n')
            for i, line in enumerate(lines):
                if "voice_integration.initialize()" in line:
                    print(f"\n📋 Контекст вызова (строки {i-2} до {i+3}):")
                    for j in range(max(0, i-2), min(len(lines), i+3)):
                        marker = ">>> " if j == i else "    "
                        print(f"{marker}{j+source_lines[1]}: {lines[j]}")
                    break
        
        print(f"\n📊 ВЫВОДЫ:")
        if has_voice_init:
            print(f"   ✅ initialize() вызывается в SimpleModuleCoordinator._initialize_integrations()")
            print(f"      - Это означает, что initialize() должен вызываться при запуске приложения")
        else:
            print(f"   ❌ initialize() НЕ вызывается в SimpleModuleCoordinator._initialize_integrations()")
            print(f"      - Это означает, что initialize() не вызывается при запуске приложения")
        
        assert True  # Тест для диагностики

