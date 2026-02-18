"""
Browser Use Module - Client Side Implementation

Feature ID: F-2025-015-browser-use
"""

import asyncio
from datetime import datetime
import logging
import os
import shutil
import sys
import time
from typing import Any, AsyncIterator
import uuid

from config.unified_config_loader import unified_config as global_config
from integration.utils.resource_path import get_user_data_dir
from modules.browser_automation.constants import FEATURE_ID

logger = logging.getLogger(__name__)
RUNTIME_BROWSER_NAME = "Chrome Nexy"

# Lazy import for browser-use (allows hot-detection without restart)
_browser_use_module_cache = {}


def _check_browser_use_available():
    """
    Dynamically check if browser-use is available.
    This allows detecting newly installed packages without app restart.
    """
    if "available" in _browser_use_module_cache:
        return _browser_use_module_cache["available"]

    try:
        # Direct import - no shadowing issue since we renamed local module to browser_automation
        from browser_use import Agent
        from browser_use.browser.profile import BrowserProfile
        from langchain_google_genai import ChatGoogleGenerativeAI as ChatGoogle

        _browser_use_module_cache["Agent"] = Agent
        _browser_use_module_cache["ChatGoogle"] = ChatGoogle
        _browser_use_module_cache["BrowserProfile"] = BrowserProfile
        _browser_use_module_cache["available"] = True
        logger.info(f"[{FEATURE_ID}] browser-use detected and loaded successfully")
        return True

    except ImportError as e:
        logger.warning(f"[{FEATURE_ID}] browser-use not installed: {e}")
        _browser_use_module_cache["available"] = False
        return False


