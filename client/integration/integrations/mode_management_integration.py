"""
ModeManagementIntegration — центральная точка управления режимами приложения.

Задачи:
- Принимать заявки на смену режима (mode.request) от модулей/интеграций
- Применять переходы согласно приоритетам и базовым правилам
- Делать реальный вызов state_manager.set_mode() ровно в одном месте

Примечание: на этапе мягкой миграции интеграции ещё могут вызывать set_mode напрямую.
Этот класс уже обеспечивает корректную обработку заявок и таймаут PROCESSING.
"""

import asyncio
import logging
from typing import Any

from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
from integration.core import selectors
from integration.core.state_manager import ApplicationStateManager

# Import AppMode with fallback mechanism (same as state_manager.py and selectors.py)
try:
    # Preferred: top-level import (packaged or PYTHONPATH includes modules)
    from mode_management import AppMode  # type: ignore[reportMissingImports]
except Exception:
    # Fallback: explicit modules path if repository layout is used
    from modules.mode_management import AppMode  # type: ignore[reportMissingImports]

# Централизованный контроллер режимов
try:
    from mode_management import (  # type: ignore[reportMissingImports]
        ModeConfig,
        ModeController,
        ModeTransition,
        ModeTransitionType,
    )
except Exception:
    # Fallback to explicit modules path when running from repo
    from modules.mode_management import (
        ModeConfig,
        ModeController,
        ModeTransition,
        ModeTransitionType,
    )

logger = logging.getLogger(__name__)


