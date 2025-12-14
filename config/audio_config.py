"""
Конфигурация аудио системы

Централизованные типы для конфигурации аудио из unified_config.yaml
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class AudioInputConfig:
    """Конфигурация входного аудио потока"""
    target_rate: int = 16000  # Целевая частота для ASR
    channels: int = 1  # Моно
    target_dtype: str = "int16"  # Формат для ASR


@dataclass
class AudioOutputConfig:
    """Конфигурация выходного аудио потока"""
    target_rate: int = 48000  # Целевая частота для воспроизведения
    channels: int = 1  # Моно (может быть 2 для стерео)
    target_dtype: str = "int16"  # Формат для воспроизведения


@dataclass
class AudioConfig:
    """Конфигурация аудио системы"""
    input: AudioInputConfig
    output: AudioOutputConfig
    
    @classmethod
    def default(cls) -> 'AudioConfig':
        """Создаёт конфигурацию по умолчанию"""
        return cls(
            input=AudioInputConfig(),
            output=AudioOutputConfig()
        )
    
    @classmethod
    def from_dict(cls, config_dict: dict) -> 'AudioConfig':
        """Создаёт конфигурацию из словаря (из unified_config.yaml)"""
        # Извлекаем параметры для input
        input_config = AudioInputConfig(
            target_rate=config_dict.get('target_sample_rate', 16000),
            channels=config_dict.get('target_channels', 1),
            target_dtype=config_dict.get('target_dtype', 'int16')
        )
        
        # Извлекаем параметры для output
        normalization = config_dict.get('normalization', {})
        output_config = AudioOutputConfig(
            target_rate=normalization.get('output_default_rate', 48000),
            channels=normalization.get('output_max_channels', 1),
            target_dtype=config_dict.get('target_dtype', 'int16')
        )
        
        return cls(
            input=input_config,
            output=output_config
        )
