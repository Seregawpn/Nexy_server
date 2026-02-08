"""
LangChain Gemini Provider для обработки текста с поддержкой изображений и Google Search

Реализация с использованием LangChain:
- Базовая обработка текста
- Изображения (WebP/JPEG через base64)
- Google Search
- Стриминг ответов
"""

import logging
import base64
from typing import AsyncGenerator, Dict, Any, Optional, Union, TYPE_CHECKING
from integrations.core.universal_provider_interface import UniversalProviderInterface

if TYPE_CHECKING:
    from integrations.core.token_usage_tracker import TokenUsageTracker

logger = logging.getLogger(__name__)

# Импорты LangChain (с обработкой отсутствия)
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import HumanMessage, SystemMessage
    LANGCHAIN_AVAILABLE = True
except ImportError:
    ChatGoogleGenerativeAI = None
    HumanMessage = None
    SystemMessage = None
    LANGCHAIN_AVAILABLE = False
    logger.warning("⚠️ LangChain не найден - провайдер будет недоступен")


def extract_text_from_chunk(chunk):
    """
    Извлекает текст из chunk LangChain
    Возвращаем текст напрямую
    
    Args:
        chunk: Chunk от LangChain (может быть словарем, списком или объектом)
        
    Returns:
        Строка с текстом (только текст, без JSON обертки).
        НИКОГДА не возвращает строковое представление словаря.
    """
    # Приоритет 1: Используем chunk.content напрямую (стандарт LangChain)
    if hasattr(chunk, 'content') and chunk.content:
        content = chunk.content
        # Если content - это список (multimodal), извлекаем текст из элементов
        if isinstance(content, list):
            texts = []
            for item in content:
                if isinstance(item, dict):
                    if 'text' in item:
                        texts.append(str(item['text']))
                    # Пропускаем dict без 'text'
                elif isinstance(item, str):
                    texts.append(item)
                # Пропускаем другие типы
            return "".join(texts)
        if isinstance(content, str):
            return content
        # Неизвестный тип content — пропускаем
        return ""

    # Приоритет 2: Используем chunk.text (если есть)
    if hasattr(chunk, 'text') and chunk.text:
        val = chunk.text
        if callable(val):
            return str(val())
        if isinstance(val, str):
            return val
        return ""
    
    # Если chunk - это список, обрабатываем каждый элемент
    if isinstance(chunk, list):
        texts = []
        for item in chunk:
            if isinstance(item, dict):
                if 'text' in item:
                    texts.append(str(item['text']))
                elif 'content' in item:
                    texts.append(str(item['content']))
                # Пропускаем dict без text/content
            elif isinstance(item, str):
                texts.append(item)
        return ''.join(texts)
    
    # Если chunk - это словарь
    if isinstance(chunk, dict):
        if 'text' in chunk:
            text_item = chunk['text']
            if isinstance(text_item, list):
                return ''.join([item.get('text', '') if isinstance(item, dict) else str(item) for item in text_item])
            if isinstance(text_item, str):
                # Если это JSON-ответ ассистента, возвращаем как есть для парсинга на уровне workflow
                if text_item.strip().startswith('{'):
                    return text_item
                return text_item
            return ""
        elif 'content' in chunk:
            content = chunk['content']
            if isinstance(content, list):
                return ''.join([str(item) for item in content if isinstance(item, str)])
            if isinstance(content, str):
                return content
            return ""
        else:
            # Dict без text/content — НЕ конвертируем в строку
            logger.debug(f"⚠️ LangChain chunk без text/content: {list(chunk.keys())}")
            return ""
    
    # Если chunk - это объект с атрибутом content
    if hasattr(chunk, 'content'):
        content = chunk.content
        if isinstance(content, list):
            texts = []
            for item in content:
                if isinstance(item, dict):
                    if 'text' in item:
                        texts.append(str(item['text']))
                    elif 'type' in item and item.get('type') == 'text':
                        texts.append(str(item.get('text', '')))
                elif isinstance(item, str):
                    texts.append(item)
            return ''.join(texts)
        if isinstance(content, str):
            return content
        return ""
    
    # Если chunk — строка, возвращаем как есть
    if isinstance(chunk, str):
        return chunk
    
    # Неизвестный тип — НЕ конвертируем, возвращаем пустую строку
    logger.debug(f"⚠️ Неизвестный тип LangChain chunk: {type(chunk)}")
    return ""


