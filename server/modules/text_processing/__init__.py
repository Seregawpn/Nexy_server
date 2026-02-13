"""
Text Processing Module - Обработка текста с использованием LangChain

Модуль предоставляет функциональность для:
- Стриминговой обработки текстовых запросов через LangChain провайдер
- Поддержки изображений (WebP/JPEG, по умолчанию WebP)
- Интеграции Google Search
- Универсального интерфейса для LangChain провайдера

Реализован только со стриминговыми методами.
"""

from .core.text_processor import TextProcessor
from .config import TextProcessingConfig
from .._version import get_module_version

__all__ = ['TextProcessor', 'TextProcessingConfig']
__version__ = get_module_version()
