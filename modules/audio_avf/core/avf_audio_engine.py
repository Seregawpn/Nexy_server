"""
AVFoundation Audio Engine

Нативная аудиосистема на основе AVFoundation для macOS.
Обеспечивает надёжную работу с Bluetooth устройствами без ошибок -9986/-10851.
"""

import asyncio
import logging
import threading
import time
import ctypes
import weakref
from typing import Optional, Callable, Any, List
from collections import deque
import objc

from config.audio_config import AudioConfig, AudioInputConfig, AudioOutputConfig
from .types import AudioState, AudioFormat, AudioInputResult, AudioDeviceInfo

logger = logging.getLogger(__name__)

# ✅ КРИТИЧНО: Импортируем AVAudioPlayerNode на модульном уровне для использования в objc.callbackFor
# objc.callbackFor требует чтобы класс был доступен на момент вызова декоратора
try:
    logger.info("🔧 [AVF] Попытка импорта AVAudioPlayerNode из AVFoundation...")
    from AVFoundation import AVAudioPlayerNode
    AVF_PLAYER_NODE_AVAILABLE = True
    logger.info("✅ [AVF] AVAudioPlayerNode успешно импортирован из AVFoundation")
    logger.info(f"✅ [AVF] AVAudioPlayerNode тип: {type(AVAudioPlayerNode)}")
except ImportError as e:
    AVAudioPlayerNode = None
    AVF_PLAYER_NODE_AVAILABLE = False
    logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: Не удалось импортировать AVAudioPlayerNode из AVFoundation")
    logger.exception("❌ [AVF] Детали ImportError при импорте AVAudioPlayerNode")
    logger.error(f"❌ [AVF] Сообщение: {e}")
    logger.error("❌ [AVF] Completion callbacks НЕ БУДУТ работать без AVAudioPlayerNode")
    logger.error("❌ [AVF] Установите PyObjC: pip install pyobjc-framework-AVFoundation")
except Exception as e:
    AVAudioPlayerNode = None
    AVF_PLAYER_NODE_AVAILABLE = False
    logger.error(f"❌ [AVF] Неожиданная ошибка при импорте AVAudioPlayerNode: {e}")
    logger.exception("❌ [AVF] Детали исключения при импорте AVAudioPlayerNode")

# ✅ КРИТИЧНО: Статический completion callback на уровне модуля
# Создаётся один раз для всех экземпляров, использует слабую ссылку на экземпляр
# Это исключает постоянное переопределение и гарантирует, что PyObjC видит правильный блок
_AVF_COMPLETION_CALLBACK = None

# ✅ КРИТИЧНО: Глобальный словарь для хранения экземпляров AVFAudioEngine
# Используется в статическом callback для доступа к экземпляру
_AVF_ENGINE_INSTANCES = weakref.WeakValueDictionary()

# ✅ КРИТИЧНО: Отображение player_node → engine для привязки callback к конкретному движку
# Используется для точной идентификации экземпляра в completion callback
_PLAYER_NODE_TO_ENGINE = weakref.WeakKeyDictionary()
# Некоторые PyObjC-обёртки (например, AVAudioPlayerNode) не поддерживают weakref,
# поэтому используем дополнительный словарь по id объекта.
_PLAYER_NODE_ID_MAP = {}


def _bind_player_node_to_engine(player_node, engine_instance):
    """Связать player_node с engine_instance, учитывая отсутствие weakref."""
    global _PLAYER_NODE_TO_ENGINE, _PLAYER_NODE_ID_MAP
    if player_node is None or engine_instance is None:
        return

    try:
        # Очистка старой записи на случай повторной привязки
        if player_node in _PLAYER_NODE_TO_ENGINE:
            del _PLAYER_NODE_TO_ENGINE[player_node]
        _PLAYER_NODE_TO_ENGINE[player_node] = engine_instance
        logger.debug("✅ [AVF] Player node привязан к engine через WeakKeyDictionary")
        return
    except TypeError:
        # AVAudioPlayerNode не поддерживает weakref, используем fallback
        player_id = id(player_node)

        def _cleanup(ref, pid=player_id):
            _PLAYER_NODE_ID_MAP.pop(pid, None)

        _PLAYER_NODE_ID_MAP[player_id] = weakref.ref(engine_instance, _cleanup)
        logger.debug("✅ [AVF] Player node привязан к engine через ID fallback")


def _lookup_engine_by_player_node(player_node):
    """Вернуть engine по player_node с учётом fallback словаря.
    
    ⚠️ ВАЖНО: AVAudioPlayerNode не поддерживает weakref, поэтому сначала проверяем
    fallback словарь _PLAYER_NODE_ID_MAP, а не _PLAYER_NODE_TO_ENGINE.
    """
    if player_node is None:
        return None

    # ✅ КРИТИЧНО: Сначала проверяем fallback словарь (AVAudioPlayerNode не поддерживает weakref)
    player_id = id(player_node)
    engine_ref = _PLAYER_NODE_ID_MAP.get(player_id)
    if engine_ref is not None:
        engine_instance = engine_ref()
        if engine_instance is not None:
            return engine_instance

    # Fallback на weakref словарь (может не работать для AVAudioPlayerNode)
    try:
        engine_instance = _PLAYER_NODE_TO_ENGINE.get(player_node)
        if engine_instance is not None:
            return engine_instance
    except TypeError:
        # AVAudioPlayerNode не поддерживает weakref - это нормально
        pass
    
    return None

def _create_avf_completion_callback():
    """Создать статический completion callback для AVAudioPlayerNode на уровне модуля
    
    ✅ КРИТИЧНО: Callback создаётся один раз при первом использовании,
    используется всеми экземплярами AVFAudioEngine. Использует слабую ссылку
    на экземпляр через глобальный словарь, чтобы избежать циклических ссылок.
    """
    global _AVF_COMPLETION_CALLBACK
    
    logger.info("🔧 [AVF] _create_avf_completion_callback() вызван")
    
    if _AVF_COMPLETION_CALLBACK is not None:
        logger.info("✅ [AVF] Используется существующий статический completion callback")
        return _AVF_COMPLETION_CALLBACK
    
    # ✅ КРИТИЧНО: Проверяем доступность AVAudioPlayerNode перед созданием callback
    logger.debug(f"🔍 [AVF] Проверка доступности: AVF_PLAYER_NODE_AVAILABLE = {AVF_PLAYER_NODE_AVAILABLE}")
    logger.debug(f"🔍 [AVF] Проверка доступности: AVAudioPlayerNode = {AVAudioPlayerNode}")
    
    if not AVF_PLAYER_NODE_AVAILABLE:
        logger.error("❌ [AVF] AVF_PLAYER_NODE_AVAILABLE = False, completion callback не будет создан")
        logger.error("❌ [AVF] Это означает, что импорт AVAudioPlayerNode из AVFoundation не удался при загрузке модуля")
        logger.error("❌ [AVF] Проверьте установку PyObjC: pip install pyobjc-framework-AVFoundation")
        return None
    
    if AVAudioPlayerNode is None:
        logger.error("❌ [AVF] AVAudioPlayerNode = None, completion callback не будет создан")
        logger.error("❌ [AVF] Это означает, что импорт AVAudioPlayerNode из AVFoundation не удался при загрузке модуля")
        logger.error("❌ [AVF] Проверьте установку PyObjC: pip install pyobjc-framework-AVFoundation")
        return None
    
    # ✅ КРИТИЧНО: Проверяем, что AVAudioPlayerNode действительно загружен PyObjC
    try:
        # Проверяем, что класс доступен и имеет нужный метод
        if not hasattr(AVAudioPlayerNode, 'scheduleBuffer_atTime_options_completionHandler_'):
            logger.error("❌ [AVF] AVAudioPlayerNode не имеет метода scheduleBuffer_atTime_options_completionHandler_")
            return None
        
        logger.debug(f"✅ [AVF] AVAudioPlayerNode доступен: {AVAudioPlayerNode}")
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка проверки AVAudioPlayerNode: {e}", exc_info=True)
        return None
    
    def playback_completion_handler_impl():
        """Callback от AVAudioPlayerNode при завершении воспроизведения буфера
        
        ✅ КРИТИЧНО: Вызывается из аудио потока. 
        ⚠️ ВАЖНО: Objective-C completion handler для scheduleBuffer_atTime_options_completionHandler_
        НЕ принимает параметров вообще! Это блок типа void (^)(void).
        
        Для идентификации экземпляра используем глобальный словарь активных воспроизведений
        или первый доступный экземпляр из _AVF_ENGINE_INSTANCES.
        """
        global _AVF_ENGINE_INSTANCES
        
        
        # ✅ КРИТИЧНО: Objective-C не передаёт player_node в completion handler
        # Используем первый доступный экземпляр из _AVF_ENGINE_INSTANCES
        # В большинстве случаев будет только один экземпляр
        engine_instance = None
        if _AVF_ENGINE_INSTANCES:
            # Получаем первый доступный экземпляр
            engine_instance = next(iter(_AVF_ENGINE_INSTANCES.values()), None)
            if engine_instance:
                logger.debug(f"🔍 [AVF] Completion callback: использован экземпляр из _AVF_ENGINE_INSTANCES")
        
        if engine_instance is None:
            logger.warning("⚠️ [AVF] Completion callback вызван, но экземпляр AVFAudioEngine не найден в _AVF_ENGINE_INSTANCES")
            return
        
        try:
            import time
            current_time = time.time()
            logger.info("✅ [AVF] Completion callback вызван (playback_completion_handler_impl)")
            
            with engine_instance._lock:
                # ✅ КРИТИЧНО: Проверяем состояние ПЕРЕД проверкой времени
                # Если состояние не RUNNING, это означает, что воспроизведение было прервано
                # (например, из-за AVAudioEngineConfigurationChangeNotification)
                # В этом случае игнорируем callback от старого буфера
                if engine_instance._output_state != AudioState.RUNNING:
                    logger.warning(
                        f"⚠️ [AVF] Completion callback игнорируется: состояние не RUNNING "
                        f"(текущее состояние: {engine_instance._output_state}). "
                        f"Возможно, это callback от прерванного буфера."
                    )
                    return
                logger.info(f"✅ [AVF] Completion callback: состояние RUNNING, продолжаем обработку")
                
                # ✅ КРИТИЧНО: Проверяем, что callback сработал в правильное время
                # Если callback сработал слишком рано (менее 80% ожидаемой длительности),
                # игнорируем его (возможно, это преждевременный вызов из PyObjC)
                if engine_instance._playback_start_time is not None and engine_instance._expected_playback_duration is not None:
                    elapsed_time = current_time - engine_instance._playback_start_time
                    expected_duration = engine_instance._expected_playback_duration
                    min_acceptable_duration = expected_duration * 0.8  # Минимум 80% от ожидаемой длительности
                    
                    if elapsed_time < min_acceptable_duration:
                        logger.warning(
                            f"⚠️ [AVF] Completion callback сработал ПРЕЖДЕВРЕМЕННО: "
                            f"прошло {elapsed_time:.2f}s из {expected_duration:.2f}s "
                            f"(минимум: {min_acceptable_duration:.2f}s). Игнорируем callback."
                        )
                        # ✅ КРИТИЧНО: Не обрабатываем преждевременный callback И не сбрасываем состояние
                        # Состояние должно остаться RUNNING, чтобы конфигурационные события
                        # не прерывали воспроизведение
                        logger.debug("🔍 [AVF] Состояние остаётся RUNNING после преждевременного callback")
                        return
                elif engine_instance._playback_start_time is None or engine_instance._expected_playback_duration is None:
                    # ✅ КРИТИЧНО: Если время начала или ожидаемая длительность не установлены,
                    # это означает, что воспроизведение было прервано и состояние сброшено
                    # Игнорируем callback от старого буфера
                    logger.debug(
                        f"🔍 [AVF] Completion callback игнорируется: время начала или ожидаемая длительность не установлены. "
                        f"Возможно, это callback от прерванного буфера."
                    )
                    return
                
                # ✅ КРИТИЧНО: Проверяем, что состояние всё ещё RUNNING (дополнительная проверка после проверки времени)
                # Это защита от race condition, когда состояние может измениться между проверками
                if engine_instance._output_state == AudioState.RUNNING:
                    # ✅ КРИТИЧНО: Обновляем счётчик проигранных сэмплов при завершении
                    engine_instance._samples_played = engine_instance._total_samples_in_buffer
                    engine_instance._output_state = AudioState.IDLE
                    
                    # Очищаем время начала воспроизведения
                    actual_duration = None
                    if engine_instance._playback_start_time is not None:
                        actual_duration = current_time - engine_instance._playback_start_time
                    engine_instance._playback_start_time = None
                    engine_instance._expected_playback_duration = None
                    
                    duration_str = f"{actual_duration:.2f}s" if actual_duration is not None else "N/A"
                    logger.info(
                        f"✅ [AVF] Воспроизведение завершено (callback от AVAudioPlayerNode, "
                        f"samples_played={engine_instance._samples_played}, duration={duration_str})"
                    )
                    
                    # ✅ УБРАНО: Отмена fallback таймера - таймеры больше не используются
                    
                    # ✅ ИСПРАВЛЕНИЕ: Проверяем is_running() перед публикацией события
                    async def _publish_completion():
                        if engine_instance._event_bus:
                            logger.info("✅ [AVF] Completion callback: публикуем audio.playback.completed")
                            await engine_instance._event_bus.publish("audio.playback.completed", {
                                "source": "AVF_PLAYER_NODE_CALLBACK",
                                "finished": True  # Всегда True, так как callback вызван
                            })
                            logger.info("✅ [AVF] Completion callback: audio.playback.completed опубликовано")
                    
                    # ✅ КРИТИЧНО: Используем централизованную проверку и прикрепление loop
                    if engine_instance._ensure_loop_attached():
                        engine_instance._submit_to_event_loop(_publish_completion(), is_async=True)
                    else:
                        # Loop недоступен - сохраняем в очередь
                        with engine_instance._pending_events_lock:
                            engine_instance._pending_events.append(("audio.playback.completed", {
                                "source": "AVF_PLAYER_NODE_CALLBACK",
                                "finished": True  # Всегда True, так как callback вызван
                            }))
                        logger.debug("🔄 [AVF] Completion событие сохранено в очередь (loop недоступен)")
                else:
                    logger.debug(f"🔍 [AVF] Playback completion callback получен, но состояние уже {engine_instance._output_state}")
                    # ✅ НОВОЕ: Увеличиваем счётчик пропущенных callback'ов для диагностики
                    engine_instance._missed_completion_callbacks += 1
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка в playback completion callback: {e}", exc_info=True)
    
    # ✅ КРИТИЧНО: Используем objc.callbackFor для явного указания сигнатуры блока
    # ⚠️ ВАЖНО: Сигнатура completion handler для scheduleBuffer_atTime_options_completionHandler_
    # это void (^)(void) = b"v" (НЕ принимает параметров вообще!)
    try:
        logger.info("🔧 [AVF] Создание completion callback через objc.callbackFor...")
        logger.debug(f"🔍 [AVF] AVAudioPlayerNode тип: {type(AVAudioPlayerNode)}")
        logger.debug(
            "🔍 [AVF] Метод scheduleBuffer_atTime_options_completionHandler_ доступен: %s",
            hasattr(AVAudioPlayerNode, 'scheduleBuffer_atTime_options_completionHandler_')
        )

        # ✅ КРИТИЧНО: AVAudioNodeCompletionHandler это void (^)(void), не принимает параметров
        # Пробуем несколько способов создания блока в PyObjC
        _AVF_COMPLETION_CALLBACK = None
        
        # Попытка 1: Передать функцию напрямую (PyObjC может автоматически преобразовать)
        try:
            # Просто сохраняем функцию - попробуем передать её напрямую в scheduleBuffer
            # PyObjC может автоматически преобразовать Python callable в Objective-C блок
            _AVF_COMPLETION_CALLBACK = playback_completion_handler_impl
            logger.info("✅ [AVF] Completion callback сохранён как Python функция (будет передан напрямую)")
        except Exception as direct_error:
            logger.warning(f"⚠️ [AVF] Не удалось сохранить функцию напрямую: {direct_error}")
            
            # Попытка 2: Использовать objc.callbackFor (может не работать с void (^)(void))
            try:
                callback_decorator = objc.callbackFor(
                    AVAudioPlayerNode.scheduleBuffer_atTime_options_completionHandler_
                )
                _AVF_COMPLETION_CALLBACK = callback_decorator(playback_completion_handler_impl)
                logger.info("✅ [AVF] Completion callback создан через objc.callbackFor")
            except Exception as callback_error:
                logger.warning(f"⚠️ [AVF] objc.callbackFor не сработал: {callback_error}")
                # Если все попытки провалились, используем None - полагаемся на fallback таймер
                logger.warning("⚠️ [AVF] Completion callback не создан, будет использован fallback таймер")
                _AVF_COMPLETION_CALLBACK = None

        if _AVF_COMPLETION_CALLBACK is None:
            logger.error("❌ [AVF] objc.callbackFor вернул None, completion callback не создан")
            logger.error("❌ [AVF] Это может быть из-за проблем с PyObjC или недоступности AVFoundation")
            return None
        
        logger.info("✅ [AVF] Статический completion callback успешно создан на уровне модуля")
        logger.info("✅ [AVF] Completion callback registered")
        return _AVF_COMPLETION_CALLBACK
        
    except ImportError as e:
        logger.exception("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: ImportError при создании completion callback")
        logger.error(f"❌ [AVF] Обычно это означает, что AVAudioPlayerNode не может быть импортирован из AVFoundation")
        logger.error(f"❌ [AVF] Проверьте установку PyObjC: pip install pyobjc-framework-AVFoundation")
        logger.error(f"❌ [AVF] Детали ImportError: {e}")
        _AVF_COMPLETION_CALLBACK = None
        return None
    except Exception as e:
        logger.exception("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: Не удалось создать completion callback через objc.callbackFor")
        logger.error(f"❌ [AVF] Тип исключения: {type(e).__name__}")
        logger.error(f"❌ [AVF] Детали ошибки: {e}")
        logger.error(f"❌ [AVF] AVAudioPlayerNode доступен: {AVAudioPlayerNode is not None}")
        logger.error(f"❌ [AVF] AVF_PLAYER_NODE_AVAILABLE: {AVF_PLAYER_NODE_AVAILABLE}")
        _AVF_COMPLETION_CALLBACK = None
        return None


