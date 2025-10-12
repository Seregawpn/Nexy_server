# Nexy v1.0.1 - Critical Fix Release

**Release Date:** October 11, 2025  
**Type:** Critical Bug Fix  
**Priority:** High

---

## 🐛 **Critical Bug Fixed**

### Issue
Permission dialogs did not appear on first application launch, causing the application to remain blocked indefinitely.

**Symptoms:**
- Microphone permission dialog never appeared
- Accessibility permission dialog never appeared  
- Input Monitoring permission dialog never appeared
- Application hung with message: "🔔 Старт последовательного запроса прав..."
- TCC database had no permission records
- Application remained unusable

**Affected Versions:** v1.0.0

### Root Cause
The permission request flow used `AppHelper.callAfter()` from PyObjC, which requires a running GUI event loop (`runloop`). However, Nexy is a **tray-only application** without a main window, and the GUI event loop was never started. This caused the permission request callback to never execute, resulting in an infinite hang.

**Technical Details:**
- File: `integration/integrations/permissions_integration.py`
- Method: `_request_permissions_sequential()`
- Line: 308 (v1.0.0)
- Issue: `AppHelper.callAfter(_mic_request)` → `await mic_future` (hangs forever)

### Solution
Removed dependency on PyObjC GUI event loop:
- Removed `AppHelper.callAfter()` call
- Direct invocation of `requestAccessForMediaType_completionHandler_`
- Thread-safe result passing using `loop.call_soon_threadsafe()`
- Added 30-second timeout protection
- Proper error handling for all permission types

---

## ✅ **What's Fixed**

### Permission Requests Now Work
- ✅ Microphone dialog appears within 1-2 seconds
- ✅ Accessibility dialog appears after microphone
- ✅ Input Monitoring dialog appears after accessibility
- ✅ Screen Capture dialog appears when needed (optional)

### Application Behavior
- ✅ No infinite hang on permission requests
- ✅ Application unblocks after permissions granted
- ✅ TCC database correctly registers permissions
- ✅ Proper timeout handling (30s per permission)
- ✅ Detailed error logging for debugging

### Code Changes
**File:** `integration/integrations/permissions_integration.py`  
**Lines:** 291-316

**Before (v1.0.0):**
```python
# ❌ Requires GUI runloop (broken for tray-only app)
AppHelper.callAfter(_mic_request)
mic_granted = await mic_future  # Hangs forever
```

**After (v1.0.1):**
```python
# ✅ Works without GUI runloop (tray-only compatible)
def mic_handler(granted):
    loop = asyncio.get_event_loop()
    loop.call_soon_threadsafe(
        lambda: mic_future.set_result(bool(granted))
    )

AVCaptureDevice.requestAccessForMediaType_completionHandler_(
    AVMediaTypeAudio, mic_handler
)
mic_granted = await asyncio.wait_for(mic_future, timeout=30.0)
```

---

## 🧪 **Testing**

### Test Environment
- macOS 14.0 Sonoma (arm64)
- macOS 13.0 Ventura (arm64)
- Fresh TCC database (all permissions reset)

### Test Results
| Test Case | Status | Notes |
|-----------|--------|-------|
| First launch permission dialogs | ✅ PASS | All 3 dialogs appear |
| Permission dialog response time | ✅ PASS | <2 seconds |
| TCC database registration | ✅ PASS | All permissions recorded |
| Application unblocking | ✅ PASS | Unblocks after permissions |
| Second launch (no dialogs) | ✅ PASS | No redundant prompts |
| Push-to-talk functionality | ✅ PASS | Spacebar works |
| Audio recording | ✅ PASS | Microphone captures audio |
| gRPC server communication | ✅ PASS | Data sent successfully |

---

## 📦 **Installation**

### New Installation

**Option 1: PKG Installer (Recommended)**
```bash
# Download Nexy-v1.0.1.pkg
sudo installer -pkg Nexy-v1.0.1.pkg -target /
```

**Option 2: DMG (Manual)**
1. Open `Nexy-v1.0.1.dmg`
2. Drag `Nexy.app` to `Applications` folder
3. Launch from Applications

### Upgrade from v1.0.0

1. **Uninstall old version** (recommended):
   ```bash
   sudo rm -rf /Applications/Nexy.app
   ```

2. **Install v1.0.1**:
   ```bash
   sudo installer -pkg Nexy-v1.0.1.pkg -target /
   ```

3. **Reset TCC permissions** (to see permission dialogs):
   ```bash
   sudo tccutil reset All com.nexy.assistant
   ```

4. **Launch application**:
   ```bash
   open /Applications/Nexy.app
   ```

5. **Grant permissions** when dialogs appear

---

## 🔄 **What to Expect**

### First Launch After Installation

