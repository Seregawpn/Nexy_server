"""
Memory Analyzer - анализ диалогов для извлечения памяти

Использует Gemini API для анализа разговоров и извлечения:
- Краткосрочной памяти (контекст текущего разговора)
- Долгосрочной памяти (важная информация о пользователе)

Этот класс заменяет отсутствующий memory_analyzer.py
"""

import asyncio
import logging
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Tuple, Optional, Any

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    ChatGoogleGenerativeAI = None

try:
    from langchain_core.messages import HumanMessage, SystemMessage
except ImportError:
    HumanMessage = None
    SystemMessage = None

LANGCHAIN_MEMORY_AVAILABLE = bool(ChatGoogleGenerativeAI and HumanMessage and SystemMessage)

logger = logging.getLogger(__name__)

class MemoryAnalyzer:
    """
    Анализатор диалогов для извлечения памяти пользователей.
    
    Использует Gemini API для анализа разговоров и извлечения важной информации
    для краткосрочной и долгосрочной памяти.
    """
    _EMPTY_VALUES = {"", "empty", "none", "no information", "n/a", "null"}
    _SECRET_PATTERN = re.compile(
        r"\b(password\w*|парол\w*|token\w*|токен\w*|api[_ -]?key|ключ\w*)\b",
        flags=re.IGNORECASE,
    )
    _INFERRED_FACT_PATTERN = re.compile(
        r"\b(implied|inferred|likely|maybe|seems|probably|possible(?:ly)?)\b",
        flags=re.IGNORECASE,
    )
    _ONE_OFF_REQUEST_PATTERN = re.compile(
        r"\b(asked\s+(?:me\s+)?to|requested|can you|could you|find\s+(?:me\s+)?)\b",
        flags=re.IGNORECASE,
    )
    _IDENTITY_FACT_PATTERN = re.compile(
        r"\b(my name is|name is|меня зовут|мо[её] имя|i am|i'm)\b",
        flags=re.IGNORECASE,
    )
    _NON_PROFILE_LONG_TERM_PATTERN = re.compile(
        r"\b(i\s+do\s+not\s+have\s+memory|i\s+don't\s+have\s+memory|"
        r"no\s+access\s+to\s+(your|past)\s+.*(memory|conversation)|"
        r"cannot\s+remember\s+past\s+conversations|"
        r"as\s+an?\s+ai\s+assistant)\b",
        flags=re.IGNORECASE,
    )
    _TRANSPORT_PAYLOAD_PATTERN = re.compile(
        r"(\{[\s\S]*?(?:\"command\"|\"args\"|\"tool\")[\s\S]*?\}"
        r"|(?:^|\b)(?:command|args|tool)\s*[:=]"
        r"|function\s*="
        r"|bundle_id\s*="
        r"|action_id\s*=)"
        ,
        flags=re.IGNORECASE,
    )
    _SHORT_TERM_VALUE_PATTERN = re.compile(
        r"^\[\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+UTC\]\s+USER:\s+.+\s+\|\s+ASSISTANT:\s+.+$",
        flags=re.IGNORECASE,
    )
    _MEDIUM_TERM_ENTRY_PATTERN = re.compile(
        r"^\[\d{4}-\d{2}-\d{2}\]\s+.+$",
        flags=re.IGNORECASE,
    )
    
    def __init__(
        self,
        gemini_api_key: str,
        token_tracker: Optional[Any] = None,
        hardware_id: Optional[str] = None,
        model_name: str = "",
        temperature: float = 0.3,
        analysis_prompt_template: str = "",
        use_vertex_ai: bool = False,
        vertex_project: str = "",
        vertex_location: str = "global",
        vertex_api_key: str = "",
    ):
        """
        Инициализация MemoryAnalyzer.
        
        Args:
            gemini_api_key: API ключ для Gemini
            token_tracker: Сервис для трекинга токенов (опционально)
            hardware_id: ID устройства для привязки токенов (опционально)
        """
        if not LANGCHAIN_MEMORY_AVAILABLE:
            raise ImportError("langchain_google_genai or langchain_core not available")

        self.api_key = gemini_api_key
        self.token_tracker = token_tracker
        self.hardware_id = hardware_id
        self.use_vertex_ai = bool(use_vertex_ai)
        self.vertex_project = str(vertex_project or "")
        self.vertex_location = str(vertex_location or "global")
        self.vertex_api_key = str(vertex_api_key or "")
        
        # Настройки модели
        self.model_name = model_name or os.getenv("GEMINI_PRIMARY_MODEL", "gemini-flash-lite-latest")
        self.temperature = temperature
        
        # Каноничный промпт приходит только из MemoryConfig (single source of truth).
        if not analysis_prompt_template.strip():
            raise ValueError("analysis_prompt_template is required and must come from MemoryConfig")
        self.analysis_prompt_template = analysis_prompt_template
        self._llm = self._build_client()
        
        logger.info(
            "✅ MemoryAnalyzer initialized with shared Gemini provider (mode=%s)",
            "vertex" if self.use_vertex_ai else "developer_api",
        )

    def _build_client(self):
        if not ChatGoogleGenerativeAI:
            raise ImportError("ChatGoogleGenerativeAI unavailable")

        llm_params = {
            "model": self.model_name,
            "temperature": self.temperature,
            "streaming": False,
            "max_output_tokens": 1024,
        }
        if self.use_vertex_ai:
            llm_params.update(
                {
                    "vertexai": True,
                    "project": self.vertex_project,
                    "location": self.vertex_location,
                }
            )
            if self.vertex_api_key:
                llm_params["google_api_key"] = self.vertex_api_key
        else:
            if not self.api_key:
                raise ValueError("gemini_api_key is required when Vertex AI is disabled")
            llm_params["google_api_key"] = self.api_key

        return ChatGoogleGenerativeAI(**llm_params)
    
    async def analyze_conversation(
        self,
        prompt: str,
        response: str,
        hardware_id: Optional[str] = None,
        existing_current_goal: str = "",
        existing_short_memory: str = "",
        existing_medium_memory: str = "",
        existing_long_memory: str = "",
        analysis_prompt_template_override: Optional[str] = None,
    ) -> Tuple[str, str, str, str, str]:
        """
        Анализирует диалог для извлечения памяти.
        
        Args:
            prompt: Запрос пользователя
            response: Ответ ассистента
            hardware_id: ID устройства для трекинга токенов (опционально)
            existing_short_memory: Текущая short-term память пользователя
            existing_medium_memory: Текущая medium-term память пользователя
            existing_long_memory: Текущая long-term память пользователя
            
        Returns:
            Кортеж (short_memory, medium_memory, long_memory, current_goal, goal_state)
        """
        try:
            # Используем переданный hardware_id или сохраненный в self
            target_hardware_id = hardware_id or self.hardware_id
            # Формируем промпт для анализа
            current_date_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            prompt_template = analysis_prompt_template_override or self.analysis_prompt_template
            analysis_prompt = self._safe_format_analysis_prompt(
                prompt_template,
                prompt=prompt,
                response=response,
                current_date_utc=current_date_utc,
                existing_current_goal=existing_current_goal or "EMPTY",
                existing_short_memory=existing_short_memory or "EMPTY",
                existing_medium_memory=existing_medium_memory or "EMPTY",
                existing_long_memory=existing_long_memory or "EMPTY",
            )
            
            # Анализируем диалог
            logger.debug(f"🧠 Analyzing conversation for memory extraction...")

            response_obj = await self._llm.ainvoke(
                [
                    SystemMessage(content="You are a strict memory analyzer. Follow the required output format exactly."),
                    HumanMessage(content=analysis_prompt),
                ]
            )

            if not response_obj:
                logger.warning("⚠️ Empty response from Gemini for memory analysis")
                return "", "", "", "", "empty"
                
            # Записываем использование токенов
            usage_metadata = getattr(response_obj, 'usage_metadata', None)
            if self.token_tracker and target_hardware_id and usage_metadata:
                try:
                    input_tokens = getattr(usage_metadata, 'input_tokens', None)
                    if input_tokens is None:
                        input_tokens = getattr(usage_metadata, 'prompt_token_count', 0)
                    output_tokens = getattr(usage_metadata, 'output_tokens', None)
                    if output_tokens is None:
                        output_tokens = getattr(usage_metadata, 'candidates_token_count', 0)
                    
                    self.token_tracker.record_usage(
                        hardware_id=target_hardware_id,
                        source='memory_analyzer',
                        input_tokens=int(input_tokens or 0),
                        output_tokens=int(output_tokens or 0),
                        model_name=self.model_name
                    )
                except Exception as e:
                    logger.warning(f"Failed to record memory analysis tokens: {e}")
            
            response_text = getattr(response_obj, 'content', '') or ''
            if isinstance(response_text, list):
                response_text = ''.join(str(item) for item in response_text)
            response_text = str(response_text).strip()
            if not response_text:
                logger.warning("⚠️ Empty text in response from Gemini")
                return "", "", "", "", "empty"
            
            # Парсим результат
            short_memory, medium_memory, long_memory, current_goal, goal_state = self._parse_analysis_response(response_text)
            
            logger.info(
                "🧠 Memory analysis completed: short-term (%s chars), medium-term (%s chars), long-term (%s chars)",
                len(short_memory),
                len(medium_memory),
                len(long_memory),
            )
            
            return short_memory, medium_memory, long_memory, current_goal, goal_state
            
        except Exception as e:
            logger.error(f"❌ Error analyzing conversation for memory: {e}")
            return "", "", "", "", "empty"

    @staticmethod
    def _safe_format_analysis_prompt(prompt_template: str, **values: str) -> str:
        template = str(prompt_template or "")
        sentinels: dict[str, str] = {}
        for key in values.keys():
            placeholder = "{" + key + "}"
            sentinel = f"__MEMORY_PROMPT_SLOT_{uuid.uuid4().hex}__"
            sentinels[sentinel] = placeholder
            template = template.replace(placeholder, sentinel)

        template = template.replace("{", "{{").replace("}", "}}")

        for sentinel, placeholder in sentinels.items():
            template = template.replace(sentinel, placeholder)

        return template.format(**values)
    
    def _parse_analysis_response(self, response_text: str) -> Tuple[str, str, str, str, str]:
        """
        Парсит ответ от Gemini для извлечения краткосрочной и долгосрочной памяти.
        
        Args:
            response_text: Текст ответа от Gemini
            
        Returns:
            Кортеж (short_memory, medium_memory, long_memory, current_goal, goal_state)
        """
        try:
            normalized_text = self._normalize_response_text(response_text)
            parsed_sections = self._parse_strict_response(normalized_text)
            if not parsed_sections:
                repaired_text = self._repair_to_strict_text(normalized_text)
                if repaired_text:
                    parsed_sections = self._parse_strict_response(repaired_text)
                    if parsed_sections:
                        logger.info("MemoryAnalyzer response repaired to strict canonical format")
                if not parsed_sections:
                    reason = self._detect_invalid_reason(normalized_text)
                    logger.warning(
                        "MemoryAnalyzer response violates strict format: reason=%s. "
                        "Expected exact canonical block with CURRENT_GOAL, SHORT_TERM, MEDIUM_TERM, LONG_TERM and no extra text.",
                        reason,
                    )
                    return "", "", "", "", "empty"

            goal_state, current_goal, short_memory, medium_memory, long_memory = parsed_sections

            current_goal = self._sanitize_memory_value(current_goal)
            goal_state = self._normalize_goal_state_value(goal_state)
            short_memory = self._sanitize_memory_value(short_memory)
            short_memory = self._dedupe_memory_facts(short_memory)
            medium_memory = self._sanitize_memory_value(medium_memory)
            medium_memory = self._dedupe_memory_facts(medium_memory)
            long_memory = self._sanitize_memory_value(long_memory)
            long_memory = self._dedupe_memory_facts(long_memory)
            long_memory = self._filter_long_term_facts(long_memory)

            current_goal = self._normalize_current_goal_value(current_goal)

            if not self._validate_short_term_value(short_memory):
                logger.warning("MemoryAnalyzer short-term value violates canonical structure")
                return "", "", "", "", "empty"
            if not self._validate_medium_term_value(medium_memory):
                logger.warning("MemoryAnalyzer medium-term value violates canonical structure")
                return "", "", "", "", "empty"
            if not self._validate_long_term_value(long_memory):
                logger.warning("MemoryAnalyzer long-term value violates canonical structure")
                return "", "", "", "", "empty"

            if self._SECRET_PATTERN.search(short_memory):
                short_memory = "[1970-01-01 00:00:00 UTC] USER: sensitive credentials were mentioned | ASSISTANT: assistant handled credentials context"
            if self._SECRET_PATTERN.search(medium_memory):
                medium_memory = "Prior conversation mentioned credentials context"
            if self._SECRET_PATTERN.search(long_memory):
                long_memory = "User has credentials for a service"
            
            logger.debug(
                "🧠 Parsed memory - Short: '%s...', Medium: '%s...', Long: '%s...'",
                short_memory[:100],
                medium_memory[:100],
                long_memory[:100],
            )
            
            return short_memory, medium_memory, long_memory, current_goal, goal_state
            
        except Exception as e:
            logger.error(f"❌ Error parsing memory analysis response: {e}")
            return "", "", "", "", "empty"

    @staticmethod
    def _parse_strict_response(text: str) -> Optional[Tuple[str, str, str, str, str]]:
        if not text:
            return None
        label_pattern = re.compile(
            r"^\s*(GOAL_STATE|CURRENT_GOAL|SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:\s*",
            flags=re.IGNORECASE | re.MULTILINE,
        )
        matches = list(label_pattern.finditer(text))
        labels = [match.group(1).upper() for match in matches]
        if labels != ["GOAL_STATE", "CURRENT_GOAL", "SHORT_TERM", "MEDIUM_TERM", "LONG_TERM"]:
            return None

        sections: list[str] = []
        for index, match in enumerate(matches):
            start = match.end()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            sections.append(text[start:end].strip())

        if len(sections) != 5:
            return None
        return sections[0], sections[1], sections[2], sections[3], sections[4]

    @staticmethod
    def _detect_invalid_reason(text: str) -> str:
        candidate = (text or "").strip()
        if not candidate:
            return "empty_response"
        if re.match(r"^\s*\{[\s\S]*\}\s*$", candidate):
            return "json_format"
        if re.search(r"<memory>|<short>|<medium>|<long>", candidate, flags=re.IGNORECASE):
            return "xml_format"
        labels = re.findall(
            r"^\s*(GOAL_STATE|CURRENT_GOAL|SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        if not labels:
            return "missing_required_labels"
        normalized = [label.upper() for label in labels]
        if any(normalized.count(label) > 1 for label in ("GOAL_STATE", "CURRENT_GOAL", "SHORT_TERM", "MEDIUM_TERM", "LONG_TERM")):
            return "duplicate_labels"
        if normalized != ["GOAL_STATE", "CURRENT_GOAL", "SHORT_TERM", "MEDIUM_TERM", "LONG_TERM"]:
            return "wrong_label_order_or_preamble"
        if not MemoryAnalyzer._parse_strict_response(candidate):
            return "multiline_or_trailing_noise"
        return "unknown_format"

    @staticmethod
    def _repair_to_strict_text(text: str) -> Optional[str]:
        if not text:
            return None
        candidate = text.strip()
        if not candidate:
            return None

        # Normalize unicode full-width colon into ASCII colon.
        candidate = candidate.replace("：", ":")

        fence_match = re.match(
            r"^```(?:[a-zA-Z0-9_-]+)?\n(?P<body>[\s\S]*?)\n```$",
            candidate,
            flags=re.IGNORECASE,
        )
        if fence_match:
            candidate = (fence_match.group("body") or "").strip()

        candidate = re.sub(
            r"\*\*\s*(GOAL_STATE|CURRENT_GOAL|SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*\*\*\s*:",
            r"\1:",
            candidate,
            flags=re.IGNORECASE,
        )
        candidate = re.sub(
            r"^\s*0\s*[\)\.\-]\s*GOAL\s+STATE\s*\(.*?\)\s*:",
            "GOAL_STATE:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(
            r"^\s*1\s*[\)\.\-]\s*CURRENT\s+GOAL\s*\(.*?\)\s*:",
            "CURRENT_GOAL:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(
            r"^\s*2\s*[\)\.\-]\s*SHORT[\s-]*TERM\s+MEMORY\s*\(.*?\)\s*:",
            "SHORT_TERM:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(
            r"^\s*3\s*[\)\.\-]\s*MEDIUM[\s-]*TERM\s+MEMORY\s*\(.*?\)\s*:",
            "MEDIUM_TERM:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(
            r"^\s*4\s*[\)\.\-]\s*LONG[\s-]*TERM\s+MEMORY\s*\(.*?\)\s*:",
            "LONG_TERM:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(r"\bGOAL[\s_-]*STATE\b", "GOAL_STATE", candidate, flags=re.IGNORECASE)
        candidate = re.sub(r"\bCURRENT[\s_-]*GOAL\b", "CURRENT_GOAL", candidate, flags=re.IGNORECASE)
        # Normalize label variants often produced by LLMs:
        # SHORT TERM / SHORT-TERM / short term -> SHORT_TERM
        candidate = re.sub(r"\bSHORT[\s_-]*TERM\b", "SHORT_TERM", candidate, flags=re.IGNORECASE)
        candidate = re.sub(r"\bMEDIUM[\s_-]*TERM\b", "MEDIUM_TERM", candidate, flags=re.IGNORECASE)
        candidate = re.sub(r"\bLONG[\s_-]*TERM\b", "LONG_TERM", candidate, flags=re.IGNORECASE)
        # Strip optional list numbering before labels: "1) SHORT_TERM: ..."
        candidate = re.sub(
            r"^\s*\d+\s*[\)\.\-]\s*((?:GOAL_STATE|CURRENT_GOAL|SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:)",
            r"\1",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(r"\r\n?", "\n", candidate).strip()
        first_label = re.search(r"^\s*(CURRENT_GOAL|SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:", candidate, flags=re.IGNORECASE | re.MULTILINE)
        if not first_label:
            return None
        # Allow one-line preamble before the first section by trimming everything before first label.
        candidate = candidate[first_label.start():].strip()

        label_pattern = re.compile(
            r"^\s*(GOAL_STATE|CURRENT_GOAL|SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:\s*",
            flags=re.IGNORECASE | re.MULTILINE,
        )
        matches = list(label_pattern.finditer(candidate))
        if not matches:
            return None

        labels_seen = [m.group(1).upper() for m in matches]
        for label in ("GOAL_STATE", "CURRENT_GOAL", "SHORT_TERM", "MEDIUM_TERM", "LONG_TERM"):
            if labels_seen.count(label) != 1:
                return None

        extracted = {"GOAL_STATE": "", "CURRENT_GOAL": "", "SHORT_TERM": "", "MEDIUM_TERM": "", "LONG_TERM": ""}
        for index, match in enumerate(matches):
            label = match.group(1).upper()
            section_start = match.end()
            section_end = matches[index + 1].start() if index + 1 < len(matches) else len(candidate)
            raw_value = candidate[section_start:section_end].strip()
            lines = []
            raw_lines = [line.strip() for line in raw_value.splitlines() if line.strip()]
            for idx, line in enumerate(raw_lines):
                if label in {"GOAL_STATE", "CURRENT_GOAL"}:
                    normalized_line = re.sub(r"^\s*[-*]\s*", "", line.strip())
                    if normalized_line:
                        lines.append(normalized_line)
                    continue
                if idx > 0 and not line.startswith(("-", "*")):
                    return None
                normalized_line = re.sub(r"^\s*[-*]\s*", "", line.strip())
                if normalized_line:
                    lines.append(normalized_line)
            if label in {"GOAL_STATE", "CURRENT_GOAL"}:
                extracted[label] = " ".join(lines).strip() or "EMPTY"
            else:
                extracted[label] = "\n".join(lines).strip() or "EMPTY"

        return (
            f"GOAL_STATE: {extracted['GOAL_STATE']}\n"
            f"CURRENT_GOAL: {extracted['CURRENT_GOAL']}\n"
            f"SHORT_TERM: {extracted['SHORT_TERM']}\n"
            f"MEDIUM_TERM: {extracted['MEDIUM_TERM']}\n"
            f"LONG_TERM: {extracted['LONG_TERM']}"
        )

    @staticmethod
    def _normalize_response_text(response_text: str) -> str:
        text = (response_text or "").strip()
        if not text:
            return ""
        # Keep normalization minimal so malformed formats are rejected by strict parser,
        # not silently transformed into valid ones.
        text = re.sub(r"\r\n?", "\n", text)
        return text.strip()

    @classmethod
    def _validate_short_term_value(cls, value: str) -> bool:
        if not value:
            return True
        return bool(cls._SHORT_TERM_VALUE_PATTERN.fullmatch(value))

    @staticmethod
    def _normalize_current_goal_value(value: str) -> str:
        goal = str(value or "").strip()
        if not goal:
            return ""
        goal = re.sub(r"\s+", " ", goal).strip()
        if goal.lower() in MemoryAnalyzer._EMPTY_VALUES:
            return ""
        return goal

    @staticmethod
    def _normalize_goal_state_value(value: str) -> str:
        state = str(value or "").strip().lower()
        if state in {"set", "keep", "clear", "replace", "empty"}:
            return state
        if state in MemoryAnalyzer._EMPTY_VALUES:
            return "empty"
        return "empty"

    @classmethod
    def _validate_medium_term_value(cls, value: str) -> bool:
        if not value:
            return True
        entries = [segment.strip() for segment in value.splitlines() if segment.strip()]
        if not entries:
            return False
        return all(cls._MEDIUM_TERM_ENTRY_PATTERN.fullmatch(entry) for entry in entries)

    @classmethod
    def _validate_long_term_value(cls, value: str) -> bool:
        if not value or value == "__CLEAR_LONG_TERM__":
            return True
        lines = [line.strip() for line in value.splitlines() if line.strip()]
        if not lines:
            return False
        return True

    def _sanitize_memory_value(self, value: str) -> str:
        if not value:
            return ""
        cleaned = str(value).strip()
        if cleaned.lower() in self._EMPTY_VALUES:
            return ""
        sanitized_lines: list[str] = []
        for line in cleaned.splitlines():
            normalized = line.strip()
            if not normalized:
                continue
            if self._TRANSPORT_PAYLOAD_PATTERN.search(normalized):
                continue
            sanitized_lines.append(normalized)
        if not sanitized_lines:
            return ""
        return "\n".join(sanitized_lines)

    def _filter_long_term_facts(self, value: str) -> str:
        """Keep only explicit stable facts in LONG_TERM, drop inferred/one-off artifacts."""
        if not value:
            return ""
        facts = self._split_memory_facts(value)
        filtered: list[str] = []
        for fact in facts:
            if self._NON_PROFILE_LONG_TERM_PATTERN.search(fact):
                continue
            if self._INFERRED_FACT_PATTERN.search(fact):
                continue
            # Keep explicit identity facts even if model wrapped them with request wording.
            if self._IDENTITY_FACT_PATTERN.search(fact):
                filtered.append(fact)
                continue
            if self._ONE_OFF_REQUEST_PATTERN.search(fact):
                continue
            filtered.append(fact)
        return self._join_memory_facts(filtered)

    @staticmethod
    def _split_memory_facts(value: str) -> list[str]:
        if not value:
            return []
        parts = []
        for line in value.splitlines():
            cleaned = line.strip()
            if cleaned:
                parts.append(cleaned)
        return parts

    @staticmethod
    def _join_memory_facts(parts: list[str]) -> str:
        if not parts:
            return ""
        return "\n".join(parts)

    @staticmethod
    def _dedupe_memory_facts(value: str) -> str:
        if not value:
            return ""
        lines = [line.strip() for line in value.splitlines() if line.strip()]
        if not lines:
            return ""
        unique_lines = []
        seen = set()
        for line in lines:
            normalized = " ".join(line.lower().split())
            if normalized in seen:
                continue
            seen.add(normalized)
            unique_lines.append(line)
        return "\n".join(unique_lines)

    def is_available(self) -> bool:
        """
        Проверяет доступность анализатора.
        
        Returns:
            True если анализатор готов к работе
        """
        return GEMINI_AVAILABLE and self.api_key is not None
