"""
Единый загрузчик конфигурации Nexy AI Assistant
Автоматически синхронизирует все настройки из unified_config.yaml

Thread-safe Singleton: используйте UnifiedConfigLoader.get_instance() или
импортируйте глобальный unified_config для доступа к конфигурации.
"""

import yaml
import os
import sys
import logging
import threading
from pathlib import Path
from typing import Dict, Any, Optional, Union
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class AppConfig:
    """Основные настройки приложения"""
    name: str
    version: str
    debug: bool
    bundle_id: str
    team_id: str

@dataclass
class GrpcServerConfig:
    """Конфигурация gRPC сервера"""
    host: str
    port: int
    ssl: bool
    timeout: int
    retry_attempts: int
    retry_delay: float
    ssl_verify: bool = True  # NEW: Проверка SSL сертификата
    use_http2: bool = True  # NEW: Использовать HTTP/2 (ALPN h2)
    keepalive: bool = True  # NEW: Включить keepalive
    grpc_path: Optional[str] = None  # NEW: Путь для Nginx reverse proxy

@dataclass
class NetworkConfig:
    """Сетевые настройки"""
    grpc_servers: Dict[str, GrpcServerConfig]
    appcast: Dict[str, Any]
    connection_check_interval: int
    auto_fallback: bool
    ping_timeout: int
    ping_hosts: list

@dataclass
class LoggingConfig:
    """Настройки логирования"""
    level: str
    file: str
    error_file: str
    max_size: str
    backup_count: int
    format: str
    loggers: Dict[str, str]

@dataclass
class KeyboardConfig:
    """Конфигурация клавиатуры - все значения загружаются из unified_config.yaml"""
    key_to_monitor: str
    short_press_threshold: float
    long_press_threshold: float
    event_cooldown: float
    hold_check_interval: float
    debounce_time: float
    backend: str
    combo_timeout_sec: float = 120.0  # Максимальное время активной комбинации (2 мин для длинных записей)
    key_state_timeout_sec: float = 60.0  # Максимальное время удержания отдельной клавиши (1 мин)

@dataclass
class InputProcessingConfig:
    """Конфигурация обработки ввода"""
    keyboard: KeyboardConfig
    enable_keyboard_monitoring: bool = True
    auto_start: bool = True
    keyboard_backend: str = "auto"
    min_recording_duration_sec: float = 0.6
    playback_idle_grace_sec: float = 0.3
    playback_wait_timeout_sec: float = 5.0
    recording_prestart_delay_sec: float = 0.3
    mic_reset_timeout_sec: float = 60.0

@dataclass
class OpenAppActionConfig:
    """Конфигурация действий открытия приложений"""
    enabled: bool = False  # По умолчанию выключено для безопасности
    timeout_sec: float = 10.0
    allowed_apps: Optional[list] = None  # None или пустой список = все разрешены
    binary: str = "/usr/bin/open"
    speak_errors: bool = True
    use_server_tts: bool = False
    
    def __post_init__(self):
        if self.allowed_apps is None:
            self.allowed_apps = []

