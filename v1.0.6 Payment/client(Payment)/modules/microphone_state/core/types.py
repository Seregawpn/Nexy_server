"""
Types for microphone state management
"""

from enum import Enum


class MicrophoneState(Enum):
    """Состояние микрофона (централизованное)"""
    IDLE = "idle"              # Микрофон закрыт, нет активных операций
    OPENING = "opening"        # Микрофон открывается (асинхронная операция)
    ACTIVE = "active"          # Микрофон активен, запись идет
    CLOSING = "closing"        # Микрофон закрывается (асинхронная операция)
    ERROR = "error"            # Ошибка, требуется восстановление


