"""
ProcessingWorkflow - Управление режимом PROCESSING
Координирует цепочку: capture → grpc → playback → sleeping
"""

import asyncio
from datetime import datetime
from enum import Enum
import logging
from typing import Any

from integration.core.event_bus import EventPriority

from .base_workflow import BaseWorkflow, WorkflowState  # type: ignore

logger = logging.getLogger(__name__)


class ProcessingStage(Enum):
    """Этапы обработки в режиме PROCESSING"""

    STARTING = "starting"
    CAPTURING = "capturing"
    SENDING_GRPC = "sending_grpc"
    PLAYING_AUDIO = "playing_audio"
    BROWSER_AUTOMATION = "browser_automation"  # Browser task in progress
    COMPLETING = "completing"


class ProcessingWorkflow(BaseWorkflow):
    """
    Workflow для режима PROCESSING.

    Координирует полную цепочку обработки:
    1. Захват скриншота (ScreenshotCaptureIntegration)
    2. Отправка на gRPC сервер (GrpcClientIntegration)
    3. Воспроизведение ответа (SpeechPlaybackIntegration)
    4. Возврат в SLEEPING

    КЛЮЧЕВАЯ ОСОБЕННОСТЬ: Ждет РЕАЛЬНЫХ событий вместо таймаутов!
    """

    def __init__(self, event_bus):
        super().__init__(event_bus, "ProcessingWorkflow")

        # Конфигурация
        self.stage_timeout = None  # ОТКЛЮЧЕНО: ждём ответа без ограничения времени на этап
        self.total_timeout = 300.0  # секунд общий таймаут (5 минут) - защита от зависания

        # Состояние цепочки
        self.current_stage = ProcessingStage.STARTING
        self.stage_start_time: datetime | None = None
        self.processing_start_time: datetime | None = None
        self.completed_stages: set[ProcessingStage] = set()

        # Мониторинг
        self.stage_timeout_task: asyncio.Task[Any] | None = None
        self.total_timeout_task: asyncio.Task[Any] | None = None

        # Флаги завершения
        self.screenshot_captured = False
        self.grpc_completed = False
        self.recognition_failed = False  # New flag for recognition failure
        self.playback_completed = False
        self.interrupted = False
        self.browser_active = False  # Browser automation in progress
        self.action_dispatched = False  # Browser action dispatched but not yet started
        self.grpc_started = False
        self._terminal_outcome_session_id: str | None = None
        self._terminal_outcome_reason: str | None = None
        self._pending_screenshot_by_session: dict[str, dict[str, Any]] = {}
        self._pending_recognition_failed_by_session: dict[str, dict[str, Any]] = {}

        # КРИТИЧНО: Единый источник истины для session_id - ApplicationStateManager.

    async def _setup_subscriptions(self):
        """Подписка на события цепочки PROCESSING"""

        # === ВХОД В PROCESSING ===
        await self.event_bus.subscribe(
            "app.mode_changed", self._on_mode_changed, EventPriority.HIGH
        )

        # === ЭТАП 1: ЗАХВАТ СКРИНШОТА ===
        await self.event_bus.subscribe(
            "screenshot.captured", self._on_screenshot_captured, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "screenshot.error", self._on_screenshot_error, EventPriority.HIGH
        )

        # === ЭТАП: РАСПОЗНАВАНИЕ ===
        await self.event_bus.subscribe(
            "voice.recognition_failed", self._on_recognition_failed, EventPriority.HIGH
        )

        # === ЭТАП 2: GRPC ЗАПРОС ===
        await self.event_bus.subscribe(
            "grpc.request_started", self._on_grpc_started, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "grpc.request_completed", self._on_grpc_completed, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "grpc.request_failed", self._on_grpc_failed, EventPriority.HIGH
        )

        # === ЭТАП 3: ВОСПРОИЗВЕДЕНИЕ ===
        await self.event_bus.subscribe(
            "playback.started", self._on_playback_started, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "playback.completed", self._on_playback_completed, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "playback.failed", self._on_playback_failed, EventPriority.HIGH
        )

        # === ПРЕРЫВАНИЯ ===
        await self.event_bus.subscribe(
            "interrupt.request", self._on_interrupt_request, EventPriority.CRITICAL
        )

        # === ЭТАП 4: BROWSER AUTOMATION ===
        await self.event_bus.subscribe(
            "actions.browser_use.started",
            self._on_browser_action_dispatched,
            EventPriority.HIGH,
        )

        await self.event_bus.subscribe(
            "browser.started", self._on_browser_started, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "browser.completed", self._on_browser_completed, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "browser.failed", self._on_browser_failed, EventPriority.HIGH
        )

        await self.event_bus.subscribe(
            "browser.cancelled",
            self._on_browser_cancelled,
            EventPriority.HIGH,
        )

    async def _on_start(self):
        """Запуск workflow'а"""
        logger.info("⚙️ ProcessingWorkflow: готов к координации обработки")

    async def _on_mode_changed(self, event):
        """Обработка смены режима"""
        # КРИТИЧНО: Все изменения идут через единый источник истины (ApplicationStateManager).
        try:
            data = event.get("data", {})
            new_mode = data.get("mode")
            session_id = data.get("session_id")

            if hasattr(new_mode, "value"):
                mode_value = new_mode.value
            else:
                mode_value = str(new_mode).lower()

            logger.debug(f"⚙️ ProcessingWorkflow: режим изменен на {mode_value}")

            if mode_value == "processing":
                # Source-of-truth guard: processing chain requires session_id.
                # Mode transitions without session_id (e.g. welcome playback) must not start
                # the capture->grpc workflow path.
                if session_id is None:
                    logger.info(
                        "⚙️ ProcessingWorkflow: mode=processing без session_id — "
                        "пропускаем запуск цепочки (source=%s)",
                        data.get("source"),
                    )
                    return

                # КРИТИЧНО: Нормализуем session_id для сравнения (может быть str или float)
                normalized_session_id = str(session_id) if session_id is not None else None
                normalized_current = (
                    str(self.current_session_id) if self.current_session_id is not None else None
                )

                # КРИТИЧНО: Если workflow уже активен с тем же session_id - игнорируем событие
                # Это защищает от ложных прерываний при синхронизации session_id (например, при audio_chunk)
                if (
                    self.current_session_id is not None
                    and normalized_session_id == normalized_current
                    and self.state == WorkflowState.ACTIVE
                ):
                    logger.debug(
                        f"⚙️ ProcessingWorkflow: событие app.mode_changed для текущего session_id={session_id} (уже обрабатывается), игнорируем"
                    )
                    return

                # КРИТИЧНО: Проверяем, это новый запрос с другим session_id?
                # Если workflow уже активен с другим session_id, прерываем предыдущий запрос
                if self.state == WorkflowState.ACTIVE and self.current_session_id is not None:
                    if normalized_session_id != normalized_current:
                        logger.info(
                            f"⚙️ ProcessingWorkflow: новый запрос с другим session_id (active={self.current_session_id}, request={session_id}) - прерываем предыдущий"
                        )
                        # Прерываем предыдущий запрос через внутренний метод
                        self.interrupted = True
                        await self._cancel_timeout_tasks()
                        await self._cancel_active_processes()
                        # НЕ возвращаемся в SLEEPING - сразу начинаем новый запрос

                # НАЧИНАЕМ координацию цепочки PROCESSING
                await self._start_processing_chain(session_id)

            elif self.state == WorkflowState.ACTIVE and mode_value != "processing":
                # Вышли из PROCESSING - завершаем координацию
                logger.info(f"⚙️ ProcessingWorkflow: вышли из PROCESSING, завершаем координацию")
                await self._cleanup_processing()

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки mode_changed - {e}")

    async def _start_processing_chain(self, session_id: str | None):
        """Начало координации цепочки PROCESSING"""
        try:
            logger.info(f"⚙️ ProcessingWorkflow: НАЧАЛО цепочки обработки, session_id={session_id}")

            # Инициализация состояния
            self.current_session_id = session_id
            self._terminal_outcome_session_id = None
            self._terminal_outcome_reason = None
            self.current_stage = ProcessingStage.STARTING
            self.processing_start_time = datetime.now()
            self.stage_start_time = datetime.now()
            self.state = WorkflowState.ACTIVE

            # Сброс флагов
            self.completed_stages.clear()
            self.screenshot_captured = False
            self.grpc_completed = False
            self.recognition_failed = False
            self.playback_completed = False
            self.interrupted = False
            self.browser_active = False
            self.action_dispatched = False
            self.grpc_started = False

            # Запуск общего таймаута
            if self.total_timeout_task and not self.total_timeout_task.done():
                self.total_timeout_task.cancel()

            # Проверяем, что session_id не None перед запуском монитора
            if session_id is not None:
                self.total_timeout_task = self._create_task(
                    self._total_timeout_monitor(session_id), "total_timeout"
                )
            else:
                logger.warning(
                    "⚙️ ProcessingWorkflow: session_id is None, skipping total timeout monitor"
                )
                self.total_timeout_task = None

            # Anti-race: recognition_failed may arrive before this workflow becomes ACTIVE.
            # Apply buffered terminal no-speech result immediately for this session.
            normalized_session_id = str(session_id) if session_id is not None else None
            buffered_failed = (
                self._pending_recognition_failed_by_session.pop(normalized_session_id, None)
                if normalized_session_id is not None
                else None
            )
            if buffered_failed:
                buffered_error = buffered_failed.get("error", "unknown")
                logger.info(
                    "🎤 ProcessingWorkflow: применяем buffered recognition_failed "
                    "для session=%s (error=%s) до grpc.request_started",
                    normalized_session_id,
                    buffered_error,
                )
                self.recognition_failed = True
                await self._complete_processing_chain()
                return

            # Переходим к этапу захвата
            await self._transition_to_stage(ProcessingStage.CAPTURING)
            await self._consume_pending_screenshot_for_session(session_id)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка начала цепочки - {e}")
            await self._handle_error("start_chain_error")

    async def _transition_to_stage(self, new_stage: ProcessingStage):
        """Переход к новому этапу обработки"""
        try:
            old_stage = self.current_stage
            self.current_stage = new_stage
            self.stage_start_time = datetime.now()

            logger.info(f"⚙️ ProcessingWorkflow: переход {old_stage.value} → {new_stage.value}")

            # Отменяем предыдущий stage timeout
            if self.stage_timeout_task and not self.stage_timeout_task.done():
                self.stage_timeout_task.cancel()

            # Запускаем новый stage timeout (если включен)
            if self.stage_timeout is not None:
                self.stage_timeout_task = self._create_task(
                    self._stage_timeout_monitor(new_stage), f"stage_timeout_{new_stage.value}"
                )

            # Отмечаем предыдущий этап как завершенный
            if old_stage != ProcessingStage.STARTING:
                self.completed_stages.add(old_stage)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка перехода к этапу {new_stage.value} - {e}")

    # === ОБРАБОТЧИКИ ЭТАПА 1: СКРИНШОТ ===

    async def _on_screenshot_captured(self, event):
        """Скриншот захвачен успешно"""
        try:
            data = event.get("data", {})
            session_id = data.get("session_id")
            screenshot_path = data.get("path")
            normalized_session_id = str(session_id) if session_id is not None else None

            if not self.is_active():
                if normalized_session_id:
                    self._pending_screenshot_by_session[normalized_session_id] = data
                    logger.debug(
                        "📸 ProcessingWorkflow: buffered early screenshot for session=%s (path=%s)",
                        normalized_session_id,
                        screenshot_path,
                    )
                return

            if not self._is_relevant_event(event):
                return

            logger.info(f"📸 ProcessingWorkflow: скриншот захвачен, path={screenshot_path}")

            self.screenshot_captured = True

            if self.current_stage == ProcessingStage.CAPTURING:
                # Переходим к отправке gRPC
                await self._transition_to_stage(ProcessingStage.SENDING_GRPC)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки screenshot.captured - {e}")

    async def _consume_pending_screenshot_for_session(self, session_id: str | None):
        if session_id is None:
            return
        normalized_session_id = str(session_id)
        cached = self._pending_screenshot_by_session.pop(normalized_session_id, None)
        if not cached:
            return

        logger.info(
            "📸 ProcessingWorkflow: using buffered screenshot for session=%s",
            normalized_session_id,
        )
        self.screenshot_captured = True
        if self.current_stage == ProcessingStage.CAPTURING:
            await self._transition_to_stage(ProcessingStage.SENDING_GRPC)

    async def _on_screenshot_error(self, event):
        """Ошибка захвата скриншота"""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            error = data.get("error", "unknown")

            logger.error(f"📸 ProcessingWorkflow: ошибка захвата скриншота - {error}")

            # Продолжаем без скриншота (graceful degradation)
            self.screenshot_captured = False

            if self.current_stage == ProcessingStage.CAPTURING:
                logger.info("📸 ProcessingWorkflow: продолжаем без скриншота")
                await self._transition_to_stage(ProcessingStage.SENDING_GRPC)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки screenshot.error - {e}")

    async def _on_recognition_failed(self, event):
        """Ошибка распознавания речи (например, тишина или неясность)"""
        data = event.get("data", {}) if isinstance(event, dict) else {}
        event_session = data.get("session_id")
        event_session_norm = str(event_session) if event_session is not None else None
        error = data.get("error", "unknown")

        if not self._is_relevant_event(event):
            if event_session_norm is not None:
                self._pending_recognition_failed_by_session[event_session_norm] = {
                    "error": error,
                    "timestamp": datetime.now().isoformat(),
                }
                logger.debug(
                    "🎤 ProcessingWorkflow: buffered recognition_failed for future session=%s "
                    "(error=%s, active_session=%s, active=%s)",
                    event_session_norm,
                    error,
                    self.current_session_id,
                    self.is_active(),
                )
            return

        try:
            logger.warning(
                f"🎤 ProcessingWorkflow: распознавание не удалось ({error}) - помечаем как failed"
            )

            self.recognition_failed = True
            # Если gRPC еще не стартовал, это terminal no-speech ветка:
            # завершаем PROCESSING сразу и не ждём несессионный playback.signal.
            # Важно: событие recognition_failed может прийти, пока workflow ещё в STARTING/CAPTURING
            # (гонка между replay screenshot и запуском цепочки), поэтому проверяем только grpc_started.
            if not self.grpc_started and self.current_stage in {
                ProcessingStage.STARTING,
                ProcessingStage.CAPTURING,
                ProcessingStage.SENDING_GRPC,
            }:
                logger.info(
                    "🎤 ProcessingWorkflow: recognition_failed до grpc.request_started "
                    "(stage=%s) → завершаем цепочку без ожидания playback",
                    self.current_stage.value,
                )
                await self._complete_processing_chain()
                return

            # Иначе сохраняем текущую логику: ждем playback.completed.
            if self.playback_completed:
                await self._complete_processing_chain()

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки recognition_failed - {e}")

    # === ОБРАБОТЧИКИ ЭТАПА 2: GRPC ===

    async def _on_grpc_started(self, event):
        """gRPC запрос начат"""
        if not self._is_relevant_event(event):
            return

        try:
            logger.info("🌐 ProcessingWorkflow: gRPC запрос начат")
            self.grpc_started = True

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки grpc.request_started - {e}")

    async def _on_grpc_completed(self, event):
        """gRPC запрос завершен успешно"""
        if not self._is_relevant_event(event):
            return

        try:
            logger.info("🌐 ProcessingWorkflow: gRPC запрос завершен успешно")

            self.grpc_completed = True

            if self.current_stage == ProcessingStage.SENDING_GRPC:
                # Переходим к воспроизведению (если оно еще не началось)
                if not self.playback_completed:
                    await self._transition_to_stage(ProcessingStage.PLAYING_AUDIO)
                else:
                    # Воспроизведение уже завершено - завершаем цепочку
                    await self._complete_processing_chain()

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки grpc.request_completed - {e}")

    async def _on_grpc_failed(self, event):
        """gRPC запрос завершился ошибкой"""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            error = data.get("error", "unknown")
            error_code = data.get("code")

            logger.error(
                "🌐 ProcessingWorkflow: gRPC запрос завершился ошибкой - %s (code=%s)",
                error,
                error_code,
            )

            self.grpc_completed = False
            normalized_reason = str(error_code or error).strip().replace(" ", "_")
            await self._handle_error(f"grpc_error_{normalized_reason}")

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки grpc.request_failed - {e}")

    # === ОБРАБОТЧИКИ ЭТАПА 3: ВОСПРОИЗВЕДЕНИЕ ===

    async def _on_playback_started(self, event):
        """Воспроизведение началось"""
        if not self._is_relevant_event(event):
            return

        try:
            # 🆕 ПРОВЕРЯЕМ ТИП ВОСПРОИЗВЕДЕНИЯ
            pattern = event.get("data", {}).get("pattern", "")

            if pattern == "welcome_message":
                logger.info("🎵 ProcessingWorkflow: воспроизведение приветствия началось")
                # Для приветствия не нужно переходить в PLAYING_AUDIO этап
                # так как это не полная цепочка обработки
                return

            # Обычная логика для полной цепочки обработки
            logger.info("🔊 ProcessingWorkflow: воспроизведение началось")

            if self.current_stage != ProcessingStage.PLAYING_AUDIO:
                await self._transition_to_stage(ProcessingStage.PLAYING_AUDIO)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки playback.started - {e}")

    async def _on_playback_completed(self, event):
        """Воспроизведение завершено - КЛЮЧЕВОЕ СОБЫТИЕ!"""
        if not self._is_relevant_event(event):
            return

        try:
            # 🆕 ПРОВЕРЯЕМ ТИП ВОСПРОИЗВЕДЕНИЯ
            pattern = event.get("data", {}).get("pattern", "")

            if pattern == "welcome_message":
                logger.info("🎵 ProcessingWorkflow: воспроизведение приветствия завершено")
                # Для приветствия не нужно обрабатывать завершение
                # так как это не полная цепочка обработки
                return

            # Остальная логика для полной цепочки обработки
            logger.info("🔊 ProcessingWorkflow: воспроизведение ЗАВЕРШЕНО - готовы к SLEEPING!")

            self.playback_completed = True

            # Если gRPC тоже завершен ИЛИ распознавание не удалось - завершаем всю цепочку
            if self.grpc_completed or self.recognition_failed:
                await self._complete_processing_chain()
            else:
                logger.info("🔊 ProcessingWorkflow: ждем завершения gRPC...")

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки playback.completed - {e}")

    async def _on_playback_failed(self, event):
        """Ошибка воспроизведения"""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            error = data.get("error", "unknown")

            logger.error(f"🔊 ProcessingWorkflow: ошибка воспроизведения - {error}")

            self.playback_completed = False
            await self._handle_error(f"playback_error_{error}")

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки playback.failed - {e}")

    # === ОБРАБОТЧИКИ ЭТАПА 4: BROWSER ===

    async def _on_browser_action_dispatched(self, event):
        """Browser action dispatched (but Chromium not yet started)"""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            session_id = data.get("session_id")

            logger.info(
                "🌐 ProcessingWorkflow: browser action DISPATCHED (session=%s), "
                "blocking premature chain completion",
                session_id,
            )

            self.action_dispatched = True

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки actions.browser_use.started - {e}")

    async def _on_browser_started(self, event):
        """Browser task начат"""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            task_id = data.get("task_id", "unknown")

            logger.info(f"🌐 ProcessingWorkflow: browser task начат, task_id={task_id}")

            self.browser_active = True
            self.action_dispatched = False  # Browser started, dispatch flag no longer needed

            # Переходим к этапу browser automation
            if self.current_stage != ProcessingStage.BROWSER_AUTOMATION:
                await self._transition_to_stage(ProcessingStage.BROWSER_AUTOMATION)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки browser.started - {e}")

    async def _on_browser_completed(self, event):
        """Browser task завершён успешно."""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            event_type = data.get("type", "unknown")

            logger.info(f"🌐 ProcessingWorkflow: browser task завершён, type={event_type}")

            self.browser_active = False
            self.action_dispatched = False  # Reset dispatch flag on completion

            # Проверяем, можем ли завершить цепочку
            if self.grpc_completed and self.playback_completed:
                await self._complete_processing_chain()
            else:
                logger.info(
                    f"🌐 ProcessingWorkflow: browser завершён, ждём gRPC={self.grpc_completed}, playback={self.playback_completed}"
                )

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки browser.completed - {e}")

    async def _on_browser_cancelled(self, event):
        """Browser task отменён (отдельно от success/failure)."""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            cancel_reason = data.get("cancel_reason") or data.get("reason") or "unknown"

            logger.info(
                "🌐 ProcessingWorkflow: browser task cancelled, reason=%s",
                cancel_reason,
            )

            self.browser_active = False
            self.action_dispatched = False  # Reset dispatch flag on cancellation

            # В текущей архитектуре cancelled терминально закрывает browser-ветку
            # так же, как completed, но с отдельным семантическим логом.
            if self.grpc_completed and self.playback_completed:
                await self._complete_processing_chain()
            else:
                logger.info(
                    "🌐 ProcessingWorkflow: browser cancelled, ждём gRPC=%s, playback=%s",
                    self.grpc_completed,
                    self.playback_completed,
                )

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки browser.cancelled - {e}")

    async def _on_browser_failed(self, event):
        """Browser task завершился ошибкой"""
        if not self._is_relevant_event(event):
            return

        try:
            data = event.get("data", {})
            error = data.get("error", "unknown")

            logger.error(f"🌐 ProcessingWorkflow: browser task ошибка - {error}")

            self.browser_active = False
            self.action_dispatched = False  # Reset dispatch flag on failure

            # Не прерываем всю цепочку при ошибке browser - просто логируем
            # Проверяем, можем ли завершить цепочку
            if self.grpc_completed and self.playback_completed:
                await self._complete_processing_chain()

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки browser.failed - {e}")

    # === ПРЕРЫВАНИЯ ===

    async def _on_interrupt_request(self, event):
        """Обработка запроса прерывания"""
        # КРИТИЧНО: Прерывание должно работать даже если workflow не активен (но воспроизведение идет)
        # Проверяем только interrupted, чтобы избежать повторной обработки
        if self.interrupted:
            logger.debug(f"⚙️ ProcessingWorkflow: прерывание уже обработано, игнорируем дубликат")
            return

        try:
            data = event.get("data", {})
            reason = data.get("reason", "user_interrupt")
            session_id = data.get("session_id")
            normalized_interrupt_sid = str(session_id) if session_id is not None else None

            # КРИТИЧНО: Проверяем, что прерывание относится к текущей активной сессии
            # Если workflow активен с другой сессией, игнорируем прерывание
            if self.is_active() and self.current_session_id is not None and session_id is not None:
                if session_id != self.current_session_id:
                    logger.debug(
                        f"⚙️ ProcessingWorkflow: игнорируем прерывание для другой сессии (current={self.current_session_id}, interrupt={session_id})"
                    )
                    return

            logger.info(
                f"⚙️ ProcessingWorkflow: получен запрос ПРЕРЫВАНИЯ, reason={reason}, stage={self.current_stage.value if hasattr(self, 'current_stage') else 'unknown'}, active={self.is_active()}"
            )

            self.interrupted = True

            # Отменяем все таймауты
            await self._cancel_timeout_tasks()

            # Публикуем события отмены для всех активных процессов
            await self._cancel_active_processes()

            # Немедленный возврат в SLEEPING (только если workflow активен)
            if self.is_active():
                # Centralization: mode transition on interrupt is owned by
                # InterruptManagementIntegration (single mode.request path).
                await self._cleanup_processing()
            else:
                # Если workflow не активен, mode.request не публикуем:
                # его публикует InterruptManagementIntegration.
                if (
                    normalized_interrupt_sid is not None
                    and self._terminal_outcome_session_id == normalized_interrupt_sid
                ):
                    logger.debug(
                        "⚙️ ProcessingWorkflow: interrupt duplicate after terminal outcome, "
                        "skip mode.request (session=%s, reason=%s)",
                        normalized_interrupt_sid,
                        reason,
                    )
                    return
                logger.info(
                    "⚙️ ProcessingWorkflow: workflow не активен, "
                    "mode.request на interrupt делегирован InterruptManagementIntegration"
                )

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки прерывания - {e}")

    async def _cancel_active_processes(self):
        """Отмена всех активных процессов через ЕДИНЫЙ канал прерывания.

        Владелец отмены: InterruptManagementIntegration.
        ProcessingWorkflow не публикует grpc.request_cancel/playback.cancelled напрямую,
        чтобы не создавать дублирующий путь прерывания.
        """
        try:
            session_id = self.current_session_id
            logger.info(
                "⚙️ ProcessingWorkflow: прерывание делегировано через interrupt.request "
                "(session_id=%s), прямые cancel-события не публикуем",
                session_id,
            )

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка отмены процессов - {e}")

    # === ЗАВЕРШЕНИЕ ЦЕПОЧКИ ===

    async def _complete_processing_chain(self):
        """Успешное завершение всей цепочки обработки"""
        try:
            # Reentrancy guard: prevent double-fire from concurrent EventBus callbacks
            if getattr(self, '_completing', False):
                logger.debug("⚙️ ProcessingWorkflow: _complete_processing_chain already in progress, skipping")
                return
            self._completing = True

            # КРИТИЧНО: Не завершаем пока browser активен
            if self.browser_active:
                logger.info("⏳ ProcessingWorkflow: ждём завершения browser task...")
                return

            # КРИТИЧНО: Не завершаем если browser action диспатчен, но ещё не стартовал.
            # Race condition fix: Chromium может стартовать медленнее, чем TTS доиграет.
            if self.action_dispatched:
                logger.info(
                    "⏳ ProcessingWorkflow: browser action dispatched but not yet started, "
                    "waiting for browser.started..."
                )
                return

            duration = (
                (datetime.now() - self.processing_start_time).total_seconds()
                if self.processing_start_time
                else 0
            )

            if self.recognition_failed:
                logger.info(
                    f"✅ ProcessingWorkflow: цепочка ЗАВЕРШЕНА (failed path) за {duration:.2f}с"
                )
            else:
                logger.info(f"✅ ProcessingWorkflow: цепочка ЗАВЕРШЕНА успешно за {duration:.2f}с")
            logger.info(
                f"📊 ProcessingWorkflow: скриншот={self.screenshot_captured}, gRPC={self.grpc_completed}, воспроизведение={self.playback_completed}, browser={not self.browser_active}"
            )

            await self._transition_to_stage(ProcessingStage.COMPLETING)

            # Возвращаемся в SLEEPING
            terminal_reason = "failed_recognition" if self.recognition_failed else "completed"
            await self._return_to_sleeping(terminal_reason)

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка завершения цепочки - {e}")
        finally:
            self._completing = False

    async def _handle_error(self, error_type: str):
        """Обработка ошибки в цепочке"""
        try:
            logger.error(
                f"❌ ProcessingWorkflow: обработка ошибки {error_type} на этапе {self.current_stage.value}"
            )

            # Отменяем таймауты
            await self._cancel_timeout_tasks()

            # Возвращаемся в SLEEPING
            await self._return_to_sleeping(f"error_{error_type}")

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка обработки ошибки - {e}")

    async def _return_to_sleeping(self, reason: str):
        """Координированный возврат в SLEEPING"""
        try:
            normalized_current_sid = (
                str(self.current_session_id) if self.current_session_id is not None else None
            )
            if (
                normalized_current_sid is not None
                and self._terminal_outcome_session_id == normalized_current_sid
            ):
                logger.debug(
                    "⚙️ ProcessingWorkflow: terminal outcome duplicate ignored "
                    "(session=%s, reason=%s, first_reason=%s)",
                    normalized_current_sid,
                    reason,
                    self._terminal_outcome_reason,
                )
                return
            if normalized_current_sid is not None:
                self._terminal_outcome_session_id = normalized_current_sid
                self._terminal_outcome_reason = reason
                terminal_result = (
                    "failed"
                    if reason.startswith("failed") or reason.startswith("error_")
                    else "success"
                )
                await self.event_bus.publish(
                    "processing.terminal",
                    {
                        "session_id": normalized_current_sid,
                        "result": terminal_result,
                        "reason": reason,
                        "source": "ProcessingWorkflow",
                    },
                )

            logger.info(
                "⚙️ ProcessingWorkflow: terminal outcome emitted, "
                "mode.request SLEEPING делегирован ModeManagementIntegration "
                "(reason=%s)",
                reason,
            )

            await self._cleanup_processing()

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка возврата в SLEEPING - {e}")

    async def _cleanup_processing(self):
        """Очистка состояния после завершения обработки"""
        try:
            # Отменяем все таймауты
            await self._cancel_timeout_tasks()

            # Сбрасываем состояние
            self.current_session_id = None
            self.current_stage = ProcessingStage.STARTING
            self.processing_start_time = None
            self.stage_start_time = None
            self.completed_stages.clear()
            self.state = WorkflowState.IDLE

            # Сбрасываем флаги
            self.screenshot_captured = False
            self.grpc_completed = False
            self.recognition_failed = False
            self.playback_completed = False
            self.interrupted = False
            self.browser_active = False
            self.action_dispatched = False
            self.grpc_started = False
            self._completing = False

            logger.debug("⚙️ ProcessingWorkflow: состояние очищено")

        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка очистки - {e}")

    # === МОНИТОРИНГ И ТАЙМАУТЫ ===

    async def _stage_timeout_monitor(self, stage: ProcessingStage):
        """Мониторинг таймаута этапа"""
        try:
            if self.stage_timeout is None:
                return
            await asyncio.sleep(self.stage_timeout)

            if self.current_stage == stage and not self.interrupted:
                logger.warning(
                    f"⏰ ProcessingWorkflow: таймаут этапа {stage.value} ({self.stage_timeout}с)"
                )
                await self._handle_error(f"stage_timeout_{stage.value}")

        except asyncio.CancelledError:
            logger.debug(f"⚙️ ProcessingWorkflow: мониторинг этапа {stage.value} отменен")
        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка мониторинга этапа - {e}")

    async def _total_timeout_monitor(self, session_id: str):
        """Мониторинг общего таймаута"""
        try:
            await asyncio.sleep(self.total_timeout)

            if self.current_session_id == session_id and not self.interrupted:
                logger.warning(f"⏰ ProcessingWorkflow: общий таймаут ({self.total_timeout}с)")
                await self._handle_error("total_timeout")

        except asyncio.CancelledError:
            logger.debug(f"⚙️ ProcessingWorkflow: общий мониторинг отменен")
        except Exception as e:
            logger.error(f"❌ ProcessingWorkflow: ошибка общего мониторинга - {e}")

    async def _cancel_timeout_tasks(self):
        """Отмена всех таймаутов"""
        if self.stage_timeout_task and not self.stage_timeout_task.done():
            self.stage_timeout_task.cancel()

        if self.total_timeout_task and not self.total_timeout_task.done():
            self.total_timeout_task.cancel()

    # === УТИЛИТЫ ===

    def _is_relevant_event(self, event) -> bool:
        """Проверка релевантности события"""
        if not self.is_active():
            return False

        # Фильтрация по сессии
        data = event.get("data", {})
        event_session = data.get("session_id")

        # КРИТИЧНО: Если current_session_id есть, а event_session нет - событие не релевантно
        # Это предотвращает завершение чужой цепочки PROCESSING
        if self.current_session_id and event_session is None:
            return False

        if self.current_session_id and event_session:
            return event_session == self.current_session_id

        return True

    def get_processing_duration(self) -> float | None:
        """Получение длительности обработки"""
        if self.processing_start_time:
            return (datetime.now() - self.processing_start_time).total_seconds()
        return None

    def get_stage_duration(self) -> float | None:
        """Получение длительности текущего этапа"""
        if self.stage_start_time:
            return (datetime.now() - self.stage_start_time).total_seconds()
        return None

    def get_status(self) -> dict[str, Any]:
        """Расширенный статус workflow'а"""
        base_status = super().get_status()
        base_status.update(
            {
                "current_stage": self.current_stage.value,
                "processing_duration": self.get_processing_duration(),
                "stage_duration": self.get_stage_duration(),
                "completed_stages": [stage.value for stage in self.completed_stages],
                "screenshot_captured": self.screenshot_captured,
                "grpc_completed": self.grpc_completed,
                "recognition_failed": self.recognition_failed,
                "playback_completed": self.playback_completed,
                "interrupted": self.interrupted,
            }
        )
        return base_status
