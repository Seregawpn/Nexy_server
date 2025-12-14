"""
VoiceRecognitionIntegration - координация распознавания речи
Концептуальная реализация с симуляцией результата для UX-потока
"""

import asyncio
import logging
import threading
from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Union, Callable
import random
import importlib.util
from shutil import which
import time

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler
from config.unified_config_loader import UnifiedConfigLoader

# ✅ КРИТИЧНО: Определяем logger ДО импорта AVFAudioEngine для логирования ошибок импорта
logger = logging.getLogger(__name__)

# ✅ AVFoundation аудиосистема (Этап 3)
try:
    from modules.audio_avf import AVFAudioEngine
    from config.audio_config import AudioConfig
    _AVF_AVAILABLE = True
    logger.info("✅ [AVF] AVFAudioEngine импортирован успешно")
except ImportError as e:
    logger.error(f"❌ [AVF] Не удалось импортировать AVFAudioEngine: {e}")
    logger.exception("❌ [AVF] Детали ImportError при импорте AVFAudioEngine")
    _AVF_AVAILABLE = False
    AVFAudioEngine = None
except Exception as e:
    logger.error(f"❌ [AVF] Неожиданная ошибка при импорте AVFAudioEngine: {e}")
    logger.exception("❌ [AVF] Детали исключения при импорте AVFAudioEngine")
    _AVF_AVAILABLE = False
    AVFAudioEngine = None
# ⚠️ MicrophoneStateManager удалён (Этап 1) - заменён на AVFoundation (Этап 3)

# ✅ SFSpeechRecognizer - нативное стриминговое распознавание macOS (Этап 4)
try:
    from modules.speech_recognition_sf import SFSpeechRecognizerWrapper, RecognitionState
    _SF_SPEECH_AVAILABLE = True
    logger.info("✅ [SPEECH] SFSpeechRecognizerWrapper импортирован успешно")
except ImportError as e:
    _SF_SPEECH_AVAILABLE = False
    SFSpeechRecognizerWrapper = None
    RecognitionState = None
    logger.warning(f"⚠️ [SPEECH] SFSpeechRecognizer недоступен: {e}")

# Опциональная реальная реализация распознавания
try:
    from modules.voice_recognition import SpeechRecognizer, DEFAULT_RECOGNITION_CONFIG, RecognitionResult
    _REAL_VOICE_AVAILABLE = True
    logger.info("✅ [AUDIO_DEBUG] SpeechRecognizer импортирован успешно")
    print("✅ [AUDIO_DEBUG] SpeechRecognizer импортирован успешно")
except Exception as e:
    # Зависимости могут отсутствовать; в этом случае используем только симуляцию
    _REAL_VOICE_AVAILABLE = False
    logger.error(f"❌ [AUDIO_DEBUG] Ошибка импорта SpeechRecognizer: {e}", exc_info=True)
    print(f"❌ [AUDIO_DEBUG] Ошибка импорта SpeechRecognizer: {e}")


@dataclass
class VoiceRecognitionConfig:
    """Конфигурация распознавания речи"""
    timeout_sec: float = 10.0
    simulate: bool = False
    simulate_success_rate: float = 0.7  # 70% успеха по умолчанию
    simulate_min_delay_sec: float = 1.0
    simulate_max_delay_sec: float = 3.0
    language: str = "en-US"


