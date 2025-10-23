# -*- mode: python ; coding: utf-8 -*-

"""
PyInstaller spec file for macOS application "Nexy AI Assistant"
"""

import sys
from pathlib import Path

# File paths - Force absolute paths
current_dir = Path.cwd().resolve()  # This is /path/to/client (PyInstaller runs from client/)
client_dir = current_dir            # This is /path/to/client
icon_path = client_dir / "assets" / "icons" / "app_icon.icns"

print(f"Using absolute path: {client_dir}")

# Check icon existence
if not icon_path.exists():
    print(f"⚠️ Icon not found: {icon_path}")
    icon_path = None

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
        # Proto files for gRPC (if exists)
        *([(str(client_dir / "streaming.proto"), ".")] if (client_dir / "streaming.proto").exists() else []),
        # Utils (if exists)
        *([(str(client_dir / "utils"), "utils")] if (client_dir / "utils").exists() else []),
        # FLAC support files
        *([("/opt/homebrew/bin/flac", ".")] if Path("/opt/homebrew/bin/flac").exists() else []),
    ],
    hiddenimports=[
        # System monitoring (must be first)
        "psutil",
        
        # Core modules
        "asyncio",
        "logging",
        "time",
        "sys",
        "pathlib",
        
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
        
        # UI
        "rich.console",
        "rich.text",
        
        # Input
        "pynput",
        
        # Screen capture
        "mss",
        "PIL",
        "PIL.Image",
        "PIL.ImageDraw",
        
        # Tray helper на rumps
        "rumps",
        
        # gRPC
        "grpc",
        "grpc.aio",
        # Protobuf runtime used by generated stubs
        "google",
        "google.protobuf",
        "google.protobuf.timestamp_pb2",
        "google.protobuf.wrappers_pb2",
        
        # macOS specific
        "Quartz",
        "AppKit",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
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
        "jiter",

        # Networking/json stacks not used
        "aiohttp",
        "multidict",
        "yarl",
        "websockets",
        "orjson",

        # Packaging/runtime helpers not needed at runtime
        "setuptools",
        "pkg_resources",
        "grpc_tools",
        "Cython",
        "zstandard",
        "pydantic_core",
        
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
        "lxml",

               # Legacy problematic binary (Intel) - causes notarization issues
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
           target_arch="arm64",  # Только Apple Silicon для нотаризации
           codesign_identity="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)",
           entitlements_file="packaging/entitlements.plist",
           codesign_deep=True,  # Deep signing
           codesign_options="runtime",  # Enable hardened runtime
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
       app = BUNDLE(
           coll,
           name="Nexy.app",
           icon=icon_path,
           bundle_identifier="com.nexy.assistant",
           codesign_identity="Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)",
           entitlements_file="packaging/entitlements.plist",
           codesign_deep=True,  # Deep signing
           codesign_options="runtime",  # Enable hardened runtime
    info_plist={
        # Main information
        "CFBundleName": "Nexy",
        "CFBundleDisplayName": "Nexy",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
        "CFBundlePackageType": "APPL",
        "CFBundleSignature": "????",
        
        # macOS specific settings
        "LSMinimumSystemVersion": "12.0.0",  # macOS 12.0+ (Monterey) - M1+ support
        "NSHighResolutionCapable": True,
        
        # Background mode (show in Dock, but background app)
        "LSUIElement": False,  # Показать в Dock
        
        # Permissions
        "NSMicrophoneUsageDescription": "Nexy needs access to your microphone to hear your commands.",
        "NSScreenCaptureUsageDescription": "Nexy needs screen recording access to capture content or control the screen based on your commands.",
        "NSAppleEventsUsageDescription": "Nexy needs to control other apps to execute your commands.",
        "NSAccessibilityUsageDescription": "Nexy needs accessibility permissions to assist you with controlling your computer.",
        
        # Architecture - Apple Silicon ONLY (M1/M2)
        "LSArchitecturePriority": ["arm64"],  # ONLY M1/M2 support, NO Intel
        "LSMinimumSystemVersion": "12.0.0",  # macOS 12.0+ (Monterey) - M1+ only
        
        # Application category
        "LSApplicationCategoryType": "public.app-category.productivity",
        
        # Background mode
        "LSBackgroundOnly": False,  # Показать в Dock, но фоновое
        
        # Additional settings
        "NSRequiresAquaSystemAppearance": False,
        "NSAppTransportSecurity": {
            "NSAllowsArbitraryLoads": True,  # For gRPC connections
        },
        
        # Critical for notarization
        "NSPrincipalClass": "NSApplication",
        "CFBundleDocumentTypes": [],
        "CFBundleURLTypes": [],
        "LSApplicationCategoryType": "public.app-category.productivity",
        
        # Sandbox and security
        "NSSupportsAutomaticTermination": False,
        "NSSupportsSuddenTermination": False,
        
        # ARM64 ONLY restrictions
        "LSRequiresNativeExecution": True,  # Только нативная ARM64 архитектура
    },
)