class AVFAudioEngine:
    """
    AVFoundation Audio Engine
    
    Единый движок для записи и воспроизведения аудио через AVFoundation.
    Автоматически обрабатывает готовность устройств и формат конвертацию.
    """
    
    def __init__(self, config: Optional[AudioConfig] = None, event_bus: Optional[Any] = None):
        """
        Инициализация AVFAudioEngine
        
        Args:
            config: Конфигурация аудио (если None - загружается из unified_config)
            event_bus: EventBus для публикации событий смены устройств (опционально)
        """
        try:
            from AVFoundation import (
                AVAudioEngine,
                AVAudioPlayerNode,
                AVAudioPCMBuffer,
                AVAudioFormat,
                AVAudioCommonFormat,
            )
            from CoreAudio import (
                AudioObjectAddPropertyListener,
                AudioObjectRemovePropertyListener,
                kAudioHardwarePropertyDefaultOutputDevice,
                kAudioHardwarePropertyDefaultInputDevice,
            )
        except ImportError as e:
            logger.error(f"❌ [AVF] Не удалось импортировать AVFoundation: {e}")
            raise RuntimeError("AVFoundation недоступен. Установите PyObjC: pip install pyobjc-framework-AVFoundation")
        
        # Загружаем конфигурацию
        if config is None:
            try:
                from config.unified_config_loader import UnifiedConfigLoader
                loader = UnifiedConfigLoader()
                config = loader.get_audio_config_object()
            except Exception as e:
                logger.warning(f"⚠️ [AVF] Ошибка загрузки конфига, используем дефолты: {e}")
                config = AudioConfig.default()
        
        self.config = config
        self._event_bus = event_bus  # EventBus для публикации событий
        
        # ✅ КРИТИЧНО: Стабильный EventBus loop для безопасной публикации событий из фоновых потоков
        self._event_loop: Optional[asyncio.AbstractEventLoop] = None
        if event_bus and hasattr(event_bus, '_loop'):
            self._event_loop = event_bus._loop
        
        # ✅ НОВОЕ: Очередь событий для fallback (если loop недоступен)
        self._pending_events: List[tuple] = []  # [(event_type, payload), ...]
        self._pending_events_lock = threading.Lock()
        
        # ✅ НОВОЕ: Pending loop для отслеживания loop, который ещё не запущен
        self._pending_loop: Optional[asyncio.AbstractEventLoop] = None
        
        # AVAudioEngine (главный движок)
        self._engine: Optional[Any] = None
        self._input_node: Optional[Any] = None
        self._output_node: Optional[Any] = None
        self._player_node: Optional[Any] = None
        self._player_node_connected: bool = False  # Флаг подключения player node

        # Состояние
        self._input_state = AudioState.IDLE
        self._output_state = AudioState.IDLE
        self._lock = threading.RLock()
        
        # Данные записи
        self._recorded_audio: List[bytes] = []
        self._recording_start_time: Optional[float] = None
        self._input_format: Optional[AudioFormat] = None
        
        # ✅ КРИТИЧНО: Отслеживание времени начала воспроизведения для проверки преждевременного callback
        self._playback_start_time: Optional[float] = None  # Время начала воспроизведения
        self._expected_playback_duration: Optional[float] = None  # Ожидаемая длительность воспроизведения
        
        # Callbacks
        self._input_callback: Optional[Callable[[bytes, int, int], None]] = None
        self._input_callback_loop: Optional[asyncio.AbstractEventLoop] = None
        
        # ✅ УБРАНО: Fallback таймер - полагаемся ТОЛЬКО на completion callback
        
        # ✅ НОВОЕ: Инициализируем статический completion callback один раз
        # Callback создаётся в _init_completion_callback() и хранится в self._output_completion_callback
        self._output_completion_callback: Optional[Any] = None
        self._missed_completion_callbacks: int = 0  # Счётчик пропущенных callback'ов
        
        # ✅ НОВОЕ: Отслеживание проигранных сэмплов для точного расчёта остатка при возобновлении
        self._samples_played: int = 0  # Количество проигранных сэмплов (обновляется в play_audio и callback)
        self._total_samples_in_buffer: int = 0  # Общее количество сэмплов в текущем буфере
        
        # ✅ НОВОЕ: Мониторинг устройств
        self._cached_output_device_name: Optional[str] = None
        self._cached_input_device_name: Optional[str] = None
        self._output_listener_active: bool = False
        self._input_listener_active: bool = False
        self._output_listener_id: Optional[Any] = None
        self._input_listener_id: Optional[Any] = None
        
        # Инициализация
        engine_init_success = self._initialize_engine()
        
        # ✅ КРИТИЧНО: Инициализируем completion callback ПОСЛЕ создания player_node
        # Это необходимо для привязки player_node → engine в _PLAYER_NODE_TO_ENGINE
        # ⚠️ ВАЖНО: Проверяем, что _player_node создан перед инициализацией callback
        if engine_init_success and self._player_node is not None:
            self._init_completion_callback()
        else:
            logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: _player_node не создан, completion callback не будет инициализирован")
            logger.error("❌ [AVF] Это означает, что _initialize_engine() не удалась или _player_node = None")
            logger.error("❌ [AVF] Воспроизведение может не работать корректно")
            self._output_completion_callback = None
        
        # ✅ НОВОЕ: Настройка мониторинга устройств после инициализации engine
        self._setup_device_monitoring()
    
    def _initialize_engine(self) -> bool:
        """Инициализация AVAudioEngine (только для output)
        
        ⚠️ ВАЖНО: inputNode() НЕ инициализируется здесь!
        В macOS вызов inputNode() автоматически активирует индикатор микрофона.
        Input node инициализируется лениво в start_input().
        """
        try:
            from AVFoundation import AVAudioEngine, AVAudioPlayerNode
            
            self._engine = AVAudioEngine.alloc().init()
            # ⚠️ НЕ вызываем inputNode() здесь - это активирует микрофон!
            # self._input_node будет инициализирован в start_input()
            self._input_node = None  # Ленивая инициализация
            self._output_node = self._engine.outputNode()
            self._player_node = AVAudioPlayerNode.alloc().init()
            
            # Подключаем player node к engine
            self._engine.attachNode_(self._player_node)
            _bind_player_node_to_engine(self._player_node, self)
            
            # ✅ КРИТИЧНО: Подключаем player_node к output_node сразу при инициализации
            # Это безопаснее, чем делать это в play_audio(), и предотвращает segmentation fault
            try:
                output_format_avf = self._output_node.inputFormatForBus_(0)
                if output_format_avf is None:
                    logger.error("❌ [AVF] output_format_avf is None при инициализации")
                    self._player_node_connected = False
                else:
                    self._engine.connect_to_format_(
                        self._player_node,
                        self._output_node,
                        output_format_avf
                    )
                    self._player_node_connected = True
                    logger.info("✅ [AVF] Player node подключен к output node при инициализации")
            except Exception as e:
                logger.error(f"❌ [AVF] Ошибка подключения player node при инициализации: {e}", exc_info=True)
                self._player_node_connected = False
            
            logger.info("✅ [AVF] AVAudioEngine инициализирован (output only, input lazy)")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка инициализации engine: {e}", exc_info=True)
            return False
    
    def _setup_device_monitoring(self):
        """Настройка мониторинга устройств через Core Audio нотификации"""
        try:
            # Инициализируем кэш имен устройств
            self._cached_output_device_name = self._get_real_output_device_name()
            self._cached_input_device_name = self._get_real_input_device_name()
            
            # Настраиваем подписки на нотификации
            self._setup_core_audio_listeners()
            self._setup_configuration_change_notification()
            
            logger.info("✅ [AVF] Мониторинг устройств настроен")
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка настройки мониторинга устройств: {e}", exc_info=True)
    
    def _setup_configuration_change_notification(self):
        """Подписка на изменения конфигурации AVAudioEngine"""
        try:
            from Foundation import NSNotificationCenter
            
            # Создаем обертку для callback
            class NotificationObserver:
                def __init__(self, handler):
                    self.handler = handler
                
                def on_configuration_change_(self, notification):
                    """Обработчик изменения конфигурации engine"""
                    logger.info("🔔 [AVF] AVAudioEngineConfigurationChangeNotification получена")
                    # Обрабатываем смену устройства в отдельном потоке
                    threading.Thread(
                        target=self.handler,
                        daemon=True
                    ).start()
            
            observer = NotificationObserver(self._handle_device_change)
            
            # Подписываемся на нотификацию
            NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                observer,
                "on_configuration_change:",
                "AVAudioEngineConfigurationChangeNotification",
                self._engine
            )
            
            # Сохраняем observer для последующего удаления
            self._notification_observer = observer
            
            logger.info("✅ [AVF] Подписка на AVAudioEngineConfigurationChangeNotification активирована")
        except Exception as e:
            logger.warning(f"⚠️ [AVF] Не удалось подписаться на AVAudioEngineConfigurationChangeNotification: {e}")
    
    def _setup_core_audio_listeners(self):
        """Подписка на Core Audio нотификации о смене устройств"""
        try:
            from CoreAudio import (
                AudioObjectAddPropertyListener,
                kAudioObjectSystemObject,
                AudioObjectPropertyAddress,
                kAudioObjectPropertyScopeGlobal,
                kAudioObjectPropertyElementMain,
                kAudioHardwarePropertyDefaultOutputDevice,
                kAudioHardwarePropertyDefaultInputDevice,
            )
            
            # ✅ КРИТИЧНО: Используем objc.callbackFor для создания PyObjC closure
            # Сигнатура: OSStatus (*AudioObjectPropertyListenerProc)(
            #     AudioObjectID inObjectID,
            #     UInt32 inNumberAddresses,
            #     const AudioObjectPropertyAddress *inAddresses,
            #     void *inClientData
            # )
            # В PyObjC это: i@:I^^{AudioObjectPropertyAddress=IIII}@
            
            def output_device_changed_impl(
                inObjectID: int,
                inNumberAddresses: int,
                inAddresses: Any,
                inClientData: Any
            ) -> int:
                """Callback для смены OUTPUT устройства"""
                logger.info("🔔 [AVF] Core Audio: default OUTPUT устройство изменилось")
                # Вызываем обработчик в отдельном потоке
                threading.Thread(
                    target=self._handle_output_device_change,
                    daemon=True
                ).start()
                return 0  # kAudioObjectPropertyListenerSucceeded
            
            def input_device_changed_impl(
                inObjectID: int,
                inNumberAddresses: int,
                inAddresses: Any,
                inClientData: Any
            ) -> int:
                """Callback для смены INPUT устройства"""
                logger.info("🔔 [AVF] Core Audio: default INPUT устройство изменилось")
                threading.Thread(
                    target=self._handle_input_device_change,
                    daemon=True
                ).start()
                return 0  # kAudioObjectPropertyListenerSucceeded
            
            # ✅ КРИТИЧНО: Создаём PyObjC closure через objc.selector с правильной сигнатурой
            # Сигнатура AudioObjectPropertyListenerProc:
            # OSStatus (*AudioObjectPropertyListenerProc)(
            #     AudioObjectID inObjectID,           // I (UInt32)
            #     UInt32 inNumberAddresses,           // I (UInt32)
            #     const AudioObjectPropertyAddress *inAddresses,  // ^^{AudioObjectPropertyAddress=IIII}
            #     void *inClientData                   // @ (void*)
            # ) -> OSStatus                           // i (int)
            # В PyObjC для C callback'ов используется objc.selector с сигнатурой без @: (без self и selector)
            # Правильная сигнатура: iI^v@ где i=OSStatus, I=UInt32, ^v=pointer, @=void*
            try:
                # Используем objc.selector с правильной сигнатурой для C callback
                # Для C callback'ов сигнатура без @: (без self и selector)
                output_device_changed_callback = objc.selector(
                    output_device_changed_impl,
                    signature=b"iI^v@",  # OSStatus (AudioObjectID, UInt32, pointer, void*) - без @: для C callback
                    isAllocator=False
                )
                logger.debug("✅ [AVF] OUTPUT device callback создан через objc.selector")
            except Exception as callback_error:
                logger.warning(f"⚠️ [AVF] Не удалось создать OUTPUT callback через objc.selector: {callback_error}")
                # Fallback: пробуем использовать функцию напрямую (может не работать)
                logger.warning("⚠️ [AVF] Используем fallback: передаём функцию напрямую")
                output_device_changed_callback = output_device_changed_impl
            
            try:
                input_device_changed_callback = objc.selector(
                    input_device_changed_impl,
                    signature=b"iI^v@",  # OSStatus (AudioObjectID, UInt32, pointer, void*) - без @: для C callback
                    isAllocator=False
                )
                logger.debug("✅ [AVF] INPUT device callback создан через objc.selector")
            except Exception as callback_error:
                logger.warning(f"⚠️ [AVF] Не удалось создать INPUT callback через objc.selector: {callback_error}")
                # Fallback: пробуем использовать функцию напрямую (может не работать)
                logger.warning("⚠️ [AVF] Используем fallback: передаём функцию напрямую")
                input_device_changed_callback = input_device_changed_impl
            
            # Подписываемся на OUTPUT
            output_address = AudioObjectPropertyAddress(
                kAudioHardwarePropertyDefaultOutputDevice,
                kAudioObjectPropertyScopeGlobal,
                kAudioObjectPropertyElementMain
            )
            result = AudioObjectAddPropertyListener(
                kAudioObjectSystemObject,
                output_address,
                output_device_changed_callback,
                None
            )
            if result == 0:
                logger.info("✅ [AVF] Подписка на OUTPUT device changes активирована")
                self._output_listener_active = True
                self._output_listener_id = output_device_changed_callback
            else:
                logger.warning(f"⚠️ [AVF] Не удалось подписаться на OUTPUT device changes: {result}")
            
            # Подписываемся на INPUT
            input_address = AudioObjectPropertyAddress(
                kAudioHardwarePropertyDefaultInputDevice,
                kAudioObjectPropertyScopeGlobal,
                kAudioObjectPropertyElementMain
            )
            result = AudioObjectAddPropertyListener(
                kAudioObjectSystemObject,
                input_address,
                input_device_changed_callback,
                None
            )
            if result == 0:
                logger.info("✅ [AVF] Подписка на INPUT device changes активирована")
                self._input_listener_active = True
                self._input_listener_id = input_device_changed_callback
            else:
                logger.warning(f"⚠️ [AVF] Не удалось подписаться на INPUT device changes: {result}")
                
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка настройки Core Audio listeners: {e}", exc_info=True)
    
    def _handle_device_change(self):
        """Обработка общего изменения конфигурации (вызывается из AVAudioEngineConfigurationChangeNotification)"""
        # Проверяем оба устройства
        self._handle_output_device_change()
        if self.is_input_active:
            self._handle_input_device_change()
    
    def _handle_output_device_change(self):
        """Обработка смены OUTPUT устройства
        
        ✅ ИСПРАВЛЕНИЕ: Всегда переподключает player node при конфигурационном событии,
        даже если имя устройства не изменилось. Это необходимо для обработки
        AVAudioEngineConfigurationChangeNotification (например, переключение режимов AirPods).
        """
        try:
            logger.info("🔄 [AVF] Обработка смены OUTPUT устройства...")
            
            # Получаем новое имя устройства
            new_device_name = self._get_real_output_device_name()
            old_device_name = self._cached_output_device_name
            
            # ✅ КРИТИЧНО: Проверяем состояние перед переподключением
            was_output_active = self.is_output_active
            was_running = self._engine.isRunning() if self._engine else False
            
            device_name_changed = (new_device_name != old_device_name)
            
            if device_name_changed:
                logger.info(f"🔄 [AVF] Смена OUTPUT устройства: {old_device_name} → {new_device_name}")
                # Обновляем кэш
                self._cached_output_device_name = new_device_name
            else:
                logger.info(f"🔄 [AVF] Конфигурационное событие для OUTPUT устройства: {new_device_name} (имя не изменилось, но требуется переподключение)")
            
            # ✅ КРИТИЧНО: Захватываем lock для проверки состояния
            with self._lock:
                # Проверяем состояние под lock (защита от race condition)
                was_output_active_under_lock = (self._output_state == AudioState.RUNNING)
                current_state_under_lock = self._output_state
            
            # ✅ КРИТИЧНО: Если воспроизведение только началось (STARTING) или активно (RUNNING), не прерываем его
            # Конфигурационные события могут приходить сразу после начала воспроизведения
            # и прерывать его до того, как оно успевает начаться
            if current_state_under_lock == AudioState.STARTING:
                logger.debug("🔍 [AVF] Воспроизведение в состоянии STARTING, пропускаем переподключение (избегаем прерывания)")
                # Просто обновляем кэш имени устройства, но не переподключаем
                self._cached_output_device_name = new_device_name
                return
            
            # ✅ КРИТИЧНО: Если воспроизведение активно (RUNNING), не прерываем его
            # Это гарантирует полное воспроизведение без сокращений
            if current_state_under_lock == AudioState.RUNNING:
                logger.debug("🔍 [AVF] Воспроизведение активно (RUNNING), пропускаем переподключение (гарантируем полное воспроизведение)")
                # ✅ КРИТИЧНО: Проверяем, что engine всё ещё запущен
                # AVAudioEngine может автоматически останавливаться при конфигурационных событиях
                if self._engine and not self._engine.isRunning():
                    logger.warning("⚠️ [AVF] Engine остановлен системой во время воспроизведения")
                    # ✅ ИСПРАВЛЕНИЕ: Если engine остановлен системой, буфер уже потерян
                    # Публикуем событие о прерывании воспроизведения для обработки в speech_playback_integration
                    # Это позволит speech_playback_integration опубликовать playback.completed или попытаться возобновить воспроизведение
                    logger.warning("⚠️ [AVF] Буфер потерян из-за остановки engine системой, публикуем событие прерывания")
                    
                    # ✅ КРИТИЧНО: Сбрасываем состояние в IDLE ПЕРЕД публикацией события
                    # Это гарантирует, что любые преждевременные completion callbacks от старого буфера будут игнорированы
                    with self._lock:
                        # ✅ КРИТИЧНО: Сохраняем информацию о прерванном воспроизведении для правильного возобновления
                        interrupted_start_time = self._playback_start_time
                        interrupted_expected_duration = self._expected_playback_duration
                        
                        # Сбрасываем состояние в IDLE
                        self._output_state = AudioState.IDLE
                        # ✅ КРИТИЧНО: Очищаем время начала воспроизведения, чтобы игнорировать преждевременные callbacks
                        self._playback_start_time = None
                        self._expected_playback_duration = None
                        # ✅ КРИТИЧНО: Сбрасываем счётчики сэмплов для правильного расчёта остатка при возобновлении
                        self._samples_played = 0
                        self._total_samples_in_buffer = 0
                    
                    self._publish_event_safe("audio.playback.interrupted", {
                        "reason": "engine_stopped_by_system",
                        "device_name": new_device_name,
                        "source": "AVF_CONFIGURATION_CHANGE",
                        "interrupted_start_time": interrupted_start_time,
                        "interrupted_expected_duration": interrupted_expected_duration
                    })
                # Просто обновляем кэш имени устройства, но не переподключаем
                self._cached_output_device_name = new_device_name
                return
            
            # ✅ КРИТИЧНО: Сбрасываем флаг подключения только если воспроизведение не активно
            # Это предотвращает потерю буфера при переподключении во время воспроизведения
            with self._lock:
                self._player_node_connected = False
            
            # ✅ КРИТИЧНО: Всегда переподключаем player node, даже если имя устройства не изменилось
            # Это необходимо для обработки AVAudioEngineConfigurationChangeNotification,
            # когда AVAudioEngine автоматически останавливается (например, при переключении режимов AirPods)
            
            # Переподключаем player_node к output_node (полный cycle: stop → disconnect → connect → start)
            reconnect_success = self._reconnect_player_node()
            
            # ✅ КРИТИЧНО: Если playback был активен, публикуем событие о необходимости ресинхронизации
            # ✅ ИСПРАВЛЕНИЕ: Используем состояние под lock и _submit_to_event_loop
            if was_output_active_under_lock and reconnect_success:
                logger.warning("⚠️ [AVF] Воспроизведение было прервано конфигурационным событием, требуется ресинхронизация")
                self._publish_event_safe("audio.device.output_resync_required", {
                    "device_name": new_device_name,
                    "was_running": was_running,
                    "was_output_active": was_output_active_under_lock,
                    "source": "AVF_CONFIGURATION_CHANGE"
                })
            
            # Публикуем событие смены устройства (только если имя изменилось)
            if device_name_changed:
                self._publish_event_safe("audio.device.output_changed", {
                                "device_name": new_device_name,
                                "old_device_name": old_device_name,
                                "source": "AVF_CORE_AUDIO"
                })
        
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка обработки смены OUTPUT устройства: {e}", exc_info=True)
    
    def _handle_input_device_change(self):
        """Обработка смены INPUT устройства"""
        try:
            logger.info("🔄 [AVF] Обработка смены INPUT устройства...")
            
            # Получаем новое имя устройства
            new_device_name = self._get_real_input_device_name()
            old_device_name = self._cached_input_device_name
            
            if new_device_name == old_device_name:
                logger.debug(f"🔍 [AVF] INPUT устройство не изменилось: {new_device_name}")
                return
            
            logger.info(f"🔄 [AVF] Смена INPUT устройства: {old_device_name} → {new_device_name}")
            
            # Обновляем кэш
            self._cached_input_device_name = new_device_name
            
            # Если запись активна, нужно переподключить input_node
            if self.is_input_active:
                logger.warning("⚠️ [AVF] INPUT устройство изменилось во время записи, требуется перезапуск")
                # TODO: Реализовать переподключение input_node без остановки записи
                # Пока просто логируем предупреждение
            
            # Публикуем событие
            self._publish_event_safe("audio.device.input_changed", {
                                "device_name": new_device_name,
                                "old_device_name": old_device_name,
                                "source": "AVF_CORE_AUDIO"
            })
        
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка обработки смены INPUT устройства: {e}", exc_info=True)
    
    def _reconnect_player_node(self):
        """Переподключение player_node к output_node после смены устройства
        
        Выполняет полный cycle: stop → disconnect → connect_to_format_ → start
        Это необходимо для корректной обработки AVAudioEngineConfigurationChangeNotification.
        
        ✅ КРИТИЧНО: Все изменения состояния выполняются под lock для защиты от race conditions
        с play_audio() и stop_output(). Использует состояние RECONNECTING для предотвращения
        конфликтов во время переподключения.
        """
        try:
            # ✅ КРИТИЧНО: Захватываем lock на всём участке обновления состояния
            with self._lock:
                # Проверяем состояние перед переподключением
                was_running = self._engine.isRunning() if self._engine else False
                was_output_active = (self._output_state == AudioState.RUNNING)
                
                logger.info(f"🔄 [AVF] Переподключение player node: engine_running={was_running}, output_active={was_output_active}, state={self._output_state}")
                
                # ✅ НОВОЕ: Переводим в состояние RECONNECTING для предотвращения конфликтов
                if was_output_active or self._output_state == AudioState.RUNNING:
                    self._output_state = AudioState.RECONNECTING
                    logger.debug("✅ [AVF] _output_state переведён в RECONNECTING")
                
                # Если engine уже остановлен системой, но состояние было RUNNING - уже переведено в RECONNECTING
                if not was_running and was_output_active:
                    logger.warning("⚠️ [AVF] Engine остановлен системой, состояние переведено в RECONNECTING")
            
            # Шаг 1: Останавливаем engine если запущен (вне lock, так как это может быть долгая операция)
            if was_running:
                self._engine.stop()
                logger.debug("🛑 [AVF] Engine остановлен для переподключения")
            
            # Шаг 2: Отключаем старый player_node (если был подключен)
            if self._player_node_connected:
                try:
                    # Отключаем input output_node от player_node
                    self._engine.disconnectNodeInput_(self._output_node)
                    logger.debug("🔌 [AVF] Player node отключен от output node")
                except Exception as e:
                    logger.debug(f"🔍 [AVF] Ошибка отключения (может быть уже отключен): {e}")
            
            # Шаг 3: Получаем новый формат output_node
            output_format_avf = self._output_node.inputFormatForBus_(0)
            if output_format_avf is None:
                logger.error("❌ [AVF] output_format_avf is None при переподключении")
                return False
            
            # ✅ НОВОЕ: Логируем формат для диагностики
            output_sample_rate = int(output_format_avf.sampleRate())
            output_channels = int(output_format_avf.channelCount())
            logger.debug(f"🔍 [AVF] Output format: {output_sample_rate}Hz, {output_channels}ch")
            
            # Шаг 4: Подключаем заново
            self._engine.connect_to_format_(
                self._player_node,
                self._output_node,
                output_format_avf
            )
            
            # ✅ КРИТИЧНО: Обновляем состояние под lock
            with self._lock:
                self._player_node_connected = True
                # Если было RECONNECTING - возвращаем в IDLE (воспроизведение не было активно)
                # Если было RUNNING и мы его перевели в RECONNECTING - остаётся RECONNECTING до завершения
                if self._output_state == AudioState.RECONNECTING and not was_output_active:
                    self._output_state = AudioState.IDLE
                    logger.debug("✅ [AVF] _output_state возвращён в IDLE (воспроизведение не было активно)")
            
            logger.info("✅ [AVF] Player node переподключен к output node")
            
            # Шаг 5: Запускаем engine обратно если был запущен
            if was_running:
                self._engine.prepare()
                error_ref = objc.NULL
                success = self._engine.startAndReturnError_(error_ref)
                if success:
                    logger.info("✅ [AVF] Engine перезапущен после переподключения")
                    # ✅ КРИТИЧНО: Если было активное воспроизведение, состояние остаётся RECONNECTING
                    # (будет сброшено в IDLE при следующем play_audio или stop_output)
                else:
                    logger.error("❌ [AVF] Не удалось перезапустить engine после переподключения")
                    if error_ref != objc.NULL:
                        error = error_ref
                        error_code = error.code() if hasattr(error, 'code') else None
                        logger.error(f"❌ [AVF] Код ошибки: {error_code}")
                    # ✅ КРИТИЧНО: При ошибке перезапуска сбрасываем состояние в IDLE
                    with self._lock:
                        if self._output_state == AudioState.RECONNECTING:
                            self._output_state = AudioState.IDLE
                    return False
            
            return True
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка переподключения player node: {e}", exc_info=True)
            return False
    
    def _get_real_output_device_name(self) -> Optional[str]:
        """Получить реальное имя OUTPUT устройства через SwitchAudioSource (как в legacy системе)"""
        try:
            import subprocess
            import json
            import shutil
            
            # Используем SwitchAudioSource (как в legacy системе)
            switch_audio_source_path = shutil.which('SwitchAudioSource')
            if not switch_audio_source_path:
                logger.warning("⚠️ [AVF] SwitchAudioSource не найден в PATH")
                return "System Default Output"
            
            result = subprocess.run(
                [switch_audio_source_path, '-c', '-t', 'output', '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                try:
                    device_info = json.loads(result.stdout.strip())
                    device_name = device_info.get('name', '')
                    if device_name:
                        logger.debug(f"✅ [AVF] Реальное имя OUTPUT устройства: {device_name}")
                        return device_name
                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ [AVF] Ошибка парсинга JSON от SwitchAudioSource: {e}")
            
            return "System Default Output"
                
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка получения реального имени OUTPUT устройства: {e}")
            return "System Default Output"
    
    def _get_real_input_device_name(self) -> Optional[str]:
        """Получить реальное имя INPUT устройства через SwitchAudioSource (как в legacy системе)"""
        try:
            import subprocess
            import json
            import shutil
            
            # Используем SwitchAudioSource (как в legacy системе)
            switch_audio_source_path = shutil.which('SwitchAudioSource')
            if not switch_audio_source_path:
                logger.warning("⚠️ [AVF] SwitchAudioSource не найден в PATH")
                return "System Default Input"
            
            result = subprocess.run(
                [switch_audio_source_path, '-c', '-t', 'input', '-f', 'json'],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                try:
                    device_info = json.loads(result.stdout.strip())
                    device_name = device_info.get('name', '')
                    if device_name:
                        logger.debug(f"✅ [AVF] Реальное имя INPUT устройства: {device_name}")
                        return device_name
                except json.JSONDecodeError as e:
                    logger.warning(f"⚠️ [AVF] Ошибка парсинга JSON от SwitchAudioSource: {e}")
            
            return "System Default Input"
                
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка получения реального имени INPUT устройства: {e}")
            return "System Default Input"
    
    def _init_completion_callback(self):
        """Инициализировать статический completion callback для AVAudioPlayerNode
        
        ✅ КРИТИЧНО: Использует глобальный callback, созданный на уровне модуля.
        Регистрирует экземпляр в глобальном словаре для доступа из callback.
        Это гарантирует, что PyObjC всегда получает правильный блок с корректной сигнатурой.
        """
        # ✅ КРИТИЧНО: Регистрируем экземпляр в глобальном словаре для доступа из статического callback
        global _AVF_ENGINE_INSTANCES, _PLAYER_NODE_TO_ENGINE
        _AVF_ENGINE_INSTANCES[id(self)] = self
        
        # ✅ КРИТИЧНО: Привязываем player_node к этому экземпляру для точной идентификации в callback
        # ⚠️ ВАЖНО: AVAudioPlayerNode не поддерживает weakref, поэтому используем fallback через ID
        if self._player_node is not None:
            try:
                _bind_player_node_to_engine(self._player_node, self)
                logger.info("✅ [AVF] Player node привязан к экземпляру AVFAudioEngine")
                
                # ✅ КРИТИЧНО: Проверяем успешность привязки (через fallback, т.к. weakref не работает)
                # Но не логируем ошибку, если проверка не удалась - это нормально для AVAudioPlayerNode
                try:
                    engine_from_binding = _lookup_engine_by_player_node(self._player_node)
                    if engine_from_binding is not None and engine_from_binding is self:
                        logger.info("✅ [AVF] Привязка player_node → engine подтверждена")
                    else:
                        logger.debug("🔍 [AVF] Привязка player_node → engine не подтверждена через lookup (это нормально, используется fallback)")
                except Exception as lookup_error:
                    # Ошибка lookup - это нормально для AVAudioPlayerNode (не поддерживает weakref)
                    logger.debug(f"🔍 [AVF] Ошибка проверки привязки через lookup (ожидаемо): {type(lookup_error).__name__}")
            except Exception as e:
                logger.error(f"❌ [AVF] Ошибка привязки player_node → engine: {e}", exc_info=True)
        else:
            logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: _player_node = None, привязка не может быть выполнена")
        
        # ✅ КРИТИЧНО: Используем глобальный callback, созданный на уровне модуля
        # Callback создаётся один раз при первом вызове, затем переиспользуется
        try:
            logger.info("🔧 [AVF] Инициализация completion callback...")
            logger.info(f"🔍 [AVF] AVF_PLAYER_NODE_AVAILABLE = {AVF_PLAYER_NODE_AVAILABLE}")
            logger.info(f"🔍 [AVF] AVAudioPlayerNode = {AVAudioPlayerNode}")
            
            # ✅ КРИТИЧНО: Проверяем доступность ПЕРЕД вызовом _create_avf_completion_callback()
            if not AVF_PLAYER_NODE_AVAILABLE:
                logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: AVF_PLAYER_NODE_AVAILABLE = False")
                logger.error("❌ [AVF] Импорт AVAudioPlayerNode не удался при загрузке модуля")
                logger.error("❌ [AVF] Completion callback НЕ БУДЕТ создан")
                self._output_completion_callback = None
                return
            
            if AVAudioPlayerNode is None:
                logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: AVAudioPlayerNode = None")
                logger.error("❌ [AVF] Импорт AVAudioPlayerNode не удался при загрузке модуля")
                logger.error("❌ [AVF] Completion callback НЕ БУДЕТ создан")
                self._output_completion_callback = None
                return
            
            logger.info("✅ [AVF] AVAudioPlayerNode доступен, создаём completion callback...")
            self._output_completion_callback = _create_avf_completion_callback()
            
            if self._output_completion_callback is None:
                logger.error("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: Completion callback недоступен!")
                logger.error("❌ [AVF] _create_avf_completion_callback() вернул None")
                logger.error("❌ [AVF] Воспроизведение будет работать, но завершение зависит ТОЛЬКО от fallback timeout")
                logger.error("❌ [AVF] Это может привести к зависанию ProcessingWorkflow, ожидающего playback.completed")
                logger.error("❌ [AVF] Проверьте логи выше для деталей ошибки создания callback")
            else:
                logger.info("✅ [AVF] Completion callback успешно инициализирован, используется статический callback с модульного уровня")
                logger.info("✅ [AVF] Completion callback registered")
                
        except Exception as e:
            logger.exception("❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА при инициализации completion callback")
            logger.error(f"❌ [AVF] Тип исключения: {type(e).__name__}")
            logger.error(f"❌ [AVF] Сообщение: {str(e)}")
            logger.error(f"❌ [AVF] AVF_PLAYER_NODE_AVAILABLE = {AVF_PLAYER_NODE_AVAILABLE}")
            logger.error(f"❌ [AVF] AVAudioPlayerNode = {AVAudioPlayerNode}")
            self._output_completion_callback = None
    
    # ✅ УБРАНО: _cancel_fallback_timer() - fallback таймеры больше не используются
    
    def _ensure_loop_attached(self) -> bool:
        """Централизованная проверка и прикрепление event loop
        
        ✅ КРИТИЧНО: Проверяет _event_loop, _pending_loop и актуальный event_bus._loop.
        Переносит валидный loop в _event_loop и вызывает _flush_pending_events().
        Используется во всех местах перед публикацией событий для устранения дублирования логики.
        
        Returns:
            bool: True если loop доступен и запущен, False иначе
        """
        # Проверяем текущий _event_loop
        if self._event_loop and not self._event_loop.is_closed() and self._event_loop.is_running():
            return True
        
        # Проверяем _pending_loop и прикрепляем если запустился
        if self._pending_loop and not self._pending_loop.is_closed():
            if self._pending_loop.is_running():
                self._event_loop = self._pending_loop
                self._pending_loop = None
                logger.debug(f"✅ [AVF] Pending event loop прикреплён (запустился): {id(self._event_loop)}")
                self._flush_pending_events()
                return True
        
        # Проверяем event_bus._loop
        if self._event_bus and hasattr(self._event_bus, '_loop'):
            bus_loop = self._event_bus._loop
            if bus_loop and not bus_loop.is_closed() and bus_loop.is_running():
                self._event_loop = bus_loop
                self._pending_loop = None
                logger.debug(f"✅ [AVF] Event loop прикреплён из EventBus: {id(bus_loop)}")
                self._flush_pending_events()
                return True
            elif bus_loop and not bus_loop.is_closed():
                # Сохраняем как pending если не запущен
                self._pending_loop = bus_loop
                logger.debug(f"🔄 [AVF] Event loop сохранён как pending (ещё не запущен): {id(bus_loop)}")
        
        return False
    
    def attach_event_loop(self, loop: Optional[asyncio.AbstractEventLoop] = None):
        """Прикрепить event loop для безопасной публикации событий из фоновых потоков
        
        ✅ КРИТИЧНО: Этот метод должен быть вызван после создания EventBus и прикрепления к нему loop.
        Если loop не передан, пытается получить его из EventBus.
        
        ✅ ИСПРАВЛЕНИЕ: Использует _ensure_loop_attached() для централизованной логики.
        
        Args:
            loop: Event loop для публикации событий (если None - получает из EventBus)
        """
        if loop is None:
            if self._event_bus and hasattr(self._event_bus, '_loop'):
                loop = self._event_bus._loop
        
        if loop is None:
            logger.warning("⚠️ [AVF] Event loop не передан (None), события будут накапливаться в очереди")
            return
        
        if loop.is_closed():
            logger.warning("⚠️ [AVF] Event loop закрыт, события будут накапливаться в очереди")
            return
        
        # ✅ КРИТИЧНО: Проверяем что loop запущен
        if loop.is_running():
            self._event_loop = loop
            self._pending_loop = None  # Очищаем pending loop
            logger.info(f"✅ [AVF] Event loop прикреплён: {id(loop)}")
            
            # ✅ КРИТИЧНО: Публикуем накопленные события из очереди сразу после прикрепления loop
            self._flush_pending_events()
        else:
            # ✅ ИСПРАВЛЕНИЕ: Сохраняем pending loop для последующей проверки
            self._pending_loop = loop
            logger.info(f"🔄 [AVF] Event loop сохранён как pending (ещё не запущен): {id(loop)}")
            # Периодически проверяем pending loop через _ensure_loop_attached()
    
    def _submit_to_event_loop(self, coro_or_callback, is_async: bool = True) -> bool:
        """Безопасная отправка корутины или callback в event loop из любого потока
        
        ✅ КРИТИЧНО: Использует сохранённый self._event_loop для call_soon_threadsafe (sync)
        или asyncio.run_coroutine_threadsafe (async). Логирует ошибки и сохраняет в очередь при недоступности loop.
        
        ✅ ИСПРАВЛЕНИЕ: Использует _ensure_loop_attached() для централизованной проверки.
        
        Args:
            coro_or_callback: Корутина (async) или callback (sync)
            is_async: True если это корутина, False если sync callback
        
        Returns:
            bool: True если задача отправлена, False если сохранена в очередь
        """
        # ✅ КРИТИЧНО: Используем централизованную проверку и прикрепление loop
        if not self._ensure_loop_attached():
            return False
        
        try:
            if is_async:
                # ✅ КРИТИЧНО: Для корутин используем run_coroutine_threadsafe
                asyncio.run_coroutine_threadsafe(coro_or_callback, self._event_loop)
            else:
                # ✅ КРИТИЧНО: Для sync callback используем call_soon_threadsafe
                self._event_loop.call_soon_threadsafe(coro_or_callback)
            return True
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка отправки задачи в event loop: {e}", exc_info=True)
            return False
    
    def _publish_event_safe(self, event_type: str, payload: dict) -> None:
        """Безопасная публикация события EventBus из любого потока (включая фоновые)
        
        ✅ КРИТИЧНО: Использует _submit_to_event_loop для гарантированной публикации.
        Сохраняет события в очередь ТОЛЬКО если loop недоступен.
        
        ✅ ИСПРАВЛЕНИЕ: Проверяет наличие loop перед вызовом _submit_to_event_loop.
        В очередь попадают только события когда loop действительно недоступен.
        
        ✅ ИСПРАВЛЕНИЕ: Если EventBus недоступен, событие сохраняется в очередь для публикации позже.
        
        Args:
            event_type: Тип события (например, "audio.device.output_resync_required")
            payload: Данные события
        """
        if not self._event_bus:
            # ✅ ИСПРАВЛЕНИЕ: Сохраняем событие в очередь, даже если EventBus недоступен
            # Оно будет опубликовано позже, когда EventBus станет доступен через _flush_pending_events()
            with self._pending_events_lock:
                self._pending_events.append((event_type, payload))
            logger.warning(f"⚠️ [AVF] EventBus не доступен, событие {event_type} сохранено в очередь для публикации позже")
            return
        
        # ✅ КРИТИЧНО: Используем централизованную проверку и прикрепление loop
        loop_available = self._ensure_loop_attached()
        
        # Если loop доступен - публикуем сразу, иначе кладём в очередь
        if loop_available:
            # Loop доступен - публикуем сразу
            async def _publish():
                try:
                    await self._event_bus.publish(event_type, payload)
                    logger.debug(f"✅ [AVF] Событие {event_type} опубликовано")
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка публикации события {event_type}: {e}", exc_info=True)
            
            # ✅ КРИТИЧНО: _submit_to_event_loop должен вернуть True если loop доступен
            # Если вернул False - это ошибка, но не кладём в очередь (loop уже проверен выше)
            success = self._submit_to_event_loop(_publish(), is_async=True)
            if not success:
                # Это не должно происходить если loop проверен выше, но на всякий случай логируем
                logger.error(f"❌ [AVF] Неожиданная ошибка: _submit_to_event_loop вернул False при доступном loop")
                # Не кладём в очередь - loop доступен, событие должно быть опубликовано
        else:
            # Loop недоступен - кладём в очередь
            with self._pending_events_lock:
                self._pending_events.append((event_type, payload))
            logger.debug(f"🔄 [AVF] Событие {event_type} сохранено в очередь (loop недоступен)")
    
    def _flush_pending_events(self):
        """Опубликовать накопленные события из очереди после прикрепления loop
        
        ✅ КРИТИЧНО: Безопасно работает даже если вызывается несколько раз.
        Защищён от гонок - использует цикл until queue пустая, чтобы обработать
        события, которые могут появиться во время flush (например, из callback в другом потоке).
        """
        if not self._event_loop or not self._event_loop.is_running():
            return
        
        total_published = 0
        max_iterations = 100  # Защита от бесконечного цикла
        
        # ✅ КРИТИЧНО: Цикл until queue пустая для защиты от гонок
        # Если во время flush появляются новые события, они тоже будут обработаны
        for iteration in range(max_iterations):
            with self._pending_events_lock:
                if not self._pending_events:
                    break
                
                events_to_publish = self._pending_events[:]
                self._pending_events.clear()
            
            # Публикуем события вне lock, чтобы не блокировать добавление новых событий
            events_count = len(events_to_publish)
            if events_count > 0:
                logger.debug(f"🔄 [AVF] Публикуем {events_count} событий из очереди (итерация {iteration + 1})")
                for event_type, payload in events_to_publish:
                    self._publish_event_safe(event_type, payload)
                total_published += events_count
        
        if total_published > 0:
            logger.info(f"✅ [AVF] Очередь событий очищена, опубликовано {total_published} событий")
        
        if iteration >= max_iterations - 1:
            logger.warning(f"⚠️ [AVF] Достигнут лимит итераций flush ({max_iterations}), возможна гонка")
    
    @property
    def is_input_active(self) -> bool:
        """Проверка активности записи"""
        with self._lock:
            return self._input_state == AudioState.RUNNING
    
    @property
    def is_output_active(self) -> bool:
        """Проверка активности воспроизведения"""
        with self._lock:
            return self._output_state == AudioState.RUNNING
    
    async def start_input(
        self,
        callback: Optional[Callable[[bytes, int, int], None]] = None
    ) -> bool:
        """
        Начать запись с микрофона
        
        Args:
            callback: Callback для получения аудио данных (data, sample_rate, channels)
        
        Returns:
            bool: True если запись начата успешно
        """
        with self._lock:
            if self._input_state == AudioState.RUNNING:
                logger.warning("⚠️ [AVF] Запись уже активна")
                return True
            
            if self._input_state == AudioState.STARTING:
                logger.warning("⚠️ [AVF] Запись уже запускается")
                return False
            
            self._input_state = AudioState.STARTING
        
        try:
            from AVFoundation import AVAudioPCMBuffer, AVAudioFormat, AVAudioCommonFormat
            
            # ⚠️ Ленивая инициализация input node (активирует микрофон только сейчас)
            if self._input_node is None:
                logger.info("🎤 [AVF] Инициализация input node (ленивая)")
                self._input_node = self._engine.inputNode()
            
            # Сохраняем callback и event loop
            self._input_callback = callback
            self._input_callback_loop = None
            try:
                # Пытаемся получить текущий event loop
                self._input_callback_loop = asyncio.get_running_loop()
            except RuntimeError:
                # Если нет запущенного loop, попробуем получить из другого потока
                try:
                    self._input_callback_loop = asyncio.get_event_loop()
                except RuntimeError:
                    logger.warning("⚠️ [AVF] Не удалось получить event loop для async callback")
            
            self._recorded_audio = []
            self._recording_start_time = time.time()
            self._recording_diagnostics = {
                "first_chunk": None,
                "chunk_count": 0,
                "total_bytes": 0
            }
            
            # Получаем формат входного устройства
            input_format_avf = self._input_node.inputFormatForBus_(0)
            sample_rate = int(input_format_avf.sampleRate())
            channels = int(input_format_avf.channelCount())
            
            self._input_format = AudioFormat(
                sample_rate=sample_rate,
                channels=channels
            )
            
            # ✅ СБОР ДАННЫХ: Сохраняем device_info
            device_name = self.get_current_input_device()
            self._input_device_info = AudioDeviceInfo(
                name=device_name or "System Default Input",
                is_input=True
            )
            
            logger.info(f"✅ [AVF] Input format: {sample_rate}Hz, {channels}ch, device={device_name}")
            
            # Создаём конвертер формата (если нужен)
            target_format = AudioFormat(
                sample_rate=self.config.input.target_rate,
                channels=self.config.input.channels
            )
            
            # Устанавливаем tap на input node
            buffer_size = 4096  # Стандартный размер буфера
            
            def recording_callback(buffer, when):
                """Callback для записи аудио"""
                if buffer is None:
                    return
                
                try:
                    # Конвертируем AVAudioPCMBuffer в bytes
                    audio_data = self._buffer_to_bytes(buffer, sample_rate, channels)
                    
                    if audio_data:
                        # Сохраняем для stop_input()
                        self._recorded_audio.append(audio_data)
                        
                        # ✅ СБОР ДАННЫХ: Сохраняем диагностику первого чанка
                        if self._recording_diagnostics and self._recording_diagnostics["first_chunk"] is None:
                            try:
                                import numpy as np
                                audio_array = np.frombuffer(audio_data, dtype=np.int16)
                                self._recording_diagnostics["first_chunk"] = {
                                    "size_bytes": len(audio_data),
                                    "samples": len(audio_array),
                                    "min": int(audio_array.min()),
                                    "max": int(audio_array.max()),
                                    "mean": float(audio_array.mean()),
                                    "std": float(audio_array.std()),
                                    "rms": float(np.sqrt(np.mean(audio_array.astype(np.float32) ** 2)))
                                }
                            except Exception as e:
                                logger.debug(f"🔍 [AVF] Не удалось собрать диагностику первого чанка: {e}")
                        
                        # Обновляем счётчики
                        if self._recording_diagnostics:
                            self._recording_diagnostics["chunk_count"] += 1
                            self._recording_diagnostics["total_bytes"] += len(audio_data)
                        
                        # Вызываем callback если есть
                        if self._input_callback:
                            try:
                                # Проверяем, является ли callback async
                                if asyncio.iscoroutinefunction(self._input_callback):
                                    # Async callback - запускаем через event loop
                                    if self._input_callback_loop:
                                        # Используем call_soon_threadsafe для безопасного вызова из другого потока
                                        future = asyncio.run_coroutine_threadsafe(
                                            self._input_callback(audio_data, sample_rate, channels),
                                            self._input_callback_loop
                                        )
                                        # Не ждём завершения, чтобы не блокировать audio thread
                                        # Ошибки будут логироваться в callback
                                    else:
                                        logger.warning("⚠️ [AVF] Async callback, но нет event loop")
                                else:
                                    # Синхронный callback - вызываем напрямую
                                    self._input_callback(audio_data, sample_rate, channels)
                            except Exception as e:
                                logger.error(f"❌ [AVF] Ошибка в input callback: {e}", exc_info=True)
                
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка обработки аудио буфера: {e}")
            
            # Устанавливаем tap
            self._input_node.installTapOnBus_bufferSize_format_block_(
                0,
                buffer_size,
                input_format_avf,
                recording_callback
            )
            
            # Запускаем engine если не запущен
            if not self._engine.isRunning():
                self._engine.prepare()
                error_ref = objc.NULL
                success = self._engine.startAndReturnError_(error_ref)
                
                if not success:
                    if error_ref != objc.NULL:
                        error = error_ref
                        error_code = error.code() if hasattr(error, 'code') else None
                        logger.error(f"❌ [AVF] Не удалось запустить engine: {error_code}")
                        
                        # Проверяем на критичные ошибки
                        if error_code == -9986:
                            logger.error("❌ [AVF] КРИТИЧНО: Ошибка -9986 (Audio Hardware Not Running)")
                            with self._lock:
                                self._input_state = AudioState.ERROR
                            return False
                    else:
                        logger.error("❌ [AVF] Не удалось запустить engine (неизвестная ошибка)")
                        with self._lock:
                            self._input_state = AudioState.ERROR
                        return False
                
                logger.info("✅ [AVF] Engine запущен")
            
            with self._lock:
                self._input_state = AudioState.RUNNING
            
            logger.info("✅ [AVF] Запись начата")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка начала записи: {e}", exc_info=True)
            with self._lock:
                self._input_state = AudioState.ERROR
            return False
    
    async def stop_input(self) -> Optional[AudioInputResult]:
        """
        Остановить запись и вернуть данные
        
        Returns:
            AudioInputResult: Результат записи или None при ошибке
        """
        with self._lock:
            if self._input_state == AudioState.IDLE:
                logger.warning("⚠️ [AVF] Запись не активна")
                return None
            
            if self._input_state == AudioState.STOPPING:
                logger.warning("⚠️ [AVF] Запись уже останавливается")
                return None
            
            self._input_state = AudioState.STOPPING
        
        try:
            # Удаляем tap
            if self._input_node:
                try:
                    self._input_node.removeTapOnBus_(0)
                except Exception as e:
                    logger.warning(f"⚠️ [AVF] Ошибка удаления tap: {e}")
            
            # Останавливаем engine если output не активен
            if not self.is_output_active:
                if self._engine and self._engine.isRunning():
                    self._engine.stop()
                    logger.info("✅ [AVF] Engine остановлен")
            
            # Собираем все данные
            all_data = b''.join(self._recorded_audio)
            
            # Вычисляем длительность
            duration_ms = 0.0
            frames_recorded = 0
            
            if self._recording_start_time and self._input_format:
                duration_ms = (time.time() - self._recording_start_time) * 1000.0
                if self._input_format.sample_rate > 0:
                    frames_recorded = len(all_data) // (self._input_format.channels * 2)  # int16 = 2 bytes
            
            # ✅ СБОР ДАННЫХ: Формируем полный результат с device_info и диагностикой
            result = AudioInputResult(
                data=all_data,
                sample_rate=self._input_format.sample_rate if self._input_format else self.config.input.target_rate,
                channels=self._input_format.channels if self._input_format else self.config.input.channels,
                duration_ms=duration_ms,
                frames_recorded=frames_recorded,
                device_info=self._input_device_info,
                input_format=self._input_format,
                diagnostics=self._recording_diagnostics.copy() if self._recording_diagnostics else None
            )
            
            # Очищаем состояние
            self._recorded_audio = []
            self._recording_start_time = None
            self._input_callback = None
            self._input_callback_loop = None
            self._input_device_info = None
            self._recording_diagnostics = None
            
            with self._lock:
                self._input_state = AudioState.IDLE
            
            logger.info(f"✅ [AVF] Запись остановлена ({duration_ms:.1f}ms, {frames_recorded} frames)")
            return result
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка остановки записи: {e}", exc_info=True)
            with self._lock:
                self._input_state = AudioState.ERROR
            return None
    
    async def play_audio(
        self,
        audio_data: bytes,
        sample_rate: int,
        channels: int = 1
    ) -> bool:
        """
        Воспроизвести аудио
        
        Args:
            audio_data: Аудио данные (PCM int16)
            sample_rate: Sample rate
            channels: Количество каналов
        
        Returns:
            bool: True если воспроизведение начато успешно
        """
        # ✅ КРИТИЧНО: Проверяем, было ли состояние IDLE ПЕРЕД изменением (возобновление после прерывания)
        # Это нужно сделать ДО изменения состояния на STARTING, чтобы правильно определить возобновление
        was_idle_before = False
        with self._lock:
            current_state = self._output_state
            was_idle_before = (current_state == AudioState.IDLE)
            
            # ✅ НОВОЕ: Обработка состояния RECONNECTING
            if current_state == AudioState.RECONNECTING:
                logger.info(f"🔄 [AVF] Воспроизведение во время переподключения (state={current_state}), продолжаем")
                # Не блокируем - переподключение должно завершиться быстро
                # Просто продолжаем, состояние будет обновлено в RUNNING после scheduleBuffer
                # ✅ КРИТИЧНО: НЕ сбрасываем callback - он статический и должен переиспользоваться
            
            if current_state == AudioState.RUNNING:
                logger.warning(f"⚠️ [AVF] Воспроизведение уже активно (state={current_state}), принудительно останавливаем перед новым воспроизведением")
                # Принудительно останавливаем перед новым воспроизведением
                try:
                    if self._player_node:
                        self._player_node.stop()
                    if not self.is_input_active and self._engine and self._engine.isRunning():
                        self._engine.stop()
                    self._output_state = AudioState.IDLE
                    logger.info("✅ [AVF] Воспроизведение принудительно остановлено")
                    was_idle_before = True  # После принудительной остановки считаем, что было IDLE
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка принудительной остановки: {e}")
                    self._output_state = AudioState.ERROR
                    return False
            
            if current_state == AudioState.STARTING:
                logger.warning(f"⚠️ [AVF] Воспроизведение уже запускается (state={current_state})")
                return False
            
            if current_state == AudioState.ERROR:
                logger.warning(f"⚠️ [AVF] Предыдущее состояние было ERROR, сбрасываем в IDLE")
                self._output_state = AudioState.IDLE
                was_idle_before = True  # После сброса ERROR считаем, что было IDLE
            
            # ✅ КРИТИЧНО: НЕ сбрасываем callback - он статический и должен переиспользоваться
            # Callback создаётся один раз при инициализации и используется для всех воспроизведений
            
            self._output_state = AudioState.STARTING
            logger.debug(f"🔍 [AVF] play_audio: состояние изменено на STARTING (было {current_state})")
        
        try:
            from AVFoundation import AVAudioPCMBuffer, AVAudioFormat, AVAudioCommonFormat
            
            # ✅ КРИТИЧНО: Проверяем, что player_node подключен
            if not self._player_node_connected:
                logger.error("❌ [AVF] КРИТИЧНО: Player node не подключен! Невозможно воспроизвести аудио")
                with self._lock:
                    self._output_state = AudioState.ERROR
                return False
            
            # Создаём формат
            output_format_avf = self._output_node.inputFormatForBus_(0)
            
            if output_format_avf is None:
                logger.error("❌ [AVF] output_format_avf is None в play_audio")
                with self._lock:
                    self._output_state = AudioState.ERROR
                return False
            
            # Логируем формат output и устройство для диагностики
            try:
                output_sample_rate = int(output_format_avf.sampleRate())
                output_channels = int(output_format_avf.channelCount())
                output_common_format = int(output_format_avf.commonFormat())
                
                # Получаем информацию о текущем устройстве вывода
                output_device_name = self.get_current_output_device()
                logger.info(f"🔍 [AVF] Output format устройства: {output_sample_rate}Hz, {output_channels}ch, format={output_common_format}, device={output_device_name}")
                logger.info(f"🔍 [AVF] Входной формат: {sample_rate}Hz, {channels}ch")
                if abs(sample_rate - output_sample_rate) > 1.0 or channels != output_channels:
                    logger.info(f"🔄 [AVF] Требуется конвертация: {sample_rate}Hz/{channels}ch → {output_sample_rate}Hz/{output_channels}ch")
            except Exception as e:
                logger.error(f"❌ [AVF] Ошибка получения параметров формата: {e}", exc_info=True)
                with self._lock:
                    self._output_state = AudioState.ERROR
                return False
            
            # ✅ КРИТИЧНО: Player node должен быть подключен при инициализации
            # Если по какой-то причине не подключен - пытаемся подключить сейчас
            if not self._player_node_connected:
                logger.warning("⚠️ [AVF] Player node не подключен, пытаемся подключить сейчас")
                try:
                    # ⚠️ ВАЖНО: Подключаем только если engine не запущен
                    # Если engine запущен, подключение может вызвать segmentation fault
                    if not self._engine.isRunning():
                        self._engine.connect_to_format_(
                            self._player_node,
                            self._output_node,
                            output_format_avf
                        )
                        self._player_node_connected = True
                        logger.info("✅ [AVF] Player node подключен к output node (fallback)")
                    else:
                        logger.error("❌ [AVF] Невозможно подключить player node - engine уже запущен")
                        with self._lock:
                            self._output_state = AudioState.ERROR
                        return False
                except Exception as e:
                    logger.error(f"❌ [AVF] Ошибка подключения player node (fallback): {e}", exc_info=True)
                    with self._lock:
                        self._output_state = AudioState.ERROR
                    return False
            
            # Конвертируем bytes в AVAudioPCMBuffer
            try:
                audio_buffer = self._bytes_to_buffer(
                    audio_data,
                    sample_rate,
                    channels,
                    output_format_avf
                )
            except Exception as e:
                logger.error(f"❌ [AVF] Ошибка в _bytes_to_buffer: {e}", exc_info=True)
                with self._lock:
                    self._output_state = AudioState.ERROR
                return False
            
            if audio_buffer is None:
                logger.error("❌ [AVF] Не удалось создать audio buffer")
                with self._lock:
                    self._output_state = AudioState.ERROR
                    return False
            
            # Запускаем engine если не запущен
            if not self._engine.isRunning():
                self._engine.prepare()
                error_ref = objc.NULL
                success = self._engine.startAndReturnError_(error_ref)
                
                if not success:
                    if error_ref != objc.NULL:
                        error = error_ref
                        error_code = error.code() if hasattr(error, 'code') else None
                        logger.error(f"❌ [AVF] Не удалось запустить engine: {error_code}")
                    else:
                        logger.error("❌ [AVF] Не удалось запустить engine (неизвестная ошибка)")
                    
                    with self._lock:
                        self._output_state = AudioState.ERROR
                    return False
                
                logger.info("✅ [AVF] Engine запущен")
            
            # Воспроизводим
            buffer_format_sample_rate = int(audio_buffer.format().sampleRate()) if audio_buffer.format() else 0
            logger.info(f"🔍 [AVF] Запуск воспроизведения: buffer={audio_buffer.frameLength()} frames, buffer_format={buffer_format_sample_rate}Hz, output_format={output_format_avf.sampleRate()}Hz")
            if buffer_format_sample_rate != int(output_format_avf.sampleRate()):
                logger.warning(f"⚠️ [AVF] Несоответствие форматов: buffer={buffer_format_sample_rate}Hz, output={output_format_avf.sampleRate()}Hz")
            
            # ✅ КРИТИЧНО: Вычисляем длительность до установки состояния (не требует lock)
            import time
            duration_sec = len(audio_data) / (sample_rate * channels * 2)
            
            # ✅ КРИТИЧНО: Если это возобновление после прерывания (было IDLE), останавливаем player_node
            # Это необходимо для очистки состояния и правильной работы completion callback
            # was_idle_before уже определён в начале функции play_audio, ДО изменения состояния
            if was_idle_before and self._player_node:
                try:
                    # Останавливаем player_node для очистки состояния перед новым scheduleBuffer
                    self._player_node.stop()
                    logger.debug("✅ [AVF] player_node остановлен перед возобновлением (очистка состояния)")
                    # Небольшая задержка для завершения остановки
                    await asyncio.sleep(0.05)
                except Exception as stop_error:
                    logger.warning(f"⚠️ [AVF] Ошибка остановки player_node перед возобновлением: {stop_error}")
            
            # ✅ КРИТИЧНО: Устанавливаем состояние в RUNNING СРАЗУ после player_node.play()
            # Это защищает от race condition с AVAudioEngineConfigurationChangeNotification,
            # которая может прийти между play() и scheduleBuffer и остановить engine
            with self._lock:
                # ✅ НОВОЕ: Если было RECONNECTING - переводим в RUNNING, иначе устанавливаем RUNNING
                if self._output_state == AudioState.RECONNECTING:
                    logger.debug("✅ [AVF] Состояние переведено из RECONNECTING в RUNNING")
                self._output_state = AudioState.RUNNING
                
                # ✅ КРИТИЧНО: Сохраняем время начала воспроизведения и ожидаемую длительность
                self._playback_start_time = time.time()
                self._expected_playback_duration = duration_sec
            
            self._player_node.play()
            
            # ✅ КРИТИЧНО: Обновляем счётчики сэмплов для точного расчёта остатка при возобновлении
            with self._lock:
                # Вычисляем количество сэмплов в буфере (frameLength * channels)
                buffer_frames = int(audio_buffer.frameLength()) if audio_buffer else 0
                buffer_channels = int(output_format_avf.channelCount()) if output_format_avf else channels
                self._total_samples_in_buffer = buffer_frames * buffer_channels
                # Если это новое воспроизведение (не возобновление), сбрасываем счётчик
                if self._output_state != AudioState.RECONNECTING:
                    self._samples_played = 0
                logger.debug(f"🔍 [AVF] Обновлены счётчики сэмплов: total={self._total_samples_in_buffer}, played={self._samples_played}")
            
            # ✅ КРИТИЧНО: Используем статический completion callback, созданный при инициализации
            # Callback уже создан в _init_completion_callback() и хранится в self._output_completion_callback
            # Это гарантирует, что PyObjC всегда получает правильный блок с корректной сигнатурой
            callback_to_use = self._output_completion_callback
            
            if callback_to_use is None:
                logger.error("❌ [AVF] КРИТИЧЕСКАЯ ПРОБЛЕМА: Completion callback недоступен, полагаемся ТОЛЬКО на fallback timeout")
                logger.error("❌ [AVF] Это означает, что playback.completed может не прийти вовремя, что приведёт к зависанию ProcessingWorkflow")
                logger.error("❌ [AVF] Проверьте логи инициализации для деталей ошибки создания callback")
            
            # ✅ КРИТИЧНО: Пробуем передать Python функцию напрямую
            # PyObjC может автоматически преобразовать Python callable в Objective-C блок
            # Если callback_to_use это Python функция, передаём её напрямую
            # Если None, передаём None и полагаемся на fallback таймер
            try:
                if callback_to_use is not None:
                    # ✅ КРИТИЧНО: Проверяем, не нужно ли остановить player_node перед новым scheduleBuffer
                    # AVAudioPlayerNode может требовать остановки перед новым scheduleBuffer после прерывания
                    # Но это может прервать воспроизведение, поэтому делаем это только если это возобновление
                    # (состояние было IDLE перед этим вызовом)
                    was_idle_before = (self._output_state == AudioState.IDLE) if hasattr(self, '_output_state') else False
                    
                    # Пробуем передать функцию напрямую
                    self._player_node.scheduleBuffer_atTime_options_completionHandler_(
                        audio_buffer,
                        None,  # atTime (None = сразу)
                        0,     # options
                        callback_to_use  # Python функция - PyObjC может преобразовать автоматически
                    )
                    logger.debug("✅ [AVF] scheduleBuffer вызван с completion handler (Python функция)")
                else:
                    # Callback недоступен - передаём None, полагаемся на fallback таймер
                    self._player_node.scheduleBuffer_atTime_options_completionHandler_(
                        audio_buffer,
                        None,  # atTime (None = сразу)
                        0,     # options
                        None   # completionHandler = None
                    )
                    logger.debug("✅ [AVF] scheduleBuffer вызван без completion handler (будет использован fallback таймер)")
            except Exception as schedule_error:
                # Если передача функции не работает, пробуем None
                logger.warning(f"⚠️ [AVF] Ошибка при передаче completion handler, пробуем None: {schedule_error}")
                try:
                    self._player_node.scheduleBuffer_atTime_options_completionHandler_(
                        audio_buffer,
                        None,
                        0,
                        None  # completionHandler = None
                    )
                    logger.debug("✅ [AVF] scheduleBuffer вызван без completion handler (fallback)")
                except Exception as schedule_error2:
                    logger.error(f"❌ [AVF] КРИТИЧЕСКАЯ ОШИБКА: Не удалось вызвать scheduleBuffer: {schedule_error2}")
                    raise
            
            # ✅ КРИТИЧНО: Логируем успешное начало воспроизведения после scheduleBuffer
            logger.info(f"✅ [AVF] Воспроизведение начато: {len(audio_data)} bytes, {sample_rate}Hz, {channels}ch, duration≈{duration_sec:.2f}s")
            
            # ✅ КРИТИЧНО: Проверяем доступность completion callback
            # БЕЗ callback воспроизведение невозможно - возвращаем False
            if callback_to_use is None:
                logger.error("❌ [AVF] КРИТИЧЕСКАЯ ПРОБЛЕМА: Completion callback недоступен, воспроизведение невозможно")
                logger.error("❌ [AVF] Проверьте логи инициализации для деталей ошибки создания callback")
                with self._lock:
                    self._output_state = AudioState.IDLE
                    self._playback_start_time = None
                    self._expected_playback_duration = None
                return False
            
            # ✅ УБРАНО: Fallback таймеры - полагаемся ТОЛЬКО на completion callback
            
            return True
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка начала воспроизведения: {e}", exc_info=True)
            with self._lock:
                self._output_state = AudioState.ERROR
            return False
    
    async def stop_output(self) -> bool:
        """Остановить воспроизведение
        
        ✅ КРИТИЧНО: Сбрасывает счётчики сэмплов при остановке.
        
        ✅ КРИТИЧНО: Все изменения состояния выполняются под lock для защиты от race conditions
        с _reconnect_player_node() и completionHandler от AVAudioPlayerNode.
        """
        # Сохраняем текущее состояние для логирования
        with self._lock:
            current_state = self._output_state
            if current_state == AudioState.IDLE:
                logger.debug("🔍 [AVF] stop_output: воспроизведение уже IDLE, пропускаем")
                return True
            
            if current_state == AudioState.STOPPING:
                logger.warning("⚠️ [AVF] Воспроизведение уже останавливается")
                return False
            
            # ✅ НОВОЕ: Обработка состояния RECONNECTING
            if current_state == AudioState.RECONNECTING:
                logger.info("🔄 [AVF] stop_output вызван во время переподключения, ждём завершения")
                # Не блокируем - переподключение должно завершиться быстро
                # Просто переводим в STOPPING, состояние будет обновлено после переподключения
            
            # ✅ УБРАНО: Отмена fallback таймера - таймеры больше не используются
            
            logger.debug(f"🔍 [AVF] stop_output: состояние {current_state} → STOPPING")
            self._output_state = AudioState.STOPPING
        
        try:
            if self._player_node:
                self._player_node.stop()
                # ⚠️ НЕ отключаем узел, оставляем подключённым для следующего воспроизведения
                # Отключение может вызвать проблемы при повторном подключении

            # Останавливаем engine если input не активен
            if not self.is_input_active:
                if self._engine and self._engine.isRunning():
                    self._engine.stop()
                    logger.info("✅ [AVF] Engine остановлен")
            
            with self._lock:
                self._output_state = AudioState.IDLE
                # ✅ КРИТИЧНО: Сбрасываем счётчики сэмплов при остановке
                self._samples_played = 0
                self._total_samples_in_buffer = 0
                # Очищаем время начала воспроизведения при остановке
                self._playback_start_time = None
                self._expected_playback_duration = None
            
            logger.info(f"✅ [AVF] Воспроизведение остановлено (state: {current_state} → IDLE)")
            return True
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка остановки воспроизведения: {e}", exc_info=True)
            with self._lock:
                self._output_state = AudioState.ERROR
            return False
    
    def get_current_input_device(self) -> Optional[str]:
        """Получить имя текущего input устройства"""
        try:
            # ✅ НОВОЕ: Возвращаем реальное имя устройства из кэша
            if self._cached_input_device_name:
                return self._cached_input_device_name
            
            # Fallback: обновляем кэш и возвращаем
            self._cached_input_device_name = self._get_real_input_device_name()
            return self._cached_input_device_name
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка получения input устройства: {e}")
            return "System Default Input"
    
    def get_samples_played(self) -> int:
        """Получить количество проигранных сэмплов для точного расчёта остатка при возобновлении
        
        ✅ КРИТИЧНО: Используется в speech_playback_integration для точного расчёта bytes_played
        при возобновлении воспроизведения после прерывания.
        
        Returns:
            int: Количество проигранных сэмплов (обновляется в play_audio и completion callback)
        """
        with self._lock:
            return self._samples_played
    
    def get_current_output_device(self) -> Optional[str]:
        """
        Получить имя текущего output устройства
        
        ✅ НОВОЕ: Возвращаем реальное имя устройства из кэша (обновляется при смене устройства)
        """
        try:
            if not self._output_node:
                return None
            
            # ✅ НОВОЕ: Возвращаем реальное имя устройства из кэша
            if self._cached_output_device_name:
                return self._cached_output_device_name
            
            # Fallback: обновляем кэш и возвращаем
            self._cached_output_device_name = self._get_real_output_device_name()
            return self._cached_output_device_name
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка получения output устройства: {e}")
            return "System Default Output"
    
    def _buffer_to_bytes(self, buffer: Any, sample_rate: int, channels: int) -> bytes:
        """Конвертировать AVAudioPCMBuffer в bytes (PCM int16)"""
        try:
            import numpy as np
            
            frame_length = int(buffer.frameLength())
            if frame_length == 0:
                return b''
            
            # Получаем формат buffer для определения типа данных
            format_avf = buffer.format()
            if format_avf is None:
                logger.error("❌ [AVF] buffer.format() вернул None")
                return b''
            
            # ⚠️ ВАЖНО: AVAudioCommonFormat значения:
            # 1 = Float32, 2 = Float64, 3 = Int16, 4 = Int32
            common_format = int(format_avf.commonFormat())
            is_float32 = (common_format == 1)  # Float32
            is_int16 = (common_format == 3)    # Int16
            
            audio_array = None
            
            if is_float32:
                # Используем floatChannelData() для float32 формата
                float_channel_data = buffer.floatChannelData()
                if float_channel_data is None or not isinstance(float_channel_data, tuple):
                    logger.error("❌ [AVF] floatChannelData() вернул None или неверный тип")
                    return b''
                
                # Собираем данные из всех каналов (non-interleaved → interleaved)
                channel_arrays = []
                for ch in range(channels):
                    if ch < len(float_channel_data):
                        ch_varlist = float_channel_data[ch]
                        if ch_varlist:
                            # ⚠️ PyObjC: используем as_buffer() для objc.varlist
                            ch_buffer = ch_varlist.as_buffer(frame_length * 4)  # float32 = 4 bytes
                            ch_array = np.frombuffer(ch_buffer, dtype=np.float32).copy()
                            channel_arrays.append(ch_array)
                
                if not channel_arrays:
                    logger.error("❌ [AVF] Не удалось получить данные каналов")
                    return b''
                
                # Interleave каналы если больше одного
                if len(channel_arrays) == 1:
                    float_array = channel_arrays[0]
                else:
                    # Interleave: [L0, R0, L1, R1, ...]
                    float_array = np.empty(frame_length * len(channel_arrays), dtype=np.float32)
                    for ch, ch_arr in enumerate(channel_arrays):
                        float_array[ch::len(channel_arrays)] = ch_arr
                
                # Конвертируем float32 → int16
                # Нормализуем [-1.0, 1.0] → [-32768, 32767] с clipping
                float_array = np.clip(float_array, -1.0, 1.0)
                audio_array = (float_array * 32767.0).astype(np.int16)
                
            elif is_int16:
                # Используем int16ChannelData() для int16 формата
                int16_channel_data = buffer.int16ChannelData()
                if int16_channel_data is None or not isinstance(int16_channel_data, tuple):
                    logger.error("❌ [AVF] int16ChannelData() вернул None или неверный тип")
                    return b''
                
                # Собираем данные из всех каналов
                channel_arrays = []
                for ch in range(channels):
                    if ch < len(int16_channel_data):
                        ch_varlist = int16_channel_data[ch]
                        if ch_varlist:
                            ch_buffer = ch_varlist.as_buffer(frame_length * 2)  # int16 = 2 bytes
                            ch_array = np.frombuffer(ch_buffer, dtype=np.int16).copy()
                            channel_arrays.append(ch_array)
                
                if not channel_arrays:
                    logger.error("❌ [AVF] Не удалось получить данные каналов (int16)")
                    return b''
                
                # Interleave каналы если больше одного
                if len(channel_arrays) == 1:
                    audio_array = channel_arrays[0]
                else:
                    audio_array = np.empty(frame_length * len(channel_arrays), dtype=np.int16)
                    for ch, ch_arr in enumerate(channel_arrays):
                        audio_array[ch::len(channel_arrays)] = ch_arr
            else:
                logger.error(f"❌ [AVF] Неподдерживаемый формат: {common_format}")
                return b''
            
            if audio_array is None:
                logger.error("❌ [AVF] Не удалось создать audio_array")
                return b''
            
            # Конвертируем в bytes
            return audio_array.tobytes()
            
        except Exception as e:
            logger.error(f"❌ [AVF] Ошибка конвертации buffer в bytes: {e}", exc_info=True)
            return b''
    
    def _bytes_to_buffer(
        self,
        audio_data: bytes,
        sample_rate: int,
        channels: int,
        target_format: Any
    ) -> Optional[Any]:
        """Конвертировать bytes в AVAudioPCMBuffer

        Args:
            audio_data: PCM int16 данные
            sample_rate: Sample rate входных данных
            channels: Количество каналов входных данных
            target_format: Целевой формат (формат output node)
        """
        if not audio_data:
            logger.error("❌ [AVF] Пустые аудио данные, нечего воспроизводить")
            return None

        if channels <= 0:
            logger.error(f"❌ [AVF] Недопустимое количество каналов: {channels}")
            return None

        try:
            import numpy as np
            from AVFoundation import (
                AVAudioPCMBuffer,
                AVAudioFormat,
                AVAudioPCMFormatFloat32,
            )
        except Exception as import_error:
            logger.error(f"❌ [AVF] Не удалось подготовить зависимости для буфера: {import_error}")
            return None

        pcm_array = np.frombuffer(audio_data, dtype=np.int16)
        total_samples = len(pcm_array)
        if total_samples == 0:
            logger.error("❌ [AVF] Не удалось распарсить аудио данные")
            return None

        frame_length = total_samples // channels
        if frame_length == 0:
            logger.error("❌ [AVF] Нулевой frame_length при конвертации аудио буфера")
            return None

        if total_samples % channels != 0:
            logger.warning(
                "⚠️ [AVF] Количество сэмплов не делится на каналы без остатка "
                f"(samples={total_samples}, channels={channels})"
            )

        output_channels = int(target_format.channelCount()) if target_format else channels
        output_channels = max(1, output_channels)
        target_sample_rate = float(target_format.sampleRate()) if target_format else float(sample_rate)

        # ✅ КРИТИЧНО: Ресемплинг если sample rate не совпадает
        resampled_audio_matrix = None
        resampled_frame_length = frame_length
        
        if abs(sample_rate - target_sample_rate) > 1.0:  # Разница больше 1Hz
            logger.info(f"🔄 [AVF] Ресемплинг необходим: {sample_rate}Hz → {target_sample_rate}Hz ({frame_length} frames, device={self.get_current_output_device()})")
            
            # Преобразуем в float32 для ресемплинга
            audio_matrix_float = pcm_array.reshape(frame_length, channels).astype(np.float32) / 32768.0
            
            # Ресемплинг каждого канала отдельно
            resampled_channels = []
            ratio = target_sample_rate / sample_rate
            resampled_frame_length = int(frame_length * ratio)
            
            try:
                # Пробуем использовать scipy для качественного ресемплинга
                from scipy import signal
                for ch in range(channels):
                    resampled_ch = signal.resample(audio_matrix_float[:, ch], resampled_frame_length)
                    resampled_channels.append(resampled_ch)
                logger.debug(f"✅ [AVF] Ресемплинг через scipy: {frame_length} → {resampled_frame_length} frames")
            except ImportError:
                # Fallback: линейная интерполяция через numpy
                logger.warning(f"⚠️ [AVF] scipy недоступен, используем линейную интерполяцию для ресемплинга")
                for ch in range(channels):
                    indices = np.linspace(0, frame_length - 1, resampled_frame_length)
                    resampled_ch = np.interp(indices, np.arange(frame_length), audio_matrix_float[:, ch])
                    resampled_channels.append(resampled_ch)
                logger.debug(f"✅ [AVF] Ресемплинг через numpy.interp: {frame_length} → {resampled_frame_length} frames")
            
            # Объединяем каналы обратно в матрицу
            if channels > 1:
                resampled_audio_matrix = np.column_stack(resampled_channels)
            else:
                # Для моно: создаём матрицу (N, 1)
                resampled_audio_matrix = resampled_channels[0].reshape(-1, 1)
            logger.info(f"✅ [AVF] Ресемплинг завершён: {frame_length} frames @ {sample_rate}Hz → {resampled_frame_length} frames @ {target_sample_rate}Hz (ratio={ratio:.3f})")
        else:
            # Sample rate совпадает, ресемплинг не нужен
            resampled_audio_matrix = pcm_array.reshape(frame_length, channels).astype(np.float32) / 32768.0
            resampled_frame_length = frame_length

        buffer_format = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
            AVAudioPCMFormatFloat32,
            target_sample_rate,
            output_channels,
            False,
        )

        if buffer_format is None:
            logger.error("❌ [AVF] Не удалось создать формат буфера для воспроизведения")
            return None

        buffer = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(buffer_format, resampled_frame_length)
        if buffer is None:
            logger.error("❌ [AVF] AVAudioPCMBuffer.alloc() вернул None")
            return None

        buffer.setFrameLength_(resampled_frame_length)

        channel_data = buffer.floatChannelData()
        if not isinstance(channel_data, tuple) or not channel_data:
            logger.error("❌ [AVF] floatChannelData() вернул пустое значение")
            return None

        buffer_frame_bytes = resampled_frame_length * 4

        # ✅ КРИТИЧНО: Обработка конвертации каналов (моно → стерео для AirPods)
        input_channels = resampled_audio_matrix.shape[1] if len(resampled_audio_matrix.shape) > 1 else 1
        
        if input_channels != output_channels:
            logger.info(f"🔄 [AVF] Конвертация каналов: {input_channels}ch → {output_channels}ch")
        
        for out_channel in range(output_channels):
            dest_varlist = channel_data[out_channel] if out_channel < len(channel_data) else None
            if dest_varlist is None:
                logger.warning(f"⚠️ [AVF] Канал {out_channel} недоступен в channel_data")
                continue

            # Выбираем исходный канал: если моно → стерео, дублируем канал 0
            if input_channels == 1 and output_channels > 1:
                source_channel = 0  # Дублируем моно канал для всех выходных каналов
            elif out_channel < input_channels:
                source_channel = out_channel  # Используем соответствующий канал
            else:
                source_channel = 0  # Fallback: используем первый канал
            
            src_view = np.ascontiguousarray(resampled_audio_matrix[:, source_channel])
            
            if len(src_view) != resampled_frame_length:
                logger.error(f"❌ [AVF] Несоответствие длины: src_view={len(src_view)}, resampled_frame_length={resampled_frame_length}")
                return None

            dest_buffer = dest_varlist.as_buffer(buffer_frame_bytes)
            dest_float_view = memoryview(dest_buffer).cast('f')

            dest_float_view[:resampled_frame_length] = src_view

        logger.debug(f"✅ [AVF] Буфер создан: {resampled_frame_length} frames @ {target_sample_rate}Hz, {output_channels}ch")
        return buffer
