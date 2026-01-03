"""
Edge TTS Provider для генерации речи

Генерирует аудио в точно таком же формате, как Azure TTS для полной совместимости:
- Формат: Raw PCM (без заголовков, как в Azure TTS после удаления RIFF заголовка)
- Sample Rate: 24kHz (Riff24Khz16BitMonoPcm)
- Bit Depth: 16-bit
- Channels: Mono (1 канал)
- Разбиение на чанки: по streaming_chunk_size (как в Azure TTS)

Это обеспечивает полную совместимость формата аудио между Edge TTS и Azure TTS провайдерами.
"""

import logging
import io
import asyncio
from typing import AsyncGenerator, Dict, Any, Optional
from integrations.core.universal_provider_interface import UniversalProviderInterface

logger = logging.getLogger(__name__)

# Импорты Edge TTS (с обработкой отсутствия)
try:
    import edge_tts
    EDGE_TTS_AVAILABLE = True
except ImportError:
    edge_tts = None
    EDGE_TTS_AVAILABLE = False
    logger.warning("⚠️ Edge TTS не найден - провайдер будет недоступен")

# Импорты для конвертации MP3 в PCM
import subprocess
import shutil

try:
    from pydub import AudioSegment
    PYDUB_AVAILABLE = True
except (ImportError, ModuleNotFoundError) as e:
    AudioSegment = None
    PYDUB_AVAILABLE = False
    logger.warning(f"⚠️ pydub не найден - конвертация MP3 в PCM будет недоступна: {e}")

# Альтернативная конвертация через ffmpeg (subprocess)
FFMPEG_AVAILABLE = shutil.which("ffmpeg") is not None
if not FFMPEG_AVAILABLE:
    logger.warning("⚠️ ffmpeg не найден - альтернативная конвертация MP3 в PCM будет недоступна")


