"""
Browser Use Module - реальная реализация с browser-use Agent

Feature ID: F-2025-015-browser-use
"""

import asyncio
import logging
import uuid
from typing import Dict, Any, AsyncIterator, Optional
from datetime import datetime

from modules.browser_use.constants import FEATURE_ID

logger = logging.getLogger(__name__)

# Попытка импорта browser-use
try:
    from browser_use import Agent, ChatGoogle
    from browser_use.browser.profile import BrowserProfile
    BROWSER_USE_AVAILABLE = True
except ImportError:
    BROWSER_USE_AVAILABLE = False
    logger.warning(f"[{FEATURE_ID}] browser-use not installed, using stub mode")


class BrowserUseModule:
    """
    Модуль для выполнения browser-use задач
    
    Интегрируется с browser-use Agent для автоматизации браузера.
    """
    
    def __init__(self):
        """Инициализация модуля"""
        self._config: Dict[str, Any] = {}
        self._active_tasks: Dict[str, Any] = {}  # task_id -> agent/worker
        self._initialized = False
        self._interrupt_workflow = None  # Будет установлен извне
        
        # Persistent browser session support
        self._persistent_session = None  # Shared BrowserSession instance
        self._keep_browser_open = False  # Config flag

    
    def _format_action_description(self, agent_output, browser_state) -> str:
        """
        Формирует человекочитаемое описание действия на основе agent_output и browser_state.
        
        Приоритеты источников данных:
        1. agent_output.memory - описание от LLM (извлекаем только выполненное действие до "Now I need")
        2. agent_output.actions[0] - структурированные данные (если memory не дало результата)
        3. browser_state.url - только как последний fallback (НЕ используется для скролла/ввода/клика)
        
        Args:
            agent_output: Выходные данные Agent с информацией о действиях
            browser_state: Состояние браузера (URL и т.д.)
        
        Returns:
            Строка с описанием действия
        """
        import re
        
        descriptions = []
        
        # ПРИОРИТЕТ 1: Используем memory от LLM и извлекаем только выполненное действие
        # memory содержит: "I have successfully navigated to YouTube. Now I need to..."
        # Извлекаем только первую часть до "Now I need" или "I need to"
        if agent_output and hasattr(agent_output, 'memory') and agent_output.memory:
            memory_text = agent_output.memory.strip()
            if memory_text:
                # Паттерн: "I have successfully..." или "I have..." до "Now I need" или "I need to"
                # Или просто первое предложение, если нет маркеров плана
                match = re.search(
                    r'I have (?:successfully )?([^.]*(?:\.|$))(?:\s*(?:Now I need|I need to|Next I will|I will))?',
                    memory_text,
                    re.IGNORECASE
                )
                if match:
                    completed_action = match.group(1).strip()
                    if completed_action:
                        descriptions.append(completed_action)
                else:
                    # Если паттерн не найден, берем первое предложение
                    first_sentence = memory_text.split('.')[0]
                    if first_sentence and len(first_sentence) > 10:  # Минимум 10 символов
                        descriptions.append(first_sentence + '.')
        
        # ПРИОРИТЕТ 2: Используем структурированные данные из actions[0] как fallback
        if not descriptions and agent_output and hasattr(agent_output, 'actions') and agent_output.actions:
            action = agent_output.actions[0]
            
            # Определяем тип действия через атрибуты объекта
            action_type = None
            if hasattr(action, 'action_type'):
                action_type = str(action.action_type).lower()
            elif hasattr(action, 'type'):
                action_type = str(action.type).lower()
            elif hasattr(action, '__class__'):
                action_type = action.__class__.__name__.lower()
            
            # Обработка разных типов действий через структурированные атрибуты
            if action_type and 'navigate' in action_type:
                url = None
                if hasattr(action, 'url'):
                    url = action.url
                elif hasattr(action, 'target_url'):
                    url = action.target_url
                
                if url:
                    try:
                        from urllib.parse import urlparse
                        parsed = urlparse(url)
                        domain = parsed.netloc.replace('www.', '')
                        if domain.startswith('www.'):
                            domain = domain[4:]
                        descriptions.append(f"Navigated to {domain}")
                    except:
                        descriptions.append(f"Navigated to {url}")
                elif browser_state and hasattr(browser_state, 'url') and browser_state.url and browser_state.url != 'about:blank':
                    try:
                        from urllib.parse import urlparse
                        parsed = urlparse(browser_state.url)
                        domain = parsed.netloc.replace('www.', '')
                        if domain.startswith('www.'):
                            domain = domain[4:]
                        descriptions.append(f"Navigated to {domain}")
                    except:
                        descriptions.append(f"Navigated to {browser_state.url}")
                else:
                    descriptions.append("Navigated to website")
            
            elif action_type and ('input' in action_type or 'type' in action_type):
                text = None
                if hasattr(action, 'text'):
                    text = action.text
                elif hasattr(action, 'input_text'):
                    text = action.input_text
                
                if text:
                    if len(text) > 50:
                        text = text[:47] + "..."
                    descriptions.append(f"Typed '{text}'")
                else:
                    descriptions.append("Entered text")
            
            elif action_type and 'click' in action_type:
                label = None
                if hasattr(action, 'aria_label'):
                    label = action.aria_label
                elif hasattr(action, 'label'):
                    label = action.label
                elif hasattr(action, 'text'):
                    label = action.text
                
                if label:
                    if len(label) > 30:
                        label = label[:27] + "..."
                    descriptions.append(f"Clicked on {label}")
                else:
                    descriptions.append("Clicked on element")
            
            elif action_type and 'done' in action_type:
                text = None
                if hasattr(action, 'text'):
                    text = action.text
                elif hasattr(action, 'result_text'):
                    text = action.result_text
                
                if text:
                    descriptions.append(text)
                else:
                    descriptions.append("Task completed")
            
            elif action_type and 'scroll' in action_type:
                descriptions.append("Scrolled page")
            
            elif action_type and 'wait' in action_type:
                descriptions.append("Waiting for page to load")
        
        # ПРИОРИТЕТ 3: Используем browser_state.url только как последний fallback
        # НЕ используем для скролла/ввода/клика, только если действительно нет других данных
        current_url = None
        if browser_state and hasattr(browser_state, 'url') and browser_state.url:
            current_url = browser_state.url
        
        if not descriptions and current_url and current_url != 'about:blank':
            try:
                from urllib.parse import urlparse
                parsed = urlparse(current_url)
                domain = parsed.netloc.replace('www.', '')
                if domain.startswith('www.'):
                    domain = domain[4:]
                descriptions.append(f"Navigated to {domain}")
            except:
                descriptions.append(f"Navigated to {current_url}")
        
        # Если все еще ничего не нашли, используем общее описание
        if not descriptions:
            descriptions.append("Step completed")
        
        result = ". ".join(descriptions) if descriptions else "Step completed"
        
        # Логируем для отладки
        logger.info(f"[{FEATURE_ID}] Formatted action description: '{result}' (url={current_url})")
        
        return result
    
    async def initialize(self, config: dict) -> None:
        """
        Инициализация модуля
        
        Args:
            config: Конфигурация модуля (из unified_config)
        """
        try:
            self._config = config
            
            # Read keep_browser_open config
            self._keep_browser_open = config.get('keep_browser_open', False)
            logger.info(f"[{FEATURE_ID}] keep_browser_open={self._keep_browser_open}")
            
            if not BROWSER_USE_AVAILABLE:
                logger.warning(f"[{FEATURE_ID}] browser-use not available, module will use stub mode")
            
            self._initialized = True
            logger.info(f"[{FEATURE_ID}] BrowserUseModule initialized")
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Ошибка инициализации: {e}")
            raise
    
    async def process(self, request: Dict[str, Any]) -> AsyncIterator[Dict[str, Any]]:
        """
        Обработка запроса на выполнение browser-use задачи
        
        Args:
            request: Запрос на выполнение задачи
                - args: Dict[str, Any] - аргументы команды (task, config_preset)
                - session_id: str - идентификатор сессии
                - hardware_id: str - идентификатор оборудования
                - feature_id: str - идентификатор фичи
        
        Yields:
            События прогресса browser-use задачи
        """
        task_id = f"task_{uuid.uuid4().hex[:12]}"
        task = request.get('args', {}).get('task', 'Unknown task')
        session_id = request.get('session_id', 'unknown')
        hardware_id = request.get('hardware_id', 'unknown')
        config_preset = request.get('args', {}).get('config_preset', 'fast')
        
        logger.info(f"[{FEATURE_ID}] Process called: task={task[:50]}, session_id={session_id}, task_id={task_id}")
        
        # Проверка доступности browser-use
        if not BROWSER_USE_AVAILABLE:
            logger.warning(f"[{FEATURE_ID}] browser-use not available, returning stub events")
            yield {
                'type': 'BROWSER_TASK_STARTED',
                'task_id': task_id,
                'description': f'Browser task started (stub - browser-use not installed): {task}',
                'timestamp': datetime.now().isoformat()
            }
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'description': 'Browser-use library not installed. Please install: pip install browser-use playwright && playwright install chromium',
                'error': 'browser-use not installed',
                'timestamp': datetime.now().isoformat()
            }
            return
        
        # Регистрация в InterruptWorkflowIntegration (если доступен)
        if self._interrupt_workflow and session_id:
            self._interrupt_workflow.active_sessions[session_id] = {
                'hardware_id': hardware_id,
                'start_time': datetime.now(),
                'status': 'processing',
                'task_type': 'browser_use',
                'task_id': task_id
            }
        
        try:
            # Событие: задача начата
            yield {
                'type': 'BROWSER_TASK_STARTED',
                'task_id': task_id,
                'description': f'Starting browser automation: {task}',
                'timestamp': datetime.now().isoformat()
            }
            
            # Запуск Agent
            async for progress in self._run_agent(task, task_id, session_id, hardware_id, config_preset):
                yield progress
                
        except asyncio.CancelledError:
            logger.info(f"[{FEATURE_ID}] Task cancelled: task_id={task_id}")
            yield {
                'type': 'BROWSER_TASK_CANCELLED',
                'task_id': task_id,
                'description': 'Task cancelled by user',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Task failed: task_id={task_id}, error={e}")
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'description': f'Task failed: {str(e)}',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
        finally:
            # Очистка
            if task_id in self._active_tasks:
                del self._active_tasks[task_id]
            if self._interrupt_workflow and session_id:
                try:
                    await self._interrupt_workflow._cleanup_session(session_id)
                except:
                    pass
    
    async def _run_agent(
        self,
        task: str,
        task_id: str,
        session_id: str,
        hardware_id: str,
        config_preset: str
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Запуск browser-use Agent с обработкой событий
        
        Args:
            task: Описание задачи
            task_id: Идентификатор задачи
            session_id: Идентификатор сессии
            hardware_id: Идентификатор оборудования
            config_preset: Пресет конфигурации (ultra_fast, fast, standard)
        """
        if not BROWSER_USE_AVAILABLE:
            return
        
        # Получение конфигурации
        agent_config = self._get_agent_config(config_preset)
        
        # Создание LLM
        try:
            llm = self._create_llm()
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Ошибка создания LLM: {e}")
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'description': f'Failed to create LLM: {str(e)}',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
            return
        
        # Создание Agent
        try:
            # 1. Reuse existing persistent session if available
            browser_session = None
            if self._keep_browser_open and self._persistent_session:
                browser_session = self._persistent_session
                logger.info(f"[{FEATURE_ID}] Reusing persistent browser session: {browser_session}")

            # 2. Or create new profile with keep_alive=True if we need a new session
            browser_profile = None
            if not browser_session and self._keep_browser_open and BROWSER_USE_AVAILABLE:
                try:
                    # Explicitly create profile with keep_alive=True to prevent BrowserStopEvent 
                    # from resetting the session (clearing listeners and closing browser)
                    browser_profile = BrowserProfile(keep_alive=True)
                    logger.info(f"[{FEATURE_ID}] Created new persistent BrowserProfile (keep_alive=True)")
                except Exception as e:
                    logger.warning(f"[{FEATURE_ID}] Failed to create BrowserProfile: {e}")

            agent = Agent(
                task=task,
                llm=llm,
                browser_session=browser_session,
                browser_profile=browser_profile,
                **agent_config
            )
            
            # Store session for next time if persistence is enabled
            if self._keep_browser_open and not self._persistent_session:
                 # Check if agent has created a session
                 if hasattr(agent, 'browser_session') and agent.browser_session:
                     self._persistent_session = agent.browser_session
                     logger.info(f"[{FEATURE_ID}] Captured new persistent session")

            self._active_tasks[task_id] = agent
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Ошибка создания Agent: {e}")
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'description': f'Failed to create Agent: {str(e)}',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
            return
        
        # Очередь для событий
        event_queue = asyncio.Queue()
        step_number = 0
        task_completed = False
        
        # Callback для новых шагов (может быть sync или async)
        # browser-use поддерживает оба варианта
        async def step_callback_async(browser_state, agent_output, step_num):
            """Async callback для каждого шага Agent"""
            nonlocal step_number
            step_number = step_num
            
            # Детальное логирование для отладки
            logger.info(f"[{FEATURE_ID}] Step {step_num} callback called")
            if agent_output:
                logger.info(f"[{FEATURE_ID}] agent_output type: {type(agent_output)}")
                logger.info(f"[{FEATURE_ID}] agent_output attributes: {dir(agent_output)}")
                if hasattr(agent_output, 'actions'):
                    logger.info(f"[{FEATURE_ID}] agent_output.actions: {agent_output.actions}")
                    if agent_output.actions:
                        action = agent_output.actions[0]
                        logger.info(f"[{FEATURE_ID}] action type: {type(action)}, action: {action}")
                        logger.info(f"[{FEATURE_ID}] action attributes: {dir(action) if hasattr(action, '__dict__') else 'no __dict__'}")
                        if hasattr(action, '__dict__'):
                            logger.info(f"[{FEATURE_ID}] action.__dict__: {action.__dict__}")
                if hasattr(agent_output, 'memory'):
                    logger.info(f"[{FEATURE_ID}] agent_output.memory: {agent_output.memory}")
                if hasattr(agent_output, 'next_goal'):
                    logger.info(f"[{FEATURE_ID}] agent_output.next_goal: {agent_output.next_goal}")
            if browser_state:
                logger.info(f"[{FEATURE_ID}] browser_state type: {type(browser_state)}")
                if hasattr(browser_state, 'url'):
                    logger.info(f"[{FEATURE_ID}] browser_state.url: {browser_state.url}")
            
            # Формируем детальное описание действия
            action_description = self._format_action_description(agent_output, browser_state)
            
            # Формирование события
            event = {
                'type': 'BROWSER_STEP_COMPLETED',
                'task_id': task_id,
                'step_number': step_num,
                'description': action_description,
                'timestamp': datetime.now().isoformat()
            }
            
            # Добавление URL и действия, если доступны
            if hasattr(browser_state, 'url') and browser_state.url:
                event['url'] = browser_state.url
            if agent_output and hasattr(agent_output, 'actions'):
                if agent_output.actions:
                    event['action'] = str(agent_output.actions[0])[:100]
            
            await event_queue.put(event)
        
        def step_callback_sync(browser_state, agent_output, step_num):
            """Sync callback для каждого шага Agent"""
            nonlocal step_number
            step_number = step_num
            
            # Формируем детальное описание действия
            action_description = self._format_action_description(agent_output, browser_state)
            
            # Формирование события
            event = {
                'type': 'BROWSER_STEP_COMPLETED',
                'task_id': task_id,
                'step_number': step_num,
                'description': action_description,
                'timestamp': datetime.now().isoformat()
            }
            
            # Добавление URL и действия, если доступны
            if hasattr(browser_state, 'url') and browser_state.url:
                event['url'] = browser_state.url
            if agent_output and hasattr(agent_output, 'actions'):
                if agent_output.actions:
                    event['action'] = str(agent_output.actions[0])[:100]
            
            # Добавляем в очередь (неблокирующе)
            try:
                event_queue.put_nowait(event)
            except asyncio.QueueFull:
                logger.warning(f"[{FEATURE_ID}] Event queue full, dropping event")
        
        # Callback для завершения
        async def done_callback_async(history):
            """Async callback при завершении задачи"""
            nonlocal task_completed
            task_completed = True
            await event_queue.put({
                'type': 'BROWSER_TASK_COMPLETED',
                'task_id': task_id,
                'description': 'Task completed successfully',
                'timestamp': datetime.now().isoformat()
            })
        
        def done_callback_sync(history):
            """Sync callback при завершении задачи"""
            nonlocal task_completed
            task_completed = True
            try:
                event_queue.put_nowait({
                    'type': 'BROWSER_TASK_COMPLETED',
                    'task_id': task_id,
                    'description': 'Task completed successfully',
                    'timestamp': datetime.now().isoformat()
                })
            except asyncio.QueueFull:
                logger.warning(f"[{FEATURE_ID}] Event queue full, dropping done event")
        
        # Установка callbacks (используем async версии, browser-use поддерживает оба)
        agent.register_new_step_callback = step_callback_async
        agent.register_done_callback = done_callback_async
        
        # Запуск Agent в фоне
        agent_task = asyncio.create_task(agent.run(max_steps=self._config.get('max_steps', 20)))
        
        try:
            # Стриминг событий
            while True:
                # Проверка прерывания
                if self._interrupt_workflow:
                    if await self._interrupt_workflow.check_interrupts(hardware_id):
                        logger.info(f"[{FEATURE_ID}] Interrupt detected, cancelling agent")
                        agent_task.cancel()
                        yield {
                            'type': 'BROWSER_TASK_CANCELLED',
                            'task_id': task_id,
                            'description': 'Task cancelled by user',
                            'timestamp': datetime.now().isoformat()
                        }
                        return
                
                # Проверка завершения
                if agent_task.done():
                    try:
                        await agent_task  # Получаем результат или исключение
                    except Exception as e:
                        logger.error(f"[{FEATURE_ID}] Agent task failed: {e}")
                        yield {
                            'type': 'BROWSER_TASK_FAILED',
                            'task_id': task_id,
                            'description': f'Agent execution failed: {str(e)}',
                            'error': str(e),
                            'timestamp': datetime.now().isoformat()
                        }
                    break
                
                # Получение событий из очереди
                try:
                    event = await asyncio.wait_for(event_queue.get(), timeout=0.1)
                    yield event
                except asyncio.TimeoutError:
                    continue
                    
        except asyncio.CancelledError:
            logger.info(f"[{FEATURE_ID}] Agent task cancelled: task_id={task_id}")
            agent_task.cancel()
            try:
                await agent_task
            except asyncio.CancelledError:
                pass
            yield {
                'type': 'BROWSER_TASK_CANCELLED',
                'task_id': task_id,
                'description': 'Task cancelled',
                'timestamp': datetime.now().isoformat()
            }
        finally:
            # Очистка браузера
            await self._cleanup_browser_context(agent, task_id)
    
    def _create_llm(self):
        """Создание LLM для Agent"""
        from config.unified_config import get_config
        
        config = get_config()
        api_key = config.text_processing.gemini_api_key
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY not configured")
        
        return ChatGoogle(
            model="gemini-2.5-flash",
            api_key=api_key
        )
    
    def _get_agent_config(self, config_preset: str) -> Dict[str, Any]:
        """Получение конфигурации Agent по пресету"""
        # Базовые настройки из конфигурации
        base_config = {
            'llm_timeout': self._config.get('llm_timeout', 120),
            'step_timeout': self._config.get('step_timeout', 180),
            'use_vision': self._config.get('use_vision', True),
            'max_actions_per_step': 5,
            'use_thinking': False,
            'flash_mode': True,
            'max_failures': 2,
            'retry_delay': 5,
            # Prevent browser-use library from closing browser automatically
            'close_browser_on_done': not self._keep_browser_open
        }
        
        # Пресеты
        if config_preset == 'ultra_fast':
            base_config.update({
                'llm_timeout': 60,
                'step_timeout': 90,
                'max_actions_per_step': 3,
                'flash_mode': True
            })
        elif config_preset == 'fast':
            base_config.update({
                'llm_timeout': 120,
                'step_timeout': 180,
                'max_actions_per_step': 5
            })
        elif config_preset == 'standard':
            base_config.update({
                'llm_timeout': 180,
                'step_timeout': 300,
                'max_actions_per_step': 10,
                'use_thinking': True,
                'flash_mode': False
            })
        
        return base_config
    
    async def _cleanup_browser_context(self, agent, task_id: str, force: bool = False):
        """
        Очистка контекста браузера
        
        Args:
            agent: Agent instance
            task_id: ID задачи
            force: Если True, принудительно закрыть браузер даже при keep_browser_open=True
        """
        # Skip cleanup if persistence is enabled and not forced
        if self._keep_browser_open and not force:
            logger.info(f"[{FEATURE_ID}] Skipping browser cleanup (keep_browser_open=True) for task_id={task_id}")
            # Ensure we have the reference stored
            if agent and hasattr(agent, 'browser_session') and not self._persistent_session:
                self._persistent_session = agent.browser_session
                logger.debug(f"[{FEATURE_ID}] Saved persistent session reference")
            return
        
        try:
            logger.info(f"[{FEATURE_ID}] Closing browser session (force={force})")
            
            # Use the explicit close() method we added or standard cleanup
            if self._persistent_session:
                 # If we have a stored session, close it explicitly
                 try:
                     # Depending on browser-use version, it might be close() or kill() or reset()
                     # But Agent usually handles this. If we are here, we want to destroy it.
                     if hasattr(self._persistent_session, 'close'):
                         await self._persistent_session.close()
                     elif hasattr(self._persistent_session, 'kill'):
                         await self._persistent_session.kill()
                 except Exception as e:
                     logger.warning(f"[{FEATURE_ID}] Error closing persistent session: {e}")
                 finally:
                     self._persistent_session = None

            elif agent and hasattr(agent, 'browser_session'):
                # Fallback for non-persistent or generic cleanup
                browser_session = agent.browser_session
                if browser_session:
                    try:
                        if hasattr(browser_session, 'close'):
                             await browser_session.close()
                    except Exception as e:
                        logger.error(f"[{FEATURE_ID}] Error closing browser session: {e}")
        
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Error in cleanup_browser_context: {e}")

    async def close_browser(self):
        """
        Explicitly close the persistent browser session.
        Called by the 'close_browser' command.
        """
        if self._persistent_session:
            logger.info(f"[{FEATURE_ID}] Explicitly closing persistent browser...")
            try:
                if hasattr(self._persistent_session, 'close'):
                    await self._persistent_session.close()
                elif hasattr(self._persistent_session, 'kill'):
                     await self._persistent_session.kill()
            except Exception as e:
                logger.error(f"[{FEATURE_ID}] Error forcing close on persistent browser: {e}")
            finally:
                self._persistent_session = None
        else:
            logger.info(f"[{FEATURE_ID}] No persistent browser to close.")
        

    
    async def cleanup(self) -> None:
        """Очистка всех активных задач при shutdown"""
        logger.info(f"[{FEATURE_ID}] Starting cleanup for BrowserUseModule")
        
        cleanup_tasks = []
        for task_id, agent in list(self._active_tasks.items()):
            if agent:
                cleanup_tasks.append(self._cleanup_browser_context(agent, task_id))
        
        if cleanup_tasks:
            try:
                await asyncio.wait_for(
                    asyncio.gather(*cleanup_tasks, return_exceptions=True),
                    timeout=10.0
                )
            except asyncio.TimeoutError:
                logger.warning(f"[{FEATURE_ID}] Timeout during cleanup, forcing close")
        
        self._active_tasks.clear()
        logger.info(f"[{FEATURE_ID}] Cleanup completed")
    
    def status(self):
        """Получение статуса модуля"""
        from integrations.core.module_status import ModuleStatus, ModuleState
        
        if not self._initialized:
            return ModuleStatus(state=ModuleState.INIT)
        
        if not BROWSER_USE_AVAILABLE:
            return ModuleStatus(state=ModuleState.READY, health="degraded", last_error="browser-use not installed")
        
        return ModuleStatus(state=ModuleState.READY, health="ok")
    
    def set_interrupt_workflow(self, interrupt_workflow):
        """Установка InterruptWorkflowIntegration (вызывается извне)"""
        self._interrupt_workflow = interrupt_workflow
