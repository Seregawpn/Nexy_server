"""
Browser Use Module - Client Side Implementation

Feature ID: F-2025-015-browser-use
"""

import asyncio
from datetime import datetime
import logging
import os
import sys
from typing import Any, AsyncIterator
import uuid

from config.unified_config_loader import unified_config as global_config
from integration.utils.resource_path import get_user_data_dir
from modules.browser_automation.constants import FEATURE_ID

logger = logging.getLogger(__name__)

# Lazy import for browser-use (allows hot-detection without restart)
_browser_use_module_cache = {}

def _check_browser_use_available():
    """
    Dynamically check if browser-use is available.
    This allows detecting newly installed packages without app restart.
    """
    if 'available' in _browser_use_module_cache:
        return _browser_use_module_cache['available']
    
    try:
        # Direct import - no shadowing issue since we renamed local module to browser_automation
        from browser_use import Agent
        from browser_use.browser.profile import BrowserProfile
        from langchain_google_genai import ChatGoogleGenerativeAI as ChatGoogle
        
        _browser_use_module_cache['Agent'] = Agent
        _browser_use_module_cache['ChatGoogle'] = ChatGoogle
        _browser_use_module_cache['BrowserProfile'] = BrowserProfile
        _browser_use_module_cache['available'] = True
        logger.info(f"[{FEATURE_ID}] browser-use detected and loaded successfully")
        return True
        
    except ImportError as e:
        logger.warning(f"[{FEATURE_ID}] browser-use not installed: {e}")
        _browser_use_module_cache['available'] = False
        return False

def _get_browser_use_classes():
    """Get cached browser-use classes after availability check."""
    return (
        _browser_use_module_cache.get('Agent'),
        _browser_use_module_cache.get('ChatGoogle'),
        _browser_use_module_cache.get('BrowserProfile')
    )

def _reset_browser_use_cache():
    """Reset cache to force re-check (useful after pip install)."""
    _browser_use_module_cache.clear()
    logger.info(f"[{FEATURE_ID}] browser-use cache cleared, will re-check on next use")