class ModeManagementIntegration:
    """Централизованное управление режимами."""

    def __init__(
        self,
        event_bus: EventBus,
        state_manager: ApplicationStateManager,
        error_handler: ErrorHandler,
    ):
        self.event_bus = event_bus
        self.state_manager = state_manager
        self.error_handler = error_handler

        self._initialized = False
        self._running = False

        # Централизованный контроллер режимов (single source of truth)
        self.controller: ModeController = ModeController(ModeConfig())

        # Управление таймаутом PROCESSING (0.0 = отключено по требованиям)
        self._processing_timeout_sec = 0.0
        self._processing_timeout_task: asyncio.Task[Any] | None = None

        # КРИТИЧНО: Единый источник истины для session_id - ApplicationStateManager
        # Не храним дублирующие переменные здесь

        # Таймаут LISTENING (0.0 = отключено по требованиям)
        self._listening_timeout_sec = 0.0
        self._listening_timeout_task: asyncio.Task[Any] | None = None

        # Приоритеты источников (чем больше — тем важнее)
        self._priorities = {
            'interrupt': 100,
            'keyboard.short_press': 80,
            'keyboard.release': 60,
            'keyboard.long_press': 60,
            'playback': 50,
            'grpc': 50,
            'fallback': 10,
        }
        # Сессии, в которых воспроизведение уже стартовало и еще не завершено.
        self._active_playback_sessions: set[str] = set()
        # Сессии, для которых уже был отложен переход в SLEEPING до завершения playback.
        self._deferred_sleep_sessions: set[str] = set()

    # ---------------- Lifecycle ----------------
    async def initialize(self) -> bool:
        try:
            # Подписки на события заявок и системные события
            await self.event_bus.subscribe("mode.request", self._on_mode_request, EventPriority.CRITICAL)
            await self.event_bus.subscribe("app.mode_changed", self._on_app_mode_changed, EventPriority.HIGH)

            # Регистрируем допустимые переходы контроллера
            # Классический цикл: SLEEPING -> LISTENING -> PROCESSING -> SLEEPING
            self.controller.register_transition(ModeTransition(AppMode.SLEEPING, AppMode.LISTENING, ModeTransitionType.AUTOMATIC))
            self.controller.register_transition(ModeTransition(AppMode.LISTENING, AppMode.PROCESSING, ModeTransitionType.AUTOMATIC))
            self.controller.register_transition(ModeTransition(AppMode.PROCESSING, AppMode.SLEEPING, ModeTransitionType.AUTOMATIC))
            
            # 🆕 Прямой переход для приветствия: SLEEPING -> PROCESSING
            self.controller.register_transition(ModeTransition(AppMode.SLEEPING, AppMode.PROCESSING, ModeTransitionType.MANUAL))
            # 🆕 PTT override: разрешаем LISTENING из PROCESSING
            self.controller.register_transition(ModeTransition(AppMode.PROCESSING, AppMode.LISTENING, ModeTransitionType.MANUAL))
            # 🆕 Позволяем отменить слушание и вернуться в сон вручную
            self.controller.register_transition(ModeTransition(AppMode.LISTENING, AppMode.SLEEPING, ModeTransitionType.MANUAL))

            # Мост: при смене режима контроллером — обновляем StateManager,
            # который централизованно публикует события (app.mode_changed/app.state_changed)
            # КРИТИЧНО: Храним session_id для передачи в set_mode через callback
            self._pending_session_id_for_callback: str | None = None
            
            async def _on_controller_mode_changed(event):
                try:
                    # event.mode — это AppMode из централизованного модуля
                    # Используем сохраненный session_id из последнего mode.request
                    session_id = getattr(self, '_pending_session_id_for_callback', None)
                    self.state_manager.set_mode(event.mode, session_id=session_id)
                    # Сбрасываем после использования
                    self._pending_session_id_for_callback = None
                except Exception as e:
                    logger.error(f"StateManager bridging failed: {e}")
            self.controller.register_mode_change_callback(_on_controller_mode_changed)

            # Мост с существующими событиями (на время миграции)
            # Отключено, чтобы избежать дублей mode.request (источник — InputProcessingIntegration)
            # await self.event_bus.subscribe("keyboard.long_press", self._bridge_keyboard_long, EventPriority.MEDIUM)
            # await self.event_bus.subscribe("keyboard.release", self._bridge_keyboard_release, EventPriority.MEDIUM)
            # await self.event_bus.subscribe("keyboard.short_press", self._bridge_keyboard_short, EventPriority.MEDIUM)

            # Внимание: не возвращаем SLEEPING по завершению gRPC — ждём завершения воспроизведения
            # Доп. подписки для контекста (без публикации режимов)
            try:
                await self.event_bus.subscribe("voice.recording_start", self._on_voice_recording_start, EventPriority.MEDIUM)
            except Exception:
                pass
            # await self.event_bus.subscribe("grpc.request_completed", self._bridge_grpc_done, EventPriority.MEDIUM)
            # await self.event_bus.subscribe("grpc.request_failed", self._bridge_grpc_done, EventPriority.MEDIUM)

            await self.event_bus.subscribe("playback.completed", self._bridge_playback_done, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.failed", self._bridge_playback_done, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.started", self._on_playback_started, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.cancelled", self._on_playback_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.completed", self._on_playback_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("playback.failed", self._on_playback_finished, EventPriority.MEDIUM)

            # УБРАНО: interrupt.request - обрабатывается централизованно в InterruptManagementIntegration

            self._initialized = True
            logger.info("ModeManagementIntegration initialized")
            return True
        except Exception as e:
            logger.error(f"ModeManagementIntegration init failed: {e}")
            return False

    async def start(self) -> bool:
        if not self._initialized:
            return False
        self._running = True
        logger.info("ModeManagementIntegration started")
        return True

    async def stop(self) -> bool:
        try:
            self._running = False
            if self._processing_timeout_task:
                self._processing_timeout_task.cancel()
            return True
        except Exception:
            return False

    # ---------------- Event handlers ----------------
    async def _on_mode_request(self, event):
        # КРИТИЧНО: Все изменения идут через единый источник истины (ApplicationStateManager)
        # EventBus уже обеспечивает последовательную обработку событий, блокировки не нужны
        try:
            data = (event or {}).get("data", {})
            target = data.get("target")  # может быть AppMode или str

            logger.info(f"🔄 MODE_REQUEST: target={target}, source={data.get('source')}, session_id={data.get('session_id')}, priority={data.get('priority')}")

            if isinstance(target, str):
                try:
                    target = AppMode(target.lower())
                except Exception:
                    # допускаем значения вида "PROCESSING" без понижения регистра
                    try:
                        target = AppMode(target.lower())
                    except Exception:
                        logger.warning(f"MODE_REQUEST: Invalid target={target}, ignoring")
                        return
            if target not in (AppMode.SLEEPING, AppMode.LISTENING, AppMode.PROCESSING):
                logger.warning(f"MODE_REQUEST: target={target} not in allowed modes, ignoring")
                return

            # Нормализация priority: поддерживаем EventPriority enum, int, str
            priority_raw = data.get("priority", 0)
            if isinstance(priority_raw, EventPriority):
                priority = priority_raw.value
            elif isinstance(priority_raw, (int, float)):
                priority = int(priority_raw)
            elif isinstance(priority_raw, str):
                # Попытка преобразовать строку в int (например, "3" -> 3)
                try:
                    priority = int(priority_raw)
                except (ValueError, TypeError):
                    priority = 0
            else:
                priority = 0
            source = str(data.get("source", "unknown"))
            session_id = data.get("session_id")
            normalized_session_id = self._normalize_session_id(session_id)

            # Фильтрация по сессии (в PROCESSING принимаем только текущую либо interrupt)
            current_mode = selectors.get_current_mode(self.state_manager)
            logger.info(f"🔄 MODE_REQUEST: current_mode={current_mode}, target={target}, source={source}")

            # КРИТИЧНО: Для PROCESSING разрешаем повторные запросы с новым session_id
            # Это позволяет обрабатывать новый запрос пользователя, даже если приложение
            # еще обрабатывает предыдущий запрос
            if target == AppMode.PROCESSING and current_mode == AppMode.PROCESSING:
                # Проверяем, это новый запрос с другим session_id?
                current_session_id = selectors.get_current_session_id(self.state_manager)
                if session_id is not None and current_session_id is not None:
                    if session_id != current_session_id:
                        # КРИТИЧНО: Просто вызываем set_mode() с новым session_id
                        # set_mode() сам опубликует app.mode_changed если session_id изменился
                        logger.info(f"🔄 MODE_REQUEST: новый запрос на PROCESSING с другим session_id (active={current_session_id}, request={session_id}) - разрешаем")
                        self.state_manager.set_mode(target, session_id=session_id)
                        return
                    else:
                        # Тот же session_id - идемпотентность
                        logger.debug(f"Mode request ignored (same mode and session): {target}, session_id={session_id}")
                        return
                elif session_id is not None:
                    # Новый запрос без активной сессии - разрешаем
                    logger.info(f"🔄 MODE_REQUEST: новый запрос на PROCESSING без активной сессии (request={session_id}) - разрешаем")
                    self.state_manager.set_mode(target, session_id=session_id)
                    return
                else:
                    # Нет session_id - идемпотентность
                    logger.debug(f"Mode request ignored (same mode, no session_id): {target}")
                    return
            
            # Идемпотентность: если запрашивают тот же режим — игнорируем (для других режимов)
            if target == current_mode:
                logger.debug(f"Mode request ignored (same mode): {target}")
                return

            # Guard: не уходим в SLEEPING из processing_completed, пока еще играет ответ текущей сессии.
            if (
                target == AppMode.SLEEPING
                and source == "ProcessingWorkflow.processing_completed"
                and normalized_session_id is not None
                and normalized_session_id in self._active_playback_sessions
            ):
                self._deferred_sleep_sessions.add(normalized_session_id)
                logger.info(
                    "MODE_REQUEST deferred: keep PROCESSING while playback is active "
                    "(session=%s, source=%s)",
                    normalized_session_id,
                    source,
                )
                return
            
            if current_mode == AppMode.PROCESSING and source != 'interrupt':
                current_session_id = selectors.get_current_session_id(self.state_manager)
                logger.info(f"🔄 MODE_REQUEST: в PROCESSING, проверяем session_id (active={current_session_id}, request={session_id})")
                if current_session_id is not None and session_id is not None:
                    if session_id != current_session_id:
                        logger.debug("Mode request ignored due to session mismatch in PROCESSING")
                        return

            # Приоритеты: если заявка из более низкого приоритета — применяем только если нет конфликтов
            # Упрощённая модель: interrupt всегда применяется, остальное — напрямую
            if source == 'interrupt' or priority >= 90:
                logger.info(f"🔄 MODE_REQUEST: применяем как interrupt (source={source}, priority={priority}) → {target}")
                # КРИТИЧНО: Все изменения идут через set_mode() - единый источник истины
                await self._apply_mode(target, source="interrupt", session_id=session_id)
                return

            logger.info(f"🔄 MODE_REQUEST: применяем mode → {target}")
            # КРИТИЧНО: Все изменения идут через set_mode() - единый источник истины
            await self._apply_mode(target, source=source, session_id=session_id)

        except Exception as e:
            logger.error(f"Mode request handling error: {e}")

    async def _on_app_mode_changed(self, event):
        try:
            data = (event or {}).get("data", {})
            new_mode = data.get("mode")
            # Синхронизируем внутренний контроллер, если режим изменили в обход
            try:
                if hasattr(self.controller, 'get_current_mode') and new_mode is not None:
                    if self.controller.get_current_mode() != new_mode:
                        # Обновляем только внутреннее состояние без действий/обработчиков
                        self.controller.previous_mode = getattr(self.controller, 'current_mode', None)
                        self.controller.current_mode = new_mode
                        self.controller.mode_start_time = __import__('time').time()
            except Exception:
                pass
            if new_mode == AppMode.PROCESSING:
                # PROCESSING: запуск таймера только если включен (>0)
                if self._processing_timeout_task and not self._processing_timeout_task.done():
                    self._processing_timeout_task.cancel()
                if (self._processing_timeout_sec or 0) > 0:
                    self._processing_timeout_task = asyncio.create_task(self._processing_timeout_guard())
                if self._listening_timeout_task and not self._listening_timeout_task.done():
                    self._listening_timeout_task.cancel()
            elif new_mode == AppMode.LISTENING:
                # LISTENING: запуск таймера только если включен (>0)
                if self._listening_timeout_task and not self._listening_timeout_task.done():
                    self._listening_timeout_task.cancel()
                if (self._listening_timeout_sec or 0) > 0:
                    self._listening_timeout_task = asyncio.create_task(self._listening_timeout_guard())
                if self._processing_timeout_task and not self._processing_timeout_task.done():
                    self._processing_timeout_task.cancel()
            else:
                # Прочие режимы — таймеры не нужны
                if self._processing_timeout_task and not self._processing_timeout_task.done():
                    self._processing_timeout_task.cancel()
                if self._listening_timeout_task and not self._listening_timeout_task.done():
                    self._listening_timeout_task.cancel()
        except Exception:
            pass

    async def _on_voice_recording_start(self, event):
        """Фиксируем session_id для контекста LISTENING/PROCESSING."""
        # КРИТИЧНО: Единый источник истины для session_id - ApplicationStateManager
        # Не нужно обновлять дублирующие переменные
        pass

    # --------------- Bridges (temporary during migration) ---------------
    async def _bridge_keyboard_long(self, event):
        try:
            await self.event_bus.publish("mode.request", {
                "target": AppMode.LISTENING,
                "source": "keyboard.long_press"
            })
        except Exception:
            pass

    async def _bridge_keyboard_release(self, event):
        try:
            data = (event or {}).get("data", {})
            await self.event_bus.publish("mode.request", {
                "target": AppMode.PROCESSING,
                "source": "keyboard.release",
                "session_id": data.get("session_id")
            })
        except Exception:
            pass

    async def _bridge_keyboard_short(self, event):
        try:
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "keyboard.short_press"
            })
        except Exception:
            pass

    async def _bridge_grpc_done(self, event):
        try:
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "grpc"
            })
        except Exception:
            pass

    async def _bridge_playback_done(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._normalize_session_id(data.get("session_id"))
            current_mode = selectors.get_current_mode(self.state_manager)
            current_session_id = self._normalize_session_id(
                selectors.get_current_session_id(self.state_manager)
            )

            # Guard: вне PROCESSING ничего не делаем.
            if current_mode != AppMode.PROCESSING:
                logger.debug(
                    "MODE_REQUEST skipped (playback done): current_mode=%s, session_id=%s",
                    current_mode,
                    session_id,
                )
                return
            if session_id is None:
                logger.debug("MODE_REQUEST skipped (playback done): no session_id")
                return

            # Разрешаем финализацию если:
            # 1) это явно отложенный sleeping для этой сессии, или
            # 2) это текущая активная сессия в state manager.
            if (
                session_id not in self._deferred_sleep_sessions
                and (current_session_id is None or session_id != current_session_id)
            ):
                logger.debug(
                    "MODE_REQUEST skipped (playback done): session mismatch event=%s current=%s",
                    session_id,
                    current_session_id,
                )
                return

            self._deferred_sleep_sessions.discard(session_id)
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "playback",
                "session_id": session_id,
            })
        except Exception:
            pass

    async def _on_playback_started(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._normalize_session_id(data.get("session_id"))
            if session_id:
                self._active_playback_sessions.add(session_id)
        except Exception:
            pass

    async def _on_playback_finished(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._normalize_session_id(data.get("session_id"))
            if session_id:
                self._active_playback_sessions.discard(session_id)
                # Fail-safe: если sleeping был отложен и bridge не смог применить (из-за гонки
                # с очисткой session_id), публикуем переход здесь.
                if (
                    session_id in self._deferred_sleep_sessions
                    and selectors.get_current_mode(self.state_manager) == AppMode.PROCESSING
                ):
                    self._deferred_sleep_sessions.discard(session_id)
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "playback.finished",
                        "session_id": session_id,
                    })
        except Exception:
            pass

    async def _bridge_interrupt(self, event):
        try:
            await self.event_bus.publish("mode.request", {
                "target": AppMode.SLEEPING,
                "source": "interrupt",
                "priority": self._priorities.get('interrupt', 100)
            })
        except Exception:
            pass

    # ---------------- Internals ----------------
    async def _apply_mode(self, target: AppMode, *, source: str, session_id: str | None = None):
        try:
            # КРИТИЧНО: Сохраняем session_id для передачи в set_mode через callback
            self._pending_session_id_for_callback = session_id
            # Поручаем переход контроллеру; он сам проверит доступность перехода
            # и при успехе через callback обновит StateManager (публикация событий сохранится централизованной)
            await self.controller.switch_mode(target)
        except Exception as e:
            logger.error(f"Apply mode error: {e}")
            # Сбрасываем session_id при ошибке
            self._pending_session_id_for_callback = None

    async def _processing_timeout_guard(self):
        try:
            await asyncio.sleep(self._processing_timeout_sec)
            if selectors.get_current_mode(self.state_manager) == AppMode.PROCESSING:
                logger.warning("PROCESSING timeout — forcing SLEEPING via controller")
                try:
                    await self.controller.switch_mode(AppMode.SLEEPING)
                except Exception:
                    # Fallback to direct state update if controller failed
                    try:
                        self.state_manager.set_mode(AppMode.SLEEPING)
                    except Exception:
                        pass
        except asyncio.CancelledError:
            return
        except Exception:
            pass

    async def _listening_timeout_guard(self):
        """Автовозврат в SLEEPING, если LISTENING затянулся без RELEASE/STOP."""
        try:
            await asyncio.sleep(self._listening_timeout_sec)
            if selectors.get_current_mode(self.state_manager) == AppMode.LISTENING:
                await self._apply_mode(AppMode.SLEEPING, source="mode_management")
        except asyncio.CancelledError:
            return
        except Exception:
            pass

    def get_status(self) -> dict[str, Any]:
        return {
            "initialized": self._initialized,
            "running": self._running,
            "processing_timeout_sec": self._processing_timeout_sec,
            "listening_timeout_sec": self._listening_timeout_sec,
            "active_session_id": selectors.get_current_session_id(self.state_manager),
            "active_playback_sessions": sorted(self._active_playback_sessions),
            "deferred_sleep_sessions": sorted(self._deferred_sleep_sessions),
        }

    @staticmethod
    def _normalize_session_id(session_id: Any) -> str | None:
        if session_id is None:
            return None
        return str(session_id)
