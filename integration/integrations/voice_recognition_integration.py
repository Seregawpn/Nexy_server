"""
VoiceRecognitionIntegration - координация распознавания речи
Концептуальная реализация с симуляцией результата для UX-потока
"""

import asyncio
import logging
import threading
from dataclasses import dataclass
from typing import Optional, Dict, Any
import random
import importlib.util
from shutil import which

from integration.core.event_bus import EventBus, EventPriority
from integration.core.state_manager import ApplicationStateManager, AppMode
from integration.core.error_handler import ErrorHandler
from config.unified_config_loader import UnifiedConfigLoader
# ✅ ЭТАП 2: Импорт MicrophoneStateManager
from modules.microphone_state import MicrophoneStateManager

logger = logging.getLogger(__name__)

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

        # Флаг блокировки во время first_run
        self._first_run_in_progress: bool = False
        # Конфигурируемая задержка между попытками запуска микрофона
        try:
            voice_cfg = UnifiedConfigLoader().get("voice") or {}
            self._start_retry_delay_sec = max(0.0, float(voice_cfg.get("start_retry_delay_ms", 300)) / 1000.0)
        except Exception:
            self._start_retry_delay_sec = 0.3
        
        # ✅ ЭТАП 2: Инициализация MicrophoneStateManager
        self._mic_state_manager: Optional[MicrophoneStateManager] = None

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
            # ✅ ЭТАП 2: Инициализация MicrophoneStateManager (КРИТИЧНО: должен быть инициализирован)
            try:
                self._mic_state_manager = MicrophoneStateManager(
                    event_bus=self.event_bus,
                    state_manager=self.state_manager,  # Для обратной совместимости (односторонняя синхронизация)
                    open_timeout=5.0,
                    close_timeout=3.0
                )
                mic_init_result = await self._mic_state_manager.initialize()
                if not mic_init_result:
                    logger.error("❌ VOICE: Не удалось инициализировать MicrophoneStateManager")
                    raise RuntimeError("MicrophoneStateManager initialization failed")
                logger.info("✅ MicrophoneStateManager инициализирован в VoiceRecognitionIntegration")
            except Exception as e:
                logger.error(f"❌ VOICE: КРИТИЧЕСКАЯ ОШИБКА инициализации MicrophoneStateManager: {e}")
                raise  # Пробрасываем ошибку - без MicrophoneStateManager интеграция не может работать
            
            # ✅ ЭТАП 2: Подписка на события запросов открытия/закрытия микрофона
            await self.event_bus.subscribe("microphone.open_requested", self._on_microphone_open_requested, EventPriority.HIGH)
            await self.event_bus.subscribe("microphone.close_requested", self._on_microphone_close_requested, EventPriority.HIGH)
            
            # Подписки на события записи/прерывания
            await self.event_bus.subscribe("voice.recording_start", self._on_recording_start, EventPriority.HIGH)
            await self.event_bus.subscribe("voice.recording_stop", self._on_recording_stop, EventPriority.HIGH)
            await self.event_bus.subscribe("keyboard.short_press", self._on_cancel_request, EventPriority.CRITICAL)
            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration
            # Гарантированно закрываем прослушивание при выходе из LISTENING
            await self.event_bus.subscribe("app.mode_changed", self._on_app_mode_changed, EventPriority.MEDIUM)

            # КРИТИЧНО: Подписываемся на события first_run для блокировки активации
            await self.event_bus.subscribe("permissions.first_run_started", self._on_first_run_started, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_completed", self._on_first_run_completed, EventPriority.CRITICAL)
            await self.event_bus.subscribe("permissions.first_run_failed", self._on_first_run_completed, EventPriority.CRITICAL)

            # Инициализация реального распознавателя, если симуляция отключена
            logger.info(f"🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}")
            print(f"🔍 [AUDIO_DEBUG] Условия создания SpeechRecognizer: simulate={self.config.simulate}, _REAL_VOICE_AVAILABLE={_REAL_VOICE_AVAILABLE}")
            if not self.config.simulate and _REAL_VOICE_AVAILABLE:
                try:
                    logger.info("🔍 [AUDIO_DEBUG] Создание SpeechRecognizer...")
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
    
    def _get_active_session_id(self) -> Optional[float]:
        """
        Получить активный session_id из state_manager (единый источник истины).
        
        Returns:
            Активный session_id или None (конвертируется в float для совместимости)
        """
        # Используем state_manager как единый источник истины
        session_id = self.state_manager.get_current_session_id()
        if session_id is not None:
            # Конвертируем в float для совместимости (state_manager хранит строки)
            try:
                return float(session_id)
            except (ValueError, TypeError):
                return None
        return None
    
    def _set_session_id(self, session_id: Optional[float], reason: str = "unknown"):
        """
        Установить session_id в state_manager (единый источник истины).
        
        КРИТИЧНО: Используем state_manager как единственный источник истины.
        Локальная переменная _current_session_id удалена - все через state_manager.
        
        Args:
            session_id: Session ID для установки (может быть float или None)
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
            # КРИТИЧНО: Проверяем first_run перед началом записи
            if self._first_run_in_progress:
                logger.warning(
                    "⚠️ [VOICE_RECOGNITION] Блокировка активации - first_run в процессе. "
                    "Запись микрофона во время запроса разрешений запрещена."
                )
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
            # Любое предыдущие распознавание отменяем
            await self._cancel_recognition(reason="new_recording_start")
            logger.debug(f"VOICE: recording_start, session={session_id}")

            # ✅ ЭТАП 2: Используем MicrophoneStateManager для запроса открытия микрофона
            # КРИТИЧНО: MicrophoneStateManager должен быть инициализирован (нет fallback для предотвращения дублирования)
            if not self._mic_state_manager:
                logger.error("❌ VOICE: MicrophoneStateManager не инициализирован - невозможно открыть микрофон")
                self._recording_active = False
                self._set_session_id(None, reason="mic_state_manager_not_initialized")
                return
            
            opened = await self._mic_state_manager.request_open(str(session_id))
            if not opened:
                logger.error(f"❌ VOICE: Не удалось открыть микрофон для session {session_id}")
                self._recording_active = False
                self._set_session_id(None, reason="mic_open_failed")
                return

            # ✅ КРИТИЧНО: request_open() публикует microphone.open_requested, который обрабатывается
            # _on_microphone_open_requested и вызывает start_listening() + публикует microphone.opened
            # НЕ вызываем start_listening() здесь повторно, чтобы избежать дублирования!
            # voice.mic_opened будет опубликовано MicrophoneStateManager после получения microphone.opened
            logger.debug(f"🎤 VOICE: запрос открытия микрофона отправлен через MicrophoneStateManager для session {session_id}")
            
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
            
            # Поддерживаем оба формата: прямой и вложенный
            if "data" in event:
                data = event.get("data", {})
            else:
                data = event
            session_id = data.get("session_id")
            logger.info(f"🛑 VOICE: recording_stop, session={session_id} (type: {type(session_id)})")

            # Останавливаем запись — запускаем распознавание для этой сессии
            # КРИТИЧНО: Используем _get_active_session_id для получения session_id (единый источник истины)
            active_session_id = self._get_active_session_id()
            logger.info(f"🛑 VOICE: active_session_id={active_session_id} (type: {type(active_session_id)}), request_session_id={session_id} (type: {type(session_id)})")
            
            # ✅ ЭТАП 1: Если session_id is None, но микрофон активен - принудительно останавливаем микрофон
            # Это может произойти при SHORT_PRESS после LONG_PRESS, когда микрофон уже открыт, но сессия была отменена
            if session_id is None:
                if self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening:
                    logger.warning("⚠️ VOICE: recording_stop с session_id=None, но микрофон активен - принудительно останавливаем микрофон")
                    # Принудительно останавливаем микрофон
                    try:
                        await self._recognizer.stop_listening()
                        logger.info("✅ VOICE: микрофон принудительно остановлен (session_id=None)")
                    except Exception as e:
                        logger.error(f"❌ VOICE: ошибка принудительной остановки микрофона: {e}")
                    # ✅ ЭТАП 2: Используем MicrophoneStateManager для принудительного закрытия
                    if self._mic_state_manager:
                        await self._mic_state_manager.force_close(reason="recording_stop_no_session")
                    else:
                        # Fallback только в критической ситуации (микрофон залип, но MicrophoneStateManager не инициализирован)
                        logger.error("❌ VOICE: MicrophoneStateManager не инициализирован при принудительном закрытии")
                        self.state_manager.force_close_microphone(reason="recording_stop_no_session_fallback")
                    # ✅ ЭТАП 3: voice.mic_closed будет опубликовано MicrophoneStateManager
                    # после получения microphone.closed или при принудительном закрытии
                    logger.debug("🎤 VOICE: ожидание закрытия микрофона (принудительная остановка)")
                    self._recording_active = False
                else:
                    logger.debug("VOICE: recording_stop с session_id=None, микрофон не активен - игнорируем")
                    # ✅ ЭТАП 2: Убеждаемся, что состояние микрофона синхронизировано через MicrophoneStateManager
                    if self._mic_state_manager and self._mic_state_manager.is_active():
                        logger.warning("⚠️ VOICE: MicrophoneStateManager показывает активный микрофон, но recognizer не активен - синхронизируем состояние")
                        await self._mic_state_manager.force_close(reason="state_mismatch")
                    elif self.state_manager.is_microphone_active():
                        # Fallback только если MicrophoneStateManager не инициализирован
                        logger.warning("⚠️ VOICE: state_manager показывает активный микрофон, но recognizer не активен - синхронизируем состояние (fallback)")
                        self.state_manager.force_close_microphone(reason="state_mismatch_fallback")
                return
            
            # ✅ КРИТИЧНО: Сравнение session_id с учетом типов (float vs str)
            # Конвертируем оба в строки для корректного сравнения
            active_session_str = str(active_session_id) if active_session_id is not None else None
            request_session_str = str(session_id) if session_id is not None else None
            
            logger.info(f"🛑 VOICE: Сравнение session_id: active='{active_session_str}' vs request='{request_session_str}'")
            
            if active_session_str != request_session_str:
                # Не наша сессия — игнорируем
                logger.warning(f"⚠️ VOICE: recording_stop ignored (session mismatch: active={active_session_str}, request={request_session_str})")
                # ✅ КРИТИЧНО: Даже при mismatch принудительно останавливаем поток, если микрофон активен
                if self._recognizer is not None and hasattr(self._recognizer, 'is_listening') and self._recognizer.is_listening:
                    logger.warning("⚠️ VOICE: Session mismatch, но микрофон активен - принудительно останавливаем поток")
                    try:
                        if hasattr(self._recognizer, '_current_stream') and self._recognizer._current_stream:
                            with getattr(self._recognizer, '_stream_lock', threading.RLock()):
                                if self._recognizer._current_stream and self._recognizer._current_stream.active:
                                    logger.warning("🛑 VOICE: Принудительная остановка потока (session mismatch)")
                                    self._recognizer._current_stream.stop()
                                    logger.info("✅ VOICE: Поток остановлен принудительно (session mismatch)")
                    except Exception as e:
                        logger.error(f"❌ VOICE: Ошибка принудительной остановки потока (session mismatch): {e}")
                return

            self._recording_active = False
            
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
                            logger.info("✅ VOICE: microphone.closed опубликовано СРАЗУ после остановки потока (разрыв deadlock)")
                        except Exception as e:
                            logger.error(f"❌ VOICE: Ошибка принудительной остановки потока (проверка физического состояния): {e}")
            
            # ✅ ЭТАП 2: Используем MicrophoneStateManager для запроса закрытия микрофона
            # КРИТИЧНО: Если поток уже остановлен и microphone.closed уже опубликовано,
            # request_close должен завершиться быстро (событие уже обработано)
            logger.info(f"🛑 VOICE: Вызов request_close: mic_state_manager={self._mic_state_manager is not None}, stream_was_active={stream_was_active}")
            if not self._mic_state_manager:
                logger.error("❌ VOICE: MicrophoneStateManager не инициализирован - принудительно закрываем через state_manager")
                # КРИТИЧНО: В случае ошибки инициализации используем прямой вызов для предотвращения залипания
                self.state_manager.force_close_microphone(reason="mic_state_manager_not_initialized")
            else:
                try:
                    # ✅ КРИТИЧНО: Если поток уже остановлен и microphone.closed уже опубликовано,
                    # request_close должен завершиться быстро (событие уже обработано в _on_microphone_closed)
                    # Используем короткий таймаут для request_close, чтобы не блокировать stop_listening
                    close_timeout = 0.5 if stream_was_active else 3.0  # Очень короткий таймаут если поток уже остановлен
                    await asyncio.wait_for(
                        self._mic_state_manager.request_close(str(session_id) if session_id else None, force=(session_id is None)),
                        timeout=close_timeout
                    )
                    logger.info("✅ VOICE: request_close завершен успешно")
                except asyncio.TimeoutError:
                    logger.warning(f"⚠️ VOICE: Таймаут request_close ({close_timeout}s) - продолжаем без ожидания (микрофон уже закрыт)")
                    # Fallback: принудительно закрываем через state_manager
                    # Но это не критично, так как поток уже остановлен
                    self.state_manager.force_close_microphone(reason="mic_state_manager_request_close_timeout")
                except Exception as e:
                    logger.error(f"❌ VOICE: Ошибка request_close: {e}", exc_info=True)
                    # Fallback: принудительно закрываем через state_manager
                    self.state_manager.force_close_microphone(reason="mic_state_manager_request_close_failed")

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

    # ✅ ЭТАП 2: Обработчики событий MicrophoneStateManager
    
    async def _on_microphone_open_requested(self, event: Dict[str, Any]):
        """Обработчик запроса открытия микрофона от MicrophoneStateManager"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            timeout = data.get("timeout", 5.0)
            
            logger.debug(f"🎤 [MIC_STATE] Запрос открытия микрофона для session {session_id}")
            
            # ✅ ДИАГНОСТИКА: Логируем условия для понимания, почему start_listening() не вызывается
            logger.info(f"🔍 [MIC_STATE] Условия для start_listening: simulate={self.config.simulate}, _recognizer={self._recognizer is not None}")
            
            # Открываем микрофон через SpeechRecognizer
            if not self.config.simulate and self._recognizer is not None:
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
        """Обработчик запроса закрытия микрофона от MicrophoneStateManager"""
        try:
            data = event.get("data", {}) or event
            session_id = data.get("session_id")
            force = data.get("force", False)
            
            logger.debug(f"🎤 [MIC_STATE] Запрос закрытия микрофона для session {session_id} (force={force})")
            
            # Закрываем микрофон через SpeechRecognizer
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

    async def _on_app_mode_changed(self, event: Dict[str, Any]):
        """Страховка: при выходе из LISTENING закрываем любое активное прослушивание"""
        try:
            data = (event or {}).get("data", {})
            new_mode = data.get("mode")
            if new_mode in (AppMode.SLEEPING, AppMode.PROCESSING):
                # Закрываем распознавание/прослушивание, если вдруг активно
                await self._cancel_recognition(reason="mode_changed")
                if not self.config.simulate and self._recognizer is not None:
                    # Пытаемся мягко отменить прослушивание (если есть такой метод)
                    try:
                        await self._recognizer.cancel_listening()
                    except Exception:
                        # Если cancel_listening недоступен — оставляем закрытие на stop_listening при release
                        pass
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
        task = self._recognition_task
        if task and not task.done():
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                logger.debug(f"VOICE: recognition cancelled ({reason})")
        self._recognition_task = None

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
