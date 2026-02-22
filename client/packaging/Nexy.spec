# -*- mode: python ; coding: utf-8 -*-

"""
PyInstaller spec file for macOS application "Nexy AI Assistant"
"""

import os
import sys
import yaml
from pathlib import Path
from PyInstaller.utils.hooks import copy_metadata

# File paths - Force absolute paths
current_dir = Path.cwd().resolve()  # This is /path/to/client (PyInstaller runs from client/)
client_dir = current_dir            # This is /path/to/client
icon_path = client_dir / "assets" / "icons" / "app_icon.icns"

# Read version from unified_config.yaml (single source of truth)
config_path = client_dir / "config" / "unified_config.yaml"
with open(config_path, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    APP_VERSION = config['app']['version']

print(f"Using absolute path: {client_dir}")
print(f"App version from config: {APP_VERSION}")

TARGET_ARCH = os.environ.get("PYI_TARGET_ARCH", "arm64")
print(f"Target architecture: {TARGET_ARCH}")

# КРИТИЧНО: Импортируем rumps ТОЛЬКО когда он нужен (для получения пути к пакету)
# Это предотвращает ранний импорт rumps до применения PyObjC-fix в runtime hook
# ВАЖНО: В .app bundle PyObjC-fix применяется в runtime_hook_pyobjc_fix.py ДО импорта rumps
def get_rumps_path():
    """Получает путь к rumps пакету, импортируя его только когда нужно."""
    try:
        import rumps
        return Path(rumps.__file__).resolve().parent
    except ImportError as e:
        print(f"❌ ERROR: rumps not found: {e}")
        print("   Please install rumps: pip install rumps")
        raise

rumps_path = get_rumps_path()

# Check icon existence
if not icon_path.exists():
    print(f"⚠️ Icon not found: {icon_path}")
    icon_path = None

# Playwright driver (optional, for browser_use in packaged app)
playwright_driver_path = None
try:
    import playwright
    playwright_driver_path = Path(playwright.__file__).resolve().parent / "driver"
except Exception as e:
    print(f"⚠️ Playwright not available in build env: {e}")

extra_datas = []
if playwright_driver_path and playwright_driver_path.exists():
    extra_datas.append((str(playwright_driver_path), "playwright/driver"))
    print(f"✅ Playwright driver bundled from: {playwright_driver_path}")
else:
    print("⚠️ Playwright driver not found; skipping bundle")

# Packaged Playwright browsers runtime (preferred deterministic path for packaged app)
playwright_browsers_bundle_path = os.environ.get("NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR", "").strip()
if playwright_browsers_bundle_path:
    p = Path(playwright_browsers_bundle_path).expanduser().resolve()
    if p.exists() and p.is_dir():
        extra_datas.append((str(p), "playwright-browsers"))
        print(f"✅ Playwright browsers bundled from: {p}")
    else:
        print(f"⚠️ NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR not found: {p} (skipping)")
else:
    print("⚠️ NEXY_PLAYWRIGHT_BROWSERS_BUNDLE_DIR is not set; packaged browser runtime may be missing")

# browser_use package with system prompt templates (.md files)
browser_use_path = None
try:
    import browser_use
    browser_use_path = Path(browser_use.__file__).resolve().parent
except Exception as e:
    print(f"⚠️ browser_use not available in build env: {e}")

if browser_use_path and browser_use_path.exists():
    extra_datas.append((str(browser_use_path), "browser_use"))
    print(f"✅ browser_use package bundled from: {browser_use_path}")
else:
    print("⚠️ browser_use package not found; skipping bundle")

# Main settings
a = Analysis(
    [str(client_dir / "main.py")],  # Main file
    pathex=[str(client_dir), str(client_dir.parent)],
    binaries=[],
    datas=[
        # Configuration files
        (str(client_dir / "config"), "config"),
        # Icons and resources
        (str(client_dir / "assets"), "assets"),
        # Resources (including FLAC binary)
        (str(client_dir / "resources"), "resources"),
        # MCP server scripts (open_app/close_app)
        (str(client_dir / "mcp_servers"), "mcp_servers"),
        # Proto files for gRPC (preserve directory structure)
        (str(client_dir / "modules" / "grpc_client" / "proto"), "modules/grpc_client/proto"),
        # =============================================================================
        # =============================================================================
        # INTEGRATION: Единственный источник истины
        # client/integration/ содержит реальные файлы (консолидировано).
        # =============================================================================
        (str(client_dir / "integration"), "integration"),
        # =============================================================================
        # КРИТИЧНО: rumps пакет (PyInstaller не подхватывает его автоматически)
        (str(rumps_path), "rumps"),
        # Messages модуль с Swift бинарниками для резолвинга контактов (F-2025-016)
        (str(client_dir / "modules" / "messages"), "modules/messages"),
        # Browser automation модуль (F-2025-015)
        (str(client_dir / "modules" / "browser_automation"), "modules/browser_automation"),
        # Metadata for browser_use and dependencies (fixes PackageNotFoundError)
        *copy_metadata("browser_use"),
        *copy_metadata("playwright"),
        *copy_metadata("langchain_core"),
        *copy_metadata("langchain_google_genai"),
    ] + extra_datas,
    hiddenimports=[
        # Playwright (F-2025-015)
        "playwright",
        "playwright._impl",
        "playwright._impl.main",
        "playwright.async_api",
        "playwright.sync_api",
        
        # System monitoring (must be first)
        "psutil",
        
        # Core modules
        "asyncio",
        "asyncio.events",
        "asyncio.futures",
        "asyncio.tasks",
        "logging",
        "time",
        "sys",
        "pathlib",
        "uuid",
        
        # Audio
        "sounddevice",
        "numpy",
        "scipy",
        "scipy.signal",
        "queue",
        "threading",
        "pydub",
        "pydub.audio_segment",
        "pydub.utils",
        
        # STT
        "speech_recognition",
        "speech_recognition.audio",
        "speech_recognition.exceptions",
        
        # UI
        "rich.console",
        "rich.text",
        
        # Input
        "pynput",
        "pynput.keyboard",
        "pynput.mouse",
        
        # Screen capture
        "PIL",
        "PIL.Image",
        "PIL.ImageDraw",
        
        # Tray helper на rumps
        "rumps",
        "rumps.rumps",
        "rumps.notifications",
        "rumps.text_field",
        "rumps.compat",

        # PyObjC базовые
        "AVFoundation",
        "objc",
        "Contacts",

        # AppKit подмодули (нужны для rumps)
        "AppKit",
        "AppKit.NSApplication",
        "AppKit.NSStatusBar",
        "AppKit.NSMenu",
        "AppKit.NSMenuItem",
        "AppKit.NSImage",
        "AppKit.NSAlert",
        "AppKit.NSTextField",
        "AppKit.NSSecureTextField",
        "AppKit.NSSlider",
        "AppKit.NSSize",
        "AppKit.NSWorkspace",
        "AppKit.NSWorkspaceWillSleepNotification",
        "AppKit.NSWorkspaceDidWakeNotification",
        "AppKit.NSKeyDown",
        "AppKit.NSCommandKeyMask",

        # Foundation подмодули (нужны для rumps)
        "Foundation",
        "Foundation.NSObject",
        "Foundation.NSRunLoop",
        "Foundation.NSTimer",
        "Foundation.NSDate",
        "Foundation.NSLog",
        "Foundation.NSDefaultRunLoopMode",
        "Foundation.NSUserDefaults",
        "Foundation.NSString",
        "Foundation.NSMutableDictionary",
        "Foundation.NSMakeRect",
        "Foundation.NSSearchPathForDirectoriesInDomains",
        "Foundation.NSUserNotification",
        "Foundation.NSUserNotificationCenter",
        
        # gRPC
        "grpc",
        "grpc.aio",
        "modules.grpc_client.proto.streaming_pb2",
        "modules.grpc_client.proto.streaming_pb2_grpc",
        # Protobuf runtime used by generated stubs
        "google",
        "google.protobuf",
        "google.protobuf.timestamp_pb2",
        "google.protobuf.wrappers_pb2",
        
        # macOS specific
        "Quartz",
        "AppKit",
        
        # Configuration
        "yaml",
        
        # MCP (Model Context Protocol) - для action_execution_integration
        "mcp",
        "mcp.client",
        "mcp.client.session",
        "mcp.client.stdio",
        "pydantic",
        "pydantic_core",
        "pydantic._migration",
        "pydantic.warnings",
        "pydantic.version",
        "jiter",  # Required by pydantic for JSON parsing (used by browser-use)

        # HTTP stack for browser-use / langchain (F-2025-015)
        "httpx",
        "httpx._config",
        "httpcore",
        "httpcore._async",
        "httpcore._sync", 
        "h11",
        "h11._connection",
        "certifi",
        "idna",
        "idna.codec",
        
        # Async I/O (required by httpx/browser-use)
        "anyio",
        "anyio._backends",
        "anyio._backends._asyncio",
        "sniffio",
        
        # Retry logic (required by langchain)
        "tenacity",
        
        # File type detection (required by langchain-google-genai)
        "filetype",
        
        # Optional: Fast JSON (C extension, speeds up pydantic)
        "orjson",

        # === INTEGRATION MODULES (dynamic imports from main.py) ===
        # integration.core
        "integration.core",
        "integration.core.base_integration",
        "integration.core.error_handler",
        "integration.core.event_bus",
        "integration.core.event_utils",
        "integration.core.integration_factory",
        "integration.core.selectors",
        "integration.core.simple_module_coordinator",
        "integration.core.state_manager",
        
        # integration.integrations
        "integration.integrations",
        "integration.integrations.action_execution_integration",
        "integration.integrations.autostart_manager_integration",
        "integration.integrations.first_run_permissions_integration",
        "integration.integrations.grpc_client_integration",
        "integration.integrations.hardware_id_integration",
        "integration.integrations.input_processing_integration",
        "integration.integrations.instance_manager_integration",
        "integration.integrations.interrupt_management_integration",
        "integration.integrations.mode_management_integration",
        "integration.integrations.network_manager_integration",
        "integration.integrations.permission_restart_integration",
        "integration.integrations.screenshot_capture_integration",
        "integration.integrations.signal_integration",
        "integration.integrations.speech_playback_integration",
        "integration.integrations.tray_controller_integration",
        "integration.integrations.tts_integration",
        "integration.integrations.update_notification_integration",
        "integration.integrations.updater_integration",
        "integration.integrations.voice_recognition_integration",
        "integration.integrations.voiceover_ducking_integration",
        "integration.integrations.welcome_message_integration",
        # DISABLED: payment_integration - not packaged (see PACKAGING_FINAL_GUIDE.md)
        
        # modules.permissions
        "modules.permissions",
        "modules.permission_restart",

        # === PERMISSION SYSTEM V2 (F-2025-018) ===
        "modules.permissions.v2",
        "modules.permissions.v2.types",
        "modules.permissions.v2.error_matrix",
        "modules.permissions.v2.classifiers",
        "modules.permissions.v2.probers",
        "modules.permissions.v2.probers.base",
        "modules.permissions.v2.probers.microphone",
        "modules.permissions.v2.probers.screen_capture",
        "modules.permissions.v2.probers.accessibility",
        "modules.permissions.v2.probers.input_monitoring",
        "modules.permissions.v2.probers.full_disk_access",
        "modules.permissions.v2.probers.contacts",
        "modules.permissions.v2.probers.messages",
        "modules.permissions.v2.integration",
        "modules.permissions.v2.orchestrator",
        "modules.permissions.v2.ledger",
        "modules.permissions.v2.settings_nav",
        "modules.permissions.v2.config_loader",

        # === BROWSER PROGRESS TYPES (F-2025-015) ===
        "modules.browser_progress",
        "modules.browser_progress.core",
        "modules.browser_progress.core.types",

        # === MESSAGES MODULE (F-2025-016) ===
        "modules.messages",
        "modules.messages.contact_resolver",
        "modules.messages.messages_db",
        "modules.messages.send_message",

        # === BROWSER AUTOMATION MODULE (F-2025-015) ===
        "modules.browser_automation",
        "modules.browser_automation.module",
        "modules.browser_automation.constants",
        
        # Browser integrations
        "integration.integrations.browser_use_integration",
        "integration.integrations.browser_progress_integration",

        # Browser Use & LangChain Dependencies (F-2025-015)
        "browser_use",
        "browser_use.browser", 
        "browser_use.browser.profile",
        "browser_use.agent",
        "browser_use.agent.service",
        "browser_use.agent.system_prompts",
        "browser_use.llm.views",
        "langchain_google_genai",
        "langchain_core",
        "langchain_core.messages",
        "langchain_core.language_models",
        "langchain_core.outputs",
    ],
           hookspath=[],
           hooksconfig={},
           runtime_hooks=[
               str(client_dir / "packaging" / "runtime_hook_pyobjc_fix.py"),
           ],
    excludes=[
        # GUI and dev tooling
        "tkinter",
        "pytest",
        "IPython",
        "jupyter",
        "notebook",

        # Data/ML stacks not used
        "matplotlib",
        "pandas",
        "numba",
        "llvmlite",
        "tokenizers",
        "tiktoken",
        # "jiter",  # KEPT: Required by pydantic for browser-use

        # Networking/json stacks not used
        # "aiohttp", # REQUIRED for PaymentIntegration
        # "multidict", # REQUIRED for aiohttp
        # "yarl", # REQUIRED for aiohttp
        # "orjson",

        # Packaging/runtime helpers not needed at runtime
        "setuptools",
        "pkg_resources",
        "grpc_tools",
        "Cython",
        # НЕ исключаем pydantic_core - нужен для mcp модуля
        
        # Optional Pillow plugins (keep core PIL only)
        "PIL.ImageTk",
        "PIL.SpiderImagePlugin",
        "PIL.PsdImagePlugin",
        "PIL.PdfImagePlugin",
        "PIL.EpsImagePlugin",
        "PIL.DdsImagePlugin",
        "PIL.FtexImagePlugin",
        "PIL.FitsImagePlugin",
        "PIL.IcnsImagePlugin",
        "PIL.XbmImagePlugin",
        "PIL.XpmImagePlugin",

        # XML stack not used
        # "lxml",

               # Legacy problematic binary (Intel) - causes notarization issues
               # Используем Universal 2 FLAC из resources/audio/flac (создаётся через stage_universal_binaries.py)
               "speech_recognition.flac-mac",  # Intel x86_64 binary - not compatible with ARM64, uses old SDK
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Remove duplicate files
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Create executable file
# ВАЖНО: Отключаем подпись в PyInstaller - подпись выполняется позже в build_final.sh
# Это предотвращает ошибки с кэшем PyInstaller при подписи файлов после strip
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Nexy",
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,
    console=False,  # Hide console for macOS application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=TARGET_ARCH,
    # Отключаем подпись в PyInstaller - подпись выполняется позже в build_final.sh
    # codesign_identity="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)",
    # entitlements_file="packaging/entitlements.plist",
    # codesign_deep=True,  # Deep signing
    # codesign_options="runtime",  # Enable hardened runtime
)

# Create .app bundle
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=False,
    upx_exclude=[],
    name="Nexy",
)

# Create .app file
# ВАЖНО: Отключаем подпись в PyInstaller - подпись выполняется позже в build_final.sh
app = BUNDLE(
    coll,
    name="Nexy.app",
    icon=icon_path,
    bundle_identifier="com.nexy.assistant",
    # Отключаем подпись в PyInstaller - подпись выполняется позже в build_final.sh
    # codesign_identity="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)",
    # entitlements_file="packaging/entitlements.plist",
    # codesign_deep=True,  # Deep signing
    # codesign_options="runtime",  # Enable hardened runtime
    info_plist={
        # Main information
        "CFBundleName": "Nexy",
        "CFBundleDisplayName": "Nexy",
        "CFBundleVersion": APP_VERSION,
        "CFBundleShortVersionString": APP_VERSION,
        "CFBundlePackageType": "APPL",
        "CFBundleExecutable": "Nexy",  # Explicit executable name
        
        # macOS specific settings
        "LSMinimumSystemVersion": "12.0.0",  # macOS 12.0+ (Monterey) - M1+ support
        "NSHighResolutionCapable": True,

        # Background mode - Menu Bar App (не показывать в Dock)
        "LSUIElement": True,  # Скрыть из Dock, показать только в Menu Bar
        # ВАЖНО: При LSUIElement=True нужно активировать NSApplication.sharedApplication()
        # в коде ДО создания menu bar иконки (см. main.py)

        # Permissions
        "NSMicrophoneUsageDescription": "Nexy needs access to your microphone to hear your commands.",
        "NSScreenCaptureUsageDescription": "Nexy needs screen recording access to capture content or control the screen based on your commands.",
        "NSAppleEventsUsageDescription": "Nexy needs to control other apps to execute your commands.",
        "NSAccessibilityUsageDescription": "Nexy needs accessibility permissions to assist you with controlling your computer.",
        # Contacts для резолвинга имён контактов (F-2025-016)
        "NSContactsUsageDescription": "Nexy needs access to your contacts to identify message senders and recipients.",
        "NSInputMonitoringUsageDescription": "Nexy needs input monitoring to detect keyboard and mouse events for hotkeys and automation.",
        "NSLocalNetworkUsageDescription": "Nexy needs access to your local network to discover and communicate with nearby devices.",
        "NSFullDiskAccessUsageDescription": "Nexy needs full disk access to read user data required for message and file processing.",

        # Architecture - Apple Silicon ONLY (M1/M2)
        "LSArchitecturePriority": ["arm64", "x86_64"],
        
        # Application category
        "LSApplicationCategoryType": "public.app-category.productivity",

        # Additional settings
        "NSRequiresAquaSystemAppearance": False,
        "NSAppTransportSecurity": {
            "NSAllowsArbitraryLoads": True,  # For gRPC connections
        },
        
        # Critical for notarization
        "NSPrincipalClass": "NSApplication",
        "CFBundleDocumentTypes": [],
        "CFBundleURLTypes": [],
        
        # Background execution and stability
        "NSSupportsAutomaticTermination": False,  # Не завершать автоматически
        "NSSupportsSuddenTermination": False,     # Не завершать внезапно
        "LSMultipleInstancesProhibited": True,    # Только одна копия приложения

        # ARM64 ONLY restrictions
        "LSRequiresNativeExecution": False,
    },
)
