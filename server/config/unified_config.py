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
    sample_rate: int = 48000
    chunk_size: int = 1024
    format: str = "int16"
    channels: int = 1
    bits_per_sample: int = 16
    
    # Azure TTS настройки
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
            sample_rate=int(os.getenv('SAMPLE_RATE', '48000')),
            chunk_size=int(os.getenv('CHUNK_SIZE', '1024')),
            format=os.getenv('AUDIO_FORMAT', 'int16'),
            channels=int(os.getenv('AUDIO_CHANNELS', '1')),
            bits_per_sample=int(os.getenv('AUDIO_BITS_PER_SAMPLE', '16')),
            azure_speech_key=os.getenv('AZURE_SPEECH_KEY', ''),
            azure_speech_region=os.getenv('AZURE_SPEECH_REGION', ''),
            azure_voice_name=os.getenv('AZURE_VOICE_NAME', 'en-US-AriaNeural'),
            azure_voice_style=os.getenv('AZURE_VOICE_STYLE', 'friendly'),
            azure_speech_rate=float(os.getenv('AZURE_SPEECH_RATE', '1.0')),
            azure_speech_pitch=float(os.getenv('AZURE_SPEECH_PITCH', '1.0')),
            azure_speech_volume=float(os.getenv('AZURE_SPEECH_VOLUME', '1.0')),
            azure_audio_format=os.getenv('AZURE_AUDIO_FORMAT', 'riff-48khz-16bit-mono-pcm'),
            streaming_chunk_size=int(os.getenv('STREAMING_CHUNK_SIZE', '4096')),
            streaming_enabled=os.getenv('STREAMING_ENABLED', 'true').lower() == 'true'
        )

