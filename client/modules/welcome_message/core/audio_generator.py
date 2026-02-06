# ruff: noqa: I001
"""Welcome Audio Generator — серверный источник приветствия."""

import logging
from typing import Any

import numpy as np

from modules.grpc_client.core.grpc_client import GrpcClient
from config.unified_config_loader import UnifiedConfigLoader

from .types import WelcomeConfig

logger = logging.getLogger(__name__)


class WelcomeAudioGenerator:
    """Генератор аудио для приветственного сообщения"""

    def __init__(
        self,
        config: WelcomeConfig,
        *,
        grpc_client: GrpcClient | None = None,
        grpc_server_name: str | None = None,
        grpc_timeout: float | None = None,
    ):
        self.config = config
        self._last_server_metadata: dict[str, Any] = {}

        self._grpc_client: GrpcClient | None = grpc_client
        self._grpc_client_config: dict[str, Any] | None = None
        self._grpc_server_name: str | None = grpc_server_name
        self._grpc_timeout: float = float(
            grpc_timeout if grpc_timeout is not None else config.server_timeout_sec
        )

        if self._grpc_client is None:
            self._load_grpc_settings()

    async def generate_audio(self, text: str) -> np.ndarray | None:
        """Генерирует аудио на сервере (совместимость API)."""
        return await self.generate_server_audio(text)

    async def generate_server_audio(self, text: str) -> np.ndarray | None:
        """Пытается получить приветствие только с сервера"""
        if not self.config.use_server:
            return None
        return await self._generate_with_server(text)

    async def _generate_with_server(self, text: str) -> np.ndarray | None:
        """Запрашивает генерацию приветствия на сервере"""
        logger.info("TRACE [WELCOME_GEN] _generate_with_server: START")
        if not text:
            logger.error("❌ [WELCOME_AUDIO] Пустой текст приветствия")
            return None

        client = self._ensure_grpc_client()
        if not client:
            logger.error("❌ [WELCOME_AUDIO] GrpcClient is None")
            return None

        try:
            logger.info(f"TRACE [WELCOME_GEN] calling client.generate_welcome_audio(timeout={self._grpc_timeout})")
            result = await client.generate_welcome_audio(
                text=text,
                voice=self.config.voice,
                language=None,
                server_name=self._grpc_server_name,
                timeout=self._grpc_timeout,
            )
            logger.info("TRACE [WELCOME_GEN] client.generate_welcome_audio returned")
            
            audio_array: np.ndarray | None = result.get('audio')
            metadata = result.get('metadata', {})
            self._last_server_metadata = metadata

            # 🔍 ДИАГНОСТИКА: Логируем RAW данные от gRPC клиента
            logger.info(
                f"🔍 [WELCOME_AUDIO_DIAG] Данные от gRPC клиента: "
                f"metadata={metadata}, audio_shape={audio_array.shape if audio_array is not None else 'None'}, "
                f"audio_dtype={audio_array.dtype if audio_array is not None else 'None'}"
            )

            if audio_array is None or len(audio_array) == 0:
                logger.error("❌ [WELCOME_AUDIO] Сервер вернул пустое аудио")
                return None

            sample_rate = metadata.get('sample_rate') or self.config.sample_rate
            channels = metadata.get('channels') or self.config.channels
            
            # 🔍 ДИАГНОСТИКА: Вычисляем ожидаемую длительность
            audio_samples = audio_array.size if hasattr(audio_array, 'size') else len(audio_array)
            expected_duration = audio_samples / float(sample_rate) if sample_rate > 0 else 0.0
            logger.info(
                f"🔍 [WELCOME_AUDIO_DIAG] Параметры аудио: samples={audio_samples}, "
                f"sr={sample_rate}Hz, ch={channels}, expected_duration={expected_duration:.3f}s, "
                f"config_sr={self.config.sample_rate}Hz"
            )

            if sample_rate != self.config.sample_rate or channels != self.config.channels:
                config_duration = audio_samples / float(self.config.sample_rate) if self.config.sample_rate > 0 else 0.0
                speed_factor = sample_rate / float(self.config.sample_rate) if self.config.sample_rate > 0 else 1.0
                logger.warning(
                    f"⚠️ [WELCOME_AUDIO_DIAG] Несовпадение формата: server_sr={sample_rate}Hz, "
                    f"config_sr={self.config.sample_rate}Hz, server_ch={channels}, config_ch={self.config.channels}, "
                    f"speed_factor={speed_factor:.2f}x, expected_duration={expected_duration:.3f}s, "
                    f"config_duration={config_duration:.3f}s"
                )
                # Пока не выполняем ресэмплинг, сообщаем в лог.

            logger.info("TRACE [WELCOME_GEN] _generate_with_server: SUCCESS")
            return audio_array
            
        except ImportError as e:
            logger.error(f"❌ [WELCOME_AUDIO] ImportError (missing deps?): {e}")
            return None
        except Exception as exc:
            logger.error(f"❌ [WELCOME_AUDIO] Ошибка серверной генерации: {exc}")
            import traceback
            logger.error(traceback.format_exc())
            return None
        except BaseException as be:
            logger.critical(f"🛑 [WELCOME_AUDIO] FATAL ERROR/CANCELLED: {type(be).__name__}: {be}")
            import traceback
            logger.critical(traceback.format_exc())
            raise

    def get_last_server_metadata(self) -> dict[str, Any]:
        """Возвращает метаданные последней серверной генерации"""
        return self._last_server_metadata

    def _load_grpc_settings(self):
        try:
            # ЦЕНТРАЛИЗОВАНО: Используем ServerManager для получения сервера
            from config.server_manager import get_default_server
            
            loader = UnifiedConfigLoader.get_instance()
            config_data = loader._load_config()
            integrations_cfg = (config_data.get('integrations') or {}).get('grpc_client', {})
            
            # Используем централизованный ServerManager вместо прямого чтения конфига
            self._grpc_server_name = get_default_server() or 'local'
            integration_timeout = float(integrations_cfg.get('request_timeout_sec', self._grpc_timeout))
            self._grpc_timeout = float(self.config.server_timeout_sec or integration_timeout)

            network_cfg = loader.get_network_config()
            servers_cfg: dict[str, dict[str, Any]] = {}
            for name, server in network_cfg.grpc_servers.items():
                servers_cfg[name] = {
                    'address': server.host,
                    'port': server.port,
                    'use_ssl': server.ssl,
                    'ssl_verify': server.ssl_verify,  # NEW: Pass ssl_verify from config
                    'use_http2': server.use_http2,  # NEW: Pass use_http2 from config
                    'keepalive': server.keepalive,  # NEW: Pass keepalive from config
                    'grpc_path': server.grpc_path,  # NEW: Pass grpc_path from config
                    'timeout': server.timeout,
                    'retry_attempts': server.retry_attempts,
                    'retry_delay': server.retry_delay,
                }

            self._grpc_client_config = {
                'servers': servers_cfg,
                'auto_fallback': network_cfg.auto_fallback,
                'connection_timeout': network_cfg.connection_check_interval,
                'max_retry_attempts': int(integrations_cfg.get('max_retries', 3)),
                'retry_delay': float(integrations_cfg.get('retry_delay', 1.0)),
                'welcome_timeout_sec': self._grpc_timeout,
            }
        except Exception as exc:
            logger.warning(f"⚠️ [WELCOME_AUDIO] Не удалось загрузить настройки gRPC: {exc}")
            self._grpc_client_config = None
            self._grpc_server_name = None
            self._grpc_timeout = 30.0

    def _ensure_grpc_client(self) -> GrpcClient | None:
        try:
            if self._grpc_client is None:
                logger.error(
                    "❌ [WELCOME_AUDIO] GrpcClient not injected. "
                    "WelcomeMessageIntegration should provide the client."
                )
                return None
            return self._grpc_client
        except Exception as exc:
            logger.error(f"❌ [WELCOME_AUDIO] Ошибка создания gRPC клиента: {exc}")
            self._grpc_client = None
            return None

    def set_grpc_client(self, grpc_client: GrpcClient | None) -> None:
        """Обновить gRPC клиент (отложенная инъекция)."""
        self._grpc_client = grpc_client