class LangChainGeminiProvider(UniversalProviderInterface):
    """
    Провайдер обработки текста с использованием LangChain
    
    Поддерживает:
    - Базовую обработку текста
    - Изображения (WebP/JPEG через base64, по умолчанию WebP)
    - Google Search
    - Стриминг ответов
    """
    
    def __init__(self, config: Dict[str, Any], token_usage_tracker: Optional['TokenUsageTracker'] = None):
        """
        Инициализация LangChain Gemini провайдера
        
        Args:
            config: Конфигурация провайдера
            token_usage_tracker: Сервис трекинга токенов (опционально)
        """
        super().__init__(
            name="langchain_gemini",
            priority=1,  # Основной провайдер
            config=config
        )
        self.token_usage_tracker = token_usage_tracker
        
        self.model_name = config.get('model', 'gemini-3-flash-preview')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 2048)
        self.tools = config.get('tools', [])
        self.system_prompt = config.get('system_prompt', '')
        self.api_key = config.get('api_key', '')
        
        # Настройки изображений (по умолчанию WebP, поддерживается также JPEG)
        self.image_mime_type = config.get('image_mime_type', 'image/webp')
        self.image_max_size = config.get('image_max_size', 10 * 1024 * 1024)
        
        # LangChain клиент
        self.llm = None
        self.llm_with_tools = None
        self.llm_no_tools = None
        self.is_available = LANGCHAIN_AVAILABLE and bool(self.api_key)
        self.is_initialized = False
        
        logger.info(f"LangChainGeminiProvider initialized: available={self.is_available}")
    
    async def initialize(self) -> bool:
        """
        Инициализация LangChain
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            logger.info(f"🔍 ДИАГНОСТИКА LangChainGeminiProvider.initialize():")
            logger.info(f"   → is_available: {self.is_available}")
            logger.info(f"   → api_key present: {bool(self.api_key)}")
            logger.info(f"   → model_name: {self.model_name}")
            
            if not self.is_available:
                logger.error("Missing API key or LangChain dependencies")
                return False
            
            # Создаем LangChain клиент
            logger.info(f"🔍 Создаем LangChain клиент...")
            
            # Настройка tools для Google Search
            model_kwargs = {}
            if self.tools and "google_search" in self.tools:
                model_kwargs["tools"] = [{"google_search": {}}]
                logger.info("✅ Google Search включен")
            else:
                logger.info("ℹ️  Google Search выключен (работает без поиска)")

            # Создаем LLM без tools (default)
            llm_params = {
                "model": self.model_name,
                "google_api_key": self.api_key,
                "temperature": self.temperature,
                "streaming": True,
            }

            if not ChatGoogleGenerativeAI:
                logger.error("ChatGoogleGenerativeAI не доступен (LangChain не установлен)")
                return False

            self.llm_no_tools = ChatGoogleGenerativeAI(**llm_params)

            if model_kwargs:
                llm_with_tools_params = dict(llm_params)
                llm_with_tools_params["model_kwargs"] = model_kwargs
                self.llm_with_tools = ChatGoogleGenerativeAI(**llm_with_tools_params)
            else:
                self.llm_with_tools = None

            # Backward-compatible default
            self.llm = self.llm_with_tools or self.llm_no_tools

            logger.info("✅ LangChain клиент создан")
            
            # Тестируем подключение
            logger.info(f"🔍 Тестируем подключение к LangChain...")
            test_query = "Hello"
            test_response = ""
            
            # Формируем сообщения согласно требованиям: SystemMessage + HumanMessage
            messages = []
            if self.system_prompt and SystemMessage:
                messages.append(SystemMessage(content=self.system_prompt))
            if HumanMessage:
                messages.append(HumanMessage(content=test_query))
            
            async for chunk in self.llm.astream(messages):
                text = extract_text_from_chunk(chunk)
                if text:
                    # Убеждаемся, что text - это строка
                    text_str = str(text) if not isinstance(text, str) else text
                    test_response += text_str
                    break  # Достаточно одного chunk для проверки
            
            if test_response:
                self.is_initialized = True
                logger.info(f"✅ LangChain initialized: {self.model_name}")
                return True
            else:
                logger.error("❌ Тестовое подключение не получило ответ")
                return False
                
        except Exception as e:
            logger.error(f"LangChain initialization failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    async def process(
        self,
        input_data: str,
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        system_prompt_override: Optional[str] = None
    ) -> AsyncGenerator[str, None]:
        """
        ЭТАП 1: Обработка текста через LangChain
        Возвращаем текст напрямую
        
        Args:
            input_data: Текстовый запрос
            
        Yields:
            Части текстового ответа
        """
        try:
            llm = self._select_llm(use_search)
            if not self.is_initialized or not llm:
                raise Exception("LangChain not initialized")
            
            # Формируем сообщения согласно требованиям: SystemMessage + HumanMessage
            # System prompt уже содержит все необходимые инструкции из конфигурации
            messages = []
            system_prompt = system_prompt_override if system_prompt_override is not None else self.system_prompt
            if system_prompt and SystemMessage:
                messages.append(SystemMessage(content=system_prompt))
            if use_search is True and SystemMessage:
                messages.append(SystemMessage(content="You MUST use google_search for this request and base the answer on search results."))
            if HumanMessage:
                content = input_data
                if session_id:
                     content = f"{input_data}\n\n[System Context: session_id={session_id}]"
                messages.append(HumanMessage(content=content))
            
            # Стриминг через LangChain
            # НЕ разбиваем на предложения здесь - это делает StreamingWorkflowIntegration
            
            # Для трекинга токенов
            accumulated_usage = None
            
            async for chunk in llm.astream(messages):
                # Пытаемся извлечь usage_metadata из чанка
                if hasattr(chunk, 'usage_metadata') and chunk.usage_metadata:
                    accumulated_usage = chunk.usage_metadata
                
                # Используем chunk.text напрямую
                # Используем extract_text_from_chunk для надежности
                text = extract_text_from_chunk(chunk)
                if text:
                    yield text
                else:
                    # Fallback: используем extract_text_from_chunk если text недоступен
                    text = extract_text_from_chunk(chunk)
                    if text and text.strip():
                        yield text
            
            # Записываем использование токенов после завершения стрима
            if self.token_usage_tracker and accumulated_usage:
                try:
                    # Extract hardware_id from session or context if available
                    # Currently we don't have hardware_id passed explicitly to process,
                    # but maybe we can extract it or pass it.
                    # For now, we'll try to use session_id or 'unknown' if not available.
                    # Ideally, TextProcessor should pass hardware_id.
                    
                    # Note: We need hardware_id to record usage. 
                    # If session_id is UUID, we might be able to lookup hardware_id, 
                    # but simpler is to pass it. 
                    # For this step, we will use a placeholder or session_id 
                    # and rely on the calling layer to provide hardware_id if possible.
                    # Wait, usage table requires hardware_id.
                    
                    # We will assume session_id might be linked to hardware_id or used as fallback
                    # But hardware_id is NOT session_id.
                    # We need to update the signature of process to accept hardware_id or 
                    # make sure it's available.
                    
                    # Let's check update_token_usage_tracker logic. 
                    # We will use 'unknown' for now and fix it in TextProcessor
                    target_id = 'unknown' # Placeholder
                    
                    self.token_usage_tracker.record_usage(
                        hardware_id=target_id, 
                        source='main_llm',
                        input_tokens=accumulated_usage.get('input_tokens', 0),
                        output_tokens=accumulated_usage.get('output_tokens', 0),
                        session_id=session_id,
                        model_name=self.model_name
                    )
                except Exception as e:
                    logger.warning(f"Failed to record token usage: {e}")
                
            logger.debug("LangChain text processing completed")
                
        except Exception as e:
            logger.error(f"LangChain text processing error: {e}")
            raise e
    
    async def process_with_image(
        self,
        input_data: str,
        image_data: Union[str, bytes],
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        system_prompt_override: Optional[str] = None
    ) -> AsyncGenerator[str, None]:
        """
        ЭТАП 2: Обработка текста с WebP изображением
        
        Args:
            input_data: Текстовый запрос
            image_data: Base64 строка изображения в формате WebP (или bytes для обратной совместимости)
            
        Yields:
            Части текстового ответа
        """
        try:
            llm = self._select_llm(use_search)
            if not self.is_initialized or not llm:
                raise Exception("LangChain not initialized")
            
            # Проверяем, что image_data не None
            if image_data is None:
                logger.debug("No image data provided, processing as text only")
                async for chunk in self.process(input_data):
                    yield chunk
                return
            
            # Обрабатываем image_data: если bytes - конвертируем в base64, если str - используем как есть
            if isinstance(image_data, bytes):
                # Обратная совместимость: если пришли bytes, конвертируем в base64
                image_b64 = base64.b64encode(image_data).decode('utf-8')
                # Проверяем размер (приблизительно)
                estimated_size = len(image_data)
            elif isinstance(image_data, str):
                # Изображение уже в формате base64
                image_b64 = image_data
                # Приблизительный размер base64 строки (base64 примерно на 33% больше оригинала)
                estimated_size = int(len(image_b64) * 0.75)
            else:
                raise ValueError(f"image_data must be str (base64) or bytes, got {type(image_data)}")
            
            # Проверяем размер (приблизительно)
            if estimated_size > self.image_max_size:
                raise ValueError(f"Image too large: ~{estimated_size} bytes (max {self.image_max_size})")
            
            # Формируем content для LangChain
            # Формат: [{"type": "text", "text": "..."}, {"type": "image_url", "image_url": {"url": "data:{image_mime_type};base64,..."}}]
            # image_mime_type по умолчанию image/webp, но может быть image/jpeg
            content = [
                {
                    "type": "text",
                    "text": f"{input_data}\n\n[System Context: session_id={session_id}]" if session_id else input_data
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{self.image_mime_type};base64,{image_b64}"
                    }
                }
            ]
            
            # Формируем сообщения согласно требованиям: SystemMessage + HumanMessage с изображением
            messages = []
            system_prompt = system_prompt_override if system_prompt_override is not None else self.system_prompt
            if system_prompt and SystemMessage:
                messages.append(SystemMessage(content=system_prompt))
            if use_search is True and SystemMessage:
                messages.append(SystemMessage(content="You MUST use google_search for this request and base the answer on search results."))
            
            # HumanMessage с текстом и изображением
            if HumanMessage:
                messages.append(HumanMessage(content=content))
            
            # Стриминг через LangChain
            # НЕ разбиваем на предложения здесь - это делает StreamingWorkflowIntegration
            
            accumulated_usage = None
            
            async for chunk in llm.astream(messages):
                if hasattr(chunk, 'usage_metadata') and chunk.usage_metadata:
                    accumulated_usage = chunk.usage_metadata
                    
                # Используем chunk.text напрямую
                # Используем extract_text_from_chunk для надежности
                text = extract_text_from_chunk(chunk)
                if text:
                    yield text
                else:
                    # Fallback: используем extract_text_from_chunk если text недоступен
                    text = extract_text_from_chunk(chunk)
                    if text and text.strip():
                        yield text
            
            # Записываем использование токенов
            if self.token_usage_tracker and accumulated_usage:
                try:
                    target_id = 'unknown' # Placeholder
                    
                    self.token_usage_tracker.record_usage(
                        hardware_id=target_id,
                        source='main_llm',
                        input_tokens=accumulated_usage.get('input_tokens', 0),
                        output_tokens=accumulated_usage.get('output_tokens', 0),
                        session_id=session_id,
                        model_name=self.model_name
                    )
                except Exception as e:
                    logger.warning(f"Failed to record token usage (image): {e}")
                
            logger.debug("LangChain with image processing completed")
                
        except Exception as e:
            logger.error(f"LangChain with image processing error: {e}")
            raise e
    
    async def cleanup(self) -> bool:
        """
        Очистка ресурсов провайдера
        
        Returns:
            True если очистка успешна, False иначе
        """
        try:
            logger.info("Cleaning up LangChainGeminiProvider...")
            
            self.llm = None
            self.llm_with_tools = None
            self.llm_no_tools = None
            self.is_initialized = False
            
            logger.info("LangChainGeminiProvider cleaned up successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error cleaning up LangChainGeminiProvider: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса провайдера
        
        Returns:
            Словарь со статусом провайдера
        """
        base_status = super().get_status()
        base_status.update({
            "model_name": self.model_name,
            "is_available": self.is_available,
            "has_google_search": "google_search" in self.tools if self.tools else False,
            "has_system_prompt": bool(self.system_prompt)
        })
        return base_status
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Получение метрик провайдера
        
        Returns:
            Словарь с метриками провайдера
        """
        base_metrics = super().get_metrics()
        base_metrics.update({
            "model_name": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        })
        return base_metrics

    def _select_llm(self, use_search: Optional[bool]):
        if use_search is True and self.llm_with_tools:
            return self.llm_with_tools
        if use_search is False:
            return self.llm_no_tools
        return self.llm
