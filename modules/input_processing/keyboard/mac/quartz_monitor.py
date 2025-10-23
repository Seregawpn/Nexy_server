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
        CFRunLoopAddSource,
        CFRunLoopGetCurrent,
        CFRunLoopGetMain,
        CFRunLoopRunInMode,
        CFRunLoopSourceInvalidate,
        CFMachPortCreateRunLoopSource,
        kCGHIDEventTap,
        kCGHeadInsertEventTap,
        kCGEventTapOptionListenOnly,
        kCGEventKeyDown,
        kCGEventKeyUp,
        kCFRunLoopCommonModes,
        kCFRunLoopDefaultMode,
        CGEventGetIntegerValueField,
        kCGKeyboardEventKeycode,
    )
    QUARTZ_AVAILABLE = True
except Exception as e:  # pragma: no cover
    QUARTZ_AVAILABLE = False

from ..types import KeyEvent, KeyEventType, KeyboardConfig

logger = logging.getLogger(__name__)


class QuartzKeyboardMonitor:
    """Глобальный монитор клавиатуры на macOS через Quartz Event Tap."""

    # Минимальная карта key_to_monitor -> keycode (US). Сейчас нужен только пробел.
    KEYCODES = {
        "space": 49,
        # При необходимости можно расширить: enter(36), esc(53), shift(56/60), ctrl(59/62), alt(58/61)
    }

    def __init__(self, config: KeyboardConfig):
        self.config = config
        self.key_to_monitor = config.key_to_monitor
        self.short_press_threshold = config.short_press_threshold
        self.long_press_threshold = config.long_press_threshold
        self.event_cooldown = config.event_cooldown
        self.hold_check_interval = config.hold_check_interval

        # Состояние
        self.is_monitoring = False
        self.key_pressed = False
        self.press_start_time: Optional[float] = None
        self.last_event_time = 0.0
        self._long_sent = False

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

        # Доступность
        self.keyboard_available = QUARTZ_AVAILABLE
        if not QUARTZ_AVAILABLE:
            logger.warning("⚠️ Quartz недоступен — нативный монитор клавиатуры отключен")

        # Целевой keycode
        self._target_keycode = self.KEYCODES.get(self.key_to_monitor, None)
        if self._target_keycode is None:
            logger.warning(f"⚠️ Неподдерживаемая клавиша для Quartz: {self.key_to_monitor}")
            self.keyboard_available = False

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
        logger.debug("QuartzMonitor: установлен event loop для async-колбэков")

    def start_monitoring(self) -> bool:
        if not self.keyboard_available:
            logger.warning("⚠️ Клавиатурный Quartz-монитор недоступен")
            print("⚠️ Клавиатурный Quartz-монитор недоступен")
            return False
        if self.is_monitoring:
            logger.warning("⚠️ Мониторинг уже запущен")
            return False

        # КРИТИЧНО: Проверяем разрешения ПЕРЕД созданием event tap
        logger.info("🔐 Проверяем разрешения для Quartz Event Tap...")
        print("🔐 Проверяем разрешения для Quartz Event Tap...")

        try:
            from ApplicationServices import AXIsProcessTrusted
            has_accessibility = AXIsProcessTrusted()
            logger.info(f"🔐 Accessibility permission: {has_accessibility}")
            print(f"🔐 Accessibility permission: {has_accessibility}")

            if not has_accessibility:
                logger.error("❌ Accessibility разрешения НЕ выданы!")
                logger.error("❌ Перейдите в: System Settings > Privacy & Security > Accessibility")
                logger.error("❌ Добавьте Nexy.app и включите переключатель")
                print("❌ Accessibility разрешения НЕ выданы!")
                print("❌ Перейдите в: System Settings > Privacy & Security > Accessibility")
                print("❌ Добавьте Nexy.app и включите переключатель")
                # Не блокируем создание event tap - позволяем CGEventTapCreate вернуть None
        except Exception as e:
            logger.warning(f"⚠️ Не удалось проверить Accessibility permissions: {e}")
            print(f"⚠️ Не удалось проверить Accessibility permissions: {e}")

        try:
            # Создаем Event Tap
            def _tap_callback(proxy, event_type, event, refcon):
                try:
                    logger.debug(f"🔍 Quartz tap вызван: event_type={event_type}")

                    if event_type not in (kCGEventKeyDown, kCGEventKeyUp):
                        return event

                    keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
                    logger.debug(f"🔍 Keycode={keycode}, target={self._target_keycode}")

                    if keycode != self._target_keycode:
                        return event

                    logger.debug(f"🔑 Целевая клавиша обнаружена! keycode={keycode}")

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
                            if not self.key_pressed:
                                return event
                            duration = now - (self.press_start_time or now)

                            # КРИТИЧНО: Сбрасываем состояние ПОСЛЕ определения типа события,
                            # но ДО вызова _trigger_event, чтобы hold_monitor прекратил работу
                            long_sent_snapshot = self._long_sent
                            self.key_pressed = False
                            self.press_start_time = None
                            self.last_event_time = now

                            # Если уже отправили LONG_PRESS — это RELEASE
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

            self._tap = CGEventTapCreate(
                kCGHIDEventTap,
                kCGHeadInsertEventTap,
                kCGEventTapOptionListenOnly,
                (1 << kCGEventKeyDown) | (1 << kCGEventKeyUp),
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

            self._tap_source = CFMachPortCreateRunLoopSource(None, self._tap, 0)

            # Добавляем в главный run loop (AppKit)
            # Важно: сохранить ссылку на callback, иначе он может быть собран GC
            self._tap_callback = _tap_callback  # type: ignore[attr-defined]
            CFRunLoopAddSource(CFRunLoopGetMain(), self._tap_source, kCFRunLoopDefaultMode)
            CGEventTapEnable(self._tap, True)
            logger.info(f"QuartzMonitor: CGEventTap включен для keycode={self._target_keycode}")

            # Запускаем поток мониторинга удержания (для long press)
            self.stop_event.clear()
            self.hold_monitor_thread = threading.Thread(
                target=self._run_hold_monitor,
                name="QuartzHoldMonitor",
                daemon=True,
            )
            self.hold_monitor_thread.start()

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

    def _run_hold_monitor(self):
        while not self.stop_event.is_set():
            try:
                with self.state_lock:
                    if self.key_pressed and self.press_start_time:
                        duration = time.time() - self.press_start_time
                        if not self._long_sent and duration >= self.long_press_threshold:
                            # КРИТИЧНО: Проверяем еще раз, что клавиша все еще нажата
                            # (keyUp мог произойти между проверкой и этой строкой)
                            if not self.key_pressed or not self.press_start_time:
                                logger.debug(f"HOLD_MONITOR: клавиша была отпущена во время проверки, пропускаем LONG_PRESS")
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
                        logger.info(f"🔑 Выполняем async callback в loop: {event.event_type.value}")
                        print(f"🔑 Выполняем async callback в loop: {event.event_type.value}")  # Для отладки
                        future = asyncio.run_coroutine_threadsafe(callback(event), self._loop)
                        # Опционально: можно дождаться выполнения с таймаутом
                        # future.result(timeout=5.0)
                    except Exception as e:
                        logger.error(f"❌ Ошибка постинга async callback в loop: {e}")
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
            return {
                "is_monitoring": self.is_monitoring,
                "key_pressed": self.key_pressed,
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
