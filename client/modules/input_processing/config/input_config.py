"""
Конфигурация модулей ввода
"""

from dataclasses import dataclass
from typing import Any

from ..keyboard.types import KeyboardConfig

# from ..speech.types import SpeechConfig  # Временно отключено

@dataclass
class InputConfig:
    """Общая конфигурация модулей ввода"""
    keyboard: KeyboardConfig | None = None
    # speech: SpeechConfig = None  # Временно отключено
    
    def __post_init__(self):
        """Инициализация конфигурации по умолчанию"""
        if self.keyboard is None:
            # Значения по умолчанию из unified_config.yaml
            self.keyboard = KeyboardConfig(
                key_to_monitor="ctrl_n",
                short_press_threshold=0.1,
                long_press_threshold=0.6,
                event_cooldown=0.1,
                hold_check_interval=0.05,
                debounce_time=0.1,
            )
        # if self.speech is None:  # Временно отключено
        #     self.speech = SpeechConfig()
    
    @classmethod
    def from_dict(cls, config_dict: dict[str, Any]) -> 'InputConfig':
        """Создает конфигурацию из словаря"""
        keyboard_config = KeyboardConfig(**config_dict.get('keyboard', {}))
        # speech_config = SpeechConfig(**config_dict.get('speech', {}))  # Временно отключено
        
        return cls(
            keyboard=keyboard_config,
            # speech=speech_config  # Временно отключено
        )
    
    def to_dict(self) -> dict[str, Any]:
        """Преобразует конфигурацию в словарь"""
        if self.keyboard is None:
            return {'keyboard': {}}
        return {
            'keyboard': {
                'key_to_monitor': self.keyboard.key_to_monitor,
                'short_press_threshold': self.keyboard.short_press_threshold,
                'long_press_threshold': self.keyboard.long_press_threshold,
                'event_cooldown': self.keyboard.event_cooldown,
                'hold_check_interval': self.keyboard.hold_check_interval,
                'debounce_time': self.keyboard.debounce_time,
                'combo_timeout_sec': self.keyboard.combo_timeout_sec,
                'key_state_timeout_sec': self.keyboard.key_state_timeout_sec,
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
    
    config_loader = UnifiedConfigLoader.get_instance()
    input_config = config_loader.get_input_processing_config()
    
    # Преобразуем KeyboardConfig из unified_config_loader в KeyboardConfig из types
    unified_kbd_config = input_config.keyboard
    keyboard_config = KeyboardConfig(
        key_to_monitor=unified_kbd_config.key_to_monitor,
        short_press_threshold=unified_kbd_config.short_press_threshold,
        long_press_threshold=unified_kbd_config.long_press_threshold,
        event_cooldown=unified_kbd_config.event_cooldown,
        hold_check_interval=unified_kbd_config.hold_check_interval,
        debounce_time=unified_kbd_config.debounce_time,
        combo_timeout_sec=unified_kbd_config.combo_timeout_sec,
        key_state_timeout_sec=unified_kbd_config.key_state_timeout_sec,
    )
    
    return InputConfig(
        keyboard=keyboard_config
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