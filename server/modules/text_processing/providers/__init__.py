"""
Text Processing Providers - Провайдеры для обработки текста

Содержит:
- LangChainGeminiProvider - провайдер для обработки текста через LangChain
- Поддержка стриминга, изображений (WebP/JPEG) и Google Search
"""

from .langchain_gemini_provider import LangChainGeminiProvider

__all__ = ['LangChainGeminiProvider']