class GeminiLLMAdapter:
    """
    Adapter to make langchain ChatGoogleGenerativeAI compatible with 
    browser-use's BaseChatModel Protocol.
    
    browser-use expects: provider, name, model properties and ainvoke method.
    """
    
    def __init__(self, api_key: str, model: str, tts_callback=None, usage_callback=None):
        from langchain_google_genai import ChatGoogleGenerativeAI
        self._llm = ChatGoogleGenerativeAI(model=model, api_key=api_key)
        self._model = model
        self._api_key = api_key
        self.tts_callback = tts_callback
        self.usage_callback = usage_callback
    
    @property
    def provider(self) -> str:
        return "google"
    
    @property
    def name(self) -> str:
        return f"google/{self._model}"
    
    @property
    def model(self) -> str:
        return self._model
    
    @property
    def model_name(self) -> str:
        return self._model
    
    async def ainvoke(self, messages, output_format=None, **kwargs):
        """
        Invoke the LLM with messages.
        
        This converts browser-use message format to langchain format and back.
        Uses with_structured_output for proper schema binding when output_format is provided.
        """
        try:
            from browser_use.llm.views import ChatInvokeCompletion, ChatInvokeUsage
            from langchain_core.messages import AIMessage, HumanMessage
            from langchain_core.messages import SystemMessage as LCSystemMessage
            
            # Convert browser-use messages to langchain format
            lc_messages = []
            for msg in messages:
                msg_type = type(msg).__name__
                if msg_type == 'SystemMessage':
                    lc_messages.append(LCSystemMessage(content=msg.content))
                elif msg_type == 'UserMessage':
                    # Handle content which can be string or list of content parts
                    if isinstance(msg.content, str):
                        lc_messages.append(HumanMessage(content=msg.content))
                    else:
                        # Complex content with images etc - convert to text for now
                        text_parts = []
                        for part in msg.content:
                            if hasattr(part, 'text'):
                                text_parts.append(part.text)
                            elif hasattr(part, 'source'):
                                text_parts.append("[Image]")
                        lc_messages.append(HumanMessage(content=' '.join(text_parts) if text_parts else str(msg.content)))
                elif msg_type == 'AssistantMessage':
                    lc_messages.append(AIMessage(content=msg.content if isinstance(msg.content, str) else str(msg.content)))
                else:
                    # Fallback
                    lc_messages.append(HumanMessage(content=str(getattr(msg, 'content', str(msg)))))

                # NOTE: "Analyzing page..." TTS feedback removed as per user request.
                # Only final action descriptions should be spoken, not intermediate status.

            # Filter out kwargs that ChatGoogleGenerativeAI doesn't support
            unsupported_kwargs = {'session_id', 'run_id', 'run_manager', 'metadata', 'tags'}
            filtered_kwargs = {k: v for k, v in kwargs.items() if k not in unsupported_kwargs}
            
            completion = None
            usage = None
            
            # Use structured output if format is provided (this is the key fix!)
            if output_format is not None:
                try:
                    structured_llm = self._llm.with_structured_output(output_format)          
                    completion = await structured_llm.ainvoke(lc_messages, **filtered_kwargs)
                    logger.debug(f"[{FEATURE_ID}] Structured output parsed successfully: {type(completion).__name__} -> {completion}")
                except Exception as struct_err:
                    logger.warning(f"[{FEATURE_ID}] Structured output failed: {struct_err}, falling back to JSON parsing")
                    # Fallback: manual JSON parsing
                    response = await self._llm.ainvoke(lc_messages, **filtered_kwargs)
                    content = response.content if hasattr(response, 'content') else str(response)
                    
                    # Ensure content is string for JSON finding
                    if not isinstance(content, str):
                        content = str(content)
                    
                    import json
                    try:
                        # Try to extract JSON from the response
                        json_start = content.find('{')
                        json_end = content.rfind('}') + 1
                        if json_start != -1 and json_end > json_start:
                            json_str = content[json_start:json_end]
                            parsed = json.loads(json_str)
                            # Cast to Any to satisfy type checker
                            completion = output_format(**parsed) if isinstance(parsed, dict) else parsed  # type: ignore[reportArgumentType]
                        else:
                            logger.error(f"[{FEATURE_ID}] No JSON found in response: {content[:200]}...")
                            completion = content
                    except (json.JSONDecodeError, TypeError, ValueError) as e:
                        logger.error(f"[{FEATURE_ID}] JSON parsing failed: {e}")
                        completion = content
                    
                    # Get usage from fallback response
                    if hasattr(response, 'usage_metadata') and response.usage_metadata:
                        input_tokens = response.usage_metadata.get('input_tokens', 0)
                        output_tokens = response.usage_metadata.get('output_tokens', 0)
                        
                        if self.usage_callback:
                            self.usage_callback(input_tokens, output_tokens, self._model)

                        usage = ChatInvokeUsage(
                            prompt_tokens=input_tokens,
                            prompt_cached_tokens=None,
                            prompt_cache_creation_tokens=None,
                            prompt_image_tokens=None,
                            completion_tokens=output_tokens,
                            total_tokens=input_tokens + output_tokens
                        )
            else:
                response = await self._llm.ainvoke(lc_messages, **filtered_kwargs)
                completion = response.content if hasattr(response, 'content') else str(response)
                
                # Build usage info from response
                if hasattr(response, 'usage_metadata') and response.usage_metadata:
                    input_tokens = response.usage_metadata.get('input_tokens', 0)
                    output_tokens = response.usage_metadata.get('output_tokens', 0)
                    
                    if self.usage_callback:
                        self.usage_callback(input_tokens, output_tokens, self._model)

                    usage = ChatInvokeUsage(
                        prompt_tokens=input_tokens,
                        prompt_cached_tokens=None,
                        prompt_cache_creation_tokens=None,
                        prompt_image_tokens=None,
                        completion_tokens=output_tokens,
                        total_tokens=input_tokens + output_tokens
                    )
            
            return ChatInvokeCompletion(
                completion=completion,  # type: ignore[reportArgumentType]
                usage=usage,
                stop_reason='end_turn'
            )
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] LLM invocation error: {e}")
            raise


