"""
Нативный монитор клавиатуры для macOS через Quartz CGEventTap.

API совместим с KeyboardMonitor: register_callback, set_loop, start_monitoring, stop_monitoring, get_status.
"""

import asyncio
import logging
import threading
import time
from typing import Optional, Callable, Dict, Any

try:
    from Quartz import (
        CGEventTapCreate,
        CGEventTapEnable,
            CGEventTapIsEnabled,  # ✅ FIX: Добавляем проверку активности tap
        CFRunLoopAddSource,
        CFRunLoopGetCurrent,
        CFRunLoopGetMain,
        CFRunLoopRunInMode,
        CFRunLoopSourceInvalidate,
        CFMachPortCreateRunLoopSource,
        kCGHIDEventTap,
        kCGHeadInsertEventTap,
        kCGEventTapOptionListenOnly,
        kCGEventTapOptionDefault,
        kCGEventKeyDown,
        kCGEventKeyUp,
        kCGEventFlagsChanged,
        kCFRunLoopCommonModes,
        kCFRunLoopDefaultMode,
        CGEventGetIntegerValueField,
        CGEventGetFlags,
        kCGKeyboardEventKeycode,
        kCGEventFlagMaskShift,
        kCGEventFlagMaskControl,
    )
    QUARTZ_AVAILABLE = True
except Exception as e:  # pragma: no cover
    QUARTZ_AVAILABLE = False

from ..types import KeyEvent, KeyEventType, KeyboardConfig

logger = logging.getLogger(__name__)


