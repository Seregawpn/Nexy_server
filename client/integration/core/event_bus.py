"""
EventBus - Система событий для интеграции модулей
"""

import asyncio
from enum import Enum
import logging
import time
from typing import Any, Callable

logger = logging.getLogger(__name__)

class EventPriority(Enum):
    """Приоритеты событий"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class EventBus:
    """Система событий для интеграции модулей"""
    
    def __init__(self):
        self.subscribers: dict[str, list[dict[str, Any]]] = {}
        self.event_history: list[dict[str, Any]] = []
        self.max_history = 1000
        self._loop: asyncio.AbstractEventLoop | None = None
        # События, обработка которых должна быть быстрой (не блокирующей):
        # публикуем обработчики как задачи и не await'им их последовательно
        self._fast_events = {"app.mode_changed", "app.state_changed"}
        # Events to exclude from history (high-frequency)
        self._exclude_from_history = {"grpc.response.audio", "grpc.response.text"}
        self._background_tasks = set()  # Set to track fire-and-forget tasks
        # High-frequency events: sample debug logs to avoid log flood.
        self._debug_sample_events = {"grpc.response.audio"}
        self._debug_sample_interval_sec = 1.0
        self._debug_sample_state: dict[tuple[str, str], dict[str, float | int]] = {}

    def _debug_log_event(self, event_type: str, key: str, message: str):
        """Debug logging with sampling for high-frequency events."""
        if event_type not in self._debug_sample_events:
            logger.debug(message)
            return

        now = time.monotonic()
        state_key = (event_type, key)
        state = self._debug_sample_state.setdefault(state_key, {"last": 0.0, "suppressed": 0})
        last = float(state["last"])
        if (now - last) >= self._debug_sample_interval_sec:
            suppressed = int(state["suppressed"])
            state["last"] = now
            state["suppressed"] = 0
            if suppressed > 0:
                logger.debug(f"{message} [suppressed={suppressed}]")
            else:
                logger.debug(message)
            return

        state["suppressed"] = int(state["suppressed"]) + 1
    
    def _log_future_exception(self, fut, event_type: str, callback_name: str):
        """Callback to log exceptions from fire-and-forget futures."""
        try:
            exc = fut.exception()
            if exc:
                logger.error(f"❌ EventBus callback failed for '{event_type}' ({callback_name}): {exc}")
        except Exception:
            pass
    
    def attach_loop(self, loop: asyncio.AbstractEventLoop | None = None):
        """Зафиксировать основной event loop для безопасной доставки событий из любых потоков."""
        try:
            self._loop = loop or asyncio.get_running_loop()
            logger.debug(f"EventBus: attached loop={id(self._loop)} running={self._loop.is_running() if self._loop else False}")
        except Exception as e:
            logger.debug(f"EventBus: failed to attach loop: {e}")
            self._loop = None
    
    def get_loop(self) -> asyncio.AbstractEventLoop | None:
        """Получить прикрепленный event loop."""
        return self._loop
        
    async def subscribe(self, event_type: str, callback: Callable[..., Any], priority: EventPriority = EventPriority.MEDIUM):
        """Подписка на событие"""
        try:
            if event_type not in self.subscribers:
                self.subscribers[event_type] = []
            else:
                for sub in self.subscribers[event_type]:
                    if sub.get("callback") is callback:
                        logger.warning(f"⚠️ Duplicate subscription ignored: event_type={event_type}, callback={callback}")
                        return
            
            subscriber = {
                "callback": callback,
                "priority": priority,
                "event_type": event_type
            }
            
            self.subscribers[event_type].append(subscriber)
            
            # Сортируем по приоритету (высокий приоритет первым)
            self.subscribers[event_type].sort(key=lambda x: x["priority"].value, reverse=True)
            
            logger.info(f"📝 Подписка на событие: {event_type} (приоритет: {priority.name})")
            
        except Exception as e:
            logger.error(f"❌ Ошибка подписки на событие {event_type}: {e}")
    
    async def unsubscribe(self, event_type: str, callback: Callable[..., Any]):
        """Отписка от события"""
        try:
            if event_type in self.subscribers:
                self.subscribers[event_type] = [
                    sub for sub in self.subscribers[event_type] 
                    if sub["callback"] != callback
                ]
                
                if not self.subscribers[event_type]:
                    del self.subscribers[event_type]
                
                logger.info(f"📝 Отписка от события: {event_type}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка отписки от события {event_type}: {e}")
    
    async def publish(self, event_type: str, data: dict[str, Any] | None = None):
        """Публикация события"""
        try:
            if data is None:
                data = {}
            
            event = {
                "type": event_type,
                "data": data,
                "timestamp": asyncio.get_event_loop().time()
            }
            
            # Добавляем в историю (кроме high-frequency событий)
            if event_type not in self._exclude_from_history:
                self.event_history.append(event)
                if len(self.event_history) > self.max_history:
                    self.event_history.pop(0)
            
            # Уведомляем подписчиков
            subs_cnt = len(self.subscribers.get(event_type, []))
            if event_type == "app.mode_changed":
                logger.info(f"EventBus: '{event_type}' → subscribers={subs_cnt}, data={data}")
            self._debug_log_event(
                event_type,
                "dispatch",
                f"EventBus: dispatch '{event_type}' to {subs_cnt} subscriber(s)",
            )
            if event_type in self.subscribers:
                for subscriber in self.subscribers[event_type]:
                    cb = subscriber["callback"]
                    try:
                        if asyncio.iscoroutinefunction(cb):
                            # Быстрые события: не блокируем публикацию
                            if event_type in self._fast_events:
                                try:
                                    if self._loop and self._loop.is_running() and self._loop != asyncio.get_event_loop():
                                        fut = asyncio.run_coroutine_threadsafe(cb(event), self._loop)
                                        fut.add_done_callback(
                                            lambda f, et=event_type, cn=str(cb): self._log_future_exception(f, et, cn)
                                        )
                                        self._debug_log_event(
                                            event_type,
                                            "schedule_fast",
                                            f"EventBus: scheduled (fast) async on main loop '{event_type}': {cb}",
                                        )
                                    else:
                                        task = asyncio.create_task(cb(event))
                                        self._background_tasks.add(task)
                                        task.add_done_callback(self._background_tasks.discard)
                                        self._debug_log_event(
                                            event_type,
                                            "create_task_fast",
                                            f"EventBus: create_task (fast) for '{event_type}': {cb}",
                                        )
                                except Exception:
                                    # last resort — выполнить inline, чтобы не терять событие
                                    await cb(event)
                            else:
                                # Стандартный режим: сохраняем прежнюю семантику
                                if self._loop and self._loop.is_running() and self._loop != asyncio.get_event_loop():
                                    fut = asyncio.run_coroutine_threadsafe(cb(event), self._loop)
                                    fut.add_done_callback(
                                        lambda f, et=event_type, cn=str(cb): self._log_future_exception(f, et, cn)
                                    )
                                    self._debug_log_event(
                                        event_type,
                                        "schedule",
                                        f"EventBus: scheduled async callback on main loop for '{event_type}': {cb}",
                                    )
                                else:
                                    self._debug_log_event(
                                        event_type,
                                        "await_inline",
                                        f"EventBus: awaiting async callback inline for '{event_type}': {cb}",
                                    )
                                    await cb(event)
                        else:
                            # Синхронные колбэки вызываем напрямую (быстро и неблокирующе)
                            self._debug_log_event(
                                event_type,
                                "call_sync",
                                f"EventBus: calling sync callback for '{event_type}': {cb}",
                            )
                            cb(event)
                    except Exception as e:
                        logger.error(f"❌ Ошибка в обработчике события {event_type}: {e}")

            self._debug_log_event(event_type, "published", f"📢 Событие опубликовано: {event_type}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка публикации события {event_type}: {e}")
    
    def get_event_history(self, event_type: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        """Получить историю событий"""
        try:
            if event_type:
                filtered_history = [
                    event for event in self.event_history 
                    if event["type"] == event_type
                ]
            else:
                filtered_history = self.event_history
            
            return filtered_history[-limit:]
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения истории событий: {e}")
            return []
    
    def get_subscribers_count(self, event_type: str | None = None) -> int:
        """Получить количество подписчиков"""
        try:
            if event_type:
                return len(self.subscribers.get(event_type, []))
            else:
                return sum(len(subs) for subs in self.subscribers.values())
                
        except Exception as e:
            logger.error(f"❌ Ошибка подсчета подписчиков: {e}")
            return 0
    
    def get_status(self) -> dict[str, Any]:
        """Получить статус EventBus"""
        return {
            "subscribers_count": self.get_subscribers_count(),
            "event_types": list(self.subscribers.keys()),
            "history_size": len(self.event_history),
            "max_history": self.max_history
        }
