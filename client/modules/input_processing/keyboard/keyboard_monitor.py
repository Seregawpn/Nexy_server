"""
Мониторинг клавиатуры - рефакторинг из improved_input_handler.py
"""

import asyncio
import logging
import threading
import time
from typing import Any, Callable

from .types import KeyboardConfig, KeyEvent, KeyEventType

logger = logging.getLogger(__name__)


class KeyboardMonitor:
    """Мониторинг клавиатуры с поддержкой различных типов нажатий"""

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
        self.press_start_time = None
        self.last_event_time = 0
        self._long_sent = False  # Флаг для предотвращения повторных LONG_PRESS

        # Threading
        self.monitor_thread = None
        self.hold_monitor_thread = None
        self.stop_event = threading.Event()
        self.state_lock = threading.RLock()

        # Callbacks
        self.event_callbacks: dict[KeyEventType, Callable[[KeyEvent], Any]] = {}

        # Event loop для async колбэков
        self._loop: asyncio.AbstractEventLoop | None = None

        # Fallback режим
        self.fallback_mode = False
        self.keyboard_available = True

        # Состояние для комбинации Control+N
        self._is_combo = self.key_to_monitor == "ctrl_n"
        self._control_pressed = False
        self._n_pressed = False
        self._combo_active = False
        self._combo_start_time: float | None = None
        self._other_modifier_pressed = False

        # pynput будет импортирован лениво в start_monitoring()
        # чтобы не триггерить проверку Accessibility при создании объекта
        self.keyboard = None

    def _init_keyboard(self):
        """
        Инициализирует клавиатуру (lazy import).

        ВАЖНО: pynput при импорте вызывает AXIsProcessTrustedWithOptions,
        что триггерит проверку Accessibility. Поэтому импортируем только
        когда start_monitoring() вызван (после получения всех разрешений).
        """
        if self.keyboard is not None:
            return  # Уже инициализировано

        try:
            import pynput.keyboard as keyboard

            self.keyboard = keyboard
            self.keyboard_available = True
            logger.info("✅ Клавиатура инициализирована (pynput загружен)")
        except ImportError as e:
            logger.warning(f"⚠️ pynput недоступен: {e}")
            self.keyboard_available = False
            self.fallback_mode = True
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации клавиатуры: {e}")
            self.keyboard_available = False

    def start_monitoring(self):
        """Начинает мониторинг клавиатуры"""
        # Lazy init: импортируем pynput только сейчас
        self._init_keyboard()

        if not self.keyboard_available:
            logger.warning("⚠️ Клавиатура недоступна, мониторинг не запущен")
            return False

        if self.is_monitoring:
            logger.warning("⚠️ Мониторинг уже запущен")
            return False

        try:
            self.is_monitoring = True
            self.stop_event.clear()

            # Запускаем поток мониторинга
            self.monitor_thread = threading.Thread(
                target=self._run_keyboard_listener, name="KeyboardMonitor", daemon=True
            )
            self.monitor_thread.start()

            # Запускаем поток мониторинга удержания
            self.hold_monitor_thread = threading.Thread(
                target=self._run_hold_monitor, name="HoldMonitor", daemon=True
            )
            self.hold_monitor_thread.start()

            logger.info("🎹 Мониторинг клавиатуры запущен")
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка запуска мониторинга: {e}")
            self.is_monitoring = False
            return False

    def stop_monitoring(self):
        """Останавливает мониторинг клавиатуры"""
        if not self.is_monitoring:
            return

        try:
            self.is_monitoring = False
            self.stop_event.set()

            # Ждем завершения потоков
            if self.monitor_thread and self.monitor_thread.is_alive():
                self.monitor_thread.join(timeout=2.0)

            if self.hold_monitor_thread and self.hold_monitor_thread.is_alive():
                self.hold_monitor_thread.join(timeout=2.0)

            logger.info("🛑 Мониторинг клавиатуры остановлен")

        except Exception as e:
            logger.error(f"❌ Ошибка остановки мониторинга: {e}")

    def register_callback(
        self, event_type: KeyEventType | str, callback: Callable[[KeyEvent], Any]
    ) -> None:
        """Регистрирует callback для типа события"""
        # Поддерживаем как KeyEventType, так и строки
        if isinstance(event_type, str):
            # Конвертируем строку в KeyEventType
            try:
                event_type = KeyEventType(event_type)
            except ValueError:
                logger.warning(f"⚠️ Неизвестный тип события: {event_type}")
                return

        self.event_callbacks[event_type] = callback
        logger.debug(f"📝 Зарегистрирован callback для {event_type.value}")

    def set_loop(self, loop: asyncio.AbstractEventLoop):
        """Устанавливает event loop для async колбэков"""
        self._loop = loop
        logger.debug("🔄 Event loop установлен для KeyboardMonitor")

    def _run_keyboard_listener(self) -> None:
        """Запускает listener клавиатуры"""
        try:
            keyboard = self.keyboard
            if keyboard is None:
                logger.error("❌ Keyboard listener unavailable: keyboard backend not initialized")
                return
            with keyboard.Listener(
                on_press=self._on_key_press, on_release=self._on_key_release
            ) as listener:
                listener.join()
        except Exception as e:
            logger.error(f"❌ Ошибка в listener клавиатуры: {e}")

    def _run_hold_monitor(self):
        """Мониторит удержание клавиши"""
        while not self.stop_event.is_set():
            try:
                with self.state_lock:
                    # Для комбинации используем combo_active, для одиночной клавиши - key_pressed
                    is_active = self._combo_active if self._is_combo else self.key_pressed
                    start_time = self._combo_start_time if self._is_combo else self.press_start_time

                    if is_active and start_time:
                        duration = time.time() - start_time

                        # Проверяем долгое нажатие (только один раз!)
                        if not self._long_sent and duration >= self.long_press_threshold:
                            # Проверяем еще раз, что комбинация/клавиша все еще активна
                            is_still_active = (
                                self._combo_active if self._is_combo else self.key_pressed
                            )
                            if not is_still_active or not start_time:
                                continue

                            logger.info(
                                f"🔑 HOLD_MONITOR: LONG_PRESS triggered! duration={duration:.3f}s, threshold={self.long_press_threshold}"
                            )
                            print(
                                f"🔑 HOLD_MONITOR: LONG_PRESS triggered! duration={duration:.3f}s, threshold={self.long_press_threshold}"
                            )  # Для отладки
                            self._trigger_event(KeyEventType.LONG_PRESS, duration)
                            self._long_sent = True  # Предотвращаем повторные срабатывания

                time.sleep(self.hold_check_interval)

            except Exception as e:
                logger.error(f"❌ Ошибка в мониторе удержания: {e}")
                time.sleep(0.1)

    def _on_key_press(self, key: Any) -> None:
        """Обработка нажатия клавиши"""
        try:
            current_time = time.time()

            if self._is_combo:
                # Обработка комбинации Control+N
                with self.state_lock:
                    # Определяем, какая клавиша нажата
                    is_control = self._is_control_key(key)
                    is_n = self._is_n_key(key)

                    if is_control:
                        if self._control_pressed:
                            return  # Игнорируем повторные нажатия
                        self._control_pressed = True
                    elif self._is_other_modifier_key(key):
                        self._other_modifier_pressed = True
                        return
                    elif is_n:
                        # Cooldown только для keyDown N
                        if current_time - self.last_event_time < self.event_cooldown:
                            return
                        if self._n_pressed:
                            return  # Игнорируем автоповтор N
                        self._n_pressed = True
                        self.last_event_time = current_time
                    else:
                        return  # Не наша клавиша

                    # Обновляем состояние комбинации
                    self._update_combo_state()
            else:
                # Обработка одиночной клавиши (left_control)
                # Проверяем cooldown
                if current_time - self.last_event_time < self.event_cooldown:
                    return

                # Проверяем, что это наша клавиша
                if not self._is_target_key(key):
                    return

                with self.state_lock:
                    # Если клавиша уже нажата, игнорируем
                    if self.key_pressed:
                        return

                    self.key_pressed = True
                    self.press_start_time = current_time
                    self._long_sent = False  # Сбрасываем флаг для нового нажатия

                # Создаем событие нажатия
                event = KeyEvent(
                    key=self._key_to_string(key),
                    event_type=KeyEventType.PRESS,
                    timestamp=current_time,
                )

                self._trigger_event(KeyEventType.PRESS, 0.0, event)
                logger.debug(f"🔑 Клавиша нажата: {self._key_to_string(key)}")

        except Exception as e:
            logger.error(f"❌ Ошибка обработки нажатия: {e}")

    def _on_key_release(self, key: Any) -> None:
        """Обработка отпускания клавиши"""
        try:
            current_time = time.time()

            if self._is_combo:
                # Обработка комбинации Control+N
                with self.state_lock:
                    # Определяем, какая клавиша отпущена
                    is_control = self._is_control_key(key)
                    is_n = self._is_n_key(key)

                    if is_control:
                        if not self._control_pressed:
                            return
                        self._control_pressed = False
                    elif self._is_other_modifier_key(key):
                        self._other_modifier_pressed = False
                        return
                    elif is_n:
                        if not self._n_pressed:
                            return
                        self._n_pressed = False
                    else:
                        return  # Не наша клавиша

                    # Обновляем состояние комбинации
                    self._update_combo_state()
            else:
                # Обработка одиночной клавиши (left_control)
                # Проверяем, что это наша клавиша
                if not self._is_target_key(key):
                    return

                with self.state_lock:
                    if not self.key_pressed:
                        return

                    duration = current_time - self.press_start_time if self.press_start_time else 0

                    # КРИТИЧНО: Сбрасываем состояние СРАЗУ, чтобы hold_monitor не отправил LONG_PRESS
                    self.key_pressed = False
                    self.press_start_time = None

                    # Определяем тип события
                    if duration < self.short_press_threshold:
                        event_type = KeyEventType.SHORT_PRESS
                    else:
                        event_type = KeyEventType.RELEASE

                    # Создаем событие
                    event = KeyEvent(
                        key=self._key_to_string(key),
                        event_type=event_type,
                        timestamp=current_time,
                        duration=duration,
                    )

                    self._trigger_event(event_type, duration, event)

                    # Обновляем время последнего события
                    self.last_event_time = current_time

                logger.debug(
                    f"🔑 Клавиша отпущена: {self._key_to_string(key)} (длительность: {duration:.3f}s)"
                )

        except Exception as e:
            logger.error(f"❌ Ошибка обработки отпускания: {e}")

    def _update_combo_state(self):
        """Обновляет состояние комбинации Control+N и генерирует события при изменениях"""
        now = time.time()
        was_active = self._combo_active
        should_be_active = (
            self._control_pressed and self._n_pressed and (not self._other_modifier_pressed)
        )

        if should_be_active and not was_active:
            # Активация комбинации: обе клавиши зажаты
            self._combo_active = True
            self._combo_start_time = now
            self._long_sent = False
            self.key_pressed = True  # Для совместимости с hold_monitor
            self.press_start_time = now

            logger.info("✅ Control+N комбинация активирована (pynput)")
            event = KeyEvent(
                key=self.key_to_monitor,
                event_type=KeyEventType.PRESS,
                timestamp=now,
            )
            self._trigger_event(KeyEventType.PRESS, 0.0, event)

        elif not should_be_active and was_active:
            # Деактивация комбинации: одна из клавиш отпущена
            # КРИТИЧНО: Для комбинации ctrl_n всегда генерируем только RELEASE
            # "Short tap" вычисляется в input_processing_integration по длительности PRESS→RELEASE
            self._combo_active = False
            duration = now - (self._combo_start_time or now)
            self._combo_start_time = None

            long_sent_snapshot = self._long_sent
            self.key_pressed = False
            self.press_start_time = None
            self.last_event_time = now

            # КРИТИЧНО: Для комбинации ctrl_n всегда генерируем только RELEASE
            # Это устраняет гонку между SHORT_PRESS и RELEASE
            # "Short tap" будет вычисляться в input_processing_integration._handle_key_release
            # по длительности PRESS→RELEASE
            logger.debug(
                f"🔑 Combo deactivation (pynput): генерируем RELEASE (long_sent={long_sent_snapshot}, duration={duration:.3f}s)"
            )
            event = KeyEvent(
                key=self.key_to_monitor,
                event_type=KeyEventType.RELEASE,
                timestamp=now,
                duration=duration,
            )
            self._trigger_event(KeyEventType.RELEASE, duration, event)

    def _is_target_key(self, key: Any) -> bool:
        """Проверяет, является ли клавиша целевой"""
        try:
            if not self.keyboard_available:
                return False

            if self._is_combo:
                # Для комбинации проверяем отдельно Control и N
                if self._is_control_key(key):
                    return True
                if self._is_n_key(key):
                    return True
                return False

            if self.key_to_monitor == "left_control":
                keyboard = self.keyboard
                if keyboard is None:
                    return False
                return key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l)
            else:
                logger.warning(f"⚠️ Неподдерживаемая клавиша для pynput: {self.key_to_monitor}")
                return False

        except Exception as e:
            logger.error(f"❌ Ошибка проверки клавиши: {e}")
            return False

    def _key_to_string(self, key: Any) -> str:
        """Преобразует клавишу в строку"""
        try:
            if not self.keyboard_available:
                return "unknown"

            key_char = getattr(key, "char", None)
            if isinstance(key_char, str) and key_char:
                return key_char
            key_name = getattr(key, "name", None)
            if isinstance(key_name, str) and key_name:
                return key_name
            else:
                return str(key)

        except Exception as e:
            logger.error(f"❌ Ошибка преобразования клавиши: {e}")
            return "unknown"

    def _trigger_event(
        self, event_type: KeyEventType, duration: float, event: KeyEvent | None = None
    ) -> None:
        """Запускает событие"""
        try:
            callback = self.event_callbacks.get(event_type)
            if callback:
                if event is None:
                    event = KeyEvent(
                        key=self.key_to_monitor,
                        event_type=event_type,
                        timestamp=time.time(),
                        duration=duration,
                    )

                # Запускаем callback в отдельном потоке
                threading.Thread(
                    target=lambda: self._run_callback(callback, event), daemon=True
                ).start()

        except Exception as e:
            logger.error(f"❌ Ошибка запуска события: {e}")

    def _run_callback(self, callback: Callable[[KeyEvent], Any], event: KeyEvent) -> None:
        """Запуск callback с правильной обработкой async/sync функций"""
        try:
            import inspect

            # Проверяем, является ли callback корутиной
            if inspect.iscoroutinefunction(callback):
                # Если это корутина, планируем в основной event loop
                if self._loop and self._loop.is_running():
                    asyncio.run_coroutine_threadsafe(callback(event), self._loop)
                else:
                    # Fallback - создаем новый event loop
                    asyncio.run(callback(event))
            else:
                # Если это обычная функция, вызываем напрямую
                callback(event)

        except Exception as e:
            logger.error(f"❌ Ошибка выполнения callback: {e}")

    def _is_control_key(self, key: Any) -> bool:
        """Проверяет, что нажата одна из control-клавиш."""
        keyboard = self.keyboard
        if keyboard is None:
            return False
        return key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r)

    def _is_n_key(self, key: Any) -> bool:
        """Проверяет, что нажата клавиша N."""
        key_char = getattr(key, "char", None)
        if isinstance(key_char, str) and key_char.lower() == "n":
            return True
        key_name = getattr(key, "name", None)
        return isinstance(key_name, str) and key_name.lower() == "n"

    def _is_other_modifier_key(self, key: Any) -> bool:
        """Проверяет, что нажат модификатор кроме Control."""
        keyboard = self.keyboard
        if keyboard is None:
            return False
        candidates = [
            getattr(keyboard.Key, "alt", None),
            getattr(keyboard.Key, "alt_l", None),
            getattr(keyboard.Key, "alt_r", None),
            getattr(keyboard.Key, "cmd", None),
            getattr(keyboard.Key, "cmd_l", None),
            getattr(keyboard.Key, "cmd_r", None),
            getattr(keyboard.Key, "shift", None),
            getattr(keyboard.Key, "shift_l", None),
            getattr(keyboard.Key, "shift_r", None),
        ]
        return any(c is not None and key == c for c in candidates)

    def get_status(self) -> dict[str, Any]:
        """Возвращает статус мониторинга"""
        with self.state_lock:
            status = {
                "is_monitoring": self.is_monitoring,
                "keyboard_available": self.keyboard_available,
                "fallback_mode": self.fallback_mode,
                "config": {
                    "key": self.key_to_monitor,
                    "short_press_threshold": self.short_press_threshold,
                    "long_press_threshold": self.long_press_threshold,
                },
                "callbacks_registered": len(self.event_callbacks),
            }

            if self._is_combo:
                status["combo_active"] = self._combo_active
                status["control_pressed"] = self._control_pressed
                status["n_pressed"] = self._n_pressed
            else:
                status["key_pressed"] = self.key_pressed

            return status