class EdgeTTSProvider(UniversalProviderInterface):
    """
    Провайдер генерации речи с использованием Microsoft Edge TTS
    
    Бесплатный провайдер для преобразования текста в речь с поддержкой
    streaming и различных форматов аудио. Не требует API ключей.
    
    Генерирует аудио в точно таком же формате, как Azure TTS:
    - Raw PCM без заголовков (24kHz, 16-bit, mono)
    - Совместимый формат для seamless переключения между провайдерами
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Инициализация Edge TTS провайдера
        
        Args:
            config: Конфигурация провайдера
        """
        super().__init__(
            name="edge_tts",
            priority=1,  # Основной провайдер
            config=config
        )
        
        # Edge TTS настройки
        self.voice_name = config.get('voice_name', 'en-US-AriaNeural')
        self.rate = config.get('rate', '+0%')
        self.volume = config.get('volume', '+0%')
        self.pitch = config.get('pitch', '+0Hz')
        
        # Аудио настройки - используем централизованную конфигурацию
        # По умолчанию используем те же параметры, что и Azure TTS для совместимости
        self.audio_format = config.get('audio_format', 'pcm')
        self.sample_rate = config.get('sample_rate', 24000)  # 24kHz как в Azure TTS
        self.channels = config.get('channels', 1)  # Mono как в Azure TTS
        self.bits_per_sample = config.get('bits_per_sample', 16)  # 16-bit как в Azure TTS
        
        # Настройки streaming - для разбиения на чанки
        self.streaming_chunk_size = config.get('streaming_chunk_size', 4096)
        
        # Таймауты
        self.timeout = config.get('timeout', 60)
        self.connection_timeout = config.get('connection_timeout', 30)
        
        # Флаг конвертации MP3 в PCM
        self.convert_to_pcm = config.get('convert_to_pcm', True)
        
        self.is_available = EDGE_TTS_AVAILABLE
        
        logger.info(f"Edge TTS Provider initialized: available={self.is_available}, voice={self.voice_name}")
    
    async def initialize(self) -> bool:
        """
        Инициализация Edge TTS провайдера
        
        Returns:
            True если инициализация успешна, False иначе
        """
        try:
            if not self.is_available:
                logger.error("Edge TTS Provider not available - missing dependencies")
                return False
            
            # Type guard для линтера
            assert edge_tts is not None, "edge_tts должен быть доступен при is_available=True"
            
            # Тестируем подключение
            test_result = await self._test_connection()
            
            if test_result:
                self.is_initialized = True
                logger.info(f"Edge TTS Provider initialized successfully with voice: {self.voice_name}")
                return True
            else:
                logger.error("Edge TTS Provider test synthesis failed")
                return False
                
        except Exception as e:
            logger.error(f"Failed to initialize Edge TTS Provider: {e}")
            return False
    
    async def process(self, input_data: str) -> AsyncGenerator[bytes, None]:
        """
        ✅ ОПТИМИЗИРОВАНО: Streaming обработка текста в речь
        
        Генерирует аудио в точно таком же формате, как Azure TTS:
        - 24kHz sample rate (Riff24Khz16BitMonoPcm)
        - 16-bit depth
        - Mono (1 channel)
        - Raw PCM без заголовков
        
        ✅ КРИТИЧНОЕ УЛУЧШЕНИЕ: MP3 chunks конвертируются в PCM по мере поступления
        вместо ожидания всего аудио. Это значительно снижает latency.
        
        Args:
            input_data: Текст для преобразования в речь
            
        Yields:
            Chunks аудио данных (PCM формат)
        """
        try:
            if not self.is_initialized:
                raise Exception("Edge TTS Provider not initialized")
            
            assert edge_tts is not None, "edge_tts должен быть доступен при is_initialized=True"
            
            logger.info(f"EdgeTTS → generating speech for text: {input_data[:100]}...")
            
            # Создаем Communicate объект
            communicate = edge_tts.Communicate(
                text=input_data,
                voice=self.voice_name,
                rate=self.rate,
                volume=self.volume,
                pitch=self.pitch
            )
            
            # ✅ ОПТИМИЗАЦИЯ: Streaming конвертация MP3→PCM
            if self.convert_to_pcm and FFMPEG_AVAILABLE:
                # Используем async streaming через ffmpeg
                async for pcm_chunk in self._stream_mp3_to_pcm_async(communicate):
                    yield pcm_chunk
            else:
                # Fallback: собираем всё MP3 и конвертируем (старый метод)
                mp3_chunks = []
                async for chunk in communicate.stream():
                    if chunk.get("type") == "audio" and "data" in chunk:
                        mp3_chunks.append(chunk["data"])
                
                if not mp3_chunks:
                    raise Exception("No audio data received from Edge TTS")
                
                mp3_data = b''.join(mp3_chunks)
                logger.info(f"EdgeTTS → received MP3: {len(mp3_data)} bytes (fallback mode)")
                
                if self.convert_to_pcm:
                    # Конвертация через pydub или ffmpeg
                    if PYDUB_AVAILABLE:
                        try:
                            assert AudioSegment is not None
                            audio = AudioSegment.from_mp3(io.BytesIO(mp3_data))
                            audio = audio.set_frame_rate(self.sample_rate)
                            audio = audio.set_channels(self.channels)
                            audio = audio.set_sample_width(self.bits_per_sample // 8)
                            pcm_data = audio.raw_data
                        except Exception as e:
                            logger.warning(f"pydub failed: {e}, trying ffmpeg...")
                            pcm_data = self._convert_mp3_to_pcm_ffmpeg(mp3_data)
                    else:
                        pcm_data = self._convert_mp3_to_pcm_ffmpeg(mp3_data)
                    
                    # Разбиваем на чанки
                    offset = 0
                    while offset < len(pcm_data):
                        chunk_end = min(offset + self.streaming_chunk_size, len(pcm_data))
                        yield pcm_data[offset:chunk_end]
                        offset = chunk_end
                else:
                    # Возвращаем MP3 как есть
                    offset = 0
                    while offset < len(mp3_data):
                        chunk_end = min(offset + self.streaming_chunk_size, len(mp3_data))
                        yield mp3_data[offset:chunk_end]
                        offset = chunk_end
                        
        except Exception as e:
            logger.error(f"Edge TTS Provider processing error: {e}")
            raise e
    
    async def _stream_mp3_to_pcm_async(self, communicate) -> AsyncGenerator[bytes, None]:
        """
        ✅ НОВОЕ: Streaming конвертация MP3 в PCM через async ffmpeg pipe
        
        Конвертирует MP3 chunks в PCM по мере их поступления от Edge TTS,
        значительно снижая latency (первый PCM chunk отправляется сразу,
        а не после получения всего аудио).
        
        Yields:
            PCM chunks (24kHz, 16-bit, mono)
        """
        if not FFMPEG_AVAILABLE:
            raise Exception("ffmpeg not available for streaming conversion")
        
        # Создаем async subprocess с pipe stdin/stdout
        ffmpeg_cmd = [
            "ffmpeg",
            "-i", "pipe:0",         # Читаем MP3 из stdin
            "-f", "s16le",           # Формат: signed 16-bit little-endian PCM
            "-ar", str(self.sample_rate),  # Sample rate (24kHz)
            "-ac", str(self.channels),     # Channels (1 = mono)
            "-loglevel", "error",
            "pipe:1"                 # Выводим PCM в stdout
        ]
        
        process = await asyncio.create_subprocess_exec(
            *ffmpeg_cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        
        chunk_count = 0
        total_mp3_bytes = 0
        total_pcm_bytes = 0
        
        async def write_mp3_to_stdin():
            """Фоновая задача: пишем MP3 chunks в stdin ffmpeg"""
            nonlocal total_mp3_bytes
            try:
                async for chunk in communicate.stream():
                    if chunk.get("type") == "audio" and "data" in chunk:
                        mp3_data = chunk["data"]
                        total_mp3_bytes += len(mp3_data)
                        if process.stdin:
                            process.stdin.write(mp3_data)
                            await process.stdin.drain()
            except Exception as e:
                logger.error(f"Error writing to ffmpeg stdin: {e}")
            finally:
                if process.stdin:
                    process.stdin.close()
                    await process.stdin.wait_closed()
        
        # Запускаем запись MP3 в фоне
        write_task = asyncio.create_task(write_mp3_to_stdin())
        
        try:
            # Читаем PCM chunks из stdout и yield'им сразу
            while True:
                pcm_chunk = await process.stdout.read(self.streaming_chunk_size) if process.stdout else b''
                if not pcm_chunk:
                    break
                chunk_count += 1
                total_pcm_bytes += len(pcm_chunk)
                yield pcm_chunk
            
            # Ждем завершения записи
            await write_task
            
            # Проверяем код возврата ffmpeg
            return_code = await process.wait()
            if return_code != 0:
                stderr = await process.stderr.read() if process.stderr else b''
                logger.error(f"ffmpeg error (code {return_code}): {stderr.decode()}")
            
            logger.info(
                f"EdgeTTS → streaming conversion complete: MP3={total_mp3_bytes} bytes, "
                f"PCM={total_pcm_bytes} bytes, chunks={chunk_count}"
            )
            
        except Exception as e:
            logger.error(f"Error in streaming MP3→PCM conversion: {e}")
            # Отменяем задачу записи при ошибке
            write_task.cancel()
            try:
                await write_task
            except asyncio.CancelledError:
                pass
            raise e
    
    def _convert_mp3_to_pcm_ffmpeg(self, mp3_data: bytes) -> bytes:
        """
        Конвертация MP3 в PCM через ffmpeg (альтернатива pydub)
        
        Конвертирует в точно такой же формат, как Azure TTS:
        - 24kHz sample rate (Riff24Khz16BitMonoPcm)
        - 16-bit depth (s16le)
        - Mono (1 channel)
        - Raw PCM без заголовков (как в Azure TTS после удаления RIFF заголовка)
        
        Args:
            mp3_data: MP3 данные в байтах
            
        Returns:
            Raw PCM данные (совместимый формат с Azure TTS)
            
        Raises:
            Exception: Если конвертация не удалась
        """
        if not FFMPEG_AVAILABLE:
            raise Exception("ffmpeg not available for MP3 to PCM conversion")
        
        try:
            # Запускаем ffmpeg для конвертации MP3 в raw PCM
            # Формат точно такой же, как в Azure TTS после удаления RIFF заголовка:
            # -f s16le: signed 16-bit little-endian PCM (16-bit как в Azure)
            # -ar: sample rate (24kHz как в Azure Riff24Khz16BitMonoPcm)
            # -ac: channels (1 = mono как в Azure)
            ffmpeg_cmd = [
                "ffmpeg",
                "-i", "pipe:0",  # Читаем из stdin
                "-f", "s16le",    # Формат: signed 16-bit little-endian PCM
                "-ar", str(self.sample_rate),  # Sample rate (24kHz)
                "-ac", str(self.channels),     # Channels (1 = mono)
                "pipe:1",          # Выводим в stdout
                "-loglevel", "error"  # Только ошибки
            ]
            
            process = subprocess.run(
                ffmpeg_cmd,
                input=mp3_data,
                capture_output=True,
                check=True,
                timeout=30
            )
            
            pcm_data = process.stdout
            logger.info(
                "EdgeTTS → converted MP3 to PCM (ffmpeg): MP3=%s bytes, PCM=%s bytes, "
                "sample_rate=%s Hz, channels=%s, bits_per_sample=%s (Azure TTS compatible format)",
                len(mp3_data),
                len(pcm_data),
                self.sample_rate,
                self.channels,
                self.bits_per_sample,
            )
            
            return pcm_data
            
        except subprocess.CalledProcessError as e:
            logger.error(f"ffmpeg conversion failed: {e.stderr.decode() if e.stderr else str(e)}")
            raise Exception(f"Failed to convert MP3 to PCM using ffmpeg: {e}")
        except Exception as e:
            logger.error(f"Error in ffmpeg conversion: {e}")
            raise Exception(f"Failed to convert MP3 to PCM: {e}")
    
    async def cleanup(self) -> bool:
        """
        Очистка ресурсов Edge TTS провайдера
        
        Returns:
            True если очистка успешна, False иначе
        """
        try:
            self.is_initialized = False
            logger.info("Edge TTS Provider cleaned up")
            return True
            
        except Exception as e:
            logger.error(f"Error cleaning up Edge TTS Provider: {e}")
            return False
    
    async def _test_connection(self) -> bool:
        """
        Тестирование подключения к Edge TTS
        
        Returns:
            True если подключение работает, False иначе
        """
        try:
            if not edge_tts:
                return False
            
            # Простой тестовый синтез
            test_text = "Hello, this is a test."
            communicate = edge_tts.Communicate(test_text, self.voice_name)
            
            # Пробуем получить хотя бы один чанк
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    return True  # Получили аудио данные
            
            return False  # Не получили аудио
            
        except Exception as e:
            logger.warning(f"Edge TTS Provider connection test failed: {e}")
            return False
    
    async def _custom_health_check(self) -> bool:
        """
        Кастомная проверка здоровья Edge TTS провайдера
        
        Returns:
            True если провайдер здоров, False иначе
        """
        try:
            if not self.is_available:
                return False
            
            # Простая проверка - тестовый синтез
            test_result = await self._test_connection()
            return test_result
            
        except Exception as e:
            logger.warning(f"Edge TTS Provider health check failed: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """
        Получение расширенного статуса Edge TTS провайдера
        
        Returns:
            Словарь со статусом провайдера
        """
        base_status = super().get_status()
        
        # Добавляем специфичную информацию
        base_status.update({
            "provider_type": "edge_tts",
            "voice_name": self.voice_name,
            "rate": self.rate,
            "volume": self.volume,
            "pitch": self.pitch,
            "audio_format": self.audio_format,
            "sample_rate": self.sample_rate,
            "channels": self.channels,
            "bits_per_sample": self.bits_per_sample,
            "is_available": self.is_available,
            "convert_to_pcm": self.convert_to_pcm,
            "pydub_available": PYDUB_AVAILABLE,
            "edge_tts_available": EDGE_TTS_AVAILABLE
        })
        
        return base_status
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Получение расширенных метрик Edge TTS провайдера
        
        Returns:
            Словарь с метриками провайдера
        """
        base_metrics = super().get_metrics()
        
        # Добавляем специфичные метрики
        base_metrics.update({
            "provider_type": "edge_tts",
            "voice_name": self.voice_name,
            "audio_format": self.audio_format,
            "is_available": self.is_available
        })
        
        return base_metrics
    
    def get_audio_info(self) -> Dict[str, Any]:
        """
        Получение информации об аудио формате
        
        Returns:
            Словарь с информацией об аудио
        """
        return {
            "format": self.audio_format,
            "sample_rate": self.sample_rate,
            "channels": self.channels,
            "bits_per_sample": self.bits_per_sample,
            "voice_name": self.voice_name,
            "rate": self.rate,
            "volume": self.volume,
            "pitch": self.pitch,
            "convert_to_pcm": self.convert_to_pcm
        }
    
    def get_pricing_info(self) -> Dict[str, Any]:
        """
        Получение информации о стоимости использования Edge TTS
        
        Returns:
            Словарь с информацией о ценах (Edge TTS бесплатный)
        """
        return {
            "provider": "edge_tts",
            "cost": "free",
            "price_per_million_characters_usd": 0.0,
            "free_tier_characters_per_month": "unlimited",
            "currency": "USD",
            "notes": [
                "Edge TTS полностью бесплатный",
                "Нет ограничений на количество символов",
                "Не требует API ключей",
                "Использует Microsoft Edge TTS API"
            ]
        }
    
    def calculate_cost(self, character_count: int) -> Dict[str, Any]:
        """
        Расчет стоимости синтеза для заданного количества символов
        
        Args:
            character_count: Количество символов для синтеза
            
        Returns:
            Словарь с расчетом стоимости (всегда 0 для Edge TTS)
        """
        return {
            "character_count": character_count,
            "cost_usd": 0.0,
            "cost_rub": 0.0,
            "currency": "USD",
            "free_tier_remaining": "unlimited",
            "message": "Edge TTS is completely free with no limits",
            "price_per_million": 0.0,
            "voice_name": self.voice_name
        }

