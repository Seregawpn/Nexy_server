# Troubleshooting Guide

## Push-to-Talk (PTT) Issues

### PTT Not Working in Password Fields (Secure Input)

**Symptom:**
When a password field is focused (e.g., in Terminal `sudo`, Safari, or System Settings), the PTT hotkey (Ctrl+N) does not activate the microphone.

**Cause:**
macOS enables "Secure Input" mode when a sensitive field is focused. This security feature blocks all other applications (including Nexy) from intercepting keyboard events to prevent keyloggers.

**Behavior:**
-   **PTT Disabled:** The microphone will not open.
-   **No System Beep:** Nexy automatically detects Secure Input and suppresses the system "beep" that usually occurs when pressing blocked hotkeys.
-   **Auto-Recovery:** As soon as you click away from the password field or close the secure window, PTT functionality restores automatically.

**Solution:**
1.  Click outside the password field to remove focus.
2.  Use PTT normally.
3.  If PTT does not recover, try clicking the Nexy menu bar icon to refresh the state.
