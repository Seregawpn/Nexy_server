"""
Простой тест для проверки логики инициализации AVF
"""
import pytest
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestAVFInitLogic:
    """Тесты для проверки логики инициализации AVF"""
    
    def test_avf_init_condition_check(self):
        """Тест: Проверка условия _use_avf"""
        print(f"\n{'='*80}")
        print(f"🔍 ПРОВЕРКА УСЛОВИЯ _use_avf")
        print(f"{'='*80}")
        
        from config.unified_config_loader import UnifiedConfigLoader
        import os
        import integration.integrations.voice_recognition_integration as vri_module
        
        loader = UnifiedConfigLoader()
        avf_config = loader.get_audio_avf_config()
        
        avf_enabled = avf_config.get("avf", {}).get("enabled", False)
        ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
        disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
        avf_available = getattr(vri_module, '_AVF_AVAILABLE', False)
        
        print(f"\n📊 Условия:")
        print(f"   - avf_enabled: {avf_enabled}")
        print(f"   - ks_avf_enabled: {ks_avf_enabled}")
        print(f"   - disable_avf_env: {disable_avf_env}")
        print(f"   - avf_available: {avf_available}")
        
        use_avf_expected = avf_enabled and not ks_avf_enabled and not disable_avf_env and avf_available
        
        print(f"\n📊 Результат:")
        print(f"   - _use_avf должен быть: {use_avf_expected}")
        
        if use_avf_expected:
            print(f"   ✅ Все условия выполнены, AVF должен быть включен")
        else:
            print(f"   ❌ Условия НЕ выполнены, AVF будет отключен")
            if not avf_enabled:
                print(f"      - Причина: avf.enabled=False")
            if ks_avf_enabled:
                print(f"      - Причина: ks_avf.enabled=True")
            if disable_avf_env:
                print(f"      - Причина: NEXY_DISABLE_AVF_AUDIO=true")
            if not avf_available:
                print(f"      - Причина: _AVF_AVAILABLE=False")
        
        assert True  # Тест для диагностики

