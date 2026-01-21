"""
Конфигурация модулей ввода
"""

from dataclasses import dataclass
from typing import Dict, Any

from ..keyboard.types import KeyboardConfig
# from ..speech.types import SpeechConfig  # Временно отключено

@dataclass
class InputConfig:
    """Общая конфигурация модулей ввода"""
    keyboard: KeyboardConfig = None
    # speech: SpeechConfig = None  # Временно отключено
    
    def __post_init__(self):
        """Инициализация конфигурации по умолчанию"""
        if self.keyboard is None:
            self.keyboard = KeyboardConfig()
        # if self.speech is None:  # Временно отключено
        #     self.speech = SpeechConfig()
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'InputConfig':
        """Создает конфигурацию из словаря"""
        keyboard_config = KeyboardConfig(**config_dict.get('keyboard', {}))
        # speech_config = SpeechConfig(**config_dict.get('speech', {}))  # Временно отключено
        
        return cls(
            keyboard=keyboard_config,
            # speech=speech_config  # Временно отключено
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Преобразует конфигурацию в словарь"""
        return {
            'keyboard': {
                'enabled': self.keyboard.enabled,
                'monitor_spacebar': self.keyboard.monitor_spacebar,
                'spacebar_short_press_duration': self.keyboard.spacebar_short_press_duration,
                'spacebar_long_press_duration': self.keyboard.spacebar_long_press_duration,
                'monitor_escape': self.keyboard.monitor_escape,
                'monitor_enter': self.keyboard.monitor_enter,
                'event_cooldown': self.keyboard.event_cooldown,
                'hold_check_interval': self.keyboard.hold_check_interval,
                'debounce_time': self.keyboard.debounce_time,
            },
            # 'speech': {  # Временно отключено
            #     'enabled': self.speech.enabled,
            #     'language': self.speech.language,
            #     'timeout': self.speech.timeout,
            #     'phrase_timeout': self.speech.phrase_timeout,
            #     'energy_threshold': self.speech.energy_threshold,
            #     'dynamic_energy_threshold': self.speech.dynamic_energy_threshold,
            #     'pause_threshold': self.speech.pause_threshold,
            #     'phrase_threshold': self.speech.phrase_threshold,
            #     'non_speaking_duration': self.speech.non_speaking_duration,
            #     'max_duration': self.speech.max_duration,
            #     'auto_start': self.speech.auto_start,
            # }
        }

def get_default_input_config() -> InputConfig:
    """Получает конфигурацию по умолчанию из UnifiedConfigLoader"""
    from config.unified_config_loader import UnifiedConfigLoader
    
    config_loader = UnifiedConfigLoader()
    input_config = config_loader.get_input_processing_config()
    
    return InputConfig(
        keyboard=input_config.keyboard
        # speech=SpeechConfig(  # Временно отключено
        #     sample_rate=16000,
        #     chunk_size=1024,
        #     channels=1,
        #     dtype='int16',
        #     energy_threshold=100,
        #     dynamic_energy_threshold=True,
        #     pause_threshold=0.5,
        #     phrase_threshold=0.3,
        #     non_speaking_duration=0.3,
        #     max_duration=30.0,
        #     auto_start=True
        # )
    )

# Для обратной совместимости
DEFAULT_INPUT_CONFIG = get_default_input_config()