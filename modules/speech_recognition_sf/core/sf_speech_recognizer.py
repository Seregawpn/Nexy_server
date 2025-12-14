"""
SFSpeechRecognizer Wrapper for macOS

Streaming speech recognition using native macOS Speech framework.
Provides real-time transcription with minimal latency.

Usage:
    recognizer = SFSpeechRecognizerWrapper(language="en-US")
    
    if await recognizer.is_available():
        await recognizer.start_recognition(
            on_result=lambda text, is_final: print(text),
            on_error=lambda error: print(error)
        )
        
        # Append audio chunks in real-time
        recognizer.append_audio(audio_data)
        
        # Finish and get final result
        final_text = await recognizer.finish_recognition()
"""

import asyncio
import logging
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional, Any
import threading

logger = logging.getLogger("Nexy")


class RecognitionState(Enum):
    """State of the speech recognition session."""
    IDLE = "idle"
    STARTING = "starting"
    RECOGNIZING = "recognizing"
    FINISHING = "finishing"
    FINISHED = "finished"
    ERROR = "error"


@dataclass
class RecognitionResult:
    """Result of speech recognition."""
    text: str
    is_final: bool
    confidence: Optional[float] = None
    segments: Optional[list] = None


class SFSpeechRecognizerWrapper:
    """
    Wrapper for macOS SFSpeechRecognizer.
    
    Provides streaming speech recognition using native macOS APIs.
    Audio chunks are sent in real-time, and results are returned
    as they become available.
    
    Attributes:
        language: Language code for recognition (e.g., "en-US", "ru-RU")
        on_device: Whether to use on-device recognition (no internet required)
    """
    
    def __init__(
        self,
        language: str = "en-US",
        on_device: bool = True
    ):
        """
        Initialize the SFSpeechRecognizer wrapper.
        
        Args:
            language: Language code for recognition
            on_device: Prefer on-device recognition if available
        """
        self._language = language
        self._on_device = on_device
        self._state = RecognitionState.IDLE
        
        # Speech framework objects (lazy initialized)
        self._speech_recognizer: Optional[Any] = None
        self._recognition_request: Optional[Any] = None
        self._recognition_task: Optional[Any] = None
        
        # Audio format
        self._audio_format: Optional[Any] = None
        
        # Callbacks
        self._on_result: Optional[Callable[[str, bool], None]] = None
        self._on_error: Optional[Callable[[str], None]] = None
        
        # Result tracking
        self._last_result: Optional[str] = None
        self._final_result: Optional[str] = None
        self._result_event: Optional[asyncio.Event] = None
        
        # Thread safety
        self._lock = threading.Lock()
        
        # Framework availability
        self._framework_available: Optional[bool] = None
        
        logger.info(f"🎤 [SFSpeech] Инициализация: language={language}, on_device={on_device}")
    
    def _ensure_framework(self) -> bool:
        """
        Ensure Speech framework is available.
        
        Returns:
            True if framework is available
        """
        if self._framework_available is not None:
            return self._framework_available
        
        try:
            # Import Speech framework via PyObjC
            from Speech import (
                SFSpeechRecognizer,
                SFSpeechAudioBufferRecognitionRequest,
                SFSpeechRecognizerAuthorizationStatus
            )
            from Foundation import NSLocale
            
            self._framework_available = True
            logger.info("✅ [SFSpeech] Speech framework доступен")
            return True
            
        except ImportError as e:
            self._framework_available = False
            logger.warning(f"⚠️ [SFSpeech] Speech framework недоступен: {e}")
            return False
    
    async def is_available(self) -> bool:
        """
        Check if speech recognition is available.
        
        Returns:
            True if recognition is available and authorized
        """
        if not self._ensure_framework():
            return False
        
        try:
            from Speech import (
                SFSpeechRecognizer,
                SFSpeechRecognizerAuthorizationStatus
            )
            from Foundation import NSLocale
            
            # Create locale for language
            locale = NSLocale.alloc().initWithLocaleIdentifier_(self._language)
            
            # Create recognizer
            recognizer = SFSpeechRecognizer.alloc().initWithLocale_(locale)
            
            if recognizer is None:
                logger.warning(f"⚠️ [SFSpeech] Язык не поддерживается: {self._language}")
                return False
            
            # Check availability
            is_available = recognizer.isAvailable()
            
            if not is_available:
                logger.warning("⚠️ [SFSpeech] Распознавание недоступно")
                return False
            
            # Check authorization
            auth_status = SFSpeechRecognizer.authorizationStatus()
            
            # В новой версии PyObjC (12.1) константы могут быть числовыми
            # 0 = notDetermined, 1 = denied, 2 = restricted, 3 = authorized
            try:
                authorized_value = SFSpeechRecognizerAuthorizationStatus.authorized
            except (AttributeError, TypeError):
                authorized_value = 3  # Fallback для новой версии
            
            try:
                not_determined_value = SFSpeechRecognizerAuthorizationStatus.notDetermined
            except (AttributeError, TypeError):
                not_determined_value = 0  # Fallback для новой версии
            
            if auth_status == authorized_value or auth_status == 3:
                logger.info("✅ [SFSpeech] Распознавание авторизовано")
                return True
            elif auth_status == not_determined_value or auth_status == 0:
                logger.info("⏳ [SFSpeech] Требуется запрос разрешения")
                # Request authorization
                authorized = await self._request_authorization()
                return authorized
            else:
                logger.warning(f"⚠️ [SFSpeech] Распознавание не авторизовано: {auth_status}")
                return False
                
        except Exception as e:
            logger.error(f"❌ [SFSpeech] Ошибка проверки доступности: {e}")
            return False
    
    async def _request_authorization(self) -> bool:
        """
        Request speech recognition authorization.
        
        Returns:
            True if authorized
        """
        try:
            from Speech import (
                SFSpeechRecognizer,
                SFSpeechRecognizerAuthorizationStatus
            )
            
            loop = asyncio.get_event_loop()
            future = loop.create_future()
            
            def handler(status: int) -> None:
                # В новой версии PyObjC (12.1) константы могут быть числовыми
                try:
                    authorized_value = SFSpeechRecognizerAuthorizationStatus.authorized
                except (AttributeError, TypeError):
                    authorized_value = 3  # Fallback для новой версии
                authorized = status == authorized_value or status == 3
                loop.call_soon_threadsafe(future.set_result, authorized)
            
            SFSpeechRecognizer.requestAuthorization_(handler)
            
            return await future
            
        except Exception as e:
            logger.error(f"❌ [SFSpeech] Ошибка запроса авторизации: {e}")
            return False
    
    async def start_recognition(
        self,
        on_result: Optional[Callable[[str, bool], None]] = None,
        on_error: Optional[Callable[[str], None]] = None,
        sample_rate: int = 48000
    ) -> bool:
        """
        Start streaming speech recognition.
        
        Args:
            on_result: Callback for recognition results (text, is_final)
            on_error: Callback for errors
            sample_rate: Audio sample rate
            
        Returns:
            True if recognition started successfully
        """
        if self._state != RecognitionState.IDLE:
            logger.warning(f"⚠️ [SFSpeech] Уже в состоянии: {self._state}")
            return False
        
        if not self._ensure_framework():
            if on_error:
                on_error("Speech framework not available")
            return False
        
        try:
            self._state = RecognitionState.STARTING
            self._on_result = on_result
            self._on_error = on_error
            self._last_result = None
            self._final_result = None
            self._result_event = asyncio.Event()
            
            from Speech import (
                SFSpeechRecognizer,
                SFSpeechAudioBufferRecognitionRequest
            )
            from AVFoundation import AVAudioFormat, AVAudioCommonFormat
            from Foundation import NSLocale
            
            # Create locale and recognizer
            locale = NSLocale.alloc().initWithLocaleIdentifier_(self._language)
            self._speech_recognizer = SFSpeechRecognizer.alloc().initWithLocale_(locale)
            
            if not self._speech_recognizer or not self._speech_recognizer.isAvailable():
                raise RuntimeError("Speech recognizer not available")
            
            # Configure on-device recognition if available
            if self._on_device and hasattr(self._speech_recognizer, 'supportsOnDeviceRecognition'):
                if self._speech_recognizer.supportsOnDeviceRecognition():
                    logger.info("✅ [SFSpeech] Используется On-Device распознавание")
                else:
                    logger.info("ℹ️ [SFSpeech] On-Device недоступен, используется сервер")
            
            # Create recognition request
            self._recognition_request = SFSpeechAudioBufferRecognitionRequest.alloc().init()
            self._recognition_request.setShouldReportPartialResults_(True)
            
            # Set on-device if available
            if self._on_device and hasattr(self._recognition_request, 'requiresOnDeviceRecognition'):
                self._recognition_request.setRequiresOnDeviceRecognition_(
                    self._speech_recognizer.supportsOnDeviceRecognition()
                )
            
            # Create audio format (mono, float32, specified sample rate)
            self._audio_format = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
                AVAudioCommonFormat.AVAudioPCMFormatFloat32,
                float(sample_rate),
                1,  # mono
                False
            )
            
            # Create recognition task with result handler
            loop = asyncio.get_event_loop()
            
            def result_handler(result: Any, error: Any) -> None:
                """Handle recognition results."""
                try:
                    if error:
                        error_msg = str(error.localizedDescription()) if hasattr(error, 'localizedDescription') else str(error)
                        logger.error(f"❌ [SFSpeech] Ошибка распознавания: {error_msg}")
                        
                        with self._lock:
                            self._state = RecognitionState.ERROR
                        
                        if self._on_error:
                            loop.call_soon_threadsafe(self._on_error, error_msg)
                        
                        if self._result_event:
                            loop.call_soon_threadsafe(self._result_event.set)
                        return
                    
                    if result:
                        # Get best transcription
                        transcription = result.bestTranscription()
                        text = transcription.formattedString() if transcription else ""
                        is_final = result.isFinal()
                        
                        with self._lock:
                            self._last_result = text
                            if is_final:
                                self._final_result = text
                                self._state = RecognitionState.FINISHED
                        
                        logger.debug(f"🎤 [SFSpeech] Результат: '{text[:50]}...' (final={is_final})")
                        
                        if self._on_result:
                            loop.call_soon_threadsafe(self._on_result, text, is_final)
                        
                        if is_final and self._result_event:
                            loop.call_soon_threadsafe(self._result_event.set)
                            
                except Exception as e:
                    logger.error(f"❌ [SFSpeech] Ошибка в result_handler: {e}")
            
            # Start recognition task
            self._recognition_task = self._speech_recognizer.recognitionTaskWithRequest_resultHandler_(
                self._recognition_request,
                result_handler
            )
            
            self._state = RecognitionState.RECOGNIZING
            logger.info("✅ [SFSpeech] Распознавание запущено")
            return True
            
        except Exception as e:
            self._state = RecognitionState.ERROR
            logger.error(f"❌ [SFSpeech] Ошибка запуска распознавания: {e}")
            if on_error:
                on_error(str(e))
            return False
    
    def append_audio(
        self,
        audio_data: bytes,
        sample_rate: int = 48000,
        channels: int = 1
    ) -> bool:
        """
        Append audio data to the recognition stream.
        
        Args:
            audio_data: PCM audio data (int16 or float32)
            sample_rate: Audio sample rate
            channels: Number of channels
            
        Returns:
            True if audio was appended successfully
        """
        if self._state != RecognitionState.RECOGNIZING:
            logger.warning(f"⚠️ [SFSpeech] Невозможно добавить аудио в состоянии: {self._state}")
            return False
        
        if not self._recognition_request:
            logger.warning("⚠️ [SFSpeech] Recognition request не инициализирован")
            return False
        
        try:
            import numpy as np
            from AVFoundation import AVAudioPCMBuffer
            
            # Convert bytes to numpy array
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
            
            # Convert to float32 [-1.0, 1.0]
            audio_float = audio_array.astype(np.float32) / 32767.0
            
            # Convert to mono if needed
            if channels > 1:
                frame_count = len(audio_float) // channels
                audio_float = audio_float[:frame_count * channels].reshape(frame_count, channels).mean(axis=1)
            else:
                frame_count = len(audio_float)
            
            # Create AVAudioPCMBuffer
            buffer = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(
                self._audio_format,
                frame_count
            )
            buffer.setFrameLength_(frame_count)
            
            # Copy data to buffer
            float_channel_data = buffer.floatChannelData()
            if float_channel_data and len(float_channel_data) > 0:
                ch_varlist = float_channel_data[0]
                if ch_varlist:
                    # ⚠️ PyObjC: ch_varlist это objc.varlist с методом as_buffer()
                    ch_buffer = ch_varlist.as_buffer(frame_count * 4)  # float32 = 4 bytes
                    ch_array = np.frombuffer(ch_buffer, dtype=np.float32)
                    np.copyto(ch_array, audio_float[:frame_count])
            
            # Append to recognition request
            self._recognition_request.appendAudioPCMBuffer_(buffer)
            
            return True
            
        except Exception as e:
            logger.error(f"❌ [SFSpeech] Ошибка добавления аудио: {e}")
            return False
    
    async def finish_recognition(self, timeout: float = 5.0) -> Optional[str]:
        """
        Finish recognition and wait for final result.
        
        Args:
            timeout: Maximum time to wait for final result
            
        Returns:
            Final recognized text or None
        """
        if self._state not in (RecognitionState.RECOGNIZING, RecognitionState.FINISHING):
            logger.warning(f"⚠️ [SFSpeech] Невозможно завершить в состоянии: {self._state}")
            return self._final_result
        
        try:
            self._state = RecognitionState.FINISHING
            
            # Signal end of audio
            if self._recognition_request:
                self._recognition_request.endAudio()
                logger.info("🎤 [SFSpeech] Сигнал окончания аудио отправлен")
            
            # Wait for final result
            if self._result_event:
                try:
                    await asyncio.wait_for(self._result_event.wait(), timeout=timeout)
                except asyncio.TimeoutError:
                    logger.warning(f"⚠️ [SFSpeech] Таймаут ожидания финального результата ({timeout}s)")
            
            result = self._final_result or self._last_result
            
            logger.info(f"✅ [SFSpeech] Финальный результат: '{result[:100] if result else 'None'}...'")
            
            # Cleanup
            await self._cleanup()
            
            return result
            
        except Exception as e:
            logger.error(f"❌ [SFSpeech] Ошибка завершения распознавания: {e}")
            await self._cleanup()
            return None
    
    async def cancel(self) -> None:
        """Cancel ongoing recognition."""
        logger.info("🎤 [SFSpeech] Отмена распознавания")
        
        if self._recognition_task:
            self._recognition_task.cancel()
        
        await self._cleanup()
    
    async def _cleanup(self) -> None:
        """Clean up recognition resources."""
        with self._lock:
            self._recognition_task = None
            self._recognition_request = None
            self._speech_recognizer = None
            self._state = RecognitionState.IDLE
            self._on_result = None
            self._on_error = None
        
        logger.debug("🧹 [SFSpeech] Ресурсы очищены")
    
    @property
    def state(self) -> RecognitionState:
        """Get current recognition state."""
        return self._state
    
    @property
    def last_result(self) -> Optional[str]:
        """Get last recognized text (may be partial)."""
        return self._last_result
    
    @property
    def language(self) -> str:
        """Get recognition language."""
        return self._language
    
    @language.setter
    def language(self, value: str) -> None:
        """Set recognition language (only when idle)."""
        if self._state != RecognitionState.IDLE:
            raise RuntimeError("Cannot change language during recognition")
        self._language = value



