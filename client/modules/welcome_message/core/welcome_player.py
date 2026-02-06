"""
Welcome Player — воспроизведение приветствия, сгенерированного на сервере.
"""

import logging
from typing import Any, Callable

import numpy as np

from modules.grpc_client.core.grpc_client import GrpcClient

from .audio_generator import WelcomeAudioGenerator
from .types import WelcomeConfig, WelcomeResult, WelcomeState

logger = logging.getLogger(__name__)


class WelcomePlayer:
    """Плеер для воспроизведения приветственного сообщения"""
    
    def __init__(
        self,
        config: WelcomeConfig,
        *,
        grpc_client: GrpcClient | None = None,
        grpc_server_name: str | None = None,
        grpc_timeout: float | None = None,
    ):
        self.config = config
        self.state = WelcomeState.IDLE
        self.audio_generator = WelcomeAudioGenerator(
            config,
            grpc_client=grpc_client,
            grpc_server_name=grpc_server_name,
            grpc_timeout=grpc_timeout,
        )
        
        # Коллбеки
        self._on_started: Callable[[], None] | None = None
        self._on_completed: Callable[[WelcomeResult], None] | None = None
        self._on_error: Callable[[str], None] | None = None
        
        # Последнее подготовленное аудио и метаданные
        self._last_audio: np.ndarray | None = None
        self._last_metadata: dict[str, Any] | None = None

    def set_grpc_client(self, grpc_client: GrpcClient | None) -> None:
        """Обновить gRPC клиент в генераторе аудио."""
        self.audio_generator.set_grpc_client(grpc_client)
    
    def set_callbacks(
        self,
        on_started: Callable[[], None] | None = None,
        on_completed: Callable[[WelcomeResult], None] | None = None,
        on_error: Callable[[str], None] | None = None
    ):
        """Установить коллбеки для событий"""
        self._on_started = on_started
        self._on_completed = on_completed
        self._on_error = on_error
    
    async def play_welcome(self) -> WelcomeResult:
        """
        Воспроизводит приветственное сообщение

        Returns:
            WelcomeResult с результатом воспроизведения
        """
        try:
            logger.info("🎵 [WELCOME_PLAYER] Начинаю воспроизведение приветствия")
            logger.info(f"🔍 [WELCOME_PLAYER] config.enabled={self.config.enabled}, config.use_server={self.config.use_server}")
            self.state = WelcomeState.LOADING
            self._last_audio = None
            self._last_metadata = None

            # Проверяем, включен ли модуль
            if not self.config.enabled:
                error_msg = "Модуль приветствия отключен в конфигурации"
                logger.info(f"🔇 [WELCOME_PLAYER] {error_msg}")
                self.state = WelcomeState.ERROR
                
                result = WelcomeResult(
                    success=False,
                    method="none",
                    duration_sec=0.0,
                    error=error_msg
                )
                
                if self._on_error:
                    self._on_error(error_msg)
                if self._on_completed:
                    self._on_completed(result)
                
                return result
            
            # Уведомляем о начале
            if self._on_started:
                self._on_started()
            
            if not self.config.use_server:
                error_msg = "Серверное воспроизведение приветствия отключено в конфигурации"
                logger.error(f"❌ [WELCOME_PLAYER] {error_msg}")
                self.state = WelcomeState.ERROR

                result = WelcomeResult(
                    success=False,
                    method="none",
                    duration_sec=0.0,
                    error=error_msg
                )

                if self._on_error:
                    self._on_error(error_msg)
                if self._on_completed:
                    self._on_completed(result)

                return result

            logger.info("🔍 [WELCOME_PLAYER] Запрашиваю серверное аудио...")
            logger.info("TRACE [WELCOME_PLAYER] calling _play_server_audio()")
            server_result = await self._play_server_audio()
            logger.info(f"TRACE [WELCOME_PLAYER] _play_server_audio() returned: success={server_result.success}")
            logger.info(f"🔍 [WELCOME_PLAYER] Серверное аудио получено: success={server_result.success}, error={server_result.error}")

            if server_result.success:
                logger.info("✅ [WELCOME_PLAYER] Серверное приветствие воспроизведено успешно")
                self.state = WelcomeState.COMPLETED
                if self._on_completed:
                    logger.info("🔍 [WELCOME_PLAYER] Вызываю _on_completed callback")
                    self._on_completed(server_result)
                return server_result

            # FALLBACK: Если серверное воспроизведение не удалось, используем локальный синтез
            logger.warning(f"⚠️ [WELCOME_PLAYER] Серверное воспроизведение не удалось: {server_result.error}")
            logger.info("🔄 [WELCOME_PLAYER] Переключаюсь на локальный fallback (macOS say)...")
            
            fallback_result = await self._play_local_fallback()
            
            if fallback_result.success:
                logger.info("✅ [WELCOME_PLAYER] Локальное приветствие (fallback) воспроизведено успешно")
                self.state = WelcomeState.COMPLETED
                if self._on_completed:
                    self._on_completed(fallback_result)
                return fallback_result

            # Если и fallback не удался
            error_msg = fallback_result.error or "Воспроизведение приветствия (сервер + fallback) не удалось"
            logger.error(f"❌ [WELCOME_PLAYER] {error_msg}")
            self.state = WelcomeState.ERROR

            result = WelcomeResult(
                success=False,
                method="none",
                duration_sec=0.0,
                error=error_msg
            )

            if self._on_error:
                logger.info("🔍 [WELCOME_PLAYER] Вызываю _on_error callback")
                self._on_error(error_msg)
            if self._on_completed:
                logger.info("🔍 [WELCOME_PLAYER] Вызываю _on_completed callback (ошибка)")
                self._on_completed(result)

            return result

        except Exception as e:
            error_msg = f"Критическая ошибка воспроизведения приветствия: {e}"
            logger.error(f"❌ [WELCOME_PLAYER] {error_msg}")
            logger.exception(f"❌ [WELCOME_PLAYER] Stack trace:")
            self.state = WelcomeState.ERROR
            
            result = WelcomeResult(
                success=False,
                method="error",
                duration_sec=0.0,
                error=error_msg
            )
            
            if self._on_error:
                self._on_error(error_msg)
            if self._on_completed:
                self._on_completed(result)
            
            return result
        except BaseException as be:
            logger.critical(f"🛑 [WELCOME_PLAYER] FATAL ERROR/CANCELLED: {type(be).__name__}: {be}")
            import traceback
            logger.critical(traceback.format_exc())
            self.state = WelcomeState.ERROR
            raise
    
    async def _play_server_audio(self) -> WelcomeResult:
        """Пытается воспроизвести приветствие, сгенерированное на сервере"""
        try:
            logger.info(f"🔍 [WELCOME_PLAYER] Генерирую аудио для текста: '{self.config.text}'")
            audio_data = await self.audio_generator.generate_server_audio(self.config.text)
            logger.info(f"🔍 [WELCOME_PLAYER] audio_data is None: {audio_data is None}")

            if audio_data is None:
                logger.error("❌ [WELCOME_PLAYER] Серверная генерация вернула None!")
                return WelcomeResult(
                    success=False,
                    method="server",
                    duration_sec=0.0,
                    error="Серверная генерация вернула пустой результат"
                )

            logger.info(f"🔍 [WELCOME_PLAYER] audio_data.shape={audio_data.shape}, dtype={audio_data.dtype}")

            server_metadata = self.audio_generator.get_last_server_metadata()
            sample_rate = server_metadata.get('sample_rate', self.config.sample_rate)
            channels = server_metadata.get('channels', self.config.channels)

            total_samples = int(audio_data.size if hasattr(audio_data, 'size') else len(audio_data))
            if audio_data.ndim > 1:
                frame_count = audio_data.shape[0]
            else:
                frame_count = total_samples // max(1, channels)
            duration_sec = frame_count / float(sample_rate)

            logger.info(f"🔍 [WELCOME_PLAYER] sample_rate={sample_rate}, channels={channels}, duration={duration_sec:.2f}s")

            metadata = {
                "sample_rate": sample_rate,
                "channels": channels,
                "samples": total_samples,
                "frames": frame_count,
                "method": server_metadata.get('method', 'server'),
                "duration_sec": server_metadata.get('duration_sec', duration_sec),
            }

            self._last_audio = audio_data
            self._last_metadata = metadata

            logger.info("✅ [WELCOME_PLAYER] Серверное аудио успешно подготовлено")

            # ВАЖНО: WelcomePlayer только подготавливает данные.
            # Реальное воспроизведение происходит в интеграции через speech_playback_integration.
            # Но для архитектурной целостности мы возвращаем успех тут, 
            # подразумевая что данные готовы к передаче в общий плеер.
            
            return WelcomeResult(
                success=True,
                method="server",
                duration_sec=duration_sec,
                metadata=metadata
            )

        except Exception as e:
            logger.error(f"❌ [WELCOME_PLAYER] Ошибка в _play_server_audio: {e}")
            logger.exception(f"❌ [WELCOME_PLAYER] Stack trace:")
            return WelcomeResult(
                success=False,
                method="server",
                duration_sec=0.0,
                error=f"Ошибка серверной генерации: {e}"
            )

    async def _play_local_fallback(self) -> WelcomeResult:
        """
        Запасной вариант: воспроизведение через macOS 'say'
        """
        import asyncio

        try:
            text = self.config.text
            if not text:
                return WelcomeResult(False, "local", 0.0, "Empty text for fallback")

            logger.info(f"🗣️ [WELCOME_PLAYER] Запуск локального синтеза: '{text}'")
            
            # Запускаем 'say' в отдельном процессе, чтобы не блокировать loop
            # Используем asyncio.create_subprocess_exec для асинхронности
            process = await asyncio.create_subprocess_exec(
                "say", text,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Ждем завершения (это блокирует текущую задачу, но не loop, пока 'say' говорит)
            # 'say' завершается только когда договорит.
            await process.wait()
            
            if process.returncode != 0:
                stderr_data = await process.stderr.read() if process.stderr else b""
                error_msg = f"Local 'say' command failed: {stderr_data.decode().strip()}"
                logger.error(f"❌ [WELCOME_PLAYER] {error_msg}")
                return WelcomeResult(False, "local", 0.0, error_msg)

            # Оценка длительности очень приблизительная, но для fallback не критично
            approx_duration = len(text) * 0.06  # ~16 chars per sec
            
            return WelcomeResult(
                success=True,
                method="local_fallback",
                duration_sec=approx_duration,
                metadata={"cmd": "say", "text": text}
            )

        except Exception as e:
            logger.error(f"❌ [WELCOME_PLAYER] Ошибка локального fallback: {e}")
            return WelcomeResult(False, "local", 0.0, str(e))


    
    def get_audio_data(self) -> np.ndarray | None:
        """Получить аудио данные для воспроизведения"""
        return self._last_audio

    def get_audio_metadata(self) -> dict[str, Any] | None:
        """Получить метаданные последнего аудио"""
        return self._last_metadata
    
    def is_ready(self) -> bool:
        """Проверить, готов ли плеер к воспроизведению"""
        return self.state in [WelcomeState.IDLE, WelcomeState.COMPLETED]
    
    def reset(self):
        """Сбросить состояние плеера"""
        self.state = WelcomeState.IDLE
        self._last_audio = None
        self._last_metadata = None
