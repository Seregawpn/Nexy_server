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
import os
import asyncio
import json
import binascii
from typing import AsyncGenerator, Dict, Any, Optional, Union, TYPE_CHECKING
from integrations.core.universal_provider_interface import UniversalProviderInterface
from config.prompts import build_intent_classifier_prompt, build_route_system_prompt
from config.unified_config import get_config

if TYPE_CHECKING:
    from integrations.core.token_usage_tracker import TokenUsageTracker

logger = logging.getLogger(__name__)

# Импорты LangChain (с обработкой отсутствия)
try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    ChatGoogleGenerativeAI = None

try:
    from google.generativeai.types.content_types import Tool as GoogleGenerativeAITool
except ImportError:
    GoogleGenerativeAITool = None

try:
    from langchain_core.messages import HumanMessage, SystemMessage
except ImportError:
    HumanMessage = None
    SystemMessage = None

LANGCHAIN_AVAILABLE = bool(HumanMessage and SystemMessage and ChatGoogleGenerativeAI)
if not LANGCHAIN_AVAILABLE:
    logger.warning("⚠️ LangChain chat adapters не найдены - провайдер будет недоступен")


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
        
        self.model_name = config.get('model', os.getenv('GEMINI_PRIMARY_MODEL', 'gemini-flash-lite-latest'))
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 2048)
        self.streaming_chunk_size = max(int(config.get('streaming_chunk_size', 120) or 120), 1)
        self.tools = config.get('tools', [])
        self.system_prompt = config.get('system_prompt', '')
        self.api_key = config.get('api_key', '')
        self.fallback_api_key = config.get('fallback_api_key', '')
        self.use_vertex_ai = bool(config.get('use_vertex_ai', False))
        self.vertex_project = str(config.get('vertex_project', os.getenv('GOOGLE_CLOUD_PROJECT', '')) or '')
        self.vertex_location = str(config.get('vertex_location', os.getenv('GOOGLE_CLOUD_LOCATION', 'global')) or 'global')
        self.vertex_api_key = str(config.get('vertex_api_key', os.getenv('VERTEX_API_KEY', os.getenv('GOOGLE_API_KEY', ''))) or '')
        
        # Настройки изображений (по умолчанию WebP, поддерживается также JPEG)
        self.image_mime_type = config.get('image_mime_type', 'image/webp')
        self.image_max_size = config.get('image_max_size', 10 * 1024 * 1024)
        
        # LangChain клиент
        self.llm = None
        self.llm_with_tools = None
        self.llm_no_tools = None
        self.llm_classifier = None
        self._api_keys = [key for key in [self.api_key, self.fallback_api_key] if key]
        self._active_key_index = 0
        self._key_switch_lock = asyncio.Lock()
        self.is_available = (
            bool(ChatGoogleGenerativeAI) and bool(self.vertex_project) and bool(self.vertex_location)
            if self.use_vertex_ai
            else bool(ChatGoogleGenerativeAI) and bool(self._api_keys)
        )
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
            logger.info(f"   → mode: {'vertex' if self.use_vertex_ai else 'developer_api'}")
            logger.info(f"   → api_key present: {bool(self._api_keys)}")
            logger.info(f"   → vertex_project: {self.vertex_project if self.vertex_project else 'not_set'}")
            logger.info(f"   → vertex_location: {self.vertex_location if self.vertex_location else 'not_set'}")
            logger.info(f"   → model_name: {self.model_name}")
            
            if not self.is_available:
                logger.error("Missing API key or LangChain dependencies")
                return False
            
            # И production Vertex path, и developer path работают через LangChain adapters.
            logger.info(f"🔍 Создаем LLM клиент...")

            self._build_clients()

            logger.info("✅ LangChain клиент создан")

            # Startup выполняет только локальную инициализацию клиента.
            # Внешняя проверка API переносится на первый реальный запрос,
            # чтобы не валить весь gRPC bootstrap из-за временной/внешней ошибки LLM.
            self.is_initialized = True
            logger.info(f"✅ LangChain initialized (startup probe skipped): {self.model_name}")
            return True
                
        except Exception as e:
            logger.error(f"LangChain initialization failed: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _build_clients(self) -> None:
        llm_params: Dict[str, Any] = {
            "model": self.model_name,
            "temperature": self.temperature,
            "streaming": True,
            "max_output_tokens": self.max_tokens,
        }

        if not ChatGoogleGenerativeAI:
            raise RuntimeError("ChatGoogleGenerativeAI is unavailable")

        if self.use_vertex_ai:
            llm_params.update({
                "vertexai": True,
                "project": self.vertex_project,
                "location": self.vertex_location,
            })
            if self.vertex_api_key:
                llm_params["google_api_key"] = self.vertex_api_key
            self.llm_no_tools = ChatGoogleGenerativeAI(**llm_params)
            if self.tools and "google_search" in self.tools:
                self.llm_with_tools = self._bind_google_search_llm_or_none(self.llm_no_tools)
            else:
                self.llm_with_tools = None
        else:
            if not self._api_keys:
                raise RuntimeError("No Gemini API keys configured")
            llm_params["google_api_key"] = self._api_keys[self._active_key_index]
            self.llm_no_tools = ChatGoogleGenerativeAI(**llm_params)
            if self.tools and "google_search" in self.tools:
                self.llm_with_tools = self._bind_google_search_llm_or_none(self.llm_no_tools)
            else:
                self.llm_with_tools = None

        classifier_params = dict(llm_params)
        classifier_params.update(
            {
                "temperature": 0,
                "streaming": False,
                "max_output_tokens": 160,
                "response_mime_type": "application/json",
            }
        )
        self.llm_classifier = ChatGoogleGenerativeAI(**classifier_params)

        self.llm = self.llm_with_tools or self.llm_no_tools

    @staticmethod
    def _build_google_search_tool():
        """
        Use Gemini's native Google Search Retrieval tool instead of a synthetic
        function declaration. The synthetic {"google_search": {}} path can be
        converted into an invalid function declaration name in current LangChain/Gemini
        bindings, which breaks live search routing.
        """
        if GoogleGenerativeAITool is not None:
            return GoogleGenerativeAITool(google_search_retrieval={})
        return {"google_search_retrieval": {}}

    def _bind_google_search_llm_or_none(self, llm):
        """
        Current langchain_google_genai releases in this environment do not reliably
        support Gemini Google Search Retrieval through bind_tools():
        - native Tool objects fail at bind time
        - synthetic dicts degrade into invalid function declarations at request time

        Keep provider initialization healthy and fall back to the no-tools LLM until
        a dedicated native google.genai search path is introduced in this provider.
        """
        tool = self._build_google_search_tool()
        try:
            return llm.bind_tools([tool])
        except Exception as exc:
            logger.warning(
                "Google Search tool binding is unsupported in current LangChain/Gemini runtime; "
                "falling back to no-tools LLM: %s",
                exc,
            )
            return None

    @staticmethod
    def _extract_runtime_memory_context(user_input: str) -> tuple[str, str]:
        """
        Split enriched text into runtime memory context and pure user input.
        Expected input format from workflow:
            MEMORY_CONTEXT:
            ...

            USER_INPUT:
            ...
        """
        raw_text = str(user_input or "")
        memory_marker = "MEMORY_CONTEXT:"
        user_marker = "USER_INPUT:"

        memory_pos = raw_text.find(memory_marker)
        user_pos = raw_text.find(user_marker)
        if memory_pos == -1 or user_pos == -1 or memory_pos > user_pos:
            return "", raw_text

        after_memory = raw_text[memory_pos + len(memory_marker):]
        memory_block, sep, user_block = after_memory.partition(user_marker)
        if not sep:
            return "", raw_text

        runtime_memory_context = memory_block.strip()
        user_input = user_block.strip() or raw_text
        return runtime_memory_context, user_input

    @staticmethod
    def _is_key_error(exc: Exception) -> bool:
        error_text = str(exc).upper()
        return (
            "API_KEY_INVALID" in error_text
            or "API KEY EXPIRED" in error_text
            or "INVALID API KEY" in error_text
            or "PERMISSION_DENIED" in error_text
        )

    async def _switch_to_fallback_key_if_needed(self, exc: Exception) -> bool:
        if self.use_vertex_ai:
            return False
        if not self._is_key_error(exc):
            return False

        async with self._key_switch_lock:
            if self._active_key_index >= len(self._api_keys) - 1:
                return False

            self._active_key_index += 1
            self._build_clients()
            logger.warning(
                "LangChain provider switched to fallback API key",
                extra={
                    'scope': 'module',
                    'decision': 'fallback_key_switch',
                    'ctx': {'active_key_index': self._active_key_index}
                }
            )
            return True
    
    def _resolve_runtime_system_prompt(
        self,
        *,
        route: Optional[str],
        system_prompt_override: Optional[str],
    ) -> str:
        if system_prompt_override is not None:
            return system_prompt_override

        route = str(route or "none").strip().lower() or "none"
        config = get_config()
        return build_route_system_prompt(
            route=route,
            system_control_available=True,
            describe_available=True,
            messages_available=bool(config.features.messages_enabled),
            whatsapp_available=bool(config.whatsapp.enabled),
            browser_available=bool(config.browser_use.enabled),
            payment_available=bool(config.subscription.is_active()),
            google_search_available=bool(config.features.google_search_enabled),
            capability_available=True,
            strict_single_route_mode=True,
        )

    def _build_messages(
        self,
        *,
        user_content: Union[str, list],
        system_prompt: str,
        use_search: Optional[bool],
    ) -> list:
        messages = []
        if system_prompt and SystemMessage:
            messages.append(SystemMessage(content=system_prompt))
        if use_search is True and SystemMessage and not self.use_vertex_ai:
            messages.append(SystemMessage(content="You MUST use google_search for this request and base the answer on search results."))
        if HumanMessage:
            messages.append(HumanMessage(content=user_content))
        return messages

    async def process(
        self,
        user_input: str,
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        use_google_search: Optional[bool] = None,
        route: Optional[str] = None,
        system_prompt_override: Optional[str] = None,
        hardware_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        _retry_with_fallback_key: bool = True
    ) -> AsyncGenerator[str, None]:
        """
        ЭТАП 1: Обработка текста через LangChain
        Возвращаем текст напрямую
        
        Args:
            user_input: Текстовый запрос
            
        Yields:
            Части текстового ответа
        """
        try:
            if use_google_search is not None:
                use_search = use_google_search
            llm = self._select_llm(use_search)
            if not self.is_initialized:
                raise Exception("LangChain not initialized")
            if not self.use_vertex_ai and not llm:
                raise Exception("LangChain not initialized")

            clean_user_input = user_input
            if runtime_memory_context is None:
                # LEGACY_EXPIRY: remove after all callers pass runtime_memory_context explicitly.
                # Backward compatibility for legacy combined payload path.
                runtime_memory_context, clean_user_input = self._extract_runtime_memory_context(user_input)
                if runtime_memory_context:
                    logger.warning(
                        "LEGACY_RUNTIME_MEMORY_PATH used in process(); prefer payload.runtime_memory_context"
                    )

            system_prompt = self._resolve_runtime_system_prompt(
                route=route,
                system_prompt_override=system_prompt_override,
            )
            if runtime_memory_context:
                if system_prompt:
                    system_prompt = (
                        f"{system_prompt}\n\n"
                        f"[Runtime Memory Context]\n{runtime_memory_context}"
                    )
                else:
                    system_prompt = f"[Runtime Memory Context]\n{runtime_memory_context}"
            content = clean_user_input
            if session_id:
                 content = f"{clean_user_input}\n\n[System Context: session_id={session_id}]"
            messages = self._build_messages(
                user_content=content,
                system_prompt=system_prompt,
                use_search=use_search,
            )

            accumulated_usage = None
            async for chunk in llm.astream(messages):
                if hasattr(chunk, 'usage_metadata') and chunk.usage_metadata:
                    accumulated_usage = chunk.usage_metadata
                text = extract_text_from_chunk(chunk)
                if text:
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
                    target_id = hardware_id or 'unknown'
                    
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
            if _retry_with_fallback_key and await self._switch_to_fallback_key_if_needed(e):
                async for chunk in self.process(
                    user_input=user_input,
                    session_id=session_id,
                    use_search=use_search,
                    use_google_search=use_google_search,
                    route=route,
                    system_prompt_override=system_prompt_override,
                    hardware_id=hardware_id,
                    runtime_memory_context=runtime_memory_context,
                    _retry_with_fallback_key=False,
                ):
                    yield chunk
                return
            logger.error(f"LangChain text processing error: {e}")
            raise e
    
    async def process_with_image(
        self,
        user_input: str,
        image_data: Union[str, bytes],
        session_id: Optional[str] = None,
        use_search: Optional[bool] = None,
        use_google_search: Optional[bool] = None,
        route: Optional[str] = None,
        system_prompt_override: Optional[str] = None,
        hardware_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        _retry_with_fallback_key: bool = True
    ) -> AsyncGenerator[str, None]:
        """
        ЭТАП 2: Обработка текста с WebP изображением
        
        Args:
            user_input: Текстовый запрос
            image_data: Base64 строка изображения в формате WebP (или bytes для обратной совместимости)
            
        Yields:
            Части текстового ответа
        """
        try:
            if use_google_search is not None:
                use_search = use_google_search
            llm = self._select_llm(use_search)
            if not self.is_initialized:
                raise Exception("LangChain not initialized")
            if not self.use_vertex_ai and not llm:
                raise Exception("LangChain not initialized")

            clean_user_input = user_input
            if runtime_memory_context is None:
                # LEGACY_EXPIRY: remove after all callers pass runtime_memory_context explicitly.
                # Backward compatibility for legacy combined payload path.
                runtime_memory_context, clean_user_input = self._extract_runtime_memory_context(user_input)
                if runtime_memory_context:
                    logger.warning(
                        "LEGACY_RUNTIME_MEMORY_PATH used in process_with_image(); prefer payload.runtime_memory_context"
                    )
            
            # Проверяем, что image_data не None
            if image_data is None:
                logger.debug("No image data provided, processing as text only")
                async for chunk in self.process(
                    user_input=clean_user_input,
                    session_id=session_id,
                    use_search=use_search,
                    use_google_search=use_google_search,
                    route=route,
                    system_prompt_override=system_prompt_override,
                    hardware_id=hardware_id,
                    runtime_memory_context=runtime_memory_context,
                    _retry_with_fallback_key=_retry_with_fallback_key,
                ):
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
                    "text": (
                        f"{clean_user_input}\n\n[System Context: session_id={session_id}]"
                        if session_id
                        else clean_user_input
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{self.image_mime_type};base64,{image_b64}"
                    }
                }
            ]
            
            system_prompt = self._resolve_runtime_system_prompt(
                route=route,
                system_prompt_override=system_prompt_override,
            )
            if runtime_memory_context:
                if system_prompt:
                    system_prompt = (
                        f"{system_prompt}\n\n"
                        f"[Runtime Memory Context]\n{runtime_memory_context}"
                    )
                else:
                    system_prompt = f"[Runtime Memory Context]\n{runtime_memory_context}"
            messages = self._build_messages(
                user_content=content,
                system_prompt=system_prompt,
                use_search=use_search,
            )

            accumulated_usage = None
            async for chunk in llm.astream(messages):
                if hasattr(chunk, 'usage_metadata') and chunk.usage_metadata:
                    accumulated_usage = chunk.usage_metadata
                text = extract_text_from_chunk(chunk)
                if text:
                    yield text
            
            # Записываем использование токенов
            if self.token_usage_tracker and accumulated_usage:
                try:
                    target_id = hardware_id or 'unknown'
                    
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
            if _retry_with_fallback_key and await self._switch_to_fallback_key_if_needed(e):
                async for chunk in self.process_with_image(
                    user_input=user_input,
                    image_data=image_data,
                    session_id=session_id,
                    use_search=use_search,
                    use_google_search=use_google_search,
                    route=route,
                    system_prompt_override=system_prompt_override,
                    hardware_id=hardware_id,
                    runtime_memory_context=runtime_memory_context,
                    _retry_with_fallback_key=False,
                ):
                    yield chunk
                return
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
            self.llm_classifier = None
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
            "use_vertex_ai": self.use_vertex_ai,
            "vertex_project": self.vertex_project,
            "vertex_location": self.vertex_location,
            "vertex_api_key_set": bool(self.vertex_api_key),
            "configured_api_keys": len(self._api_keys),
            "active_api_key_index": self._active_key_index,
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
        # Default-safe policy: internet tooling is enabled only when explicitly requested.
        if use_search is False or use_search is None:
            return self.llm_no_tools
        return self.llm

    @staticmethod
    def _build_classifier_prompt_with_context(
        base_prompt: str,
        classifier_context: Optional[Dict[str, str]] = None,
    ) -> str:
        """
        Inject classification context directly into classifier system prompt.
        This keeps context tied to classification instructions, as required.
        """
        if not classifier_context:
            return base_prompt

        parts = [base_prompt.rstrip(), "", "[Classification Context For This Request]"]
        ordered_keys = ("current_goal", "short_term_memory")
        for key in ordered_keys:
            value = str(classifier_context.get(key, "")).strip()
            if value:
                parts.append(f"- {key}:")
                parts.append("```text")
                parts.append(value)
                parts.append("```")
        if len(parts) == 3:
            return base_prompt
        if str(classifier_context.get("short_term_memory", "")).strip():
            parts.append(
                "Short-term read order contract: top-to-bottom is newest-to-oldest; CURRENT_TURN is newest; use TIME_UTC for temporal grounding."
            )
        parts.append("")
        parts.append(
            "Use current_goal first when it exists. Use short_term_memory second to disambiguate recent dialogue."
        )
        parts.append(
            "Resolve ambiguous input from CURRENT_TURN first, then PREVIOUS_TURN_n by recency."
        )
        return "\n".join(parts)

    async def classify_intent_route(
        self,
        user_input: str,
        classifier_context: Optional[Dict[str, str]] = None,
    ) -> str:
        decision = await self.classify_intent_decision(
            user_input=user_input,
            classifier_context=classifier_context,
        )
        return str(decision.get("category", "none")).strip().lower() or "none"

    async def classify_intent_decision(
        self,
        user_input: str,
        classifier_context: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        raw_input = str(user_input or "").strip()
        if not raw_input:
            return {"category": "none"}
        try:
            return await asyncio.to_thread(
                self._classify_intent_decision_sync,
                raw_input,
                classifier_context or {},
            )
        except Exception as exc:
            logger.warning("Intent classifier decision failed, defaulting to none: %s", exc)
            return {"category": "none"}

    def _classify_intent_decision_sync(
        self,
        user_input: str,
        classifier_context: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        if not self.is_available:
            return {"category": "none"}

        allowed = {
            "none",
            "whatsapp",
            "messages",
            "browser",
            "google_search",
            "describe",
            "system_control",
            "payment",
            "capability",
        }
        classifier_prompt = self._build_classifier_prompt_with_context(
            build_intent_classifier_prompt(),
            classifier_context=classifier_context,
        )

        if not self.llm_classifier:
            self._build_clients()

        messages = self._build_messages(
            user_content=json.dumps({"user_input": user_input}, ensure_ascii=False),
            system_prompt=classifier_prompt,
            use_search=False,
        )
        response = self.llm_classifier.invoke(messages)
        raw = extract_text_from_chunk(response).strip()
        try:
            parsed = json.loads(raw)
            category = str(parsed.get("category", "")).strip().lower()
            if category in allowed:
                return {"category": category}
        except Exception:
            pass
        return {"category": "none"}