@dataclass
class TextProcessingConfig:
    """Конфигурация обработки текста"""
    gemini_api_key: str = ""
    
    # Live API настройки
    gemini_live_model: str = "gemini-live-2.5-flash-preview"
    gemini_live_temperature: float = 0.7
    gemini_live_max_tokens: int = 2048
    gemini_live_tools: list = field(default_factory=lambda: ['google_search'])
    gemini_system_prompt: str = (
        "You are Nexy Assistant — a friendly, empathetic, and highly concise AI designed for blind and low-vision users on macOS.\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "**CRITICAL: Output Format Requirements**\n\n"
        "You MUST always respond with a **single valid JSON object** starting with `{` and ending with `}`.\n\n"
        "- Output ONLY the raw JSON object, NO markdown code fences (```json ... ```), NO text before/after\n\n"
        "- The response must be parseable as JSON directly, without any preprocessing\n\n"
        "- NEVER include markdown formatting, code blocks, explanations, or extra text\n\n"
        "**WRONG (DO NOT DO THIS):**\n"
        "```json\n{\"text\": \"Hello\"}\n```\n"
        "Here is the response: {\"text\": \"Hello\"}\n\n"
        "**CORRECT:**\n"
        "{\"text\": \"Hello\"}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Adaptive Pre-Analyzer — DO NOT OUTPUT]\n\n"
        "Before generating the JSON response, classify the user request:\n\n"
        "──────────────────────\n\n"
        "1. Action Intent (System Actions)\n\n"
        "User wants to perform an action (e.g., opening an application).\n\n"
        "If user asks to open/launch an app:\n"
        "- Use **Action JSON format** with:\n"
        "  • \"command\": \"open_app\"\n"
        "  • \"args\": {\"app_name\": \"<exact macOS app name>\"}\n"
        "  • \"session_id\": <MUST reuse from request, REQUIRED, never null>\n"
        "  • \"text\": short confirmation (\"Opening Safari now.\")\n\n"
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
        "Request involves online information (\"search\", \"find\", \"Google\", \"price\", \"latest\", \"compare\", \"news\", \"current\", \"where to buy\", product names, events, years like 2024/2025).\n"
        "- ALWAYS perform a **real web search** using the web search tool\n"
        "- NEVER guess or simulate\n"
        "- Use **Text-only JSON format** with:\n"
        "  • 1–3 verified key results\n"
        "  • Optional reliable source\n"
        "  • If nothing found → say that and suggest refining the query\n"
        "- Do NOT output steps or instructions for WebSearch results\n\n"
        "──────────────────────\n\n"
        "4. Ambiguous Intent\n\n"
        "If unclear:\n"
        "- Use **Text-only JSON format**\n"
        "- Provide best short answer + ask 1 clarifying question: \"Would you like me to describe it or perform an action?\"\n\n"
        "──────────────────────\n\n"
        "5. SmallTalk\n\n"
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
        "1) Describe\n"
        "2) WebSearch\n"
        "3) Action\n"
        "4) SmallTalk\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "[Action Output Format — DO NOT OUTPUT]\n\n"
        "You MUST use **one of the two formats below**:\n\n"
        "──────────────\n\n"
        "1) Action Response (when performing an action, e.g. opening an app)\n\n"
        "{\n"
        "  \"session_id\": \"<MUST use session_id from request, REQUIRED>\",\n"
        "  \"command\": \"open_app\",\n"
        "  \"args\": {\n"
        "    \"app_name\": \"Calculator\"\n"
        "  },\n"
        "  \"text\": \"Opening Calculator.\"\n"
        "}\n\n"
        "Rules:\n"
        "- session_id: REQUIRED, must be the exact session_id from the request (never null)\n"
        "- text: 1–3 short sentences\n"
        "- args must contain app_name\n"
        "- NEVER add any extra fields\n"
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
    image_format: str = "jpeg"
    image_mime_type: str = "image/jpeg"
    image_max_size: int = 10 * 1024 * 1024  # 10MB
    streaming_chunk_size: int = 8192
    
    
    # Fallback настройки
    fallback_timeout: int = 30
    circuit_breaker_threshold: int = 3
    circuit_breaker_timeout: int = 300
    
    # Производительность
    max_concurrent_requests: int = 10
    request_timeout: int = 60
    
    @classmethod
    def from_env(cls) -> 'TextProcessingConfig':
        return cls(
            gemini_api_key=os.getenv('GEMINI_API_KEY', ''),
            gemini_live_model=os.getenv('GEMINI_LIVE_MODEL', 'gemini-live-2.5-flash-preview'),
            gemini_live_temperature=float(os.getenv('GEMINI_LIVE_TEMPERATURE', '0.7')),
            gemini_live_max_tokens=int(os.getenv('GEMINI_LIVE_MAX_TOKENS', '2048')),
            gemini_live_tools=os.getenv('GEMINI_LIVE_TOOLS', 'google_search').split(',') if os.getenv('GEMINI_LIVE_TOOLS') else ['google_search'],
            gemini_system_prompt=os.getenv('GEMINI_SYSTEM_PROMPT', cls.gemini_system_prompt),
            image_format=os.getenv('IMAGE_FORMAT', 'jpeg'),
            image_mime_type=os.getenv('IMAGE_MIME_TYPE', 'image/jpeg'),
            image_max_size=int(os.getenv('IMAGE_MAX_SIZE', str(10 * 1024 * 1024))),
            streaming_chunk_size=int(os.getenv('STREAMING_CHUNK_SIZE', '8192')),
            fallback_timeout=int(os.getenv('FALLBACK_TIMEOUT', '30')),
            circuit_breaker_threshold=int(os.getenv('CIRCUIT_BREAKER_THRESHOLD', '3')),
            circuit_breaker_timeout=int(os.getenv('CIRCUIT_BREAKER_TIMEOUT', '300')),
            max_concurrent_requests=int(os.getenv('MAX_CONCURRENT_REQUESTS', '10')),
            request_timeout=int(os.getenv('REQUEST_TIMEOUT', '60'))
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

    stream_min_chars: int = 15
    stream_min_words: int = 3
    stream_first_sentence_min_words: int = 2
    stream_punct_flush_strict: bool = True
    force_flush_max_chars: int = 0

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
            force_flush_max_chars=int(os.getenv('STREAM_FORCE_FLUSH_MAX_CHARS', '0') or 0)
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
    default_version: str = '1.0.1'
    default_build: str = '1.0.1'
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
            default_version=os.getenv('SERVER_VERSION', '1.0.1'),
            default_build=os.getenv('SERVER_BUILD', os.getenv('SERVER_VERSION', '1.0.1')),
            default_arch=os.getenv('UPDATE_DEFAULT_ARCH', 'universal2'),
            default_min_os=os.getenv('UPDATE_DEFAULT_MIN_OS', '11.0')
        )


@dataclass
class ServerMetadataConfig:
    """Метаданные сервера"""

    version: str = '1.0.1'
    build: str = '1.0.1'
    channel: str = 'stable'

    @classmethod
    def from_env(cls) -> 'ServerMetadataConfig':
        version = os.getenv('SERVER_VERSION', '1.0.1')
        build = os.getenv('SERVER_BUILD', version)
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
    """Конфигурация backpressure для стримов"""
    max_concurrent_streams: int = 50
    idle_timeout_seconds: int = 300
    max_message_rate_per_second: int = 10
    grace_period_seconds: int = 30
    
    @classmethod
    def from_env(cls) -> 'BackpressureConfig':
        return cls(
            max_concurrent_streams=int(os.getenv('BACKPRESSURE_MAX_STREAMS', '50')),
            idle_timeout_seconds=int(os.getenv('BACKPRESSURE_IDLE_TIMEOUT', '300')),
            max_message_rate_per_second=int(os.getenv('BACKPRESSURE_MAX_RATE', '10')),
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
            idle_timeout_seconds=300,
            max_message_rate_per_second=10,
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
    
    def __post_init__(self):
        """Пост-инициализация для валидации"""
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Валидация всей конфигурации"""
        errors = []
        
        # Проверяем критические настройки
        if not self.text_processing.gemini_api_key:
            errors.append("GEMINI_API_KEY не установлен")
        
        if not self.audio.azure_speech_key:
            errors.append("AZURE_SPEECH_KEY не установлен")
            
        if not self.audio.azure_speech_region:
            errors.append("AZURE_SPEECH_REGION не установлен")
        
        # Проверяем диапазоны значений
        if not (0 <= self.text_processing.gemini_live_temperature <= 2):
            errors.append("gemini_live_temperature должен быть между 0 и 2")
            
        if not (0.5 <= self.audio.azure_speech_rate <= 2.0):
            errors.append("azure_speech_rate должен быть между 0.5 и 2.0")
            
        if self.audio.sample_rate not in [8000, 16000, 22050, 44100, 48000]:
            errors.append("sample_rate должен быть одним из: 8000, 16000, 22050, 44100, 48000")

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
            'logging': self.logging.__dict__
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
            'gemini_live': {
                'api_key': self.text_processing.gemini_api_key,
                'model': self.text_processing.gemini_live_model,
                'temperature': self.text_processing.gemini_live_temperature,
                'max_tokens': self.text_processing.gemini_live_max_tokens,
                'timeout': self.text_processing.request_timeout
            },
            'azure_tts': {
                'speech_key': self.audio.azure_speech_key,
                'speech_region': self.audio.azure_speech_region,
                'voice_name': self.audio.azure_voice_name,
                'voice_style': self.audio.azure_voice_style,
                'speech_rate': self.audio.azure_speech_rate,
                'speech_pitch': self.audio.azure_speech_pitch,
                'speech_volume': self.audio.azure_speech_volume,
                'audio_format': self.audio.azure_audio_format,
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
            'backpressure': self.backpressure.__dict__
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
            config_dict = yaml.safe_load(f)
        
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
            backpressure=backpressure
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
                'azure_speech_key_set': bool(self.audio.azure_speech_key),
                'azure_speech_region_set': bool(self.audio.azure_speech_region),
                'azure_voice_name': self.audio.azure_voice_name,
                'streaming_enabled': self.audio.streaming_enabled
            },
            'text_processing': {
                'gemini_api_key_set': bool(self.text_processing.gemini_api_key),
                'gemini_live_model': self.text_processing.gemini_live_model,
                'gemini_live_temperature': self.text_processing.gemini_live_temperature,
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
            'backpressure': self.backpressure.__dict__
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
    config.save_to_yaml("server/config/unified_config_example.yaml")
    print("\n✅ Пример конфигурации сохранен в server/config/unified_config_example.yaml")
