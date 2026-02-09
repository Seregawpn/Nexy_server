"""
Основной TextProcessor - координатор модуля обработки текста

Использует LangChain провайдер для обработки текста:
- Стриминговая обработка текста (текст → поток текста)
- Стриминговая обработка с изображениями (текст + изображение WebP/JPEG → поток текста)  
- Google Search (текст + изображение + поиск → поток текста)
"""

import logging
from typing import Dict, Any, Optional, Union, AsyncGenerator
from modules.text_processing.config import TextProcessingConfig
from modules.text_processing.providers.langchain_gemini_provider import LangChainGeminiProvider
from config.unified_config import get_config
from config.prompts import build_system_prompt, resolve_prompt_sections

logger = logging.getLogger(__name__)

class TextProcessor:
    """
    Основной процессор текста с использованием LangChain провайдера
    
    Обеспечивает единый интерфейс для стриминговой обработки 
    текстовых запросов с поддержкой изображений и поиска.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None, token_usage_tracker: Optional[Any] = None):
        """
        Инициализация процессора текста
        
        Args:
            config: Конфигурация модуля
            token_usage_tracker: Сервис трекинга токенов (опционально)
        """
        self.config = TextProcessingConfig(config)
        self.token_usage_tracker = token_usage_tracker
        
        # Всегда используем LangChain провайдер
        logger.info("TextProcessor: Using LangChain provider")
        self.live_provider = LangChainGeminiProvider(
            self.config.get_provider_config('langchain'),
            token_usage_tracker=self.token_usage_tracker
        )
        
        self.is_initialized = False
        
        logger.info("TextProcessor initialized with LangChain provider")

    @staticmethod
    def _build_prompt_for_text(text: str) -> tuple[str, Dict[str, bool]]:
        config = get_config()
        sections = resolve_prompt_sections(text)

        prompt = build_system_prompt(
            system_control_enabled=sections["system_control"],
            describe_enabled=sections["describe"],
            messages_enabled=bool(config.features.messages_enabled and sections["messages"]),
            whatsapp_enabled=bool(config.whatsapp.enabled and sections["whatsapp"]),
            browser_enabled=bool(config.browser_use.enabled and sections["browser"]),
            payment_enabled=bool(config.subscription.is_active() and sections["payment"]),
            web_search_enabled=bool(config.features.web_search_enabled and sections["web_search"]),
        )
        return prompt, sections
    
    async def initialize(self) -> bool:
        """
        Инициализация LangChain провайдера
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info("Initializing TextProcessor with LangChain provider...")
            
            if await self.live_provider.initialize():
                self.is_initialized = True
                logger.info("TextProcessor initialized with LangChain provider")
                return True
            else:
                logger.error("Failed to initialize LangChain provider")
                return False
                
        except Exception as e:
            logger.error(f"TextProcessor initialization error: {e}")
            return False
    
    
    async def process_text_streaming(
        self,
        text: str,
        image_data: Optional[Union[str, bytes]] = None,
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None
    ) -> AsyncGenerator[str, None]:
        """
        Стриминговая обработка текста с изображением через LangChain провайдер
        Возвращает текст напрямую
        
        Args:
            text: Текстовый запрос
            image_data: Base64 строка (str) или bytes изображения в формате WebP/JPEG (опционально)
            session_id: ID сессии (опционально, для контекста LLM)
            
        Yields:
            Части текстового ответа
        """
        try:
            if not self.is_initialized:
                raise Exception("TextProcessor not initialized")

            system_prompt_override = None
            if text:
                system_prompt_override, sections = self._build_prompt_for_text(text)
                if use_search is None:
                    use_search = bool(self.config.web_search_enabled and sections.get("web_search"))
                logger.info(
                    "TextProcessor: prompt_sections=%s use_search=%s",
                    sections,
                    use_search
                )
            
            # Вызываем правильный метод в зависимости от наличия изображения
            if image_data:
                async for chunk in self.live_provider.process_with_image(
                    text,
                    image_data,
                    session_id=session_id,
                    use_search=use_search,
                    system_prompt_override=system_prompt_override
                ):
                    yield chunk
            else:
                async for chunk in self.live_provider.process(
                    text,
                    session_id=session_id,
                    use_search=use_search,
                    system_prompt_override=system_prompt_override
                ):
                    yield chunk
                
        except Exception as e:
            logger.error(f"Text streaming error: {e}")
            raise e
    
    async def cleanup(self) -> bool:
        """
        Очистка ресурсов процессора
        
        Returns:
            True если очистка успешна, False иначе
        """
        try:
            logger.info("Cleaning up TextProcessor...")
            
            # Очищаем LangChain провайдер
            if self.live_provider:
                await self.live_provider.cleanup()
            
            self.is_initialized = False
            logger.info("TextProcessor cleaned up successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error cleaning up TextProcessor: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса процессора
        
        Returns:
            Словарь со статусом процессора
        """
        status = {
            "is_initialized": self.is_initialized,
            "config_status": self.config.get_status(),
            "live_provider": self.live_provider.get_status() if self.live_provider else None
        }
        
        return status
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Получение метрик процессора
        
        Returns:
            Словарь с метриками процессора
        """
        metrics = {
            "is_initialized": self.is_initialized,
            "live_provider": self.live_provider.get_metrics() if self.live_provider else None
        }
        
        return metrics
    
    def get_healthy_providers(self) -> list:
        """
        Получение списка здоровых провайдеров
        
        Returns:
            Список здоровых провайдеров (LangChain)
        """
        if self.live_provider and self.live_provider.is_initialized:
            return [self.live_provider]
        return []
    
    def get_failed_providers(self) -> list:
        """
        Получение списка failed провайдеров
        
        Returns:
            Список failed провайдеров
        """
        if self.live_provider and not self.live_provider.is_initialized:
            return [self.live_provider]
        return []
    
    def reset_metrics(self):
        """Сброс метрик процессора"""
        logger.info("TextProcessor metrics reset")
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Получение краткой сводки по процессору
        
        Returns:
            Словарь со сводкой
        """
        summary = {
            "is_initialized": self.is_initialized,
            "total_providers": 1,
            "healthy_providers": len(self.get_healthy_providers()),
            "failed_providers": len(self.get_failed_providers()),
            "config_valid": self.config.validate(),
            "live_api_available": self.live_provider.is_available if self.live_provider else False
        }
        
        return summary
    
    def __str__(self) -> str:
        """Строковое представление процессора"""
        return f"TextProcessor(initialized={self.is_initialized}, provider=langchain, provider_initialized={self.live_provider.is_initialized if self.live_provider else False})"
    
    def __repr__(self) -> str:
        """Представление процессора для отладки"""
        return (
            f"TextProcessor("
            f"initialized={self.is_initialized}, "
            f"provider=langchain, "
            f"provider_initialized={self.live_provider.is_initialized if self.live_provider else False}, "
            f"provider_available={self.live_provider.is_available if self.live_provider else False}"
            f")"
        )