class BrowserUseModule:
    """
    Client-side module for executing browser-use tasks.
    Manages local Chromium installation and execution.
    """
    
    _install_lock = asyncio.Lock()
    _browser_installed = False

    def __init__(self):
        """Initialize the module."""
        self._config: dict[str, Any] = {}
        self._active_tasks: dict[str, Any] = {}  # task_id -> agent
        self._initialized = False
        
        # Persistent browser session support
        self._persistent_session = None
        self._keep_browser_open = False

    async def initialize(self, config: dict[str, Any] | None = None, notification_callback: Any | None = None, tts_callback: Any | None = None, usage_callback: Any | None = None) -> None:
        """
        Initialize the module.
        
        Args:
            config: Module configuration (optional)
            notification_callback: Async callback(message: str) for user notifications
            tts_callback: Async callback(text: str, session_id: str) for immediate audio feedback
            usage_callback: Callback(input_tokens: int, output_tokens: int) for token usage tracking
        """
        try:
            self.notification_callback = notification_callback
            self.tts_callback = tts_callback
            self.usage_callback = usage_callback
            
            # Load config from unified_config just in case
            if config is None:
                # Assuming config is passed or we load it from global
                # In client architecture, usually integration passes config.
                pass
            
            self._config = config or {}
            
            # Read keep_browser_open config
            # FIX: Load from root config section 'browser_use' which contains the actual settings
            # get_feature_config only returns what's under 'features' (usually just enabled/disabled)
            root_config = global_config._load_config() if hasattr(global_config, '_load_config') else {}
            browser_use_root_config = root_config.get('browser_use', {})
            
            # Merge root config into self._config (root config takes precedence)
            if browser_use_root_config:
                logger.debug(f"[{FEATURE_ID}] Loading root config: {browser_use_root_config.keys()}")
                self._config.update(browser_use_root_config)

            self._keep_browser_open = self._config.get('keep_browser_open', False)
            logger.info(f"[{FEATURE_ID}] keep_browser_open={self._keep_browser_open}")
            self._apply_runtime_tuning()
            
            if not _check_browser_use_available():
                logger.warning(f"[{FEATURE_ID}] browser-use not available locally")
            else:
                # Ensure browser is installed eager
                self._install_task = asyncio.create_task(self._ensure_browser_installed())
            
            self._initialized = True
            logger.info(f"[{FEATURE_ID}] Client BrowserUseModule initialized")
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Initialization error: {e}")
            raise

    def _apply_runtime_tuning(self) -> None:
        """Apply runtime tuning for browser-use timeouts/logging."""
        # Increase browser-use event timeouts via env vars to avoid early timeouts.
        timeouts = self._config.get("event_timeouts", {}) if isinstance(self._config, dict) else {}
        overrides = {
            "BrowserStartEvent": int(timeouts.get("BrowserStartEvent", 60)),
            "BrowserLaunchEvent": int(timeouts.get("BrowserLaunchEvent", 60)),
        }
        for name, value in overrides.items():
            env_key = f"TIMEOUT_{name}"
            os.environ.setdefault(env_key, str(value))
            logger.info(f"[{FEATURE_ID}] {env_key}={os.environ.get(env_key)}")

        # Suppress browser_use/bubus watchdog warnings if configured.
        if self._config.get("suppress_watchdog_warnings", False):
            logging.getLogger("bubus").setLevel(logging.ERROR)

    async def _ensure_browser_installed(self):
        """Check and install Chromium if necessary (single-flight)."""
        if not _check_browser_use_available():
            return

        if BrowserUseModule._browser_installed:
            return

        logger.debug(f"[{FEATURE_ID}] Waiting for install lock...")
        async with BrowserUseModule._install_lock:
            logger.debug(f"[{FEATURE_ID}] Acquired install lock")
            # Double-check
            if BrowserUseModule._browser_installed:
                return

            logger.info(f"[{FEATURE_ID}] Checking browser installation (Chromium)...")

            # Ensure Playwright browsers path is writable and deterministic in .app
            def _resolve_playwright_browsers_path() -> str:
                # Use centralized resource path resolution to match app's user data dir and handle sandbox
                app_support = get_user_data_dir()
                browsers_path = os.path.join(app_support, "ms-playwright")
                try:
                    os.makedirs(browsers_path, exist_ok=True)
                except Exception as e:
                    logger.warning(f"[{FEATURE_ID}] Failed to ensure browsers path: {browsers_path} err={e}")
                return browsers_path

            browsers_path = _resolve_playwright_browsers_path()
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = browsers_path
            logger.info(f"[{FEATURE_ID}] PLAYWRIGHT_BROWSERS_PATH={browsers_path}")

            # Optimization: Check if chromium is already installed to avoid redundant 'install' calls
            # Playwright creates folders like 'chromium-123456' inside browsers_path
            try:
                if os.path.exists(browsers_path):
                    installed_browsers = os.listdir(browsers_path)
                    has_chromium = any(name.startswith("chromium-") for name in installed_browsers)
                    if has_chromium:
                        logger.info(f"[{FEATURE_ID}] Chromium detected in {browsers_path}, skipping install check")
                        BrowserUseModule._browser_installed = True
                        return
            except Exception as e:
                logger.warning(f"[{FEATURE_ID}] Failed to check existing browsers: {e}")
            
            # Use playwright cli to install
            async def run_install():
                # Detect if frozen (PyInstaller)
                is_frozen = getattr(sys, 'frozen', False)
                env = os.environ.copy()
                
                # If frozen, we can't use "sys.executable -m playwright".
                # We need to find the bundled driver or fallback to internal API.
                # Standard approach: The 'playwright' module path contains the driver.
                
                cmd = [sys.executable, "-m", "playwright", "install", "chromium"]
                
                if is_frozen:
                    logger.info(f"[{FEATURE_ID}] Detected Frozen/PyInstaller environment.")
                    # Try to locate the driver executable provided by playwright package
                    # Usually in: playwright/driver/playwright.sh (or .cmd)
                    try:
                        import playwright
                        package_path = os.path.dirname(playwright.__file__)
                        driver_name = "playwright.cmd" if sys.platform == "win32" else "playwright.sh"
                        driver_path = os.path.join(package_path, "driver", driver_name)
                        
                        if os.path.exists(driver_path):
                            logger.info(f"[{FEATURE_ID}] Found playwright driver at: {driver_path}")
                            try:
                                os.chmod(driver_path, 0o755)
                            except Exception as e:
                                logger.warning(f"[{FEATURE_ID}] Failed to chmod driver: {driver_path} err={e}")
                            cmd = [driver_path, "install", "chromium"]
                        else:
                            # Fallback 1: sys._MEIPASS (onefile)
                            if hasattr(sys, "_MEIPASS"):
                                base_path = sys._MEIPASS  # type: ignore[reportAttributeAccessIssue]
                                driver_path = os.path.join(base_path, "playwright", "driver", driver_name)
                                if os.path.exists(driver_path):
                                    logger.info(f"[{FEATURE_ID}] Found bundled driver at (onefile): {driver_path}")
                                    try:
                                        os.chmod(driver_path, 0o755)
                                    except Exception as e:
                                        logger.warning(f"[{FEATURE_ID}] Failed to chmod bundled driver: {driver_path} err={e}")
                                    cmd = [driver_path, "install", "chromium"]
                                else:
                                    logger.warning(f"[{FEATURE_ID}] Driver NOT found at _MEIPASS path: {driver_path}")
                            
                            # Fallback 2: Relative to executable (onedir / .app)
                            # In .app, sys.executable is inside Contents/MacOS/
                            # Resources are usually nearby or in ../Resources
                            # Based on Nexy.spec, we collect 'playwright/driver' into 'playwright/driver' folder in the bundle root.
                            # In onedir, bundle root is os.path.dirname(sys.executable).
                            bundle_root = os.path.dirname(sys.executable)
                            onedir_driver_path = os.path.join(bundle_root, "playwright", "driver", driver_name)
                             
                            if os.path.exists(onedir_driver_path):
                                logger.info(f"[{FEATURE_ID}] Found bundled driver at (onedir): {onedir_driver_path}")
                                try:
                                    os.chmod(onedir_driver_path, 0o755)
                                except Exception as e:
                                    logger.warning(f"[{FEATURE_ID}] Failed to chmod onedir driver: {onedir_driver_path} err={e}")
                                cmd = [onedir_driver_path, "install", "chromium"]
                                # Fix: Ensure bundled 'node' and other binaries are executable
                                driver_dir = os.path.dirname(onedir_driver_path)
                                try:
                                    for root, dirs, files in os.walk(driver_dir):
                                        for fname in files:
                                            fpath = os.path.join(root, fname)
                                            try:
                                                os.chmod(fpath, 0o755)
                                            except Exception:
                                                pass
                                    logger.info(f"[{FEATURE_ID}] Recursively chmod+x applied to {driver_dir}")
                                except Exception as e:
                                    logger.warning(f"[{FEATURE_ID}] Failed to recursive chmod driver dir: {e}")
                            else:
                                logger.warning(f"[{FEATURE_ID}] Driver NOT found at onedir path: {onedir_driver_path}")

                    except Exception as e:
                        logger.warning(f"[{FEATURE_ID}] Failed to resolve driver path in frozen mode: {e}")
                        # Fallback to sys.executable as a hail mary, or maybe just proceed
                
                logger.info(f"[{FEATURE_ID}] Executing install command: {cmd}")
                
                process = await asyncio.create_subprocess_exec(
                    *cmd,
                    env=env,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                stdout_text = stdout.decode().strip()
                stderr_text = stderr.decode().strip()
                if stdout_text:
                    logger.info(f"[{FEATURE_ID}] Playwright install stdout: {stdout_text}")
                if stderr_text:
                    logger.warning(f"[{FEATURE_ID}] Playwright install stderr: {stderr_text}")
                return process.returncode, stderr_text

            try:
                # Start install task
                install_task = asyncio.create_task(run_install())
                
                # Check if it finishes quickly (already installed)
                try:
                    returncode, err_msg = await asyncio.wait_for(asyncio.shield(install_task), timeout=2.0)
                except asyncio.TimeoutError:
                    # Taking longer -> downloading
                    logger.info(f"[{FEATURE_ID}] Installing browser (downloading)...")
                    if hasattr(self, 'notification_callback') and self.notification_callback:
                        try:
                            await self.notification_callback("Setting up browser: Downloading Chromium...")
                        except Exception:
                            pass
                    
                    returncode, err_msg = await install_task

                if returncode != 0:
                    logger.error(f"[{FEATURE_ID}] Failed to install browser: {err_msg}")
                    raise Exception(f"Failed to install browser: {err_msg}")
                else:
                    logger.info(f"[{FEATURE_ID}] Browser installation check passed")
                    BrowserUseModule._browser_installed = True
                    if hasattr(self, 'notification_callback') and self.notification_callback:
                        try:
                            await self.notification_callback("Browser setup complete. Ready to use.")
                        except Exception:
                            pass
                    
            except Exception as e:
                logger.error(f"[{FEATURE_ID}] Error ensuring browser installation: {e}")
                raise

    def _format_action_description(self, agent_output, browser_state) -> str:
        """
        Formats a human-readable action description.
        Same logic as server implementation.
        """
        import re
        descriptions = []
        
        # Priority 1: Memory from LLM
        if agent_output and hasattr(agent_output, 'memory') and agent_output.memory:
            memory_text = agent_output.memory.strip()
            if memory_text:
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
                    first_sentence = memory_text.split('.')[0]
                    if first_sentence and len(first_sentence) > 10:
                        descriptions.append(first_sentence + '.')
        
        # Priority 2: Structured actions
        if not descriptions and agent_output and hasattr(agent_output, 'actions') and agent_output.actions:
            action = agent_output.actions[0]
            # Determine type
            action_type = None
            if hasattr(action, 'action_type'): action_type = str(action.action_type).lower()
            elif hasattr(action, 'type'): action_type = str(action.type).lower()
            elif hasattr(action, '__class__'): action_type = action.__class__.__name__.lower()
            
            if action_type:
                if 'navigate' in action_type:
                    url = getattr(action, 'url', getattr(action, 'target_url', None))
                    if url:
                        descriptions.append(f"Navigated to {url}")
                    else:
                        descriptions.append("Navigated to website")
                elif 'input' in action_type or 'type' in action_type:
                    text = getattr(action, 'text', getattr(action, 'input_text', None))
                    if text:
                        descriptions.append(f"Typed '{text[:47]}...'" if len(text) > 50 else f"Typed '{text}'")
                    else:
                        descriptions.append("Entered text")
                elif 'click' in action_type:
                    label = getattr(action, 'aria_label', getattr(action, 'label', getattr(action, 'text', None)))
                    if label:
                        descriptions.append(f"Clicked on {label[:27]}...'") if len(label) > 30 else descriptions.append(f"Clicked on {label}")
                    else:
                        descriptions.append("Clicked on element")
                elif 'done' in action_type:
                    text = getattr(action, 'text', getattr(action, 'result_text', None))
                    descriptions.append(text if text else "Task completed")
                elif 'scroll' in action_type:
                    descriptions.append("Scrolled page")
                elif 'wait' in action_type:
                    descriptions.append("Waiting for page load")
        
        # Priority 3: Browser state URL fallback
        if not descriptions and browser_state and hasattr(browser_state, 'url') and browser_state.url:
            if browser_state.url != 'about:blank':
                descriptions.append(f"Navigated to {browser_state.url}")
        
        if not descriptions:
            descriptions.append("Step completed")
            
        return ". ".join(descriptions)

    async def process(self, request: dict[str, Any]) -> AsyncIterator[dict[str, Any]]:
        """
        Execute a browser-use task.
        
        Args:
            request: Task request
                - args: {task: str, config_preset: str}
                - session_id: str
        
        Yields:
            Progress events
        """
        task_id = f"task_{uuid.uuid4().hex[:12]}"
        task = request.get('args', {}).get('task')
        if not task:
            # Fallback: maybe it's in the root
            task = request.get('task', 'Unknown task')
            
        session_id = request.get('session_id', 'unknown')
        config_preset = request.get('args', {}).get('config_preset', 'fast')
        
        logger.info(f"[{FEATURE_ID}] Process called: task={task[:50]}, session_id={session_id}")
        
        # Reset cache to force re-check (allows hot-detection after pip install)
        _reset_browser_use_cache()
        
        if not _check_browser_use_available():
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'session_id': session_id,
                'description': 'Browser-use not installed locally',
                'error': 'browser-use not installed',
                'timestamp': datetime.now().isoformat()
            }
            return

        try:
            # Install browser if needed
            try:
                await self._ensure_browser_installed()
            except Exception as e:
                yield {
                    'type': 'BROWSER_TASK_FAILED',
                    'task_id': task_id,
                    'session_id': session_id,
                    'description': f'Failed to install browser: {e}',
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                }
                return

            yield {
                'type': 'BROWSER_TASK_STARTED',
                'task_id': task_id,
                'session_id': session_id,
                'description': f'Starting browser automation: {task}',
                'timestamp': datetime.now().isoformat()
            }
            
            # Run Agent
            async for progress in self._run_agent(task, task_id, session_id, config_preset):
                yield progress
                
        except asyncio.CancelledError:
            logger.info(f"[{FEATURE_ID}] Task cancelled: task_id={task_id}")
            yield {
                'type': 'BROWSER_TASK_CANCELLED',
                'task_id': task_id,
                'session_id': session_id,
                'description': 'Task cancelled by user',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Task failed: {e}")
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'session_id': session_id,
                'description': f'Task failed: {str(e)}',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
        finally:
            if task_id in self._active_tasks:
                del self._active_tasks[task_id]

    async def _run_agent(
        self,
        task: str,
        task_id: str,
        session_id: str,
        config_preset: str,
        *,
        retry_count: int = 0,
    ) -> AsyncIterator[dict[str, Any]]:
        # Get/Create LLM
        try:
            # Create session-aware usage callback
            usage_cb = None
            actual_model = None
            if self.usage_callback:
                def _cb(input_tokens, output_tokens, model_name=None):
                    self.usage_callback(input_tokens, output_tokens, session_id, model_name or "unknown")
                usage_cb = _cb
                
            llm = self._create_llm(self.tts_callback, usage_callback=usage_cb)
        except Exception as e:
            yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'session_id': session_id,
                'description': f'Failed to configure AI model: {e}',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
            return

        agent_config = self._get_agent_config(config_preset)
        
        try:
            # Persistent session handling
            Agent, ChatGoogle, BrowserProfile = _get_browser_use_classes()
            
            if not Agent or not BrowserProfile:
                raise ImportError("browser-use classes not loaded")

            browser_session = None
            if self._keep_browser_open and self._persistent_session:
                browser_session = self._persistent_session
                logger.info(f"[{FEATURE_ID}] Reusing persistent browser session")
            
            browser_profile = None
            if not browser_session and self._keep_browser_open:
                try:
                    browser_profile = BrowserProfile(keep_alive=True)
                except Exception as e:
                    logger.warning(f"[{FEATURE_ID}] Failed to create BrowserProfile: {e}")

            # Event processing
            event_queue = asyncio.Queue()
            
            async def step_callback(browser_state, agent_output, step_num):
                desc = self._format_action_description(agent_output, browser_state)
                event = {
                    'type': 'BROWSER_STEP_COMPLETED',
                    'task_id': task_id,
                    'session_id': session_id,
                    'step_number': step_num,
                    'description': desc,
                    'timestamp': datetime.now().isoformat()
                }
                if hasattr(browser_state, 'url') and browser_state.url:
                    event['url'] = browser_state.url
                await event_queue.put(event)

            async def done_callback(history):
                await event_queue.put({
                    'type': 'BROWSER_TASK_COMPLETED',
                    'task_id': task_id,
                    'session_id': session_id,
                    'description': 'Task completed',
                    'timestamp': datetime.now().isoformat()
                })

            agent = Agent(
                task=task,
                llm=llm,
                browser_session=browser_session,
                browser_profile=browser_profile,
                register_new_step_callback=step_callback,
                register_done_callback=done_callback,
                **agent_config
            )
            
            if self._keep_browser_open and not self._persistent_session:
                if hasattr(agent, 'browser_session') and agent.browser_session:
                    self._persistent_session = agent.browser_session

            self._active_tasks[task_id] = agent
        except Exception as e:
             yield {
                'type': 'BROWSER_TASK_FAILED',
                'task_id': task_id,
                'session_id': session_id,
                'description': f'Failed to create Agent: {e}',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
             return

        agent_task = asyncio.create_task(agent.run(max_steps=self._config.get('max_steps', 20)))

        try:
            while True:
                if agent_task.done():
                    try:
                        await agent_task
                    except Exception as e:
                        if self._should_retry_browser_session(e, retry_count):
                            await self._cleanup_browser_context(agent, task_id, force=True)
                            yield {
                                'type': 'BROWSER_TASK_RETRY',
                                'task_id': task_id,
                                'session_id': session_id,
                                'description': 'Browser session lost, retrying task',
                                'timestamp': datetime.now().isoformat()
                            }
                            async for progress in self._run_agent(
                                task,
                                task_id,
                                session_id,
                                config_preset,
                                retry_count=retry_count + 1,
                            ):
                                yield progress
                            return
                        yield {
                            'type': 'BROWSER_TASK_FAILED',
                            'task_id': task_id,
                            'session_id': session_id,
                            'description': f'Agent execution error: {e}',
                            'error': str(e),
                            'timestamp': datetime.now().isoformat()
                        }
                    break

                try:
                    event = await asyncio.wait_for(event_queue.get(), timeout=0.1)
                    yield event
                except asyncio.TimeoutError:
                    continue

        except asyncio.CancelledError:
            agent_task.cancel()
            yield {
                'type': 'BROWSER_TASK_CANCELLED',
                'task_id': task_id,
                'session_id': session_id,
                'description': 'Cancelled',
                'timestamp': datetime.now().isoformat()
            }
        finally:
             await self._cleanup_browser_context(agent, task_id)

    def _should_retry_browser_session(self, exc: Exception, retry_count: int) -> bool:
        max_retries = int(self._config.get('recovery_retries', 1))
        if retry_count >= max_retries:
            return False
        message = str(exc).lower()
        retry_signals = [
            "browser not connected",
            "no browser is open",
            "failed to open new tab",
            "target closed",
        ]
        return any(signal in message for signal in retry_signals)

    def _create_llm(self, tts_callback=None, usage_callback=None):
        """Создание LLM для Agent, совместимого с browser-use Protocol"""
        import os
        from config.unified_config_loader import unified_config
        
        # Load config from centralized source
        browser_config = unified_config.get_browser_use_config()
        
        # Priority: Env Var > Config > Fallback
        api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or browser_config.get("gemini_api_key")
        model_name = os.environ.get("GEMINI_MODEL") or os.environ.get("BROWSER_USE_MODEL") or browser_config.get("gemini_model")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY not configured in environment variables or config")
            
        if not model_name:
            # Fallback should ideally never be reached if config is correct
            model_name = "gemini-3-flash-preview" 
        
        # Use adapter to make ChatGoogleGenerativeAI compatible with browser-use
        return GeminiLLMAdapter(api_key=api_key, model=model_name, tts_callback=tts_callback, usage_callback=usage_callback)


    def _get_agent_config(self, config_preset: str) -> dict[str, Any]:
        base_config = {
            'llm_timeout': 120,
            'step_timeout': 180,
            'max_actions_per_step': 5,
            'close_browser_on_done': not self._keep_browser_open
        }
        # Presets logic
        if config_preset == 'ultra_fast':
            base_config.update({'llm_timeout': 60, 'max_actions_per_step': 3})
        elif config_preset == 'standard':
            base_config.update({'llm_timeout': 180, 'max_actions_per_step': 10})
        
        return base_config

    async def _cleanup_browser_context(self, agent, task_id: str, force: bool = False):
        if self._keep_browser_open and not force:
            return
            
        try:
            if self._persistent_session:
                 if hasattr(self._persistent_session, 'close'):
                     await self._persistent_session.close()
                 self._persistent_session = None
            elif agent and hasattr(agent, 'browser_session') and agent.browser_session:
                 if hasattr(agent.browser_session, 'close'):
                     await agent.browser_session.close()
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Cleanup error: {e}") 
        finally:
            if force and self._persistent_session:
                 self._persistent_session = None

    async def close_browser(self):
        """Explicitly close persistent browser."""
        if self._persistent_session:
            try:
                if hasattr(self._persistent_session, 'close'):
                    await self._persistent_session.close()
            finally:
                self._persistent_session = None