class UnifiedConfigLoader:
    """
    Единый загрузчик конфигурации с автоматической синхронизацией.
    
    Thread-safe Singleton Pattern:
    - Используйте UnifiedConfigLoader.get_instance() для явного получения
    - Или import unified_config из этого модуля
    - Прямой вызов UnifiedConfigLoader() также вернёт singleton
    """
    
    _instance: Optional["UnifiedConfigLoader"] = None
    _lock: threading.Lock = threading.Lock()
    _initialized: bool = False
    
    def __new__(cls, config_file: Optional[Union[str, Path]] = None) -> "UnifiedConfigLoader":
        """Thread-safe singleton: возвращает единственный экземпляр."""
        if cls._instance is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def get_instance(cls, config_file: Optional[Union[str, Path]] = None) -> "UnifiedConfigLoader":
        """
        Явный метод получения singleton экземпляра.
        
        Рекомендуется использовать этот метод для clarity.
        """
        return cls(config_file)
    
    @classmethod
    def reset_instance(cls) -> None:
        """
        Сбрасывает singleton (только для тестов!).
        
        WARNING: Не использовать в production коде.
        """
        with cls._lock:
            cls._instance = None
            cls._initialized = False
    
    def __init__(self, config_file: Optional[Union[str, Path]] = None):
        # Предотвращаем повторную инициализацию singleton
        if UnifiedConfigLoader._initialized:
            return
        
        # По умолчанию используем файл, расположенный рядом с этим модулем,
        # чтобы не зависеть от текущего рабочего каталога запуска.
        if config_file is None:
            self.config_file = Path(__file__).resolve().parent / "unified_config.yaml"
        else:
            self.config_file = Path(config_file)
        self._config_cache: Optional[Dict[str, Any]] = None
        self._last_modified: Optional[float] = None
        self._environment: str = self._detect_environment()
        
        UnifiedConfigLoader._initialized = True
        logger.debug("UnifiedConfigLoader singleton initialized")

    
    def _load_config(self) -> Dict[str, Any]:
        """Загружает конфигурацию с проверкой изменений"""
        if self._config_cache is None or self._is_config_modified():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self._config_cache = yaml.safe_load(f) or {}
            self._last_modified = self.config_file.stat().st_mtime
        return self._config_cache or {}
    
    def _is_config_modified(self) -> bool:
        """Проверяет, был ли файл конфигурации изменен"""
        if not self.config_file.exists():
            return True
        current_mtime = self.config_file.stat().st_mtime
        return self._last_modified is None or current_mtime > self._last_modified
    
    def reload(self):
        """Принудительно перезагружает конфигурацию"""
        self._config_cache = None
        self._last_modified = None
    
    # =====================================================
    # ОСНОВНЫЕ НАСТРОЙКИ ПРИЛОЖЕНИЯ
    # =====================================================
    
    def get_app_config(self) -> AppConfig:
        """Получает основные настройки приложения"""
        config = self._load_config()
        app_data = config['app']
        return AppConfig(
            name=app_data['name'],
            version=app_data['version'],
            debug=app_data['debug'],
            bundle_id=app_data['bundle_id'],
            team_id=app_data['team_id']
        )
    
    def get_version(self) -> str:
        """Получает версию приложения (используется везде)"""
        return self.get_app_config().version
    
    def get_bundle_id(self) -> str:
        """Получает Bundle ID приложения"""
        return self.get_app_config().bundle_id
    
    def get_team_id(self) -> str:
        """Получает Team ID для подписи"""
        return self.get_app_config().team_id
    
    # =====================================================
    # СЕТЕВЫЕ НАСТРОЙКИ
    # =====================================================
    
    def get_network_config(self) -> NetworkConfig:
        """Получает сетевые настройки"""
        config = self._load_config()
        
        # Получаем gRPC настройки из секции grpc
        grpc_data = config.get('grpc', {})
        
        # Создаем конфигурации для всех серверов из централизованной конфигурации
        grpc_servers = {}
        servers_config = grpc_data.get('servers', {})
        
        for server_name, server_config in servers_config.items():
            # DEBUG: Log what we're reading from YAML
            ssl_verify_value = server_config.get('ssl_verify', True)
            logger.info(f"🔌 [DEBUG] Loading server '{server_name}' from YAML: ssl_verify={ssl_verify_value}")

            grpc_servers[server_name] = GrpcServerConfig(
                host=server_config.get('host', '127.0.0.1'),
                port=server_config.get('port', 50051),
                ssl=server_config.get('ssl', False),
                timeout=server_config.get('timeout', grpc_data.get('connection_timeout', 30)),
                retry_attempts=server_config.get('retry_attempts', grpc_data.get('retry_attempts', 3)),
                retry_delay=server_config.get('retry_delay', grpc_data.get('retry_delay', 1.0)),
                ssl_verify=ssl_verify_value,  # NEW
                use_http2=server_config.get('use_http2', True),  # NEW
                keepalive=server_config.get('keepalive', True),  # NEW
                grpc_path=server_config.get('grpc_path')  # NEW
            )
        
        # Получаем настройки сети (если есть)
        network_data = config.get('network', {})
        
        return NetworkConfig(
            grpc_servers=grpc_servers,
            appcast=network_data.get('appcast', {'base_url': 'https://updates.nexy.ai'}),
            connection_check_interval=network_data.get('connection_check_interval', 30),
            auto_fallback=network_data.get('auto_fallback', True),
            ping_timeout=network_data.get('ping_timeout', 5),
            ping_hosts=network_data.get('ping_hosts', ['8.8.8.8', '1.1.1.1'])
        )
    
    def get_grpc_config(self, environment: str = "local") -> GrpcServerConfig:
        """Получает конфигурацию gRPC для указанного окружения"""
        network_config = self.get_network_config()
        if environment not in network_config.grpc_servers:
            raise ValueError(f"Environment '{environment}' not found")
        return network_config.grpc_servers[environment]
    
    def get_appcast_url(self) -> str:
        """Получает URL AppCast (используется везде)"""
        network_config = self.get_network_config()
        return network_config.appcast['base_url'] + "/appcast.xml"
    
    def get_grpc_host(self, environment: str = "local") -> str:
        """Получает хост gRPC сервера"""
        return self.get_grpc_config(environment).host
    
    def get_grpc_port(self, environment: str = "local") -> int:
        """Получает порт gRPC сервера"""
        return self.get_grpc_config(environment).port
    
    # =====================================================
    # РАЗРЕШЕНИЯ
    # =====================================================

    def get_permission_config(self) -> Dict[str, Any]:
        """Получает настройки разрешений"""
        config = self._load_config()
        return config.get('permissions', {})

    def get_permission_override_config(self) -> Dict[str, Any]:
        """Возвращает настройку override для разрешений с учетом окружения"""
        config = self._load_config()
        raw_override = config.get('permission_override', {})

        if isinstance(raw_override, bool):
            return {"assume_granted": raw_override}

        if not isinstance(raw_override, dict):
            return {}

        # Поддержка формата с default + окружениями
        if any(isinstance(raw_override.get(key), dict) for key in ('default', self._environment)):
            resolved: Dict[str, Any] = {}

            default_section = raw_override.get('default')
            if isinstance(default_section, dict):
                resolved.update(default_section)

            env_section = raw_override.get(self._environment)
            if isinstance(env_section, dict):
                resolved.update(env_section)

            return resolved

        # Формат legacy (плоский словарь)
        return raw_override

    def get_environment(self) -> str:
        """Возвращает активное окружение (development / production / custom)"""
        return self._environment

    # =====================================================
    # СЛУЖЕБНЫЕ МЕТОДЫ
    # =====================================================

    def _detect_environment(self) -> str:
        """
        Определяет, в каком окружении работает приложение.
        Приоритет:
          1. Переменные окружения NEXY_ENV/NEXY_ENVIRONMENT
          2. Признак упакованного приложения (sys.frozen, .app)
          3. Значение по умолчанию — development
        """
        env_candidate = os.getenv("NEXY_ENV") or os.getenv("NEXY_ENVIRONMENT")
        if env_candidate:
            normalized = env_candidate.strip().lower()
            if normalized in ("prod", "production"):
                env = "production"
            elif normalized in ("dev", "development"):
                env = "development"
            else:
                env = normalized
            logger.debug("UnifiedConfigLoader: environment set via env var -> %s", env)
            return env

        # PyInstaller / py2app ставят sys.frozen
        if getattr(sys, "frozen", False):
            env = "production"
            logger.debug("UnifiedConfigLoader: environment detected as %s (sys.frozen)", env)
            return env

        argv_path = Path(sys.argv[0]).resolve()
        if ".app/Contents/MacOS" in str(argv_path):
            env = "production"
            logger.debug("UnifiedConfigLoader: environment detected as %s (.app launch)", env)
            return env

        env = "development"
        logger.debug("UnifiedConfigLoader: environment defaulted to %s", env)
        return env

    # =====================================================
    # НАСТРОЙКИ ЛОГИРОВАНИЯ
    # =====================================================
    
    def get_logging_config(self) -> LoggingConfig:
        """Получает настройки логирования"""
        config = self._load_config()
        logging_data = config['logging']
        return LoggingConfig(
            level=logging_data['level'],
            file=logging_data['file'],
            error_file=logging_data['error_file'],
            max_size=logging_data['max_size'],
            backup_count=logging_data['backup_count'],
            format=logging_data['format'],
            loggers=logging_data['loggers']
        )
    
    def get_log_file(self) -> str:
        """Получает путь к файлу логов (используется везде)"""
        return self.get_logging_config().file
    
    def get_error_log_file(self) -> str:
        """Получает путь к файлу ошибок"""
        return self.get_logging_config().error_file
    
    # =====================================================
    # ДРУГИЕ НАСТРОЙКИ
    # =====================================================
    
    def get_default_audio_config(self) -> Dict[str, Any]:
        """Получает настройки default_audio"""
        config = self._load_config()
        return config.get('default_audio', {})
    
    def get_audio_config(self) -> Dict[str, Any]:
        """Получает настройки аудио (legacy - для совместимости)"""
        # Возвращаем default_audio конфигурацию
        return self.get_default_audio_config()
    
    def get_speech_playback_config(self) -> Dict[str, Any]:
        """Получает настройки воспроизведения речи"""
        config = self._load_config()
        audio_config = self.get_audio_config()
        speech_playback_config = audio_config.get('speech_playback', {})
        
        # Получаем формат аудио от сервера (централизованный источник истины)
        server_audio_format = config.get('server_audio_format', {
            'sample_rate': 24000,
            'channels': 1,
            'dtype': 'int16'
        })
        
        # 🔍 ИСПРАВЛЕНО: Используем sample_rate из конфига (24000Hz согласно спецификации gRPC)
        # Если sample_rate отличается от server_audio_format, будет выполняться ресемплинг
        # НО: лучше использовать реальный sample_rate из metadata аудио, а не fallback
        playback_sample_rate = speech_playback_config.get('sample_rate', 24000)  # ИСПРАВЛЕНО: было 48000, должно быть 24000
        
        # 🔍 ДИАГНОСТИКА: Логируем загруженный sample_rate
        logger.info(f"🔍 [CONFIG_DIAG] speech_playback sample_rate загружен: {playback_sample_rate}Hz (из конфига: {speech_playback_config.get('sample_rate', 'N/A')})")
        
        return {
            'sample_rate': playback_sample_rate,  # Целевая частота для воспроизведения (24000Hz согласно спецификации)
            'channels': speech_playback_config.get('channels', 1),
            'dtype': speech_playback_config.get('dtype', 'int16'),
            'buffer_size': speech_playback_config.get('buffer_size', 512),
            'max_memory_mb': speech_playback_config.get('max_memory_mb', 50),
            'auto_device_selection': speech_playback_config.get('auto_device_selection', True),
            'auto_output_device_switch': speech_playback_config.get('auto_output_device_switch', True),
            'enable_resampling': speech_playback_config.get('enable_resampling', True),
            # Добавляем формат сервера для справки (используется как fallback при получении данных)
            'server_audio_format': server_audio_format
        }
    
    def get_server_audio_format(self) -> Dict[str, Any]:
        """Получает централизованный формат аудио от сервера (источник истины)"""
        config = self._load_config()
        return config.get('server_audio_format', {
            'sample_rate': 24000,  # 24 kHz согласно спецификации gRPC
            'channels': 1,         # mono
            'dtype': 'int16',       # 16-bit PCM
            'bit_depth': 16,
            'endianness': 'little',
            'format': 'raw_pcm'
        })
    
    def get_stt_config(self) -> Dict[str, Any]:
        """Получает настройки распознавания речи"""
        config = self._load_config()
        return config['stt']

    def get_stt_language(self, default: str = "en-US") -> str:
        """Получает язык распознавания речи (централизованно)"""
        try:
            stt = self.get_stt_config()
            return stt.get('language', default) or default
        except Exception:
            return default
    
    def get_screen_capture_config(self) -> Dict[str, Any]:
        """Получает настройки захвата экрана"""
        config = self._load_config()
        return config['screen_capture']
    
    def get_update_manager_config(self) -> Dict[str, Any]:
        """Получает настройки менеджера обновлений"""
        config = self._load_config()
        update_config = config['update_manager'].copy()
        # Автоматически подставляем AppCast URL
        update_config['appcast_url'] = self.get_appcast_url()
        return update_config
    
    def get_performance_config(self) -> Dict[str, Any]:
        """Получает настройки производительности"""
        config = self._load_config()
        return config['performance']
    
    def get_security_config(self) -> Dict[str, Any]:
        """Получает настройки безопасности"""
        config = self._load_config()
        return config['security']
    
    # =====================================================
    # УТИЛИТЫ ДЛЯ ОБРАТНОЙ СОВМЕСТИМОСТИ
    # =====================================================
    
    def get_legacy_app_config(self) -> Dict[str, Any]:
        """Возвращает конфигурацию в старом формате для обратной совместимости"""
        config = self._load_config()
        
        # Создаем конфигурацию в старом формате
        legacy_config = {
            'app': config['app'],
            'audio': config['audio'],
            'stt': config['stt'],
            'screen_capture': config['screen_capture'],
            'grpc': {
                'config_file': 'config/unified_config.yaml',
                'server_priority': ['local', 'production', 'fallback'],
                'auto_fallback': config['network']['auto_fallback'],
                'connection_check_interval': config['network']['connection_check_interval']
            },
            'logging': config['logging'],
            'accessibility': config['accessibility'],
            'autostart': config['autostart'],
            'performance': config['performance'],
            'security': config['security'],
            'update_manager': self.get_update_manager_config()
        }
        
        return legacy_config

    def get_keyboard_config(self) -> KeyboardConfig:
        """Получает конфигурацию клавиатуры из unified_config.yaml"""
        kbd_cfg = self._load_config().get('integrations', {}).get('keyboard', {})
        
        # Проверяем, что все обязательные поля присутствуют
        required_fields = ['key_to_monitor', 'short_press_threshold', 'long_press_threshold', 
                          'event_cooldown', 'hold_check_interval', 'debounce_time', 'backend']
        
        for field in required_fields:
            if field not in kbd_cfg:
                raise ValueError(f"Отсутствует обязательное поле '{field}' в конфигурации клавиатуры")
        
        # Валидация поддерживаемых клавиш
        key_to_monitor = kbd_cfg['key_to_monitor']
        supported_keys = {'left_shift', 'ctrl_n'}
        if key_to_monitor not in supported_keys:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(
                f"⚠️ Неподдерживаемая клавиша '{key_to_monitor}'. "
                f"Поддерживаемые: {', '.join(supported_keys)}. "
                f"Используется '{key_to_monitor}' (может не работать)."
            )
        
        return KeyboardConfig(
            key_to_monitor=key_to_monitor,
            short_press_threshold=kbd_cfg['short_press_threshold'],
            long_press_threshold=kbd_cfg['long_press_threshold'],
            event_cooldown=kbd_cfg['event_cooldown'],
            hold_check_interval=kbd_cfg['hold_check_interval'],
            debounce_time=kbd_cfg['debounce_time'],
            backend=kbd_cfg['backend'],
            combo_timeout_sec=kbd_cfg.get('combo_timeout_sec', 10.0),
            key_state_timeout_sec=kbd_cfg.get('key_state_timeout_sec', 5.0)
        )

    def get_input_processing_config(self) -> InputProcessingConfig:
        """Получает конфигурацию обработки ввода"""
        input_cfg = self._load_config().get('integrations', {}).get('input_processing', {})
        kbd_cfg = self._load_config().get('integrations', {}).get('keyboard', {})
        return InputProcessingConfig(
            keyboard=self.get_keyboard_config(),
            enable_keyboard_monitoring=input_cfg.get('enable_keyboard_monitoring', True),
            auto_start=input_cfg.get('auto_start', True),
            keyboard_backend=kbd_cfg.get('backend', 'auto'),
            min_recording_duration_sec=float(input_cfg.get('min_recording_duration_sec', 0.6)),
            playback_idle_grace_sec=float(input_cfg.get('playback_idle_grace_sec', 0.3)),
            playback_wait_timeout_sec=float(input_cfg.get('playback_wait_timeout_sec', 5.0)),
            recording_prestart_delay_sec=float(input_cfg.get('recording_prestart_delay_sec', 0.3)),
            mic_reset_timeout_sec=float(input_cfg.get('mic_reset_timeout_sec', 60.0)),
        )

    def get_actions_config(self) -> Dict[str, OpenAppActionConfig]:
        """
        Получает конфигурацию действий.
        
        Returns:
            Словарь с конфигурациями действий, ключ - тип действия (например, "open_app")
        """
        config = self._load_config()
        actions_cfg = config.get('actions', {})
        
        result = {}
        
        # Конфигурация для open_app
        open_app_cfg = actions_cfg.get('open_app', {})
        result['open_app'] = OpenAppActionConfig(
            enabled=bool(open_app_cfg.get('enabled', False)),
            timeout_sec=float(open_app_cfg.get('timeout_sec', 10.0)),
            allowed_apps=list(open_app_cfg.get('allowed_apps', [])) if open_app_cfg.get('allowed_apps') else [],
            binary=str(open_app_cfg.get('binary', '/usr/bin/open')),
            speak_errors=bool(open_app_cfg.get('speak_errors', True)),
            use_server_tts=bool(open_app_cfg.get('use_server_tts', False)),
        )
        
        # Конфигурация для close_app (используем тот же тип, так как структура похожа)
        close_app_cfg = actions_cfg.get('close_app', {})
        result['close_app'] = OpenAppActionConfig(
            enabled=bool(close_app_cfg.get('enabled', False)),
            timeout_sec=float(close_app_cfg.get('timeout_sec', 10.0)),
            allowed_apps=[],  # close_app не использует whitelist
            binary="",  # close_app не использует binary (использует MCP)
            speak_errors=bool(close_app_cfg.get('speak_errors', True)),
            use_server_tts=bool(close_app_cfg.get('use_server_tts', False)),
        )
        
        return result
    
    def get_mcp_config(self) -> Dict[str, Dict[str, Any]]:
        """
        Получает конфигурацию MCP серверов.
        
        Returns:
            Словарь с конфигурациями MCP серверов, ключ - тип действия (например, "open_app", "close_app")
        """
        config = self._load_config()
        mcp_cfg = config.get('mcp', {})
        
        result = {}
        
        # Конфигурация для open_app MCP сервера
        open_app_mcp = mcp_cfg.get('open_app', {})
        result['open_app'] = {
            'server_path': str(open_app_mcp.get('server_path', '')),
            'enabled': bool(open_app_mcp.get('enabled', True)),
            'timeout_sec': float(open_app_mcp.get('timeout_sec', 10.0)),
        }
        
        # Конфигурация для close_app MCP сервера
        close_app_mcp = mcp_cfg.get('close_app', {})
        result['close_app'] = {
            'server_path': str(close_app_mcp.get('server_path', '')),
            'enabled': bool(close_app_mcp.get('enabled', True)),
            'timeout_sec': float(close_app_mcp.get('timeout_sec', 10.0)),
        }
        
        return result

    def get_tray_config(self) -> Dict[str, Any]:
        """Получает конфигурацию трея"""
        config = self._load_config()
        return config.get('tray', {})

    def get_hardware_id_config(self) -> Dict[str, Any]:
        """Получает конфигурацию hardware_id"""
        config = self._load_config()
        return config.get('integrations', {}).get('hardware_id', {})

# Глобальный экземпляр загрузчика
unified_config = UnifiedConfigLoader()

# Удобные функции для быстрого доступа
def get_version() -> str:
    """Получает версию приложения"""
    return unified_config.get_version()

def get_appcast_url() -> str:
    """Получает URL AppCast"""
    return unified_config.get_appcast_url()

def get_grpc_host(environment: str = "local") -> str:
    """Получает хост gRPC сервера"""
    return unified_config.get_grpc_host(environment)

def get_grpc_port(environment: str = "local") -> int:
    """Получает порт gRPC сервера"""
    return unified_config.get_grpc_port(environment)

def get_log_file() -> str:
    """Получает путь к файлу логов"""
    return unified_config.get_log_file()

def get_bundle_id() -> str:
    """Получает Bundle ID"""
    return unified_config.get_bundle_id()

def get_team_id() -> str:
    """Получает Team ID"""
    return unified_config.get_team_id()
