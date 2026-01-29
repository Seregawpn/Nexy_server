#!/usr/bin/env python3
"""
Централизованная конфигурация для всего сервера Nexy
Объединяет все настройки из разных модулей в единую точку управления
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass, field
import logging

# Загружаем переменные окружения из config.env
config_path = Path(__file__).parent.parent / "config.env"
if config_path.exists():
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                # Используем rsplit для правильного разбора строк с = в значениях
                key, value = line.rsplit('=', 1)
                os.environ[key.strip()] = value.strip()

logger = logging.getLogger(__name__)


def get_version_from_file() -> str:
    """
    Читает версию из VERSION файла (единый источник истины)
    
    Returns:
        str: Версия из VERSION файла или дефолтное значение
    """
    # Ищем VERSION файл в корне проекта (на уровень выше server/)
    version_file = Path(__file__).parent.parent.parent / "VERSION"
    
    if version_file.exists():
        try:
            version = version_file.read_text().strip()
            if version:
                return version
        except Exception as e:
            logger.warning(f"Не удалось прочитать VERSION файл: {e}")
    
    # Fallback: используем переменную окружения или дефолт
    return os.getenv('SERVER_VERSION', '1.6.0.62')

@dataclass
class DatabaseConfig:
    """Конфигурация базы данных"""
    host: str = "localhost"
    port: int = 5432
    name: str = "voice_assistant_db"
    user: str = "postgres"
    password: str = ""
    
    @classmethod
    def from_env(cls) -> 'DatabaseConfig':
        return cls(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', '5432')),
            name=os.getenv('DB_NAME', 'voice_assistant_db'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', '')
        )

@dataclass
class GrpcConfig:
    """Конфигурация gRPC сервера"""
    host: str = "0.0.0.0"
    port: int = 50051
    max_workers: int = 10
    
    @classmethod
    def from_env(cls) -> 'GrpcConfig':
        env = os.getenv('NEXY_ENV', 'prod').lower()
        default_host = '127.0.0.1' if env in ('prod', 'stage') else '0.0.0.0'
        host_override = os.getenv('GRPC_HOST')
        host_value = host_override if host_override and host_override.lower() != 'auto' else default_host
        return cls(
            host=host_value,
            port=int(os.getenv('GRPC_PORT', '50051')),
            max_workers=int(os.getenv('MAX_WORKERS', '10'))
        )

@dataclass
class HttpConfig:
    """Конфигурация HTTP сервера health/status"""
    host: str = "0.0.0.0"
    port: int = 8080
    
    @classmethod
    def from_env(cls) -> 'HttpConfig':
        env = os.getenv('NEXY_ENV', 'prod').lower()
        default_host = '127.0.0.1' if env in ('prod', 'stage') else '0.0.0.0'
        host_override = os.getenv('HTTP_HOST')
        host_value = host_override if host_override and host_override.lower() != 'auto' else default_host
        return cls(
            host=host_value,
            port=int(os.getenv('HTTP_PORT', '8080'))
        )

@dataclass
class AudioConfig:
    """Конфигурация аудио (синхронизирована с клиентом)"""
    sample_rate: int = 48000  # 48kHz - единый источник истины для сервера и клиента
    chunk_size: int = 1024
    format: str = "int16"
    channels: int = 1
    bits_per_sample: int = 16
    
    # Edge TTS настройки (бесплатный, не требует API ключей)
    edge_tts_voice_name: str = "en-US-AriaNeural"
    edge_tts_rate: str = "+0%"
    edge_tts_volume: str = "+0%"
    edge_tts_pitch: str = "+0Hz"
    audio_format: str = "pcm"  # PCM для стриминга
    
    # Azure TTS (Legacy support for config loading)
    azure_speech_key: str = ""
    azure_speech_region: str = ""
    azure_voice_name: str = "en-US-AriaNeural"
    azure_voice_style: str = "friendly"
    azure_speech_rate: float = 1.0
    azure_speech_pitch: float = 1.0
    azure_speech_volume: float = 1.0
    azure_audio_format: str = "riff-48khz-16bit-mono-pcm"
    
    # Streaming настройки
    streaming_chunk_size: int = 4096
    streaming_enabled: bool = True
    
    @classmethod
    def from_env(cls) -> 'AudioConfig':
        return cls(
            sample_rate=int(os.getenv('SAMPLE_RATE', '48000')),  # 48kHz по умолчанию (синхронизировано с клиентом)
            chunk_size=int(os.getenv('CHUNK_SIZE', '1024')),
            format=os.getenv('AUDIO_FORMAT', 'int16'),
            channels=int(os.getenv('AUDIO_CHANNELS', '1')),
            bits_per_sample=int(os.getenv('AUDIO_BITS_PER_SAMPLE', '16')),
            edge_tts_voice_name=os.getenv('EDGE_TTS_VOICE_NAME', 'en-US-AriaNeural'),
            edge_tts_rate=os.getenv('EDGE_TTS_RATE', '+0%'),
            edge_tts_volume=os.getenv('EDGE_TTS_VOLUME', '+0%'),
            edge_tts_pitch=os.getenv('EDGE_TTS_PITCH', '+0Hz'),
            audio_format=os.getenv('AUDIO_FORMAT', 'pcm'),
            streaming_chunk_size=int(os.getenv('STREAMING_CHUNK_SIZE', '4096')),
            streaming_enabled=os.getenv('STREAMING_ENABLED', 'true').lower() == 'true'
        )

@dataclass
class TextProcessingConfig:
    """Конфигурация обработки текста"""
    gemini_api_key: str = ""
    
    # LangChain настройки
    langchain_model: str = "gemini-3-flash-preview"
    # Общие настройки для text processing
    temperature: float = 0.4
    max_tokens: int = 2048
    tools: list = field(default_factory=lambda: ['google_search'])
    gemini_system_prompt: str = (
        "You are Nexy Assistant — a friendly, empathetic, and highly concise AI designed for blind and low-vision users on macOS.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "**CRITICAL: Output Format Requirements**\n\n"
        "You MUST always respond with a **single valid JSON object** starting with `{` and ending with `}`.\n"
        "**NO PLAIN TEXT RESPONSES ALLOWED.**\n\n"
        "**session_id MUST be copied exactly from the request context** (provided by the system), never invented.\n"
        "- If the request session_id is not visible, do NOT output any action; return text-only JSON.\n\n"
        "- Output ONLY the raw JSON object, NO markdown code fences (```json ... ```), NO text before/after\n\n"
        "- The response must be parseable as JSON directly, without any preprocessing\n\n"
        "- NEVER include markdown formatting, code blocks, explanations, or extra text\n\n"
        "**JSON Field Specifications (STRICT):**\n"
        "1. \"session_id\" (Required):\n"
        "   - MUST be the exact UUID string from the user's request context.\n"
        "   - Place this at the TOP LEVEL of the JSON object.\n"
        "   - Example: \"session_id\": \"123e4567-e89b-...\"\n\n"
        "2. \"text\" (Required):\n"
        "   - This is what Nexy speaks to the user.\n"
        "   - Keep it short, friendly, and confirmation-based.\n"
        "   - Place this at the TOP LEVEL of the JSON object.\n"
        "   - Example: \"text\": \"Opening Safari for you.\"\n\n"
        "3. \"command\" (Optional - Action Only):\n"
        "   - The system command ID (e.g., \"open_app\").\n"
        "   - Place this at the TOP LEVEL.\n\n"
        "4. \"args\" (Optional - Action Only):\n"
        "   - A nested JSON object containing command parameters.\n"
        "   - Do NOT stringify this field.\n"
        "   - Example: \"args\": {\"app_name\": \"Safari\"}\n\n"
        "**SAFETY & REFUSALS:**\n"
        "- If you must refuse a request (e.g., safety, policy, toxic content), you MUST still output a valid JSON object.\n"
        "- Use the **Text-only JSON format** for refusals.\n"
        "- NEVER output raw text refusal.\n\n"
        "**WRONG (DO NOT DO THIS):**\n"
        "```json\n{\"text\": \"Hello\"}\n```\n"
        "Here is the response: {\"text\": \"Hello\"}\n"
        "Searching for Eminem clips...  <-- WRONG (Raw text)\n\n"
        "**CORRECT:**\n"
        "{\"text\": \"Hello\"}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Adaptive Pre-Analyzer — DO NOT OUTPUT]\n\n"
        "Before generating the JSON response, classify the user request:\n\n"
        "──────────────────────\n\n"
        "1. Action Intent (System Actions)\n\n"
        "User wants to perform an action (e.g., opening or closing an application).\n\n"
        "If user asks to open/launch an app:\n"
        "- **YOU MUST USE Action JSON format** with:\n"
        "  • \"command\": \"open_app\"\n"
        "  • \"args\": {\"app_name\": \"<exact macOS app name>\"}\n"
        "  • \"session_id\": <MUST reuse from request, REQUIRED, never null>\n"
        "  • \"text\": short confirmation (\"Opening Safari now.\")\n\n"
        "If user asks to close/quit an app:\n"
        "- Use **Action JSON format** with:\n"
        "  • \"command\": \"close_app\"\n"
        "  • \"args\": {\"app_name\": \"<exact macOS app name>\"}\n"
        "  • \"session_id\": <MUST reuse from request, REQUIRED, never null>\n"
        "  • \"text\": short confirmation (\"Closing Safari now.\")\n\n"
        "**MESSAGES ACTIONS (ALWAYS use Action JSON, NEVER ask to open Messages app):**\n\n"
        "If user asks to read/check/show messages (triggers: \"read messages\", \"check messages\", \"show messages\", \"last messages\", \"messages from\", \"what did X say\", \"прочитай сообщения\", \"покажи сообщения\"):\n"
        "- Use **Action JSON format** with:\n"
        "  • \"command\": \"read_messages\"\n"
        "  • \"args\": {\"contact\": \"<name, phone, or 'all' for recent>\", \"limit\": <number, default 10>}\n"
        "  • \"session_id\": <reuse from request>\n"
        "  • \"text\": short confirmation (\"Reading messages from Mom.\")\n\n"
        "If user asks to send/text a message (triggers: \"send message\", \"text\", \"tell X\", \"message X\", \"отправь сообщение\", \"напиши\"):\n"
        "- Use **Action JSON format** with:\n"
        "  • \"command\": \"send_message\"\n"
        "  • \"args\": {\"contact\": \"<name or phone>\", \"message\": \"<text>\"}\n"
        "  • \"session_id\": <reuse from request>\n"
        "  • \"text\": short confirmation (\"Sending message to Mom.\")\n\n"
        "If user asks to find a contact (triggers: \"find contact\", \"search contact\", \"who is\", \"найди контакт\"):\n"
        "- Use **Action JSON format** with:\n"
        "  • \"command\": \"find_contact\"\n"
        "  • \"args\": {\"query\": \"<name, phone, or email>\"}\n"
        "  • \"session_id\": <reuse from request>\n"
        "  • \"text\": short confirmation (\"Searching for contact.\")\n\n"
        "If action is unsupported:\n"
        "- Use **Text-only JSON format** with explanation + one helpful suggestion\n\n"
        "If user needs navigation steps:\n"
        "- Use **Text-only JSON format** with numbered VoiceOver-friendly steps in \"text\"\n\n"
        "──────────────────────\n\n"
        "2. Describe Intent (Screen, images, interface)\n\n"
        "User asks to describe visible content.\n"
        "- Use **Text-only JSON format** with:\n"
        "  • 1-line summary\n"
        "  • 3–5 key elements with spatial hints (\"top-left\", \"center\", \"right side\")\n"
        "  • 1–2 short next-step suggestions\n"
        "- If something expected is missing, state that and offer concrete action\n\n"
        "──────────────────────\n\n"
        "3. WebSearch Intent\n\n"
        "Request involves finding information, facts, news, or prices (\"search\", \"find\", \"Google\", \"price\", \"latest\", \"compare\").\n"
        "- ALWAYS perform a **real web search** using the web search tool\n"
        "- NEVER guess or simulate\n"
        "- Use **Text-only JSON format** with:\n"
        "  • 1–3 verified key results\n"
        "  • Optional reliable source\n"
        "  • If nothing found → say that and suggest refining the query\n"
        "- Do NOT output steps or instructions for WebSearch results\n\n"
        "──────────────────────\n\n"
        "4. Browser Automation Intent (browser_use)\n\n"
        "User wants to interact with **WEBSITES** to perform tasks (navigation, login, ordering, watching).\n"
        "Triggers: \"Open [Site]\", \"Go to [Site]\", \"Play [Video]\", \"Order [Item]\", \"Log in to...\", \"Check my...\" on a specific site.\n"
        "**Note:** General information queries (\"Search for cats\", \"Who is...\", \"Price of...\") are **WebSearch**, NOT Browser.\n"
        "- **Explicitly prefers browser_use** for: YouTube, Google, Wikipedia, Amazon, Reddit, etc.\n"
        "- Use **Action JSON format** with:\n"
        "  • \"command\": \"browser_use\"\n"
        "  • command MUST be exactly \"browser_use\" (no hyphens/dots/spaces)\n"
        "  • DO NOT wrap in action_json/payload, DO NOT JSON-encode the object or args\n"
        "  • \"args\": {\"task\": \"<detailed description of the task>\"}\n"
        "  • \"session_id\": <MUST reuse from request, REQUIRED>\n"
        "  • \"text\": short confirmation (e.g. \"Starting browser task...\")\n"
        "- **CRITICAL**: Do NOT ask for confirmation. Do NOT say \"Would you like me to...?\". JUST DO IT.\n"
        "- Do NOT use browser_use for simple informational searches (use WebSearch instead).\n"
        "- If the user says \"Open [Website]\", it is ALWAYS a browser_use command.\n\n"
        "──────────────────────\n\n"
        "5. Ambiguous Intent\n\n"
        "If unclear:\n"
        "- Use **Text-only JSON format**\n"
        "- Provide best short answer + ask 1 clarifying question: \"Would you like me to describe it or perform an action?\"\n\n"
        "──────────────────────\n\n"
        "6. SmallTalk\n\n"
        "Greetings, emotions, light conversation.\n"
        "- Use **Text-only JSON format**\n"
        "- 1–2 short friendly sentences\n"
        "- No steps, no actions unless requested\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Contextual Visibility Layer — DO NOT OUTPUT]\n\n"
        "If user asks \"Do you see…?\", \"Is there…?\", \"Can you find…?\":\n"
        "- If visible: text confirms, gives approximate location, provides one action suggestion\n"
        "- If NOT visible: text clearly says it's not visible, offers 1–2 concrete next actions\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Language & Style]\n\n"
        "- ALWAYS respond in English\n"
        "- Keep text simple, short, and VoiceOver-friendly\n"
        "- No filler, no apologies, no self-references\n"
        "- Prefer compact lists when useful\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Processing Priority]\n\n"
        "If multiple intentions overlap, resolve in this order:\n"
        "1) Messages Actions (read_messages, send_message, find_contact) - HIGHEST PRIORITY for any message-related requests\n"
        "2) Browser Automation (browser_use) - for any 'Open [Website]' or 'Search [Website]'\n"
        "3) System Actions (open_app / close_app)\n"
        "4) Describe\n"
        "5) WebSearch\n"
        "6) SmallTalk\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[DECISION GUIDE: Text vs Action]\n\n"
        "1. **Text-Only JSON** (Use for answers, explanations, refusals)\n"
        "   - \"How do I change volume?\" -> Explain steps (Text).\n"
        "   - \"Who is the president?\" -> Answer fact (Text).\n"
        "   - \"I am sad.\" -> Empathize (Text).\n"
        "   - \"Open the pod bay doors.\" -> \"I cannot do that.\" (Text refusal).\n\n"
        "2. **Action JSON** (Use ONLY when you can actually perform it)\n"
        "   - \"Change volume to 50%\" -> run_command(...) (Action). *Only if tool exists!*\n"
        "   - \"Open Safari\" -> open_app (Action).\n"
        "   - \"Search for cats on YouTube\" -> browser_use (Action).\n\n"
        "**CRITICAL:** Do NOT simulate actions with text.\n"
        "- Wrong: {\"text\": \"Opening Safari...\"} (Text-only)\n"
        "- Wrong: Opening Safari... (Plain text - FORBIDDEN)\n"
        "- Right: {\"command\": \"open_app\", ...} (Action)\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Action Output Format — DO NOT OUTPUT]\n\n"
        "You MUST use **one of the two formats below**:\n\n"
        "──────────────\n\n"
        "1) Action Response (when performing an action, e.g. opening or closing an app)\n\n"
        "Example 1: Opening an app\n"
        "{\n"
        "  \"session_id\": \"<MUST use session_id from request, REQUIRED>\",\n"
        "  \"command\": \"open_app\",\n"
        "  \"args\": {\n"
        "    \"app_name\": \"Calculator\"\n"
        "  },\n"
        "  \"text\": \"Opening Calculator.\"\n"
        "}\n\n"
        "Example 2: Closing an app\n"
        "{\n"
        "  \"session_id\": \"<MUST use session_id from request, REQUIRED>\",\n"
        "  \"command\": \"close_app\",\n"
        "  \"args\": {\n"
        "    \"app_name\": \"Safari\"\n"
        "  },\n"
        "  \"text\": \"Closing Safari.\"\n"
        "}\n\n"
        "Example 3: Browser Automation\n"
        "{\n"
        "  \"session_id\": \"<MUST use session_id from request>\",\n"
        "  \"command\": \"browser_use\",\n"
        "  \"args\": {\n"
        "    \"task\": \"Open YouTube\"\n"
        "  },\n"
        "  \"text\": \"Opening YouTube in browser.\"\n"
        "}\n\n"
        "Example 4: Reading messages\n"
        "{\n"
        "  \"session_id\": \"<from request>\",\n"
        "  \"command\": \"read_messages\",\n"
        "  \"args\": {\n"
        "    \"contact\": \"Mom\",\n"
        "    \"limit\": 5\n"
        "  },\n"
        "  \"text\": \"Reading last 5 messages from Mom.\"\n"
        "}\n\n"
        "Example 5: Sending a message\n"
        "{\n"
        "  \"session_id\": \"<from request>\",\n"
        "  \"command\": \"send_message\",\n"
        "  \"args\": {\n"
        "    \"contact\": \"Mom\",\n"
        "    \"message\": \"I'll be there in 10 minutes\"\n"
        "  },\n"
        "  \"text\": \"Sending message to Mom.\"\n"
        "}\n\n"
        "Rules:\n"
        "- session_id: REQUIRED, must be the exact session_id from the request (never null)\n"
        "- command: lowercase string, MUST be exactly one of: open_app, close_app, browser_use, close_browser, read_messages, send_message, find_contact\n"
        "- args: MUST be a JSON object (not a string), never JSON-encoded\n"
        "- text: 1–3 short sentences\n"
        "- For open_app: args must contain app_name\n"
        "- For close_app: args must contain app_name\n"
        "- For browser_use: args must contain task\\n"
        "- For close_browser: args can be empty (explicit close only)\\n"
        "- For read_messages: args must contain contact; limit is optional (default 10)\n"
        "- For send_message: args must contain contact and message\n"
        "- For find_contact: args must contain query\n"
        "- NEVER add any extra fields\n"
        "- NEVER wrap the response in another JSON object or string field\n"
        "- If session_id is missing or null → action will be ignored, only text will be used\n\n"
        "──────────────\n\n"
        "2) Normal Response (NO action required)\n\n"
        "{\n"
        "  \"text\": \"The Calculator app is already open. What would you like to do next?\"\n"
        "}\n\n"
        "Rules:\n"
        "- Only the \"text\" field is allowed\n"
        "- No command, no args, no session_id unless performing an action\n"
    )
    
    # Настройки изображений
    image_format: str = "webp"
    image_mime_type: str = "image/webp"
    image_max_size: int = 10 * 1024 * 1024  # 10MB
    streaming_chunk_size: int = 8192
    
    
    # Fallback настройки
    fallback_timeout: int = 30
    circuit_breaker_threshold: int = 3
    circuit_breaker_timeout: int = 300
    
    # Производительность
    max_concurrent_requests: int = 10
    request_timeout: int = 300  # Увеличено до 5 минут для длинных TTS ответов (было 60)
    
    @classmethod
    def from_env(cls) -> 'TextProcessingConfig':
        return cls(
            gemini_api_key=os.getenv('GEMINI_API_KEY', ''),
            langchain_model=os.getenv('LANGCHAIN_MODEL', 'gemini-3-flash-preview'),
            temperature=float(os.getenv('TEXT_PROCESSING_TEMPERATURE', os.getenv('GEMINI_LIVE_TEMPERATURE', '0.4'))),
            max_tokens=int(os.getenv('TEXT_PROCESSING_MAX_TOKENS', os.getenv('GEMINI_LIVE_MAX_TOKENS', '2048'))),
            tools=os.getenv('TEXT_PROCESSING_TOOLS', os.getenv('GEMINI_LIVE_TOOLS', 'google_search')).split(',') if os.getenv('TEXT_PROCESSING_TOOLS') or os.getenv('GEMINI_LIVE_TOOLS') else ['google_search'],
            gemini_system_prompt=os.getenv('GEMINI_SYSTEM_PROMPT', cls.gemini_system_prompt),
            image_format=os.getenv('IMAGE_FORMAT', 'webp'),
            image_mime_type=os.getenv('IMAGE_MIME_TYPE', 'image/webp'),
            image_max_size=int(os.getenv('IMAGE_MAX_SIZE', str(10 * 1024 * 1024))),
            streaming_chunk_size=int(os.getenv('STREAMING_CHUNK_SIZE', '8192')),
            fallback_timeout=int(os.getenv('FALLBACK_TIMEOUT', '30')),
            circuit_breaker_threshold=int(os.getenv('CIRCUIT_BREAKER_THRESHOLD', '3')),
            circuit_breaker_timeout=int(os.getenv('CIRCUIT_BREAKER_TIMEOUT', '300')),
            max_concurrent_requests=int(os.getenv('MAX_CONCURRENT_REQUESTS', '10')),
            request_timeout=int(os.getenv('REQUEST_TIMEOUT', '300'))  # Синхронизировано: 5 минут для длинных TTS ответов
        )

@dataclass
class MemoryConfig:
    """Конфигурация управления памятью"""
    gemini_api_key: str = ""
    max_short_term_memory_size: int = 10240  # 10KB
    max_long_term_memory_size: int = 10240   # 10KB
    memory_timeout: float = 2.0
    analysis_timeout: float = 5.0
    memory_analysis_model: str = "gemini-2.5-flash-lite"
    memory_analysis_temperature: float = 0.3
    
    @classmethod
    def from_env(cls) -> 'MemoryConfig':
        return cls(
            gemini_api_key=os.getenv('GEMINI_API_KEY', ''),
            max_short_term_memory_size=int(os.getenv('MAX_SHORT_TERM_MEMORY_SIZE', '10240')),
            max_long_term_memory_size=int(os.getenv('MAX_LONG_TERM_MEMORY_SIZE', '10240')),
            memory_timeout=float(os.getenv('MEMORY_TIMEOUT', '2.0')),
            analysis_timeout=float(os.getenv('ANALYSIS_TIMEOUT', '5.0')),
            memory_analysis_model=os.getenv('MEMORY_ANALYSIS_MODEL', 'gemini-2.5-flash-lite'),
            memory_analysis_temperature=float(os.getenv('MEMORY_ANALYSIS_TEMPERATURE', '0.3'))
        )

@dataclass
class SessionConfig:
    """Конфигурация управления сессиями"""
    max_sessions: int = 100
    session_timeout: int = 3600  # 1 час
    hardware_id_length: int = 32
    
    @classmethod
    def from_env(cls) -> 'SessionConfig':
        return cls(
            max_sessions=int(os.getenv('MAX_SESSIONS', '100')),
            session_timeout=int(os.getenv('SESSION_TIMEOUT', '3600')),
            hardware_id_length=int(os.getenv('HARDWARE_ID_LENGTH', '32'))
        )

@dataclass
class InterruptConfig:
    """Конфигурация управления прерываниями"""
    global_interrupt_timeout: int = 300  # 5 минут
    session_interrupt_timeout: int = 60  # 1 минута
    max_active_sessions: int = 50
    
    @classmethod
    def from_env(cls) -> 'InterruptConfig':
        return cls(
            global_interrupt_timeout=int(os.getenv('GLOBAL_INTERRUPT_TIMEOUT', '300')),
            session_interrupt_timeout=int(os.getenv('SESSION_INTERRUPT_TIMEOUT', '60')),
            max_active_sessions=int(os.getenv('MAX_ACTIVE_SESSIONS', '50'))
        )

@dataclass
class WorkflowConfig:
    """Конфигурация потокового workflow"""

    stream_min_chars: int = 5
    stream_min_words: int = 2
    stream_first_sentence_min_words: int = 1
    stream_punct_flush_strict: bool = True
    force_flush_max_chars: int = 300
    # Guard по hardware_id: если True, блокирует параллельные сессии одного устройства
    # Если False (по умолчанию), допускаются параллельные сессии одного hardware_id
    prevent_concurrent_hardware_id_sessions: bool = False

    @classmethod
    def from_env(cls) -> 'WorkflowConfig':
        return cls(
            stream_min_chars=int(os.getenv('STREAM_MIN_CHARS', os.getenv('TTS_MIN_CHARS', '15'))),
            stream_min_words=int(os.getenv('STREAM_MIN_WORDS', os.getenv('TTS_MIN_WORDS', '3'))),
            stream_first_sentence_min_words=int(
                os.getenv(
                    'STREAM_FIRST_SENTENCE_MIN_WORDS',
                    os.getenv('TTS_FIRST_SENTENCE_MIN_WORDS', '2')
                )
            ),
            stream_punct_flush_strict=os.getenv(
                'STREAM_PUNCT_FLUSH_STRICT', os.getenv('TTS_PUNCT_FLUSH_STRICT', 'true')
            ).lower() == 'true',
            force_flush_max_chars=int(os.getenv('STREAM_FORCE_FLUSH_MAX_CHARS', '0') or 0),
            prevent_concurrent_hardware_id_sessions=os.getenv(
                'PREVENT_CONCURRENT_HARDWARE_ID_SESSIONS', 'false'
            ).lower() == 'true'
        )


@dataclass
class UpdateServiceConfig:
    """Конфигурация сервиса обновлений"""

    enabled: bool = True
    host: str = '0.0.0.0'
    port: int = 8081
    cors_enabled: bool = True
    cache_control: str = 'no-cache, no-store, must-revalidate'
    require_https: bool = False
    verify_signatures: bool = True
    log_requests: bool = True
    log_downloads: bool = True
    updates_dir: Optional[str] = None
    downloads_dir: Optional[str] = None
    keys_dir: Optional[str] = None
    manifests_dir: Optional[str] = None
    default_version: str = get_version_from_file()
    default_build: str = get_version_from_file()
    default_arch: str = 'universal2'
    default_min_os: str = '11.0'

    @classmethod
    def from_env(cls) -> 'UpdateServiceConfig':
        base_dir = Path(__file__).parent.parent / 'updates'
        env = os.getenv('NEXY_ENV', 'prod').lower()
        default_host = '127.0.0.1' if env in ('prod', 'stage') else '0.0.0.0'
        host_override = os.getenv('UPDATE_HOST')
        host_value = host_override if host_override and host_override.lower() != 'auto' else default_host
        return cls(
            enabled=os.getenv('UPDATE_ENABLED', 'true').lower() == 'true',
            host=host_value,
            port=int(os.getenv('UPDATE_PORT', '8081')),
            cors_enabled=os.getenv('UPDATE_CORS', 'true').lower() == 'true',
            cache_control=os.getenv('UPDATE_CACHE_CONTROL', 'no-cache, no-store, must-revalidate'),
            require_https=os.getenv('UPDATE_REQUIRE_HTTPS', 'false').lower() == 'true',
            verify_signatures=os.getenv('UPDATE_VERIFY_SIGNATURES', 'true').lower() == 'true',
            log_requests=os.getenv('UPDATE_LOG_REQUESTS', 'true').lower() == 'true',
            log_downloads=os.getenv('UPDATE_LOG_DOWNLOADS', 'true').lower() == 'true',
            updates_dir=os.getenv('UPDATE_DIR') or str(base_dir),
            downloads_dir=os.getenv('UPDATE_DOWNLOADS_DIR') or str(base_dir / 'downloads'),
            keys_dir=os.getenv('UPDATE_KEYS_DIR') or str(base_dir / 'keys'),
            manifests_dir=os.getenv('UPDATE_MANIFESTS_DIR') or str(base_dir / 'manifests'),
            default_version=os.getenv('SERVER_VERSION') or get_version_from_file(),
            default_build=os.getenv('SERVER_BUILD') or get_version_from_file(),
            default_arch=os.getenv('UPDATE_DEFAULT_ARCH', 'universal2'),
            default_min_os=os.getenv('UPDATE_DEFAULT_MIN_OS', '11.0')
        )


@dataclass
class ServerMetadataConfig:
    """Метаданные сервера"""

    version: str = get_version_from_file()
    build: str = get_version_from_file()
    channel: str = 'stable'

    @classmethod
    def from_env(cls) -> 'ServerMetadataConfig':
        version = os.getenv('SERVER_VERSION') or get_version_from_file()
        build = os.getenv('SERVER_BUILD') or version
        return cls(
            version=version,
            build=build,
            channel=os.getenv('SERVER_CHANNEL', 'stable')
        )


@dataclass
class LoggingConfig:
    """Конфигурация логирования"""
    level: str = "INFO"
    log_requests: bool = True
    log_responses: bool = False
    log_file: str = "server.log"
    max_file_size: int = 10485760  # 10MB
    backup_count: int = 5
    
    @classmethod
    def from_env(cls) -> 'LoggingConfig':
        return cls(
            level=os.getenv('LOG_LEVEL', 'INFO'),
            log_requests=os.getenv('LOG_REQUESTS', 'true').lower() == 'true',
            log_responses=os.getenv('LOG_RESPONSES', 'false').lower() == 'true',
            log_file=os.getenv('LOG_FILE', 'server.log'),
            max_file_size=int(os.getenv('LOG_MAX_FILE_SIZE', '10485760')),
            backup_count=int(os.getenv('LOG_BACKUP_COUNT', '5'))
        )

@dataclass
class FeaturesConfig:
    """Конфигурация фича-флагов"""
    use_module_coordinator: bool = True
    use_workflow_integrations: bool = True
    use_fallback_manager: bool = True
    forward_assistant_actions: bool = False  # MCP command forwarding (Phase 1)
    
    @classmethod
    def from_env(cls) -> 'FeaturesConfig':
        return cls(
            use_module_coordinator=os.getenv('USE_MODULE_COORDINATOR', 'true').lower() == 'true',
            use_workflow_integrations=os.getenv('USE_WORKFLOW_INTEGRATIONS', 'true').lower() == 'true',
            use_fallback_manager=os.getenv('USE_FALLBACK_MANAGER', 'true').lower() == 'true',
            forward_assistant_actions=os.getenv('FORWARD_ASSISTANT_ACTIONS', 'false').lower() == 'true'
        )

@dataclass
class BackpressureConfig:
    """
    Конфигурация backpressure для стримов
    
    Note:
        max_message_rate_per_second: Максимальное количество сообщений в секунду на стрим.
        Если установлено в 0 или меньше, rate limit отключается полностью.
        Используйте 0 для отключения ограничения частоты сообщений (например, для аудио стримов с высокой частотой).
    """
    max_concurrent_streams: int = 50
    idle_timeout_seconds: int = 900  # Увеличено до 15 минут для длинных TTS ответов (было 300)
    max_message_rate_per_second: int = 0  # Синхронизировано: 0 = отключить rate limit по умолчанию (было 20)
    grace_period_seconds: int = 30
    
    @classmethod
    def from_env(cls) -> 'BackpressureConfig':
        return cls(
            max_concurrent_streams=int(os.getenv('BACKPRESSURE_MAX_STREAMS', '50')),
            idle_timeout_seconds=int(os.getenv('BACKPRESSURE_IDLE_TIMEOUT', '900')),  # Синхронизировано: 15 минут для длинных TTS ответов
            max_message_rate_per_second=int(os.getenv('BACKPRESSURE_MAX_RATE', '0')),  # Синхронизировано: 0 = отключить rate limit по умолчанию
            grace_period_seconds=int(os.getenv('BACKPRESSURE_GRACE_PERIOD', '30'))
        )
    
    @classmethod
    def from_env_dev(cls) -> 'BackpressureConfig':
        """Конфигурация для dev окружения"""
        return cls(
            max_concurrent_streams=10,
            idle_timeout_seconds=60,
            max_message_rate_per_second=5,
            grace_period_seconds=10
        )
    
    @classmethod
    def from_env_stage(cls) -> 'BackpressureConfig':
        """Конфигурация для stage окружения"""
        return cls(
            max_concurrent_streams=25,
            idle_timeout_seconds=180,
            max_message_rate_per_second=8,
            grace_period_seconds=20
        )
    
    @classmethod
    def from_env_prod(cls) -> 'BackpressureConfig':
        """Конфигурация для prod окружения"""
        return cls(
            max_concurrent_streams=50,
            idle_timeout_seconds=900,  # Увеличено до 15 минут для длинных TTS ответов (было 300)
            max_message_rate_per_second=0,  # Синхронизировано: 0 = отключить rate limit по умолчанию
            grace_period_seconds=30
        )

@dataclass
class KillSwitchesConfig:
    """Конфигурация kill-switch"""
    disable_module_coordinator: bool = False
    disable_workflow_integrations: bool = False
    disable_forward_assistant_actions: bool = False  # MCP command forwarding kill-switch (Phase 1)
    
    @classmethod
    def from_env(cls) -> 'KillSwitchesConfig':
        return cls(
            disable_module_coordinator=os.getenv('NEXY_KS_DISABLE_MODULE_COORDINATOR', 'false').lower() == 'true',
            disable_workflow_integrations=os.getenv('NEXY_KS_DISABLE_WORKFLOW_INTEGRATIONS', 'false').lower() == 'true',
            disable_forward_assistant_actions=os.getenv('NEXY_KS_DISABLE_FORWARD_ASSISTANT_ACTIONS', 'false').lower() == 'true'
        )

@dataclass
class BrowserUseConfig:
    """Конфигурация browser-use автоматизации"""
    enabled: bool = False
    default_preset: str = 'ultra_fast'
    keep_browser_open: bool = False
    timeout_sec: int = 120
    max_steps: int = 50
    gemini_model: str = 'gemini-2.5-flash'
    
    @classmethod
    def from_env(cls) -> 'BrowserUseConfig':
        return cls(
            enabled=os.getenv('BROWSER_USE_ENABLED', 'false').lower() == 'true',
            default_preset=os.getenv('BROWSER_USE_PRESET', 'ultra_fast'),
            keep_browser_open=os.getenv('BROWSER_USE_KEEP_OPEN', 'false').lower() == 'true',
            timeout_sec=int(os.getenv('BROWSER_USE_TIMEOUT', '120')),
            max_steps=int(os.getenv('BROWSER_USE_MAX_STEPS', '50')),
            gemini_model=os.getenv('BROWSER_USE_MODEL', 'gemini-2.5-flash')
        )

@dataclass
class PaymentUseConfig:
    """Конфигурация payment-use автоматизации"""
    enabled: bool = False
    timeout_sec: int = 120
    max_steps: int = 50
    gemini_model: str = 'gemini-2.5-flash'
    log_steps: bool = True
    log_transactions: bool = True
    
    @classmethod
    def from_env(cls) -> 'PaymentUseConfig':
        return cls(
            enabled=os.getenv('PAYMENT_USE_ENABLED', 'false').lower() == 'true',
            timeout_sec=int(os.getenv('PAYMENT_USE_TIMEOUT', '120')),
            max_steps=int(os.getenv('PAYMENT_USE_MAX_STEPS', '50')),
            gemini_model=os.getenv('PAYMENT_USE_MODEL', 'gemini-2.5-flash'),
            log_steps=os.getenv('PAYMENT_USE_LOG_STEPS', 'true').lower() == 'true',
            log_transactions=os.getenv('PAYMENT_USE_LOG_TRANSACTIONS', 'true').lower() == 'true'
        )

@dataclass
class SubscriptionConfig:
    """
    Конфигурация платёжной системы Stripe
    
    Feature ID: F-2025-017-stripe-payment
    
    По умолчанию ОТКЛЮЧЕНО - продукт работает без проверок подписок.
    """
    # Feature flags
    enabled: bool = False  # Главный переключатель - по умолчанию ОТКЛЮЧЕНО
    kill_switch: bool = False  # Аварийное отключение
    
    # Stripe API keys
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_publishable_key: str = ""
    stripe_price_id: str = ""  # Monthly subscription price ID
    
    # Trial configuration
    trial_days: int = 14
    grace_period_hours: int = 24
    
    # Quota limits (for limited_free_trial)
    quota_daily: int = 5
    quota_weekly: int = 25
    quota_monthly: int = 50
    
    # Cache configuration
    cache_ttl_seconds: int = 30
    
    # Scheduler intervals (in hours)
    trial_check_interval_hours: int = 6
    grace_period_check_interval_hours: int = 6
    
    @classmethod
    def from_env(cls) -> 'SubscriptionConfig':
        return cls(
            enabled=os.getenv('SUBSCRIPTION_ENABLED', 'false').lower() == 'true',
            kill_switch=os.getenv('SUBSCRIPTION_KILL_SWITCH', 'false').lower() == 'true',
            stripe_secret_key=os.getenv('STRIPE_SECRET_KEY', ''),
            stripe_webhook_secret=os.getenv('STRIPE_WEBHOOK_SECRET', ''),
            stripe_publishable_key=os.getenv('STRIPE_PUBLISHABLE_KEY', ''),
            stripe_price_id=os.getenv('STRIPE_PRICE_ID', ''),
            trial_days=int(os.getenv('SUBSCRIPTION_TRIAL_DAYS', '14')),
            grace_period_hours=int(os.getenv('SUBSCRIPTION_GRACE_PERIOD_HOURS', '24')),
            quota_daily=int(os.getenv('SUBSCRIPTION_QUOTA_DAILY', '5')),
            quota_weekly=int(os.getenv('SUBSCRIPTION_QUOTA_WEEKLY', '25')),
            quota_monthly=int(os.getenv('SUBSCRIPTION_QUOTA_MONTHLY', '50')),
            cache_ttl_seconds=int(os.getenv('SUBSCRIPTION_CACHE_TTL', '30')),
            trial_check_interval_hours=int(os.getenv('SUBSCRIPTION_TRIAL_CHECK_HOURS', '6')),
            grace_period_check_interval_hours=int(os.getenv('SUBSCRIPTION_GRACE_CHECK_HOURS', '6'))
        )
    
    def is_active(self) -> bool:
        """Проверяет, активна ли платёжная система (enabled и не kill_switch)"""
        return self.enabled and not self.kill_switch


@dataclass
class WhatsappConfig:
    """
    Конфигурация интеграции WhatsApp
    
    Feature ID: F-2025-WHATSAPP
    """
    enabled: bool = False
    
    @classmethod
    def from_env(cls) -> 'WhatsappConfig':
        return cls(
            enabled=os.getenv('WHATSAPP_ENABLED', 'false').lower() == 'true'
        )

@dataclass
class UnifiedServerConfig:
    """Централизованная конфигурация всего сервера"""
    database: DatabaseConfig = field(default_factory=DatabaseConfig.from_env)
    grpc: GrpcConfig = field(default_factory=GrpcConfig.from_env)
    http: HttpConfig = field(default_factory=HttpConfig.from_env)
    audio: AudioConfig = field(default_factory=AudioConfig.from_env)
    text_processing: TextProcessingConfig = field(default_factory=TextProcessingConfig.from_env)
    memory: MemoryConfig = field(default_factory=MemoryConfig.from_env)
    session: SessionConfig = field(default_factory=SessionConfig.from_env)
    interrupt: InterruptConfig = field(default_factory=InterruptConfig.from_env)
    workflow: WorkflowConfig = field(default_factory=WorkflowConfig.from_env)
    update: UpdateServiceConfig = field(default_factory=UpdateServiceConfig.from_env)
    server: ServerMetadataConfig = field(default_factory=ServerMetadataConfig.from_env)
    logging: LoggingConfig = field(default_factory=LoggingConfig.from_env)
    features: FeaturesConfig = field(default_factory=FeaturesConfig.from_env)
    kill_switches: KillSwitchesConfig = field(default_factory=KillSwitchesConfig.from_env)
    backpressure: BackpressureConfig = field(default_factory=BackpressureConfig.from_env)
    browser_use: BrowserUseConfig = field(default_factory=BrowserUseConfig.from_env)
    payment_use: PaymentUseConfig = field(default_factory=PaymentUseConfig.from_env)
    subscription: SubscriptionConfig = field(default_factory=SubscriptionConfig.from_env)
    whatsapp: WhatsappConfig = field(default_factory=WhatsappConfig.from_env)
    
    def __post_init__(self):
        """Пост-инициализация для валидации"""
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Валидация всей конфигурации"""
        errors = []
        
        # Проверяем критические настройки
        if not self.text_processing.gemini_api_key:
            errors.append("GEMINI_API_KEY не установлен")
        
        # Edge TTS не требует ключей - пропускаем проверку
        
        # Проверяем диапазоны значений
        if not (0 <= self.text_processing.temperature <= 2):
            errors.append("temperature должен быть между 0 и 2")
            
        # Edge TTS использует строковые параметры, не проверяем диапазоны
        
        if self.audio.sample_rate not in [8000, 16000, 22050, 24000, 44100, 48000]:
            errors.append("sample_rate должен быть одним из: 8000, 16000, 22050, 24000, 44100, 48000")

        if self.server.build != self.server.version:
            errors.append("SERVER_BUILD должен совпадать с SERVER_VERSION")

        if self.update.default_version != self.server.version:
            errors.append("Update.default_version должен совпадать с SERVER_VERSION")

        if self.update.default_build != self.server.build:
            errors.append("Update.default_build должен совпадать с SERVER_BUILD")

        # Выводим предупреждения
        for error in errors:
            logger.warning(f"⚠️ {error}")
        
        if errors:
            logger.warning("⚠️ Конфигурация имеет предупреждения, но система может работать")
    
    def get_module_config(self, module_name: str) -> Dict[str, Any]:
        """
        Получение конфигурации для конкретного модуля

        Args:
            module_name: Имя модуля

        Returns:
            Словарь с конфигурацией модуля
        """
        config_mapping = {
            'database': self.database.__dict__,
            'grpc': self.grpc.__dict__,
            'http': self.http.__dict__,
            'audio': self.audio.__dict__,
            'text_processing': self.text_processing.__dict__,
            'memory': self.memory.__dict__,
            'session': self.session.__dict__,
            'interrupt': self.interrupt.__dict__,
            'workflow': self.workflow.__dict__,
            'update': self.update.__dict__,
            'server': self.server.__dict__,
            'logging': self.logging.__dict__,
            'browser_use': self.browser_use.__dict__,
            'payment_use': self.payment_use.__dict__,
            'payment_use': self.payment_use.__dict__,
            'subscription': self.subscription.__dict__,
            'whatsapp': self.whatsapp.__dict__
        }

        return config_mapping.get(module_name, {})

    def get_workflow_thresholds(self) -> WorkflowConfig:
        """Возвращает конфигурацию потокового workflow"""

        return self.workflow

    def get_update_service_config(self) -> UpdateServiceConfig:
        """Возвращает конфигурацию сервиса обновлений"""

        return self.update

    def get_server_metadata(self) -> ServerMetadataConfig:
        """Возвращает метаданные сервера"""

        return self.server

    def is_feature_enabled(self, feature_name: str) -> bool:
        """
        Проверка, включен ли фича-флаг
        
        Args:
            feature_name: Имя фича-флага
            
        Returns:
            True если фича включена, False иначе
        """
        if not hasattr(self, 'features'):
            return False
        
        feature_map = {
            'use_module_coordinator': self.features.use_module_coordinator,
            'use_workflow_integrations': self.features.use_workflow_integrations,
            'use_fallback_manager': self.features.use_fallback_manager
        }
        
        return feature_map.get(feature_name, False)
    
    def is_kill_switch_active(self, kill_switch_name: str) -> bool:
        """
        Проверка, активен ли kill-switch
        
        Args:
            kill_switch_name: Имя kill-switch
            
        Returns:
            True если kill-switch активен, False иначе
        """
        if not hasattr(self, 'kill_switches'):
            return False
        
        kill_switch_map = {
            'disable_module_coordinator': self.kill_switches.disable_module_coordinator,
            'disable_workflow_integrations': self.kill_switches.disable_workflow_integrations
        }
        
        return kill_switch_map.get(kill_switch_name, False)
    
    def get_provider_config(self, provider_name: str) -> Dict[str, Any]:
        """
        Получение конфигурации для конкретного провайдера
        
        Args:
            provider_name: Имя провайдера
            
        Returns:
            Словарь с конфигурацией провайдера
        """
        provider_configs = {
            'langchain': {
                'api_key': self.text_processing.gemini_api_key,
                'model': self.text_processing.langchain_model,
                'temperature': self.text_processing.temperature,
                'max_tokens': self.text_processing.max_tokens,
                'tools': self.text_processing.tools,
                'system_prompt': self.text_processing.gemini_system_prompt,
                'image_mime_type': self.text_processing.image_mime_type,
                'image_max_size': self.text_processing.image_max_size,
            },
            'edge_tts': {
                'voice_name': self.audio.edge_tts_voice_name,
                'rate': self.audio.edge_tts_rate,
                'volume': self.audio.edge_tts_volume,
                'pitch': self.audio.edge_tts_pitch,
                'audio_format': self.audio.audio_format,
                'sample_rate': self.audio.sample_rate,
                'channels': self.audio.channels,
                'bits_per_sample': self.audio.bits_per_sample,
                'timeout': self.text_processing.request_timeout
            },
            'postgresql': {
                'host': self.database.host,
                'port': self.database.port,
                'database': self.database.name,
                'user': self.database.user,
                'password': self.database.password
            }
        }
        
        return provider_configs.get(provider_name, {})
    
    def get_fallback_config(self) -> Dict[str, Any]:
        """
        Получение конфигурации fallback менеджера
        
        Returns:
            Словарь с конфигурацией fallback
        """
        return {
            'timeout': self.text_processing.fallback_timeout,
            'circuit_breaker_threshold': self.text_processing.circuit_breaker_threshold,
            'circuit_breaker_timeout': self.text_processing.circuit_breaker_timeout,
            'max_concurrent_requests': self.text_processing.max_concurrent_requests
        }
    
    def get_streaming_config(self) -> Dict[str, Any]:
        """
        Получение конфигурации streaming
        
        Returns:
            Словарь с конфигурацией streaming
        """
        return {
            'chunk_size': self.audio.streaming_chunk_size,
            'enabled': self.audio.streaming_enabled,
            'sample_rate': self.audio.sample_rate,
            'channels': self.audio.channels,
            'bits_per_sample': self.audio.bits_per_sample
        }
    
    def save_to_yaml(self, file_path: Union[str, Path]) -> None:
        """
        Сохранение конфигурации в YAML файл
        
        Args:
            file_path: Путь к файлу
        """
        config_dict = {
            'database': self.database.__dict__,
            'grpc': self.grpc.__dict__,
            'http': self.http.__dict__,
            'audio': self.audio.__dict__,
            'text_processing': self.text_processing.__dict__,
            'memory': self.memory.__dict__,
            'session': self.session.__dict__,
            'interrupt': self.interrupt.__dict__,
            'workflow': self.workflow.__dict__,
            'update': self.update.__dict__,
            'server': self.server.__dict__,
            'logging': self.logging.__dict__,
            'features': self.features.__dict__,
            'kill_switches': self.kill_switches.__dict__,
            'backpressure': self.backpressure.__dict__,
            'browser_use': self.browser_use.__dict__,
            'payment_use': self.payment_use.__dict__
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f, default_flow_style=False, allow_unicode=True)
        
        logger.info(f"✅ Конфигурация сохранена в {file_path}")
    
    @classmethod
    def load_from_yaml(cls, file_path: Union[str, Path]) -> 'UnifiedServerConfig':
        """
        Загрузка конфигурации из YAML файла
        
        Args:
            file_path: Путь к файлу
            
        Returns:
            Экземпляр UnifiedServerConfig
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            loaded_data = yaml.safe_load(f)
        
        # Убеждаемся, что загруженные данные - это словарь
        if not isinstance(loaded_data, dict):
            if loaded_data is None:
                loaded_data = {}
            else:
                raise ValueError(f"YAML файл должен содержать словарь, получен {type(loaded_data).__name__}")
        
        config_dict: Dict[str, Any] = loaded_data
        
        # Создаем экземпляры конфигураций из словаря
        database = DatabaseConfig(**config_dict.get('database', {}))
        grpc = GrpcConfig(**config_dict.get('grpc', {}))
        http = HttpConfig(**config_dict.get('http', {}))
        audio = AudioConfig(**config_dict.get('audio', {}))
        text_processing = TextProcessingConfig(**config_dict.get('text_processing', {}))
        memory = MemoryConfig(**config_dict.get('memory', {}))
        session = SessionConfig(**config_dict.get('session', {}))
        interrupt = InterruptConfig(**config_dict.get('interrupt', {}))
        workflow = WorkflowConfig(**config_dict.get('workflow', {}))
        update = UpdateServiceConfig(**config_dict.get('update', {}))
        server_meta = ServerMetadataConfig(**config_dict.get('server', {}))
        logging_config = LoggingConfig(**config_dict.get('logging', {}))
        features = FeaturesConfig(**config_dict.get('features', {}))
        kill_switches = KillSwitchesConfig(**config_dict.get('kill_switches', {}))
        browser_use = BrowserUseConfig(**config_dict.get('browser_use', {}))
        payment_use = PaymentUseConfig(**config_dict.get('payment_use', {}))
        whatsapp = WhatsappConfig(**config_dict.get('whatsapp', {}))
        
        # Backpressure config с учетом окружения
        env = os.getenv('NEXY_ENV', 'prod').lower()
        if env == 'dev':
            backpressure = BackpressureConfig.from_env_dev()
        elif env == 'stage':
            backpressure = BackpressureConfig.from_env_stage()
        else:
            backpressure = BackpressureConfig(**config_dict.get('backpressure', {}))
        
        return cls(
            database=database,
            grpc=grpc,
            http=http,
            audio=audio,
            text_processing=text_processing,
            memory=memory,
            session=session,
            interrupt=interrupt,
            workflow=workflow,
            update=update,
            server=server_meta,
            logging=logging_config,
            features=features,
            kill_switches=kill_switches,
            backpressure=backpressure,
            browser_use=browser_use,
            payment_use=payment_use,
            whatsapp=whatsapp
        )
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение статуса всей конфигурации
        
        Returns:
            Словарь со статусом конфигурации
        """
        return {
            'database': {
                'host': self.database.host,
                'port': self.database.port,
                'name': self.database.name,
                'user': self.database.user,
                'password_set': bool(self.database.password)
            },
            'grpc': self.grpc.__dict__,
            'http': self.http.__dict__,
            'audio': {
                'sample_rate': self.audio.sample_rate,
                'chunk_size': self.audio.chunk_size,
                'format': self.audio.format,
                'edge_tts_voice_name': self.audio.edge_tts_voice_name,
                'edge_tts_rate': self.audio.edge_tts_rate,
                'edge_tts_volume': self.audio.edge_tts_volume,
                'edge_tts_pitch': self.audio.edge_tts_pitch,
                'streaming_enabled': self.audio.streaming_enabled
            },
            'text_processing': {
                'gemini_api_key_set': bool(self.text_processing.gemini_api_key),
                'langchain_model': self.text_processing.langchain_model,
                'temperature': self.text_processing.temperature,
                'max_tokens': self.text_processing.max_tokens,
                'max_concurrent_requests': self.text_processing.max_concurrent_requests
            },
            'memory': {
                'gemini_api_key_set': bool(self.memory.gemini_api_key),
                'max_short_term_memory_size': self.memory.max_short_term_memory_size,
                'max_long_term_memory_size': self.memory.max_long_term_memory_size,
                'memory_timeout': self.memory.memory_timeout
            },
            'session': self.session.__dict__,
            'interrupt': self.interrupt.__dict__,
            'workflow': self.workflow.__dict__,
            'update': self.update.__dict__,
            'server': self.server.__dict__,
            'logging': self.logging.__dict__,
            'features': self.features.__dict__,
            'kill_switches': self.kill_switches.__dict__,
            'backpressure': self.backpressure.__dict__,
            'browser_use': self.browser_use.__dict__,
            'payment_use': self.payment_use.__dict__
        }

# Глобальный экземпляр конфигурации
_config_instance: Optional[UnifiedServerConfig] = None

def get_config() -> UnifiedServerConfig:
    """
    Получение глобального экземпляра конфигурации
    
    Returns:
        Экземпляр UnifiedServerConfig
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = UnifiedServerConfig()
        logger.info("✅ Централизованная конфигурация инициализирована")
    return _config_instance

def reload_config() -> UnifiedServerConfig:
    """
    Перезагрузка конфигурации из переменных окружения
    
    Returns:
        Новый экземпляр UnifiedServerConfig
    """
    global _config_instance
    _config_instance = UnifiedServerConfig()
    logger.info("✅ Конфигурация перезагружена")
    return _config_instance

if __name__ == "__main__":
    # Тестирование конфигурации
    config = get_config()
    print("📊 Статус конфигурации:")
    status = config.get_status()
    
    for section, values in status.items():
        print(f"\n🔧 {section.upper()}:")
        for key, value in values.items():
            print(f"  {key}: {value}")
    
    # Сохраняем пример конфигурации
    config.save_to_yaml("server/config/unified_config.yaml")
    print("\n✅ Пример конфигурации сохранен в server/config/unified_config.yaml")
