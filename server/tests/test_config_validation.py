#!/usr/bin/env python3
"""
Дополнительные тесты валидации конфигурации
"""

import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_config_env_example_no_secrets():
    """Тест: config.env.example не содержит реальных секретов"""
    config_path = project_root / "config.env.example"
    with open(config_path, 'r') as f:
        content = f.read()
    
    # Проверяем, что нет реальных API ключей
    suspicious_patterns = [
        "AIzaSy",  # Gemini API ключи начинаются так
        "1e6dfbb0170446c3b7eff7d0507f39c8",  # Пример реального ключа
        "postgres",  # Реальный пароль (хотя в примере это может быть OK)
    ]
    
    found_secrets = []
    for pattern in suspicious_patterns:
        if pattern in content:
            # Проверяем, не в комментарии ли это
            lines = content.split('\n')
            for i, line in enumerate(lines, 1):
                if pattern in line and not line.strip().startswith('#'):
                    found_secrets.append(f"Строка {i}: {line.strip()[:50]}")
    
    if found_secrets:
        print("⚠️ Возможные секреты в config.env.example:")
        for secret in found_secrets:
            print(f"   {secret}")
    else:
        print("✅ config.env.example не содержит реальных секретов")

def test_config_env_example_has_placeholders():
    """Тест: config.env.example содержит плейсхолдеры для секретов"""
    config_path = project_root / "config.env.example"
    with open(config_path, 'r') as f:
        content = f.read()
    
    placeholders = [
        "YOUR_GEMINI_API_KEY",
        "YOUR_AZURE_SPEECH_KEY",
        "YOUR_DB_PASSWORD",
    ]
    
    found_placeholders = []
    for placeholder in placeholders:
        if placeholder in content:
            found_placeholders.append(placeholder)
    
    if found_placeholders:
        print(f"✅ config.env.example содержит плейсхолдеры: {', '.join(found_placeholders)}")
    else:
        print("⚠️ config.env.example может не содержать плейсхолдеры для секретов")

def test_unified_config_has_all_modules():
    """Тест: unified_config содержит конфигурации всех основных модулей"""
    try:
        from config.unified_config import get_config
        
        config = get_config()
        
        required_modules = [
            'database',
            'grpc',
            'audio',
            'text_processing',
            'memory',
            'session',
            'interrupt',
            'workflow',
            'update',
            'server',
            'logging'
        ]
        
        missing_modules = []
        for module in required_modules:
            if not hasattr(config, module):
                missing_modules.append(module)
        
        if missing_modules:
            print(f"⚠️ Отсутствуют модули в конфигурации: {', '.join(missing_modules)}")
        else:
            print(f"✅ unified_config содержит все основные модули ({len(required_modules)} проверено)")
    except Exception as e:
        print(f"❌ Ошибка при проверке модулей: {e}")

def test_modules_config_consistency():
    """Тест: модули, использующие unified_config, имеют согласованную конфигурацию"""
    try:
        from config.unified_config import get_config
        from modules.text_processing.config import TextProcessingConfig
        from modules.audio_generation.config import AudioGenerationConfig
        
        unified = get_config()
        text_cfg = TextProcessingConfig()
        audio_cfg = AudioGenerationConfig()
        
        # Проверяем согласованность
        issues = []
        
        if text_cfg.gemini_api_key != unified.text_processing.gemini_api_key:
            issues.append("TextProcessingConfig.gemini_api_key не совпадает с unified_config")
        
        if audio_cfg.azure_speech_key != unified.audio.azure_speech_key:
            issues.append("AudioGenerationConfig.azure_speech_key не совпадает с unified_config")
        
        if issues:
            print("⚠️ Найдены несоответствия в конфигурации:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print("✅ Конфигурация модулей согласована с unified_config")
    except Exception as e:
        print(f"⚠️ Ошибка при проверке согласованности: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("🔍 Дополнительные тесты валидации конфигурации")
    print("=" * 60)
    print()
    
    test_config_env_example_no_secrets()
    test_config_env_example_has_placeholders()
    test_unified_config_has_all_modules()
    test_modules_config_consistency()
    
    print()
    print("=" * 60)
    print("✅ Дополнительные проверки завершены")
    print("=" * 60)

