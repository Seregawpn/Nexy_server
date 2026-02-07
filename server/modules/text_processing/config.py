"""
Конфигурация модуля Text Processing
Использует централизованную конфигурацию
"""

from typing import Dict, Any, Optional

from config.unified_config import get_config


class TextProcessingConfig:
    """Конфигурация модуля обработки текста"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация конфигурации из централизованной системы
        
        Args:
            config: Словарь с конфигурацией (опционально, переопределяет централизованную)
        """
        # Получаем централизованную конфигурацию
        unified_config = get_config()
        self.config = config or {}
        
        # Используем централизованные настройки с возможностью переопределения
        self.gemini_api_key = self.config.get('gemini_api_key', unified_config.text_processing.gemini_api_key)
        # Note: System prompt is now built dynamically via build_system_prompt() in get_provider_config()
        
        # LangChain настройки
        self.langchain_model = self.config.get('langchain_model', getattr(unified_config.text_processing, 'langchain_model', 'gemini-3-flash-preview'))
        # Общие настройки для temperature, max_tokens, tools
        self.temperature = self.config.get('temperature', getattr(unified_config.text_processing, 'temperature', 0.7))
        self.max_tokens = self.config.get('max_tokens', getattr(unified_config.text_processing, 'max_tokens', 2048))
        self.tools = self.config.get('tools', getattr(unified_config.text_processing, 'tools', ['google_search']))

        self.web_search_enabled = getattr(unified_config.features, 'web_search_enabled', True)

        
        # Настройки изображений
        self.image_format = self.config.get('image_format', unified_config.text_processing.image_format)
        self.image_mime_type = self.config.get('image_mime_type', unified_config.text_processing.image_mime_type)
        self.image_max_size = self.config.get('image_max_size', unified_config.text_processing.image_max_size)
        self.streaming_chunk_size = self.config.get('streaming_chunk_size', unified_config.text_processing.streaming_chunk_size)
        
        
        # Настройки fallback
        self.fallback_timeout = self.config.get('fallback_timeout', unified_config.text_processing.fallback_timeout)
        self.circuit_breaker_threshold = self.config.get('circuit_breaker_threshold', unified_config.text_processing.circuit_breaker_threshold)
        self.circuit_breaker_timeout = self.config.get('circuit_breaker_timeout', unified_config.text_processing.circuit_breaker_timeout)
        
        # Настройки логирования
        self.log_level = self.config.get('log_level', unified_config.logging.level)
        self.log_requests = self.config.get('log_requests', unified_config.logging.log_requests)
        self.log_responses = self.config.get('log_responses', unified_config.logging.log_responses)
        
        # Настройки производительности
        self.max_concurrent_requests = self.config.get('max_concurrent_requests', unified_config.text_processing.max_concurrent_requests)
        self.request_timeout = self.config.get('request_timeout', unified_config.text_processing.request_timeout)
        
    def get_provider_config(self, provider_name: str) -> Dict[str, Any]:
        """
        Получение конфигурации для конкретного провайдера
        
        Args:
            provider_name: Имя провайдера (только 'langchain' поддерживается)
            
        Returns:
            Словарь с конфигурацией провайдера
        """
        if provider_name == 'langchain':
            # CRITICAL: Use dynamic system prompt with feature-specific instructions
            # Import here to avoid circular dependency at module level
            from config.prompts import build_system_prompt
            
            unified_config = get_config()
            dynamic_prompt = build_system_prompt(
                whatsapp_enabled=unified_config.whatsapp.enabled,
                browser_enabled=unified_config.browser_use.enabled,
                payment_enabled=unified_config.subscription.is_active(),
                messages_enabled=unified_config.features.messages_enabled,
                web_search_enabled=unified_config.features.web_search_enabled,
            )
            
            return {
                'api_key': self.gemini_api_key,
                'model': self.langchain_model,
                'temperature': self.temperature,
                'max_tokens': self.max_tokens,
                'tools': self.tools,
                'system_prompt': dynamic_prompt,
                'image_mime_type': self.image_mime_type,
                'image_max_size': self.image_max_size,
            }
        
        return {}
    
    def get_fallback_config(self) -> Dict[str, Any]:
        """
        Получение конфигурации fallback менеджера
        
        Returns:
            Словарь с конфигурацией fallback
        """
        return {
            'timeout': self.fallback_timeout,
            'circuit_breaker_threshold': self.circuit_breaker_threshold,
            'circuit_breaker_timeout': self.circuit_breaker_timeout,
            'max_concurrent_requests': self.max_concurrent_requests
        }
    
    def validate(self) -> bool:
        """
        Валидация конфигурации
        
        Returns:
            True если конфигурация валидна, False иначе
        """
        # Проверяем наличие API ключа
        if not self.gemini_api_key:
            print("⚠️ GEMINI_API_KEY не установлен")
            return False
            
        # Проверяем корректность параметров
        if not (0 <= self.temperature <= 2):
            print("❌ temperature должен быть между 0 и 2")
            return False
            
        if self.max_tokens <= 0:
            print("❌ max_tokens должен быть положительным")
            return False
            
        if self.fallback_timeout <= 0:
            print("❌ fallback_timeout должен быть положительным")
            return False
            
        return True
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса конфигурации
        
        Returns:
            Словарь со статусом конфигурации
        """
        return {
            'gemini_api_key_set': bool(self.gemini_api_key),
            'langchain_model': self.langchain_model,
            'temperature': self.temperature,
            'max_tokens': self.max_tokens,
            'tools': self.tools,
            'image_format': self.image_format,
            'image_mime_type': self.image_mime_type,
            'image_max_size': self.image_max_size,
            'streaming_chunk_size': self.streaming_chunk_size,
            'fallback_timeout': self.fallback_timeout,
            'circuit_breaker_threshold': self.circuit_breaker_threshold,
            'circuit_breaker_timeout': self.circuit_breaker_timeout,
            'log_level': self.log_level,
            'log_requests': self.log_requests,
            'log_responses': self.log_responses,
            'max_concurrent_requests': self.max_concurrent_requests,
            'request_timeout': self.request_timeout
        }
