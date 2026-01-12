"""
ApplicationStateManager - Управление состоянием приложения
"""

import logging
import threading
import uuid
from typing import Dict, Any, Optional

"""
NOTE: AppMode is imported from the centralized mode_management module to avoid
duplication and desynchronization. This keeps a single source of truth for
application modes across all integrations.
"""
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

# Экспортируем AppMode для использования в других модулях
__all__ = ['ApplicationStateManager', 'AppMode']

logger = logging.getLogger(__name__)

class ApplicationStateManager:
    """Менеджер состояния приложения"""
    
    def __init__(self):
        # Thread-safety lock for state mutations
        self._lock = threading.Lock()
        self.current_mode = AppMode.SLEEPING
        self.previous_mode = None
        self.mode_history = []
        self.state_data = {}
        # КРИТИЧНО: Единый источник истины для session_id
        self.current_session_id: Optional[str] = None
        # EventBus (необязателен). Устанавливается координатором.
        self._event_bus = None
        self._loop = None  # основной asyncio loop, на который публикуем события

    def attach_event_bus(self, event_bus):
        """Прикрепить EventBus для публикации событий смены режима"""
        self._event_bus = event_bus
        try:
            import asyncio
            # Сохраняем текущий running loop как основной для публикаций
            self._loop = asyncio.get_running_loop()
            logger.debug(f"StateManager: attached EventBus with loop={id(self._loop)} running={self._loop.is_running() if self._loop else False}")
        except Exception:
            self._loop = None
        
    def set_mode(self, mode: AppMode, session_id: Optional[str] = None):
        """Установить режим приложения
        
        Публикует app.mode_changed если:
        - Режим изменился, ИЛИ
        - session_id изменился (даже если режим не изменился)
        
        Thread-safe: state mutations are protected by lock.
        Event publication happens OUTSIDE lock to prevent deadlocks.
        """
        # Snapshot for event publication (outside lock)
        should_publish = False
        snapshot_mode = None
        snapshot_previous_mode = None
        snapshot_session_id = None
        event_bus = None
        
        try:
            # === CRITICAL SECTION: Mutate state under lock ===
            with self._lock:
                mode_changed = self.current_mode != mode
                
                # Обновляем режим если изменился
                if mode_changed:
                    self.previous_mode = self.current_mode
                    self.current_mode = mode
                    
                    # Добавляем в историю
                    self.mode_history.append({
                        "mode": mode,
                        "previous_mode": self.previous_mode,
                        "timestamp": self._get_timestamp()
                    })
                    
                    # Ограничиваем историю
                    if len(self.mode_history) > 100:
                        self.mode_history.pop(0)
                    
                    logger.info(f"🔄 Режим изменен: {self.previous_mode.value} → {mode.value}")
                
                # Обновляем session_id если передан и валиден
                session_id_for_event = None
                if session_id is not None:
                    if self._is_valid_session_id(session_id):
                        self.current_session_id = session_id
                        session_id_for_event = session_id
                    else:
                        logger.warning(
                            f"⚠️ StateManager: invalid session_id ignored: {session_id} "
                            f"(type={type(session_id)})"
                        )
                
                # Prepare snapshot for publishing OUTSIDE lock
                if mode_changed:
                    should_publish = True
                    snapshot_mode = self.current_mode
                    snapshot_previous_mode = self.previous_mode
                    snapshot_session_id = session_id_for_event
                    event_bus = self._event_bus
            # === END CRITICAL SECTION ===
            
            # Publish events OUTSIDE lock to prevent deadlocks
            if should_publish and event_bus is not None:
                self._publish_mode_changed(
                    event_bus, snapshot_mode, snapshot_previous_mode, snapshot_session_id
                )
            elif should_publish:
                logger.warning("⚠️ StateManager: EventBus не подключен, события не публикуются")
            
        except Exception as e:
            logger.error(f"❌ Ошибка установки режима: {e}")
    
    def _publish_mode_changed(self, event_bus, mode, previous_mode, session_id):
        """Publish mode change events. Called OUTSIDE lock."""
        try:
            import asyncio
            loop = getattr(event_bus, "_loop", None)
            
            async def _publish_changes():
                event_data = {"mode": mode}
                if session_id is not None:
                    event_data["session_id"] = session_id
                await event_bus.publish("app.mode_changed", event_data)
                await event_bus.publish("app.state_changed", {
                    "old_mode": previous_mode,
                    "new_mode": mode
                })
            
            def _log_exception(fut):
                """Callback to log exceptions from fire-and-forget coroutines."""
                try:
                    exc = fut.exception()
                    if exc:
                        logger.error(f"❌ StateManager event publish failed: {exc}")
                except Exception:
                    pass
            
            if loop is not None and getattr(loop, 'is_running', lambda: False)():
                fut = asyncio.run_coroutine_threadsafe(_publish_changes(), loop)
                fut.add_done_callback(_log_exception)
            else:
                asyncio.create_task(_publish_changes())
            
        except Exception as e:
            logger.error(f"❌ StateManager: Не удалось опубликовать события: {e}")
    
    def update_session_id(self, session_id: Optional[str]) -> bool:
        """
        Обновить session_id БЕЗ публикации app.mode_changed.
        
        Используется для синхронизации session_id без побочных эффектов
        (например, при получении audio_chunk во время активной обработки).
        
        Args:
            session_id: Новый session_id (может быть None для сброса)
            
        Returns:
            True если session_id изменился, False если остался прежним
        """
        try:
            with self._lock:
                if session_id is not None and not self._is_valid_session_id(session_id):
                    logger.warning(
                        f"⚠️ StateManager: invalid session_id ignored: {session_id} "
                        f"(type={type(session_id)})"
                    )
                    return False
                if session_id != self.current_session_id:
                    old_session_id = self.current_session_id
                    self.current_session_id = session_id
                    logger.debug(
                        f"🔄 Session ID обновлен (без публикации события): "
                        f"{old_session_id} → {session_id}"
                    )
                    return True
                return False
        except Exception as e:
            logger.error(f"❌ Ошибка обновления session_id: {e}")
            return False
    
    def get_current_session_id(self) -> Optional[str]:
        """Получить текущий session_id"""
        with self._lock:
            return self.current_session_id

    @staticmethod
    def _is_valid_session_id(value: Any) -> bool:
        """Validate session_id as uuid4 string."""
        if not isinstance(value, str):
            return False
        try:
            uuid_obj = uuid.UUID(value)
            return uuid_obj.version == 4
        except (ValueError, TypeError):
            return False
    
    def get_current_mode(self) -> AppMode:
        """Получить текущий режим"""
        with self._lock:
            return self.current_mode
    
    def get_previous_mode(self) -> Optional[AppMode]:
        """Получить предыдущий режим"""
        with self._lock:
            return self.previous_mode
    
    def set_state_data(self, key: str, value: Any):
        """Установить данные состояния (thread-safe)"""
        try:
            with self._lock:
                self.state_data[key] = value
            logger.debug(f"📊 Данные состояния обновлены: {key}")
            
        except Exception as e:
            logger.error(f"❌ Ошибка установки данных состояния: {e}")
    
    def get_state_data(self, key: str, default: Any = None) -> Any:
        """Получить данные состояния"""
        with self._lock:
            return self.state_data.get(key, default)
    
    def get_mode_history(self, limit: int = 10) -> list:
        """Получить историю режимов"""
        with self._lock:
            return self.mode_history[-limit:]
    
    # Typed State Setters (Architectural Guards)
    
    def set_first_run_state(self, in_progress: bool, required: bool, completed: bool):
        """Update first run state flags safely."""
        self.set_state_data("first_run_in_progress", in_progress)
        self.set_state_data("first_run_required", required)
        self.set_state_data("first_run_completed", completed)
        
    def set_restart_pending(self, pending: bool):
        """Update restart pending flag."""
        self.set_state_data("permissions_restart_pending", pending)
        
    def set_update_in_progress(self, in_progress: bool):
        """Update update in progress status."""
        self.set_state_data("update_in_progress", in_progress)
        
    def set_restart_completed_fallback(self, completed: bool):
        """Update restart completed fallback flag."""
        self.set_state_data("permissions_restart_completed_fallback", completed)

    def _get_timestamp(self) -> float:
        """Получить текущий timestamp"""
        import time
        return time.time()
    
    def get_status(self) -> Dict[str, Any]:
        """Получить статус менеджера состояния"""
        return {
            "current_mode": self.current_mode.value,
            "previous_mode": self.previous_mode.value if self.previous_mode else None,
            "mode_history_size": len(self.mode_history),
            "state_data_keys": list(self.state_data.keys())
        }
