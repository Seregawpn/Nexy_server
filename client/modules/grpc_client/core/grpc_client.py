"""
Основной gRPC клиент с модульной архитектурой
"""

import asyncio
import logging
from typing import Optional, Dict, Any, AsyncGenerator, Tuple, List
import importlib
import sys
from pathlib import Path
from datetime import datetime

import numpy as np

from integration.utils.resource_path import get_resource_path

from .types import ServerConfig, RetryConfig, HealthCheckConfig, RetryStrategy
from .retry_manager import RetryManager
from .connection_manager import ConnectionManager

logger = logging.getLogger(__name__)


class GrpcClient:  # type: ignore[no-redef]
    """Основной gRPC клиент с модульной архитектурой"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or self._create_default_config()
        
        # Модульные компоненты
        self.connection_manager = ConnectionManager()
        self.retry_manager = RetryManager(
            RetryConfig(
                max_attempts=self.config.get('max_retry_attempts', 3),
                base_delay=self.config.get('retry_delay', 1.0),
                strategy=RetryStrategy.EXPONENTIAL  # Используем enum вместо строки
            )
        )
        
        # Инициализация
        self._initialize_servers()
        self._setup_callbacks()
        
        # Устанавливаем сервер по умолчанию из конфигурации
        self._set_default_server()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Создает конфигурацию по умолчанию из централизованной системы"""
        try:
            # Загружаем конфигурацию из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            grpc_data = config.get('grpc', {})
            servers_config = grpc_data.get('servers', {})
            
            # Преобразуем конфигурацию в формат, ожидаемый GrpcClient
            servers = {}
            for server_name, server_config in servers_config.items():
                server_dict = {
                    'address': server_config.get('host', '127.0.0.1'),
                    'port': server_config.get('port', 50051),
                    'use_ssl': server_config.get('ssl', False),
                    'ssl_verify': server_config.get('ssl_verify', True),
                    'grpc_path': server_config.get('grpc_path'),
                    'use_http2': server_config.get('use_http2', True),
                    'timeout': server_config.get('timeout', grpc_data.get('connection_timeout', 30)),
                    'retry_attempts': server_config.get('retry_attempts', grpc_data.get('retry_attempts', 3)),
                    'retry_delay': server_config.get('retry_delay', grpc_data.get('retry_delay', 1.0)),
                    'keepalive': server_config.get('keepalive', True)
                }
                # DEBUG: Логируем конфигурацию каждого сервера
                logger.info(f"🔌 [DEBUG] Loaded server '{server_name}': {server_dict['address']}:{server_dict['port']}, ssl={server_dict['use_ssl']}, ssl_verify={server_dict['ssl_verify']}")
                servers[server_name] = server_dict
            
            return {
                'servers': servers,
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': grpc_data.get('connection_timeout', 10),
                'max_retry_attempts': grpc_data.get('retry_attempts', 3),
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
            
        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить централизованную конфигурацию: {e}")
            # Fallback к минимальной конфигурации
            return {
                'servers': {
                    'local': {
                        'address': '127.0.0.1',
                        'port': 50051,
                        'use_ssl': False,
                        'timeout': 30,
                        'retry_attempts': 3,
                        'retry_delay': 1.0
                    }
                },
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': 10,
                'max_retry_attempts': 3,
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
    
    def _initialize_servers(self):
        """Инициализирует конфигурации серверов"""
        try:
            servers_config = self.config.get('servers', {})
            for name, server_config in servers_config.items():
                # DEBUG: Log what we're reading from config dict
                ssl_verify_from_config = server_config.get('ssl_verify', True)
                logger.info(f"🔌 [DEBUG] _initialize_servers creating ServerConfig for '{name}': ssl_verify={ssl_verify_from_config}")

                config = ServerConfig(
                    address=server_config['address'],
                    port=server_config['port'],
                    use_ssl=server_config.get('use_ssl', False),
                    ssl_verify=ssl_verify_from_config,  # NEW: Add ssl_verify
                    grpc_path=server_config.get('grpc_path'),  # NEW: Add grpc_path
                    use_http2=server_config.get('use_http2', True),  # NEW: Add use_http2
                    timeout=server_config.get('timeout', 30),
                    retry_attempts=server_config.get('retry_attempts', 3),
                    retry_delay=server_config.get('retry_delay', 1.0),
                    max_message_size=server_config.get('max_message_size', 50 * 1024 * 1024),
                    keepalive=server_config.get('keepalive', True)  # NEW: Add keepalive
                )

                # DEBUG: Log the created ServerConfig
                logger.info(f"🔌 [DEBUG] Created ServerConfig for '{name}': ssl_verify={config.ssl_verify}")

                self.connection_manager.add_server(name, config)

            logger.info(f"🌐 Инициализировано {len(servers_config)} серверов")
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации серверов: {e}")
    
    def _setup_callbacks(self):
        """Настраивает callback'и"""
        self.connection_manager.set_connection_callback(self._on_connection_changed)
        self.connection_manager.set_error_callback(self._on_error)
    
    def _set_default_server(self):
        """Устанавливает сервер по умолчанию из конфигурации"""
        try:
            # Пытаемся получить сервер из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            # Получаем настройки gRPC клиента из секции integrations
            integrations = config.get('integrations', {})
            grpc_config = integrations.get('grpc_client', {})
            default_server = grpc_config.get('server', 'local')

            # DEBUG: Логируем выбор сервера
            logger.info(f"🔌 [DEBUG] Config says default server: '{default_server}'")
            logger.info(f"🔌 [DEBUG] Available servers: {list(self.connection_manager.servers.keys())}")

            # Устанавливаем сервер по умолчанию
            if default_server in self.connection_manager.servers:
                self.connection_manager.current_server = default_server
                logger.info(f"🌐 Установлен сервер по умолчанию: {default_server}")
            else:
                logger.warning(f"⚠️ Сервер '{default_server}' не найден, используем 'local'")
                self.connection_manager.current_server = 'local'

        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить конфигурацию gRPC: {e}")
            # Используем local по умолчанию
            self.connection_manager.current_server = 'local'
    
    def _on_connection_changed(self, state):
        """Обрабатывает изменения состояния соединения"""
        logger.info(f"🔄 Состояние соединения: {state.value}")
    
    def _on_error(self, error: Exception, context: str):
        """Обрабатывает ошибки"""
        logger.error(f"❌ Ошибка в {context}: {error}")
    
    async def connect(self, server_name: Optional[str] = None) -> bool:
        """Подключается к серверу"""
        return await self.connection_manager.connect(server_name)
    
    async def disconnect(self):
        """Отключается от сервера"""
        await self.connection_manager.disconnect()
    
    async def switch_server(self, server_name: str) -> bool:
        """Переключается на другой сервер"""
        return await self.connection_manager.switch_server(server_name)
    
    async def execute_with_retry(self, operation, *args, **kwargs):
        """Выполняет операцию с retry механизмом"""
        return await self.retry_manager.execute_with_retry(operation, *args, **kwargs)

    def get_connection_state(self):
        """Возвращает текущее состояние соединения"""
        return self.connection_manager.get_connection_state()
    
    def get_metrics(self):
        """Возвращает метрики соединения"""
        return self.connection_manager.get_metrics()
    
    def is_connected(self) -> bool:
        """Проверяет, подключен ли клиент"""
        return self.connection_manager.is_connected()
    
    async def stream_audio(self, prompt: str, screenshot_base64: str, screen_info: dict, hardware_id: str) -> AsyncGenerator[Any, None]:
        """Стриминг аудио и текста на сервер"""
        try:
            logger.info(f"🔍 screen_info type: {type(screen_info)}")
            logger.info(f"🔍 screen_info content: {screen_info}")
            
            if not self.is_connected():
                await self.connect()

            # Импортируем protobuf-модули с фолбэком на server/
            streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()
            
            # Создаем запрос
            if hasattr(screen_info, 'get'):
                # Это словарь
                screen_width = screen_info.get('width')
                screen_height = screen_info.get('height')
            elif hasattr(screen_info, 'width') and hasattr(screen_info, 'height'):
                # Это объект с атрибутами width и height
                screen_width = screen_info.width  # type: ignore[attr-defined]
                screen_height = screen_info.height  # type: ignore[attr-defined]
            else:
                # Неизвестный тип, используем значения по умолчанию
                logger.warning(f"⚠️ Неизвестный тип screen_info: {type(screen_info)}, используем значения по умолчанию")
                screen_width = None
                screen_height = None
            
            request = streaming_pb2.StreamRequest(
                prompt=prompt,
                screenshot=screenshot_base64,
                screen_width=screen_width,
                screen_height=screen_height,
                hardware_id=hardware_id,
                session_id=None
            )
            
            # Выполняем стриминг
            async for response in streaming_pb2_grpc.StreamingServiceStub(
                self.connection_manager.channel
            ).StreamAudio(request, timeout=30):
                yield response
                
        except Exception as e:
            logger.error(f"❌ Ошибка стриминга аудио: {e}")
            raise

    async def generate_welcome_audio(
        self,
        text: str,
        *,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        session_id: Optional[str] = None,
        timeout: Optional[float] = None,
        server_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Запрашивает серверную генерацию приветственного аудио.

        Returns dict c numpy массивом аудио и метаданными.
        """
        if not text or not text.strip():
            raise ValueError("Welcome text must be non-empty")

        target_server = server_name or self.connection_manager.current_server

        if not self.is_connected():
            await self.connect(target_server)
        elif server_name and self.connection_manager.current_server != server_name:
            await self.connection_manager.switch_server(server_name)

        streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()

        request = streaming_pb2.WelcomeRequest(
            text=text,
            session_id=session_id or f"welcome_{datetime.now().timestamp()}",
        )

        if voice:
            request.voice = voice
        if language:
            request.language = language

        stub = streaming_pb2_grpc.StreamingServiceStub(self.connection_manager.channel)
        rpc_timeout = timeout or self.config.get('welcome_timeout_sec', 30.0)

        audio_chunks: List[bytes] = []
        metadata: Dict[str, Any] = {}
        chunk_dtype: Optional[str] = None

        try:
            async for response in stub.GenerateWelcomeAudio(request, timeout=rpc_timeout):
                content = response.WhichOneof('content')
                if content == 'audio_chunk':
                    chunk = response.audio_chunk
                    if chunk.audio_data:
                        audio_bytes = bytes(chunk.audio_data)
                        if audio_bytes:
                            audio_chunks.append(audio_bytes)
                            chunk_dtype = chunk.dtype or chunk_dtype
                elif content == 'metadata':
                    metadata = {
                        'method': response.metadata.method,
                        'duration_sec': response.metadata.duration_sec,
                        'sample_rate': response.metadata.sample_rate,
                        'channels': response.metadata.channels,
                    }
                elif content == 'error_message':
                    raise RuntimeError(response.error_message)
                elif content == 'end_message':
                    break

        except Exception as e:
            logger.error(f"❌ Ошибка генерации приветственного аудио: {e}")
            raise

        if not audio_chunks:
            raise RuntimeError("Server returned no audio data")

        raw_bytes = b''.join(audio_chunks)
        dtype = (chunk_dtype or 'int16').lower()

        if dtype not in ('int16', 'pcm_s16le', 'short'):
            logger.warning(f"⚠️ Неподдерживаемый dtype '{dtype}', привожу к int16")
            dtype = 'int16'

        np_dtype = np.int16
        audio_array = np.frombuffer(raw_bytes, dtype=np_dtype)

        if metadata.get('channels', 1) > 1:
            try:
                audio_array = audio_array.reshape(-1, metadata['channels'])
            except Exception:
                logger.warning("⚠️ Не удалось изменить форму аудио по каналам, оставляю одномерный массив")

        # 🔍 ДИАГНОСТИКА: Финальные метаданные перед возвратом
        final_sample_rate = metadata.get('sample_rate', 24000)  # ИСПРАВЛЕНО: было 48000, должно быть 24000 согласно спецификации
        if final_sample_rate != 24000:
            logger.warning(
                f"⚠️ [GRPC_DIAG] Sample rate не соответствует спецификации! "
                f"Ожидается: 24000Hz, получено: {final_sample_rate}Hz"
            )
        
        # 🔍 ДИАГНОСТИКА: Вычисляем реальную длительность
        actual_samples = len(audio_array) if audio_array.ndim == 1 else audio_array.shape[0]
        calculated_duration = actual_samples / float(final_sample_rate) if final_sample_rate > 0 else 0.0
        logger.info(
            f"🔍 [GRPC_DIAG] Финальный результат: samples={actual_samples}, "
            f"sr={final_sample_rate}Hz, calculated_duration={calculated_duration:.3f}s, "
            f"metadata_duration={metadata.get('duration_sec', 'N/A')}"
        )
        
        result = {
            'audio': audio_array,
            'metadata': {
                'method': metadata.get('method', 'server'),
                'duration_sec': metadata.get('duration_sec'),
                'sample_rate': final_sample_rate,
                'channels': metadata.get('channels', 1),
                'dtype': 'int16',
            }
        }

        return result

    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.connection_manager.cleanup()
            logger.info("🧹 GrpcClient очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcClient: {e}")

    def _import_proto_modules(self) -> Tuple[Any, Any]:
        """Гибкий импорт streaming_pb2 и streaming_pb2_grpc.
        Сначала пробуем из proto директории модуля, затем fallback в server/.
        """
        # 1) Пытаемся импортировать из proto директории модуля
        try:
            # Путь: client/modules/grpc_client/proto/
            proto_dir = Path(__file__).resolve().parent.parent / 'proto'
            
            if proto_dir.exists() and str(proto_dir) not in sys.path:
                sys.path.insert(0, str(proto_dir))
                logger.info(f"✅ Добавлен путь к proto модулям: {proto_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из proto/")
            return pb2, pb2_grpc
        except Exception as local_err:
            logger.warning(f"⚠️ Не удалось импортировать из proto/: {local_err}")

        # 2) Пытаемся взять из server/ (репозиторий корень/ server)
        try:
            repo_root = Path(__file__).resolve().parents[4]
            server_dir = repo_root / 'server'
            
            # Проверяем существование и добавляем только если нужно
            if server_dir.exists() and str(server_dir) not in sys.path:
                sys.path.append(str(server_dir))
                logger.info(f"✅ Добавлен путь к server модулям: {server_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из server/")
            return pb2, pb2_grpc
        except Exception as e:
            raise ImportError(f"Unable to import protobuf modules (streaming_pb2*). Error: {e}")



"""
Основной класс gRPC клиента

Обеспечивает:
- Управление соединениями через ConnectionManager
- Стриминг аудио через protobuf StreamingService
- Retry механизмы
- Health checking
"""

import asyncio
import logging
from typing import Optional, Dict, Any, AsyncIterator, TYPE_CHECKING
from pathlib import Path

from .connection_manager import ConnectionManager
from .types import ServerConfig, ConnectionState
from .retry_manager import RetryManager

# Type checking imports for protobuf modules
if TYPE_CHECKING:
    from streaming_pb2 import StreamRequest, StreamResponse  # type: ignore
    from streaming_pb2_grpc import StreamingServiceStub  # type: ignore
else:
    StreamRequest = None
    StreamResponse = None
    StreamingServiceStub = None

# Runtime protobuf imports (dynamic path addition)
try:
    import sys
    proto_path = Path(__file__).parent.parent / "proto"
    if str(proto_path) not in sys.path:
        sys.path.insert(0, str(proto_path))
    
    from streaming_pb2 import StreamRequest, StreamResponse  # type: ignore[import-untyped]
    from streaming_pb2_grpc import StreamingServiceStub  # type: ignore[import-untyped]
except ImportError as e:
    logging.getLogger(__name__).error(f"❌ Ошибка импорта protobuf: {e}")
    if not TYPE_CHECKING:
        StreamRequest = None
        StreamResponse = None
        StreamingServiceStub = None

logger = logging.getLogger(__name__)


class GrpcClient:  # type: ignore[no-redef]
    """
    Основной класс gRPC клиента
    
    Использует ConnectionManager для управления соединениями
    и предоставляет высокоуровневый API для стриминга аудио.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация gRPC клиента
        
        Args:
            config: Конфигурация клиента (servers, auto_fallback, etc.)
        """
        self.config = config or {}
        self.connection_manager = ConnectionManager()
        self.retry_manager = RetryManager()
        
        # Инициализация серверов из конфигурации
        self._initialize_servers()
        
        # Stub будет создан при подключении
        self._stub: Optional[StreamingServiceStub] = None
        
        logger.info("🔌 GrpcClient инициализирован")
    
    def _initialize_servers(self):
        """Инициализирует серверы из конфигурации"""
        servers = self.config.get('servers', {})
        if not servers:
            logger.warning("⚠️ Нет серверов в конфигурации")
            return
        
        for name, server_cfg in servers.items():
            try:
                config = ServerConfig(
                    address=server_cfg.get('address', '127.0.0.1'),
                    port=server_cfg.get('port', 50051),
                    use_ssl=server_cfg.get('use_ssl', False),
                    ssl_verify=server_cfg.get('ssl_verify', True),
                    grpc_path=server_cfg.get('grpc_path'),
                    use_http2=server_cfg.get('use_http2', True),
                    timeout=server_cfg.get('timeout', 30),
                    retry_attempts=server_cfg.get('retry_attempts', 3),
                    retry_delay=server_cfg.get('retry_delay', 1.0),
                    keepalive=server_cfg.get('keepalive', True),
                )
                self.connection_manager.add_server(name, config)
            except Exception as e:
                logger.error(f"❌ Ошибка добавления сервера {name}: {e}")
        
        # Устанавливаем сервер по умолчанию
        default_server = self.config.get('default_server')
        if default_server and default_server in servers:
            self.connection_manager.current_server = default_server
            logger.info(f"🌐 Установлен сервер по умолчанию: {default_server}")
    
    async def connect(self, server_name: Optional[str] = None) -> bool:
        """
        Подключается к серверу
        
        Args:
            server_name: Имя сервера (если None, используется default)
            
        Returns:
            bool: True если подключение успешно
        """
        # Переопределяем _create_stub для создания StreamingServiceStub
        original_create_stub = self.connection_manager._create_stub
        
        def create_streaming_stub():
            """Создает StreamingServiceStub из protobuf"""
            if StreamingServiceStub is None:
                logger.error("❌ StreamingServiceStub не импортирован")
                return None
            if self.connection_manager.channel is None:
                logger.error("❌ Канал не создан")
                return None
            stub = StreamingServiceStub(self.connection_manager.channel)
            logger.debug("✅ StreamingServiceStub создан")
            return stub
        
        # Временно переопределяем метод создания stub
        self.connection_manager._create_stub = create_streaming_stub  # type: ignore[assignment]
        
        try:
            success = await self.connection_manager.connect(server_name)
            if success:
                self._stub = self.connection_manager.stub
                logger.info("✅ GrpcClient подключен")
            return success
        finally:
            # Восстанавливаем оригинальный метод
            self.connection_manager._create_stub = original_create_stub
    
    def is_connected(self) -> bool:
        """Проверяет, подключен ли клиент"""
        return self.connection_manager.is_connected()
    
    async def stream_audio(
        self,
        prompt: str,
        screenshot_base64: str = "",
        screen_info: Optional[Dict[str, int]] = None,
        hardware_id: str = "",
        session_id: Optional[str] = None,
    ) -> AsyncIterator[StreamResponse]:
        """
        Стримит аудио от сервера
        
        Args:
            prompt: Текст запроса
            screenshot_base64: Base64 скриншота (опционально)
            screen_info: Информация о размере экрана {"width": int, "height": int}
            hardware_id: ID оборудования
            session_id: ID сессии (опционально)
            
        Yields:
            StreamResponse: Ответы от сервера
        """
        if not self._stub:
            logger.error("❌ Stub не создан, невозможно стримить")
            return
        
        if StreamRequest is None or StreamResponse is None:
            logger.error("❌ Protobuf классы не импортированы")
            return
        
        # Создаем запрос
        request = StreamRequest()
        request.prompt = prompt
        request.hardware_id = hardware_id
        
        if screenshot_base64:
            request.screenshot = screenshot_base64
        
        if screen_info:
            if 'width' in screen_info:
                request.screen_width = screen_info['width']
            if 'height' in screen_info:
                request.screen_height = screen_info['height']
        
        if session_id:
            request.session_id = session_id
        
        try:
            # Вызываем streaming метод
            async for response in self._stub.StreamAudio(request):
                yield response
        except Exception as e:
            logger.error(f"❌ Ошибка стриминга аудио: {e}")
            raise
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.connection_manager.cleanup()
            self._stub = None
            logger.info("🧹 GrpcClient очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcClient: {e}")

"""
Основной класс gRPC клиента

Обеспечивает:
- Управление соединениями через ConnectionManager
- Стриминг аудио через protobuf StreamingService
- Генерацию приветственного аудио
- Retry механизмы
- Health checking
"""

import asyncio
import logging
from typing import Optional, Dict, Any, AsyncIterator, TYPE_CHECKING
from pathlib import Path
import numpy as np

from .connection_manager import ConnectionManager
from .types import ServerConfig, ConnectionState
from .retry_manager import RetryManager

# Type checking imports for protobuf modules
if TYPE_CHECKING:
    from streaming_pb2 import StreamRequest, StreamResponse, WelcomeRequest, WelcomeResponse  # type: ignore
    from streaming_pb2_grpc import StreamingServiceStub  # type: ignore
else:
    StreamRequest = None
    StreamResponse = None
    WelcomeRequest = None
    WelcomeResponse = None
    StreamingServiceStub = None

# Runtime protobuf imports (dynamic path addition)
try:
    import sys
    proto_path = Path(__file__).parent.parent / "proto"
    if str(proto_path) not in sys.path:
        sys.path.insert(0, str(proto_path))
    
    from streaming_pb2 import StreamRequest, StreamResponse, WelcomeRequest, WelcomeResponse  # type: ignore[import-untyped]
    from streaming_pb2_grpc import StreamingServiceStub  # type: ignore[import-untyped]
except ImportError as e:
    logging.getLogger(__name__).error(f"❌ Ошибка импорта protobuf: {e}")
    if not TYPE_CHECKING:
        StreamRequest = None
        StreamResponse = None
        WelcomeRequest = None
        WelcomeResponse = None
        StreamingServiceStub = None

logger = logging.getLogger(__name__)


class GrpcClient:  # type: ignore[no-redef]
    """
    Основной класс gRPC клиента
    
    Использует ConnectionManager для управления соединениями
    и предоставляет высокоуровневый API для стриминга аудио и генерации приветствия.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Инициализация gRPC клиента
        
        Args:
            config: Конфигурация клиента (servers, auto_fallback, etc.)
        """
        self.config = config or {}
        self.connection_manager = ConnectionManager()
        self.retry_manager = RetryManager()
        
        # Инициализация серверов из конфигурации
        self._initialize_servers()
        
        # Stub будет создан при подключении
        self._stub: Optional[StreamingServiceStub] = None
        
        logger.info("🔌 GrpcClient инициализирован")
    
    def _initialize_servers(self):
        """Инициализирует серверы из конфигурации"""
        servers = self.config.get('servers', {})
        if not servers:
            logger.warning("⚠️ Нет серверов в конфигурации")
            return
        
        for name, server_cfg in servers.items():
            try:
                config = ServerConfig(
                    address=server_cfg.get('address', '127.0.0.1'),
                    port=server_cfg.get('port', 50051),
                    use_ssl=server_cfg.get('use_ssl', False),
                    ssl_verify=server_cfg.get('ssl_verify', True),
                    grpc_path=server_cfg.get('grpc_path'),
                    use_http2=server_cfg.get('use_http2', True),
                    timeout=server_cfg.get('timeout', 30),
                    retry_attempts=server_cfg.get('retry_attempts', 3),
                    retry_delay=server_cfg.get('retry_delay', 1.0),
                    keepalive=server_cfg.get('keepalive', True),
                )
                self.connection_manager.add_server(name, config)
            except Exception as e:
                logger.error(f"❌ Ошибка добавления сервера {name}: {e}")
        
        # Устанавливаем сервер по умолчанию
        default_server = self.config.get('default_server')
        if default_server and default_server in servers:
            self.connection_manager.current_server = default_server
            logger.info(f"🌐 Установлен сервер по умолчанию: {default_server}")
    
    async def connect(self, server_name: Optional[str] = None) -> bool:
        """
        Подключается к серверу
        
        Args:
            server_name: Имя сервера (если None, используется default)
            
        Returns:
            bool: True если подключение успешно
        """
        # Переопределяем _create_stub для создания StreamingServiceStub
        original_create_stub = self.connection_manager._create_stub
        
        def create_streaming_stub():
            """Создает StreamingServiceStub из protobuf"""
            if StreamingServiceStub is None:
                logger.error("❌ StreamingServiceStub не импортирован")
                return None
            if self.connection_manager.channel is None:
                logger.error("❌ Канал не создан")
                return None
            stub = StreamingServiceStub(self.connection_manager.channel)
            logger.debug("✅ StreamingServiceStub создан")
            return stub
        
        # Временно переопределяем метод создания stub
        self.connection_manager._create_stub = create_streaming_stub  # type: ignore[assignment]
        
        try:
            success = await self.connection_manager.connect(server_name)
            if success:
                self._stub = self.connection_manager.stub
                logger.info("✅ GrpcClient подключен")
            return success
        finally:
            # Восстанавливаем оригинальный метод
            self.connection_manager._create_stub = original_create_stub
    
    def is_connected(self) -> bool:
        """Проверяет, подключен ли клиент"""
        return self.connection_manager.is_connected()
    
    async def stream_audio(
        self,
        prompt: str,
        screenshot_base64: str = "",
        screen_info: Optional[Dict[str, int]] = None,
        hardware_id: str = "",
        session_id: Optional[str] = None,
    ) -> AsyncIterator[StreamResponse]:
        """
        Стримит аудио от сервера
        
        Args:
            prompt: Текст запроса
            screenshot_base64: Base64 скриншота (опционально)
            screen_info: Информация о размере экрана {"width": int, "height": int}
            hardware_id: ID оборудования
            session_id: ID сессии (опционально)
            
        Yields:
            StreamResponse: Ответы от сервера
        """
        if not self._stub:
            logger.error("❌ Stub не создан, невозможно стримить")
            return
        
        if StreamRequest is None or StreamResponse is None:
            logger.error("❌ Protobuf классы не импортированы")
            return
        
        # Создаем запрос
        request = StreamRequest()
        request.prompt = prompt
        request.hardware_id = hardware_id
        
        if screenshot_base64:
            request.screenshot = screenshot_base64
        
        if screen_info:
            if 'width' in screen_info:
                request.screen_width = screen_info['width']
            if 'height' in screen_info:
                request.screen_height = screen_info['height']
        
        if session_id:
            request.session_id = session_id
        
        try:
            # Вызываем streaming метод
            async for response in self._stub.StreamAudio(request):
                yield response
        except Exception as e:
            logger.error(f"❌ Ошибка стриминга аудио: {e}")
            raise
    
    async def generate_welcome_audio(
        self,
        text: str,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        server_name: Optional[str] = None,
        timeout: float = 30.0,
    ) -> Dict[str, Any]:
        """
        Генерирует приветственное аудио на сервере
        
        Args:
            text: Текст приветствия
            voice: Голос для генерации (опционально)
            language: Язык/локаль (опционально)
            server_name: Имя сервера для подключения (опционально)
            timeout: Таймаут в секундах
            
        Returns:
            Dict с ключами:
                - 'audio': numpy.ndarray с аудио данными
                - 'metadata': Dict с метаданными (sample_rate, channels, method, duration_sec)
        """
        # Подключаемся к серверу если не подключены
        if not self.is_connected():
            logger.info(f"🔌 Подключение к серверу {server_name or 'default'} для генерации приветствия...")
            success = await self.connect(server_name)
            if not success:
                logger.error("❌ Не удалось подключиться к серверу")
                return {'audio': None, 'metadata': {}}
        
        if not self._stub:
            logger.error("❌ Stub не создан, невозможно генерировать приветствие")
            return {'audio': None, 'metadata': {}}
        
        if WelcomeRequest is None or WelcomeResponse is None:
            logger.error("❌ Protobuf классы для приветствия не импортированы")
            return {'audio': None, 'metadata': {}}
        
        # Создаем запрос
        request = WelcomeRequest()
        request.text = text
        if voice:
            request.voice = voice
        if language:
            request.language = language
        
        # Собираем аудио чанки
        audio_chunks: list = []
        metadata: Dict[str, Any] = {}
        got_error = False
        error_message = None
        
        try:
            async for response in asyncio.wait_for(  # type: ignore[arg-type]
                self._stub.GenerateWelcomeAudio(request),
                timeout=timeout
            ):
                # Проверяем тип контента (oneof)
                which_oneof = response.WhichOneof('content') if hasattr(response, 'WhichOneof') else None
                
                if which_oneof == 'audio_chunk':
                    chunk = response.audio_chunk
                    audio_data = chunk.audio_data
                    if audio_data:
                        audio_chunks.append(audio_data)
                        logger.debug(f"📦 Получен аудио чанк: {len(audio_data)} байт")
                
                elif which_oneof == 'metadata':
                    meta = response.metadata
                    # 🔍 ДИАГНОСТИКА: Логируем RAW значения из protobuf перед обработкой
                    raw_sr = meta.sample_rate if hasattr(meta, 'sample_rate') else None
                    raw_ch = meta.channels if hasattr(meta, 'channels') else None
                    raw_method = meta.method if hasattr(meta, 'method') else None
                    raw_duration = meta.duration_sec if hasattr(meta, 'duration_sec') else None
                    logger.info(
                        f"🔍 [GRPC_DIAG] RAW metadata от сервера: "
                        f"sample_rate={raw_sr}, channels={raw_ch}, method={raw_method}, duration_sec={raw_duration}"
                    )
                    
                    metadata = {
                        'method': meta.method if meta.method else 'server',
                        'duration_sec': meta.duration_sec if meta.duration_sec else 0.0,
                        'sample_rate': meta.sample_rate if meta.sample_rate else 24000,  # Fallback согласно спецификации
                        'channels': meta.channels if meta.channels else 1,  # Fallback: моно
                    }
                    logger.info(f"📋 [GRPC_DIAG] Обработанные метаданные: {metadata}")
                    
                    # 🔍 ДИАГНОСТИКА: Проверка соответствия спецификации
                    if metadata['sample_rate'] != 24000:
                        logger.warning(
                            f"⚠️ [GRPC_DIAG] Sample rate не соответствует спецификации! "
                            f"Ожидается: 24000Hz, получено: {metadata['sample_rate']}Hz"
                        )
                
                elif which_oneof == 'end_message':
                    logger.info(f"✅ Генерация приветствия завершена: {response.end_message}")
                    break
                
                elif which_oneof == 'error_message':
                    error_message = response.error_message
                    got_error = True
                    logger.error(f"❌ Ошибка генерации приветствия: {error_message}")
                    break
        
        except asyncio.TimeoutError:
            logger.error(f"⏰ Таймаут генерации приветствия ({timeout}s)")
            return {'audio': None, 'metadata': metadata, 'error': 'timeout'}
        except Exception as e:
            logger.error(f"❌ Ошибка генерации приветствия: {e}")
            return {'audio': None, 'metadata': metadata, 'error': str(e)}
        
        if got_error:
            return {'audio': None, 'metadata': metadata, 'error': error_message}
        
        if not audio_chunks:
            logger.error("❌ Не получено ни одного аудио чанка")
            return {'audio': None, 'metadata': metadata, 'error': 'no_audio_chunks'}
        
        # Объединяем все чанки в один массив байт
        all_audio_bytes = b''.join(audio_chunks)
        
        # 🔍 ДИАГНОСТИКА: Логируем размер данных перед конвертацией
        total_bytes = len(all_audio_bytes)
        logger.info(
            f"🔍 [GRPC_DIAG] Объединение чанков: chunks={len(audio_chunks)}, "
            f"total_bytes={total_bytes}, expected_samples={total_bytes // 2} (16-bit)"
        )
        
        # Конвертируем в numpy array
        # По умолчанию используем int16 (16-bit PCM) согласно спецификации
        sample_rate = metadata.get('sample_rate', 24000)
        channels = metadata.get('channels', 1)
        
        # 🔍 ДИАГНОСТИКА: Вычисляем ожидаемую длительность
        expected_samples = total_bytes // 2  # 16-bit = 2 bytes per sample
        expected_duration = expected_samples / float(sample_rate) if sample_rate > 0 else 0.0
        logger.info(
            f"🔍 [GRPC_DIAG] Параметры аудио: samples={expected_samples}, sr={sample_rate}Hz, "
            f"ch={channels}, expected_duration={expected_duration:.3f}s"
        )
        
        # Используем int16 по умолчанию (соответствует спецификации: 16-bit PCM)
        audio_array = np.frombuffer(all_audio_bytes, dtype=np.int16)
        
        # 🔍 ДИАГНОСТИКА: Проверяем размер массива
        actual_samples = len(audio_array)
        logger.info(
            f"🔍 [GRPC_DIAG] После конвертации: array_shape={audio_array.shape}, "
            f"actual_samples={actual_samples}, matches_expected={actual_samples == expected_samples}"
        )
        
        # Если channels > 1, нужно переформировать массив
        if channels > 1 and len(audio_array) % channels == 0:
            audio_array = audio_array.reshape(-1, channels)
        
        logger.info(f"✅ Приветствие сгенерировано: {len(audio_array)} сэмплов, {sample_rate}Hz, {channels} канал(ов)")
        
        return {
            'audio': audio_array,
            'metadata': metadata,
        }
    
    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.connection_manager.cleanup()
            self._stub = None
            logger.info("🧹 GrpcClient очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcClient: {e}")

"""
Основной gRPC клиент с модульной архитектурой
"""

import asyncio
import logging
from typing import Optional, Dict, Any, AsyncGenerator, Tuple, List
import importlib
import sys
from pathlib import Path
from datetime import datetime

import numpy as np

from integration.utils.resource_path import get_resource_path

from .types import ServerConfig, RetryConfig, HealthCheckConfig, RetryStrategy
from .retry_manager import RetryManager
from .connection_manager import ConnectionManager

logger = logging.getLogger(__name__)


class GrpcClient:  # type: ignore[no-redef]
    """Основной gRPC клиент с модульной архитектурой"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or self._create_default_config()
        
        # Модульные компоненты
        self.connection_manager = ConnectionManager()
        self.retry_manager = RetryManager(
            RetryConfig(
                max_attempts=self.config.get('max_retry_attempts', 3),
                base_delay=self.config.get('retry_delay', 1.0),
                strategy=RetryStrategy.EXPONENTIAL  # Используем enum вместо строки
            )
        )
        
        # Инициализация
        self._initialize_servers()
        self._setup_callbacks()
        
        # Устанавливаем сервер по умолчанию из конфигурации
        self._set_default_server()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Создает конфигурацию по умолчанию из централизованной системы"""
        try:
            # Загружаем конфигурацию из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            grpc_data = config.get('grpc', {})
            servers_config = grpc_data.get('servers', {})
            
            # Преобразуем конфигурацию в формат, ожидаемый GrpcClient
            servers = {}
            for server_name, server_config in servers_config.items():
                server_dict = {
                    'address': server_config.get('host', '127.0.0.1'),
                    'port': server_config.get('port', 50051),
                    'use_ssl': server_config.get('ssl', False),
                    'ssl_verify': server_config.get('ssl_verify', True),
                    'grpc_path': server_config.get('grpc_path'),
                    'use_http2': server_config.get('use_http2', True),
                    'timeout': server_config.get('timeout', grpc_data.get('connection_timeout', 30)),
                    'retry_attempts': server_config.get('retry_attempts', grpc_data.get('retry_attempts', 3)),
                    'retry_delay': server_config.get('retry_delay', grpc_data.get('retry_delay', 1.0)),
                    'keepalive': server_config.get('keepalive', True)
                }
                # DEBUG: Логируем конфигурацию каждого сервера
                logger.info(f"🔌 [DEBUG] Loaded server '{server_name}': {server_dict['address']}:{server_dict['port']}, ssl={server_dict['use_ssl']}, ssl_verify={server_dict['ssl_verify']}")
                servers[server_name] = server_dict
            
            return {
                'servers': servers,
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': grpc_data.get('connection_timeout', 10),
                'max_retry_attempts': grpc_data.get('retry_attempts', 3),
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
            
        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить централизованную конфигурацию: {e}")
            # Fallback к минимальной конфигурации
            return {
                'servers': {
                    'local': {
                        'address': '127.0.0.1',
                        'port': 50051,
                        'use_ssl': False,
                        'timeout': 30,
                        'retry_attempts': 3,
                        'retry_delay': 1.0
                    }
                },
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': 10,
                'max_retry_attempts': 3,
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
    
    def _initialize_servers(self):
        """Инициализирует конфигурации серверов"""
        try:
            servers_config = self.config.get('servers', {})
            for name, server_config in servers_config.items():
                # DEBUG: Log what we're reading from config dict
                ssl_verify_from_config = server_config.get('ssl_verify', True)
                logger.info(f"🔌 [DEBUG] _initialize_servers creating ServerConfig for '{name}': ssl_verify={ssl_verify_from_config}")

                config = ServerConfig(
                    address=server_config['address'],
                    port=server_config['port'],
                    use_ssl=server_config.get('use_ssl', False),
                    ssl_verify=ssl_verify_from_config,  # NEW: Add ssl_verify
                    grpc_path=server_config.get('grpc_path'),  # NEW: Add grpc_path
                    use_http2=server_config.get('use_http2', True),  # NEW: Add use_http2
                    timeout=server_config.get('timeout', 30),
                    retry_attempts=server_config.get('retry_attempts', 3),
                    retry_delay=server_config.get('retry_delay', 1.0),
                    max_message_size=server_config.get('max_message_size', 50 * 1024 * 1024),
                    keepalive=server_config.get('keepalive', True)  # NEW: Add keepalive
                )

                # DEBUG: Log the created ServerConfig
                logger.info(f"🔌 [DEBUG] Created ServerConfig for '{name}': ssl_verify={config.ssl_verify}")

                self.connection_manager.add_server(name, config)

            logger.info(f"🌐 Инициализировано {len(servers_config)} серверов")
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации серверов: {e}")
    
    def _setup_callbacks(self):
        """Настраивает callback'и"""
        self.connection_manager.set_connection_callback(self._on_connection_changed)
        self.connection_manager.set_error_callback(self._on_error)
    
    def _set_default_server(self):
        """Устанавливает сервер по умолчанию из конфигурации"""
        try:
            # Пытаемся получить сервер из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            # Получаем настройки gRPC клиента из секции integrations
            integrations = config.get('integrations', {})
            grpc_config = integrations.get('grpc_client', {})
            default_server = grpc_config.get('server', 'local')

            # DEBUG: Логируем выбор сервера
            logger.info(f"🔌 [DEBUG] Config says default server: '{default_server}'")
            logger.info(f"🔌 [DEBUG] Available servers: {list(self.connection_manager.servers.keys())}")

            # Устанавливаем сервер по умолчанию
            if default_server in self.connection_manager.servers:
                self.connection_manager.current_server = default_server
                logger.info(f"🌐 Установлен сервер по умолчанию: {default_server}")
            else:
                logger.warning(f"⚠️ Сервер '{default_server}' не найден, используем 'local'")
                self.connection_manager.current_server = 'local'

        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить конфигурацию gRPC: {e}")
            # Используем local по умолчанию
            self.connection_manager.current_server = 'local'
    
    def _on_connection_changed(self, state):
        """Обрабатывает изменения состояния соединения"""
        logger.info(f"🔄 Состояние соединения: {state.value}")
    
    def _on_error(self, error: Exception, context: str):
        """Обрабатывает ошибки"""
        logger.error(f"❌ Ошибка в {context}: {error}")
    
    async def connect(self, server_name: Optional[str] = None) -> bool:
        """Подключается к серверу"""
        return await self.connection_manager.connect(server_name)
    
    async def disconnect(self):
        """Отключается от сервера"""
        await self.connection_manager.disconnect()
    
    async def switch_server(self, server_name: str) -> bool:
        """Переключается на другой сервер"""
        return await self.connection_manager.switch_server(server_name)
    
    async def execute_with_retry(self, operation, *args, **kwargs):
        """Выполняет операцию с retry механизмом"""
        return await self.retry_manager.execute_with_retry(operation, *args, **kwargs)

    def get_connection_state(self):
        """Возвращает текущее состояние соединения"""
        return self.connection_manager.get_connection_state()
    
    def get_metrics(self):
        """Возвращает метрики соединения"""
        return self.connection_manager.get_metrics()
    
    def is_connected(self) -> bool:
        """Проверяет, подключен ли клиент"""
        return self.connection_manager.is_connected()
    
    async def stream_audio(self, prompt: str, screenshot_base64: str, screen_info: dict, hardware_id: str) -> AsyncGenerator[Any, None]:
        """Стриминг аудио и текста на сервер"""
        try:
            logger.info(f"🔍 screen_info type: {type(screen_info)}")
            logger.info(f"🔍 screen_info content: {screen_info}")
            
            if not self.is_connected():
                await self.connect()

            # Импортируем protobuf-модули с фолбэком на server/
            streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()
            
            # Создаем запрос
            if hasattr(screen_info, 'get'):
                # Это словарь
                screen_width = screen_info.get('width')
                screen_height = screen_info.get('height')
            elif hasattr(screen_info, 'width') and hasattr(screen_info, 'height'):
                # Это объект с атрибутами width и height
                screen_width = screen_info.width  # type: ignore[attr-defined]
                screen_height = screen_info.height  # type: ignore[attr-defined]
            else:
                # Неизвестный тип, используем значения по умолчанию
                logger.warning(f"⚠️ Неизвестный тип screen_info: {type(screen_info)}, используем значения по умолчанию")
                screen_width = None
                screen_height = None
            
            request = streaming_pb2.StreamRequest(
                prompt=prompt,
                screenshot=screenshot_base64,
                screen_width=screen_width,
                screen_height=screen_height,
                hardware_id=hardware_id,
                session_id=None
            )
            
            # Выполняем стриминг
            async for response in streaming_pb2_grpc.StreamingServiceStub(
                self.connection_manager.channel
            ).StreamAudio(request, timeout=30):
                yield response
                
        except Exception as e:
            logger.error(f"❌ Ошибка стриминга аудио: {e}")
            raise

    async def generate_welcome_audio(
        self,
        text: str,
        *,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        session_id: Optional[str] = None,
        timeout: Optional[float] = None,
        server_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Запрашивает серверную генерацию приветственного аудио.

        Returns dict c numpy массивом аудио и метаданными.
        """
        if not text or not text.strip():
            raise ValueError("Welcome text must be non-empty")

        target_server = server_name or self.connection_manager.current_server

        if not self.is_connected():
            await self.connect(target_server)
        elif server_name and self.connection_manager.current_server != server_name:
            await self.connection_manager.switch_server(server_name)

        streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()

        request = streaming_pb2.WelcomeRequest(
            text=text,
            session_id=session_id or f"welcome_{datetime.now().timestamp()}",
        )

        if voice:
            request.voice = voice
        if language:
            request.language = language

        stub = streaming_pb2_grpc.StreamingServiceStub(self.connection_manager.channel)
        rpc_timeout = timeout or self.config.get('welcome_timeout_sec', 30.0)

        audio_chunks: List[bytes] = []
        metadata: Dict[str, Any] = {}
        chunk_dtype: Optional[str] = None

        try:
            async for response in stub.GenerateWelcomeAudio(request, timeout=rpc_timeout):
                content = response.WhichOneof('content')
                if content == 'audio_chunk':
                    chunk = response.audio_chunk
                    if chunk.audio_data:
                        audio_bytes = bytes(chunk.audio_data)
                        if audio_bytes:
                            audio_chunks.append(audio_bytes)
                            chunk_dtype = chunk.dtype or chunk_dtype
                elif content == 'metadata':
                    metadata = {
                        'method': response.metadata.method,
                        'duration_sec': response.metadata.duration_sec,
                        'sample_rate': response.metadata.sample_rate,
                        'channels': response.metadata.channels,
                    }
                elif content == 'error_message':
                    raise RuntimeError(response.error_message)
                elif content == 'end_message':
                    break

        except Exception as e:
            logger.error(f"❌ Ошибка генерации приветственного аудио: {e}")
            raise

        if not audio_chunks:
            raise RuntimeError("Server returned no audio data")

        raw_bytes = b''.join(audio_chunks)
        dtype = (chunk_dtype or 'int16').lower()

        if dtype not in ('int16', 'pcm_s16le', 'short'):
            logger.warning(f"⚠️ Неподдерживаемый dtype '{dtype}', привожу к int16")
            dtype = 'int16'

        np_dtype = np.int16
        audio_array = np.frombuffer(raw_bytes, dtype=np_dtype)

        if metadata.get('channels', 1) > 1:
            try:
                audio_array = audio_array.reshape(-1, metadata['channels'])
            except Exception:
                logger.warning("⚠️ Не удалось изменить форму аудио по каналам, оставляю одномерный массив")

        # 🔍 ДИАГНОСТИКА: Финальные метаданные перед возвратом
        final_sample_rate = metadata.get('sample_rate', 24000)  # ИСПРАВЛЕНО: было 48000, должно быть 24000 согласно спецификации
        if final_sample_rate != 24000:
            logger.warning(
                f"⚠️ [GRPC_DIAG] Sample rate не соответствует спецификации! "
                f"Ожидается: 24000Hz, получено: {final_sample_rate}Hz"
            )
        
        # 🔍 ДИАГНОСТИКА: Вычисляем реальную длительность
        actual_samples = len(audio_array) if audio_array.ndim == 1 else audio_array.shape[0]
        calculated_duration = actual_samples / float(final_sample_rate) if final_sample_rate > 0 else 0.0
        logger.info(
            f"🔍 [GRPC_DIAG] Финальный результат: samples={actual_samples}, "
            f"sr={final_sample_rate}Hz, calculated_duration={calculated_duration:.3f}s, "
            f"metadata_duration={metadata.get('duration_sec', 'N/A')}"
        )
        
        result = {
            'audio': audio_array,
            'metadata': {
                'method': metadata.get('method', 'server'),
                'duration_sec': metadata.get('duration_sec'),
                'sample_rate': final_sample_rate,
                'channels': metadata.get('channels', 1),
                'dtype': 'int16',
            }
        }

        return result

    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.connection_manager.cleanup()
            logger.info("🧹 GrpcClient очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcClient: {e}")

    def _import_proto_modules(self) -> Tuple[Any, Any]:
        """Гибкий импорт streaming_pb2 и streaming_pb2_grpc.
        Сначала пробуем из proto директории модуля, затем fallback в server/.
        """
        # 1) Пытаемся импортировать из proto директории модуля
        try:
            # Путь: client/modules/grpc_client/proto/
            proto_dir = Path(__file__).resolve().parent.parent / 'proto'
            
            if proto_dir.exists() and str(proto_dir) not in sys.path:
                sys.path.insert(0, str(proto_dir))
                logger.info(f"✅ Добавлен путь к proto модулям: {proto_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из proto/")
            return pb2, pb2_grpc
        except Exception as local_err:
            logger.warning(f"⚠️ Не удалось импортировать из proto/: {local_err}")

        # 2) Пытаемся взять из server/ (репозиторий корень/ server)
        try:
            repo_root = Path(__file__).resolve().parents[4]
            server_dir = repo_root / 'server'
            
            # Проверяем существование и добавляем только если нужно
            if server_dir.exists() and str(server_dir) not in sys.path:
                sys.path.append(str(server_dir))
                logger.info(f"✅ Добавлен путь к server модулям: {server_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из server/")
            return pb2, pb2_grpc
        except Exception as e:
            raise ImportError(f"Unable to import protobuf modules (streaming_pb2*). Error: {e}")

"""
Основной gRPC клиент с модульной архитектурой
"""

import asyncio
import logging
from typing import Optional, Dict, Any, AsyncGenerator, Tuple, List
import importlib
import sys
from pathlib import Path
from datetime import datetime

import numpy as np

from integration.utils.resource_path import get_resource_path

from .types import ServerConfig, RetryConfig, HealthCheckConfig, RetryStrategy
from .retry_manager import RetryManager
from .connection_manager import ConnectionManager

logger = logging.getLogger(__name__)


class GrpcClient:  # type: ignore[no-redef]
    """Основной gRPC клиент с модульной архитектурой"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or self._create_default_config()
        
        # Модульные компоненты
        self.connection_manager = ConnectionManager()
        self.retry_manager = RetryManager(
            RetryConfig(
                max_attempts=self.config.get('max_retry_attempts', 3),
                base_delay=self.config.get('retry_delay', 1.0),
                strategy=RetryStrategy.EXPONENTIAL  # Используем enum вместо строки
            )
        )
        
        # Инициализация
        self._initialize_servers()
        self._setup_callbacks()
        
        # Устанавливаем сервер по умолчанию из конфигурации
        self._set_default_server()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Создает конфигурацию по умолчанию из централизованной системы"""
        try:
            # Загружаем конфигурацию из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            grpc_data = config.get('grpc', {})
            servers_config = grpc_data.get('servers', {})
            
            # Преобразуем конфигурацию в формат, ожидаемый GrpcClient
            servers = {}
            for server_name, server_config in servers_config.items():
                server_dict = {
                    'address': server_config.get('host', '127.0.0.1'),
                    'port': server_config.get('port', 50051),
                    'use_ssl': server_config.get('ssl', False),
                    'ssl_verify': server_config.get('ssl_verify', True),
                    'grpc_path': server_config.get('grpc_path'),
                    'use_http2': server_config.get('use_http2', True),
                    'timeout': server_config.get('timeout', grpc_data.get('connection_timeout', 30)),
                    'retry_attempts': server_config.get('retry_attempts', grpc_data.get('retry_attempts', 3)),
                    'retry_delay': server_config.get('retry_delay', grpc_data.get('retry_delay', 1.0)),
                    'keepalive': server_config.get('keepalive', True)
                }
                # DEBUG: Логируем конфигурацию каждого сервера
                logger.info(f"🔌 [DEBUG] Loaded server '{server_name}': {server_dict['address']}:{server_dict['port']}, ssl={server_dict['use_ssl']}, ssl_verify={server_dict['ssl_verify']}")
                servers[server_name] = server_dict
            
            return {
                'servers': servers,
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': grpc_data.get('connection_timeout', 10),
                'max_retry_attempts': grpc_data.get('retry_attempts', 3),
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
            
        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить централизованную конфигурацию: {e}")
            # Fallback к минимальной конфигурации
            return {
                'servers': {
                    'local': {
                        'address': '127.0.0.1',
                        'port': 50051,
                        'use_ssl': False,
                        'timeout': 30,
                        'retry_attempts': 3,
                        'retry_delay': 1.0
                    }
                },
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': 10,
                'max_retry_attempts': 3,
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
    
    def _initialize_servers(self):
        """Инициализирует конфигурации серверов"""
        try:
            servers_config = self.config.get('servers', {})
            for name, server_config in servers_config.items():
                # DEBUG: Log what we're reading from config dict
                ssl_verify_from_config = server_config.get('ssl_verify', True)
                logger.info(f"🔌 [DEBUG] _initialize_servers creating ServerConfig for '{name}': ssl_verify={ssl_verify_from_config}")

                config = ServerConfig(
                    address=server_config['address'],
                    port=server_config['port'],
                    use_ssl=server_config.get('use_ssl', False),
                    ssl_verify=ssl_verify_from_config,  # NEW: Add ssl_verify
                    grpc_path=server_config.get('grpc_path'),  # NEW: Add grpc_path
                    use_http2=server_config.get('use_http2', True),  # NEW: Add use_http2
                    timeout=server_config.get('timeout', 30),
                    retry_attempts=server_config.get('retry_attempts', 3),
                    retry_delay=server_config.get('retry_delay', 1.0),
                    max_message_size=server_config.get('max_message_size', 50 * 1024 * 1024),
                    keepalive=server_config.get('keepalive', True)  # NEW: Add keepalive
                )

                # DEBUG: Log the created ServerConfig
                logger.info(f"🔌 [DEBUG] Created ServerConfig for '{name}': ssl_verify={config.ssl_verify}")

                self.connection_manager.add_server(name, config)

            logger.info(f"🌐 Инициализировано {len(servers_config)} серверов")
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации серверов: {e}")
    
    def _setup_callbacks(self):
        """Настраивает callback'и"""
        self.connection_manager.set_connection_callback(self._on_connection_changed)
        self.connection_manager.set_error_callback(self._on_error)
    
    def _set_default_server(self):
        """Устанавливает сервер по умолчанию из конфигурации"""
        try:
            # Пытаемся получить сервер из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            # Получаем настройки gRPC клиента из секции integrations
            integrations = config.get('integrations', {})
            grpc_config = integrations.get('grpc_client', {})
            default_server = grpc_config.get('server', 'local')

            # DEBUG: Логируем выбор сервера
            logger.info(f"🔌 [DEBUG] Config says default server: '{default_server}'")
            logger.info(f"🔌 [DEBUG] Available servers: {list(self.connection_manager.servers.keys())}")

            # Устанавливаем сервер по умолчанию
            if default_server in self.connection_manager.servers:
                self.connection_manager.current_server = default_server
                logger.info(f"🌐 Установлен сервер по умолчанию: {default_server}")
            else:
                logger.warning(f"⚠️ Сервер '{default_server}' не найден, используем 'local'")
                self.connection_manager.current_server = 'local'

        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить конфигурацию gRPC: {e}")
            # Используем local по умолчанию
            self.connection_manager.current_server = 'local'
    
    def _on_connection_changed(self, state):
        """Обрабатывает изменения состояния соединения"""
        logger.info(f"🔄 Состояние соединения: {state.value}")
    
    def _on_error(self, error: Exception, context: str):
        """Обрабатывает ошибки"""
        logger.error(f"❌ Ошибка в {context}: {error}")
    
    async def connect(self, server_name: Optional[str] = None) -> bool:
        """Подключается к серверу"""
        return await self.connection_manager.connect(server_name)
    
    async def disconnect(self):
        """Отключается от сервера"""
        await self.connection_manager.disconnect()
    
    async def switch_server(self, server_name: str) -> bool:
        """Переключается на другой сервер"""
        return await self.connection_manager.switch_server(server_name)
    
    async def execute_with_retry(self, operation, *args, **kwargs):
        """Выполняет операцию с retry механизмом"""
        return await self.retry_manager.execute_with_retry(operation, *args, **kwargs)

    def get_connection_state(self):
        """Возвращает текущее состояние соединения"""
        return self.connection_manager.get_connection_state()
    
    def get_metrics(self):
        """Возвращает метрики соединения"""
        return self.connection_manager.get_metrics()
    
    def is_connected(self) -> bool:
        """Проверяет, подключен ли клиент"""
        return self.connection_manager.is_connected()
    
    async def stream_audio(self, prompt: str, screenshot_base64: str, screen_info: dict, hardware_id: str) -> AsyncGenerator[Any, None]:
        """Стриминг аудио и текста на сервер"""
        try:
            logger.info(f"🔍 screen_info type: {type(screen_info)}")
            logger.info(f"🔍 screen_info content: {screen_info}")
            
            if not self.is_connected():
                await self.connect()

            # Импортируем protobuf-модули с фолбэком на server/
            streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()
            
            # Создаем запрос
            if hasattr(screen_info, 'get'):
                # Это словарь
                screen_width = screen_info.get('width')
                screen_height = screen_info.get('height')
            elif hasattr(screen_info, 'width') and hasattr(screen_info, 'height'):
                # Это объект с атрибутами width и height
                screen_width = screen_info.width  # type: ignore[attr-defined]
                screen_height = screen_info.height  # type: ignore[attr-defined]
            else:
                # Неизвестный тип, используем значения по умолчанию
                logger.warning(f"⚠️ Неизвестный тип screen_info: {type(screen_info)}, используем значения по умолчанию")
                screen_width = None
                screen_height = None
            
            request = streaming_pb2.StreamRequest(
                prompt=prompt,
                screenshot=screenshot_base64,
                screen_width=screen_width,
                screen_height=screen_height,
                hardware_id=hardware_id,
                session_id=None
            )
            
            # Выполняем стриминг
            async for response in streaming_pb2_grpc.StreamingServiceStub(
                self.connection_manager.channel
            ).StreamAudio(request, timeout=30):
                yield response
                
        except Exception as e:
            logger.error(f"❌ Ошибка стриминга аудио: {e}")
            raise

    async def generate_welcome_audio(
        self,
        text: str,
        *,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        session_id: Optional[str] = None,
        timeout: Optional[float] = None,
        server_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Запрашивает серверную генерацию приветственного аудио.

        Returns dict c numpy массивом аудио и метаданными.
        """
        if not text or not text.strip():
            raise ValueError("Welcome text must be non-empty")

        target_server = server_name or self.connection_manager.current_server

        if not self.is_connected():
            await self.connect(target_server)
        elif server_name and self.connection_manager.current_server != server_name:
            await self.connection_manager.switch_server(server_name)

        streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()

        request = streaming_pb2.WelcomeRequest(
            text=text,
            session_id=session_id or f"welcome_{datetime.now().timestamp()}",
        )

        if voice:
            request.voice = voice
        if language:
            request.language = language

        stub = streaming_pb2_grpc.StreamingServiceStub(self.connection_manager.channel)
        rpc_timeout = timeout or self.config.get('welcome_timeout_sec', 30.0)

        audio_chunks: List[bytes] = []
        metadata: Dict[str, Any] = {}
        chunk_dtype: Optional[str] = None

        try:
            async for response in stub.GenerateWelcomeAudio(request, timeout=rpc_timeout):
                content = response.WhichOneof('content')
                if content == 'audio_chunk':
                    chunk = response.audio_chunk
                    if chunk.audio_data:
                        audio_bytes = bytes(chunk.audio_data)
                        if audio_bytes:
                            audio_chunks.append(audio_bytes)
                            chunk_dtype = chunk.dtype or chunk_dtype
                elif content == 'metadata':
                    metadata = {
                        'method': response.metadata.method,
                        'duration_sec': response.metadata.duration_sec,
                        'sample_rate': response.metadata.sample_rate,
                        'channels': response.metadata.channels,
                    }
                elif content == 'error_message':
                    raise RuntimeError(response.error_message)
                elif content == 'end_message':
                    break

        except Exception as e:
            logger.error(f"❌ Ошибка генерации приветственного аудио: {e}")
            raise

        if not audio_chunks:
            raise RuntimeError("Server returned no audio data")

        raw_bytes = b''.join(audio_chunks)
        dtype = (chunk_dtype or 'int16').lower()

        if dtype not in ('int16', 'pcm_s16le', 'short'):
            logger.warning(f"⚠️ Неподдерживаемый dtype '{dtype}', привожу к int16")
            dtype = 'int16'

        np_dtype = np.int16
        audio_array = np.frombuffer(raw_bytes, dtype=np_dtype)

        if metadata.get('channels', 1) > 1:
            try:
                audio_array = audio_array.reshape(-1, metadata['channels'])
            except Exception:
                logger.warning("⚠️ Не удалось изменить форму аудио по каналам, оставляю одномерный массив")

        # 🔍 ДИАГНОСТИКА: Финальные метаданные перед возвратом
        final_sample_rate = metadata.get('sample_rate', 24000)  # ИСПРАВЛЕНО: было 48000, должно быть 24000 согласно спецификации
        if final_sample_rate != 24000:
            logger.warning(
                f"⚠️ [GRPC_DIAG] Sample rate не соответствует спецификации! "
                f"Ожидается: 24000Hz, получено: {final_sample_rate}Hz"
            )
        
        # 🔍 ДИАГНОСТИКА: Вычисляем реальную длительность
        actual_samples = len(audio_array) if audio_array.ndim == 1 else audio_array.shape[0]
        calculated_duration = actual_samples / float(final_sample_rate) if final_sample_rate > 0 else 0.0
        logger.info(
            f"🔍 [GRPC_DIAG] Финальный результат: samples={actual_samples}, "
            f"sr={final_sample_rate}Hz, calculated_duration={calculated_duration:.3f}s, "
            f"metadata_duration={metadata.get('duration_sec', 'N/A')}"
        )
        
        result = {
            'audio': audio_array,
            'metadata': {
                'method': metadata.get('method', 'server'),
                'duration_sec': metadata.get('duration_sec'),
                'sample_rate': final_sample_rate,
                'channels': metadata.get('channels', 1),
                'dtype': 'int16',
            }
        }

        return result

    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.connection_manager.cleanup()
            logger.info("🧹 GrpcClient очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcClient: {e}")

    def _import_proto_modules(self) -> Tuple[Any, Any]:
        """Гибкий импорт streaming_pb2 и streaming_pb2_grpc.
        Сначала пробуем из proto директории модуля, затем fallback в server/.
        """
        # 1) Пытаемся импортировать из proto директории модуля
        try:
            # Путь: client/modules/grpc_client/proto/
            proto_dir = Path(__file__).resolve().parent.parent / 'proto'
            
            if proto_dir.exists() and str(proto_dir) not in sys.path:
                sys.path.insert(0, str(proto_dir))
                logger.info(f"✅ Добавлен путь к proto модулям: {proto_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из proto/")
            return pb2, pb2_grpc
        except Exception as local_err:
            logger.warning(f"⚠️ Не удалось импортировать из proto/: {local_err}")

        # 2) Пытаемся взять из server/ (репозиторий корень/ server)
        try:
            repo_root = Path(__file__).resolve().parents[4]
            server_dir = repo_root / 'server'
            
            # Проверяем существование и добавляем только если нужно
            if server_dir.exists() and str(server_dir) not in sys.path:
                sys.path.append(str(server_dir))
                logger.info(f"✅ Добавлен путь к server модулям: {server_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из server/")
            return pb2, pb2_grpc
        except Exception as e:
            raise ImportError(f"Unable to import protobuf modules (streaming_pb2*). Error: {e}")


"""
Основной gRPC клиент с модульной архитектурой
"""

import asyncio
import logging
from typing import Optional, Dict, Any, AsyncGenerator, Tuple, List
import importlib
import sys
from pathlib import Path
from datetime import datetime

import numpy as np

from integration.utils.resource_path import get_resource_path

from .types import ServerConfig, RetryConfig, HealthCheckConfig, RetryStrategy
from .retry_manager import RetryManager
from .connection_manager import ConnectionManager

logger = logging.getLogger(__name__)


class GrpcClient:  # type: ignore[no-redef]
    """Основной gRPC клиент с модульной архитектурой"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or self._create_default_config()
        
        # Модульные компоненты
        self.connection_manager = ConnectionManager()
        self.retry_manager = RetryManager(
            RetryConfig(
                max_attempts=self.config.get('max_retry_attempts', 3),
                base_delay=self.config.get('retry_delay', 1.0),
                strategy=RetryStrategy.EXPONENTIAL  # Используем enum вместо строки
            )
        )
        
        # Инициализация
        self._initialize_servers()
        self._setup_callbacks()
        
        # Устанавливаем сервер по умолчанию из конфигурации
        self._set_default_server()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Создает конфигурацию по умолчанию из централизованной системы"""
        try:
            # Загружаем конфигурацию из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
            
            grpc_data = config.get('grpc', {})
            servers_config = grpc_data.get('servers', {})
            
            # Преобразуем конфигурацию в формат, ожидаемый GrpcClient
            servers = {}
            for server_name, server_config in servers_config.items():
                server_dict = {
                    'address': server_config.get('host', '127.0.0.1'),
                    'port': server_config.get('port', 50051),
                    'use_ssl': server_config.get('ssl', False),
                    'ssl_verify': server_config.get('ssl_verify', True),
                    'grpc_path': server_config.get('grpc_path'),
                    'use_http2': server_config.get('use_http2', True),
                    'timeout': server_config.get('timeout', grpc_data.get('connection_timeout', 30)),
                    'retry_attempts': server_config.get('retry_attempts', grpc_data.get('retry_attempts', 3)),
                    'retry_delay': server_config.get('retry_delay', grpc_data.get('retry_delay', 1.0)),
                    'keepalive': server_config.get('keepalive', True)
                }
                # DEBUG: Логируем конфигурацию каждого сервера
                logger.info(f"🔌 [DEBUG] Loaded server '{server_name}': {server_dict['address']}:{server_dict['port']}, ssl={server_dict['use_ssl']}, ssl_verify={server_dict['ssl_verify']}")
                servers[server_name] = server_dict
            
            return {
                'servers': servers,
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': grpc_data.get('connection_timeout', 10),
                'max_retry_attempts': grpc_data.get('retry_attempts', 3),
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
            
        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить централизованную конфигурацию: {e}")
            # Fallback к минимальной конфигурации
            return {
                'servers': {
                    'local': {
                        'address': '127.0.0.1',
                        'port': 50051,
                        'use_ssl': False,
                        'timeout': 30,
                        'retry_attempts': 3,
                        'retry_delay': 1.0
                    }
                },
                'auto_fallback': True,
                'health_check_interval': 30,
                'connection_timeout': 10,
                'max_retry_attempts': 3,
                'retry_strategy': 'exponential',
                'circuit_breaker_threshold': 5,
                'circuit_breaker_timeout': 60,
                'welcome_timeout_sec': 30.0
            }
    
    def _initialize_servers(self):
        """Инициализирует конфигурации серверов"""
        try:
            servers_config = self.config.get('servers', {})
            for name, server_config in servers_config.items():
                # DEBUG: Log what we're reading from config dict
                ssl_verify_from_config = server_config.get('ssl_verify', True)
                logger.info(f"🔌 [DEBUG] _initialize_servers creating ServerConfig for '{name}': ssl_verify={ssl_verify_from_config}")

                config = ServerConfig(
                    address=server_config['address'],
                    port=server_config['port'],
                    use_ssl=server_config.get('use_ssl', False),
                    ssl_verify=ssl_verify_from_config,  # NEW: Add ssl_verify
                    grpc_path=server_config.get('grpc_path'),  # NEW: Add grpc_path
                    use_http2=server_config.get('use_http2', True),  # NEW: Add use_http2
                    timeout=server_config.get('timeout', 30),
                    retry_attempts=server_config.get('retry_attempts', 3),
                    retry_delay=server_config.get('retry_delay', 1.0),
                    max_message_size=server_config.get('max_message_size', 50 * 1024 * 1024),
                    keepalive=server_config.get('keepalive', True)  # NEW: Add keepalive
                )

                # DEBUG: Log the created ServerConfig
                logger.info(f"🔌 [DEBUG] Created ServerConfig for '{name}': ssl_verify={config.ssl_verify}")

                self.connection_manager.add_server(name, config)

            logger.info(f"🌐 Инициализировано {len(servers_config)} серверов")
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации серверов: {e}")
    
    def _setup_callbacks(self):
        """Настраивает callback'и"""
        self.connection_manager.set_connection_callback(self._on_connection_changed)
        self.connection_manager.set_error_callback(self._on_error)
    
    def _set_default_server(self):
        """Устанавливает сервер по умолчанию из конфигурации"""
        try:
            # Пытаемся получить сервер из unified_config.yaml
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)

            # Получаем настройки gRPC клиента из секции integrations
            integrations = config.get('integrations', {})
            grpc_config = integrations.get('grpc_client', {})
            default_server = grpc_config.get('server', 'local')

            # DEBUG: Логируем выбор сервера
            logger.info(f"🔌 [DEBUG] Config says default server: '{default_server}'")
            logger.info(f"🔌 [DEBUG] Available servers: {list(self.connection_manager.servers.keys())}")

            # Устанавливаем сервер по умолчанию
            if default_server in self.connection_manager.servers:
                self.connection_manager.current_server = default_server
                logger.info(f"🌐 Установлен сервер по умолчанию: {default_server}")
            else:
                logger.warning(f"⚠️ Сервер '{default_server}' не найден, используем 'local'")
                self.connection_manager.current_server = 'local'

        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить конфигурацию gRPC: {e}")
            # Используем local по умолчанию
            self.connection_manager.current_server = 'local'
    
    def _on_connection_changed(self, state):
        """Обрабатывает изменения состояния соединения"""
        logger.info(f"🔄 Состояние соединения: {state.value}")
    
    def _on_error(self, error: Exception, context: str):
        """Обрабатывает ошибки"""
        logger.error(f"❌ Ошибка в {context}: {error}")
    
    async def connect(self, server_name: Optional[str] = None) -> bool:
        """Подключается к серверу"""
        return await self.connection_manager.connect(server_name)
    
    async def disconnect(self):
        """Отключается от сервера"""
        await self.connection_manager.disconnect()
    
    async def switch_server(self, server_name: str) -> bool:
        """Переключается на другой сервер"""
        return await self.connection_manager.switch_server(server_name)
    
    async def execute_with_retry(self, operation, *args, **kwargs):
        """Выполняет операцию с retry механизмом"""
        return await self.retry_manager.execute_with_retry(operation, *args, **kwargs)

    def get_connection_state(self):
        """Возвращает текущее состояние соединения"""
        return self.connection_manager.get_connection_state()
    
    def get_metrics(self):
        """Возвращает метрики соединения"""
        return self.connection_manager.get_metrics()
    
    def is_connected(self) -> bool:
        """Проверяет, подключен ли клиент"""
        return self.connection_manager.is_connected()
    
    async def stream_audio(self, prompt: str, screenshot_base64: str, screen_info: dict, hardware_id: str) -> AsyncGenerator[Any, None]:
        """Стриминг аудио и текста на сервер"""
        try:
            logger.info(f"🔍 screen_info type: {type(screen_info)}")
            logger.info(f"🔍 screen_info content: {screen_info}")
            
            if not self.is_connected():
                await self.connect()

            # Импортируем protobuf-модули с фолбэком на server/
            streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()
            
            # Создаем запрос
            if hasattr(screen_info, 'get'):
                # Это словарь
                screen_width = screen_info.get('width')
                screen_height = screen_info.get('height')
            elif hasattr(screen_info, 'width') and hasattr(screen_info, 'height'):
                # Это объект с атрибутами width и height
                screen_width = screen_info.width  # type: ignore[attr-defined]
                screen_height = screen_info.height  # type: ignore[attr-defined]
            else:
                # Неизвестный тип, используем значения по умолчанию
                logger.warning(f"⚠️ Неизвестный тип screen_info: {type(screen_info)}, используем значения по умолчанию")
                screen_width = None
                screen_height = None
            
            request = streaming_pb2.StreamRequest(
                prompt=prompt,
                screenshot=screenshot_base64,
                screen_width=screen_width,
                screen_height=screen_height,
                hardware_id=hardware_id,
                session_id=None
            )
            
            # Выполняем стриминг
            async for response in streaming_pb2_grpc.StreamingServiceStub(
                self.connection_manager.channel
            ).StreamAudio(request, timeout=30):
                yield response
                
        except Exception as e:
            logger.error(f"❌ Ошибка стриминга аудио: {e}")
            raise

    async def generate_welcome_audio(
        self,
        text: str,
        *,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        session_id: Optional[str] = None,
        timeout: Optional[float] = None,
        server_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Запрашивает серверную генерацию приветственного аудио.

        Returns dict c numpy массивом аудио и метаданными.
        """
        if not text or not text.strip():
            raise ValueError("Welcome text must be non-empty")

        target_server = server_name or self.connection_manager.current_server

        if not self.is_connected():
            await self.connect(target_server)
        elif server_name and self.connection_manager.current_server != server_name:
            await self.connection_manager.switch_server(server_name)

        streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()

        request = streaming_pb2.WelcomeRequest(
            text=text,
            session_id=session_id or f"welcome_{datetime.now().timestamp()}",
        )

        if voice:
            request.voice = voice
        if language:
            request.language = language

        stub = streaming_pb2_grpc.StreamingServiceStub(self.connection_manager.channel)
        rpc_timeout = timeout or self.config.get('welcome_timeout_sec', 30.0)

        audio_chunks: List[bytes] = []
        metadata: Dict[str, Any] = {}
        chunk_dtype: Optional[str] = None

        try:
            async for response in stub.GenerateWelcomeAudio(request, timeout=rpc_timeout):
                content = response.WhichOneof('content')
                if content == 'audio_chunk':
                    chunk = response.audio_chunk
                    if chunk.audio_data:
                        audio_bytes = bytes(chunk.audio_data)
                        if audio_bytes:
                            audio_chunks.append(audio_bytes)
                            chunk_dtype = chunk.dtype or chunk_dtype
                elif content == 'metadata':
                    metadata = {
                        'method': response.metadata.method,
                        'duration_sec': response.metadata.duration_sec,
                        'sample_rate': response.metadata.sample_rate,
                        'channels': response.metadata.channels,
                    }
                elif content == 'error_message':
                    raise RuntimeError(response.error_message)
                elif content == 'end_message':
                    break

        except Exception as e:
            logger.error(f"❌ Ошибка генерации приветственного аудио: {e}")
            raise

        if not audio_chunks:
            raise RuntimeError("Server returned no audio data")

        raw_bytes = b''.join(audio_chunks)
        dtype = (chunk_dtype or 'int16').lower()

        if dtype not in ('int16', 'pcm_s16le', 'short'):
            logger.warning(f"⚠️ Неподдерживаемый dtype '{dtype}', привожу к int16")
            dtype = 'int16'

        np_dtype = np.int16
        audio_array = np.frombuffer(raw_bytes, dtype=np_dtype)

        if metadata.get('channels', 1) > 1:
            try:
                audio_array = audio_array.reshape(-1, metadata['channels'])
            except Exception:
                logger.warning("⚠️ Не удалось изменить форму аудио по каналам, оставляю одномерный массив")

        # 🔍 ДИАГНОСТИКА: Финальные метаданные перед возвратом
        final_sample_rate = metadata.get('sample_rate', 24000)  # ИСПРАВЛЕНО: было 48000, должно быть 24000 согласно спецификации
        if final_sample_rate != 24000:
            logger.warning(
                f"⚠️ [GRPC_DIAG] Sample rate не соответствует спецификации! "
                f"Ожидается: 24000Hz, получено: {final_sample_rate}Hz"
            )
        
        # 🔍 ДИАГНОСТИКА: Вычисляем реальную длительность
        actual_samples = len(audio_array) if audio_array.ndim == 1 else audio_array.shape[0]
        calculated_duration = actual_samples / float(final_sample_rate) if final_sample_rate > 0 else 0.0
        logger.info(
            f"🔍 [GRPC_DIAG] Финальный результат: samples={actual_samples}, "
            f"sr={final_sample_rate}Hz, calculated_duration={calculated_duration:.3f}s, "
            f"metadata_duration={metadata.get('duration_sec', 'N/A')}"
        )
        
        result = {
            'audio': audio_array,
            'metadata': {
                'method': metadata.get('method', 'server'),
                'duration_sec': metadata.get('duration_sec'),
                'sample_rate': final_sample_rate,
                'channels': metadata.get('channels', 1),
                'dtype': 'int16',
            }
        }

        return result

    async def cleanup(self):
        """Очистка ресурсов"""
        try:
            await self.connection_manager.cleanup()
            logger.info("🧹 GrpcClient очищен")
        except Exception as e:
            logger.error(f"❌ Ошибка очистки GrpcClient: {e}")

    def _import_proto_modules(self) -> Tuple[Any, Any]:
        """Гибкий импорт streaming_pb2 и streaming_pb2_grpc.
        Сначала пробуем из proto директории модуля, затем fallback в server/.
        """
        # 1) Пытаемся импортировать из proto директории модуля
        try:
            # Путь: client/modules/grpc_client/proto/
            proto_dir = Path(__file__).resolve().parent.parent / 'proto'
            
            if proto_dir.exists() and str(proto_dir) not in sys.path:
                sys.path.insert(0, str(proto_dir))
                logger.info(f"✅ Добавлен путь к proto модулям: {proto_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из proto/")
            return pb2, pb2_grpc
        except Exception as local_err:
            logger.warning(f"⚠️ Не удалось импортировать из proto/: {local_err}")

        # 2) Пытаемся взять из server/ (репозиторий корень/ server)
        try:
            repo_root = Path(__file__).resolve().parents[4]
            server_dir = repo_root / 'server'
            
            # Проверяем существование и добавляем только если нужно
            if server_dir.exists() and str(server_dir) not in sys.path:
                sys.path.append(str(server_dir))
                logger.info(f"✅ Добавлен путь к server модулям: {server_dir}")
            
            pb2 = importlib.import_module('streaming_pb2')
            pb2_grpc = importlib.import_module('streaming_pb2_grpc')
            logger.info("✅ Protobuf модули успешно импортированы из server/")
            return pb2, pb2_grpc
        except Exception as e:
            raise ImportError(f"Unable to import protobuf modules (streaming_pb2*). Error: {e}")
