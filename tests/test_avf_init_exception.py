"""
Тест для проверки исключений при инициализации AVF
"""
import pytest
import sys
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestAVFInitException:
    """Тесты для проверки исключений при инициализации AVF"""
    
    def test_avf_config_loading(self):
        """Тест: Проверка загрузки конфигурации AVF"""
        from config.unified_config_loader import UnifiedConfigLoader
        
        loader = UnifiedConfigLoader()
        
        print(f"\n🔍 ДИАГНОСТИКА: Загрузка конфигурации AVF:")
        
        try:
            audio_config = loader.get_audio_config_object()
            print(f"   ✅ audio_config загружен: {audio_config is not None}")
        except Exception as e:
            print(f"   ❌ Ошибка загрузки audio_config: {e}")
            import traceback
            traceback.print_exc()
            raise
        
        try:
            avf_config = loader.get_audio_avf_config()
            print(f"   ✅ avf_config загружен: {avf_config is not None}")
            print(f"   - avf.enabled: {avf_config.get('avf', {}).get('enabled', False)}")
            print(f"   - ks_avf.enabled: {avf_config.get('ks_avf', {}).get('enabled', False)}")
        except Exception as e:
            print(f"   ❌ Ошибка загрузки avf_config: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def test_avf_engine_creation(self):
        """Тест: Проверка создания AVFAudioEngine"""
        from config.unified_config_loader import UnifiedConfigLoader
        from modules.audio_avf import AVFAudioEngine
        
        loader = UnifiedConfigLoader()
        
        print(f"\n🔍 ДИАГНОСТИКА: Создание AVFAudioEngine:")
        
        try:
            audio_config = loader.get_audio_config_object()
            print(f"   ✅ audio_config получен")
            
            avf_engine = AVFAudioEngine(audio_config)
            print(f"   ✅ AVFAudioEngine создан: {avf_engine is not None}")
        except Exception as e:
            print(f"   ❌ Ошибка создания AVFAudioEngine: {e}")
            import traceback
            traceback.print_exc()
            raise