def _get_browser_use_classes():
    """Get cached browser-use classes after availability check."""
    return (
        _browser_use_module_cache.get("Agent"),
        _browser_use_module_cache.get("ChatGoogle"),
        _browser_use_module_cache.get("BrowserProfile"),
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

    def __init__(
        self,
        api_key: str,
        fallback_api_key: str | None,
        model: str,
        tts_callback: Any | None = None,
        usage_callback: Any | None = None,
        llm_error_callback: Any | None = None,
    ):
        from langchain_google_genai import ChatGoogleGenerativeAI

        self._primary_llm = ChatGoogleGenerativeAI(model=model, api_key=api_key)
        self._fallback_llm = None
        fallback_key = (fallback_api_key or "").strip()
        if fallback_key and fallback_key != api_key:
            self._fallback_llm = ChatGoogleGenerativeAI(model=model, api_key=fallback_key)
        # Backward-compat alias for tests/diagnostics.
        self._llm = self._primary_llm
        self._model = model
        self._api_key = api_key
        self._fallback_api_key = fallback_key
        self._fallback_active = False
        self.tts_callback = tts_callback
        self.usage_callback = usage_callback
        self.llm_error_callback = llm_error_callback
        self._service_unavailable_notified = False
        self._rate_limited_notified = False

    @staticmethod
    def _is_service_unavailable_error(error_text: str) -> bool:
        text = (error_text or "").lower()
        return (
            "503" in text
            or "unavailable" in text
            or "high demand" in text
            or "try again later" in text
            or "servererror" in text
        )

    @staticmethod
    def _is_rate_limited_error(error_text: str) -> bool:
        text = (error_text or "").lower()
        return (
            "429" in text
            or "resource_exhausted" in text
            or "quota exceeded" in text
            or "rate limit" in text
            or "too many requests" in text
        )

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
                if msg_type == "SystemMessage":
                    lc_messages.append(LCSystemMessage(content=msg.content))
                elif msg_type == "UserMessage":
                    # Handle content which can be string or list of content parts
                    if isinstance(msg.content, str):
                        lc_messages.append(HumanMessage(content=msg.content))
                    else:
                        # Complex content with images etc - convert to text for now
                        text_parts = []
                        for part in msg.content:
                            if hasattr(part, "text"):
                                text_parts.append(part.text)
                            elif hasattr(part, "source"):
                                text_parts.append("[Image]")
                        lc_messages.append(
                            HumanMessage(
                                content=" ".join(text_parts) if text_parts else str(msg.content)
                            )
                        )
                elif msg_type == "AssistantMessage":
                    lc_messages.append(
                        AIMessage(
                            content=msg.content
                            if isinstance(msg.content, str)
                            else str(msg.content)
                        )
                    )
                else:
                    # Fallback
                    lc_messages.append(HumanMessage(content=str(getattr(msg, "content", str(msg)))))

                # NOTE: "Analyzing page..." TTS feedback removed as per user request.
                # Only final action descriptions should be spoken, not intermediate status.

            # Filter out kwargs that ChatGoogleGenerativeAI doesn't support
            unsupported_kwargs = {"session_id", "run_id", "run_manager", "metadata", "tags"}
            filtered_kwargs = {k: v for k, v in kwargs.items() if k not in unsupported_kwargs}

            completion = None
            usage = None

            llm_client = self._fallback_llm if (self._fallback_active and self._fallback_llm) else self._primary_llm

            # Use structured output if format is provided (this is the key fix!)
            if output_format is not None:
                try:
                    structured_llm = llm_client.with_structured_output(output_format)
                    completion = await structured_llm.ainvoke(lc_messages, **filtered_kwargs)
                    logger.debug(
                        f"[{FEATURE_ID}] Structured output parsed successfully: {type(completion).__name__} -> {completion}"
                    )
                except Exception as struct_err:
                    logger.warning(
                        f"[{FEATURE_ID}] Structured output failed: {struct_err}, falling back to JSON parsing"
                    )
                    # Fallback: manual JSON parsing
                    response = await llm_client.ainvoke(lc_messages, **filtered_kwargs)
                    content = response.content if hasattr(response, "content") else str(response)

                    # Ensure content is string for JSON finding
                    if not isinstance(content, str):
                        content = str(content)

                    import json

                    try:
                        # Try to extract JSON from the response
                        json_start = content.find("{")
                        json_end = content.rfind("}") + 1
                        if json_start != -1 and json_end > json_start:
                            json_str = content[json_start:json_end]
                            parsed = json.loads(json_str)
                            # Cast to Any to satisfy type checker
                            completion = (
                                output_format(**parsed) if isinstance(parsed, dict) else parsed
                            )  # type: ignore[reportArgumentType]
                        else:
                            logger.error(
                                f"[{FEATURE_ID}] No JSON found in response: {content[:200]}..."
                            )
                            completion = content
                    except (json.JSONDecodeError, TypeError, ValueError) as e:
                        logger.error(f"[{FEATURE_ID}] JSON parsing failed: {e}")
                        completion = content

                    # Get usage from fallback response
                    if hasattr(response, "usage_metadata") and response.usage_metadata:
                        input_tokens = response.usage_metadata.get("input_tokens", 0)
                        output_tokens = response.usage_metadata.get("output_tokens", 0)

                        if self.usage_callback:
                            self.usage_callback(input_tokens, output_tokens, self._model)

                        usage = ChatInvokeUsage(
                            prompt_tokens=input_tokens,
                            prompt_cached_tokens=None,
                            prompt_cache_creation_tokens=None,
                            prompt_image_tokens=None,
                            completion_tokens=output_tokens,
                            total_tokens=input_tokens + output_tokens,
                        )
            else:
                response = await llm_client.ainvoke(lc_messages, **filtered_kwargs)
                completion = response.content if hasattr(response, "content") else str(response)

                # Build usage info from response
                if hasattr(response, "usage_metadata") and response.usage_metadata:
                    input_tokens = response.usage_metadata.get("input_tokens", 0)
                    output_tokens = response.usage_metadata.get("output_tokens", 0)

                    if self.usage_callback:
                        self.usage_callback(input_tokens, output_tokens, self._model)

                    usage = ChatInvokeUsage(
                        prompt_tokens=input_tokens,
                        prompt_cached_tokens=None,
                        prompt_cache_creation_tokens=None,
                        prompt_image_tokens=None,
                        completion_tokens=output_tokens,
                        total_tokens=input_tokens + output_tokens,
                    )

            return ChatInvokeCompletion(
                completion=completion,  # type: ignore[reportArgumentType]
                usage=usage,
                stop_reason="end_turn",
            )
        except Exception as e:
            error_text = str(e)
            if (
                not self._fallback_active
                and self._fallback_llm is not None
                and self._is_rate_limited_error(error_text)
            ):
                self._fallback_active = True
                logger.warning(
                    f"[{FEATURE_ID}] Browser LLM rate-limited for model={self._model}; "
                    "switching to fallback API key"
                )
                return await self.ainvoke(messages, output_format=output_format, **kwargs)

            if (
                self.llm_error_callback
                and not self._rate_limited_notified
                and self._is_rate_limited_error(error_text)
            ):
                self._rate_limited_notified = True
                try:
                    payload = {
                        "reason": "llm_rate_limited",
                        "model": self._model,
                        "error": error_text,
                    }
                    maybe_result = self.llm_error_callback(payload)
                    if asyncio.iscoroutine(maybe_result):
                        await maybe_result
                except Exception as cb_error:
                    logger.debug(f"[{FEATURE_ID}] LLM error callback failed: {cb_error}")
            elif (
                self.llm_error_callback
                and not self._service_unavailable_notified
                and self._is_service_unavailable_error(error_text)
            ):
                self._service_unavailable_notified = True
                try:
                    payload = {
                        "reason": "llm_service_unavailable",
                        "model": self._model,
                        "error": error_text,
                    }
                    maybe_result = self.llm_error_callback(payload)
                    if asyncio.iscoroutine(maybe_result):
                        await maybe_result
                except Exception as cb_error:
                    logger.debug(f"[{FEATURE_ID}] LLM error callback failed: {cb_error}")
            logger.error(f"[{FEATURE_ID}] LLM invocation error: {e}")
            raise


class BrowserUseModule:
    """
    Client-side module for executing browser-use tasks.
    Manages local Chromium installation and execution.
    """

    _install_lock = asyncio.Lock()
    _browser_installed = False
    _install_task: asyncio.Task[Any] | None = None
    _install_task_guard = asyncio.Lock()

    def __init__(self):
        """Initialize the module."""
        self._config: dict[str, Any] = {}
        self._active_tasks: dict[str, Any] = {}  # task_id -> agent
        self._initialized = False

        # Persistent browser session support
        self._persistent_session = None
        self._keep_browser_open = False

    async def initialize(
        self,
        config: dict[str, Any] | None = None,
        notification_callback: Any | None = None,
        tts_callback: Any | None = None,
        install_status_callback: Any | None = None,
        usage_callback: Any | None = None,
        llm_error_callback: Any | None = None,
    ) -> None:
        """
        Initialize the module.

        Args:
            config: Module configuration (optional)
            notification_callback: Async callback(message: str) for user notifications
            tts_callback: Async callback(text: str, session_id: str) for immediate audio feedback
            install_status_callback: Async callback(event: dict[str, Any]) for install lifecycle events
            usage_callback: Callback(input_tokens: int, output_tokens: int) for token usage tracking
            llm_error_callback: Async callback(event: dict[str, Any]) for user-facing LLM errors
        """
        try:
            self.notification_callback = notification_callback
            self.tts_callback = tts_callback
            self.install_status_callback = install_status_callback
            self.usage_callback = usage_callback
            self.llm_error_callback = llm_error_callback

            # Load config from unified_config just in case
            if config is None:
                # Assuming config is passed or we load it from global
                # In client architecture, usually integration passes config.
                pass

            self._config = config or {}

            # Read keep_browser_open config
            # FIX: Load from root config section 'browser_use' which contains the actual settings
            # get_feature_config only returns what's under 'features' (usually just enabled/disabled)
            root_config = (
                global_config._load_config() if hasattr(global_config, "_load_config") else {}
            )
            browser_use_root_config = root_config.get("browser_use", {})

            # Merge root config into self._config (root config takes precedence)
            if browser_use_root_config:
                logger.debug(
                    f"[{FEATURE_ID}] Loading root config: {browser_use_root_config.keys()}"
                )
                self._config.update(browser_use_root_config)

            self._keep_browser_open = self._config.get("keep_browser_open", False)
            logger.info(f"[{FEATURE_ID}] keep_browser_open={self._keep_browser_open}")
            self._apply_runtime_tuning()

            if not _check_browser_use_available():
                logger.warning(f"[{FEATURE_ID}] browser-use not available locally")
            else:
                if self._is_local_chromium_ready():
                    BrowserUseModule._browser_installed = True
                    logger.info(f"[{FEATURE_ID}] Chromium already present locally, install task skipped")
                else:
                    if self._allow_runtime_install():
                        # Ensure browser is installed eager only when policy allows it.
                        await self._get_or_start_install_task(restart_if_failed=False)
                    else:
                        logger.info(
                            f"[{FEATURE_ID}] Runtime browser install disabled by policy; "
                            "expecting pre-bundled Chromium"
                        )

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

    def _is_frozen_runtime(self) -> bool:
        return bool(getattr(sys, "frozen", False))

    def _allow_runtime_install(self) -> bool:
        """Policy gate for runtime browser install."""
        cfg_value = self._config.get("allow_runtime_install")
        if isinstance(cfg_value, bool):
            return cfg_value
        # Default: in packaged app we avoid runtime installers; in dev keep enabled.
        return not self._is_frozen_runtime()

    def _is_command_available(self, cmd: str) -> bool:
        return bool(shutil.which(cmd))

    def _install_pending_flag_path(self) -> str:
        app_support = get_user_data_dir()
        return os.path.join(app_support, "browser_install_pending.flag")

    def _resolve_playwright_browsers_path(self) -> str:
        app_support = get_user_data_dir()
        return os.path.join(app_support, "chrome-nexy")

    def _legacy_playwright_browsers_path(self) -> str:
        app_support = get_user_data_dir()
        return os.path.join(app_support, "ms-playwright")

    def _ensure_runtime_browser_path(self) -> str:
        """Use a single runtime path and migrate legacy ms-playwright if present."""
        target_path = self._resolve_playwright_browsers_path()
        legacy_path = self._legacy_playwright_browsers_path()
        try:
            if os.path.isdir(legacy_path) and not os.path.exists(target_path):
                os.rename(legacy_path, target_path)
                logger.info(
                    f"[{FEATURE_ID}] Migrated legacy browser runtime path: {legacy_path} -> {target_path}"
                )
        except Exception as e:
            logger.warning(
                f"[{FEATURE_ID}] Failed to migrate browser runtime path to {RUNTIME_BROWSER_NAME}: {e}"
            )
        return target_path

    def _resolve_local_chromium_executable(self) -> str | None:
        """Resolve a valid local Chromium executable under PLAYWRIGHT_BROWSERS_PATH."""
        try:
            browsers_path = self._ensure_runtime_browser_path()
            if not os.path.isdir(browsers_path):
                return None

            for name in os.listdir(browsers_path):
                if not name.startswith("chromium-"):
                    continue

                base_dir = os.path.join(browsers_path, name)
                candidates = [
                    # macOS (Playwright Chromium bundle)
                    os.path.join(base_dir, "chrome-mac", "Chromium.app", "Contents", "MacOS", "Chromium"),
                    os.path.join(
                        base_dir,
                        "chrome-mac",
                        "Google Chrome for Testing.app",
                        "Contents",
                        "MacOS",
                        "Google Chrome for Testing",
                    ),
                    os.path.join(
                        base_dir,
                        "chrome-mac-arm64",
                        "Google Chrome for Testing.app",
                        "Contents",
                        "MacOS",
                        "Google Chrome for Testing",
                    ),
                    os.path.join(
                        base_dir,
                        "chrome-mac-arm64",
                        "Chromium.app",
                        "Contents",
                        "MacOS",
                        "Chromium",
                    ),
                    # Linux
                    os.path.join(base_dir, "chrome-linux", "chrome"),
                    os.path.join(base_dir, "chrome-linux64", "chrome"),
                    # Windows
                    os.path.join(base_dir, "chrome-win", "chrome.exe"),
                    os.path.join(base_dir, "chrome-win64", "chrome.exe"),
                ]
                for candidate in candidates:
                    if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                        return candidate
            return None
        except Exception as e:
            logger.debug(f"[{FEATURE_ID}] Chromium executable resolve failed: {e}")
            return None

    def _is_local_chromium_ready(self) -> bool:
        """Return True only when local Chromium has marker + executable."""
        try:
            browsers_path = self._ensure_runtime_browser_path()
            if not os.path.isdir(browsers_path):
                return False
            for name in os.listdir(browsers_path):
                if not name.startswith("chromium-"):
                    continue
                marker = os.path.join(browsers_path, name, "INSTALLATION_COMPLETE")
                if not os.path.isfile(marker):
                    continue
                executable = self._resolve_local_chromium_executable()
                if executable:
                    return True
                logger.warning(
                    f"[{FEATURE_ID}] Chromium marker exists but executable missing; reinstall required"
                )
            return False
        except Exception as e:
            logger.debug(f"[{FEATURE_ID}] Local chromium readiness check failed: {e}")
            return False

    def _resolve_frozen_playwright_install_cmd(self) -> list[str] | None:
        """
        Resolve Playwright install command in frozen (.app) mode.

        Supports both legacy wrapper-script layout (playwright.sh/cmd)
        and modern driver layout (node + package/cli.js).
        """
        driver_name = "playwright.cmd" if sys.platform == "win32" else "playwright.sh"
        candidate_driver_dirs: list[str] = []

        # 1) Inside installed playwright package
        try:
            import playwright

            pkg_driver_dir = os.path.join(os.path.dirname(playwright.__file__), "driver")
            candidate_driver_dirs.append(pkg_driver_dir)
        except Exception as e:
            logger.debug(f"[{FEATURE_ID}] playwright package path resolve skipped: {e}")

        # 2) PyInstaller onefile extraction dir
        if hasattr(sys, "_MEIPASS"):
            candidate_driver_dirs.append(
                os.path.join(getattr(sys, "_MEIPASS"), "playwright", "driver")
            )

        # 3) onedir next to executable (Contents/MacOS/playwright/driver)
        exe_dir = os.path.dirname(sys.executable)
        candidate_driver_dirs.append(os.path.join(exe_dir, "playwright", "driver"))

        # 4) macOS .app Resources (Contents/Resources/playwright/driver)
        # sys.executable -> .../Contents/MacOS/Nexy
        resources_dir = os.path.normpath(os.path.join(exe_dir, "..", "Resources"))
        candidate_driver_dirs.append(os.path.join(resources_dir, "playwright", "driver"))

        # De-duplicate while preserving order
        seen: set[str] = set()
        unique_driver_dirs: list[str] = []
        for d in candidate_driver_dirs:
            nd = os.path.normpath(d)
            if nd in seen:
                continue
            seen.add(nd)
            unique_driver_dirs.append(nd)

        for driver_dir in unique_driver_dirs:
            script_path = os.path.join(driver_dir, driver_name)
            if os.path.exists(script_path):
                logger.info(f"[{FEATURE_ID}] Found playwright wrapper at: {script_path}")
                try:
                    os.chmod(script_path, 0o755)
                except Exception as e:
                    logger.warning(
                        f"[{FEATURE_ID}] Failed to chmod wrapper: {script_path} err={e}"
                    )
                return [script_path, "install", "chromium"]

            # Newer Playwright layout in wheels/bundles
            node_path = os.path.join(driver_dir, "node")
            cli_js_path = os.path.join(driver_dir, "package", "cli.js")
            if os.path.exists(node_path) and os.path.exists(cli_js_path):
                logger.info(
                    f"[{FEATURE_ID}] Found playwright driver layout (node+cli) at: {driver_dir}"
                )
                try:
                    os.chmod(node_path, 0o755)
                except Exception as e:
                    logger.warning(
                        f"[{FEATURE_ID}] Failed to chmod driver node: {node_path} err={e}"
                    )
                return [node_path, cli_js_path, "install", "chromium"]

            logger.debug(f"[{FEATURE_ID}] Playwright driver not usable at: {driver_dir}")

        return None

    def _mark_install_pending(self) -> None:
        try:
            flag_path = self._install_pending_flag_path()
            with open(flag_path, "w", encoding="utf-8") as f:
                f.write(datetime.now().isoformat())
        except Exception as e:
            logger.debug(f"[{FEATURE_ID}] Failed to write install pending flag: {e}")

    def _clear_install_pending(self) -> None:
        try:
            flag_path = self._install_pending_flag_path()
            if os.path.exists(flag_path):
                os.remove(flag_path)
        except Exception as e:
            logger.debug(f"[{FEATURE_ID}] Failed to clear install pending flag: {e}")

    def _is_install_pending(self) -> bool:
        try:
            return os.path.exists(self._install_pending_flag_path())
        except Exception:
            return False

    async def _emit_install_status(self, status: str, **data: Any) -> None:
        cb = getattr(self, "install_status_callback", None)
        if not cb:
            return
        event = {"status": status, **data}
        try:
            await cb(event)
        except Exception as e:
            logger.debug(f"[{FEATURE_ID}] Failed to publish install status '{status}': {e}")

    async def _ensure_browser_installed(self):
        """Check and install Chromium if necessary (single-flight)."""
        if not _check_browser_use_available():
            return

        if BrowserUseModule._browser_installed:
            return

        install_lock_timeout_sec = float(self._config.get("install_lock_timeout_sec", 180.0))
        wait_heartbeat_sec = float(self._config.get("install_wait_heartbeat_sec", 10.0))
        wait_heartbeat_sec = max(1.0, wait_heartbeat_sec)

        logger.debug(f"[{FEATURE_ID}] Waiting for install lock...")
        lock_acquired = False
        wait_started = time.monotonic()
        try:
            while not lock_acquired:
                elapsed = time.monotonic() - wait_started
                remaining = install_lock_timeout_sec - elapsed
                if remaining <= 0:
                    raise TimeoutError(
                        f"Timed out waiting for browser install lock after {install_lock_timeout_sec:.0f}s"
                    )

                wait_slice = min(wait_heartbeat_sec, remaining)
                try:
                    await asyncio.wait_for(BrowserUseModule._install_lock.acquire(), wait_slice)
                    lock_acquired = True
                except asyncio.TimeoutError:
                    elapsed = time.monotonic() - wait_started
                    logger.info(
                        f"[{FEATURE_ID}] Still waiting for install lock ({elapsed:.1f}s elapsed)"
                    )
                    await self._emit_install_status(
                        "lock_wait",
                        elapsed_sec=round(elapsed, 1),
                    )

            logger.debug(f"[{FEATURE_ID}] Acquired install lock")
            # Double-check
            if BrowserUseModule._browser_installed:
                return

            logger.info(f"[{FEATURE_ID}] Checking browser installation ({RUNTIME_BROWSER_NAME})...")

            # Ensure Playwright browsers path is writable and deterministic in .app
            browsers_path = self._ensure_runtime_browser_path()
            try:
                os.makedirs(browsers_path, exist_ok=True)
            except Exception as e:
                logger.warning(
                    f"[{FEATURE_ID}] Failed to ensure browsers path: {browsers_path} err={e}"
                )
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = browsers_path
            logger.info(f"[{FEATURE_ID}] {RUNTIME_BROWSER_NAME} runtime path={browsers_path}")

            # Optimization: Check if chromium is already installed to avoid redundant 'install' calls
            if self._is_local_chromium_ready():
                logger.info(
                    f"[{FEATURE_ID}] Chromium detected in {browsers_path}, skipping install check"
                )
                BrowserUseModule._browser_installed = True
                if self._is_install_pending():
                    await self._emit_install_status("completed")
                    self._clear_install_pending()
                else:
                    await self._emit_install_status("already_installed")
                return

            # Use playwright cli to install
            install_start_announced = False
            async def run_install():
                # Detect if frozen (PyInstaller)
                is_frozen = getattr(sys, "frozen", False)
                env = os.environ.copy()

                # If frozen, we can't use "sys.executable -m playwright".
                # We need to find the bundled driver or fallback to internal API.
                # Standard approach: The 'playwright' module path contains the driver.

                cmd = None

                if is_frozen:
                    logger.info(f"[{FEATURE_ID}] Detected Frozen/PyInstaller environment.")
                    try:
                        cmd = self._resolve_frozen_playwright_install_cmd()
                    except Exception as e:
                        logger.warning(
                            f"[{FEATURE_ID}] Failed to resolve frozen playwright driver: {e}"
                        )
                        cmd = None
                    # Do not fallback to sys.executable in frozen mode.
                    # In .app builds sys.executable points to Nexy binary and would
                    # spawn a duplicate app process (restart/focus loop).
                else:
                    cmd = [sys.executable, "-m", "playwright", "install", "chromium"]

                if not cmd:
                    err = (
                        "Playwright driver not found in frozen bundle; "
                        "blocked fallback to Nexy executable to prevent duplicate-instance loop"
                    )
                    logger.error(f"[{FEATURE_ID}] {err}")
                    return 1, err

                # In hardened-runtime macOS app bundles, bundled Node can fail V8 CodeRange
                # allocation when JIT is enabled. For one-shot browser install, run jitless.
                if is_frozen and len(cmd) >= 3 and cmd[0].endswith("/playwright/driver/node"):
                    existing_opts = env.get("NODE_OPTIONS", "").strip()
                    if "--jitless" not in existing_opts:
                        env["NODE_OPTIONS"] = (
                            f"{existing_opts} --jitless".strip() if existing_opts else "--jitless"
                        )
                    logger.info(
                        f"[{FEATURE_ID}] Applying NODE_OPTIONS for frozen playwright install: {env['NODE_OPTIONS']}"
                    )

                logger.info(f"[{FEATURE_ID}] Executing install command: {cmd}")

                process = await asyncio.create_subprocess_exec(
                    *cmd, env=env, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
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
                # Announce install start immediately when install command is about to run.
                # This path is more reliable than waiting for the >2s timeout branch.
                await self._emit_install_status("started")
                install_start_announced = True
                self._mark_install_pending()

                # Start install task
                install_task = asyncio.create_task(run_install())

                # Check if it finishes quickly (already installed)
                try:
                    returncode, err_msg = await asyncio.wait_for(
                        asyncio.shield(install_task), timeout=2.0
                    )
                except asyncio.TimeoutError:
                    # Taking longer -> downloading
                    logger.info(f"[{FEATURE_ID}] Installing browser (downloading)...")
                    await self._emit_install_status("downloading")
                    if not install_start_announced:
                        await self._emit_install_status("started")

                    returncode, err_msg = await install_task

                if returncode != 0:
                    self._clear_install_pending()
                    await self._emit_install_status("failed", error=str(err_msg))
                    logger.error(f"[{FEATURE_ID}] Failed to install browser: {err_msg}")
                    raise Exception(f"Failed to install browser: {err_msg}")
                else:
                    if not self._is_local_chromium_ready():
                        self._clear_install_pending()
                        await self._emit_install_status(
                            "failed",
                            error="install_completed_but_chromium_not_ready",
                        )
                        logger.error(
                            f"[{FEATURE_ID}] Install command completed but Chromium executable is not ready"
                        )
                        raise Exception("install_completed_but_chromium_not_ready")

                    executable = self._resolve_local_chromium_executable()
                    logger.info(
                        f"[{FEATURE_ID}] Browser installation check passed (executable={executable})"
                    )
                    BrowserUseModule._browser_installed = True
                    await self._emit_install_status("completed")
                    self._clear_install_pending()

            except Exception as e:
                logger.error(f"[{FEATURE_ID}] Error ensuring browser installation: {e}")
                raise
        finally:
            if lock_acquired:
                BrowserUseModule._install_lock.release()

    async def _get_or_start_install_task(
        self, *, restart_if_failed: bool
    ) -> tuple[asyncio.Task[Any], bool]:
        """
        Return current install task or create one atomically.

        Returns:
            (task, started_new_task)
        """
        async with BrowserUseModule._install_task_guard:
            install_task = BrowserUseModule._install_task
            if install_task is None:
                install_task = asyncio.create_task(self._ensure_browser_installed())
                BrowserUseModule._install_task = install_task
                return install_task, True

            if install_task.done():
                install_error = None
                try:
                    install_error = install_task.exception()
                except asyncio.CancelledError:
                    install_error = RuntimeError("browser install task was cancelled")

                if restart_if_failed and (
                    install_error is not None or not BrowserUseModule._browser_installed
                ):
                    install_task = asyncio.create_task(self._ensure_browser_installed())
                    BrowserUseModule._install_task = install_task
                    return install_task, True

            return install_task, False

    def _format_action_description(self, agent_output, browser_state) -> str:
        """
        Formats a human-readable action description.
        Same logic as server implementation.
        """
        import re

        descriptions = []

        # Priority 1: Memory from LLM
        if agent_output and hasattr(agent_output, "memory") and agent_output.memory:
            memory_text = agent_output.memory.strip()
            if memory_text:
                match = re.search(
                    r"I have (?:successfully )?([^.]*(?:\.|$))(?:\s*(?:Now I need|I need to|Next I will|I will))?",
                    memory_text,
                    re.IGNORECASE,
                )
                if match:
                    completed_action = match.group(1).strip()
                    if completed_action:
                        descriptions.append(completed_action)
                else:
                    first_sentence = memory_text.split(".")[0]
                    if first_sentence and len(first_sentence) > 10:
                        descriptions.append(first_sentence + ".")

        # Priority 2: Structured actions
        if (
            not descriptions
            and agent_output
            and hasattr(agent_output, "actions")
            and agent_output.actions
        ):
            action = agent_output.actions[0]
            # Determine type
            action_type = None
            if hasattr(action, "action_type"):
                action_type = str(action.action_type).lower()
            elif hasattr(action, "type"):
                action_type = str(action.type).lower()
            elif hasattr(action, "__class__"):
                action_type = action.__class__.__name__.lower()

            if action_type:
                if "navigate" in action_type:
                    url = getattr(action, "url", getattr(action, "target_url", None))
                    if url:
                        descriptions.append(f"Navigated to {url}")
                    else:
                        descriptions.append("Navigated to website")
                elif "input" in action_type or "type" in action_type:
                    text = getattr(action, "text", getattr(action, "input_text", None))
                    if text:
                        descriptions.append(
                            f"Typed '{text[:47]}...'" if len(text) > 50 else f"Typed '{text}'"
                        )
                    else:
                        descriptions.append("Entered text")
                elif "click" in action_type:
                    label = getattr(
                        action,
                        "aria_label",
                        getattr(action, "label", getattr(action, "text", None)),
                    )
                    if label:
                        descriptions.append(f"Clicked on {label[:27]}...'") if len(
                            label
                        ) > 30 else descriptions.append(f"Clicked on {label}")
                    else:
                        descriptions.append("Clicked on element")
                elif "done" in action_type:
                    text = getattr(action, "text", getattr(action, "result_text", None))
                    descriptions.append(text if text else "Task completed")
                elif "scroll" in action_type:
                    descriptions.append("Scrolled page")
                elif "wait" in action_type:
                    descriptions.append("Waiting for page load")

        # Priority 3: Browser state URL fallback
        if (
            not descriptions
            and browser_state
            and hasattr(browser_state, "url")
            and browser_state.url
        ):
            if browser_state.url != "about:blank":
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
        task = self._resolve_request_task(request)
        session_id = request.get("session_id", "unknown")
        args = request.get("args", {}) if isinstance(request.get("args"), dict) else {}
        config_preset = args.get("config_preset", "fast")

        if not task:
            yield {
                "type": "BROWSER_TASK_FAILED",
                "task_id": task_id,
                "session_id": session_id,
                "description": "Task failed: missing browser task or url",
                "error": "missing_task_or_url",
                "timestamp": datetime.now().isoformat(),
            }
            return

        logger.info(f"[{FEATURE_ID}] Process called: task={task[:50]}, session_id={session_id}")

        # Reset cache to force re-check (allows hot-detection after pip install)
        _reset_browser_use_cache()

        if not _check_browser_use_available():
            yield {
                "type": "BROWSER_TASK_FAILED",
                "task_id": task_id,
                "session_id": session_id,
                "description": "Browser-use not installed locally",
                "error": "browser-use not installed",
                "timestamp": datetime.now().isoformat(),
            }
            return

        try:
            # Guard against stale "setup in progress" loops: local-ready browser wins.
            if BrowserUseModule._browser_installed and not self._is_local_chromium_ready():
                BrowserUseModule._browser_installed = False
                logger.warning(
                    f"[{FEATURE_ID}] Browser installed cache was stale; forcing reinstall path"
                )

            if not BrowserUseModule._browser_installed and self._is_local_chromium_ready():
                BrowserUseModule._browser_installed = True
                logger.info(f"[{FEATURE_ID}] Local chromium ready; bypassing setup wait path")
                async with BrowserUseModule._install_task_guard:
                    install_task = BrowserUseModule._install_task
                    if install_task and not install_task.done():
                        install_task.cancel()

            # Setup must complete before agent launch; otherwise browser_use may
            # fall back to its internal installer path (expects 'uvx' in PATH).
            if not BrowserUseModule._browser_installed:
                if self._allow_runtime_install():
                    install_task, _ = await self._get_or_start_install_task(restart_if_failed=True)
                    await install_task
                else:
                    yield {
                        "type": "BROWSER_TASK_FAILED",
                        "task_id": task_id,
                        "session_id": session_id,
                        "description": "Browser runtime is not preinstalled for app mode",
                        "error": "browser_runtime_missing_preinstalled_chromium_required",
                        "timestamp": datetime.now().isoformat(),
                    }
                    return

            chromium_executable = self._resolve_local_chromium_executable()
            if not chromium_executable:
                if not self._allow_runtime_install() and not self._is_command_available("uvx"):
                    raise RuntimeError(
                        "chromium_executable_not_found_and_uvx_unavailable_in_app_mode"
                    )
                raise RuntimeError("chromium_executable_not_found_after_setup")

            yield {
                "type": "BROWSER_TASK_STARTED",
                "task_id": task_id,
                "session_id": session_id,
                "description": f"Starting browser automation: {task}",
                "timestamp": datetime.now().isoformat(),
            }

            # Run Agent
            async for progress in self._run_agent(
                task,
                task_id,
                session_id,
                config_preset,
                chromium_executable=chromium_executable,
            ):
                yield progress

        except asyncio.CancelledError:
            logger.info(f"[{FEATURE_ID}] Task cancelled: task_id={task_id}")
            yield {
                "type": "BROWSER_TASK_CANCELLED",
                "task_id": task_id,
                "session_id": session_id,
                "description": "Task cancelled by user",
                "timestamp": datetime.now().isoformat(),
            }
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Task failed: {e}")
            yield {
                "type": "BROWSER_TASK_FAILED",
                "task_id": task_id,
                "session_id": session_id,
                "description": f"Task failed: {str(e)}",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            }
        finally:
            if task_id in self._active_tasks:
                del self._active_tasks[task_id]

    def _resolve_request_task(self, request: dict[str, Any]) -> str:
        args = request.get("args", {}) if isinstance(request.get("args"), dict) else {}
        raw_task = args.get("task")
        if not isinstance(raw_task, str) or not raw_task.strip():
            raw_task = request.get("task")
        task = raw_task.strip() if isinstance(raw_task, str) else ""
        if task:
            return task

        raw_url = args.get("url")
        if not isinstance(raw_url, str) or not raw_url.strip():
            raw_url = request.get("url")
        url = raw_url.strip() if isinstance(raw_url, str) else ""
        if not url:
            return ""
        return f"Open this page: {url}"

    async def _run_agent(
        self,
        task: str,
        task_id: str,
        session_id: str,
        config_preset: str,
        chromium_executable: str,
        *,
        retry_count: int = 0,
    ) -> AsyncIterator[dict[str, Any]]:
        # Get/Create LLM
        try:
            # Create session-aware usage callback
            usage_cb = None
            actual_model = None
            current_cb = self.usage_callback
            if current_cb:

                def _cb(input_tokens, output_tokens, model_name=None):
                    current_cb(
                        input_tokens, output_tokens, session_id, model_name or "unknown"
                    )

                usage_cb = _cb

            llm = self._create_llm(
                self.tts_callback,
                usage_callback=usage_cb,
                llm_error_callback=getattr(self, "llm_error_callback", None),
            )
        except Exception as e:
            yield {
                "type": "BROWSER_TASK_FAILED",
                "task_id": task_id,
                "session_id": session_id,
                "description": f"Failed to configure AI model: {e}",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
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
            if not browser_session:
                try:
                    browser_profile = BrowserProfile(
                        keep_alive=bool(self._keep_browser_open),
                        is_local=True,
                        executable_path=chromium_executable,
                    )
                except Exception as e:
                    # Fail-fast: do not let browser_use fallback to its own
                    # local browser installer path (can require uvx in dev setups).
                    raise RuntimeError(f"browser_profile_init_failed:{e}") from e

            # Event processing
            event_queue = asyncio.Queue()

            async def step_callback(browser_state, agent_output, step_num):
                desc = self._format_action_description(agent_output, browser_state)
                event = {
                    "type": "BROWSER_STEP_COMPLETED",
                    "task_id": task_id,
                    "session_id": session_id,
                    "step_number": step_num,
                    "description": desc,
                    "timestamp": datetime.now().isoformat(),
                }
                if hasattr(browser_state, "url") and browser_state.url:
                    event["url"] = browser_state.url
                await event_queue.put(event)

            async def done_callback(history):
                await event_queue.put(
                    {
                        "type": "BROWSER_TASK_COMPLETED",
                        "task_id": task_id,
                        "session_id": session_id,
                        "description": "Task completed",
                        "timestamp": datetime.now().isoformat(),
                    }
                )

            agent = Agent(
                task=task,
                llm=llm,
                browser_session=browser_session,
                browser_profile=browser_profile,
                register_new_step_callback=step_callback,
                register_done_callback=done_callback,
                **agent_config,
            )

            if self._keep_browser_open and not self._persistent_session:
                if hasattr(agent, "browser_session") and agent.browser_session:
                    self._persistent_session = agent.browser_session

            self._active_tasks[task_id] = agent
        except Exception as e:
            yield {
                "type": "BROWSER_TASK_FAILED",
                "task_id": task_id,
                "session_id": session_id,
                "description": f"Failed to create Agent: {e}",
                "error": str(e),
                "timestamp": datetime.now().isoformat(),
            }
            return

        agent_task = asyncio.create_task(agent.run(max_steps=self._config.get("max_steps", 20)))

        try:
            while True:
                if agent_task.done():
                    try:
                        await agent_task
                    except Exception as e:
                        if self._should_retry_browser_session(e, retry_count):
                            await self._cleanup_browser_context(agent, task_id, force=True)
                            yield {
                                "type": "BROWSER_TASK_RETRY",
                                "task_id": task_id,
                                "session_id": session_id,
                                "description": "Browser session lost, retrying task",
                                "timestamp": datetime.now().isoformat(),
                            }
                            async for progress in self._run_agent(
                                task,
                                task_id,
                                session_id,
                                config_preset,
                                chromium_executable=chromium_executable,
                                retry_count=retry_count + 1,
                            ):
                                yield progress
                            return
                        yield {
                            "type": "BROWSER_TASK_FAILED",
                            "task_id": task_id,
                            "session_id": session_id,
                            "description": f"Agent execution error: {e}",
                            "error": str(e),
                            "timestamp": datetime.now().isoformat(),
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
                "type": "BROWSER_TASK_CANCELLED",
                "task_id": task_id,
                "session_id": session_id,
                "description": "Cancelled",
                "timestamp": datetime.now().isoformat(),
            }
        finally:
            await self._cleanup_browser_context(agent, task_id)

    def _should_retry_browser_session(self, exc: Exception, retry_count: int) -> bool:
        max_retries = int(self._config.get("recovery_retries", 1))
        if retry_count >= max_retries:
            return False
        message = str(exc).lower()
        retry_signals = [
            "browser not connected",
            "no browser is open",
            "failed to open new tab",
            "target closed",
            "session with given id not found",
            "no valid agent focus available",
        ]
        return any(signal in message for signal in retry_signals)

    def _create_llm(self, tts_callback=None, usage_callback=None, llm_error_callback=None):
        """Создание LLM для Agent, совместимого с browser-use Protocol"""
        import os

        from config.unified_config_loader import unified_config

        # Load config from centralized source
        browser_config = unified_config.get_browser_use_config()

        # Use secure API key loader (priority: env var > secure credentials > config fallback)
        api_key = unified_config.get_api_key("gemini_api_key")
        fallback_api_key = unified_config.get_api_key("gemini_api_key_fallback")
        model_name = (
            os.environ.get("GEMINI_MODEL")
            or os.environ.get("BROWSER_USE_MODEL")
            or browser_config.get("gemini_model")
        )

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not configured in environment or ~/Library/Application Support/Nexy/credentials.yaml"
            )

        if not model_name:
            # Fallback should ideally never be reached if config is correct
            model_name = "gemini-3-flash-preview"

        # Use adapter to make ChatGoogleGenerativeAI compatible with browser-use
        return GeminiLLMAdapter(
            api_key=api_key,
            fallback_api_key=fallback_api_key,
            model=model_name,
            tts_callback=tts_callback,
            usage_callback=usage_callback,
            llm_error_callback=llm_error_callback,
        )

    def _get_agent_config(self, config_preset: str) -> dict[str, Any]:
        base_config = {
            "llm_timeout": 120,
            "step_timeout": 180,
            "max_actions_per_step": 5,
            "close_browser_on_done": not self._keep_browser_open,
        }
        # Presets logic
        if config_preset == "ultra_fast":
            base_config.update({"llm_timeout": 60, "max_actions_per_step": 3})
        elif config_preset == "standard":
            base_config.update({"llm_timeout": 180, "max_actions_per_step": 10})

        return base_config

    async def _cleanup_browser_context(self, agent, task_id: str, force: bool = False):
        if self._keep_browser_open and not force:
            return

        try:
            if self._persistent_session:
                if hasattr(self._persistent_session, "close"):
                    await self._persistent_session.close()
                self._persistent_session = None
            elif agent and hasattr(agent, "browser_session") and agent.browser_session:
                if hasattr(agent.browser_session, "close"):
                    await agent.browser_session.close()
        except Exception as e:
            logger.error(f"[{FEATURE_ID}] Cleanup error: {e}")
        finally:
            if force and self._persistent_session:
                self._persistent_session = None

    async def close_browser(self):
        """Explicitly close persistent browser and clear all active tasks."""
        # Очищаем активные задачи при принудительном закрытии браузера
        if self._active_tasks:
            logger.info(
                f"[{FEATURE_ID}] Clearing {len(self._active_tasks)} active tasks on browser close"
            )
            self._active_tasks.clear()

        if self._persistent_session:
            try:
                if hasattr(self._persistent_session, "close"):
                    await self._persistent_session.close()
            finally:
                self._persistent_session = None
