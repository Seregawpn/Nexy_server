"""
Основной TextProcessor - координатор модуля обработки текста

Использует LangChain провайдер для обработки текста:
- Стриминговая обработка текста (текст → поток текста)
- Стриминговая обработка с изображениями (текст + изображение WebP/JPEG → поток текста)  
- Google Search (текст + изображение + поиск → поток текста)
"""

import logging
import re
from typing import Dict, Any, Optional, Union, AsyncGenerator, Set, Tuple
from modules.text_processing.config import TextProcessingConfig
from modules.text_processing.providers.langchain_gemini_provider import LangChainGeminiProvider
from config.unified_config import get_config
from config.prompts import build_system_prompt
from config.intent_routing_policy import (
    NEGATION_TOKENS,
    CATEGORY_RULES,
)
from config.intent_routes import ALLOWED_PRIMARY_ROUTES

logger = logging.getLogger(__name__)

TOKEN_NORMALIZATION_MAP = {
    "msg": "message",
    "msgs": "messages",
    "mesage": "message",
    "mesg": "message",
    "snd": "send",
    "smd": "send",
}

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
    def _extract_intent_text(text: str) -> str:
        """
        Extract user-intent portion from enriched workflow prompt.

        Workflow may pass:
          MEMORY_CONTEXT: ...
          USER_INPUT:
          <actual user text>
        Intent routing must rely on USER_INPUT only to avoid false-positive sections.
        """
        if not isinstance(text, str):
            return ""
        marker = "USER_INPUT:"
        if marker not in text:
            return text
        _, _, tail = text.partition(marker)
        extracted = tail.strip()
        return extracted or text

    @staticmethod
    def _replace_user_input_text(original_text: str, normalized_intent_text: str) -> str:
        if not isinstance(original_text, str):
            return normalized_intent_text
        marker = "USER_INPUT:"
        if marker not in original_text:
            return normalized_intent_text
        head, _, _ = original_text.partition(marker)
        return f"{head}{marker}\n{normalized_intent_text.strip()}".strip()

    @staticmethod
    def _tokenize(text: str) -> Set[str]:
        lowered = str(text or "").lower()
        tokens = re.findall(r"[a-z0-9']+", lowered)
        normalized = [TOKEN_NORMALIZATION_MAP.get(tok, tok) for tok in tokens]
        return set(normalized)

    @staticmethod
    def _has_explicit_whatsapp_marker(tokens: Set[str], intent_text: str) -> bool:
        if "whatsapp" in tokens:
            return True
        # Treat bare "WA" as WhatsApp only for messaging-like intents.
        if "wa" in tokens and bool(tokens & {"send", "message", "messages", "reply", "read", "check"}):
            return True
        lowered = str(intent_text or "").lower()
        return bool(re.search(r"\bwhat'?s?app\b", lowered))

    @staticmethod
    def _is_generic_message_intent(tokens: Set[str]) -> bool:
        action_tokens = {"send", "reply", "read", "check", "text", "message", "messages"}
        return bool(tokens & action_tokens) and bool(tokens & {"message", "messages", "text", "reply"})

    @staticmethod
    def _extract_memory_section(runtime_memory_context: str, header: str) -> str:
        """
        Extract section body from structured runtime memory context.
        Expected format:
          <Header>:
          <body>
          <blank line>
          <Next Header>:
        """
        if not runtime_memory_context:
            return ""
        text = str(runtime_memory_context)
        start_marker = f"{header}:"
        start = text.find(start_marker)
        if start == -1:
            return ""
        start = start + len(start_marker)
        tail = text[start:]
        # Section blocks are separated by blank lines in current formatter.
        section = tail.split("\n\n", 1)[0].strip()
        return section

    def _resolve_tier_a_route(self, tokens: Set[str]) -> Tuple[str, str]:
        if not tokens:
            return "none", "no_match"

        # Negation nearby is treated as ambiguous for safe fallback.
        if tokens & NEGATION_TOKENS:
            return "none", "low_confidence"

        if "whatsapp" in tokens and ("imessage" in tokens or "messages" in tokens):
            return "none", "conflict"

        # Global keyword-conflict gate:
        # if the same utterance matches keys from more than one category,
        # delegate to LLM classifier instead of finalizing Tier-A locally.
        key_hit_categories = []
        for category, rule in CATEGORY_RULES.items():
            domains = set(rule["domains"])
            actions = set(rule["actions"])
            excludes = set(rule["excludes"])
            if tokens & excludes:
                continue
            if tokens & (domains | actions):
                key_hit_categories.append(category)
        if len(key_hit_categories) > 1:
            return "none", "conflict"

        candidates = []
        for category, rule in CATEGORY_RULES.items():
            domains = rule["domains"]
            actions = rule["actions"]
            requires_action = bool(rule["requires_action"])
            excludes = rule["excludes"]
            if tokens & excludes:
                continue
            if not (tokens & domains):
                continue
            if requires_action and not (tokens & actions):
                continue
            candidates.append(category)

        if len(candidates) == 1:
            return candidates[0], "tier_a_match"
        if len(candidates) > 1:
            return "none", "conflict"
        return "none", "no_match"

    async def _build_classifier_context(
        self,
        session_id: Optional[str],
        runtime_memory_context: Optional[str],
    ) -> Dict[str, str]:
        context: Dict[str, str] = {}
        if runtime_memory_context:
            short_term = self._extract_memory_section(runtime_memory_context, "Short-term memory")
            if short_term:
                # Classifier contract: only short-term memory, no truncation.
                context["short_term_memory"] = short_term
        return context

    async def _resolve_route_and_reason(
        self,
        intent_text: str,
        session_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
    ) -> Tuple[str, str]:
        route = await self._classify_route_tier_c(intent_text, session_id, runtime_memory_context)
        return route, "classifier_only"

    async def _classify_route_tier_c(
        self,
        intent_text: str,
        session_id: Optional[str],
        runtime_memory_context: Optional[str],
    ) -> str:
        classifier_context = await self._build_classifier_context(session_id, runtime_memory_context)
        try:
            decision = await self.live_provider.classify_intent_decision(
                input_data=intent_text,
                classifier_context=classifier_context,
            )
        except Exception as exc:
            logger.warning("TextProcessor: classifier failed, fallback to none: %s", exc)
            return "none"

        route = str((decision or {}).get("category", "none")).strip().lower() or "none"
        if route not in ALLOWED_PRIMARY_ROUTES:
            return "none"
        return route

    async def prepare_generation_request(
        self,
        text: str,
        session_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        has_image: bool = False,
        use_google_search: Optional[bool] = None,
    ) -> Dict[str, Any]:
        prompt, sections, normalized_text, routing_system_context = await self._build_prompt_for_text(
            text,
            session_id=session_id,
            runtime_memory_context=runtime_memory_context,
            has_image=has_image,
        )
        resolved_use_google_search = use_google_search
        if resolved_use_google_search is None:
            config = get_config()
            resolved_use_google_search = bool(
                config.features.google_search_enabled and sections.get("primary_route") == "google_search"
            )
        return {
            "system_prompt_override": prompt,
            "sections": sections,
            "normalized_text": normalized_text,
            "routing_system_context": routing_system_context,
            "primary_route": str(sections.get("primary_route", "none")),
            "use_google_search": bool(resolved_use_google_search),
        }

    async def _build_prompt_for_text(
        self,
        text: str,
        session_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        has_image: bool = False,
    ) -> tuple[str, Dict[str, bool], str, str]:
        config = get_config()
        intent_text = TextProcessor._extract_intent_text(text)
        if has_image and not intent_text.strip():
            primary_route, fallback_reason = "describe", "image_forced_describe"
        else:
            primary_route, fallback_reason = await self._resolve_route_and_reason(
                intent_text=intent_text,
                session_id=session_id,
                runtime_memory_context=runtime_memory_context,
            )
        route = str(primary_route or "none").strip().lower() or "none"
        if route not in ALLOWED_PRIMARY_ROUTES:
            route = "none"
        sections = {
            "system_control": route == "system_control",
            "messages": route == "messages",
            "whatsapp": route == "whatsapp",
            "browser": route == "browser",
            "payment": route == "payment",
            "google_search": route == "google_search",
            "describe": route == "describe",
            "capability": route == "capability",
            "primary_route": route,
            "is_follow_up": False,
        }
        prompt = build_system_prompt(
            primary_route=primary_route,
            system_control_enabled=True,
            describe_enabled=True,
            messages_enabled=bool(config.features.messages_enabled),
            whatsapp_enabled=bool(config.whatsapp.enabled),
            browser_enabled=bool(config.browser_use.enabled),
            payment_enabled=bool(config.subscription.is_active()),
            google_search_enabled=bool(config.features.google_search_enabled),
            capability_enabled=True,
            strict_single_route_mode=True,
        )
        normalized_text = self._replace_user_input_text(text, intent_text)
        logger.info(
            "TextProcessor: route=%s fallback_reason=%s intent_len=%s",
            sections.get("primary_route", "none"),
            fallback_reason,
            len(intent_text),
        )
        routing_system_context = (
            "[Routing System Data]\n"
            f"- primary_route: {sections.get('primary_route', 'none')}\n"
            f"- has_image: {str(bool(has_image)).lower()}"
        )
        return prompt, sections, normalized_text, routing_system_context
    
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
        use_google_search: Optional[bool] = None,
        hardware_id: Optional[str] = None,
        runtime_memory_context: Optional[str] = None,
        prepared_request: Optional[Dict[str, Any]] = None,
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
            sections: Optional[Dict[str, bool]] = None
            routing_system_context = None
            llm_input_text = text
            if text:
                prepared = prepared_request or await self.prepare_generation_request(
                    text,
                    session_id=session_id,
                    runtime_memory_context=runtime_memory_context,
                    has_image=bool(image_data),
                    use_google_search=use_google_search,
                )
                system_prompt_override = str(prepared["system_prompt_override"])
                sections = dict(prepared["sections"])
                llm_input_text = str(prepared["normalized_text"])
                routing_system_context = str(prepared["routing_system_context"])
                use_google_search = bool(prepared["use_google_search"])
                logger.info(
                    "TextProcessor: prompt_sections=%s use_google_search=%s",
                    sections,
                    use_google_search
                )
            use_image_for_generation = bool(image_data)
            if image_data and sections is not None:
                # Image is passed to LLM only for describe route.
                use_image_for_generation = bool(sections.get("describe", False))
            logger.info(
                "TextProcessor: use_image_for_generation=%s has_image=%s primary_route=%s",
                use_image_for_generation,
                bool(image_data),
                str((sections or {}).get("primary_route", "none")),
            )
            
            # Вызываем правильный метод в зависимости от наличия изображения
            if use_image_for_generation:
                async for chunk in self.live_provider.process_with_image(
                    llm_input_text,
                    image_data,
                    session_id=session_id,
                    use_google_search=use_google_search,
                    system_prompt_override=system_prompt_override,
                    hardware_id=hardware_id,
                    runtime_memory_context=runtime_memory_context,
                ):
                    yield chunk
            else:
                async for chunk in self.live_provider.process(
                    llm_input_text,
                    session_id=session_id,
                    use_google_search=use_google_search,
                    system_prompt_override=system_prompt_override,
                    hardware_id=hardware_id,
                    runtime_memory_context=runtime_memory_context,
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
