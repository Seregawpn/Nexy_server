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

# Импорт для получения server_audio_format (источник истины)
try:
    from config.unified_config_loader import UnifiedConfigLoader
except ImportError:
    UnifiedConfigLoader = None

logger = logging.getLogger(__name__)


class GrpcClient:
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
        """Настраивает callback функции"""
        self.connection_manager.set_connection_callback(self._on_connection_changed)
        self.connection_manager.set_error_callback(self._on_error)
    
    def _get_server_audio_format(self) -> Dict[str, Any]:
        """
        Получает server_audio_format из unified_config (источник истины)
            
        Returns:
            Dict с полями sample_rate, channels, dtype
        """
        # Попытка 1: UnifiedConfigLoader (предпочтительный способ)
        if UnifiedConfigLoader is not None:
            try:
                unified_config = UnifiedConfigLoader.get_instance()
                config = unified_config._load_config()
                server_audio_format = config.get('server_audio_format', {})
                return {
                    'sample_rate': server_audio_format.get('sample_rate', 48000),
                    'channels': server_audio_format.get('channels', 1),
                    'dtype': server_audio_format.get('dtype', 'int16')
                }
            except Exception as e:
                logger.warning(f"⚠️ Не удалось загрузить server_audio_format из UnifiedConfigLoader: {e}")
        
        # Fallback: загружаем напрямую из YAML
        try:
            import yaml
            config_path = get_resource_path('config/unified_config.yaml')
            with open(config_path, 'r') as f:
                config = yaml.safe_load(f)
                server_audio_format = config.get('server_audio_format', {})
                return {
                    'sample_rate': server_audio_format.get('sample_rate', 48000),
                    'channels': server_audio_format.get('channels', 1),
                    'dtype': server_audio_format.get('dtype', 'int16')
                }
        except Exception as e:
            logger.warning(f"⚠️ Не удалось загрузить server_audio_format из YAML: {e}")
        
        # Последний fallback: значения по умолчанию (Edge TTS = 48k)
            return {
            'sample_rate': 48000,
            'channels': 1,
            'dtype': 'int16'
        }
    
    def _set_default_server(self):
        """Устанавливает сервер по умолчанию из конфигурации"""
        try:
            # ЦЕНТРАЛИЗОВАНО: Используем ServerManager вместо прямого чтения YAML
            from config.server_manager import get_default_server
            
            default_server = get_default_server() or 'local'

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
    
    async def stream_audio(
        self,
        prompt: str,
        screenshot_base64: str,
        screen_info: dict,
        hardware_id: str,
        session_id: str,
        *,
        timeout: Optional[float] = None,
    ) -> AsyncGenerator[Any, None]:
        """Стриминг аудио и текста на сервер
        
        Args:
            prompt: Текстовая команда пользователя
            screenshot_base64: Base64-кодированный скриншот
            screen_info: Информация о размере экрана (dict с 'width' и 'height' или объект с атрибутами)
            hardware_id: Уникальный Hardware ID оборудования
            session_id: ID сессии (обязателен, единственный источник истины - ApplicationStateManager)
        """
        # КРИТИЧНО: Fail-fast проверка session_id
        # Преобразуем session_id в строку (может быть float или другой тип)
        session_id = str(session_id) if session_id is not None else ""
        if not session_id or not session_id.strip():
            error_msg = "session_id is required and must be provided (Source of Truth: ApplicationStateManager)"
            logger.error(f"❌ [gRPC] {error_msg}")
            raise ValueError(error_msg)
        
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
                session_id=session_id  # КРИТИЧНО: передаем session_id из ApplicationStateManager
            )
            
            # Выполняем стриминг
            rpc_timeout = timeout if timeout and timeout > 0 else None
            async for response in streaming_pb2_grpc.StreamingServiceStub(
                self.connection_manager.channel
            ).StreamAudio(request, timeout=rpc_timeout):
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
                        'dtype': getattr(response.metadata, 'dtype', None),  # Проверяем dtype из metadata
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
        
        # Определяем dtype: приоритет metadata.dtype > chunk_dtype > server_audio_format > fallback int16
        metadata_dtype = metadata.get('dtype')
        if metadata_dtype:
            dtype_str = str(metadata_dtype).lower()
        elif chunk_dtype:
            dtype_str = str(chunk_dtype).lower()
        else:
            # Fallback: используем server_audio_format или int16
            server_audio_format = self._get_server_audio_format()
            dtype_str = str(server_audio_format.get('dtype', 'int16')).lower()
        
        # Нормализуем dtype и выбираем numpy тип
        if dtype_str in ('int16', 'pcm_s16le', 'short', 's16'):
            np_dtype = np.int16
            dtype_str = 'int16'
        elif dtype_str in ('float32', 'float', 'f32'):
            np_dtype = np.float32
            dtype_str = 'float32'
        elif dtype_str in ('int32', 's32'):
            np_dtype = np.int32
            dtype_str = 'int32'
        else:
            logger.warning(f"⚠️ Неподдерживаемый dtype '{dtype_str}', привожу к int16")
            np_dtype = np.int16
            dtype_str = 'int16'
        
        audio_array = np.frombuffer(raw_bytes, dtype=np_dtype)

        # 🔍 ДИАГНОСТИКА: Финальные метаданные перед возвратом
        # Приоритет: metadata от сервера > server_audio_format (источник истины) > fallback
        server_audio_format = self._get_server_audio_format()
        
        # Если metadata содержит sample_rate/channels/dtype → используем их (приоритет metadata)
        # Если нет → используем server_audio_format (источник истины)
        # dtype уже определен выше при декодировании (dtype_str)
        metadata_sr = metadata.get('sample_rate')
        metadata_ch = metadata.get('channels')
        
        final_sample_rate = int(metadata_sr) if metadata_sr is not None else int(server_audio_format.get('sample_rate', 48000))
        final_channels = int(metadata_ch) if metadata_ch is not None else int(server_audio_format.get('channels', 1))
        final_dtype = dtype_str  # Используем dtype, определенный при декодировании
        
        # Используем final_channels для reshape (безопасно, даже если metadata пустая)
        if final_channels > 1:
            try:
                audio_array = audio_array.reshape(-1, final_channels)
            except Exception:
                logger.warning("⚠️ Не удалось изменить форму аудио по каналам, оставляю одномерный массив")

        logger.info(
            f"🔍 [GRPC_DIAG] Финальный sample_rate: {final_sample_rate}Hz "
            f"(из metadata: {metadata.get('sample_rate', 'N/A')}, "
            f"из server_audio_format: {server_audio_format.get('sample_rate', 'N/A')})"
            )
        
        # 🔍 ДИАГНОСТИКА: Вычисляем реальную длительность
        actual_samples = len(audio_array) if audio_array.ndim == 1 else audio_array.shape[0]
        calculated_duration = actual_samples / float(final_sample_rate) if final_sample_rate > 0 else 0.0
        metadata_duration = metadata.get('duration_sec')
        logger.info(
            f"🔍 [GRPC_DIAG] Финальный результат: samples={actual_samples}, "
            f"sr={final_sample_rate}Hz, calculated_duration={calculated_duration:.3f}s, "
            f"metadata_duration={metadata_duration if metadata_duration is not None else 'N/A'}"
        )
        
        result = {
            'audio': audio_array,
            'metadata': {
                'method': metadata.get('method', 'server'),
                'duration_sec': metadata.get('duration_sec'),
                'sample_rate': final_sample_rate,
                'channels': final_channels,
                'dtype': final_dtype,
            }
        }

        return result

    async def stream_tts_audio(
        self,
        text: str,
        *,
        voice: Optional[str] = None,
        language: Optional[str] = None,
        session_id: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """Streams TTS audio chunks via GenerateWelcomeAudio.
        
        Unlike generate_welcome_audio which buffers all audio, this yields each chunk
        immediately for real-time playback.
        
        Yields:
            Dict with 'audio_chunk' data: dtype, sample_rate, channels, bytes
        """
        if not text or not text.strip():
            logger.warning("stream_tts_audio called with empty text")
            return

        if not self.is_connected():
            await self.connect()

        streaming_pb2, streaming_pb2_grpc = self._import_proto_modules()

        request = streaming_pb2.WelcomeRequest(
            text=text,
            session_id=session_id or f"tts_{datetime.now().timestamp()}",
        )
        if voice:
            request.voice = voice
        if language:
            request.language = language

        stub = streaming_pb2_grpc.StreamingServiceStub(self.connection_manager.channel)
        rpc_timeout = timeout or self.config.get('welcome_timeout_sec', 30.0)

        try:
            async for response in stub.GenerateWelcomeAudio(request, timeout=rpc_timeout):
                content = response.WhichOneof('content')
                if content == 'audio_chunk':
                    ch = response.audio_chunk
                    if ch.audio_data and len(ch.audio_data) > 0:
                        yield {
                            'type': 'audio_chunk',
                            'bytes': bytes(ch.audio_data),
                            'dtype': ch.dtype or 'int16',
                            'sample_rate': ch.sample_rate or 48000,
                            'channels': ch.channels or 1,
                            'shape': list(ch.shape) if ch.shape else [],
                        }
                elif content == 'metadata':
                    yield {
                        'type': 'metadata',
                        'method': response.metadata.method,
                        'duration_sec': response.metadata.duration_sec,
                        'sample_rate': response.metadata.sample_rate,
                        'channels': response.metadata.channels,
                    }
                elif content == 'error_message':
                    logger.error(f"TTS error: {response.error_message}")
                    yield {'type': 'error', 'message': response.error_message}
                    break
                elif content == 'end_message':
                    yield {'type': 'end', 'message': response.end_message}
                    break
        except Exception as e:
            logger.error(f"❌ stream_tts_audio error: {e}")
            yield {'type': 'error', 'message': str(e)}

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
