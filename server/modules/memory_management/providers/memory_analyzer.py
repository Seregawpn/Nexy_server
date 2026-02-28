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
from datetime import datetime, timezone
from typing import Tuple, Optional, Any

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    genai = None  # type: ignore

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
    _STRICT_RESPONSE_PATTERN = re.compile(
        r"^\s*"
        r"SHORT_TERM\s*:\s*(?P<short>[^\n]*)"
        r"\nMEDIUM_TERM\s*:\s*(?P<medium>[^\n]*)"
        r"\nLONG_TERM\s*:\s*(?P<long>[^\n]*)"
        r"\s*$",
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
    ):
        """
        Инициализация MemoryAnalyzer.
        
        Args:
            gemini_api_key: API ключ для Gemini
            token_tracker: Сервис для трекинга токенов (опционально)
            hardware_id: ID устройства для привязки токенов (опционально)
        """
        if not GEMINI_AVAILABLE or genai is None:
            raise ImportError("google.generativeai not available")
        
        self.api_key = gemini_api_key
        self.token_tracker = token_tracker
        self.hardware_id = hardware_id
        
        genai.configure(api_key=gemini_api_key)  # type: ignore
        
        # Настройки модели
        self.model_name = model_name or os.getenv("GEMINI_PRIMARY_MODEL", "gemini-flash-lite-latest")
        self.temperature = temperature
        
        # Каноничный промпт приходит только из MemoryConfig (single source of truth).
        if not analysis_prompt_template.strip():
            raise ValueError("analysis_prompt_template is required and must come from MemoryConfig")
        self.analysis_prompt_template = analysis_prompt_template
        
        logger.info("✅ MemoryAnalyzer initialized with Gemini API")
    
    async def analyze_conversation(
        self,
        prompt: str,
        response: str,
        hardware_id: Optional[str] = None,
        existing_short_memory: str = "",
        existing_medium_memory: str = "",
        existing_long_memory: str = "",
    ) -> Tuple[str, str, str]:
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
            Кортеж (short_memory, medium_memory, long_memory)
        """
        try:
            # Используем переданный hardware_id или сохраненный в self
            target_hardware_id = hardware_id or self.hardware_id
            # Формируем промпт для анализа
            current_date_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            analysis_prompt = self.analysis_prompt_template.format(
                prompt=prompt,
                response=response,
                current_date_utc=current_date_utc,
                existing_short_memory=existing_short_memory or "EMPTY",
                existing_medium_memory=existing_medium_memory or "EMPTY",
                existing_long_memory=existing_long_memory or "EMPTY",
            )
            
            # Создаем модель
            if genai is None:
                raise ImportError("google.generativeai not available")
            
            model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=genai.types.GenerationConfig(
                    temperature=self.temperature,
                    max_output_tokens=1024,
                )
            )
            
            # Анализируем диалог
            logger.debug(f"🧠 Analyzing conversation for memory extraction...")
            
            # Выполняем анализ асинхронно
            response_obj = await asyncio.to_thread(
                model.generate_content,
                analysis_prompt
            )
            
            if not response_obj:
                logger.warning("⚠️ Empty response from Gemini for memory analysis")
                return "", "", ""
                
            # Записываем использование токенов
            if self.token_tracker and target_hardware_id and hasattr(response_obj, 'usage_metadata'):
                try:
                    input_tokens = response_obj.usage_metadata.prompt_token_count
                    output_tokens = response_obj.usage_metadata.candidates_token_count
                    
                    self.token_tracker.record_usage(
                        hardware_id=target_hardware_id,
                        source='memory_analyzer',
                        input_tokens=input_tokens,
                        output_tokens=output_tokens,
                        model_name=self.model_name
                    )
                except Exception as e:
                    logger.warning(f"Failed to record memory analysis tokens: {e}")
            
            if not response_obj.text:
                logger.warning("⚠️ Empty text in response from Gemini")
                return "", "", ""
            
            # Парсим результат
            short_memory, medium_memory, long_memory = self._parse_analysis_response(response_obj.text)
            
            logger.info(
                "🧠 Memory analysis completed: short-term (%s chars), medium-term (%s chars), long-term (%s chars)",
                len(short_memory),
                len(medium_memory),
                len(long_memory),
            )
            
            return short_memory, medium_memory, long_memory
            
        except Exception as e:
            logger.error(f"❌ Error analyzing conversation for memory: {e}")
            return "", "", ""
    
    def _parse_analysis_response(self, response_text: str) -> Tuple[str, str, str]:
        """
        Парсит ответ от Gemini для извлечения краткосрочной и долгосрочной памяти.
        
        Args:
            response_text: Текст ответа от Gemini
            
        Returns:
            Кортеж (short_memory, medium_memory, long_memory)
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
                        "Expected exact canonical block with SHORT_TERM, MEDIUM_TERM, LONG_TERM and no extra text.",
                        reason,
                    )
                    return "", "", ""

            short_memory, medium_memory, long_memory = parsed_sections

            short_memory = self._sanitize_memory_value(short_memory)
            short_memory = self._dedupe_memory_facts(short_memory)
            medium_memory = self._sanitize_memory_value(medium_memory)
            medium_memory = self._dedupe_memory_facts(medium_memory)
            long_memory = self._sanitize_memory_value(long_memory)
            long_memory = self._dedupe_memory_facts(long_memory)
            long_memory = self._filter_long_term_facts(long_memory)

            if self._SECRET_PATTERN.search(short_memory):
                short_memory = "Sensitive credentials were mentioned"
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
            
            return short_memory, medium_memory, long_memory
            
        except Exception as e:
            logger.error(f"❌ Error parsing memory analysis response: {e}")
            return "", "", ""

    @staticmethod
    def _parse_strict_response(text: str) -> Optional[Tuple[str, str, str]]:
        if not text:
            return None
        labels = re.findall(
            r"^\s*(SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:",
            text,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        normalized_labels = [label.upper() for label in labels]
        if normalized_labels != ["SHORT_TERM", "MEDIUM_TERM", "LONG_TERM"]:
            return None
        match = MemoryAnalyzer._STRICT_RESPONSE_PATTERN.fullmatch(text)
        if not match:
            return None
        short_memory = (match.group("short") or "").strip()
        medium_memory = (match.group("medium") or "").strip()
        long_memory = (match.group("long") or "").strip()
        return short_memory, medium_memory, long_memory

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
            r"^\s*(SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        if not labels:
            return "missing_required_labels"
        normalized = [label.upper() for label in labels]
        if any(normalized.count(label) > 1 for label in ("SHORT_TERM", "MEDIUM_TERM", "LONG_TERM")):
            return "duplicate_labels"
        if normalized != ["SHORT_TERM", "MEDIUM_TERM", "LONG_TERM"]:
            return "wrong_label_order_or_preamble"
        if not MemoryAnalyzer._STRICT_RESPONSE_PATTERN.fullmatch(candidate):
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
            r"\*\*\s*(SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*\*\*\s*:",
            r"\1:",
            candidate,
            flags=re.IGNORECASE,
        )
        # Normalize label variants often produced by LLMs:
        # SHORT TERM / SHORT-TERM / short term -> SHORT_TERM
        candidate = re.sub(r"\bSHORT[\s_-]*TERM\b", "SHORT_TERM", candidate, flags=re.IGNORECASE)
        candidate = re.sub(r"\bMEDIUM[\s_-]*TERM\b", "MEDIUM_TERM", candidate, flags=re.IGNORECASE)
        candidate = re.sub(r"\bLONG[\s_-]*TERM\b", "LONG_TERM", candidate, flags=re.IGNORECASE)
        # Strip optional list numbering before labels: "1) SHORT_TERM: ..."
        candidate = re.sub(
            r"^\s*\d+\s*[\)\.\-]\s*((?:SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:)",
            r"\1",
            candidate,
            flags=re.IGNORECASE | re.MULTILINE,
        )
        candidate = re.sub(r"\r\n?", "\n", candidate).strip()
        first_label = re.search(r"^\s*(SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:", candidate, flags=re.IGNORECASE | re.MULTILINE)
        if not first_label:
            return None
        # Allow one-line preamble before the first section by trimming everything before first label.
        candidate = candidate[first_label.start():].strip()

        label_pattern = re.compile(
            r"^\s*(SHORT_TERM|MEDIUM_TERM|LONG_TERM)\s*:\s*",
            flags=re.IGNORECASE | re.MULTILINE,
        )
        matches = list(label_pattern.finditer(candidate))
        if not matches:
            return None

        labels_seen = [m.group(1).upper() for m in matches]
        for label in ("SHORT_TERM", "MEDIUM_TERM", "LONG_TERM"):
            if labels_seen.count(label) != 1:
                return None

        extracted = {"SHORT_TERM": "", "MEDIUM_TERM": "", "LONG_TERM": ""}
        for index, match in enumerate(matches):
            label = match.group(1).upper()
            section_start = match.end()
            section_end = matches[index + 1].start() if index + 1 < len(matches) else len(candidate)
            raw_value = candidate[section_start:section_end].strip()
            lines = []
            raw_lines = [line.strip() for line in raw_value.splitlines() if line.strip()]
            for idx, line in enumerate(raw_lines):
                if idx > 0 and not line.startswith(("-", "*")):
                    return None
                normalized_line = re.sub(r"^\s*[-*]\s*", "", line.strip())
                if normalized_line:
                    lines.append(normalized_line)
            extracted[label] = "; ".join(lines).strip() or "EMPTY"

        return (
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

    def _sanitize_memory_value(self, value: str) -> str:
        if not value:
            return ""
        cleaned = str(value).strip()
        if cleaned.lower() in self._EMPTY_VALUES:
            return ""
        return cleaned

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
            for part in line.split(";"):
                cleaned = part.strip()
                if cleaned:
                    parts.append(cleaned)
        return parts

    @staticmethod
    def _join_memory_facts(parts: list[str]) -> str:
        if not parts:
            return ""
        return "; ".join(parts)

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
            # Deduplicate atomic facts inside semicolon-based lines.
            if ";" in line:
                parts = [part.strip() for part in line.split(";") if part.strip()]
                unique_parts = []
                for part in parts:
                    normalized_part = " ".join(part.lower().split())
                    if normalized_part in seen:
                        continue
                    seen.add(normalized_part)
                    unique_parts.append(part)
                if unique_parts:
                    unique_lines.append("; ".join(unique_parts))
                continue

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