class VoiceRecognitionIntegration:
    """Интеграция распознавания речи с EventBus"""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
        config: Optional[VoiceRecognitionConfig] = None,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler
        self.config = config or VoiceRecognitionConfig()

        # Текущее состояние распознавания
        # КРИТИЧНО: _current_session_id удален - используем только state_manager.get_current_session_id()
        self._recording_active: bool = False
        self._recognition_task: Optional[asyncio.Task] = None
        self._initialized: bool = False
        self._running: bool = False
        # Реальный распознаватель (если доступен и симуляция отключена)
        self._recognizer: Optional["SpeechRecognizer"] = None
        
        # ✅ AVFoundation аудиосистема (Этап 3)
        self._avf_engine: Optional[AVFAudioEngine] = None
        self._use_avf: bool = False
        self._audio_config: Optional[AudioConfig] = None
        self._audio_buffer: List[bytes] = []  # Буфер для накопления аудио чанков (fallback)
        self._audio_buffer_bytes: int = 0
        # ✅ ИНФОРМАЦИЯ ОБ УСТРОЙСТВЕ: сохраняем диагностику от AVF
        self._avf_device_info: Optional[Dict[str, Any]] = None
        # ✅ GOOGLE ЗАПИСЬ: объекты для прямой записи через speech_recognition
        self._google_recognizer: Optional[Any] = None
        self._google_microphone: Optional[Any] = None
        self._google_audio_data: Optional[Any] = None
        self._google_audio_chunks: list = []  # ✅ Инициализация для накопления аудио чанков
        self._google_audio_chunks_lock = threading.Lock()  # ✅ ИСПРАВЛЕНИЕ: Lock для синхронизации доступа к _google_audio_chunks
        self._google_stop_listening: Optional[Callable] = None  # ✅ Функция остановки listen_in_background
        self._google_chunk_event = threading.Event()  # Событие для ожидания первого аудио чанка
        self._google_recording_active: bool = False  # ✅ КРИТИЧНО: Флаг активности Google записи для защиты callback от обработки после остановки
        self._playback_active: bool = False  # ✅ КРИТИЧНО: Флаг активности воспроизведения для блокировки callback во время воспроизведения
        self._user_initiated_recording: bool = False  # ✅ КРИТИЧНО: Флаг пользовательской активации микрофона (source="keyboard") для разрешения прерывания воспроизведения
        self._audio_buffer_sample_rate: Optional[int] = None
        self._audio_buffer_channels: Optional[int] = None
        
        # ✅ SFSpeechRecognizer - стриминговое распознавание (Этап 4)
        self._sf_recognizer: Optional["SFSpeechRecognizerWrapper"] = None
        # 🔁 Глобальный флаг готовности стриминга и параметры конфигурации
        self._use_streaming: bool = False
        self._streaming_feature_enabled: bool = False
        self._streaming_env_disabled: bool = False
        self._streaming_on_device: bool = True
        self._streaming_language: str = "en-US"
        self._streaming_sample_rate: int = 48000
        self._streaming_timeout: float = 5.0
        self._batch_language: str = "en-US"
        self._batch_sample_rate: int = 48000
        self._streaming_retry_after: float = 0.0
        self._streaming_retry_interval: float = 60.0  # сек до следующей попытки инициализации
        self._streaming_session_id: Optional[float] = None
        self._streaming_session_active: bool = False
        self._streaming_partial_result: Optional[str] = None
        self._streaming_error: Optional[str] = None
        self._recording_start_time: Optional[float] = None  # ✅ ИСПРАВЛЕНИЕ: Время начала записи для обрезки аудио
        self._last_recording_stop_time: float = 0.0  # ✅ Время последней остановки записи (time.monotonic())
        self._recording_stop_cooldown_sec: float = 0.5  # ✅ Cooldown период после остановки записи (500мс)

        # Флаг блокировки во время first_run
        self._first_run_in_progress: bool = False
        # Конфигурируемая задержка между попытками запуска микрофона
        try:
            loader = UnifiedConfigLoader()
            config_dict = loader._load_config()
            voice_cfg = config_dict.get("voice", {})
            self._start_retry_delay_sec = max(0.0, float(voice_cfg.get("start_retry_delay_ms", 300)) / 1000.0)
        except Exception:
            self._start_retry_delay_sec = 0.3
        
        # ⚠️ MicrophoneStateManager удалён (Этап 1) - заменён на AVFoundation (Этап 3)
        self._mic_state_manager = None

    @classmethod
    def run_dependency_check(cls) -> bool:
        """
        Проверяет наличие ключевых зависимостей для работы распознавания речи.
        Возвращает True при успехе, иначе False.
        """
        logger = logging.getLogger(__name__)
        logger.info("🔍 Запуск диагностики зависимостей распознавания речи")

        dependencies = [
            ("speech_recognition", "SpeechRecognition (speech_recognition)"),
            ("sounddevice", "SoundDevice (sounddevice)"),
            ("numpy", "NumPy (numpy)"),
        ]

        all_ok = True

        for module_name, human_readable in dependencies:
            spec = importlib.util.find_spec(module_name)
            if spec is None:
                logger.error(f"❌ Не найдена зависимость: {human_readable}")
                all_ok = False
            else:
                origin = spec.origin or "built-in"
                logger.debug(f"✅ {human_readable} доступен ({origin})")

        # Проверяем доступность FLAC-конвертера, необходимого для SpeechRecognition
        flac_available = False
        flac_path = None

        if importlib.util.find_spec("speech_recognition"):
            try:
                import speech_recognition as sr  # type: ignore

                get_converter = getattr(sr, "get_flac_converter", None)
                if callable(get_converter):
                    flac_path = get_converter()
                    flac_available = bool(flac_path)
                    if flac_available:
                        logger.debug(f"✅ FLAC-конвертер найден: {flac_path}")
            except Exception as e:
                logger.warning(f"⚠️ Не удалось определить FLAC-конвертер через SpeechRecognition: {e}")

        if not flac_available:
            flac_path = which("flac")
            flac_available = flac_path is not None
            if flac_available:
                logger.debug(f"✅ Найден системный FLAC-конвертер: {flac_path}")

        if not flac_available:
            logger.error(
                "❌ FLAC-конвертер не найден. Установите пакет 'flac' (например, `brew install flac`) "
                "или добавьте совместимый бинарник в сборку."
            )
            all_ok = False

        if all_ok:
            logger.info("✅ Диагностика распознавания речи пройдена успешно")
        else:
            logger.error("❌ Диагностика распознавания речи завершилась с ошибками")

        return all_ok
        
    async def initialize(self) -> bool:
        logger.info("🔍 [AUDIO_DEBUG] VoiceRecognitionIntegration.initialize() ВЫЗВАН")
        logger.info(f"🔍 [AUDIO_DEBUG] Параметры: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}")
        print(f"🔍 [AUDIO_DEBUG] VoiceRecognitionIntegration.initialize() ВЫЗВАН")
        print(f"🔍 [AUDIO_DEBUG] Параметры: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}")
        try:
            # ✅ AVFoundation аудиосистема (Этап 3)
            # Проверяем feature flag для AVFoundation
            try:
                logger.info("🔍 [AVF] Начало инициализации AVF...")
                loader = UnifiedConfigLoader()
                logger.info("🔍 [AVF] UnifiedConfigLoader создан")
                audio_config = loader.get_audio_config_object()
                logger.info(f"🔍 [AVF] audio_config загружен: {audio_config is not None}")
                avf_config = loader.get_audio_avf_config()
                logger.info(f"🔍 [AVF] avf_config загружен: {avf_config is not None}")
                
                # Проверяем feature flag и kill-switch
                avf_enabled = avf_config.get("avf", {}).get("enabled", False)
                ks_avf_enabled = avf_config.get("ks_avf", {}).get("enabled", False)
                logger.info(f"🔍 [AVF] avf.enabled={avf_enabled}, ks_avf.enabled={ks_avf_enabled}")
                
                # Проверяем env переменную для отключения (dry-run режим)
                import os
                disable_avf_env = os.getenv("NEXY_DISABLE_AVF_AUDIO", "false").lower() == "true"
                logger.info(f"🔍 [AVF] NEXY_DISABLE_AVF_AUDIO={disable_avf_env}")
                logger.info(f"🔍 [AVF] _AVF_AVAILABLE={_AVF_AVAILABLE}")
                
                self._use_avf = avf_enabled and not ks_avf_enabled and not disable_avf_env and _AVF_AVAILABLE
                logger.info(f"🔍 [AVF] _use_avf вычислен: {self._use_avf}")
                
                if self._use_avf:
                    logger.info("✅ [AVF] AVFoundation аудиосистема включена")
                    logger.debug("🔍 [AVF] Сохранение audio_config...")
                    self._audio_config = audio_config
                    logger.debug("🔍 [AVF] Создание AVFAudioEngine...")
                    try:
                        self._avf_engine = AVFAudioEngine(audio_config)
                        logger.info("✅ [AVF] AVFAudioEngine инициализирован")
                    except Exception as avf_create_error:
                        logger.error(f"❌ [AVF] Ошибка создания AVFAudioEngine: {avf_create_error}")
                        logger.exception("❌ [AVF] Детали исключения при создании AVFAudioEngine:")
                        self._use_avf = False
                        self._avf_engine = None
                else:
                    reason = []
                    if not avf_enabled:
                        reason.append("feature flag disabled")
                    if ks_avf_enabled:
                        reason.append("kill-switch enabled")
                    if disable_avf_env:
                        reason.append("env variable disabled")
                    if not _AVF_AVAILABLE:
                        reason.append("AVF not available")
                    logger.info(f"ℹ️ [AVF] AVFoundation аудиосистема отключена: {', '.join(reason)}")
            except Exception as e:
                logger.error(f"❌ [AVF] Ошибка проверки feature flag, используем legacy: {e}")
                logger.exception("❌ [AVF] Детали исключения при инициализации AVF:")
                self._use_avf = False
            
            # ✅ SFSpeechRecognizer - стриминговое распознавание (Этап 4)
            # ✅ ДИАГНОСТИКА: Логируем состояние перед проверкой
            logger.debug(f"🔍 [SFSpeech] Проверка условий: _use_avf={self._use_avf}, _SF_SPEECH_AVAILABLE={_SF_SPEECH_AVAILABLE}")
            
            if self._use_avf and _SF_SPEECH_AVAILABLE:
                try:
                    # ✅ ЦЕНТРАЛИЗАЦИЯ: Читаем все параметры из unified_config.yaml
                    config_dict = loader._load_config()
                    speech_config = config_dict.get("speech_recognition", {})
                    streaming_config = speech_config.get("streaming", {})
                    
                    # Общие параметры
                    default_language = speech_config.get("language", "en-US")
                    default_sample_rate = speech_config.get("default_sample_rate", 48000)
                    
                    # Параметры стриминга
                    streaming_enabled = streaming_config.get("enabled", True)
                    streaming_on_device = streaming_config.get("on_device", True)
                    streaming_language = streaming_config.get("language") or default_language
                    streaming_timeout = streaming_config.get("timeout_sec", 5.0)
                    streaming_sample_rate = streaming_config.get("sample_rate") or (self._audio_config.input.target_rate if self._audio_config else default_sample_rate)
                    
                    # Проверяем env переменную
                    import os
                    disable_streaming_env = os.getenv("NEXY_DISABLE_STREAMING_RECOGNITION", "false").lower() == "true"
                    
                    self._streaming_feature_enabled = streaming_enabled
                    self._streaming_env_disabled = disable_streaming_env
                    self._streaming_on_device = streaming_on_device
                    
                    # ✅ ДИАГНОСТИКА: Логируем параметры
                    logger.info(
                        "🔍 [SFSpeech] Параметры: streaming_enabled=%s, disable_streaming_env=%s",
                        streaming_enabled,
                        disable_streaming_env,
                    )
                    
                    # Сохраняем параметры для использования в других методах
                    self._streaming_language = streaming_language
                    self._streaming_timeout = streaming_timeout
                    self._streaming_sample_rate = streaming_sample_rate
                    self._batch_language = speech_config.get("batch", {}).get("language") or default_language
                    self._batch_sample_rate = speech_config.get("batch", {}).get("sample_rate") or default_sample_rate
                    
                    if streaming_enabled and not disable_streaming_env:
                        await self._ensure_streaming_ready(context="initialize")
                    else:
                        reason = []
                        if not streaming_enabled:
                            reason.append("feature flag disabled")
                        if disable_streaming_env:
                            reason.append("env variable disabled")
                        logger.info(f"ℹ️ [SFSpeech] Стриминговое распознавание отключено: {', '.join(reason)}")
                except Exception as e:
                    logger.warning(f"⚠️ [SFSpeech] Ошибка инициализации стриминга: {e}", exc_info=True)
                    self._disable_streaming("exception during streaming init")
            else:
                reason = []
                if not self._use_avf:
                    reason.append("AVFoundation не включен")
                if not _SF_SPEECH_AVAILABLE:
                    reason.append("SFSpeechRecognizer недоступен")
                logger.debug(f"ℹ️ [SFSpeech] Стриминг не инициализируется: {', '.join(reason)}")
            
            # Подписки на события записи/прерывания
            await self.event_bus.subscribe("voice.recording_start", self._on_recording_start, EventPriority.HIGH)
            await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop, EventPriority.HIGH)
            # ✅ УДАЛЕНО: Подписка на voice.mic_data_ready (больше не используется)
            await self.event_bus.subscribe("keyboard.short_press", self._on_cancel_request, EventPriority.CRITICAL)
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            # Гарантированно закрываем прослушивание при выходе из LISTENING
            await self.event_bus.subscribe("app.mode_changed", self._on_app_mode_changed, EventPriority.MEDIUM)
            # ✅ КРИТИЧНО: Подписка на playback.started для принудительной остановки микрофона во время воспроизведения
            await self.event_bus.subscribe("playback.started", self._on_playback_started, EventPriority.HIGH)
            # ✅ КРИТИЧНО: Подписка на playback.completed/cancelled/failed для сброса флага воспроизведения
            await self.event_bus.subscribe("playback.completed", self._on_playback_finished, EventPriority.HIGH)
            await self.event_bus.subscribe("playback.cancelled", self._on_playback_finished, EventPriority.HIGH)
            await self.event_bus.subscribe("playback.failed", self._on_playback_finished, EventPriority.HIGH)

            # КРИТИЧНО: Подписываемся на события first_run для блокировки активации
            await self.event_bus.subscribe("permissions.first_run_started", self._on_first_run_started, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_failed", self._on_first_run_completed, EventPriority.CRITICAL)

            # Инициализация реального распознавателя, если симуляция отключена
            logger.info(f"🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}, _use_avf={self._use_avf}")
            print(f"🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}, _use_avf={self._use_avf}")
            
            # ✅ ИЗМЕНЕНИЕ: Создаём SpeechRecognizer ДАЖЕ при использовании AVF
            # AVF будет использоваться только для диагностики (активация на ~1 секунду)
            # Google (SpeechRecognizer) будет использоваться для записи речи
            if self._use_avf:
                # ✅ Создаём SpeechRecognizer для Google записи
                if not self.config.simulate and _REAL_VOICE_AVAILABLE:
                    try:
                        logger.info("🔍 [AUDIO_DEBUG] Создание SpeechRecognizer для Google записи (AVF используется для диагностики)...")
                        self._recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
                        logger.info(f"✅ [AUDIO_DEBUG] SpeechRecognizer создан успешно: {self._recognizer is not None}")
                        print(f"✅ [AUDIO_DEBUG] SpeechRecognizer создан успешно: {self._recognizer is not None}")
                        
                        # НАСТРАИВАЕМ EventBus в SpeechRecognizer для получения событий выбора устройств
                        if hasattr(self._recognizer, 'set_event_bus'):
                            self._recognizer.set_event_bus(self.event_bus)
                            logger.debug("🔍 [AUDIO_DEBUG] EventBus настроен в SpeechRecognizer")
                        else:
                            logger.warning("⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_bus")
                        
                        # Устанавливаем event loop для асинхронных операций из audio callback
                        if hasattr(self._recognizer, 'set_event_loop'):
                            self._recognizer.set_event_loop(asyncio.get_running_loop())
                            logger.debug("🔍 [AUDIO_DEBUG] Event loop установлен в SpeechRecognizer")
                        else:
                            logger.warning("⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_loop")
                    except Exception as e:
                        logger.warning(f"⚠️ [AUDIO_DEBUG] Не удалось создать SpeechRecognizer: {e}")
                        self._recognizer = None
                else:
                    logger.info("ℹ️ [AUDIO_DEBUG] SpeechRecognizer НЕ создаётся (simulate=True или _REAL_VOICE_AVAILABLE=False)")
                    self._recognizer = None
            elif not self.config.simulate and _REAL_VOICE_AVAILABLE:
                try:
                    logger.info("🔍 [AUDIO_DEBUG] Создание SpeechRecognizer (legacy режим, AVF отключен)...")
                    # ИСПОЛЬЗУЕМ ГОТОВУЮ КОНФИГУРАЦИЮ ИЗ МОДУЛЯ - тонкая интеграция
                    self._recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
                    logger.info(f"✅ [AUDIO_DEBUG] SpeechRecognizer создан успешно: {self._recognizer is not None}")
                    print(f"✅ [AUDIO_DEBUG] SpeechRecognizer создан успешно: {self._recognizer is not None}")
                    
                    # НАСТРАИВАЕМ EventBus в SpeechRecognizer для получения событий выбора устройств
                    if hasattr(self._recognizer, 'set_event_bus'):
                        self._recognizer.set_event_bus(self.event_bus)
                        logger.debug("🔍 [AUDIO_DEBUG] EventBus настроен в SpeechRecognizer")
                    else:
                        logger.warning("⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_bus")
                    
                    # Устанавливаем event loop для асинхронных операций из audio callback
                    if hasattr(self._recognizer, 'set_event_loop'):
                        self._recognizer.set_event_loop(asyncio.get_running_loop())
                        logger.debug("🔍 [AUDIO_DEBUG] Event loop установлен в SpeechRecognizer")
                    else:
                        logger.warning("⚠️ [AUDIO_DEBUG] SpeechRecognizer не поддерживает set_event_loop")
                    
                    logger.info("✅ VoiceRecognitionIntegration: real SpeechRecognizer initialized with EventBus")
                except Exception as e:
                    logger.error(f"❌ VoiceRecognitionIntegration: failed to init real recognizer, fallback to simulate. Error: {e}", exc_info=True)
                    self.config.simulate = True
            else:
                if self.config.simulate:
                    logger.warning(f"⚠️ [AUDIO_DEBUG] SpeechRecognizer не создается: симуляция включена (simulate=True)")
                if not _REAL_VOICE_AVAILABLE:
                    logger.error(f"❌ [AUDIO_DEBUG] SpeechRecognizer не создается: модуль недоступен (_REAL_VOICE_AVAILABLE=False)")
            
            # ✅ ДИАГНОСТИКА: Логируем финальное состояние
            logger.info(f"🔍 [AUDIO_DEBUG] Финальное состояние после initialize: _recognizer={self._recognizer is not None}, simulate={self.config.simulate}")
            print(f"🔍 [AUDIO_DEBUG] Финальное состояние после initialize: _recognizer={self._recognizer is not None}, simulate={self.config.simulate}")

            self._initialized = True
            logger.info("VoiceRecognitionIntegration initialized")
            return True
        except Exception as e:
            if hasattr(self.error_handler, 'handle_error'):
                await self.error_handler.handle_error(
                    severity="error",
                    category="voice",
                    message=f"Ошибка инициализации VoiceRecognitionIntegration: {e}",
                    context={"where": "voice.initialize"}
                )
            else:
                logger.error(f"Error initializing VoiceRecognitionIntegration: {e}")
            return False
    
    async def start(self) -> bool:
        if not self._initialized:
            logger.error("VoiceRecognitionIntegration not initialized")
            return False
        if self._running:
            return True
        
        # Проверяем разрешения микрофона перед запуском
        await self._check_microphone_permissions()
        
        self._running = True
        logger.info("VoiceRecognitionIntegration started")
        return True
    
    async def stop(self) -> bool:
        try:
            self._running = False
            await self._cancel_recognition(reason="stopping")
            logger.info("VoiceRecognitionIntegration stopped")
            return True
        except Exception as e:
            logger.error(f"Error stopping VoiceRecognitionIntegration: {e}")
            return False
    
    # ✅ ИСПРАВЛЕНИЕ: Хелпер-методы для устранения дублирования
    def _is_streaming_active(self) -> bool:
        """Проверка активности стриминга (thread-safe)"""
        return self._use_streaming and self._sf_recognizer is not None
    
    def _clear_audio_buffer(self) -> None:
        """Очистка аудио буфера"""
        self._audio_buffer = []
        self._audio_buffer_bytes = 0
        self._audio_buffer_sample_rate = None
        self._audio_buffer_channels = None
        logger.debug("🧹 [AVF] Аудио буфер очищен (reason=clear_audio_buffer)")

    async def _ensure_streaming_ready(self, context: str = "runtime") -> bool:
        """
        Пытается инициализировать SFSpeechRecognizer при необходимости.

        Args:
            context: строка для логов (например, initialize/recording_start)

        Returns:
            True если стриминг готов к работе.
        """
        if (
            not self._streaming_feature_enabled
            or self._streaming_env_disabled
            or not self._use_avf
            or not _SF_SPEECH_AVAILABLE
        ):
            return False

        # Уже есть готовый recognizer в IDLE состоянии
        if self._sf_recognizer is not None:
            state = getattr(self._sf_recognizer, "state", None)
            if state in (None, RecognitionState.IDLE):
                self._use_streaming = True
                logger.debug("🎤 [SFSpeech] Reusing existing recognizer (context=%s)", context)
                return True

        now = time.monotonic()
        if now < self._streaming_retry_after:
            logger.debug(
                "⏳ [SFSpeech] Пропускаем повторную инициализацию (%s). Следующая попытка через %.1fs",
                context,
                self._streaming_retry_after - now,
            )
            return False

        try:
            logger.info(
                "🎤 [SFSpeech] Пытаемся инициализировать стриминг (context=%s, language=%s, on_device=%s)",
                context,
                self._streaming_language,
                self._streaming_on_device,
            )
            recognizer = SFSpeechRecognizerWrapper(
                language=self._streaming_language,
                on_device=self._streaming_on_device,
            )
            is_available = await recognizer.is_available()
            if not is_available:
                logger.warning(
                    "⚠️ [SFSpeech] Недоступен (context=%s). Повторная попытка через %ss",
                    context,
                    int(self._streaming_retry_interval),
                )
                self._disable_streaming("recognizer not available", retry_interval=self._streaming_retry_interval)
                return False

            self._sf_recognizer = recognizer
            self._use_streaming = True
            self._streaming_retry_after = now + 5.0  # небольшая пауза, чтобы не спамить
            logger.info(
                "✅ [SFSpeech] Стриминговое распознавание готово (context=%s, language=%s)",
                context,
                self._streaming_language,
            )
            return True
        except Exception as e:
            logger.error(
                "❌ [SFSpeech] Ошибка инициализации (context=%s): %s",
                context,
                e,
                exc_info=True,
            )
            self._disable_streaming("initialization error", retry_interval=self._streaming_retry_interval)
            return False

    def _disable_streaming(self, reason: str, *, retry_interval: Optional[float] = None) -> None:
        """Полностью отключает текущий стриминг до следующей попытки инициализации."""
        if self._use_streaming or self._sf_recognizer is not None:
            logger.warning("⚠️ [SFSpeech] Стриминг отключен: %s", reason)
        self._use_streaming = False
        self._streaming_session_active = False
        self._streaming_session_id = None
        self._streaming_partial_result = None
        self._streaming_error = None
        self._sf_recognizer = None
        interval = retry_interval if retry_interval is not None else self._streaming_retry_interval
        self._streaming_retry_after = time.monotonic() + max(0.0, interval)

    def _is_streaming_session_live(self, session_id: Optional[float] = None) -> bool:
        """True если есть активная стриминговая сессия (и совпадает session_id, если указан)."""
        if not self._streaming_session_active or not self._use_streaming:
            return False
        if self._sf_recognizer is None:
            return False
        if session_id is not None and self._streaming_session_id != session_id:
            return False
        return True

    async def _handle_streaming_failure(
        self,
        session_id: Optional[float],
        reason: str,
        *,
        disable: bool = False
    ) -> None:
        """Останавливает текущую стриминговую сессию и (опционально) отключает стриминг глобально."""
        logger.warning("⚠️ [SFSpeech] Ошибка стриминга (session=%s): %s", session_id, reason)
        self._streaming_error = reason
        if self._sf_recognizer is not None:
            try:
                await self._sf_recognizer.cancel()
            except Exception as cancel_error:
                logger.error("❌ [SFSpeech] Ошибка отмены стриминга: %s", cancel_error)
        self._streaming_session_active = False
        self._streaming_session_id = None
        self._streaming_partial_result = None
        if disable:
            self._disable_streaming(reason)

    async def _start_streaming_session(self, session_id: float) -> bool:
        """Запускает стриминговое распознавание для указанной сессии."""
        if not self._is_streaming_active():
            return False
        recognizer = self._sf_recognizer
        if recognizer is None:
            return False

        loop = asyncio.get_running_loop()

        def on_streaming_result(text: str, is_final: bool) -> None:
            self._streaming_partial_result = text
            if is_final:
                logger.info("✅ [SFSpeech] Финальный результат (stream): '%s...'", text[:100])
            else:
                logger.debug("🔄 [SFSpeech] Промежуточный результат: '%s...'", text[:50])

        def on_streaming_error(error_msg: str) -> None:
            loop.create_task(
                self._handle_streaming_failure(session_id, f"callback error: {error_msg}", disable=True)
            )

        sample_rate = getattr(
            self,
            "_streaming_sample_rate",
            self._audio_config.input.target_rate if self._audio_config else 48000,
        )
        started = await recognizer.start_recognition(
            on_result=on_streaming_result,
            on_error=on_streaming_error,
            sample_rate=sample_rate,
        )

        if not started:
            await self._handle_streaming_failure(session_id, "start_failed", disable=True)
            return False

        self._streaming_session_id = session_id
        self._streaming_session_active = True
        self._streaming_partial_result = None
        self._streaming_error = None
        logger.info("🎤 [SFSpeech] Стриминговая сессия запущена (session=%s)", session_id)
        return True

    # ========== МЕТОДЫ-ПОМОЩНИКИ ДЛЯ ПРОВЕРКИ СОСТОЯНИЯ ==========
    # Эти методы упрощают логику проверок и делают код более читаемым.
    # Они не изменяют логику, а только инкапсулируют проверки состояния.
    # Шаг 1: Добавление методов-помощников для подготовки к миграции на state_manager.
    
    def _has_active_session(self) -> bool:
        """
        Проверка: есть ли активная сессия.
        
        Returns:
            True если есть активная сессия (из state_manager - единый источник истины)
        """
        # Используем state_manager как единый источник истины
        session_id = self.state_manager.get_current_session_id()
        return session_id is not None
    
    def is_microphone_actually_active(self) -> bool:
        """
        Единый источник истины для проверки состояния микрофона.
        Проверяет централизованное состояние и физическое состояние потока.
        
        Returns:
            True если микрофон действительно активен, False иначе
        """
        # 1. Проверяем централизованное состояние (основной источник)
        if self.state_manager.is_microphone_active():
            return True
        
        # 2. Проверяем физическое состояние потока (fallback для обнаружения рассинхронизации)
        if self._recognizer and hasattr(self._recognizer, '_current_stream'):
            try:
                with getattr(self._recognizer, '_stream_lock', threading.RLock()):
                    if self._recognizer._current_stream and self._recognizer._current_stream.active:
                        logger.warning("⚠️ [VOICE] Обнаружена рассинхронизация: поток активен, но state_manager не знает")
                        return True
            except Exception as e:
                logger.debug(f"⚠️ [VOICE] Ошибка проверки физического состояния потока: {e}")
        
        return False
    
    def _get_active_session_id(self) -> Optional[str]:
        """
        Получить активный session_id из state_manager (единый источник истины).
        
        Returns:
            Активный session_id (строка) или None
        """
        # Используем state_manager как единый источник истины
        session_id = self.state_manager.get_current_session_id()
        # Возвращаем как есть (строка), не конвертируем в float
        return session_id
    
    def _set_session_id(self, session_id: Optional[Union[float, str]], reason: str = "unknown"):
        """
        Установить session_id в state_manager (единый источник истины).
        
        КРИТИЧНО: Используем state_manager как единственный источник истины.
        Локальная переменная _current_session_id удалена - все через state_manager.
        
        Args:
            session_id: Session ID для установки (может быть float, str или None)
            reason: Причина установки (для логирования)
        """
        # Устанавливаем в state_manager (единый источник истины)
        if session_id is not None:
            # Конвертируем в строку для state_manager (он хранит строки)
            session_id_str = str(session_id)
            # Обновляем state_manager только если session_id изменился
            current_state_session = self.state_manager.get_current_session_id()
            if current_state_session != session_id_str:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(session_id_str)
                logger.debug(f"🔄 [VOICE] Session ID синхронизирован с state_manager: {session_id_str} (reason: {reason})")
        else:
            # Сбрасываем session_id в state_manager только если он был установлен
            if self.state_manager.get_current_session_id() is not None:
                # КРИТИЧНО: Используем update_session_id() БЕЗ публикации app.mode_changed
                # Это предотвращает ложные прерывания в ProcessingWorkflow
                self.state_manager.update_session_id(None)
                logger.debug(f"🔄 [VOICE] Session ID сброшен в state_manager (reason: {reason})")

    # События записи
    async def _on_recording_start(self, event: Dict[str, Any]):
        try:
            # ✅ ДИАГНОСТИКА: Логируем вход в метод
            logger.info("🎤 [VOICE] _on_recording_start ВХОД: event получен")
            logger.info(f"🎤 [VOICE] _on_recording_start: event={event}")
            # #region agent log
            import json
            import time
            import os
            try:
                event_data = event.get("data", {}) if isinstance(event, dict) else event
                session_id = event_data.get("session_id") if isinstance(event_data, dict) else None
                google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
                state_mic_active = self.state_manager.is_microphone_active()
                current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
                log_path = '/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log'
                # ✅ КРИТИЧНО: Создаем директорию, если её нет
                os.makedirs(os.path.dirname(log_path), exist_ok=True)
                with open(log_path, 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "voice_recognition_integration.py:708", "message": "_on_recording_start called", "data": {"session_id": session_id, "source": event_data.get("source") if isinstance(event_data, dict) else None, "recording_active": getattr(self, "_recording_active", False), "google_mic_active": google_mic_active, "legacy_mic_active": legacy_mic_active, "state_mic_active": state_mic_active, "current_mode": str(current_mode)}, "timestamp": int(time.time() * 1000)}) + "\n")
            except Exception as log_err:
                logger.debug(f"🔍 [VOICE] Ошибка записи в debug.log: {log_err}")
            # #endregion
            if event and isinstance(event, dict):
                event_data = event.get("data", {})
                session_id = event_data.get("session_id")
                logger.info(f"🎤 [VOICE] _on_recording_start: session_id={session_id}, source={event_data.get('source')}")
            
            # ✅ КРИТИЧНО: Проверяем режим ПЕРЕД началом записи
            # Если режим PROCESSING, значит идет воспроизведение ответа ассистента
            # НО: разрешаем активацию микрофона по нажатию пользователя (source="keyboard") для прерывания воспроизведения
            # Блокируем только автоматическую активацию (когда source не "keyboard")
            current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
            event_source = event_data.get("source") if isinstance(event_data, dict) else None
            
            # ✅ КРИТИЧНО: Сохраняем информацию о том, что микрофон был активирован пользователем
            # Это нужно для разрешения обработки аудио в callback даже во время воспроизведения (для прерывания)
            self._user_initiated_recording = (event_source == "keyboard")
            
            if current_mode == AppMode.PROCESSING and event_source != "keyboard":
                logger.warning("🔒 [VOICE] Режим PROCESSING (воспроизведение ответа ассистента) - автоматическая активация микрофона заблокирована (source не keyboard)")
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "voice_recognition_integration.py:736", "message": "_on_recording_start blocked: PROCESSING mode (automatic activation)", "data": {"current_mode": "PROCESSING", "session_id": session_id, "source": event_source}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                return
            elif current_mode == AppMode.PROCESSING and event_source == "keyboard":
                logger.info("✅ [VOICE] Режим PROCESSING, но активация разрешена - пользователь нажал Ctrl+N для прерывания воспроизведения")
            
            # КРИТИЧНО: Проверяем first_run перед началом записи
            if self._first_run_in_progress:
                logger.warning(
                    "⚠️ [VOICE_RECOGNITION] Блокировка активации - first_run в процессе. "
                    "Запись микрофона во время запроса разрешений запрещена."
                )
                return
            
            # ✅ ЗАЩИТА ОТ ПОВТОРНОЙ АКТИВАЦИИ: Проверка cooldown периода после остановки записи
            import time
            now = time.monotonic()
            time_since_last_stop = now - self._last_recording_stop_time
            if time_since_last_stop < self._recording_stop_cooldown_sec:
                logger.warning(f"🔒 VOICE: recording_start blocked by cooldown: {time_since_last_stop*1000:.1f}ms < {self._recording_stop_cooldown_sec*1000:.0f}ms после остановки записи, игнорируем")
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "voice_recognition_integration.py:733", "message": "recording_start blocked by cooldown", "data": {"time_since_last_stop": time_since_last_stop, "cooldown_sec": self._recording_stop_cooldown_sec, "session_id": session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                return

            # Поддерживаем оба формата: прямой и вложенный
            if "data" in event:
                data = event.get("data", {})
            else:
                data = event
            session_id = data.get("session_id")
            # Началась запись — фиксируем сессию
            # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
            self._set_session_id(session_id, reason="recording_start")
            self._recording_active = True

            # Перед началом записи пытаемся подготовить стриминговый распознаватель
            if self._streaming_feature_enabled and not self._streaming_env_disabled:
                await self._ensure_streaming_ready(context="recording_start")

            # Любое предыдущие распознавание отменяем
            await self._cancel_recognition(reason="new_recording_start")
            logger.info(f"🎤 [VOICE] recording_start, session={session_id}")

            # ✅ ДИАГНОСТИКА: Проверяем условия для новой логики
            logger.info(f"🔍 [VOICE] Проверка условий: _use_avf={self._use_avf}, _avf_engine={'None' if self._avf_engine is None else 'initialized'}")

            # ✅ НОВАЯ ЛОГИКА: AVF диагностика → Google запись
            if self._use_avf and self._avf_engine is not None:
                try:
                    # ✅ ШАГ 1: Получаем диагностику через AVF (активация на ~1 секунду)
                    logger.info("🔍 [AVF] Получение диагностики устройства...")
                    device_info = await self._get_device_info_via_avf()
                    if device_info:
                        # Сохраняем информацию об устройстве для использования
                        self._avf_device_info = device_info
                        logger.info(f"✅ [AVF] Информация об устройстве сохранена: {device_info.get('device_info', {}).get('name') if device_info.get('device_info') else 'unknown'}")
                    else:
                        logger.warning("⚠️ [AVF] Не удалось получить диагностику, продолжаем без неё")
                    
                    # ✅ ШАГ 2: Небольшая пауза для гарантии деактивации AVF
                    # ✅ ИСПРАВЛЕНИЕ 4: Используем значение из конфига вместо hardcoded
                    deactivation_pause = 0.2  # Значение по умолчанию
                    try:
                        loader = UnifiedConfigLoader()
                        avf_config = loader.get_audio_avf_config()
                        if 'avf' in avf_config and isinstance(avf_config['avf'], dict):
                            diagnostics_config = avf_config['avf'].get('diagnostics', {})
                            if isinstance(diagnostics_config, dict):
                                deactivation_pause = diagnostics_config.get('deactivation_pause_sec', 0.2)
                    except Exception as e:
                        logger.debug(f"🔍 [AVF] Не удалось прочитать конфиг, используем значение по умолчанию: {e}")
                    logger.info(f"⏳ [AVF] Пауза {deactivation_pause} сек для гарантии деактивации AVF (из конфига)")
                    await asyncio.sleep(deactivation_pause)
                    
                    # ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 2.1: Гарантированная деактивация AVF (5 попыток)
                    # ✅ КРИТИЧНО: Проверяем, что AVF полностью деактивирован после диагностики
                    max_avf_check_attempts = 5
                    avf_deactivated = False
                    for attempt in range(max_avf_check_attempts):
                        # Проверяем через свойство is_input_active
                        is_active = False
                        if hasattr(self._avf_engine, 'is_input_active'):
                            # is_input_active может быть свойством или методом
                            if callable(self._avf_engine.is_input_active):
                                is_active = self._avf_engine.is_input_active()
                            else:
                                is_active = self._avf_engine.is_input_active
                        
                        if is_active:
                            logger.warning(f"⚠️ [AVF] AVF все еще активен (попытка {attempt+1}/{max_avf_check_attempts})")
                            await asyncio.sleep(0.2)
                        else:
                            logger.info(f"✅ [AVF] AVF полностью деактивирован (попытка {attempt+1})")
                            avf_deactivated = True
                            break
                    
                    if not avf_deactivated:
                        logger.error("❌ [AVF] AVF не деактивирован после всех попыток - возможен конфликт с Google Speech Recognition")
                        raise RuntimeError("AVF not deactivated after all attempts - cannot activate Google Speech Recognition")
                    
                    # ✅ ШАГ 3: Активируем Google через speech_recognition напрямую
                    try:
                        import speech_recognition as sr
                        import threading
                        
                        # ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 2.2: Обязательная проверка разрешений (ошибка → исключение)
                        try:
                            from modules.permissions.first_run.status_checker import check_microphone_status, PermissionStatus as StatusCheckerPermissionStatus
                            mic_status = check_microphone_status()
                            logger.info(f"🔍 [Google] Проверка разрешений микрофона: {mic_status} (value={mic_status.value})")
                            # ✅ Исправление: сравниваем по значению, так как enum из разных модулей могут быть разными объектами
                            if mic_status.value != "granted":
                                logger.error(f"❌ [Google] Разрешение микрофона не предоставлено: {mic_status} (value={mic_status.value})")
                                raise RuntimeError(f"Microphone permission not granted: {mic_status.value}")
                        except RuntimeError:
                            # ✅ Пробрасываем RuntimeError (отсутствие разрешений)
                            # ✅ КРИТИЧНО: Закрываем микрофон при ошибке разрешений
                            logger.error("❌ [Google] Ошибка активации микрофона: разрешения не предоставлены")
                            self.state_manager.set_microphone_state("idle", session_id=None, reason="google_mic_activate_exception")
                            await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                            raise
                        except Exception as perm_error:
                            # ✅ Пробрасываем любую ошибку проверки разрешений
                            logger.error(f"❌ [Google] Критическая ошибка проверки разрешений: {perm_error}")
                            # ✅ КРИТИЧНО: Закрываем микрофон при ошибке проверки разрешений
                            self.state_manager.set_microphone_state("idle", session_id=None, reason="google_mic_activate_exception")
                            await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                            raise RuntimeError(f"Microphone permission check failed: {perm_error}") from perm_error
                        
                        logger.info("🎤 [Google] Активация микрофона через speech_recognition...")
                        
                        # ✅ КРИТИЧНО: Получаем конфигурацию от AVF для настройки Google микрофона
                        device_index = None
                        sample_rate = None
                        chunk_size = 1024  # Значение по умолчанию
                        
                        if device_info and device_info.get('input_format'):
                            input_format = device_info['input_format']
                            sample_rate = input_format.get('sample_rate')
                            logger.info(f"🔍 [Google] Используем sample_rate={sample_rate}Hz от AVF")
                        
                        # ✅ КРИТИЧНО: Находим device_index по имени устройства от AVF
                        if device_info and device_info.get('device_info') and device_info['device_info'].get('name'):
                            device_name = device_info['device_info']['name']
                            try:
                                # Получаем список всех микрофонов
                                mic_names = sr.Microphone.list_microphone_names()
                                logger.info(f"🔍 [Google] Доступно микрофонов: {len(mic_names)}")
                                
                                # Ищем индекс устройства по имени
                                for idx, name in enumerate(mic_names):
                                    if device_name.lower() in name.lower() or name.lower() in device_name.lower():
                                        device_index = idx
                                        logger.info(f"✅ [Google] Найден device_index={device_index} для устройства '{device_name}' (PyAudio имя: '{name}')")
                                        break
                                
                                if device_index is None:
                                    logger.warning(f"⚠️ [Google] Не удалось найти device_index для '{device_name}', используем default")
                                    logger.debug(f"🔍 [Google] Доступные микрофоны: {mic_names}")
                            except Exception as e:
                                logger.warning(f"⚠️ [Google] Ошибка поиска device_index: {e}, используем default")
                        
                        # ✅ КРИТИЧНО: Создаём recognizer и microphone с конфигурацией от AVF
                        recognizer = sr.Recognizer()
                        
                        # Создаём microphone с параметрами от AVF (если доступны)
                        if device_index is not None and sample_rate is not None:
                            logger.info(f"✅ [Google] Создаём Microphone с device_index={device_index}, sample_rate={sample_rate}Hz")
                            microphone = sr.Microphone(device_index=device_index, sample_rate=sample_rate, chunk_size=chunk_size)
                        elif sample_rate is not None:
                            logger.info(f"✅ [Google] Создаём Microphone с sample_rate={sample_rate}Hz (device_index=default)")
                            microphone = sr.Microphone(sample_rate=sample_rate, chunk_size=chunk_size)
                        elif device_index is not None:
                            logger.info(f"✅ [Google] Создаём Microphone с device_index={device_index} (sample_rate=default)")
                            microphone = sr.Microphone(device_index=device_index, chunk_size=chunk_size)
                        else:
                            logger.warning("⚠️ [Google] Конфигурация от AVF недоступна, используем default параметры")
                            microphone = sr.Microphone()
                        
                        # Сохраняем для использования в _on_recording_stop
                        self._google_recognizer = recognizer
                        self._google_microphone = microphone
                        self._google_audio_data: Optional[sr.AudioData] = None
                        with self._google_audio_chunks_lock:
                            self._google_audio_chunks = []  # Накопление аудио чанков
                        self._google_chunk_event.clear()
                        
                        # Сохраняем время начала записи
                        import time
                        self._recording_start_time = time.time()
                        
                        # ✅ ИСПОЛЬЗУЕМ listen_in_background() для контроля записи
                        # Это позволяет остановить запись при voice.recording_stop
                        # ✅ КРИТИЧНО: Устанавливаем флаг активности перед запуском
                        self._google_recording_active = True
                        
                        def callback(recognizer, audio):
                            """Callback для обработки аудио из listen_in_background"""
                            # ✅ КРИТИЧНО: Логируем ВСЕГДА, даже если callback будет проигнорирован
                            logger.info(f"🔔 [Google] Callback ВЫЗВАН! audio_size={len(audio.get_raw_data()) if hasattr(audio, 'get_raw_data') else 0} bytes")
                            # #region agent log (entry)
                            import json
                            import time
                            try:
                                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback ENTRY", "data": {"google_recording_active": self._google_recording_active, "google_stop_listening": self._google_stop_listening is not None, "state_mic_active": self.state_manager.is_microphone_active(), "audio_size": len(audio.get_raw_data()) if hasattr(audio, 'get_raw_data') else 0}, "timestamp": int(time.time() * 1000)}) + "\n")
                            except: pass
                            # #endregion
                            try:
                                # ✅ КРИТИЧНО: Проверяем флаг активности перед обработкой аудио
                                # Это предотвращает обработку callback'ов после остановки микрофона
                                if not self._google_recording_active:
                                    logger.warning("🔒 [Google] Callback игнорирован: запись уже остановлена (_google_recording_active=False)")
                                    # #region agent log
                                    try:
                                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback ignored: _google_recording_active=False", "data": {"google_recording_active": False, "state_mic_active": self.state_manager.is_microphone_active()}, "timestamp": int(time.time() * 1000)}) + "\n")
                                    except: pass
                                    # #endregion
                                    return
                                
                                # ✅ КРИТИЧНО: Дополнительная проверка _google_stop_listening
                                # Если он None, значит микрофон был остановлен
                                if self._google_stop_listening is None:
                                    logger.warning("🔒 [Google] Callback игнорирован: _google_stop_listening is None")
                                    # #region agent log
                                    import json
                                    import time
                                    try:
                                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback ignored: _google_stop_listening is None", "data": {"google_stop_listening": None, "state_mic_active": self.state_manager.is_microphone_active()}, "timestamp": int(time.time() * 1000)}) + "\n")
                                    except: pass
                                    # #endregion
                                    return
                                
                                # ✅ КРИТИЧНО: Проверяем флаг воспроизведения ПЕРЕД обработкой аудио
                                # Если воспроизведение активно, callback должен игнорировать аудио
                                # НО: если микрофон был активирован пользователем (_user_initiated_recording=True), разрешаем обработку для прерывания воспроизведения
                                # Это предотвращает автоматическую активацию микрофона во время воспроизведения ответа ассистента
                                # но разрешает пользователю прерывать воспроизведение нажатием Ctrl+N
                                playback_active = hasattr(self, '_playback_active') and self._playback_active
                                user_initiated = hasattr(self, '_user_initiated_recording') and self._user_initiated_recording
                                # #region agent log
                                import json
                                import time
                                try:
                                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback checking playback flags", "data": {"playback_active": playback_active, "user_initiated": user_initiated, "google_recording_active": self._google_recording_active, "state_mic_active": self.state_manager.is_microphone_active()}, "timestamp": int(time.time() * 1000)}) + "\n")
                                except: pass
                                # #endregion
                                if playback_active:
                                    # ✅ КРИТИЧНО: Если микрофон был активирован пользователем, разрешаем обработку аудио даже во время воспроизведения
                                    # Это позволяет пользователю прерывать воспроизведение нажатием Ctrl+N
                                    if user_initiated:
                                        logger.info("✅ [Google] Callback разрешен: воспроизведение активно, но микрофон активирован пользователем - разрешаем обработку для прерывания")
                                    else:
                                        logger.warning("🔒 [Google] Callback игнорирован: воспроизведение активно (_playback_active=True) - автоматическая активация микрофона заблокирована")
                                        # #region agent log
                                        try:
                                            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback ignored: playback active (automatic activation)", "data": {"playback_active": True, "user_initiated": False, "google_recording_active": self._google_recording_active, "state_mic_active": self.state_manager.is_microphone_active()}, "timestamp": int(time.time() * 1000)}) + "\n")
                                        except: pass
                                        # #endregion
                                        return
                                
                                # ✅ КРИТИЧНО: Проверяем состояние микрофона в state_manager
                                # Если микрофон не активен в state_manager, значит он был закрыт
                                state_mic_active = self.state_manager.is_microphone_active()
                                if not state_mic_active:
                                    logger.warning("🔒 [Google] Callback игнорирован: микрофон не активен в state_manager (возможно, воспроизведение активно) - принудительно сбрасываем флаг")
                                    logger.warning(f"🔒 [Google] Детали: _google_recording_active={self._google_recording_active}, state_mic_active={state_mic_active}, _google_stop_listening={self._google_stop_listening is not None}")
                                    # ✅ КРИТИЧНО: Сбрасываем флаг активности, чтобы последующие callback'и не обрабатывались
                                    self._google_recording_active = False
                                    # #region agent log
                                    import json
                                    import time
                                    try:
                                        with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                            f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback ignored: microphone not active in state_manager", "data": {"state_mic_active": False, "google_recording_active_before": self._google_recording_active, "google_recording_active_after": False}, "timestamp": int(time.time() * 1000)}) + "\n")
                                    except: pass
                                    # #endregion
                                    return
                                
                                # ✅ УДАЛЕНО: Проверка режима PROCESSING в callback
                                # Эта проверка избыточна, так как мы уже блокируем автоматическую активацию в начале _on_recording_start
                                # и перед вызовом listen_in_background. Проверка в callback мешает нормальной работе микрофона
                                # при нажатии пользователя (source="keyboard") во время PROCESSING режима.
                                # Если микрофон активирован (прошел проверки выше), значит это было разрешено, и callback должен обрабатывать аудио.
                                
                                # #region agent log
                                import json
                                import time
                                try:
                                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "H", "location": "voice_recognition_integration.py:callback", "message": "Callback processing audio chunk", "data": {"google_recording_active": self._google_recording_active, "state_mic_active": state_mic_active, "audio_size": len(audio.get_raw_data()) if hasattr(audio, 'get_raw_data') else 0}, "timestamp": int(time.time() * 1000)}) + "\n")
                                except: pass
                                # #endregion
                                
                                # ✅ ИСПРАВЛЕНИЕ: Синхронизированный доступ к _google_audio_chunks
                                with self._google_audio_chunks_lock:
                                    self._google_audio_chunks.append(audio)
                                    chunks_count = len(self._google_audio_chunks)
                                    self._google_chunk_event.set()
                                raw_data = audio.get_raw_data() if hasattr(audio, 'get_raw_data') else b''
                                logger.info(f"🔍 [Google] Получен чанк аудио #{chunks_count}: {len(raw_data)} bytes (всего чанков: {chunks_count})")
                            except Exception as e:
                                logger.error(f"❌ [Google] Ошибка обработки аудио в callback: {e}", exc_info=True)
                        
                        # Настраиваем микрофон для фонового шума
                        try:
                            # ✅ КРИТИЧНО: Уменьшаем duration для более быстрой настройки
                            # и устанавливаем более низкий энергетический порог
                            logger.info(f"🔍 [Google] Настройка фонового шума (duration=0.3)...")
                            recognizer.adjust_for_ambient_noise(microphone, duration=0.3)
                            logger.info(f"✅ [Google] Фоновый шум настроен")
                            # ✅ КРИТИЧНО: Устанавливаем более низкий энергетический порог для лучшей чувствительности
                            # По умолчанию порог может быть слишком высоким для тихой речи
                            if hasattr(recognizer, 'energy_threshold'):
                                current_threshold = recognizer.energy_threshold
                                # ✅ КРИТИЧНО: Устанавливаем очень низкий порог для гарантии вызова callback
                                # Уменьшаем порог на 50% для максимальной чувствительности
                                recognizer.energy_threshold = max(30, int(current_threshold * 0.5))
                                logger.info(f"🔍 [Google] Энергетический порог установлен: {recognizer.energy_threshold} (было: {current_threshold})")
                            else:
                                logger.warning("⚠️ [Google] recognizer не имеет атрибута energy_threshold")
                        except Exception as e:
                            logger.warning(f"⚠️ [Google] Не удалось настроить фоновый шум: {e}")
                            # ✅ КРИТИЧНО: Устанавливаем очень низкий порог даже при ошибке настройки
                            try:
                                if hasattr(recognizer, 'energy_threshold'):
                                    recognizer.energy_threshold = 30  # Очень низкий порог по умолчанию для гарантии вызова callback
                                    logger.info(f"🔍 [Google] Энергетический порог установлен по умолчанию: {recognizer.energy_threshold}")
                                else:
                                    logger.warning("⚠️ [Google] recognizer не имеет атрибута energy_threshold после ошибки настройки")
                            except Exception as e2:
                                logger.warning(f"⚠️ [Google] Не удалось установить энергетический порог: {e2}")
                        
                        # ✅ ИСПРАВЛЕНИЕ 7: Логируем параметры микрофона для проверки формата
                        mic_sample_rate = microphone.SAMPLE_RATE if hasattr(microphone, 'SAMPLE_RATE') else None
                        mic_sample_width = microphone.SAMPLE_WIDTH if hasattr(microphone, 'SAMPLE_WIDTH') else None
                        mic_device_index = microphone.device_index if hasattr(microphone, 'device_index') else None
                        logger.info(f"✅ [Google] Микрофон создан с параметрами:")
                        logger.info(f"   - device_index={mic_device_index}")
                        logger.info(f"   - sample_rate={mic_sample_rate}Hz")
                        logger.info(f"   - sample_width={mic_sample_width} bytes")
                        if device_info and device_info.get('input_format'):
                            avf_sample_rate = device_info['input_format'].get('sample_rate')
                            if avf_sample_rate and mic_sample_rate and avf_sample_rate != mic_sample_rate:
                                logger.warning(f"⚠️ [Google] Несоответствие sample_rate: AVF={avf_sample_rate}Hz, Google={mic_sample_rate}Hz")
                            else:
                                logger.info(f"✅ [Google] sample_rate совпадает с AVF: {mic_sample_rate}Hz")
                        
                        # Запускаем фоновое прослушивание
                        logger.info("🎤 [Google] Начинаем запись через recognizer.listen_in_background()...")
                        # ✅ КРИТИЧНО: Проверяем, что AVF не активен перед активацией Google
                        avf_still_active = hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active
                        if avf_still_active:
                            logger.error("❌ [Google] AVF все еще активен перед активацией Google Speech Recognition - возможен конфликт доступа к микрофону!")
                            logger.error(f"❌ [Google] Принудительно останавливаем AVF перед активацией Google Speech Recognition")
                            # ✅ КРИТИЧНО: Принудительно останавливаем AVF перед активацией Google
                            try:
                                await self._avf_engine.stop_input()
                                logger.info("✅ [Google] AVF остановлен принудительно")
                                # Ждём немного, чтобы AVF освободил микрофон
                                await asyncio.sleep(0.2)
                                # Проверяем ещё раз
                                avf_still_active_after = hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active
                                if avf_still_active_after:
                                    logger.error("❌ [Google] AVF все еще активен после принудительной остановки - критическая проблема!")
                                else:
                                    logger.info("✅ [Google] AVF успешно остановлен, микрофон освобожден")
                            except Exception as e:
                                logger.error(f"❌ [Google] Ошибка принудительной остановки AVF: {e}", exc_info=True)
                        else:
                            logger.info(f"✅ [Google] AVF не активен перед активацией Google Speech Recognition (is_input_active=False)")
                        # #region agent log
                        import json
                        import time
                        try:
                            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "I", "location": "voice_recognition_integration.py:998", "message": "Before listen_in_background", "data": {"google_recording_active": self._google_recording_active, "google_stop_listening": self._google_stop_listening is not None, "mic_device_index": device_index, "mic_sample_rate": sample_rate, "recognizer_energy_threshold": recognizer.energy_threshold if hasattr(recognizer, 'energy_threshold') else None, "avf_still_active": avf_still_active}, "timestamp": int(time.time() * 1000)}) + "\n")
                        except: pass
                        # #endregion
                        logger.info(f"🔍 [Google] Вызов listen_in_background: device_index={device_index}, sample_rate={sample_rate}, energy_threshold={recognizer.energy_threshold if hasattr(recognizer, 'energy_threshold') else 'N/A'}")
                        logger.info(f"🔍 [Google] Состояние перед listen_in_background: _google_recording_active={self._google_recording_active}, _google_stop_listening={self._google_stop_listening is not None}")
                        logger.info(f"🔍 [Google] Параметры микрофона: device_index={mic_device_index if 'mic_device_index' in locals() else device_index}, sample_rate={mic_sample_rate if 'mic_sample_rate' in locals() else sample_rate}")
                        logger.info(f"🔍 [Google] AVF состояние перед listen_in_background: is_input_active={avf_still_active if 'avf_still_active' in locals() else 'N/A'}")
                        # ✅ КРИТИЧНО: Проверяем разрешения микрофона перед вызовом listen_in_background
                        try:
                            from modules.permissions.first_run.status_checker import check_microphone_status, PermissionStatus as StatusCheckerPermissionStatus
                            mic_status = check_microphone_status()
                            logger.info(f"🔍 [Google] Разрешения микрофона перед listen_in_background: {mic_status} (value={mic_status.value})")
                            # ✅ Исправление: сравниваем по значению, так как enum из разных модулей могут быть разными объектами
                            if mic_status.value != "granted":
                                logger.error(f"❌ [Google] Разрешение микрофона не предоставлено: {mic_status} (value={mic_status.value})")
                                raise RuntimeError(f"Microphone permission not granted: {mic_status.value}")
                        except RuntimeError:
                            # ✅ Пробрасываем RuntimeError (отсутствие разрешений)
                            raise
                        except Exception as perm_error:
                            # ✅ Пробрасываем любую ошибку проверки разрешений
                            logger.error(f"❌ [Google] Критическая ошибка проверки разрешений: {perm_error}")
                            raise RuntimeError(f"Microphone permission check failed: {perm_error}") from perm_error
                        # ✅ КРИТИЧНО: Логируем вызов listen_in_background для диагностики
                        logger.info(f"🔍 [Google] ВЫЗОВ listen_in_background: microphone={microphone}, callback={callback}, recognizer={recognizer}")
                        logger.info(f"🔍 [Google] microphone.device_index={microphone.device_index if hasattr(microphone, 'device_index') else 'N/A'}, microphone.SAMPLE_RATE={microphone.SAMPLE_RATE if hasattr(microphone, 'SAMPLE_RATE') else 'N/A'}")
                        # ✅ КРИТИЧНО: Проверяем, что callback не None
                        if callback is None:
                            logger.error("❌ [Google] Callback is None - невозможно активировать listen_in_background!")
                            raise RuntimeError("Callback is None")
                        # ✅ КРИТИЧНО: Проверяем режим ПЕРЕД активацией микрофона
                        # Если режим PROCESSING, значит идет воспроизведение ответа ассистента
                        # НО: разрешаем активацию микрофона по нажатию пользователя (source="keyboard") для прерывания воспроизведения
                        # Блокируем только автоматическую активацию (когда source не "keyboard")
                        current_mode = self.state_manager.get_current_mode() if hasattr(self.state_manager, 'get_current_mode') else None
                        event_source = event_data.get("source") if isinstance(event_data, dict) else None
                        if current_mode == AppMode.PROCESSING and event_source != "keyboard":
                            logger.warning("🔒 [Google] Режим PROCESSING (воспроизведение ответа ассистента) - автоматическая активация микрофона заблокирована (source не keyboard)")
                            # ✅ КРИТИЧНО: Сбрасываем флаг активности, чтобы предотвратить активацию
                            self._google_recording_active = False
                            raise RuntimeError("Cannot activate microphone during PROCESSING mode (automatic activation blocked, user keyboard press allowed)")
                        elif current_mode == AppMode.PROCESSING and event_source == "keyboard":
                            logger.info("✅ [Google] Режим PROCESSING, но активация разрешена - пользователь нажал Ctrl+N для прерывания воспроизведения")
                        
                        # ✅ КРИТИЧНО: Устанавливаем состояние микрофона ПЕРЕД вызовом listen_in_background
                        # Это предотвращает race condition: callback может быть вызван до установки состояния
                        logger.info("🔍 [Google] Устанавливаем состояние микрофона ПЕРЕД listen_in_background (предотвращение race condition)")
                        self.state_manager.set_microphone_state("active", session_id=str(session_id), reason="google_recording_started")
                        await self.event_bus.publish("microphone.opened", {"session_id": session_id})
                        logger.info("✅ [Google] Состояние микрофона установлено: active")

                        self._google_stop_listening = recognizer.listen_in_background(microphone, callback)
                        logger.info(f"🔍 [Google] listen_in_background ВЫЗВАН, возвращено: {self._google_stop_listening is not None}")
                        # ✅ ИСПРАВЛЕНИЕ 1: Проверяем возвращаемое значение listen_in_background
                        if self._google_stop_listening is None:
                            raise RuntimeError("recognizer.listen_in_background вернул None - запись не запущена")
                        logger.info(f"✅ [Google] listen_in_background вернул функцию остановки: {self._google_stop_listening is not None}")
                        # #region agent log
                        try:
                            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "I", "location": "voice_recognition_integration.py:990", "message": "After listen_in_background", "data": {"google_stop_listening": self._google_stop_listening is not None, "google_recording_active": self._google_recording_active}, "timestamp": int(time.time() * 1000)}) + "\n")
                        except: pass
                        # #endregion
                        logger.info("✅ [Google] Фоновое прослушивание запущено (без ограничений по времени), stop_listening получен")
                        # ✅ КРИТИЧНО: Ждём немного и проверяем, был ли вызван callback
                        logger.info("⏳ [Google] Ожидание первого callback (2 секунды)...")
                        await asyncio.sleep(2.0)
                        callback_called = self._google_chunk_event.is_set()
                        with self._google_audio_chunks_lock:
                            chunks_count = len(self._google_audio_chunks) if hasattr(self, '_google_audio_chunks') else 0
                        if callback_called:
                            logger.info(f"✅ [Google] Callback вызван! Получено чанков: {chunks_count}")
                        else:
                            logger.error(f"❌ [Google] Callback НЕ вызван через 2 секунды после listen_in_background!")
                            logger.error(f"❌ [Google] Диагностика:")
                            logger.error(f"   - _google_recording_active={self._google_recording_active}")
                            logger.error(f"   - _google_stop_listening={self._google_stop_listening is not None}")
                            logger.error(f"   - state_mic_active={self.state_manager.is_microphone_active()}")
                            logger.error(f"   - energy_threshold={recognizer.energy_threshold if hasattr(recognizer, 'energy_threshold') else 'N/A'}")
                            logger.error(f"   - device_index={mic_device_index if 'mic_device_index' in locals() else device_index}")
                            logger.error(f"   - sample_rate={mic_sample_rate if 'mic_sample_rate' in locals() else sample_rate}")
                            logger.error(f"   - AVF is_input_active={avf_still_active if 'avf_still_active' in locals() else 'N/A'}")
                            logger.error(f"❌ [Google] Возможные причины:")
                            logger.error(f"   1. Конфликт доступа к микрофону (AVF или другое приложение)")
                            logger.error(f"   2. Проблемы с разрешениями микрофона")
                            logger.error(f"   3. Проблемы с PyAudio или speech_recognition библиотекой")
                            logger.error(f"   4. Неправильный device_index или sample_rate")
                            logger.error(f"   5. Слишком высокий energy_threshold (текущий: {recognizer.energy_threshold if hasattr(recognizer, 'energy_threshold') else 'N/A'})")
                        
                        logger.info("✅ [Google] Микрофон активирован, запись началась")
                        
                        # ✅ ПРИМЕЧАНИЕ: Состояние микрофона уже установлено ПЕРЕД listen_in_background (см. строку 1075)
                        # Это предотвращает race condition, когда callback вызывается до установки состояния
                        
                    except Exception as e:
                        logger.error(f"❌ [Google] Ошибка активации микрофона: {e}", exc_info=True)
                        # ✅ ИСПРАВЛЕНИЕ 2: Восстанавливаем состояние микрофона в state_manager
                        # Если microphone.opened уже был опубликован, нужно закрыть микрофон
                        if self.state_manager.is_microphone_active():
                            logger.warning("⚠️ [Google] Микрофон был открыт, но произошла ошибка - закрываем")
                            self.state_manager.set_microphone_state("idle", session_id=None, reason="google_mic_activate_exception")
                            await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                            await self.event_bus.publish("voice.recognition_failed", {
                                "session_id": session_id,
                                "error": f"Microphone activation failed: {str(e)}",
                                "source": "google_recognition"
                            })
                        # ✅ Очищаем состояние при ошибке
                        self._google_recording_active = False  # ✅ КРИТИЧНО: Сбрасываем флаг активности
                        self._google_recognizer = None
                        self._google_microphone = None
                        with self._google_audio_chunks_lock:
                            self._google_audio_chunks = []
                        self._google_stop_listening = None
                        self._recording_active = False
                        self._set_session_id(None, reason="google_mic_activate_exception")
                        return
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка в новой логике активации: {e}", exc_info=True)
                    # ✅ Очищаем состояние при ошибке
                    self._google_recording_active = False  # ✅ КРИТИЧНО: Сбрасываем флаг активности
                    self._google_recognizer = None
                    self._google_microphone = None
                    with self._google_audio_chunks_lock:
                        self._google_audio_chunks = []
                    self._google_stop_listening = None
                    self.state_manager.set_microphone_state("idle", session_id=None, reason="activation_exception")
                    self._recording_active = False
                    self._set_session_id(None, reason="avf_mic_open_failed")
                    logger.error(f"❌ [DEBUG] AVF ошибка: _use_avf={self._use_avf}, _avf_engine={self._avf_engine is not None}")
                    if self._is_streaming_session_live(session_id):
                        await self._handle_streaming_failure(session_id, "avf_exception", disable=False)
                    # Отменяем стриминг если запущен
                    if self._is_streaming_active():
                        await self._sf_recognizer.cancel()
                    return
            else:
                # ✅ ДИАГНОСТИКА: Логируем почему новая логика не используется
                reason = []
                if not self._use_avf:
                    reason.append("_use_avf=False")
                if self._avf_engine is None:
                    reason.append("_avf_engine=None")
                logger.warning(f"⚠️ [VOICE] Новая логика AVF→Google НЕ используется: {', '.join(reason) if reason else 'неизвестная причина'}")
                logger.info(f"🔍 [VOICE] Переход на legacy путь или симуляцию")
            
            # Legacy путь или симуляция
            if not self.config.simulate and self._recognizer is not None:
                # Legacy путь через SpeechRecognizer (sounddevice)
                logger.warning("⚠️ [VOICE] Используется LEGACY путь через SpeechRecognizer.start_listening() - это активирует AVF поток!")
                try:
                    await self._recognizer.start_listening()
                    # ✅ КРИТИЧНО: Обновляем состояние микрофона в state_manager ПЕРЕД публикацией события
                    self.state_manager.set_microphone_state("active", session_id=str(session_id), reason="legacy_recording_started")
                    await self.event_bus.publish("microphone.opened", {"session_id": session_id})
                    logger.info(f"✅ [VOICE] Микрофон открыт через SpeechRecognizer для session {session_id}")
                except Exception as e:
                    logger.error(f"❌ [VOICE] Ошибка открытия микрофона: {e}")
                    # ✅ КРИТИЧНО: Обновляем состояние при ошибке (idle)
                    self.state_manager.set_microphone_state("idle", session_id=None, reason="mic_open_failed")
                    self._recording_active = False
                    self._set_session_id(None, reason="mic_open_failed")
                    return
            else:
                # Симуляция
                # ✅ КРИТИЧНО: Обновляем состояние микрофона в state_manager даже для симуляции
                self.state_manager.set_microphone_state("active", session_id=str(session_id), reason="simulated_recording_started")
                await self.event_bus.publish("microphone.opened", {"session_id": session_id})
            
            # Публикуем voice.recognition_started для единообразия (microphone.opened будет опубликовано в _on_microphone_open_requested)
            await self.event_bus.publish("voice.recognition_started", {
                "session_id": session_id,
                "language": self.config.language
            })
            logger.debug(f"✓ voice.recognition_started опубликован для session {session_id}")
        except Exception as e:
            logger.error(f"VOICE: error in recording_start handler: {e}")

    async def _on_recording_stop(self, event: Dict[str, Any]):
        try:
            # ✅ КРИТИЧНО: Логирование входа в метод для диагностики залипания
            logger.info(f"🛑 VOICE: _on_recording_stop ВХОД: event={event}")
            # #region agent log
            import json
            import time
            try:
                event_data = event.get("data", {}) if isinstance(event, dict) else event
                session_id = event_data.get("session_id") if isinstance(event_data, dict) else None
                google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
                state_mic_active = self.state_manager.is_microphone_active()
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "voice_recognition_integration.py:1017", "message": "_on_recording_stop called", "data": {"session_id": session_id, "google_mic_active": google_mic_active, "legacy_mic_active": legacy_mic_active, "state_mic_active": state_mic_active, "recording_active": getattr(self, "_recording_active", False)}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            
            # Поддерживаем оба формата: прямой и вложенный
            if "data" in event:
                data = event.get("data", {})
            else:
                data = event
            session_id = data.get("session_id")
            # ✅ ИСПРАВЛЕНИЕ: Получаем duration из события для обрезки аудио
            duration = data.get("duration")
            logger.info(f"🛑 VOICE: recording_stop, session={session_id} (type: {type(session_id)}), duration={duration}")

            # Останавливаем запись — запускаем распознавание для этой сессии
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id (единый источник истины)
            active_session_id = self._get_active_session_id()
            # ✅ ДИАГНОСТИКА: Проверяем что session_id действительно в state_manager
            state_manager_session = self.state_manager.get_current_session_id()
            logger.info(f"🛑 VOICE: active_session_id={active_session_id} (type: {type(active_session_id)}), request_session_id={session_id} (type: {type(session_id)})")
            logger.info(f"🛑 VOICE: state_manager.get_current_session_id()={state_manager_session} (type: {type(state_manager_session)})")
            
            # ✅ ЭТАП 1: Если session_id is None, но микрофон активен - принудительно останавливаем микрофон
            # Это может произойти при SHORT_PRESS после LONG_PRESS, когда микрофон уже открыт, но сессия была отменена
            if session_id is None:
                # ✅ КРИТИЧНО: Проверяем оба типа микрофонов (Google и legacy)
                google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
                
                if google_mic_active or legacy_mic_active:
                    logger.warning(f"⚠️ VOICE: recording_stop с session_id=None, но микрофон активен (google={google_mic_active}, legacy={legacy_mic_active}) - принудительно останавливаем микрофон")
                    
                    # ✅ КРИТИЧНО: Останавливаем Google микрофон, если активен
                    if google_mic_active:
                        try:
                            logger.info("🛑 [Google] Принудительная остановка Google микрофона (session_id=None)")
                            # ✅ КРИТИЧНО: Сначала сбрасываем флаг активности, чтобы callback'и не обрабатывались
                            self._google_recording_active = False
                            # ✅ КРИТИЧНО: Небольшая задержка для завершения текущих callback'ов
                            await asyncio.sleep(0.1)
                            # ✅ КРИТИЧНО: Останавливаем listen_in_background
                            self._google_stop_listening(wait_for_stop=False)
                            logger.info("✅ [Google] Google микрофон принудительно остановлен (session_id=None)")
                            # Очищаем состояние
                            self._google_stop_listening = None
                            self._google_recognizer = None
                            self._google_microphone = None
                            with self._google_audio_chunks_lock:
                                self._google_audio_chunks = []
                        except Exception as e:
                            logger.error(f"❌ [Google] Ошибка принудительной остановки Google микрофона: {e}", exc_info=True)
                            # ✅ КРИТИЧНО: Даже при ошибке сбрасываем флаг активности
                            self._google_recording_active = False
                            # ✅ КРИТИЧНО: Принудительно синхронизируем состояние при ошибке
                            if self.state_manager.is_microphone_active():
                                logger.warning("⚠️ [VOICE] state_manager всё ещё показывает active после ошибки (session_id=None) - принудительная синхронизация")
                                self.state_manager.force_close_microphone(reason="error_sync_no_session")
                                await self.event_bus.publish("microphone.closed", {"session_id": None})
                    
                    # ✅ КРИТИЧНО: Останавливаем legacy микрофон, если активен
                    if legacy_mic_active:
                        try:
                            await self._recognizer.stop_listening()
                            logger.info("✅ VOICE: legacy микрофон принудительно остановлен (session_id=None)")
                        except Exception as e:
                            logger.error(f"❌ VOICE: ошибка принудительной остановки legacy микрофона: {e}")
                    
                    # ⚠️ MicrophoneStateManager удалён (Этап 1) - используем прямой вызов
                    logger.warning("⚠️ [VOICE] Принудительное закрытие микрофона (временная заглушка)")
                    # ✅ КРИТИЧНО: Сначала обновляем состояние, затем публикуем событие
                    state_changed = self.state_manager.force_close_microphone(reason="recording_stop_no_session")
                    if state_changed:
                        logger.info("✅ [VOICE] Состояние микрофона обновлено на idle через force_close_microphone")
                    # ✅ КРИТИЧНО: Проверяем, что состояние действительно обновлено
                    if self.state_manager.is_microphone_active():
                        logger.warning("⚠️ [VOICE] state_manager всё ещё показывает active после force_close_microphone - повторная попытка")
                        self.state_manager.set_microphone_state("idle", session_id=None, reason="force_close_retry")
                    await self.event_bus.publish("microphone.closed", {"session_id": None})
                    logger.debug("🎤 VOICE: ожидание закрытия микрофона (принудительная остановка)")
                    self._recording_active = False
                else:
                    logger.debug("VOICE: recording_stop с session_id=None, микрофон не активен - игнорируем")
                    # ⚠️ MicrophoneStateManager удалён (Этап 1) - проверяем только state_manager
                    if self.state_manager.is_microphone_active():
                        logger.warning("⚠️ VOICE: state_manager показывает активный микрофон, но recognizer не активен - синхронизируем состояние")
                        self.state_manager.force_close_microphone(reason="state_mismatch")
                return
            
            # ✅ КРИТИЧНО: Сравнение session_id (оба теперь строки)
            # Конвертируем оба в строки для корректного сравнения
            active_session_str = str(active_session_id) if active_session_id is not None else None
            request_session_str = str(session_id) if session_id is not None else None
            
            logger.info(f"🛑 VOICE: Сравнение session_id: active='{active_session_str}' vs request='{request_session_str}'")
            
            if active_session_str != request_session_str:
                # Не наша сессия — игнорируем
                logger.warning(f"⚠️ VOICE: recording_stop ignored (session mismatch: active={active_session_str}, request={request_session_str})")
                
                # ✅ КРИТИЧНО: Даже при mismatch принудительно останавливаем микрофон, если он активен
                # Проверяем оба типа микрофонов (Google и legacy)
                google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
                
                if google_mic_active or legacy_mic_active:
                    logger.warning(f"⚠️ VOICE: Session mismatch, но микрофон активен (google={google_mic_active}, legacy={legacy_mic_active}) - принудительно останавливаем микрофон")
                    
                    # ✅ КРИТИЧНО: Останавливаем Google микрофон, если активен
                    if google_mic_active:
                        try:
                            logger.info("🛑 [Google] Принудительная остановка Google микрофона (session mismatch)")
                            # ✅ КРИТИЧНО: Сначала сбрасываем флаг активности, чтобы callback'и не обрабатывались
                            self._google_recording_active = False
                            # ✅ КРИТИЧНО: Небольшая задержка для завершения текущих callback'ов
                            await asyncio.sleep(0.1)
                            # ✅ КРИТИЧНО: Останавливаем listen_in_background
                            self._google_stop_listening(wait_for_stop=False)
                            logger.info("✅ [Google] Google микрофон принудительно остановлен (session mismatch)")
                            # Очищаем состояние (флаг уже сброшен выше на строке 1040)
                            self._google_stop_listening = None
                            self._google_recognizer = None
                            self._google_microphone = None
                            with self._google_audio_chunks_lock:
                                self._google_audio_chunks = []
                            # Обновляем состояние микрофона
                            state_changed = self.state_manager.set_microphone_state("idle", session_id=None, reason="google_recording_stopped_mismatch")
                            if state_changed:
                                logger.info("✅ [VOICE] Состояние микрофона обновлено на idle через set_microphone_state")
                            # ✅ КРИТИЧНО: Проверяем, что состояние действительно обновлено
                            if self.state_manager.is_microphone_active():
                                logger.warning("⚠️ [VOICE] state_manager всё ещё показывает active после set_microphone_state - повторная попытка")
                                self.state_manager.force_close_microphone(reason="set_idle_retry")
                            await self.event_bus.publish("microphone.closed", {"session_id": request_session_str})
                        except Exception as e:
                            logger.error(f"❌ [Google] Ошибка принудительной остановки Google микрофона (session mismatch): {e}", exc_info=True)
                            # ✅ КРИТИЧНО: Даже при ошибке сбрасываем флаг активности
                            self._google_recording_active = False
                            # ✅ КРИТИЧНО: Принудительно синхронизируем состояние при ошибке
                            if self.state_manager.is_microphone_active():
                                logger.warning("⚠️ [VOICE] state_manager всё ещё показывает active после ошибки - принудительная синхронизация")
                                self.state_manager.force_close_microphone(reason="error_sync_after_mismatch")
                                await self.event_bus.publish("microphone.closed", {"session_id": request_session_str})
                    
                    # ✅ КРИТИЧНО: Останавливаем legacy микрофон, если активен
                    if legacy_mic_active:
                        try:
                            if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                                with getattr(self._recognizer, '_stream_lock', threading.RLock()):
                                    if self._recognizer._current_stream and self._recognizer._current_stream.active:
                                        logger.warning("🛑 VOICE: Принудительная остановка потока (session mismatch)")
                                        self._recognizer._current_stream.stop()
                                        logger.info("✅ VOICE: Поток остановлен принудительно (session mismatch)")
                            await self._recognizer.stop_listening()
                            logger.info("✅ VOICE: legacy микрофон принудительно остановлен (session mismatch)")
                        except Exception as e:
                            logger.error(f"❌ VOICE: Ошибка принудительной остановки legacy микрофона (session mismatch): {e}")
                return

            self._recording_active = False
            
            # ✅ КРИТИЧНО: Флаг для отслеживания публикации microphone.closed
            # Это предотвращает двойную публикацию события
            mic_closed_published = False
            
            # ✅ КРИТИЧНО: ПРОВЕРЯЕМ ФИЗИЧЕСКОЕ СОСТОЯНИЕ ПОТОКА ПЕРЕД ВСЕМ ОСТАЛЬНЫМ
            # Это предотвращает залипание микрофона, даже если state_manager рассинхронизирован
            stream_was_active = False
            if self._recognizer is not None and hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                with getattr(self._recognizer, '_stream_lock', threading.RLock()):
                    if self._recognizer._current_stream and self._recognizer._current_stream.active:
                        stream_was_active = True
                        logger.warning("🛑 VOICE: Поток физически активен - принудительно останавливаем ПЕРЕД request_close")
                        try:
                            self._recognizer._current_stream.stop()
                            logger.info("✅ VOICE: Поток остановлен принудительно (проверка физического состояния)")
                            # ✅ КРИТИЧНО: Публикуем microphone.closed СРАЗУ после остановки потока
                            # Это разрывает deadlock: request_close ждет microphone.closed, но оно публикуется только после stop_listening
                            # Но stop_listening вызывается только после request_close - deadlock!
                            # Решение: публикуем microphone.closed сразу после остановки потока
                            await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                            mic_closed_published = True
                            logger.info("✅ VOICE: microphone.closed опубликовано СРАЗУ после остановки потока (разрыв deadlock)")
                        except Exception as e:
                            logger.error(f"❌ VOICE: Ошибка принудительной остановки потока (проверка физического состояния): {e}")

            # ✅ КРИТИЧНО: НЕ закрываем микрофон в state_manager ДО остановки Google записи
            # Это позволяет callback'ам от listen_in_background обрабатываться до закрытия микрофона
            # Закрытие микрофона будет выполнено ПОСЛЕ остановки Google записи (см. строку 1441)
            # ⚠️ MicrophoneStateManager удалён (Этап 1) - используем прямой вызов через state_manager
            logger.info(f"🛑 VOICE: Закрытие микрофона будет выполнено ПОСЛЕ остановки Google записи, stream_was_active={stream_was_active}")

            # ✅ НОВАЯ ЛОГИКА: Останавливаем Google запись и распознаём
            logger.info(f"🔍 [Google] Проверка условий для новой логики: _use_avf={self._use_avf}, _google_recognizer={'initialized' if self._google_recognizer else 'None'}, _google_microphone={'initialized' if self._google_microphone else 'None'}")
            
            if self._use_avf and self._google_recognizer and self._google_microphone:
                # ✅ Останавливаем Google запись
                try:
                    logger.info("🎤 [Google] Остановка записи через speech_recognition...")
                    logger.info(f"🔍 [Google] Состояние перед остановкой: _google_stop_listening={'initialized' if hasattr(self, '_google_stop_listening') and self._google_stop_listening else 'None/not set'}")

                    # ✅ Настройки ожидания callback/чанков для listen_in_background
                    callback_wait = 0.5
                    chunk_wait = 1.0
                    try:
                        loader = UnifiedConfigLoader()
                        avf_config = loader.get_audio_avf_config()
                        if 'google_recognition' in avf_config and isinstance(avf_config['google_recognition'], dict):
                            google_cfg = avf_config['google_recognition']
                            callback_wait = float(google_cfg.get('callback_wait_sec', callback_wait))
                            chunk_wait = float(google_cfg.get('chunk_wait_sec', chunk_wait))
                            callback_wait = max(0.0, callback_wait)
                            chunk_wait = max(0.0, chunk_wait)
                    except Exception as e:
                        logger.debug(f"🔍 [Google] Не удалось прочитать конфиг ожидания: {e}")

                    # ⏳ Ждём появления хотя бы одного чанка перед остановкой потока
                    chunk_received = self._google_chunk_event.is_set()
                    if not chunk_received and chunk_wait > 0:
                        logger.info(f"⏳ [Google] Ожидание первого чанка до {chunk_wait:.2f}с перед остановкой listen_in_background")
                        try:
                            chunk_received = await asyncio.to_thread(self._google_chunk_event.wait, chunk_wait)
                        except Exception as wait_error:
                            logger.error(f"❌ [Google] Ошибка ожидания чанка: {wait_error}", exc_info=True)
                    if not chunk_received:
                        logger.warning("⚠️ [Google] Финальный чанк не получен до остановки listen_in_background (возможно, пользователь молчал или энергия порога слишком высока)")
                        # ✅ КРИТИЧНО: Логируем текущий энергетический порог для диагностики
                        if hasattr(self._google_recognizer, 'energy_threshold'):
                            logger.warning(f"🔍 [Google] Текущий энергетический порог: {self._google_recognizer.energy_threshold}")
                        # ✅ КРИТИЧНО: Проверяем, был ли callback вызван хотя бы раз
                        if not self._google_chunk_event.is_set():
                            logger.error("❌ [Google] Callback НИ РАЗУ не был вызван - проблема с активацией микрофона или разрешениями!")
                            logger.error("🔍 [Google] Диагностика:")
                            logger.error(f"   - _google_recording_active={self._google_recording_active}")
                            logger.error(f"   - _google_stop_listening={self._google_stop_listening is not None}")
                            logger.error(f"   - state_mic_active={self.state_manager.is_microphone_active()}")
                            logger.error(f"   - energy_threshold={self._google_recognizer.energy_threshold if hasattr(self._google_recognizer, 'energy_threshold') else 'N/A'}")
                            logger.error(f"   - microphone.device_index={self._google_microphone.device_index if hasattr(self._google_microphone, 'device_index') else 'N/A'}")
                            logger.error("🔍 [Google] Проверьте:")
                            logger.error("   1. Разрешения микрофона в System Settings → Privacy & Security → Microphone")
                            logger.error("   2. Микрофон подключен и работает")
                            logger.error("   3. Нет конфликтов с другими приложениями, использующими микрофон")
                            logger.error("   4. AVF не держит микрофон (is_input_active=False)")
                            logger.error("   5. PyAudio правильно установлен и работает")

                    # ✅ ОСТАНОВКА ЗАПИСИ: Останавливаем listen_in_background()
                    # ✅ ИСПРАВЛЕНИЕ 6: Улучшенная обработка исключений при вызове _google_stop_listening
                    if hasattr(self, '_google_stop_listening') and self._google_stop_listening:
                        try:
                            logger.info("🛑 [Google] Остановка фонового прослушивания...")
                            # ✅ КРИТИЧНО: Сначала сбрасываем флаг активности, чтобы callback'и не обрабатывались
                            self._google_recording_active = False
                            # ✅ КРИТИЧНО: Небольшая задержка для завершения текущих callback'ов
                            await asyncio.sleep(0.1)
                            
                            # Останавливаем фоновое прослушивание (wait_for_stop=False для быстрой остановки)
                            # ✅ ИСПРАВЛЕНИЕ 6: Перехватываем исключения от PyAudio (OSError и др.)
                            try:
                                self._google_stop_listening(wait_for_stop=False)
                                logger.info("✅ [Google] Фоновое прослушивание остановлено")
                            except OSError as e:
                                logger.error(f"❌ [Google] OSError при остановке прослушивания (PyAudio): {e}", exc_info=True)
                                # Продолжаем работу, даже если остановка не удалась
                            except Exception as e:
                                logger.error(f"❌ [Google] Неожиданная ошибка при остановке прослушивания: {e}", exc_info=True)
                                # Продолжаем работу

                            # Ждём немного для завершения последних callback'ов
                            await asyncio.sleep(callback_wait)
                        except Exception as e:
                            logger.error(f"❌ [Google] Критическая ошибка при остановке фонового прослушивания: {e}", exc_info=True)
                            # ✅ КРИТИЧНО: Даже при ошибке сбрасываем флаг активности
                            self._google_recording_active = False
                    elif self._google_stop_listening is None:
                        logger.warning("⚠️ [Google] _google_stop_listening is None, запись может не остановиться корректно")
                        # ✅ КРИТИЧНО: Сбрасываем флаг активности, если _google_stop_listening уже None
                        self._google_recording_active = False

                    # ✅ ИСПРАВЛЕНИЕ: Синхронизированный доступ к _google_audio_chunks
                    import speech_recognition as sr
                    with self._google_audio_chunks_lock:
                        chunks_count = len(self._google_audio_chunks)
                        logger.info(f"🔍 [Google] Проверка накопленных чанков: {chunks_count} чанков")
                        # #region agent log
                        import json
                        import time
                        try:
                            total_bytes_before = sum(len(chunk.get_raw_data()) if hasattr(chunk, 'get_raw_data') else 0 for chunk in self._google_audio_chunks)
                            with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "J", "location": "voice_recognition_integration.py:1541", "message": "Checking accumulated chunks", "data": {"chunks_count": chunks_count, "total_bytes_before": total_bytes_before, "session_id": session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                        except: pass
                        # #endregion

                        if chunks_count > 0:
                            # ✅ ИСПРАВЛЕНИЕ: Объединяем ВСЕ чанки, а не только последний
                            # Используем первый чанк как основу и добавляем остальные
                            first_chunk = self._google_audio_chunks[0]
                            
                            # Логируем детали каждого чанка
                            for i, chunk in enumerate(self._google_audio_chunks):
                                chunk_bytes = len(chunk.get_raw_data()) if hasattr(chunk, 'get_raw_data') else 0
                                chunk_duration = chunk_bytes / (chunk.sample_rate * chunk.sample_width) if hasattr(chunk, 'sample_rate') and hasattr(chunk, 'sample_width') else 0
                                logger.info(f"   Чанк #{i+1}: {chunk_bytes} bytes, {chunk_duration:.2f}s, {chunk.sample_rate if hasattr(chunk, 'sample_rate') else 'unknown'}Hz")
                            
                            if chunks_count == 1:
                                # Один чанк - используем как есть
                                self._google_audio_data = first_chunk
                                total_bytes = len(first_chunk.get_raw_data())
                            else:
                                # Объединяем несколько чанков
                                all_raw_data = first_chunk.get_raw_data()
                                for chunk in self._google_audio_chunks[1:]:
                                    all_raw_data += chunk.get_raw_data()
                                
                                # Создаём новый AudioData из объединённых данных
                                sample_rate = first_chunk.sample_rate
                                sample_width = first_chunk.sample_width
                                self._google_audio_data = sr.AudioData(all_raw_data, sample_rate, sample_width)
                                total_bytes = len(all_raw_data)
                                logger.info(f"✅ [Google] Объединено {chunks_count} чанков: {total_bytes} bytes, {sample_rate}Hz, {sample_width} bytes/sample")
                            
                            logger.info(f"✅ [Google] Получены данные из {chunks_count} чанков: {total_bytes} bytes")
                            # #region agent log
                            try:
                                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "J", "location": "voice_recognition_integration.py:1574", "message": "Audio data prepared for recognition", "data": {"chunks_count": chunks_count, "total_bytes": total_bytes, "sample_rate": first_chunk.sample_rate if chunks_count > 0 else None, "sample_width": first_chunk.sample_width if chunks_count > 0 else None, "duration_sec": total_bytes / (first_chunk.sample_rate * first_chunk.sample_width) if chunks_count > 0 and hasattr(first_chunk, 'sample_rate') and hasattr(first_chunk, 'sample_width') else 0, "session_id": session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                            except: pass
                            # #endregion
                        else:
                            logger.warning("⚠️ [Google] Нет накопленных чанков после остановки записи")
                            # #region agent log
                            try:
                                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "J", "location": "voice_recognition_integration.py:1576", "message": "No chunks accumulated", "data": {"chunks_count": 0, "session_id": session_id}, "timestamp": int(time.time() * 1000)}) + "\n")
                            except: pass
                            # #endregion
                            logger.warning("🔍 [Google] Возможные причины:")
                            logger.warning("   - Callback не вызывался (проверьте логи 'Получен чанк аудио')")
                            logger.warning("   - Микрофон не активировался (проверьте разрешения)")
                            logger.warning("   - Запись была слишком короткой (< 0.1 сек)")
                            self._google_audio_data = None
                    
                    # ✅ ИСПРАВЛЕНИЕ 3: Детальная очистка и публикация voice.recognition_failed если нет данных
                    if self._google_audio_data:
                        logger.info(f"✅ [Google] Получены данные: {len(self._google_audio_data.get_raw_data())} bytes")
                        # Распознаём через Google
                        await self._recognize_google_audio(self._google_audio_data, session_id)
                    else:
                        logger.warning("⚠️ [Google] Нет данных от записи (нулевая длительность или ошибка записи)")
                        # ✅ Детальная очистка состояния
                        self._google_recording_active = False  # ✅ КРИТИЧНО: Сбрасываем флаг активности
                        self._google_recognizer = None
                        self._google_microphone = None
                        with self._google_audio_chunks_lock:
                            self._google_audio_chunks = []
                        self._google_stop_listening = None
                        # ✅ Публикуем ошибку
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": "No audio data from Google recording (zero duration or recording error)",
                            "source": "google_recognition",
                            "device_info": self._avf_device_info  # Передаём диагностику от AVF
                        })
                    
                    # ✅ Очищаем состояние (гарантированная очистка)
                    self._google_recording_active = False  # ✅ КРИТИЧНО: Сбрасываем флаг активности
                    self._google_audio_data = None
                    with self._google_audio_chunks_lock:
                        self._google_audio_chunks = []  # ✅ ИСПРАВЛЕНИЕ 5: Очистка уже выполнена в finally _recognize_google_audio, но дублируем для безопасности
                    self._google_stop_listening = None
                    
                except Exception as e:
                    logger.error(f"❌ [Google] Ошибка остановки записи: {e}", exc_info=True)
                    await self.event_bus.publish("voice.recognition_failed", {
                        "session_id": session_id,
                        "error": str(e),
                        "source": "google_recognition"
                    })
                finally:
                    # ✅ КРИТИЧНО: Гарантированно сбрасываем флаг активности в finally
                    self._google_recording_active = False
                    # ✅ КРИТИЧНО: Сбрасываем флаг пользовательской активации при остановке записи
                    self._user_initiated_recording = False
                    # ✅ КРИТИЧНО: Обновляем состояние микрофона ПОСЛЕ остановки Google записи
                    # Это позволяет callback'ам от listen_in_background обрабатываться до закрытия микрофона
                    self.state_manager.set_microphone_state("idle", session_id=None, reason="google_recording_stopped")
                    # ✅ КРИТИЧНО: Публикуем microphone.closed только если оно еще не было опубликовано
                    # (например, если поток был остановлен принудительно выше)
                    if not mic_closed_published:
                        await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                    self._google_chunk_event.clear()
                    
                    # ✅ КРИТИЧНО: Принудительно сбрасываем is_listening для _recognizer
                    # Это необходимо, так как при использовании Google микрофона stop_listening() не вызывается
                    if self._recognizer is not None and hasattr(self._recognizer, 'is_listening'):
                        if self._recognizer.is_listening:
                            logger.warning("⚠️ VOICE: is_listening все еще True при использовании Google микрофона - принудительно сбрасываем")
                            self._recognizer.is_listening = False
                            # Также останавливаем поток, если он активен
                            if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                                try:
                                    if self._recognizer._current_stream.active:
                                        self._recognizer._current_stream.stop()
                                        logger.info("✅ VOICE: Поток остановлен принудительно (Google микрофон)")
                                except Exception as e:
                                    logger.warning(f"⚠️ VOICE: Ошибка принудительной остановки потока (Google микрофон): {e}")
                
                # ✅ КРИТИЧНО: Возвращаемся, чтобы не выполнять старую логику stop_listening
                # Новая логика Google записи уже обработала всё необходимое
                logger.debug("✅ [Google] Новая логика Google записи завершена, возвращаемся")
                return
            
            # ✅ LEGACY: Старая логика AVF (если не используется новая логика)
            elif self._use_avf and self._avf_engine is not None:
                # Используем AVFAudioEngine для остановки записи
                try:
                    result = await self._avf_engine.stop_input()
                    if result:
                        logger.info(f"✅ [AVF] Запись остановлена через AVFAudioEngine: {result.frames_recorded} frames, {result.duration_ms:.1f}ms")
                        
                        # ✅ Этап 4: Если стриминг активен, получаем финальный результат
                        streaming_processed = False
                        if self._is_streaming_session_live(session_id):
                            logger.info("🎤 [SFSpeech] Завершение стримингового распознавания...")
                            try:
                                timeout = getattr(self, '_streaming_timeout', 5.0)
                                final_text = await self._sf_recognizer.finish_recognition(timeout=timeout)
                                if not final_text and self._streaming_partial_result:
                                    final_text = self._streaming_partial_result
                                
                                if final_text:
                                    logger.info(f"✅ [SFSpeech] Стриминговый результат: '{final_text[:100]}...' (session={session_id})")
                                    await self.event_bus.publish("voice.recognition_completed", {
                                        "session_id": session_id,
                                        "text": final_text,
                                        "confidence": None,
                                        "language": self.config.language,
                                        "source": "sf_speech_streaming"
                                    })
                                    streaming_processed = True
                                else:
                                    logger.warning(f"⚠️ [SFSpeech] Пустой результат стриминга (session={session_id})")
                                    await self.event_bus.publish("voice.recognition_failed", {
                                        "session_id": session_id,
                                        "error": "Empty streaming result",
                                        "source": "sf_speech_streaming"
                                    })
                            except Exception as e:
                                logger.error(f"❌ [SFSpeech] Ошибка завершения стриминга: {e}", exc_info=True)
                                await self.event_bus.publish("voice.recognition_failed", {
                                    "session_id": session_id,
                                    "error": str(e),
                                    "source": "sf_speech_streaming"
                                })
                            finally:
                                self._streaming_session_active = False
                                self._streaming_session_id = None
                                self._streaming_partial_result = None
                                self._streaming_error = None
                        
                        # ✅ ЭСТАФЕТА: Публикуем событие ТОЛЬКО если есть данные в result
                        # AVF освободил микрофон, теперь можно безопасно использовать данные
                        # ✅ ОСНОВНОЙ ПУТЬ: Данные получены от AVF, но новая логика использует Google запись напрямую
                        # Legacy путь с voice.mic_data_ready удалён, так как событие не обрабатывается
                        # НЕ обрабатываем буфер здесь, чтобы избежать двойного распознавания
                        if result.data and len(result.data) > 0:
                            # Данные получены, но используем Google запись напрямую (не через voice.mic_data_ready)
                            pass
                        elif self._audio_buffer and not streaming_processed:
                            # ✅ LEGACY FALLBACK: Если result.data пустой, используем буфер (fallback для совместимости)
                            logger.warning(f"⚠️ [AVF] result.data пустой, используем legacy fallback из буфера")
                            total_audio = b''.join(self._audio_buffer)
                            # ✅ ЦЕНТРАЛИЗАЦИЯ: Используем sample_rate из конфигурации или из буфера
                            sample_rate = self._audio_buffer_sample_rate or getattr(self, '_batch_sample_rate', 48000)
                            channels = self._audio_buffer_channels or 1
                            
                            # ✅ ИСПРАВЛЕНИЕ: Обрезаем аудио по duration из события (если указано)
                            if duration is not None and self._recording_start_time is not None:
                                import time
                                actual_duration = time.time() - self._recording_start_time
                                expected_duration = float(duration)
                                
                                # ✅ ИСПРАВЛЕНИЕ: Всегда обрезаем до expected_duration (не только если больше)
                                # Это гарантирует, что в Google уйдёт именно ожидаемая длительность
                                bytes_per_second = sample_rate * channels * 2  # 2 bytes per sample (int16)
                                expected_bytes = int(expected_duration * bytes_per_second)
                                if expected_bytes < len(total_audio):
                                    total_audio = total_audio[:expected_bytes]
                                    logger.info(f"✂️ [AVF] Обрезано аудио: {len(b''.join(self._audio_buffer))} → {len(total_audio)} bytes (duration: {actual_duration:.2f}s → {expected_duration:.2f}s)")
                                elif expected_bytes > len(total_audio):
                                    logger.debug(f"🔍 [AVF] Аудио короче ожидаемого: {len(total_audio)} < {expected_bytes} bytes (duration: {actual_duration:.2f}s < {expected_duration:.2f}s)")
                            else:
                                # ✅ ЗАПАСНОЙ ВАРИАНТ: Если duration отсутствует, обрезаем тишину автоматически (VAD/trim)
                                logger.debug(f"🔍 [AVF] duration не указан, выполняем автоматическую обрезку тишины...")
                                total_audio = self._trim_silence(total_audio, sample_rate, channels)
                                if len(total_audio) < len(b''.join(self._audio_buffer)):
                                    logger.info(f"✂️ [AVF] Автоматически обрезано тишины: {len(b''.join(self._audio_buffer))} → {len(total_audio)} bytes")
                            
                            logger.info(f"🔊 [AVF] Накоплено {len(total_audio)} bytes аудио для batch-распознавания")
                            logger.info(f"📤 [AVF] Отправляем на распознавание: {len(total_audio)} bytes, {sample_rate}Hz, {channels}ch")
                            
                            # ✅ ЭСТАФЕТА: Используем данные из буфера (legacy путь для совместимости)
                            # В будущем можно перейти на voice.mic_data_ready для единообразия
                            # Отправляем на распознавание через библиотеку SpeechRecognition
                            try:
                                await self._recognize_avf_audio(
                                    total_audio,
                                    sample_rate,
                                    channels,
                                    session_id
                                )
                            except Exception as e:
                                logger.error(f"❌ [AVF] Ошибка распознавания аудио: {e}", exc_info=True)
                                await self.event_bus.publish("voice.recognition_failed", {
                                    "session_id": session_id,
                                    "error": str(e),
                                    "source": "avf_recognition"
                                })
                        
                        # ✅ ИСПРАВЛЕНИЕ: Очищаем время начала записи
                        self._recording_start_time = None
                        
                        # ✅ КРИТИЧНО: Обновляем состояние микрофона в state_manager ПЕРЕД публикацией события
                        self.state_manager.set_microphone_state("idle", session_id=None, reason="avf_recording_stopped")
                        
                        # Публикуем событие закрытия микрофона
                        if not stream_was_active:
                            await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                            logger.debug(f"✅ [AVF] microphone.closed опубликовано для session {session_id}")
                    else:
                        logger.warning("⚠️ [AVF] stop_input вернул None")
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка остановки записи через AVFAudioEngine: {e}", exc_info=True)
                finally:
                    # ✅ КРИТИЧНО: Буфер будет очищен в finally блоке
                    self._clear_audio_buffer()
                    self._recording_start_time = None
                    logger.debug(f"🧹 [VOICE] Буфер очищен в finally блоке _on_recording_stop")
                return

            # ✅ КРИТИЧНО: Добавляем логирование для диагностики залипания
            logger.info(f"🔍 VOICE: Проверка условий для stop_listening: simulate={self.config.simulate}, recognizer={self._recognizer is not None}")
            if self.config.simulate:
                logger.warning("⚠️ VOICE: config.simulate=True, stop_listening не вызывается")
                return
            if self._recognizer is None:
                logger.error("❌ VOICE: _recognizer is None, stop_listening не вызывается")
                return
            
            logger.info("🛑 VOICE: Условия для stop_listening выполнены, вызываем stop_listening")
            if not self.config.simulate and self._recognizer is not None:
                # ✅ КРИТИЧНО: Принудительно останавливаем поток ПЕРЕД вызовом stop_listening
                # Это предотвращает продолжение вызовов callback после voice.recording_stop
                try:
                    if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                        with getattr(self._recognizer, '_stream_lock', threading.RLock()):
                            if self._recognizer._current_stream and self._recognizer._current_stream.active:
                                logger.warning("🛑 VOICE: Принудительная остановка потока ПЕРЕД stop_listening")
                                try:
                                    self._recognizer._current_stream.stop()
                                    logger.info("✅ VOICE: Поток остановлен принудительно")
                                except Exception as e:
                                    logger.error(f"❌ VOICE: Ошибка принудительной остановки потока: {e}")
                except Exception as e:
                    logger.warning(f"⚠️ VOICE: Ошибка проверки потока перед stop_listening: {e}")
                
                # ✅ FIX: Синхронно останавливаем микрофон для немедленного закрытия
                try:
                    logger.info(f"🎤 Вызов stop_listening для session {session_id}")
                    result: "RecognitionResult" = await self._recognizer.stop_listening()
                    
                    # ✅ КРИТИЧНО: Проверяем, что is_listening действительно обновлен после stop_listening
                    # Если нет, принудительно обновляем состояние
                    if hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening:
                        logger.warning("⚠️ VOICE: is_listening все еще True после stop_listening - принудительно обновляем состояние")
                        # Принудительно устанавливаем is_listening = False
                        self._recognizer.is_listening = False
                        # Дополнительно останавливаем поток, если он еще активен
                        if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                            try:
                                if self._recognizer._current_stream.active:
                                    self._recognizer._current_stream.stop()
                                    logger.info("✅ VOICE: Поток остановлен принудительно (is_listening был True)")
                            except Exception as e:
                                logger.warning(f"⚠️ VOICE: Ошибка принудительной остановки потока: {e}")
                    
                    # ✅ КРИТИЧНО: Обновляем состояние микрофона в state_manager ПЕРЕД публикацией события
                    self.state_manager.set_microphone_state("idle", session_id=None, reason="legacy_recording_stopped")
                    
                    # ✅ ЭТАП 2: Публикуем событие успешного закрытия микрофона
                    # КРИТИЧНО: microphone.closed может быть уже опубликовано выше (если поток был остановлен принудительно)
                    # Проверяем, не было ли оно уже опубликовано, чтобы избежать дублирования
                    # Но если поток не был остановлен принудительно, публикуем здесь
                    if not stream_was_active:
                        await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                        logger.debug(f"✅ VOICE: microphone.closed опубликовано для session {session_id} (после stop_listening)")
                    else:
                        logger.debug(f"✅ VOICE: microphone.closed уже опубликовано выше (поток был остановлен принудительно)")

                    # Диагностика результата
                    chunks_count = getattr(self._recognizer, 'audio_data_len', 0) if hasattr(self._recognizer, 'audio_data_len') else 'N/A'
                    logger.debug(f"🎤 stop_listening завершён: chunks={chunks_count}, text={result.text if result else None}, error={result.error if result else None}")

                    if result and result.text and not result.error:
                        logger.info(f"✓ Распознавание успешно: text='{result.text[:50]}...', confidence={result.confidence}")
                        await self.event_bus.publish("voice.recognition_completed", {
                            "session_id": session_id,
                            "text": result.text,
                            "confidence": result.confidence,
                            "language": result.language
                        })
                    else:
                        error_msg = result.error if result else "unknown"
                        logger.warning(f"⚠️ Распознавание не дало текста: error={error_msg}, chunks={chunks_count}")
                        if chunks_count == 0 or chunks_count == 'N/A':
                            logger.warning(f"⚠️ Похоже на тишину: chunks={chunks_count}")
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": error_msg,
                            "reason": "no_text"
                        })
                except Exception as e:
                    logger.error(f"❌ VOICE: error while stopping listening/recognizing: {e}")
                    import traceback
                    logger.error(f"❌ Traceback: {traceback.format_exc()}")
                    # ✅ КРИТИЧНО: Обновляем состояние микрофона при ошибке
                    self.state_manager.set_microphone_state("idle", session_id=None, reason="legacy_recording_error")
                    # ✅ FIX: Все равно публикуем microphone.closed для закрытия микрофона
                    await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                    await self.event_bus.publish("voice.recognition_failed", {
                        "session_id": session_id,
                        "error": "recognition_error",
                        "reason": str(e)
                    })
            else:
                # Симуляция распознавания
                await self._start_recognition(session_id)
        except Exception as e:
            logger.error(f"VOICE: error in recording_stop handler: {e}")
        finally:
            # ✅ КРИТИЧНО: Гарантированная очистка буфера в конце обработки (для всех путей)
            self._clear_audio_buffer()
            self._recording_start_time = None
            # ✅ ЗАЩИТА ОТ ПОВТОРНОЙ АКТИВАЦИИ: Устанавливаем время последней остановки
            import time
            self._last_recording_stop_time = time.monotonic()
            logger.debug(f"🧹 [VOICE] Буфер очищен в finally блоке _on_recording_stop")
            
            # ✅ КРИТИЧНО: Проверяем состояние микрофона после небольшой задержки
            # Это дает время is_listening обновиться после stop_listening()
            async def check_mic_state_in_finally():
                await asyncio.sleep(0.2)  # Задержка для обновления is_listening
                google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
                state_mic_active = self.state_manager.is_microphone_active()
                
                # #region agent log
                import json
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "D", "location": "voice_recognition_integration.py:1602", "message": "_on_recording_stop finally (delayed check)", "data": {"google_mic_active": google_mic_active, "legacy_mic_active": legacy_mic_active, "state_mic_active": state_mic_active, "recording_active": getattr(self, "_recording_active", False)}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                
                # ✅ КРИТИЧНО: Если legacy микрофон все еще активен, принудительно останавливаем
                if legacy_mic_active:
                    logger.warning(f"⚠️ VOICE: legacy микрофон все еще активен в finally блоке (is_listening={legacy_mic_active}) - принудительно останавливаем")
                    try:
                        # Принудительно устанавливаем is_listening = False
                        if hasattr(self._recognizer, 'is_listening'):
                            self._recognizer.is_listening = False
                        # Останавливаем поток, если он еще активен
                        if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                            if self._recognizer._current_stream.active:
                                self._recognizer._current_stream.stop()
                                logger.info("✅ VOICE: Поток остановлен принудительно в finally блоке")
                        # Обновляем состояние микрофона
                        self.state_manager.set_microphone_state("idle", session_id=None, reason="legacy_mic_force_stop_finally")
                    except Exception as e:
                        logger.error(f"❌ VOICE: Ошибка принудительной остановки legacy микрофона в finally блоке: {e}")
            
            # Запускаем проверку асинхронно
            try:
                asyncio.create_task(check_mic_state_in_finally())
            except Exception as e:
                logger.warning(f"⚠️ VOICE: Ошибка создания задачи проверки микрофона в finally блоке: {e}")
    
    async def _get_device_info_via_avf(self) -> Optional[Dict[str, Any]]:
        """
        Получает информацию об устройстве через AVF (активация на ~1 секунду).
        
        AVF активирует микрофон на короткое время для получения:
        - Информации об устройстве (имя, UID)
        - Формата входного аудио (sample_rate, channels)
        - Диагностики (первый чанк, RMS, min/max)
        
        Returns:
            Dict с информацией: device_info, input_format, diagnostics
            None если не удалось получить
        """
        if not self._use_avf or not self._avf_engine:
            logger.warning("⚠️ [AVF] AVF недоступен для получения диагностики")
            return None
        
        try:
            logger.info("🔍 [AVF] Получение информации об устройстве (активация на ~1 секунду)...")
            
            # ✅ ШАГ 1: Активируем AVF на ~1 секунду
            success = await self._avf_engine.start_input()
            if not success:
                logger.warning("⚠️ [AVF] Не удалось активировать для диагностики")
                return None
            
            # ✅ ИСПРАВЛЕНИЕ 4: Используем значение из конфига вместо hardcoded
            activation_duration = 1.0  # Значение по умолчанию
            try:
                loader = UnifiedConfigLoader()
                avf_config = loader.get_audio_avf_config()
                if 'avf' in avf_config and isinstance(avf_config['avf'], dict):
                    diagnostics_config = avf_config['avf'].get('diagnostics', {})
                    if isinstance(diagnostics_config, dict):
                        activation_duration = diagnostics_config.get('activation_duration_sec', 1.0)
            except Exception as e:
                logger.debug(f"🔍 [AVF] Не удалось прочитать конфиг, используем значение по умолчанию: {e}")
            logger.debug(f"🔍 [AVF] Используем activation_duration={activation_duration} сек из конфига")
            await asyncio.sleep(activation_duration)
            
            # ✅ ШАГ 2: Останавливаем и получаем результат
            result = await self._avf_engine.stop_input()
            if not result:
                logger.warning("⚠️ [AVF] Не удалось получить диагностику")
                return None
            
            # Формируем информацию об устройстве
            device_info = {
                "device_info": {
                    "name": result.device_info.name if result.device_info else None,
                    "uid": result.device_info.uid if result.device_info else None,
                    "is_input": result.device_info.is_input if result.device_info else True
                } if result.device_info else None,
                "input_format": {
                    "sample_rate": result.input_format.sample_rate if result.input_format else None,
                    "channels": result.input_format.channels if result.input_format else None,
                    "bit_depth": result.input_format.bit_depth if result.input_format else 16
                } if result.input_format else None,
                "diagnostics": result.diagnostics
            }
            
            device_name = device_info['device_info']['name'] if device_info['device_info'] else 'unknown'
            format_info = device_info['input_format']
            logger.info(f"✅ [AVF] Диагностика получена: device={device_name}, format={format_info}")
            
            return device_info
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка получения диагностики: {e}", exc_info=True)
            return None
    
    async def _recognize_google_audio(self, audio_data: Any, session_id: str) -> None:
        """
        Распознавание аудио через Google Speech API.
        
        Args:
            audio_data: AudioData объект от speech_recognition
            session_id: ID сессии
        """
        try:
            import speech_recognition as sr
            
            # Проверяем тип данных
            if not isinstance(audio_data, sr.AudioData):
                logger.error(f"❌ [Google] Неверный тип данных: {type(audio_data)}")
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": "Invalid audio data type",
                    "source": "google_recognition"
                })
                return
            
            # Получаем язык из конфигурации
            language = self.config.language
            
            # Используем тот же recognizer, что использовался для записи
            recognizer = self._google_recognizer or sr.Recognizer()
            
            # ✅ ИСПРАВЛЕНИЕ 7: Логируем sample_rate для проверки формата
            audio_sample_rate = audio_data.sample_rate if hasattr(audio_data, 'sample_rate') else None
            audio_sample_width = audio_data.sample_width if hasattr(audio_data, 'sample_width') else None
            audio_size = len(audio_data.get_raw_data())
            duration_sec = audio_size / (audio_sample_rate * audio_sample_width) if audio_sample_rate and audio_sample_width else 0
            logger.info(f"🎤 [Google] Начинаем распознавание: language={language}, audio_size={audio_size} bytes, sample_rate={audio_sample_rate}Hz, sample_width={audio_sample_width}, duration={duration_sec:.2f}s")
            
            # ✅ КРИТИЧНО: Google Speech API рекомендует 16kHz, но принимает и другие частоты
            # Если sample_rate != 16000, библиотека speech_recognition автоматически конвертирует
            # Но лучше явно проверить и предупредить
            if audio_sample_rate and audio_sample_rate != 16000:
                logger.warning(f"⚠️ [Google] sample_rate={audio_sample_rate}Hz (рекомендуется 16kHz). Google Speech API может автоматически конвертировать, но качество может снизиться.")
            
            # Распознаём через Google
            try:
                # #region agent log
                import json
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({
                            "sessionId": "debug-session",
                            "runId": "run1",
                            "hypothesisId": "B",
                            "location": "voice_recognition_integration.py:1996",
                            "message": "Before Google recognition",
                            "data": {
                                "session_id": session_id,
                                "audio_size": audio_size,
                                "sample_rate": audio_sample_rate,
                                "sample_width": audio_sample_width,
                                "duration_sec": duration_sec,
                                "language": language
                            },
                            "timestamp": int(__import__('time').time() * 1000)
                        }) + "\n")
                except: pass
                # #endregion
                text = recognizer.recognize_google(audio_data, language=language)
                
                logger.info(f"✅ [Google] Распознавание успешно: '{text[:100]}...'")
                
                # Публикуем результат с диагностикой от AVF
                device_name = "unknown"
                if self._avf_device_info and self._avf_device_info.get('device_info'):
                    device_name = self._avf_device_info['device_info'].get('name', 'unknown')
                logger.info(f"📊 [Google] Передаём device_info в событие: device={device_name}")
                
                event_data = {
                    "session_id": session_id,
                    "text": text,
                    "confidence": None,
                    "language": language,
                    "source": "google_recognition",
                    "device_info": self._avf_device_info  # Добавляем диагностику от AVF
                }
                logger.info(f"📤 [Google] Публикуем voice.recognition_completed: session_id={session_id}, text='{text[:50]}...' (длина: {len(text)})")
                await self.event_bus.publish("voice.recognition_completed", event_data)
                
            except sr.UnknownValueError:
                logger.warning("⚠️ [Google] Речь не распознана")
                # #region agent log
                import json
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({
                            "sessionId": "debug-session",
                            "runId": "run1",
                            "hypothesisId": "A",
                            "location": "voice_recognition_integration.py:2017",
                            "message": "Google UnknownValueError - speech not recognized",
                            "data": {
                                "session_id": session_id,
                                "audio_size": audio_size,
                                "sample_rate": audio_sample_rate,
                                "sample_width": audio_sample_width,
                                "duration_sec": duration_sec,
                                "language": language,
                                "error": "Speech not recognized"
                            },
                            "timestamp": int(__import__('time').time() * 1000)
                        }) + "\n")
                except: pass
                # #endregion
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": "Speech not recognized",
                    "source": "google_recognition",
                    "device_info": self._avf_device_info  # Добавляем диагностику от AVF
                })
            except sr.RequestError as e:
                logger.error(f"❌ [Google] Ошибка сервиса: {e}")
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": str(e),
                    "source": "google_recognition",
                    "device_info": self._avf_device_info  # Добавляем диагностику от AVF
                })
            finally:
                # ✅ ИСПРАВЛЕНИЕ 5: Очищаем _google_audio_chunks в finally после вызова Google
                # Это гарантирует очистку даже при UnknownValueError или других ошибках
                with self._google_audio_chunks_lock:
                    self._google_audio_chunks = []
                logger.debug("🧹 [Google] _google_audio_chunks очищен в finally после распознавания")
                
        except Exception as e:
            logger.error(f"❌ [Google] Ошибка распознавания: {e}", exc_info=True)
            # ✅ ИСПРАВЛЕНИЕ 5: Очищаем _google_audio_chunks при общей ошибке
            with self._google_audio_chunks_lock:
                self._google_audio_chunks = []
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": str(e),
                "source": "google_recognition",
                "device_info": self._avf_device_info  # Добавляем диагностику от AVF
            })
    
    def _trim_silence(self, audio_data: bytes, sample_rate: int, channels: int, silence_threshold: float = 200.0, frame_duration_ms: int = 100) -> bytes:
        """
        Обрезает тишину в начале и конце аудио (простая VAD).
        
        Args:
            audio_data: PCM int16 аудио данные (bytes)
            sample_rate: Sample rate аудио
            channels: Количество каналов
            silence_threshold: Порог RMS для определения тишины (по умолчанию 200)
            frame_duration_ms: Длительность окна анализа в миллисекундах (по умолчанию 100мс)
        
        Returns:
            Обрезанные аудио данные (bytes)
        """
        try:
            import numpy as np
            
            # Конвертируем bytes в numpy array (int16)
            audio_array = np.frombuffer(audio_data, dtype=np.int16)
            
            # Если многоканальное - усредняем до моно для анализа
            if channels > 1:
                frame_count = len(audio_array) // channels
                audio_array_mono = audio_array[:frame_count * channels].reshape(frame_count, channels).mean(axis=1).astype(np.int16)
            else:
                audio_array_mono = audio_array
            
            # Размер окна в сэмплах
            frame_size = int(sample_rate * frame_duration_ms / 1000)
            
            # Находим начало речи (первый кадр с RMS > threshold)
            start_idx = 0
            for i in range(0, len(audio_array_mono) - frame_size, frame_size):
                frame = audio_array_mono[i:i + frame_size]
                rms = np.sqrt(np.mean(frame.astype(np.float32) ** 2))
                if rms > silence_threshold:
                    start_idx = i
                    break
            
            # Находим конец речи (последний кадр с RMS > threshold)
            end_idx = len(audio_array_mono)
            for i in range(len(audio_array_mono) - frame_size, 0, -frame_size):
                frame = audio_array_mono[i:i + frame_size]
                rms = np.sqrt(np.mean(frame.astype(np.float32) ** 2))
                if rms > silence_threshold:
                    end_idx = i + frame_size
                    break
            
            # Если многоканальное - конвертируем индексы обратно
            if channels > 1:
                start_idx = start_idx * channels
                end_idx = end_idx * channels
            
            # Обрезаем аудио
            trimmed_audio = audio_array[start_idx:end_idx]
            
            # Конвертируем обратно в bytes
            return trimmed_audio.tobytes()
            
        except Exception as e:
            logger.warning(f"⚠️ [AVF] Не удалось обрезать тишину: {e}, возвращаем исходное аудио")
            return audio_data
    
    async def _recognize_avf_audio(
        self,
        audio_data: bytes,
        sample_rate: int,
        channels: int,
        session_id: float
    ) -> None:
        """
        Распознает накопленное аудио из AVFAudioEngine через библиотеку SpeechRecognition
        
        Использует библиотеку speech_recognition (pip install SpeechRecognition),
        которая под капотом использует Google Speech API через метод recognize_google().
        
        Args:
            audio_data: PCM int16 аудио данные
            sample_rate: Sample rate аудио (исходный)
            channels: Количество каналов
            session_id: ID сессии
        """
        try:
            import numpy as np
            
            # ✅ КРИТИЧНО: Фиксируем исходный sample_rate для правильного вычисления duration
            original_sample_rate = sample_rate
            
            # Проверяем доступность speech_recognition
            if not importlib.util.find_spec("speech_recognition"):
                logger.error("❌ [AVF] speech_recognition не доступен для распознавания")
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": "speech_recognition not available",
                    "source": "avf_recognition"
                })
                return
            
            import speech_recognition as sr
            
            # Конвертируем bytes в numpy array (int16)
            audio_array_int16 = np.frombuffer(audio_data, dtype=np.int16)
            
            # ✅ КРИТИЧНО: Вычисляем duration ДО ресемплинга (по исходному sample_rate)
            # len(audio_array_int16) - это количество сэмплов (не байт!)
            # Для многоканального аудио: количество сэмплов = frames * channels
            # Duration = frames / sample_rate = (samples / channels) / sample_rate
            total_samples = len(audio_array_int16)
            total_frames = total_samples // channels  # Количество фреймов (каждый фрейм = channels сэмплов)
            original_duration_sec = total_frames / original_sample_rate
            
            logger.debug(f"🔍 [AVF] Исходное аудио: {total_samples} samples, {channels}ch, {total_frames} frames, {original_sample_rate}Hz → {original_duration_sec:.2f}s")
            
            # ✅ ДИАГНОСТИКА: Логируем характеристики аудио (RMS, первые sample значения)
            try:
                audio_rms = np.sqrt(np.mean(audio_array_int16.astype(np.float32) ** 2))
                first_samples = audio_array_int16[:min(10, len(audio_array_int16))].tolist()
                logger.info(f"🔍 [AVF] Характеристики аудио перед распознаванием:")
                logger.info(f"   - RMS={audio_rms:.2f}")
                logger.info(f"   - Первые 10 samples: {first_samples}")
                logger.info(f"   - Min={audio_array_int16.min()}, Max={audio_array_int16.max()}, Mean={audio_array_int16.mean():.1f}")
            except Exception as diag_error:
                logger.debug(f"🔍 [AVF] Не удалось проанализировать аудио: {diag_error}")
            
            # ✅ КРИТИЧНО: Сохраняем аудио в WAV файл ПЕРЕД распознаванием (для проверки качества)
            # Это позволяет прослушать файл и убедиться, что в буфер попадает голос, а не только клавиатура
            try:
                import os
                debug_audio_save = os.getenv("NEXY_DEBUG_SAVE_AUDIO", "false").lower() == "true"
                if debug_audio_save:
                    import wave
                    # Конвертируем session_id в строку для имени файла (может быть float или str)
                    session_id_str = str(session_id).replace(".", "_").replace("-", "_")
                    wav_path = f"/tmp/nexy_debug_session_{session_id_str}.wav"
                    with wave.open(wav_path, 'wb') as wav_file:
                        wav_file.setnchannels(channels)
                        wav_file.setsampwidth(2)  # int16 = 2 bytes
                        wav_file.setframerate(original_sample_rate)
                        wav_file.writeframes(audio_data)
                    logger.info(f"💾 [AVF] Аудио сохранено для диагностики (ДО распознавания): {wav_path}")
                    logger.info(f"💾 [AVF] Параметры сохраненного аудио: {len(audio_data)} bytes, {original_sample_rate}Hz, {channels}ch, duration={original_duration_sec:.2f}s")
                    logger.info(f"💾 [AVF] ПРОСЛУШАЙТЕ ФАЙЛ для проверки: есть ли голос или только клавиатура/тишина")
            except Exception as save_error:
                logger.debug(f"🔍 [AVF] Не удалось сохранить аудио: {save_error}")
            
            # Конвертируем int16 → float32 и нормализуем [-32768, 32767] → [-1.0, 1.0]
            # ✅ ИСПРАВЛЕНИЕ: Используем 32768.0 для симметричной нормализации (как при обратной конвертации)
            audio_array_float32 = audio_array_int16.astype(np.float32) / 32768.0
            
            # Если многоканальное - усредняем до моно
            if channels > 1:
                frame_count = len(audio_array_float32) // channels
                audio_array_float32 = audio_array_float32[:frame_count * channels].reshape(frame_count, channels).mean(axis=1)
            else:
                frame_count = len(audio_array_float32)
            
            # ✅ ИСПРАВЛЕНИЕ: Google Speech API требует 16kHz, конвертируем если нужно
            target_sample_rate = 16000  # Google Speech API стандарт
            if sample_rate != target_sample_rate:
                # Ресемплинг через scipy (если доступен) или простое усреднение
                try:
                    from scipy import signal
                    # Ресемплинг с использованием scipy
                    num_samples = int(frame_count * target_sample_rate / sample_rate)
                    logger.debug(f"🔄 [AVF] Ресемплинг: {sample_rate}Hz → {target_sample_rate}Hz ({frame_count} frames → {num_samples} frames)")
                    audio_array_float32 = signal.resample(audio_array_float32, num_samples)
                    sample_rate = target_sample_rate
                    frame_count = num_samples
                    logger.debug(f"🔄 [AVF] После ресемплинга: {frame_count} frames @ {sample_rate}Hz = {frame_count/sample_rate:.2f}s")
                except ImportError:
                    # Fallback: простое усреднение (не идеально, но лучше чем ничего)
                    logger.warning(f"⚠️ [AVF] scipy недоступен, используем простое усреднение для ресемплинга {sample_rate}Hz → {target_sample_rate}Hz")
                    # Простое усреднение: берём каждый N-й сэмпл
                    step = sample_rate // target_sample_rate
                    audio_array_float32 = audio_array_float32[::step]
                    sample_rate = target_sample_rate
                    frame_count = len(audio_array_float32)
            
            # Конвертируем обратно в int16 для sr.AudioData
            # ✅ ИСПРАВЛЕНИЕ: Используем полный диапазон int16 [-32768, 32767]
            audio_array_int16_resampled = (np.clip(audio_array_float32, -1.0, 1.0) * 32768.0).astype(np.int16)
            # Защита от переполнения
            audio_array_int16_resampled = np.clip(audio_array_int16_resampled, -32768, 32767)
            audio_bytes_int16 = audio_array_int16_resampled.tobytes()
            
            # ✅ ПРОВЕРКА: Валидация формата перед созданием AudioData
            if len(audio_bytes_int16) == 0:
                logger.error(f"❌ [AVF] Пустой аудио буфер после обработки!")
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": "Empty audio buffer",
                    "source": "avf_recognition"
                })
                return
            
            # ✅ ИСПРАВЛЕНИЕ: При использовании AVF не используем SpeechRecognizer (избегаем двойной активации микрофона)
            # Используем SpeechRecognizer только если НЕ используем AVF (legacy режим)
            # ✅ ЦЕНТРАЛИЗАЦИЯ: Используем language из конфигурации
            batch_language = getattr(self, '_batch_language', 'en-US')
            
            if self._use_avf:
                # ✅ КРИТИЧНО: При AVF создаём новый Recognizer напрямую (без SpeechRecognizer)
                # Это избегает двойной активации микрофона через PyAudio
                recognizer = sr.Recognizer()
                language = batch_language
                logger.debug(f"🔍 [AVF] Используем прямой Recognizer (избегаем двойной активации микрофона)")
            elif self._recognizer is not None and hasattr(self._recognizer, 'recognizer'):
                # Используем recognizer из SpeechRecognizer (legacy режим)
                recognizer = self._recognizer.recognizer
                language = getattr(self._recognizer.config, 'language', batch_language)
            else:
                # Создаём новый recognizer (fallback)
                recognizer = sr.Recognizer()
                language = batch_language
            
            # ✅ ИСПРАВЛЕНИЕ: Правильный расчёт duration для ресемплинга
            # Количество сэмплов = количество байт / 2 (int16 = 2 bytes per sample)
            num_samples_resampled = len(audio_bytes_int16) // 2
            resampled_duration_sec = num_samples_resampled / sample_rate
            
            # ✅ ДИАГНОСТИКА: Детальная информация перед распознаванием
            audio_rms_original = np.sqrt(np.mean(audio_array_int16.astype(np.float32) ** 2))
            audio_array_resampled = np.frombuffer(audio_bytes_int16, dtype=np.int16).astype(np.float32)
            audio_rms_resampled = np.sqrt(np.mean(audio_array_resampled ** 2))
            
            # ✅ ДИАГНОСТИКА: Проверка диапазона значений (должны быть в [-32768, 32767])
            min_val = audio_array_resampled.min()
            max_val = audio_array_resampled.max()
            mean_val = audio_array_resampled.mean()
            
            logger.info(f"🔍 [AVF] Параметры распознавания:")
            logger.info(f"   - language={language}")
            logger.info(f"   - sample_rate (original)={original_sample_rate}Hz")
            logger.info(f"   - sample_rate (resampled)={sample_rate}Hz")
            logger.info(f"   - audio_size={len(audio_bytes_int16)} bytes ({num_samples_resampled} samples)")
            logger.info(f"   - duration (original)={original_duration_sec:.2f}s")
            logger.info(f"   - duration (resampled)={resampled_duration_sec:.2f}s")
            logger.info(f"   - RMS (original)={audio_rms_original:.2f}")
            logger.info(f"   - RMS (resampled)={audio_rms_resampled:.2f}")
            logger.info(f"   - Range: min={min_val:.1f}, max={max_val:.1f}, mean={mean_val:.1f}")
            
            # ✅ ПРОВЕРКА: Валидация аудио перед отправкой в Google
            if resampled_duration_sec < 0.3:
                logger.warning(f"⚠️ [AVF] Аудио слишком короткое ({resampled_duration_sec:.2f}s < 0.3s), Google может отказать")
            if resampled_duration_sec > 60:
                logger.warning(f"⚠️ [AVF] Аудио слишком длинное ({resampled_duration_sec:.2f}s > 60s), Google может отказать")
            if audio_rms_resampled < 50:
                logger.warning(f"⚠️ [AVF] RMS очень низкий ({audio_rms_resampled:.2f} < 50), возможно тишина")
            if abs(mean_val) > 1000:
                logger.warning(f"⚠️ [AVF] Mean смещён ({mean_val:.1f}), возможно DC offset")
            if max_val - min_val < 100:
                logger.warning(f"⚠️ [AVF] Диапазон очень мал ({max_val:.1f} - {min_val:.1f} = {max_val - min_val:.1f}), возможно тишина")
            
            # Создаём AudioData для speech_recognition
            # ✅ КРИТИЧНО: sample_width=2 (int16), но нужно убедиться что channels=1 (моно)
            audio_data_obj = sr.AudioData(audio_bytes_int16, sample_rate, 2)  # sample_width=2 (int16), mono
            
            logger.info(f"🎤 [AVF] Начинаем распознавание: {len(audio_bytes_int16)} bytes, {sample_rate}Hz, mono")
            
            # Распознаём речь
            try:
                # ✅ ДИАГНОСТИКА: Удаляем дублирующие логи (уже выведены выше)
                
                logger.debug(f"🔍 [AVF] Вызываем recognize_google с language='{language}'...")
                import time
                start_time = time.time()
                
                # ✅ ИСПРАВЛЕНИЕ: Добавляем таймаут для recognize_google
                try:
                    # ✅ ДИАГНОСТИКА: Проверяем доступность интернета перед вызовом
                    try:
                        import urllib.request
                        urllib.request.urlopen('https://www.google.com', timeout=2)
                        logger.debug(f"🔍 [AVF] Интернет доступен, вызываем Google Speech API...")
                    except Exception as net_error:
                        logger.warning(f"⚠️ [AVF] Проблема с интернетом: {net_error}. Google Speech API может быть недоступен.")
                    
                    # ✅ ДИАГНОСТИКА: Используем show_all=True для получения детальной информации об ошибке
                    try:
                        # Пробуем сначала с show_all=False (обычный режим)
                        text = recognizer.recognize_google(audio_data_obj, language=language, show_all=False)
                    except Exception as first_error:
                        # Если ошибка, пробуем с show_all=True для получения детальной информации
                        logger.debug(f"🔍 [AVF] Первая попытка failed, пробуем show_all=True для диагностики...")
                        try:
                            result = recognizer.recognize_google(audio_data_obj, language=language, show_all=True)
                            logger.debug(f"🔍 [AVF] show_all=True результат: {result}")
                            # Если show_all=True вернул результат, извлекаем текст
                            if isinstance(result, dict) and 'alternative' in result:
                                if len(result['alternative']) > 0:
                                    text = result['alternative'][0].get('transcript', '')
                                    logger.info(f"✅ [AVF] Распознавание успешно (show_all=True): '{text}'")
                                else:
                                    raise first_error  # Нет альтернатив, пробрасываем исходную ошибку
                            else:
                                raise first_error  # Неожиданный формат, пробрасываем исходную ошибку
                        except Exception:
                            # Если и show_all=True не помог, пробрасываем исходную ошибку
                            raise first_error
                    elapsed_time = time.time() - start_time
                    logger.info(f"✅ [AVF] Распознавание успешно за {elapsed_time:.2f}s: '{text[:100]}...' (session={session_id})")
                except Exception as api_error:
                    elapsed_time = time.time() - start_time
                    error_type = type(api_error).__name__
                    error_msg = str(api_error) if str(api_error) else repr(api_error)
                    logger.error(f"❌ [AVF] Ошибка при вызове recognize_google (заняло {elapsed_time:.2f}s): {error_type}: {error_msg}", exc_info=True)
                    
                    # ✅ ДИАГНОСТИКА: Дополнительная информация об ошибке
                    if error_type == "RequestError":
                        logger.error(f"   💡 Это может быть проблема с сетью или доступностью Google Speech API")
                        logger.error(f"   💡 Проверьте интернет-соединение и доступность https://speech.googleapis.com")
                    elif error_type == "UnknownValueError":
                        logger.warning(f"   💡 Google Speech API не смог распознать речь (возможно тишина или неразборчивая речь)")
                        logger.warning(f"   💡 Проверьте:")
                        logger.warning(f"      - RMS resampled: {audio_rms_resampled:.2f} (должно быть > 100)")
                        logger.warning(f"      - Duration: {resampled_duration_sec:.2f}s (должно быть 0.3-60s)")
                        logger.warning(f"      - Range: [{min_val:.1f}, {max_val:.1f}] (должен быть широкий диапазон)")
                        logger.warning(f"      - WAV файл: /tmp/nexy_debug_session_*.wav (прослушайте для проверки)")
                    else:
                        logger.error(f"   💡 Неожиданная ошибка типа {error_type}")
                    
                    raise  # Пробрасываем дальше для обработки в except блоках
                
                # Публикуем результат
                await self.event_bus.publish("voice.recognition_completed", {
                    "session_id": session_id,
                    "text": text,
                    "confidence": None,  # SpeechRecognition (Google Speech API) не всегда предоставляет confidence
                    "language": language,
                    "source": "avf_recognition"
                })
                
            except sr.UnknownValueError:
                # ✅ ДИАГНОСТИКА: Улучшенное логирование для UnknownValueError
                # ✅ ИСПРАВЛЕНИЕ: Используем исходный sample_rate для duration
                resampled_duration_sec = len(audio_bytes_int16) / (sample_rate * 2)
                audio_rms_original = np.sqrt(np.mean(audio_array_int16.astype(np.float32) ** 2))
                audio_rms_resampled = np.sqrt(np.mean((np.frombuffer(audio_bytes_int16, dtype=np.int16).astype(np.float32)) ** 2))
                
                logger.warning(f"⚠️ [AVF] SpeechRecognition не распознал аудио (session={session_id})")
                logger.warning(f"🔍 [AVF] Детальная диагностика:")
                logger.warning(f"   - audio_size={len(audio_bytes_int16)} bytes")
                logger.warning(f"   - sample_rate (original)={original_sample_rate}Hz")
                logger.warning(f"   - sample_rate (resampled)={sample_rate}Hz")
                logger.warning(f"   - language={language}")
                logger.warning(f"   - duration (original)={original_duration_sec:.2f}s")
                logger.warning(f"   - duration (resampled)={resampled_duration_sec:.2f}s")
                logger.warning(f"   - RMS (original)={audio_rms_original:.2f}")
                logger.warning(f"   - RMS (resampled)={audio_rms_resampled:.2f}")
                
                # Возможные причины
                if original_duration_sec < 0.5:
                    logger.warning(f"   ⚠️ Возможная причина: аудио слишком короткое ({original_duration_sec:.2f}s)")
                if audio_rms_resampled < 100:
                    logger.warning(f"   ⚠️ Возможная причина: тишина (RMS={audio_rms_resampled:.2f} < 100)")
                if audio_rms_resampled > 10000:
                    logger.warning(f"   ⚠️ Возможная причина: перегрузка/искажение (RMS={audio_rms_resampled:.2f} > 10000)")
                
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": "Speech not recognized",
                    "source": "avf_recognition"
                })
            except sr.RequestError as e:
                logger.error(f"❌ [AVF] Ошибка сервиса распознавания (session={session_id}): {e}")
                logger.error(f"   Это может быть проблема с сетью или доступностью Google Speech API")
                await self.event_bus.publish("voice.recognition_failed", {
                    "session_id": session_id,
                    "error": str(e),
                    "source": "avf_recognition"
                })
                
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка распознавания аудио: {e}", exc_info=True)
            await self.event_bus.publish("voice.recognition_failed", {
                "session_id": session_id,
                "error": str(e),
                "source": "avf_recognition"
            })

    # ⚠️ Обработчики событий MicrophoneStateManager удалены (Этап 1)
    # Эти события больше не публикуются, так как MicrophoneStateManager удалён
    
    async def _on_microphone_open_requested(self, event: Dict[str, Any]):
        """Обработчик запроса открытия микрофона (временная заглушка - MicrophoneStateManager удалён)"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            timeout = data.get("timeout", 5.0)
            
            logger.debug(f"🎤 [MIC_STATE] Запрос открытия микрофона для session {session_id}")
            
            # ✅ ДИАГНОСТИКА: Логируем условия для понимания, почему start_listening() не вызывается
            logger.info(f"🔍 [MIC_STATE] Условия для start_listening: simulate={self.config.simulate}, _recognizer={self._recognizer is not None}, use_avf={self._use_avf}")
            
            # ✅ AVFoundation аудиосистема (Этап 3)
            if self._use_avf and self._avf_engine is not None:
                # Используем AVFAudioEngine для открытия микрофона
                try:
                    async def audio_callback(data: bytes, sample_rate: int, channels: int):
                        """Callback для получения аудио данных из AVFAudioEngine"""
                        if self._recognizer and hasattr(self._recognizer, '_process_audio_chunk'):
                            try:
                                await self._recognizer._process_audio_chunk(data, sample_rate, channels)
                            except Exception as e:
                                logger.debug(f"⚠️ [AVF] Ошибка обработки чанка в recognizer: {e}")
                    
                    success = await self._avf_engine.start_input(callback=audio_callback)
                    if success:
                        await self.event_bus.publish("microphone.opened", {"session_id": session_id})
                        logger.info(f"✅ [AVF] Микрофон открыт через AVFAudioEngine для session {session_id}")
                    else:
                        logger.error(f"❌ [AVF] Ошибка открытия микрофона через AVFAudioEngine")
                        return
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка открытия микрофона через AVFAudioEngine: {e}", exc_info=True)
                    return
            # Открываем микрофон через SpeechRecognizer (legacy)
            elif not self.config.simulate and self._recognizer is not None:
                # КРИТИЧНО: Проверяем состояние перед запуском для предотвращения двойного старта
                # Используем is_listening как основной индикатор активности
                is_listening = getattr(self._recognizer, 'is_listening', False)
                recognizer_state = getattr(self._recognizer, 'state', None)
                # Также проверяем физическое состояние потока
                stream_active = False
                if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                    try:
                        stream_active = self._recognizer._current_stream.active
                    except Exception:
                        pass
                
                if is_listening or stream_active or (recognizer_state and str(recognizer_state).upper() in ['LISTENING', 'RECOGNITIONSTATE.LISTENING']):
                    logger.warning(f"⚠️ [MIC_STATE] Уже в режиме прослушивания (is_listening={is_listening}, stream_active={stream_active}, state={recognizer_state}), пропускаем start для session {session_id}")
                    # Публикуем событие успешного открытия (микрофон уже открыт)
                    await self.event_bus.publish("microphone.opened", {"session_id": session_id})
                    logger.info(f"✅ [MIC_STATE] Микрофон уже открыт для session {session_id}")
                    return
                
                try:
                    logger.info(f"🎤 [MIC_STATE] Вызываем start_listening() для session {session_id}")
                    await self._recognizer.start_listening()
                    logger.info(f"✅ [MIC_STATE] start_listening() завершен успешно для session {session_id}")
                    # Публикуем событие успешного открытия
                    await self.event_bus.publish("microphone.opened", {"session_id": session_id})
                    logger.info(f"✅ [MIC_STATE] Микрофон успешно открыт для session {session_id}")
                except Exception as e:
                    error_str = str(e)
                    is_already_running = "there already is a thread" in error_str.lower()
                    
                    if is_already_running:
                        logger.warning(f"⚠️ [MIC_STATE] CoreAudio thread already running, микрофон уже активен для session {session_id}")
                        # Публикуем событие успешного открытия (микрофон уже работает)
                        await self.event_bus.publish("microphone.opened", {"session_id": session_id})
                        logger.info(f"✅ [MIC_STATE] Микрофон уже активен для session {session_id}")
                    else:
                        logger.error(f"❌ [MIC_STATE] Ошибка открытия микрофона: {e}")
                        # Публикуем событие ошибки
                        await self.event_bus.publish("microphone.error", {
                            "session_id": session_id,
                            "error": str(e)
                        })
            else:
                # Симуляция или recognizer не инициализирован - сразу публикуем успешное открытие
                reason = "simulation" if self.config.simulate else "recognizer_not_initialized"
                logger.warning(f"⚠️ [MIC_STATE] Пропуск start_listening() для session {session_id} (reason: {reason})")
                await self.event_bus.publish("microphone.opened", {"session_id": session_id})
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.open_requested: {e}")
    
    async def _on_microphone_close_requested(self, event: Dict[str, Any]):
        """Обработчик запроса закрытия микрофона (временная заглушка - MicrophoneStateManager удалён)"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            force = data.get("force", False)
            
            logger.debug(f"🎤 [MIC_STATE] Запрос закрытия микрофона для session {session_id} (force={force})")
            
            # ✅ AVFoundation аудиосистема (Этап 3)
            if self._use_avf and self._avf_engine is not None:
                # Используем AVFAudioEngine для закрытия микрофона
                try:
                    result = await self._avf_engine.stop_input()
                    if result:
                        logger.info(f"✅ [AVF] Микрофон закрыт через AVFAudioEngine: {result.frames_recorded} frames")
                    await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                    logger.info(f"✅ [AVF] Микрофон успешно закрыт для session {session_id}")
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка закрытия микрофона через AVFAudioEngine: {e}", exc_info=True)
                    # Все равно публикуем событие закрытия
                    await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                return
            
            # Закрываем микрофон через SpeechRecognizer (legacy)
            if not self.config.simulate and self._recognizer is not None:
                try:
                    await self._recognizer.stop_listening()
                    # Публикуем событие успешного закрытия
                    await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                    logger.info(f"✅ [MIC_STATE] Микрофон успешно закрыт для session {session_id}")
                except Exception as e:
                    logger.error(f"❌ [MIC_STATE] Ошибка закрытия микрофона: {e}")
                    # Все равно публикуем закрытие (принудительное)
                    await self.event_bus.publish("microphone.closed", {"session_id": session_id})
            else:
                # Симуляция - сразу публикуем успешное закрытие
                await self.event_bus.publish("microphone.closed", {"session_id": session_id})
        except Exception as e:
            logger.error(f"❌ [MIC_STATE] Ошибка обработки microphone.close_requested: {e}")
    
    # Отмена/прерывание
    async def _on_cancel_request(self, event: Dict[str, Any]):
        try:
            logger.debug("VOICE: cancel requested")
            await self._cancel_recognition(reason="cancel_requested")
            # Останавливаем реальное прослушивание, если активно
            if not self.config.simulate and self._recognizer is not None:
                try:
                    await self._recognizer.cancel_listening()  # будет no-op если не реализовано
                except Exception:
                    # Если в классе нет cancel_listening, игнорируем
                    pass
            # Сбрасываем текущую сессию целиком
            # КРИТИЧНО: Используем _set_session_id для синхронизации с state_manager
            self._set_session_id(None, reason="cancel_requested")
            self._recording_active = False
        except Exception as e:
            logger.error(f"VOICE: error in cancel handler: {e}")

    async def _on_playback_started(self, event: Dict[str, Any]):
        """КРИТИЧНО: Принудительно останавливаем микрофон при начале воспроизведения"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            logger.info(f"🔊 [VOICE] playback.started получено, проверяем состояние микрофона (session={session_id})")
            
            # #region agent log
            import json
            import time
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "voice_recognition_integration.py:2626", "message": "_on_playback_started ENTRY", "data": {"playback_session_id": session_id, "recording_active": self._recording_active, "mic_active": self.state_manager.is_microphone_active(), "google_mic_active": hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            
            # ✅ КРИТИЧНО: Проверяем состояние Google микрофона
            google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
            legacy_mic_active = self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening
            state_mic_active = self.state_manager.is_microphone_active()
            
            # ✅ КРИТИЧНО: Дополнительная проверка физического состояния PyAudio потока через speech_recognition
            # PyAudio может продолжать держать микрофон открытым, даже если мы думаем, что остановили его
            pyaudio_mic_active = False
            if hasattr(self, '_google_microphone') and self._google_microphone is not None:
                try:
                    import speech_recognition as sr
                    # Проверяем, не открыт ли микрофон через PyAudio
                    # speech_recognition использует PyAudio внутри, и микрофон может оставаться открытым
                    if hasattr(self._google_microphone, 'device_index'):
                        # Если микрофон имеет device_index, значит он был инициализирован
                        # Но это не гарантирует, что поток активен
                        # Проверяем через _google_stop_listening - если он не None, значит listen_in_background еще работает
                        pyaudio_mic_active = google_mic_active
                except Exception as e:
                    logger.debug(f"🔍 [VOICE] Ошибка проверки PyAudio потока: {e}")
            
            # #region agent log
            import json
            import time
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "voice_recognition_integration.py:2417", "message": "_on_playback_started called", "data": {"playback_session_id": session_id, "google_mic_active": google_mic_active, "legacy_mic_active": legacy_mic_active, "state_mic_active": state_mic_active, "pyaudio_mic_active": pyaudio_mic_active, "recording_active": self._recording_active}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            
            # ✅ КРИТИЧНО: Устанавливаем флаг воспроизведения ПЕРЕД остановкой микрофона
            # Это гарантирует, что callback'и будут игнорировать аудио во время воспроизведения
            # НО: если микрофон был активирован пользователем (_user_initiated_recording=True), callback все равно будет обрабатывать аудио для прерывания
            self._playback_active = True
            logger.info(f"🔊 [VOICE] Флаг воспроизведения установлен: _playback_active=True (session={session_id})")
            
            # ✅ КРИТИЧНО: ВСЕГДА принудительно сбрасываем флаг активности Google записи при начале воспроизведения
            # НО: только если микрофон НЕ был активирован пользователем (для автоматической активации)
            # Если микрофон был активирован пользователем, разрешаем обработку для прерывания воспроизведения
            if hasattr(self, '_google_recording_active'):
                # ✅ КРИТИЧНО: Если микрофон был активирован пользователем, НЕ сбрасываем флаг активности
                # Это позволяет callback обрабатывать аудио для прерывания воспроизведения
                if hasattr(self, '_user_initiated_recording') and self._user_initiated_recording:
                    logger.info(f"✅ [VOICE] Микрофон активирован пользователем - разрешаем обработку аудио для прерывания воспроизведения (session={session_id})")
                else:
                    if self._google_recording_active:
                        logger.warning(f"⚠️ [VOICE] _google_recording_active=True во время воспроизведения (session={session_id}) - принудительно сбрасываем флаг (автоматическая активация)")
                    # ✅ КРИТИЧНО: ВСЕГДА сбрасываем флаг для автоматической активации
                    # Это гарантирует, что callback'и не будут обрабатываться во время воспроизведения
                    self._google_recording_active = False
            
            # ✅ КРИТИЧНО: ВСЕГДА принудительно останавливаем Google микрофон при начале воспроизведения
            # Это гарантирует, что даже если PyAudio продолжает держать микрофон открытым, мы не обрабатываем callback'и
            # Проверяем, не остался ли микрофон "залипшим" после предыдущей записи
            if hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None:
                try:
                    logger.warning(f"⚠️ [VOICE] _google_stop_listening не None во время воспроизведения (session={session_id}) - принудительно останавливаем")
                    self._google_recording_active = False
                    await asyncio.sleep(0.1)
                    self._google_stop_listening(wait_for_stop=False)
                    logger.info(f"✅ [VOICE] _google_stop_listening вызван при начале воспроизведения (session={session_id})")
                except Exception as e:
                    logger.error(f"❌ [VOICE] Ошибка остановки _google_stop_listening при начале воспроизведения: {e}", exc_info=True)
                finally:
                    # ✅ КРИТИЧНО: ВСЕГДА очищаем состояние, даже при ошибке
                    self._google_stop_listening = None
                    self._google_recognizer = None
                    self._google_microphone = None
                    with self._google_audio_chunks_lock:
                        self._google_audio_chunks = []
                    self._google_recording_active = False
            elif hasattr(self, '_google_microphone') and self._google_microphone is not None:
                # Если микрофон был инициализирован, но _google_stop_listening is None, значит микрофон мог остаться открытым
                logger.warning(f"⚠️ [VOICE] _google_microphone не None, но _google_stop_listening is None во время воспроизведения (session={session_id}) - принудительно очищаем состояние")
                self._google_microphone = None
                self._google_recognizer = None
                with self._google_audio_chunks_lock:
                    self._google_audio_chunks = []
                self._google_recording_active = False
            
            # ✅ КРИТИЧНО: Если микрофон активен во время воспроизведения - это ошибка, принудительно останавливаем
            # Проверяем все возможные источники активности микрофона
            if google_mic_active or legacy_mic_active or state_mic_active or pyaudio_mic_active:
                logger.warning(f"⚠️ [VOICE] Микрофон активен во время воспроизведения (google={google_mic_active}, legacy={legacy_mic_active}, state={state_mic_active}, pyaudio={pyaudio_mic_active}) - принудительно останавливаем")
                
                # Останавливаем Google микрофон, если активен
                if google_mic_active or pyaudio_mic_active:
                    try:
                        logger.info("🛑 [Google] Принудительная остановка Google микрофона (playback.started)")
                        self._google_recording_active = False
                        await asyncio.sleep(0.1)
                        if self._google_stop_listening is not None:
                            self._google_stop_listening(wait_for_stop=False)
                            logger.info("✅ [Google] _google_stop_listening вызван (playback.started)")
                        else:
                            logger.warning("⚠️ [Google] _google_stop_listening is None, но микрофон активен - принудительно очищаем состояние")
                        # ✅ КРИТИЧНО: Очищаем состояние даже если _google_stop_listening is None
                        # Это гарантирует, что микрофон не останется "залипшим"
                        self._google_stop_listening = None
                        self._google_recognizer = None
                        # ✅ КРИТИЧНО: Закрываем микрофон через speech_recognition, если он открыт
                        if hasattr(self, '_google_microphone') and self._google_microphone is not None:
                            try:
                                # speech_recognition.Microphone не имеет явного метода close()
                                # Но мы можем попытаться очистить ссылку
                                logger.debug("🔍 [Google] Очищаем ссылку на микрофон")
                            except Exception as e:
                                logger.debug(f"🔍 [Google] Ошибка очистки микрофона: {e}")
                        self._google_microphone = None
                        with self._google_audio_chunks_lock:
                            self._google_audio_chunks = []
                        logger.info("✅ [Google] Google микрофон принудительно остановлен (playback.started)")
                    except Exception as e:
                        logger.error(f"❌ [Google] Ошибка принудительной остановки Google микрофона (playback.started): {e}", exc_info=True)
                        self._google_recording_active = False
                        # ✅ КРИТИЧНО: Даже при ошибке очищаем состояние
                        self._google_stop_listening = None
                        self._google_recognizer = None
                        self._google_microphone = None
                
                # Останавливаем legacy микрофон, если активен
                if legacy_mic_active:
                    try:
                        if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                            with getattr(self._recognizer, '_stream_lock', threading.RLock()):
                                if self._recognizer._current_stream and self._recognizer._current_stream.active:
                                    logger.warning("🛑 [VOICE] Принудительная остановка потока (playback.started)")
                                    self._recognizer._current_stream.stop()
                                    logger.info("✅ [VOICE] Поток остановлен принудительно (playback.started)")
                        await self._recognizer.stop_listening()
                        logger.info("✅ [VOICE] Legacy микрофон принудительно остановлен (playback.started)")
                    except Exception as e:
                        logger.error(f"❌ [VOICE] Ошибка принудительной остановки legacy микрофона (playback.started): {e}")
                
                # Синхронизируем состояние
                if state_mic_active:
                    self.state_manager.force_close_microphone(reason="playback_started")
                    await self.event_bus.publish("microphone.closed", {"session_id": session_id})
                    logger.info("✅ [VOICE] Состояние микрофона синхронизировано (playback.started)")
                
                self._recording_active = False
            else:
                logger.debug(f"✅ [VOICE] Микрофон не активен во время воспроизведения (session={session_id})")
        except Exception as e:
            logger.error(f"❌ [VOICE] Ошибка обработки playback.started: {e}", exc_info=True)
    
    async def _on_playback_finished(self, event: Dict[str, Any]):
        """Сбрасываем флаг воспроизведения при завершении воспроизведения"""
        try:
            data = (event or {}).get("data", {})
            session_id = data.get("session_id")
            event_type = event.get("type") if isinstance(event, dict) else None
            logger.info(f"🔊 [VOICE] playback.finished получено ({event_type}), сбрасываем флаг воспроизведения (session={session_id})")
            
            # ✅ КРИТИЧНО: Сбрасываем флаг воспроизведения
            self._playback_active = False
            # ✅ КРИТИЧНО: НЕ сбрасываем флаг пользовательской активации при завершении воспроизведения
            # Это позволяет пользователю активировать микрофон после завершения воспроизведения
            # Флаг будет сброшен только при остановке записи или при новом начале воспроизведения
            # if hasattr(self, '_user_initiated_recording') and self._user_initiated_recording:
            #     logger.info(f"✅ [VOICE] Микрофон активирован пользователем - сохраняем флаг _user_initiated_recording=True (session={session_id})")
            # else:
            #     self._user_initiated_recording = False
            logger.info(f"✅ [VOICE] Флаг воспроизведения сброшен: _playback_active=False (session={session_id})")
        except Exception as e:
            logger.error(f"❌ [VOICE] Ошибка обработки playback.finished: {e}", exc_info=True)

    async def _on_app_mode_changed(self, event: Dict[str, Any]):
        """Страховка: при выходе из LISTENING закрываем любое активное прослушивание"""
        try:
            data = (event or {}).get("data", {})
            new_mode = data.get("mode")
            # #region agent log
            import json
            import time
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "C", "location": "voice_recognition_integration.py:2394", "message": "_on_app_mode_changed called", "data": {"new_mode": str(new_mode), "recording_active": self._recording_active, "mic_active": self.state_manager.is_microphone_active(), "google_mic_active": hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            # #region agent log
            import json
            try:
                with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "voice_recognition_integration.py:2762", "message": "_on_app_mode_changed checking mode", "data": {"new_mode": str(new_mode), "recording_active": self._recording_active, "mic_active": self.state_manager.is_microphone_active(), "google_mic_active": hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None, "should_close_mic": new_mode in (AppMode.SLEEPING, AppMode.PROCESSING)}, "timestamp": int(time.time() * 1000)}) + "\n")
            except: pass
            # #endregion
            
            if new_mode in (AppMode.SLEEPING, AppMode.PROCESSING):
                # ✅ КРИТИЧНО: Закрываем распознавание/прослушивание, если вдруг активно
                # Это предотвращает "залипание" микрофона при переходе в PROCESSING
                # #region agent log
                try:
                    google_mic_active_before = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "A", "location": "voice_recognition_integration.py:2787", "message": "_on_app_mode_changed closing mic (PROCESSING/SLEEPING)", "data": {"new_mode": str(new_mode), "recording_active": self._recording_active, "mic_active": self.state_manager.is_microphone_active(), "google_mic_active_before": google_mic_active_before}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                
                # ✅ КРИТИЧНО: Принудительно останавливаем Google микрофон при переходе в PROCESSING/SLEEPING
                # Это предотвращает автоматическую активацию микрофона во время воспроизведения ответа ассистента
                google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
                if google_mic_active:
                    logger.warning(f"⚠️ [VOICE] Google микрофон активен при переходе в {new_mode} - принудительно останавливаем (предотвращение залипания)")
                    try:
                        # ✅ КРИТИЧНО: Сначала сбрасываем флаг активности, чтобы callback'и не обрабатывались
                        self._google_recording_active = False
                        # ✅ КРИТИЧНО: Небольшая задержка для завершения текущих callback'ов
                        await asyncio.sleep(0.1)
                        # ✅ КРИТИЧНО: Останавливаем listen_in_background
                        self._google_stop_listening(wait_for_stop=False)
                        logger.info(f"✅ [VOICE] Google микрофон принудительно остановлен (переход в {new_mode})")
                        # Очищаем состояние
                        self._google_stop_listening = None
                        self._google_recognizer = None
                        self._google_microphone = None
                        with self._google_audio_chunks_lock:
                            self._google_audio_chunks = []
                        # ✅ КРИТИЧНО: Синхронизируем состояние микрофона
                        if self.state_manager.is_microphone_active():
                            self.state_manager.force_close_microphone(reason=f"mode_changed_to_{new_mode.value}")
                            await self.event_bus.publish("microphone.closed", {"session_id": None})
                    except Exception as e:
                        logger.error(f"❌ [VOICE] Ошибка принудительной остановки Google микрофона (переход в {new_mode}): {e}", exc_info=True)
                        # ✅ КРИТИЧНО: Даже при ошибке сбрасываем флаг активности
                        self._google_recording_active = False
                        self._google_stop_listening = None
                        self._google_recognizer = None
                        self._google_microphone = None
                        # ✅ КРИТИЧНО: Принудительно синхронизируем состояние при ошибке
                        if self.state_manager.is_microphone_active():
                            self.state_manager.force_close_microphone(reason=f"mode_changed_error_{new_mode.value}")
                            await self.event_bus.publish("microphone.closed", {"session_id": None})
                
                await self._cancel_recognition(reason="mode_changed")
                if not self.config.simulate and self._recognizer is not None:
                    # Пытаемся мягко отменить прослушивание (если есть такой метод)
                    try:
                        await self._recognizer.cancel_listening()
                    except Exception:
                        # Если cancel_listening недоступен — оставляем закрытие на stop_listening при release
                        pass
            elif new_mode == AppMode.LISTENING:
                # #region agent log
                try:
                    with open('/Users/sergiyzasorin/Development/Nexy/Fix/client/.cursor/debug.log', 'a') as f:
                        f.write(json.dumps({"sessionId": "debug-session", "runId": "run1", "hypothesisId": "F", "location": "voice_recognition_integration.py:2775", "message": "_on_app_mode_changed LISTENING mode - checking if mic should activate", "data": {"new_mode": str(new_mode), "recording_active": self._recording_active, "mic_active": self.state_manager.is_microphone_active(), "google_mic_active": hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None, "should_NOT_activate_automatically": True}, "timestamp": int(time.time() * 1000)}) + "\n")
                except: pass
                # #endregion
                # ✅ КРИТИЧНО: При переходе в LISTENING микрофон НЕ должен активироваться автоматически
                # Микрофон активируется ТОЛЬКО при публикации voice.recording_start (из LONG_PRESS)
                # Если микрофон не активен, значит voice.recording_start еще не был опубликован
                if not self.state_manager.is_microphone_active():
                    logger.debug(f"🔍 [VOICE] Переход в LISTENING, но микрофон не активен - это нормально, микрофон активируется только при voice.recording_start")
                else:
                    logger.warning(f"⚠️ [VOICE] Переход в LISTENING, но микрофон уже активен - это может быть проблемой, если voice.recording_start не был опубликован")
        except Exception as e:
            logger.debug(f"VOICE: mode_changed guard failed: {e}")

    async def _on_first_run_started(self, event: Dict[str, Any]):
        """Обработчик начала процедуры first_run - блокируем активацию"""
        try:
            self._first_run_in_progress = True
            logger.info(
                "🔒 [VOICE_RECOGNITION] First run начат - блокировка активации микрофона"
            )
            # Отменяем любую текущую запись/распознавание
            await self._cancel_recognition(reason="first_run_started")
            if self._recording_active:
                self._recording_active = False
                logger.info("   Остановлена активная запись (если была)")
        except Exception as e:
            logger.error(f"❌ [VOICE_RECOGNITION] Ошибка обработки first_run_started: {e}")

    async def _on_first_run_completed(self, event: Dict[str, Any]):
        """Обработчик завершения/ошибки процедуры first_run - разблокируем активацию"""
        try:
            self._first_run_in_progress = False
            logger.info(
                "🔓 [VOICE_RECOGNITION] First run завершён - разблокировка активации микрофона"
            )
        except Exception as e:
            logger.error(f"❌ [VOICE_RECOGNITION] Ошибка обработки first_run_completed: {e}")

    async def _start_recognition(self, session_id: float):
        # Публикуем старт распознавания
        await self.event_bus.publish("voice.recognition_started", {
            "session_id": session_id,
            "language": self.config.language
        })

        # Запускаем задачу распознавания (симуляция/реал)
        async def _recognize():
            try:
                # Таймаут всей операции
                timeout = self.config.timeout_sec

                async def _simulate_work():
                    # Имитируем задержку от 1 до 3 секунд
                    delay = random.uniform(self.config.simulate_min_delay_sec, self.config.simulate_max_delay_sec)
                    await asyncio.sleep(delay)
                    # Имитируем успех/неуспех
                    if random.random() <= self.config.simulate_success_rate:
                        text = "открой браузер"
                        confidence = round(random.uniform(0.75, 0.98), 2)
                        await self.event_bus.publish("voice.recognition_completed", {
                            "session_id": session_id,
                            "text": text,
                            "confidence": confidence,
                            "language": self.config.language
                        })
                    else:
                        await self.event_bus.publish("voice.recognition_failed", {
                            "session_id": session_id,
                            "error": "no_speech",
                            "reason": "silence_or_noise"
                        })
                        # Не переводим режим здесь — финализацию режима делает воспроизведение
                        # (SpeechPlaybackIntegration по playback.completed/failed)

                if self.config.simulate:
                    await asyncio.wait_for(_simulate_work(), timeout=timeout)
                else:
                    # Здесь будет реальная интеграция с движком SR
                    await asyncio.wait_for(_simulate_work(), timeout=timeout)

            except asyncio.TimeoutError:
                await self.event_bus.publish("voice.recognition_timeout", {
                    "session_id": session_id,
                    "timeout_sec": self.config.timeout_sec
                })
                # Не переводим режим здесь — финализация режима делает воспроизведение
            except asyncio.CancelledError:
                # Отмена — ничего не публикуем, считается корректной отменой
                raise
            except Exception as e:
                # Неожиданная ошибка распознавания
                if hasattr(self.error_handler, 'handle_error'):
                    await self.error_handler.handle_error(
                        severity="warning",
                        category="voice",
                        message=f"Ошибка распознавания: {e}",
                        context={"where": "voice.recognize"}
                    )
                else:
                    logger.error(f"VOICE: recognition unexpected error: {e}")

        # Отменяем предыдущую задачу, если есть
        await self._cancel_recognition(reason="new_recognition")

        # Создаём и сохраняем новую
        loop = asyncio.get_running_loop()
        self._recognition_task = loop.create_task(_recognize())

    async def _cancel_recognition(self, reason: str = ""):
        """Отменяет распознавание и принудительно останавливает Google микрофон"""
        # Отменяем задачу распознавания
        task = self._recognition_task
        if task and not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                logger.debug(f"VOICE: recognition cancelled ({reason})")
        self._recognition_task = None
        
        # ✅ КРИТИЧНО: Принудительно останавливаем Google микрофон при отмене распознавания
        # Это предотвращает "залипание" микрофона, когда callback от listen_in_background продолжает работать
        google_mic_active = hasattr(self, '_google_stop_listening') and self._google_stop_listening is not None
        if google_mic_active:
            logger.warning(f"⚠️ [VOICE] Google микрофон активен при отмене распознавания (reason={reason}) - принудительно останавливаем")
            try:
                # ✅ КРИТИЧНО: Сначала сбрасываем флаг активности, чтобы callback'и не обрабатывались
                self._google_recording_active = False
                # ✅ КРИТИЧНО: Небольшая задержка для завершения текущих callback'ов
                await asyncio.sleep(0.1)
                # ✅ КРИТИЧНО: Останавливаем listen_in_background
                self._google_stop_listening(wait_for_stop=False)
                logger.info(f"✅ [VOICE] Google микрофон принудительно остановлен (reason={reason})")
                # Очищаем состояние
                self._google_stop_listening = None
                self._google_recognizer = None
                self._google_microphone = None
                with self._google_audio_chunks_lock:
                    self._google_audio_chunks = []
                # ✅ КРИТИЧНО: Синхронизируем состояние микрофона
                if self.state_manager.is_microphone_active():
                    self.state_manager.force_close_microphone(reason=f"cancel_recognition_{reason}")
                    await self.event_bus.publish("microphone.closed", {"session_id": None})
            except Exception as e:
                logger.error(f"❌ [VOICE] Ошибка принудительной остановки Google микрофона (reason={reason}): {e}", exc_info=True)
                # ✅ КРИТИЧНО: Даже при ошибке сбрасываем флаг активности
                self._google_recording_active = False
                self._google_stop_listening = None
                self._google_recognizer = None
                self._google_microphone = None
                # ✅ КРИТИЧНО: Принудительно синхронизируем состояние при ошибке
                if self.state_manager.is_microphone_active():
                    self.state_manager.force_close_microphone(reason=f"cancel_recognition_error_{reason}")
                    await self.event_bus.publish("microphone.closed", {"session_id": None})

    def get_status(self) -> Dict[str, Any]:
        # КРИТИЧНО: Используем _get_active_session_id для получения session_id (единый источник истины)
        active_session_id = self._get_active_session_id()
        return {
            "initialized": self._initialized,
            "running": self._running,
            "session_id": active_session_id,
            "recording": self._recording_active,
            "recognizing": self._recognition_task is not None and not self._recognition_task.done(),
            "config": {
                "timeout_sec": self.config.timeout_sec,
                "simulate": self.config.simulate,
                "language": self.config.language,
            }
        }
    
    async def _check_microphone_permissions(self):
        """Проверить разрешения микрофона (получаем от macOS)"""
        try:
            # macOS самостоятельно управляет разрешениями и активным устройством.
            # Здесь просто фиксируем, что проверка выполнена, без дополнительных запросов.
            logger.debug("🔍 Microphone permission check relies on macOS defaults")
            return True
        except Exception as e:
            logger.info(f"ℹ️ Microphone permission check failed: {e}")
            # В случае ошибки/отказа доступа — мягко переходим в симуляцию
            self.config.simulate = True
            logger.info("🔄 Switching to simulation mode due to microphone probe failure")
            return False

    @classmethod
    def run_dependency_check(cls) -> bool:
        """Статический метод для проверки зависимостей распознавания речи"""
        try:
            logger.info("🔍 Проверяем зависимости распознавания речи...")
            
            # Проверяем доступность SpeechRecognizer
            if _REAL_VOICE_AVAILABLE:
                logger.info("✅ SpeechRecognizer доступен")
                try:
                    from modules.voice_recognition import SpeechRecognizer, DEFAULT_RECOGNITION_CONFIG
                    # Пытаемся создать экземпляр для проверки
                    recognizer = SpeechRecognizer(DEFAULT_RECOGNITION_CONFIG)
                    logger.info("✅ SpeechRecognizer успешно инициализирован")
                    return True
                except Exception as e:
                    logger.warning(f"⚠️ SpeechRecognizer не удалось инициализировать: {e}")
                    logger.info("ℹ️ Будет использоваться режим симуляции")
                    return True  # Возвращаем True, так как симуляция всегда доступна
            else:
                logger.warning("⚠️ SpeechRecognizer недоступен")
                logger.info("ℹ️ Будет использоваться режим симуляции")
                return True  # Возвращаем True, так как симуляция всегда доступна
                
        except Exception as e:
            logger.error(f"❌ Ошибка при проверке зависимостей: {e}")
            return False
