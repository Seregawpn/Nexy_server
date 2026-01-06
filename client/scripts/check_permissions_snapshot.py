#!/usr/bin/env python3
"""
Diagnostic script for checking macOS permission statuses.
Read-only, no runtime interference.

Usage:
    python3 scripts/check_permissions_snapshot.py [--loop N]
    
Options:
    --loop N    Run N iterations with 2s delay to detect stale cache (default: 1)
"""

import subprocess
import sys
import time
from datetime import datetime
from enum import Enum
from typing import Dict, Optional

class Status(Enum):
    GRANTED = "✅ GRANTED"
    DENIED = "❌ DENIED"
    NOT_DETERMINED = "⚠️ NOT_DETERMINED"
    ERROR = "🔴 ERROR"
    UNAVAILABLE = "⚫ UNAVAILABLE"


def check_microphone() -> tuple[Status, str]:
    """Check microphone permission via AVFoundation."""
    try:
        import AVFoundation
        status = AVFoundation.AVCaptureDevice.authorizationStatusForMediaType_(
            AVFoundation.AVMediaTypeAudio
        )
        # 0=NotDetermined, 1=Restricted, 2=Denied, 3=Authorized
        if status == 3:
            return Status.GRANTED, f"AVFoundation status={status}"
        elif status == 2 or status == 1:
            return Status.DENIED, f"AVFoundation status={status}"
        else:
            return Status.NOT_DETERMINED, f"AVFoundation status={status}"
    except ImportError:
        # Fallback: try sounddevice
        try:
            import sounddevice as sd
            devices = sd.query_devices()
            input_devices = [d for d in devices if d.get('max_input_channels', 0) > 0]
            if input_devices:
                return Status.GRANTED, f"sounddevice found {len(input_devices)} input devices"
            else:
                return Status.DENIED, "sounddevice: no input devices"
        except Exception as e:
            return Status.ERROR, f"fallback failed: {e}"
    except Exception as e:
        return Status.ERROR, str(e)


def check_accessibility() -> tuple[Status, str]:
    """Check accessibility via tccutil (safe method, no TCC errors)."""
    try:
        # Get bundle_id
        try:
            from Foundation import NSBundle
            bundle_id = NSBundle.mainBundle().bundleIdentifier() or "com.nexy.assistant"
        except Exception:
            bundle_id = "com.nexy.assistant"
        
        # tccutil check Accessibility <bundle_id>
        result = subprocess.run(
            ['tccutil', 'check', 'Accessibility', bundle_id],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            return Status.GRANTED, f"tccutil check Accessibility {bundle_id}=True"
        else:
            return Status.DENIED, f"tccutil check Accessibility {bundle_id}=False"
    except subprocess.TimeoutExpired:
        return Status.ERROR, "tccutil timeout"
    except FileNotFoundError:
        return Status.UNAVAILABLE, "tccutil not found"
    except Exception as e:
        return Status.ERROR, str(e)


def check_input_monitoring() -> tuple[Status, str]:
    """Check input monitoring via IOHIDCheckAccess or pynput fallback."""
    # Try IOHIDCheckAccess first
    try:
        from Quartz import (
            kIOHIDRequestTypeListenEvent,
            IOHIDCheckAccess,
        )
        # IOHIDCheckAccess returns: 0=Denied, 1=Granted, 2=Unknown/NotDetermined
        access = IOHIDCheckAccess(kIOHIDRequestTypeListenEvent)
        if access == 1:
            return Status.GRANTED, f"IOHIDCheckAccess={access}"
        elif access == 0:
            return Status.DENIED, f"IOHIDCheckAccess={access}"
        else:
            return Status.NOT_DETERMINED, f"IOHIDCheckAccess={access}"
    except (ImportError, AttributeError):
        pass  # Fall through to pynput check
    except Exception as e:
        return Status.ERROR, str(e)
    
    # Fallback: try pynput listener briefly
    try:
        from pynput import keyboard
        import threading
        
        result = {"status": Status.NOT_DETERMINED, "detail": "pynput test"}
        event_received = threading.Event()
        
        def on_press(key):
            result["status"] = Status.GRANTED
            result["detail"] = "pynput listener received events"
            event_received.set()
            return False  # Stop listener
        
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        
        # Wait briefly - if listener starts without error, likely granted
        listener.join(timeout=0.1)
        
        if listener.is_alive():
            listener.stop()
            # Listener ran without error = likely granted
            return Status.GRANTED, "pynput listener started successfully"
        elif result["status"] == Status.GRANTED:
            return result["status"], result["detail"]
        else:
            return Status.GRANTED, "pynput listener completed"
            
    except Exception as e:
        error_str = str(e).lower()
        if "permission" in error_str or "not trusted" in error_str:
            return Status.DENIED, f"pynput: {e}"
        return Status.UNAVAILABLE, f"pynput fallback: {e}"


def check_screen_capture() -> tuple[Status, str]:
    """Check screen capture via CGPreflightScreenCaptureAccess."""
    try:
        from Quartz import CGPreflightScreenCaptureAccess
        granted = CGPreflightScreenCaptureAccess()
        if granted:
            return Status.GRANTED, "CGPreflightScreenCaptureAccess=True"
        else:
            return Status.DENIED, "CGPreflightScreenCaptureAccess=False"
    except ImportError as e:
        return Status.UNAVAILABLE, f"Quartz not available: {e}"
    except Exception as e:
        return Status.ERROR, str(e)


def run_snapshot() -> Dict[str, tuple[Status, str]]:
    """Run all permission checks and return results."""
    return {
        "Microphone": check_microphone(),
        "Accessibility": check_accessibility(),
        "Input Monitoring": check_input_monitoring(),
        "Screen Capture": check_screen_capture(),
    }


def print_table(results: Dict[str, tuple[Status, str]], iteration: int, timestamp: str):
    """Print results as a formatted table."""
    print(f"\n{'='*70}")
    print(f"Iteration {iteration} | {timestamp}")
    print(f"{'='*70}")
    print(f"{'Permission':<20} {'Status':<20} {'Details'}")
    print(f"{'-'*70}")
    for perm, (status, details) in results.items():
        print(f"{perm:<20} {status.value:<20} {details}")
    print(f"{'='*70}")


def main():
    iterations = 1
    
    # Parse --loop argument
    if "--loop" in sys.argv:
        idx = sys.argv.index("--loop")
        if idx + 1 < len(sys.argv):
            try:
                iterations = int(sys.argv[idx + 1])
            except ValueError:
                print("Error: --loop requires an integer")
                sys.exit(1)
    
    print("\n" + "="*70)
    print("  macOS PERMISSIONS SNAPSHOT")
    print("  Read-only diagnostic — no prompts, no side effects")
    print("="*70)
    
    history = []
    
    for i in range(1, iterations + 1):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        results = run_snapshot()
        print_table(results, i, timestamp)
        history.append((timestamp, results))
        
        if i < iterations:
            print(f"\nWaiting 2 seconds before next check...")
            time.sleep(2)
    
    # Summary if multiple iterations
    if iterations > 1:
        print(f"\n{'='*70}")
        print("  CHANGE DETECTION SUMMARY")
        print(f"{'='*70}")
        
        changes_detected = False
        for perm in history[0][1].keys():
            statuses = [h[1][perm][0] for h in history]
            if len(set(s.value for s in statuses)) > 1:
                changes_detected = True
                print(f"{perm}: CHANGED")
                for ts, res in history:
                    print(f"  {ts}: {res[perm][0].value}")
        
        if not changes_detected:
            print("No status changes detected across iterations.")
        print(f"{'='*70}")


if __name__ == "__main__":
    main()