1. **Application starts** - Tray icon may not appear yet
2. **Microphone dialog** - Click "OK" to grant
3. **Accessibility dialog** - Click "Open System Settings" → Enable Nexy
4. **Input Monitoring dialog** - Click "Open System Settings" → Enable Nexy
5. **Application unblocks** - Tray icon appears
6. **Ready to use** - Press spacebar to start recording

### Subsequent Launches
- No permission dialogs (already granted)
- Application starts immediately
- Tray icon appears within 1-2 seconds
- All functionality available

---

## 📊 **System Requirements**

- macOS 13.0 (Ventura) or later
- 200 MB free disk space
- Active internet connection
- Administrator rights (for installation only)

### Required Permissions
- 🎤 **Microphone** - For voice recording (critical)
- ♿ **Accessibility** - For keyboard monitoring (critical)
- ⌨️ **Input Monitoring** - For push-to-talk (critical)
- 📸 **Screen Recording** - For screenshots (optional)

---

## 🔐 **Security**

### Code Signing
- Signed with **Developer ID Application**
- Team ID: `5NKLL2CLB9`
- Bundle ID: `com.nexy.assistant`

### Notarization
- ✅ Notarized by Apple
- ✅ Stapled ticket included
- ✅ Passes Gatekeeper verification

### Verification Commands
```bash
# Verify PKG signature
pkgutil --check-signature Nexy-v1.0.1.pkg

# Verify notarization
xcrun stapler validate Nexy-v1.0.1.pkg

# Verify app signature
codesign --verify --deep --strict /Applications/Nexy.app
spctl --assess --verbose /Applications/Nexy.app
```

---

## 📝 **Changelog**

### [1.0.1] - 2025-10-11

#### Fixed
- **Critical:** Permission dialogs not appearing on first launch
- Application hanging indefinitely waiting for permissions
- TCC database not registering permission requests

#### Changed
- Removed `AppHelper.callAfter()` dependency for tray-only app compatibility
- Refactored `_request_permissions_sequential()` in `PermissionsIntegration`
- Added 30-second timeout protection for permission requests
- Improved thread-safety with `loop.call_soon_threadsafe()`
- Enhanced error handling and logging

#### Technical
- File: `integration/integrations/permissions_integration.py:291-316`
- Removed PyObjC GUI runloop dependency
- Direct invocation of macOS permission APIs
- Async/await with proper timeout handling

---

## 📚 **Documentation**

### For Users
- `QUICK_PERMISSIONS_CHECK.md` - How to check and fix permissions
- `README.md` - General usage guide

### For Developers
- `PERMISSION_DIALOG_FIX.md` - Technical details of the fix
- `FINAL_BUILD_INSTRUCTIONS.md` - How to build from source
- `REBUILD_GUIDE.md` - Complete rebuild process
- `SUPPORT_PLAYBOOK.md` - Troubleshooting guide

---

## 🆘 **Troubleshooting**

### Permission Dialogs Still Not Appearing?

1. **Check TCC is reset:**
   ```bash
   sqlite3 ~/Library/Application\ Support/com.apple.TCC/TCC.db \
     "SELECT * FROM access WHERE client='com.nexy.assistant';"
   ```
   Should return empty (no rows)

2. **Verify correct version:**
   ```bash
   defaults read /Applications/Nexy.app/Contents/Info.plist CFBundleVersion
   ```
   Should show: `1.0.1`

3. **Check bundle ID:**
   ```bash
   defaults read /Applications/Nexy.app/Contents/Info.plist CFBundleIdentifier
   ```
   Should show: `com.nexy.assistant`

4. **Launch from Terminal** (see debug output):
   ```bash
   /Applications/Nexy.app/Contents/MacOS/Nexy
   ```
   Look for: `"🔔 Старт последовательного запроса прав..."` followed by permission prompts

### Still Having Issues?

1. **Completely remove old installation:**
   ```bash
   sudo rm -rf /Applications/Nexy.app
   sudo rm -rf ~/Library/Application\ Support/Nexy
   sudo tccutil reset All com.nexy.assistant
   ```

2. **Clear Launch Services cache:**
   ```bash
   /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister \
     -kill -r -domain local -domain system -domain user
   ```

3. **Reinstall:**
   ```bash
   sudo installer -pkg Nexy-v1.0.1.pkg -target /
   ```

4. **Restart Mac** (clears all system caches)

---

## 🙏 **Acknowledgments**

Special thanks to:
- Early testers who reported the permission dialog issue
- Apple Developer Support for TCC clarifications
- PyObjC community for event loop insights

---

## 📞 **Support**

**Issues?** Check `SUPPORT_PLAYBOOK.md` or contact support.

**Feedback?** We appreciate your input to make Nexy better!

---

**🎉 Enjoy Nexy v1.0.1 - Now with working permission dialogs!**

---

*This is a critical fix release. All v1.0.0 users should upgrade immediately.*

