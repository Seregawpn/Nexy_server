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
import time
from typing import Any

from integration.core import selectors
from integration.core.error_handler import ErrorHandler
from integration.core.event_bus import EventBus, EventPriority
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
        # Сессии с активным browser task.
        self._active_browser_sessions: set[str] = set()
        # Сессии с активными actions (open_app/close_app).
        self._active_action_sessions: dict[str, int] = {}
        # Сессии, для которых уже пришло намерение action (grpc.response.action),
        # но lifecycle.started может прийти немного позже (гонка между потоками событий).
        self._pending_action_intents: dict[str, float] = {}
        self._action_intent_ttl_sec = 3.0
        # Короткое окно дедупликации mode.request по (target_mode, session_id).
        self._mode_request_dedup_window_sec: float = 0.5
        self._last_mode_request_ts: dict[tuple[str, str, str], float] = {}
        self._last_mode_request_id_ts: dict[str, float] = {}

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
            async def _on_controller_mode_changed(event):
                try:
                    # event.mode — это AppMode из централизованного модуля.
                    # session_id передаётся request-scoped через event.data, чтобы
                    # не было гонки на shared mutable поле между concurrent mode.request.
                    payload = getattr(event, "data", None)
                    session_id = payload.get("session_id") if isinstance(payload, dict) else None
                    self.state_manager.set_mode(event.mode, session_id=session_id)
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
            await self.event_bus.subscribe("browser.started", self._on_browser_started, EventPriority.MEDIUM)
            await self.event_bus.subscribe("browser.completed", self._on_browser_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("browser.failed", self._on_browser_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("browser.cancelled", self._on_browser_finished, EventPriority.MEDIUM)
            # Единый источник истины для активности actions: lifecycle-события.
            # Не подписываемся на actions.open_app/close_app.* дополнительно, чтобы
            # не учитывать одно действие дважды.
            await self.event_bus.subscribe("actions.lifecycle.started", self._on_action_started, EventPriority.MEDIUM)
            await self.event_bus.subscribe("actions.lifecycle.finished", self._on_action_finished, EventPriority.MEDIUM)
            await self.event_bus.subscribe("grpc.response.action", self._on_action_intent, EventPriority.MEDIUM)

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

            # PROCESSING без session_id запрещён: иначе появляется "пустой" processing-контур
            # (лишние app.mode_changed/screenshot/tray без request context).
            if target == AppMode.PROCESSING and normalized_session_id is None:
                logger.warning(
                    "MODE_REQUEST rejected: target=PROCESSING requires session_id (source=%s)",
                    source,
                )
                logger.info(
                    "CUE_TRACE phase=mode_request.rejected target=%s source=%s session_id=%s reason=processing_requires_session",
                    target,
                    source,
                    normalized_session_id,
                )
                return

            dedup_sid = normalized_session_id or "__none__"
            dedup_source = source or "__unknown__"
            dedup_key = (target.value if hasattr(target, "value") else str(target), dedup_sid, dedup_source)
            request_id = data.get("request_id")
            dedup_request_id = str(request_id) if request_id is not None else None
            now = time.monotonic()

            # Lightweight cleanup to keep map bounded.
            cutoff = now - (self._mode_request_dedup_window_sec * 4.0)
            stale_keys = [k for k, ts in self._last_mode_request_ts.items() if ts < cutoff]
            for k in stale_keys:
                self._last_mode_request_ts.pop(k, None)
            stale_request_ids = [rid for rid, ts in self._last_mode_request_id_ts.items() if ts < cutoff]
            for rid in stale_request_ids:
                self._last_mode_request_id_ts.pop(rid, None)

            # Важно: для финализаторов deferred-сессии не применяем ранний dedup.
            # Иначе request "processing_completed" (deferred) может "съесть"
            # следующий "playback.finished" и оставить PROCESSING залипшим.
            dedup_bypass = (
                source in {"playback.finished", "browser.finished", "actions.finished"}
                and normalized_session_id is not None
                and normalized_session_id in self._deferred_sleep_sessions
            )
            if not dedup_bypass:
                # Primary dedup: request_id (if provided by publisher).
                if dedup_request_id:
                    last_ts = self._last_mode_request_id_ts.get(dedup_request_id, 0.0)
                    if (now - last_ts) < self._mode_request_dedup_window_sec:
                        logger.debug(
                            "MODE_REQUEST dedup by request_id: request_id=%s target=%s session_id=%s source=%s dt=%.3fs",
                            dedup_request_id,
                            target,
                            normalized_session_id,
                            source,
                            now - last_ts,
                        )
                        logger.info(
                            "CUE_TRACE phase=mode_request.dedup target=%s source=%s session_id=%s reason=request_id",
                            target,
                            source,
                            normalized_session_id,
                        )
                        return
                    self._last_mode_request_id_ts[dedup_request_id] = now
                else:
                    # Backward-compatible dedup for publishers without request_id.
                    last_ts = self._last_mode_request_ts.get(dedup_key, 0.0)
                    if (now - last_ts) < self._mode_request_dedup_window_sec:
                        logger.debug(
                            "MODE_REQUEST dedup: target=%s session_id=%s source=%s dt=%.3fs",
                            target,
                            normalized_session_id,
                            source,
                            now - last_ts,
                        )
                        logger.info(
                            "CUE_TRACE phase=mode_request.dedup target=%s source=%s session_id=%s reason=key_window",
                            target,
                            source,
                            normalized_session_id,
                        )
                        return
                    self._last_mode_request_ts[dedup_key] = now
            else:
                logger.debug(
                    "MODE_REQUEST dedup bypass: target=%s session_id=%s source=%s (deferred finalize)",
                    target,
                    normalized_session_id,
                    source,
                )

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
                logger.info(
                    "CUE_TRACE phase=mode_request.ignored target=%s source=%s session_id=%s reason=same_mode",
                    target,
                    source,
                    normalized_session_id,
                )
                return

            # Guard: не уходим в SLEEPING по "штатному завершению", пока у сессии
            # есть активное воспроизведение/браузер/действия.
            if (
                target == AppMode.SLEEPING
                and source in {
                    "ProcessingWorkflow.processing_completed",
                    "playback",
                    "playback.finished",
                    "browser.finished",
                    "actions.finished",
                }
            ):
                guard_session_id = normalized_session_id or self._get_current_processing_session_id()
                blockers = self._collect_blockers_for_sleep_guard(guard_session_id)
                if blockers:
                    if guard_session_id is not None:
                        self._deferred_sleep_sessions.add(guard_session_id)
                    logger.info(
                        "MODE_REQUEST deferred: keep PROCESSING while work is active "
                        "(request_session=%s, guard_session=%s, source=%s, blockers=%s)",
                        normalized_session_id,
                        guard_session_id,
                        source,
                        ",".join(blockers),
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

            # Если browser/actions ещё идут, откладываем sleep до их завершения.
            if (
                session_id in self._active_browser_sessions
                or self._active_action_sessions.get(session_id, 0) > 0
                or self._has_pending_action_intent(session_id)
            ):
                self._deferred_sleep_sessions.add(session_id)
                logger.info(
                    "MODE_REQUEST deferred on playback_done: non-playback work still active "
                    "(session=%s, browser=%s, actions=%s, action_intent=%s)",
                    session_id,
                    session_id in self._active_browser_sessions,
                    self._active_action_sessions.get(session_id, 0),
                    self._has_pending_action_intent(session_id),
                )
                return

            # Единый путь публикации sleep после playback — через _on_playback_finished,
            # когда playback-сессия гарантированно снята из active_playback_sessions.
            self._deferred_sleep_sessions.add(session_id)
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
                    and session_id not in self._active_browser_sessions
                    and self._active_action_sessions.get(session_id, 0) == 0
                    and not self._has_pending_action_intent(session_id)
                ):
                    self._deferred_sleep_sessions.discard(session_id)
                    await self.event_bus.publish("mode.request", {
                        "target": AppMode.SLEEPING,
                        "source": "playback.finished",
                        "session_id": session_id,
                    })
        except Exception:
            pass

    async def _on_browser_started(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._normalize_session_id(data.get("session_id"))
            if session_id:
                self._active_browser_sessions.add(session_id)
        except Exception:
            pass

    async def _on_browser_finished(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._normalize_session_id(data.get("session_id"))
            if not session_id:
                return
            self._active_browser_sessions.discard(session_id)
            if (
                session_id in self._deferred_sleep_sessions
                and selectors.get_current_mode(self.state_manager) == AppMode.PROCESSING
                and session_id not in self._active_playback_sessions
                and self._active_action_sessions.get(session_id, 0) == 0
                and not self._has_pending_action_intent(session_id)
            ):
                self._deferred_sleep_sessions.discard(session_id)
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.SLEEPING,
                    "source": "browser.finished",
                    "session_id": session_id,
                })
        except Exception:
            pass

    async def _on_action_started(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._resolve_action_session_id(data.get("session_id"), source="action_started")
            if session_id:
                self._pending_action_intents.pop(session_id, None)
                self._active_action_sessions[session_id] = self._active_action_sessions.get(session_id, 0) + 1
        except Exception:
            pass

    async def _on_action_finished(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._resolve_action_session_id(data.get("session_id"), source="action_finished")
            if not session_id:
                return
            self._pending_action_intents.pop(session_id, None)
            current = self._active_action_sessions.get(session_id, 0)
            if current <= 1:
                self._active_action_sessions.pop(session_id, None)
            else:
                self._active_action_sessions[session_id] = current - 1

            if (
                session_id in self._deferred_sleep_sessions
                and selectors.get_current_mode(self.state_manager) == AppMode.PROCESSING
                and session_id not in self._active_playback_sessions
                and session_id not in self._active_browser_sessions
                and self._active_action_sessions.get(session_id, 0) == 0
                and not self._has_pending_action_intent(session_id)
            ):
                self._deferred_sleep_sessions.discard(session_id)
                await self.event_bus.publish("mode.request", {
                    "target": AppMode.SLEEPING,
                    "source": "actions.finished",
                    "session_id": session_id,
                })
        except Exception:
            pass

    async def _on_action_intent(self, event):
        try:
            data = (event or {}).get("data", {}) or {}
            session_id = self._resolve_action_session_id(data.get("session_id"), source="grpc.response.action")
            if session_id:
                self._pending_action_intents[session_id] = time.monotonic()
                logger.info(
                    "ACTION_INTENT received: session=%s source=%s command_preview=%s",
                    session_id,
                    data.get("source"),
                    str(data.get("action_json", ""))[:80],
                )
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
            # Поручаем переход контроллеру; он сам проверит доступность перехода
            # и при успехе через callback обновит StateManager (публикация событий сохранится централизованной)
            await self.controller.switch_mode(
                target,
                data={
                    "source": source,
                    "session_id": session_id,
                },
            )
        except Exception as e:
            logger.error(f"Apply mode error: {e}")

    async def _processing_timeout_guard(self):
        try:
            await asyncio.sleep(self._processing_timeout_sec)
            if selectors.get_current_mode(self.state_manager) == AppMode.PROCESSING:
                logger.warning("PROCESSING timeout — forcing SLEEPING via controller")
                try:
                    await self.controller.switch_mode(AppMode.SLEEPING)
                except Exception as exc:
                    logger.error("PROCESSING timeout switch failed via controller: %s", exc)
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
            "active_browser_sessions": sorted(self._active_browser_sessions),
            "active_action_sessions": dict(self._active_action_sessions),
            "pending_action_intents": sorted(self._pending_action_intents.keys()),
            "deferred_sleep_sessions": sorted(self._deferred_sleep_sessions),
        }

    def _has_pending_action_intent(self, session_id: str) -> bool:
        ts = self._pending_action_intents.get(session_id)
        if ts is None:
            return False
        if (time.monotonic() - ts) <= self._action_intent_ttl_sec:
            return True
        self._pending_action_intents.pop(session_id, None)
        return False

    def _has_any_pending_action_intent(self) -> bool:
        now = time.monotonic()
        for sid, ts in list(self._pending_action_intents.items()):
            if (now - ts) <= self._action_intent_ttl_sec:
                return True
            self._pending_action_intents.pop(sid, None)
        return False

    def _get_current_processing_session_id(self) -> str | None:
        if selectors.get_current_mode(self.state_manager) != AppMode.PROCESSING:
            return None
        return self._normalize_session_id(selectors.get_current_session_id(self.state_manager))

    def _resolve_action_session_id(self, incoming_session_id: Any, *, source: str) -> str | None:
        normalized = self._normalize_session_id(incoming_session_id)
        if normalized is not None:
            return normalized

        fallback = self._get_current_processing_session_id()
        if fallback is not None:
            logger.warning(
                "ACTION_SESSION_FALLBACK: source=%s missing session_id, "
                "using active processing session=%s",
                source,
                fallback,
            )
        return fallback

    def _collect_blockers_for_sleep_guard(self, session_id: str | None) -> list[str]:
        blockers: list[str] = []
        if session_id is not None:
            if session_id in self._active_playback_sessions:
                blockers.append("playback")
            if session_id in self._active_browser_sessions:
                blockers.append("browser")
            if self._active_action_sessions.get(session_id, 0) > 0:
                blockers.append("actions")
            if self._has_pending_action_intent(session_id):
                blockers.append("action_intent")

        # Global fallback guard: защищает от раннего sleep при рассинхроне session_id.
        if not blockers:
            if self._active_playback_sessions:
                blockers.append("playback_any")
            elif self._active_browser_sessions:
                blockers.append("browser_any")
            elif self._active_action_sessions:
                blockers.append("actions_any")
            elif self._has_any_pending_action_intent():
                blockers.append("action_intent_any")
        return blockers

    @staticmethod
    def _normalize_session_id(session_id: Any) -> str | None:
        if session_id is None:
            return None
        return str(session_id)
