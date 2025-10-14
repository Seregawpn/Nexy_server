"""
Конфигурация для модуля автопереключения аудио устройств
"""

import re
from typing import List, Dict, Any

# Паттерны для распознавания устройств
AIRPODS_PATTERNS = [
    r"AirPods",
    r"airpods",
    r"Air Pods",
    r"air pods"
]

HEADSET_PATTERNS = [
    r"Headset",
    r"headset",
    r"Headphones",
    r"headphones",
    r"USB.*Audio",
    r"USB.*Headset"
]

BUILTIN_INPUT_NAMES = [
    r"Built-in Microphone",
    r"Built-in Input",
    r"MacBook.*Microphone",
    r"MacBook.*Input",
    r"Internal Microphone",
    r"Internal Input"
]

BUILTIN_OUTPUT_NAMES = [
    r"Built-in Output",
    r"Built-in Speakers",
    r"MacBook.*Speakers",
    r"MacBook.*Output",
    r"Internal Speakers",
    r"Internal Output"
]

# Игнорируемые устройства (например, iPhone Microphone)
IGNORED_PATTERNS = [
    r"iPhone.*Microphone",
    r"iPhone.*Input",
    r"iPad.*Microphone",
    r"iPad.*Input",
    r"iPhone.*",
    r"iPad.*"
]

# Тайминги и пороги
POLL_SEC = 1.0                    # Интервал опроса устройств
DEBOUNCE_MS = 1000                # Дебаунс при изменениях
HEALTH_SEC = 0.3                  # Время health-check
RMS_MIN = 1e-3                    # Минимальный RMS для считания устройства рабочим
FAILS_TO_QUARANTINE = 2           # Количество провалов до карантина
QUARANTINE_SEC = 45               # Время карантина
MAX_RETRIES = 3                   # Максимальное количество попыток переключения
RETRY_DELAYS = [0.0, 0.3, 0.8]   # Задержки между попытками

# Настройки аудио
DEFAULT_SAMPLE_RATE = 24000       # Частота дискретизации по умолчанию
DEFAULT_CHANNELS = 1              # Количество каналов
DEFAULT_DTYPE = 'int16'           # Тип данных

# Логирование
LOG_LEVEL = 'INFO'                # Уровень логирования
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Конфигурация по умолчанию
DEFAULT_CONFIG = {
    'poll_interval': POLL_SEC,
    'debounce_ms': DEBOUNCE_MS,
    'health_duration': HEALTH_SEC,
    'rms_threshold': RMS_MIN,
    'fails_to_quarantine': FAILS_TO_QUARANTINE,
    'quarantine_duration': QUARANTINE_SEC,
    'max_retries': MAX_RETRIES,
    'retry_delays': RETRY_DELAYS,
    'sample_rate': DEFAULT_SAMPLE_RATE,
    'channels': DEFAULT_CHANNELS,
    'dtype': DEFAULT_DTYPE,
    'log_level': LOG_LEVEL,
    'log_format': LOG_FORMAT
}

def get_config() -> Dict[str, Any]:
    """Получает конфигурацию по умолчанию"""
    return DEFAULT_CONFIG.copy()

def get_device_patterns() -> Dict[str, List[str]]:
    """Получает паттерны для распознавания устройств"""
    return {
        'airpods': AIRPODS_PATTERNS,
        'headset': HEADSET_PATTERNS,
        'builtin_input': BUILTIN_INPUT_NAMES,
        'builtin_output': BUILTIN_OUTPUT_NAMES,
        'ignored': IGNORED_PATTERNS
    }

def compile_patterns(patterns: List[str]) -> List[re.Pattern]:
    """Компилирует регулярные выражения"""
    return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]

"""

import re
from typing import List, Dict, Any

# Паттерны для распознавания устройств
AIRPODS_PATTERNS = [
    r"AirPods",
    r"airpods",
    r"Air Pods",
    r"air pods"
]

HEADSET_PATTERNS = [
    r"Headset",
    r"headset",
    r"Headphones",
    r"headphones",
    r"USB.*Audio",
    r"USB.*Headset"
]

BUILTIN_INPUT_NAMES = [
    r"Built-in Microphone",
    r"Built-in Input",
    r"MacBook.*Microphone",
    r"MacBook.*Input",
    r"Internal Microphone",
    r"Internal Input"
]

BUILTIN_OUTPUT_NAMES = [
    r"Built-in Output",
    r"Built-in Speakers",
    r"MacBook.*Speakers",
    r"MacBook.*Output",
    r"Internal Speakers",
    r"Internal Output"
]

# Игнорируемые устройства (например, iPhone Microphone)
IGNORED_PATTERNS = [
    r"iPhone.*Microphone",
    r"iPhone.*Input",
    r"iPad.*Microphone",
    r"iPad.*Input",
    r"iPhone.*",
    r"iPad.*"
]

# Тайминги и пороги
POLL_SEC = 1.0                    # Интервал опроса устройств
DEBOUNCE_MS = 1000                # Дебаунс при изменениях
HEALTH_SEC = 0.3                  # Время health-check
RMS_MIN = 1e-3                    # Минимальный RMS для считания устройства рабочим
FAILS_TO_QUARANTINE = 2           # Количество провалов до карантина
QUARANTINE_SEC = 45               # Время карантина
MAX_RETRIES = 3                   # Максимальное количество попыток переключения
RETRY_DELAYS = [0.0, 0.3, 0.8]   # Задержки между попытками

# Настройки аудио
DEFAULT_SAMPLE_RATE = 24000       # Частота дискретизации по умолчанию
DEFAULT_CHANNELS = 1              # Количество каналов
DEFAULT_DTYPE = 'int16'           # Тип данных

# Логирование
LOG_LEVEL = 'INFO'                # Уровень логирования
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Конфигурация по умолчанию
DEFAULT_CONFIG = {
    'poll_interval': POLL_SEC,
    'debounce_ms': DEBOUNCE_MS,
    'health_duration': HEALTH_SEC,
    'rms_threshold': RMS_MIN,
    'fails_to_quarantine': FAILS_TO_QUARANTINE,
    'quarantine_duration': QUARANTINE_SEC,
    'max_retries': MAX_RETRIES,
    'retry_delays': RETRY_DELAYS,
    'sample_rate': DEFAULT_SAMPLE_RATE,
    'channels': DEFAULT_CHANNELS,
    'dtype': DEFAULT_DTYPE,
    'log_level': LOG_LEVEL,
    'log_format': LOG_FORMAT
}

def get_config() -> Dict[str, Any]:
    """Получает конфигурацию по умолчанию"""
    return DEFAULT_CONFIG.copy()

def get_device_patterns() -> Dict[str, List[str]]:
    """Получает паттерны для распознавания устройств"""
    return {
        'airpods': AIRPODS_PATTERNS,
        'headset': HEADSET_PATTERNS,
        'builtin_input': BUILTIN_INPUT_NAMES,
        'builtin_output': BUILTIN_OUTPUT_NAMES,
        'ignored': IGNORED_PATTERNS
    }

def compile_patterns(patterns: List[str]) -> List[re.Pattern]:
    """Компилирует регулярные выражения"""
    return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