class QuartzKeyboardMonitor:
    """Глобальный монитор клавиатуры на macOS через Quartz Event Tap."""

    # Keycodes для macOS (US layout)
    KEYCODES = {
        "left_shift": 56,  # Левый Shift
        # При необходимости можно расширить: space(49), enter(36), esc(53), right_shift(60), alt(58/61)
    }
    
    # Keycodes для комбинации Control+N
    CONTROL_KEYCODES = {59, 62}  # Левый и правый Control (по умолчанию используем оба)
    N_KEYCODE = 45  # Клавиша N (US layout)

    def __init__(self, config: KeyboardConfig):
        self.config = config
        self.key_to_monitor = config.key_to_monitor
        self.short_press_threshold = config.short_press_threshold
        self.long_press_threshold = config.long_press_threshold
        self.event_cooldown = config.event_cooldown
        self.hold_check_interval = config.hold_check_interval
        # Защита от залипания: таймауты для сброса состояния
        self.combo_timeout_sec = config.combo_timeout_sec
        self.key_state_timeout_sec = config.key_state_timeout_sec

        # Состояние
        self.is_monitoring = False
        self.key_pressed = False
        self.press_start_time: Optional[float] = None
        self.last_event_time = 0.0
        self._long_sent = False
        # КРИТИЧНО: Флаг для предотвращения двойной обработки между flagsChanged и keyUp
        self._event_processed = False
        self._last_event_timestamp = 0.0

        # Потоки
        self.hold_monitor_thread: Optional[threading.Thread] = None
        self.stop_event = threading.Event()
        self.state_lock = threading.RLock()

        # Callbacks
        self.event_callbacks: Dict[KeyEventType, Callable] = {}

        # Async loop для async-колбэков
        self._loop: Optional[asyncio.AbstractEventLoop] = None

        # Quartz объекты
        self._tap = None
        self._tap_source = None
        
        # Отслеживание предыдущего состояния модификаторов (для kCGEventFlagsChanged)
        self._previous_left_shift_pressed = False
        
        # Состояние для комбинации Control+N
        self._control_pressed = False
        self._previous_control_pressed = False  # ✅ FIX: Отслеживаем предыдущее состояние Control
        self._n_pressed = False
        self._combo_active = False
        self._combo_start_time: Optional[float] = None
        # Время последнего события для каждой клавиши (для защиты от залипания)
        self._control_last_event_time: Optional[float] = None
        self._n_last_event_time: Optional[float] = None

        # Доступность
        self.keyboard_available = QUARTZ_AVAILABLE
        if not QUARTZ_AVAILABLE:
            logger.warning("⚠️ Quartz недоступен — нативный монитор клавиатуры отключен")

        # Целевой keycode или комбинация
        if self.key_to_monitor == "ctrl_n":
            # Для комбинации не нужен одиночный keycode
            self._target_keycode = None
            self._is_combo = True
        else:
            self._target_keycode = self.KEYCODES.get(self.key_to_monitor, None)
            self._is_combo = False
            if self._target_keycode is None:
                logger.warning(f"⚠️ Неподдерживаемая клавиша для Quartz: {self.key_to_monitor}")
                self.keyboard_available = False

    def _handle_combo_event(self, event_type, event):
        """Обрабатывает события для комбинации Control+N"""
        try:
            now = time.time()
            
            # Обработка flagsChanged для Control
            if event_type == kCGEventFlagsChanged:
                keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                flags = CGEventGetFlags(event)
                control_pressed = bool(flags & kCGEventFlagMaskControl)
                
                # ✅ FIX: Всегда проверяем изменение состояния Control по flags
                # flagsChanged может прийти с keycode=0 или другим keycode, но flags всегда содержат актуальное состояние
                # Это критично для правильной обработки отпускания Control
                with self.state_lock:
                    was_control_pressed = self._control_pressed
                    
                    # ✅ FIX: Обновляем состояние Control если оно изменилось
                    # Это гарантирует, что мы всегда знаем актуальное состояние, даже если keycode не совпадает
                    if control_pressed != was_control_pressed:
                        self._control_pressed = control_pressed
                        self._previous_control_pressed = control_pressed
                        
                        # Обновляем время последнего события для защиты от залипания
                        self._control_last_event_time = now if control_pressed else None
                        
                        # ✅ ПЛАН: При отпускании Control сбрасываем все связанные состояния
                        if not control_pressed and was_control_pressed:
                            logger.debug(f"🔄 [RESET] Control отпущен через flagsChanged, сбрасываем связанные состояния")
                            # Сбрасываем N, если она была зажата (защита от залипания)
                            if self._n_pressed:
                                logger.debug(f"🔄 [RESET] Сбрасываем _n_pressed (было True)")
                                self._n_pressed = False
                                self._n_last_event_time = None
                            # Сбрасываем флаги комбинации
                            if self._combo_active:
                                logger.debug(f"🔄 [RESET] Сбрасываем _combo_active (было True)")
                            if self._long_sent:
                                logger.debug(f"🔄 [RESET] Сбрасываем _long_sent (было True)")
                                self._long_sent = False
                        
                        # ✅ FIX: Логируем изменение состояния для диагностики
                        logger.debug(f"🔍 FlagsChanged: Control (keycode={keycode}), control_pressed={control_pressed} (было {was_control_pressed})")
                        
                        # Обновляем состояние комбинации
                        self._update_combo_state()
                    elif keycode in self.CONTROL_KEYCODES:
                        # ✅ FIX: Даже если состояние не изменилось, обновляем время события
                        # Это помогает избежать ложных срабатываний залипания
                        self._control_last_event_time = now if control_pressed else None
                
                return event
            
            # Обработка keyDown/keyUp для N
            if event_type in (kCGEventKeyDown, kCGEventKeyUp):
                keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                
                if keycode != self.N_KEYCODE:
                    return event
                
                with self.state_lock:
                    if event_type == kCGEventKeyDown:
                        # ✅ ПЛАН: Игнорируем автоповтор N, но обновляем время для защиты от залипания
                        if self._n_pressed:
                            logger.debug("🔒 [SUPPRESS] Quartz: игнорируем автоповтор N (обновляем _n_last_event_time)")
                            # КРИТИЧНО: Обновляем время последнего события при автоповторе,
                            # чтобы показать, что клавиша реально зажата (не залипла)
                            self._n_last_event_time = now
                            # Подавляем событие - возвращаем None для блокировки keyDown N
                            # Подавляем если комбинация активна ИЛИ Control зажат (для надежности)
                            if self._combo_active or self._control_pressed:
                                logger.debug(f"🔒 [SUPPRESS] Подавляем keyDown N (combo_active={self._combo_active}, control_pressed={self._control_pressed})")
                                return None
                            return event
                        
                        # Cooldown только для keyDown N
                        if (now - self.last_event_time) < self.event_cooldown:
                            logger.debug("🔒 Quartz: keyDown N пропущен из-за cooldown")
                            return event
                        
                        self._n_pressed = True
                        self.last_event_time = now
                        # Обновляем время последнего события для защиты от залипания
                        self._n_last_event_time = now
                        
                        # Обновляем состояние комбинации
                        self._update_combo_state()
                        # 2. Control уже зажат (даже если комбинация еще не активирована из-за race condition)
                        # Это предотвращает системные щелчки macOS
                        if self._combo_active or self._control_pressed:
                            logger.debug(f"🔒 Quartz: подавляем keyDown N (combo_active={self._combo_active}, control_pressed={self._control_pressed}, предотвращаем системные щелчки)")
                            return None
                        
                    else:  # kCGEventKeyUp
                        if not self._n_pressed:
                            return event
                        
                        # КРИТИЧНО: Сохраняем состояние комбинации ДО обновления,
                        # чтобы знать, была ли она активна в момент keyUp
                        was_combo_active = self._combo_active
                        was_control_pressed = self._control_pressed
                        was_long_sent = self._long_sent
                        
                        # ✅ ПЛАН: При keyUp N сбрасываем все связанные состояния
                        logger.debug(f"🔄 [RESET] keyUp N: сбрасываем _n_pressed, _long_sent (было: _n_pressed=True, _long_sent={was_long_sent})")
                        self._n_pressed = False
                        # Обновляем время последнего события для защиты от залипания
                        self._n_last_event_time = None
                        # ✅ ПЛАН: Сбрасываем _long_sent при keyUp
                        if was_long_sent:
                            logger.debug(f"🔄 [RESET] Сбрасываем _long_sent при keyUp N")
                            self._long_sent = False
                        
                        # Обновляем состояние комбинации
                        self._update_combo_state()
                        
                        # КРИТИЧНО: Подавляем keyUp N если:
                        # 1. Комбинация БЫЛА активна в момент keyUp, ИЛИ
                        # 2. Control БЫЛ зажат в момент keyUp (даже если комбинация не была активна из-за race condition)
                        # Это предотвращает системные щелчки macOS
                        if was_combo_active or was_control_pressed:
                            logger.debug(f"🔒 Quartz: подавляем keyUp N (was_combo_active={was_combo_active}, was_control_pressed={was_control_pressed}, предотвращаем системные щелчки)")
                            return None
                
                return event
            
            return event
        except Exception as e:
            logger.error(f"❌ Ошибка обработки combo события: {e}")
            return event
    
    def _update_combo_state(self):
        """Обновляет состояние комбинации Control+N и генерирует события при изменениях"""
        now = time.time()
        was_active = self._combo_active
        should_be_active = self._control_pressed and self._n_pressed
        
        if should_be_active and not was_active:
            # Активация комбинации: обе клавиши зажаты
            self._combo_active = True
            self._combo_start_time = now
            self._long_sent = False
            self._event_processed = False
            self._last_event_timestamp = 0.0
            self.key_pressed = True  # Для совместимости с hold_monitor
            self.press_start_time = now
            
            logger.info("✅ Control+N комбинация активирована")
            ev = KeyEvent(
                key=self.key_to_monitor,
                event_type=KeyEventType.PRESS,
                timestamp=now,
            )
            self._trigger_event(KeyEventType.PRESS, 0.0, ev)
            
        elif not should_be_active and was_active:
            # Деактивация комбинации: одна из клавиш отпущена
            # ✅ ПЛАН: Сбрасываем все состояния при деактивации
            logger.debug(f"🔄 [RESET] Деактивация комбинации: control_pressed={self._control_pressed}, n_pressed={self._n_pressed}")
            
            self._combo_active = False
            duration = now - (self._combo_start_time or now)
            self._combo_start_time = None
            
            # Защита от двойной обработки
            if self._event_processed and (now - self._last_event_timestamp) < 0.1:
                logger.debug("🔒 Combo deactivation: событие уже обработано, пропускаем")
                return
            
            long_sent_snapshot = self._long_sent
            # ✅ ПЛАН: Сбрасываем все связанные состояния
            self.key_pressed = False
            self.press_start_time = None
            self.last_event_time = now
            self._event_processed = True
            self._last_event_timestamp = now
            # ✅ ПЛАН: Сбрасываем _long_sent при деактивации (если не был отправлен LONG_PRESS)
            if not long_sent_snapshot:
                self._long_sent = False
            
            if long_sent_snapshot:
                # LONG_PRESS уже был отправлен - генерируем только RELEASE
                logger.debug("🔑 Combo deactivation: LONG_PRESS уже был, генерируем RELEASE")
                event_type_out = KeyEventType.RELEASE
            else:
                # Короткое нажатие - генерируем SHORT_PRESS
                logger.debug("🔑 Combo deactivation: короткое нажатие, генерируем SHORT_PRESS")
                event_type_out = KeyEventType.SHORT_PRESS
            
            ev = KeyEvent(
                key=self.key_to_monitor,
                event_type=event_type_out,
                timestamp=now,
                duration=duration,
            )
            self._trigger_event(event_type_out, duration, ev)
            
            # RELEASE всегда отправляется после SHORT_PRESS
            if event_type_out != KeyEventType.RELEASE:
                ev_release = KeyEvent(
                    key=self.key_to_monitor,
                    event_type=KeyEventType.RELEASE,
                    timestamp=now,
                    duration=duration,
                )
                self._trigger_event(KeyEventType.RELEASE, duration, ev_release)
    
    def register_callback(self, event_type, callback: Callable):
        if isinstance(event_type, str):
            try:
                event_type = KeyEventType(event_type)
            except ValueError:
                logger.warning(f"⚠️ Неизвестный тип события: {event_type}")
                return
        self.event_callbacks[event_type] = callback
        logger.info(f"🔑 QuartzMonitor: callback зарегистрирован для {event_type.value}")
        print(f"🔑 QuartzMonitor: callback зарегистрирован для {event_type.value}")  # Для отладки

    def set_loop(self, loop: asyncio.AbstractEventLoop):
        self._loop = loop
        logger.info(f"🔑 QuartzMonitor: установлен event loop для async-колбэков (loop={id(loop)}, running={loop.is_running() if loop else False})")
        print(f"🔑 QuartzMonitor: установлен event loop (loop={id(loop)}, running={loop.is_running() if loop else False})")

    def start_monitoring(self) -> bool:
        if not self.keyboard_available:
            logger.warning("⚠️ Клавиатурный Quartz-монитор недоступен")
            print("⚠️ Клавиатурный Quartz-монитор недоступен")
            return False
        if self.is_monitoring:
            logger.warning("⚠️ Мониторинг уже запущен")
            return False

        # КРИТИЧНО: Проверяем разрешения ПЕРЕД созданием event tap
        # ВАЖНО: Используем только публичный API с prompt=False (только проверка статуса, без запроса диалога)
        # Запрос диалога должен происходить только в activate_accessibility() при первом запуске
        logger.info("🔐 Проверяем разрешения для Quartz Event Tap...")
        print("🔐 Проверяем разрешения для Quartz Event Tap...")

        try:
            # Унифицируем импорты на Quartz (как в activator/handler)
            from Quartz import AXIsProcessTrustedWithOptions, kAXTrustedCheckOptionPrompt
            from Foundation import NSDictionary, NSNumber
            
            # КРИТИЧНО: prompt=False - только проверка статуса, НЕ запрос диалога
            # Диалог должен запрашиваться только в activate_accessibility() при первом запуске
            options = NSDictionary.dictionaryWithObject_forKey_(
                NSNumber.numberWithBool_(False),  # prompt=False - только проверка
                    kAXTrustedCheckOptionPrompt,
                )
            has_accessibility = bool(AXIsProcessTrustedWithOptions(options))

            logger.info(f"🔐 Accessibility permission: {has_accessibility}")
            print(f"🔐 Accessibility permission: {has_accessibility}")

            if not has_accessibility:
                logger.warning("⚠️ Accessibility разрешения НЕ выданы!")
                logger.warning("⚠️ Перейдите в: System Settings > Privacy & Security > Accessibility")
                logger.warning("⚠️ Добавьте Nexy.app и включите переключатель")
                print("⚠️ Accessibility разрешения НЕ выданы!")
                print("⚠️ Перейдите в: System Settings > Privacy & Security > Accessibility")
                print("⚠️ Добавьте Nexy.app и включите переключатель")
                # Не блокируем создание event tap - позволяем CGEventTapCreate вернуть None
        except ImportError as import_err:
            logger.warning(f"⚠️ Quartz/AX API недоступен для проверки разрешений: {import_err}")
            logger.warning(f"⚠️ Проверьте, что PyObjC-framework-Quartz установлен")
            print(f"⚠️ Quartz/AX API недоступен: {import_err}")
            has_accessibility = False
        except Exception as e:
            logger.warning(f"⚠️ Не удалось проверить Accessibility permissions: {e}")
            print(f"⚠️ Не удалось проверить Accessibility permissions: {e}")
            has_accessibility = False

        try:
            # Создаем Event Tap
            def _tap_callback(proxy, event_type, event, refcon):
                try:
                    # ✅ FIX: Логируем все события для диагностики (только для Control+N)
                    if self._is_combo:
                        # Логируем только Control и N события для диагностики
                        if event_type == kCGEventFlagsChanged:
                            keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                            flags = CGEventGetFlags(event)
                            control_pressed = bool(flags & kCGEventFlagMaskControl)
                            if keycode in self.CONTROL_KEYCODES:
                                logger.debug(f"🔍 [TAP] FlagsChanged: Control (keycode={keycode}), control_pressed={control_pressed}")
                        elif event_type in (kCGEventKeyDown, kCGEventKeyUp):
                            keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                            if keycode == self.N_KEYCODE:
                                logger.debug(f"🔍 [TAP] {('KeyDown' if event_type == kCGEventKeyDown else 'KeyUp')}: N (keycode={keycode})")
                    
                    # Обработка комбинации Control+N
                    if self._is_combo:
                        return self._handle_combo_event(event_type, event)
                    
                    # Обработка одиночной клавиши (left_shift для обратной совместимости)
                    # Логируем только события flagsChanged (для модификаторов) - это наша целевая клавиша
                    # Остальные события (keyDown/keyUp для обычных клавиш) обрабатываем без логирования

                    # Для модификаторов (Shift, Ctrl, Alt) может использоваться kCGEventFlagsChanged
                    # В kCGEventFlagsChanged можно получить keycode события, чтобы определить, какой модификатор изменился
                    if event_type == kCGEventFlagsChanged:
                        # Получаем keycode события - это указывает, какой именно модификатор изменился
                        keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                        flags = CGEventGetFlags(event)
                        shift_pressed = bool(flags & kCGEventFlagMaskShift)
                        
                        # Обрабатываем только Левый Shift (keycode=56), если это целевая клавиша
                        # Игнорируем все остальные модификаторы (Right Shift, Ctrl, Alt и т.д.)
                        if keycode == 56 and self._target_keycode == 56:
                            logger.debug(f"🔍 FlagsChanged: Left Shift, shift_pressed={shift_pressed} (было {self._previous_left_shift_pressed})")
                            # Отслеживаем изменение состояния: нажатие (False → True) или отпускание (True → False)
                            if shift_pressed and not self._previous_left_shift_pressed:
                                # Это keyDown для Левого Shift (состояние изменилось с False на True)
                                logger.info(f"✅ Найден Левый Shift через FlagsChanged (keyDown)")
                                with self.state_lock:
                                    if not self.key_pressed:  # Защита от повторных событий
                                        self.key_pressed = True
                                        self.press_start_time = time.time()
                                        self._long_sent = False  # Сбрасываем флаг для нового нажатия
                                        self._event_processed = False  # Сбрасываем флаг обработки для нового нажатия
                                        self._last_event_timestamp = 0.0
                                        
                                        # PRESS
                                        ev = KeyEvent(
                                            key=self.key_to_monitor,
                                            event_type=KeyEventType.PRESS,
                                            timestamp=self.press_start_time,
                                        )
                                        self._trigger_event(KeyEventType.PRESS, 0.0, ev)
                            elif not shift_pressed and self._previous_left_shift_pressed:
                                # Это keyUp для Левого Shift (состояние изменилось с True на False)
                                logger.info(f"✅ Отпущен Левый Shift через FlagsChanged (keyUp)")
                                with self.state_lock:
                                    # КРИТИЧНО: Защита от двойной обработки - проверяем, что событие не было обработано через keyUp
                                    now = time.time()
                                    if self._event_processed and (now - self._last_event_timestamp) < 0.1:
                                        logger.debug(f"🔒 FlagsChanged keyUp: событие уже обработано через keyUp, пропускаем")
                                        # Обновляем состояние, но не генерируем события
                                        if keycode == 56:
                                            self._previous_left_shift_pressed = shift_pressed
                                        return event
                                    
                                    if self.key_pressed:  # Защита от повторных событий
                                        duration = now - (self.press_start_time or now)
                                        
                                        # КРИТИЧНО: Сбрасываем состояние ПОСЛЕ определения типа события,
                                        # но ДО вызова _trigger_event, чтобы hold_monitor прекратил работу
                                        long_sent_snapshot = self._long_sent
                                        self.key_pressed = False
                                        self.press_start_time = None
                                        self.last_event_time = now
                                        self._event_processed = True
                                        self._last_event_timestamp = now
                                        
                                        # КРИТИЧНО: LONG_PRESS генерируется ТОЛЬКО из hold_monitor (во время удержания)
                                        # При keyUp НЕ генерируем LONG_PRESS - только SHORT_PRESS или RELEASE
                                        if long_sent_snapshot:
                                            # LONG_PRESS уже был отправлен из hold_monitor - генерируем только RELEASE
                                            logger.debug(f"🔑 keyUp: LONG_PRESS уже был отправлен из hold_monitor, генерируем только RELEASE")
                                            event_type_out = KeyEventType.RELEASE
                                        else:
                                            # Если LONG_PRESS не был отправлен из hold_monitor, значит это было короткое нажатие
                                            # Генерируем SHORT_PRESS (LONG_PRESS генерируется ТОЛЬКО из hold_monitor)
                                            event_type_out = KeyEventType.SHORT_PRESS
                                        
                                        # Создаем событие
                                        ev = KeyEvent(
                                            key=self.key_to_monitor,
                                            event_type=event_type_out,
                                            timestamp=now,
                                            duration=duration,
                                        )
                                        
                                        # Отправляем событие (SHORT_PRESS или RELEASE)
                                        # LONG_PRESS генерируется ТОЛЬКО из hold_monitor, не при keyUp
                                        self._trigger_event(event_type_out, duration, ev)
                                        
                                        # RELEASE всегда отправляется после SHORT_PRESS
                                        # НО: если event_type_out уже RELEASE, не отправляем его повторно
                                        if event_type_out != KeyEventType.RELEASE:
                                            ev_release = KeyEvent(
                                                key=self.key_to_monitor,
                                                event_type=KeyEventType.RELEASE,
                                                timestamp=now,
                                                duration=duration,
                                            )
                                            self._trigger_event(KeyEventType.RELEASE, duration, ev_release)
                            
                            # Обновляем предыдущее состояние только для Левого Shift
                            if keycode == 56:
                                self._previous_left_shift_pressed = shift_pressed
                        return event

                    if event_type not in (kCGEventKeyDown, kCGEventKeyUp):
                        # Игнорируем все события, кроме keyDown/keyUp/flagsChanged (для модификаторов)
                        return event

                    keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                    
                    # Игнорируем все клавиши, кроме целевой (left_shift = 56)
                    # Не логируем игнорируемые клавиши, чтобы не засорять логи
                    if keycode != self._target_keycode:
                        return event
                    
                    # Только для целевой клавиши (left_shift) логируем
                    logger.debug(f"🔑 Целевая клавиша обнаружена через keyDown/keyUp: keycode={keycode}")

                    now = time.time()

                    # cooldown работает только для повторных keyDown, keyUp обрабатываем всегда
                    if event_type == kCGEventKeyDown and (now - self.last_event_time) < self.event_cooldown:
                        logger.debug("🔒 Quartz: keyDown пропущен из-за cooldown")
                        return event

                    if event_type == kCGEventKeyDown:
                        logger.info("🔽 Quartz tap: keyDown detected for target key")
                        with self.state_lock:
                            if self.key_pressed:
                                # игнорируем авто-повтор
                                logger.debug("🔒 Quartz: игнорируем авто-повтор keyDown")
                                return event
                            self.key_pressed = True
                            self.press_start_time = now
                            self._long_sent = False  # Сбрасываем флаг для нового нажатия
                            self._event_processed = False  # Сбрасываем флаг обработки для нового нажатия
                            self._last_event_timestamp = 0.0
                            self.last_event_time = now  # Обновляем время последнего события

                        # PRESS
                        ev = KeyEvent(
                            key=self.key_to_monitor,
                            event_type=KeyEventType.PRESS,
                            timestamp=now,
                        )
                        self._trigger_event(KeyEventType.PRESS, 0.0, ev)
                    else:  # kCGEventKeyUp
                        logger.debug("Quartz tap: keyUp detected for target key")
                        with self.state_lock:
                            # КРИТИЧНО: Защита от двойной обработки - проверяем, что событие не было обработано через flagsChanged
                            if self._event_processed and (now - self._last_event_timestamp) < 0.1:
                                logger.debug(f"🔒 keyUp: событие уже обработано через flagsChanged, пропускаем")
                                return event
                            
                            if not self.key_pressed:
                                return event
                            duration = now - (self.press_start_time or now)

                            # КРИТИЧНО: Сбрасываем состояние ПОСЛЕ определения типа события,
                            # но ДО вызова _trigger_event, чтобы hold_monitor прекратил работу
                            long_sent_snapshot = self._long_sent
                            self.key_pressed = False
                            self.press_start_time = None
                            self.last_event_time = now
                            self._event_processed = True
                            self._last_event_timestamp = now

                            # КРИТИЧНО: LONG_PRESS генерируется ТОЛЬКО из hold_monitor (во время удержания)
                            # При keyUp НЕ генерируем LONG_PRESS - только SHORT_PRESS или RELEASE
                            # Если уже отправили LONG_PRESS из hold_monitor — это RELEASE
                            # Иначе (короткое нажатие) — это SHORT_PRESS
                            event_type_out = (
                                KeyEventType.RELEASE if long_sent_snapshot
                                else KeyEventType.SHORT_PRESS
                            )
                            import threading
                            thread_name = threading.current_thread().name
                            logger.info(f"🔑 PTT: keyUp → {event_type_out.value}, duration={duration:.3f}s, _long_sent={long_sent_snapshot}, thread={thread_name}")
                            logger.debug(f"Quartz keyUp: duration={duration:.3f}s, _long_sent={long_sent_snapshot} → {event_type_out.value}")

                        ev = KeyEvent(
                            key=self.key_to_monitor,
                            event_type=event_type_out,
                            timestamp=now,
                            duration=duration,
                        )
                        self._trigger_event(event_type_out, duration, ev)

                    return event
                except Exception as e:
                    logger.error(f"❌ Ошибка в tap callback: {e}")
                    return event

            # Маска событий: keyDown, keyUp для обычных клавиш, flagsChanged для модификаторов (Shift, Ctrl, Alt)
            event_mask = (1 << kCGEventKeyDown) | (1 << kCGEventKeyUp) | (1 << kCGEventFlagsChanged)
            
            tap_option = kCGEventTapOptionDefault if self._is_combo else kCGEventTapOptionListenOnly
            self._tap = CGEventTapCreate(
                kCGHIDEventTap,
                kCGHeadInsertEventTap,
                tap_option,
                event_mask,
                _tap_callback,
                None,
            )

            if not self._tap:
                logger.error("❌ Не удалось создать CGEventTap — проверьте Accessibility/Input Monitoring")
                logger.error("❌ КРИТИЧНО: CGEventTap вернул None!")
                logger.error("❌ Это означает, что приложению НЕ выданы разрешения:")
                logger.error("❌   1. System Settings > Privacy & Security > Accessibility")
                logger.error("❌   2. System Settings > Privacy & Security > Input Monitoring")
                logger.error("❌ Добавьте 'Nexy' в оба списка и перезапустите приложение")
                print("❌ Не удалось создать CGEventTap — проверьте Accessibility/Input Monitoring")
                print("❌ КРИТИЧНО: CGEventTap вернул None!")
                print("❌ Это означает, что приложению НЕ выданы разрешения:")
                print("❌   1. System Settings > Privacy & Security > Accessibility")
                print("❌   2. System Settings > Privacy & Security > Input Monitoring")
                print("❌ Добавьте 'Nexy' в оба списка и перезапустите приложение")
                self.keyboard_available = False
                return False

            print(f"✅ CGEventTap создан успешно: {self._tap}")  # Для отладки
            logger.info(f"✅ CGEventTap создан успешно: {self._tap}")

            self._tap_source = CFMachPortCreateRunLoopSource(None, self._tap, 0)
            print(f"✅ CFRunLoopSource создан: {self._tap_source}")  # Для отладки
            logger.info(f"✅ CFRunLoopSource создан: {self._tap_source}")

            # Добавляем в главный run loop (AppKit)
            # Важно: сохранить ссылку на callback, иначе он может быть собран GC
            # КРИТИЧНО: Используем kCFRunLoopCommonModes вместо kCFRunLoopDefaultMode
            # для обработки событий даже когда приложение неактивно (не frontmost)
            self._tap_callback = _tap_callback  # type: ignore[attr-defined]
            main_loop = CFRunLoopGetMain()
            print(f"✅ Добавляем source в главный run loop: {main_loop}")  # Для отладки
            CFRunLoopAddSource(main_loop, self._tap_source, kCFRunLoopCommonModes)
            print(f"✅ Source добавлен в run loop (kCFRunLoopCommonModes)")  # Для отладки
            CGEventTapEnable(self._tap, True)
            print(f"✅ CGEventTap включен для keycode={self._target_keycode}")  # Для отладки
            logger.info(f"QuartzMonitor: CGEventTap включен для keycode={self._target_keycode}")
            
            # ✅ FIX: Проверяем активность tap после включения
            try:
                is_enabled = CGEventTapIsEnabled(self._tap)
                logger.info(f"🔍 [TAP] CGEventTap активен: {is_enabled}")
                if not is_enabled:
                    logger.warning("⚠️ [TAP] CGEventTap создан, но НЕ активен! Возможно, нет разрешений.")
            except Exception as e:
                logger.warning(f"⚠️ [TAP] Не удалось проверить активность tap: {e}")

            # Запускаем поток мониторинга удержания (для long press)
            self.stop_event.clear()
            self.hold_monitor_thread = threading.Thread(
                target=self._run_hold_monitor,
                name="QuartzHoldMonitor",
                daemon=True,
            )
            self.hold_monitor_thread.start()
            
            # ✅ FIX: Запускаем поток мониторинга активности tap
            self._tap_monitor_thread = threading.Thread(
                target=self._monitor_tap_activity,
                name="QuartzTapMonitor",
                daemon=True,
            )
            self._tap_monitor_thread.start()

            self.is_monitoring = True
            logger.info("🎹 Quartz-монитор клавиатуры запущен")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка запуска Quartz-монитора: {e}")
            self.is_monitoring = False
            return False

    def stop_monitoring(self):
        if not self.is_monitoring:
            return
        try:
            self.is_monitoring = False
            self.stop_event.set()
            if self.hold_monitor_thread and self.hold_monitor_thread.is_alive():
                self.hold_monitor_thread.join(timeout=2.0)

            # ✅ FIX: Останавливаем поток мониторинга активности tap
            if self._tap_monitor_thread and self._tap_monitor_thread.is_alive():
                self.stop_event.set()
                self._tap_monitor_thread.join(timeout=1.0)
                self._tap_monitor_thread = None

            if self._tap_source:
                try:
                    CFRunLoopSourceInvalidate(self._tap_source)
                except Exception:
                    pass
                self._tap_source = None

            if self._tap:
                try:
                    CGEventTapEnable(self._tap, False)
                except Exception:
                    pass
                self._tap = None

            logger.info("🛑 Quartz-монитор клавиатуры остановлен")
        except Exception as e:
            logger.error(f"❌ Ошибка остановки Quartz-монитора: {e}")

    def _monitor_tap_activity(self):
        """Мониторит активность event tap и перезапускает если он стал неактивным"""
        while not self.stop_event.is_set():
            try:
                # ✅ FIX: Защищаем доступ к _tap блокировкой
                with self.state_lock:
                    tap_ref = self._tap
                
                if tap_ref is not None:
                    try:
                        is_enabled = CGEventTapIsEnabled(tap_ref)
                        if not is_enabled:
                            logger.warning("⚠️ [TAP] CGEventTap стал неактивным! Пытаемся перезапустить...")
                            # Пытаемся перезапустить tap
                            with self.state_lock:
                                # Проверяем, что tap всё ещё тот же (не был заменён в stop_monitoring)
                                if self._tap == tap_ref:
                                    CGEventTapEnable(self._tap, True)
                                    time.sleep(0.1)  # Небольшая задержка
                                    is_enabled_after = CGEventTapIsEnabled(self._tap)
                                    if is_enabled_after:
                                        logger.info("✅ [TAP] CGEventTap успешно перезапущен")
                                    else:
                                        logger.error("❌ [TAP] Не удалось перезапустить CGEventTap. Проверьте разрешения.")
                    except Exception as e:
                        logger.debug(f"⚠️ [TAP] Ошибка проверки активности: {e}")
                
                # Проверяем каждые 5 секунд
                time.sleep(5.0)
            except Exception as e:
                logger.error(f"❌ Ошибка в мониторе активности tap: {e}")
                time.sleep(1.0)

    def _run_hold_monitor(self):
        while not self.stop_event.is_set():
            try:
                with self.state_lock:
                    # ЗАЩИТА ОТ ЗАЛИПАНИЯ: Проверка таймаутов для сброса состояния
                    self._check_and_reset_stuck_state()
                    
                    # Для комбинации используем combo_active, для одиночной клавиши - key_pressed
                    is_active = self._combo_active if self._is_combo else self.key_pressed
                    start_time = self._combo_start_time if self._is_combo else self.press_start_time
                    
                    if is_active and start_time:
                        duration = time.time() - start_time
                        if not self._long_sent and duration >= self.long_press_threshold:
                            # КРИТИЧНО: Проверяем еще раз, что комбинация/клавиша все еще активна
                            is_still_active = self._combo_active if self._is_combo else self.key_pressed
                            if not is_still_active or not start_time:
                                logger.debug(f"HOLD_MONITOR: комбинация/клавиша была отпущена во время проверки, пропускаем LONG_PRESS")
                                continue

                            import threading
                            thread_name = threading.current_thread().name
                            logger.info(f"🔑 PTT: LONG_PRESS triggered! duration={duration:.3f}s, threshold={self.long_press_threshold}, thread={thread_name}")
                            logger.debug(f"HOLD_MONITOR: _long_sent={self._long_sent} → True, event_type=LONG_PRESS")
                            ev = KeyEvent(
                                key=self.key_to_monitor,
                                event_type=KeyEventType.LONG_PRESS,
                                timestamp=time.time(),
                                duration=duration,
                            )
                            self._trigger_event(KeyEventType.LONG_PRESS, duration, ev)
                            self._long_sent = True
                time.sleep(self.hold_check_interval)
            except Exception as e:
                logger.error(f"❌ Ошибка в мониторе удержания: {e}")
                time.sleep(0.1)
    
    def _check_and_reset_stuck_state(self):
        """Проверяет и сбрасывает залипшее состояние на основе таймаутов
        
        ✅ ПЛАН: Watchdog для защиты от залипания состояний
        Вызывается регулярно из _run_hold_monitor для проверки таймаутов
        """
        if not self._is_combo:
            return  # Для одиночных клавиш проверка не нужна (уже есть в hold_monitor)
        
        now = time.time()
        
        # ✅ ПЛАН: Проверка таймаута для комбинации
        if self._combo_active and self._combo_start_time:
            combo_duration = now - self._combo_start_time
            if combo_duration > self.combo_timeout_sec:
                logger.warning(
                    f"⚠️ [WATCHDOG] ЗАЛИПАНИЕ: Комбинация активна слишком долго ({combo_duration:.1f}s > {self.combo_timeout_sec}s), "
                    f"принудительно сбрасываем состояние"
                )
                self._reset_stuck_combo_state("combo_timeout")
                return
        
        # ✅ FIX: Проверка таймаута для Control (если зажат без событий)
        # КРИТИЧНО: Control использует flagsChanged, который НЕ генерирует повторные события при удержании
        # Поэтому проверяем таймаут только если комбинация НЕ активна
        # Если комбинация активна и N получает автоповтор - это означает, что Control реально зажат
        # Увеличиваем таймаут до 10 секунд для Control (в 2 раза), т.к. модификаторы не генерируют повторные события
        if self._control_pressed and self._control_last_event_time:
            time_since_event = now - self._control_last_event_time
            # ✅ FIX: Увеличиваем таймаут для Control, но также проверяем реальное состояние через Quartz
            timeout = self.key_state_timeout_sec * 2  # 10 секунд вместо 5
            
            # ✅ FIX: Проверяем реальное состояние Control через Quartz API
            try:
                from Quartz import CGEventSourceSecondsSinceLastEventType, kCGEventSourceStateHIDSystemState
                last_event_time = CGEventSourceSecondsSinceLastEventType(kCGEventSourceStateHIDSystemState, kCGEventFlagsChanged)
                # Если последнее событие flagsChanged было очень давно, возможно Control залип
                if last_event_time > timeout:
                    logger.debug(f"🔍 Quartz: последнее flagsChanged было {last_event_time:.1f}s назад")
            except Exception:
                pass
            
            if time_since_event > timeout:
                logger.warning(
                    f"⚠️ ЗАЛИПАНИЕ: Control зажат без событий слишком долго ({time_since_event:.1f}s > {timeout}s), "
                    f"combo_active={self._combo_active}, принудительно сбрасываем"
                )
                self._control_pressed = False
                self._previous_control_pressed = False  # ✅ FIX: Сбрасываем предыдущее состояние
                self._control_last_event_time = None
                self._update_combo_state()
        
        # Проверка таймаута для N (если зажата без событий)
        # КРИТИЧНО: Проверяем только если комбинация НЕ активна или нет автоповтора
        # Если комбинация активна, автоповтор N обновляет _n_last_event_time, поэтому залипания быть не должно
        if self._n_pressed and self._n_last_event_time:
            time_since_event = now - self._n_last_event_time
            # Увеличиваем таймаут для активной комбинации (автоповтор может быть реже)
            timeout = self.key_state_timeout_sec * 2 if self._combo_active else self.key_state_timeout_sec
            if time_since_event > timeout:
                logger.warning(
                    f"⚠️ ЗАЛИПАНИЕ: N зажата без событий слишком долго ({time_since_event:.1f}s > {timeout}s), "
                    f"combo_active={self._combo_active}, принудительно сбрасываем"
                )
                self._n_pressed = False
                self._n_last_event_time = None
                self._update_combo_state()
    
    def _reset_stuck_combo_state(self, reason: str):
        """Сбрасывает залипшее состояние комбинации
        
        ✅ ПЛАН: Watchdog сброс всех состояний при залипании
        """
        now = time.time()
        was_active = self._combo_active
        was_control = self._control_pressed
        was_n = self._n_pressed
        was_long = self._long_sent
        
        logger.warning(
            f"🔄 [WATCHDOG] Сброс залипшего состояния комбинации (причина: {reason})"
        )
        logger.debug(
            f"🔄 [WATCHDOG] Состояние до сброса: combo_active={was_active}, "
            f"control_pressed={was_control}, n_pressed={was_n}, long_sent={was_long}"
        )
        
        # ✅ ПЛАН: Сбрасываем все состояния
        self._combo_active = False
        self._combo_start_time = None
        self._control_pressed = False
        self._previous_control_pressed = False  # ✅ FIX: Сбрасываем предыдущее состояние
        self._n_pressed = False
        self._control_last_event_time = None
        self._n_last_event_time = None
        self.key_pressed = False
        self.press_start_time = None
        self._long_sent = False
        self._event_processed = False
        self._last_event_timestamp = 0.0
        
        logger.debug(
            f"✅ [WATCHDOG] Все состояния сброшены: combo_active=False, "
            f"control_pressed=False, n_pressed=False, long_sent=False"
        )
        
        # Если комбинация была активна, генерируем RELEASE событие
        if was_active:
            logger.info(f"🔄 [WATCHDOG] Генерируем RELEASE событие для активной комбинации")
            ev = KeyEvent(
                key=self.key_to_monitor,
                event_type=KeyEventType.RELEASE,
                timestamp=now,
                duration=0.0,
            )
            self._trigger_event(KeyEventType.RELEASE, 0.0, ev)

    def _trigger_event(self, event_type: KeyEventType, duration: float, event: Optional[KeyEvent] = None):
        try:
            callback = self.event_callbacks.get(event_type)
            if not callback:
                return
            if event is None:
                event = KeyEvent(
                    key=self.key_to_monitor,
                    event_type=event_type,
                    timestamp=time.time(),
                    duration=duration,
                )

            import threading
            thread_name = threading.current_thread().name
            logger.debug(f"🔑 _trigger_event: type={event_type.value}, duration={duration:.3f}s, thread={thread_name}")
            threading.Thread(target=lambda: self._run_callback(callback, event), daemon=True).start()
        except Exception as e:
            logger.error(f"❌ Ошибка запуска события: {e}")

    def _run_callback(self, callback: Callable, event: KeyEvent):
        try:
            logger.info(f"🔑 _run_callback: {event.event_type.value}, callback={callback.__name__ if hasattr(callback, '__name__') else 'unknown'}")
            print(f"🔑 _run_callback: {event.event_type.value}, callback={callback.__name__ if hasattr(callback, '__name__') else 'unknown'}")  # Для отладки
            
            import inspect
            if inspect.iscoroutinefunction(callback):
                # ИСПРАВЛЕНО: Всегда используем основной loop через run_coroutine_threadsafe
                # Это гарантирует, что события попадут в правильный EventBus
                if self._loop:
                    try:
                        logger.info(f"🔑 Выполняем async callback в loop: {event.event_type.value} (loop={id(self._loop)}, running={self._loop.is_running()})")
                        print(f"🔑 Выполняем async callback в loop: {event.event_type.value} (loop={id(self._loop)}, running={self._loop.is_running()})")
                        future = asyncio.run_coroutine_threadsafe(callback(event), self._loop)
                        # Fire-and-forget: не блокируем поток клавиатуры
                        # Добавляем callback для логирования завершения/ошибок
                        def _on_done(f):
                            try:
                                f.result()  # Проверяем на исключения
                                logger.info(f"✅ Async callback {event.event_type.value} completed successfully")
                                print(f"✅ Async callback {event.event_type.value} completed successfully")
                            except Exception as e:
                                logger.error(f"❌ Async callback {event.event_type.value} failed: {e}", exc_info=True)
                                print(f"❌ Async callback {event.event_type.value} failed: {e}")
                        future.add_done_callback(_on_done)
                    except Exception as e:
                        logger.error(f"❌ Ошибка постинга async callback в loop: {e}", exc_info=True)
                        print(f"❌ Ошибка постинга async callback в loop: {e}")
                else:
                    # Fallback: если loop не установлен, пытаемся выполнить в новом loop
                    logger.warning("⚠️ Loop не установлен, создаем временный (события могут не дойти до EventBus)")
                    asyncio.run(callback(event))
            else:
                logger.info(f"🔑 Выполняем sync callback: {event.event_type.value}")
                print(f"🔑 Выполняем sync callback: {event.event_type.value}")  # Для отладки
                callback(event)
        except Exception as e:
            logger.error(f"❌ Ошибка выполнения callback: {e}")

    def get_status(self) -> Dict[str, Any]:
        with self.state_lock:
            status = {
                "is_monitoring": self.is_monitoring,
                "keyboard_available": self.keyboard_available,
                "fallback_mode": False,
                "config": {
                    "key": self.key_to_monitor,
                    "short_press_threshold": self.short_press_threshold,
                    "long_press_threshold": self.long_press_threshold,
                },
                "callbacks_registered": len(self.event_callbacks),
                "backend": "quartz",
            }
            
            if self._is_combo:
                status["combo_active"] = self._combo_active
                status["control_pressed"] = self._control_pressed
                status["n_pressed"] = self._n_pressed
            else:
                status["key_pressed"] = self.key_pressed
            
            return status
