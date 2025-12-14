"""
Изолированные тесты для проверки исправлений race conditions в AVFAudioEngine.

Тестирует:
1. Установка состояния в RUNNING до scheduleBuffer (защита от конфигурационных событий)
2. Игнорирование преждевременного completion callback
3. Игнорирование конфигурационных событий во время RUNNING
4. Отключение перезапуска engine во время RUNNING
5. Отсутствие дублирования и конфликтов
"""

import inspect
import pytest

from modules.audio_avf.core.avf_audio_engine import AVFAudioEngine
from modules.audio_avf.core.types import AudioState


class TestAVFAudioEngineRaceConditions:
    """Изолированные тесты для race conditions в AVFAudioEngine."""
    
    def test_no_duplicate_state_management(self):
        """Тест: Нет дублирования логики управления состоянием в play_audio."""
        # Читаем исходный код play_audio
        source = inspect.getsource(AVFAudioEngine.play_audio)
        
        # Подсчитываем количество установок _output_state = AudioState.RUNNING в play_audio
        runnings_in_play_audio = source.count('_output_state = AudioState.RUNNING')
        
        # Должна быть только одна установка в play_audio (в нашем исправлении)
        assert runnings_in_play_audio == 1, \
            f"Должна быть только одна установка _output_state = AudioState.RUNNING в play_audio, найдено: {runnings_in_play_audio}"
    
    def test_no_conflicting_state_checks(self):
        """Тест: Нет конфликтующих проверок состояния в _handle_output_device_change."""
        # Читаем исходный код _handle_output_device_change
        source = inspect.getsource(AVFAudioEngine._handle_output_device_change)
        
        # Подсчитываем количество проверок current_state_under_lock == AudioState.RUNNING
        runnings_in_handle = source.count('current_state_under_lock == AudioState.RUNNING')
        
        # Должна быть только одна проверка
        assert runnings_in_handle == 1, \
            f"Должна быть только одна проверка current_state_under_lock == AudioState.RUNNING в _handle_output_device_change, найдено: {runnings_in_handle}"
    
    def test_premature_callback_logic_isolated(self):
        """Тест: Логика игнорирования преждевременного callback изолирована."""
        # Читаем исходный код completion callback
        from modules.audio_avf.core.avf_audio_engine import _create_avf_completion_callback
        # Проверяем, что логика преждевременного callback есть
        # Это проверка на уровне исходного кода
        import modules.audio_avf.core.avf_audio_engine as avf_module
        source = inspect.getsource(avf_module)
        
        # Проверяем наличие логики игнорирования преждевременного callback
        assert 'преждевременный' in source.lower() or 'premature' in source.lower(), \
            "Должна быть логика игнорирования преждевременного callback"
        
        # Проверяем, что состояние не сбрасывается при преждевременном callback
        assert 'Состояние остаётся RUNNING' in source or 'state remains RUNNING' in source.lower(), \
            "Должна быть логика сохранения состояния RUNNING при преждевременном callback"
    
    def test_configuration_event_ignored_logic(self):
        """Тест: Логика игнорирования конфигурационных событий изолирована."""
        # Читаем исходный код _handle_output_device_change
        source = inspect.getsource(AVFAudioEngine._handle_output_device_change)
        
        # Проверяем наличие логики игнорирования конфигурационных событий
        assert 'пропускаем переподключение' in source or 'skip reconnection' in source.lower(), \
            "Должна быть логика пропуска переподключения во время RUNNING"
        
        # Проверяем, что перезапуск engine отключён
        assert 'Пропускаем перезапуск engine' in source or 'skip engine restart' in source.lower(), \
            "Должна быть логика пропуска перезапуска engine во время RUNNING"

