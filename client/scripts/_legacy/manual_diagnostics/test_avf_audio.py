#!/usr/bin/env python3
"""
Test: Does NSApplication (rumps) run loop interfere with AVAudioEngine playback?

This test runs AVAudioEngine playback INSIDE an NSApplication context,
matching the real app's setup.

Usage:
    python scripts/test_avf_audio.py
"""

import math
import sys
import time

import numpy as np

# ── AVFoundation imports ──────────────────────────────────────────────────
try:
    from AVFoundation import (
        AVAudioEngine,
        AVAudioFormat,
        AVAudioPCMBuffer,
        AVAudioPlayerNode,
        AVAudioSession,
    )
    print("✅ AVFoundation loaded")
except ImportError as e:
    print(f"❌ Cannot import AVFoundation: {e}")
    sys.exit(1)

try:
    import rumps
    HAS_RUMPS = True
    print("✅ rumps loaded")
except ImportError:
    HAS_RUMPS = False
    print("⚠️ rumps not available")

try:
    import pyaudio
    HAS_PYAUDIO = True
    print("✅ PyAudio loaded")
except ImportError:
    HAS_PYAUDIO = False

SAMPLE_RATE = 48000
CHANNELS = 1
DURATION_SEC = 3.0
FREQUENCY_HZ = 440.0


def generate_float32_sine(sr, freq, duration, amp=0.5):
    t = np.arange(int(sr * duration), dtype=np.float32) / sr
    return (amp * np.sin(2.0 * math.pi * freq * t)).astype(np.float32)


def play_tone_and_report(label, engine, player, fmt, context=""):
    """Schedule and play a tone."""
    audio = generate_float32_sine(SAMPLE_RATE, FREQUENCY_HZ, DURATION_SEC)
    frame_count = len(audio)
    buf = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(fmt, frame_count)
    buf.setFrameLength_(frame_count)
    ptr = buf.floatChannelData()[0]
    raw = ptr.as_buffer(frame_count)
    dst = np.frombuffer(raw, dtype=np.float32, count=frame_count)
    dst[:] = np.ascontiguousarray(audio, dtype=np.float32)
    peak = float(np.max(np.abs(dst)))

    out_fmt = engine.outputNode().outputFormatForBus_(0)
    print(f"  [{label}] {context}")
    print(f"  [{label}] output={out_fmt.sampleRate()}Hz/{out_fmt.channelCount()}ch, "
          f"buf_peak={peak:.4f}, engine={engine.isRunning()}, player={player.isPlaying()}")

    player.scheduleBuffer_completionHandler_(buf, None)
    print(f"  [{label}] 🔊 Playing {DURATION_SEC}s tone at {FREQUENCY_HZ}Hz...")
    time.sleep(DURATION_SEC + 0.5)
    print(f"  [{label}] Done")


def create_engine():
    engine = AVAudioEngine.alloc().init()
    player = AVAudioPlayerNode.alloc().init()
    fmt = AVAudioFormat.alloc().initWithCommonFormat_sampleRate_channels_interleaved_(
        1, SAMPLE_RATE, CHANNELS, False
    )
    engine.attachNode_(player)
    mixer = engine.mainMixerNode()
    engine.connect_to_format_(player, mixer, fmt)
    player.setVolume_(1.0)
    mixer.setOutputVolume_(1.0)
    engine.prepare()
    success, err = engine.startAndReturnError_(None)
    if not success:
        print(f"  ❌ Engine failed: {err}")
        return None, None, None
    player.play()
    return engine, player, fmt


def test_with_session_config(label, category_obj=None, options=0):
    """Test playback WITH AVAudioSession configuration."""
    print(f"\n{'='*60}")
    print(f"TEST: {label}")
    print(f"{'='*60}")

    if category_obj is not None:
        try:
            session = AVAudioSession.sharedInstance()
            session.setCategory_mode_options_error_(
                category_obj, session.mode(), options, None
            )
            session.setActive_error_(True, None)
            print(f"  Session: {session.category()}, options={options}")
        except Exception as e:
            print(f"  Session error: {e}")

    engine, player, fmt = create_engine()
    if engine is None:
        return

    play_tone_and_report(label, engine, player, fmt, "with session config")
    player.stop()
    engine.stop()
    time.sleep(0.3)


def run_without_nsapp():
    """Run all tests WITHOUT NSApplication run loop."""
    print(f"\n{'#'*60}")
    print("# PART A: WITHOUT NSApplication (normal Python)")
    print(f"{'#'*60}")

    # Test 1: No session config
    test_with_session_config("A1_NO_SESSION")

    # Test 2: Playback session
    from AVFoundation import AVAudioSessionCategoryPlayback
    test_with_session_config("A2_PLAYBACK", AVAudioSessionCategoryPlayback, 32)

    # Test 3: PlayAndRecord session
    from AVFoundation import AVAudioSessionCategoryPlayAndRecord
    test_with_session_config("A3_PLAY_AND_RECORD", AVAudioSessionCategoryPlayAndRecord, 40)


def run_with_nsapp():
    """Run tests INSIDE NSApplication run loop (like the real app)."""
    if not HAS_RUMPS:
        print("\n⚠️ rumps not available, skipping NSApp tests")
        return

    print(f"\n{'#'*60}")
    print("# PART B: WITH NSApplication (rumps) — matches real app")
    print(f"{'#'*60}")

    results = []

    class TestApp(rumps.App):
        def __init__(self):
            super().__init__("AudioTest", quit_button=None)
            # Schedule the test to run after app starts
            self._timer = rumps.Timer(self._run_tests, 1)
            self._timer.start()

        def _run_tests(self, _timer):
            self._timer.stop()
            print(f"  📱 NSApplication run loop is active")
            print(f"  📱 Running tests inside NSApp context...")

            # Test B1: No session, inside NSApp
            print(f"\n{'='*60}")
            print("TEST B1: No session config, inside NSApp run loop")
            print(f"{'='*60}")
            engine, player, fmt = create_engine()
            if engine:
                play_tone_and_report("B1", engine, player, fmt, "inside NSApp, no session")
                player.stop()
                engine.stop()
                time.sleep(0.3)
                results.append(("B1_NSAPP_NO_SESSION", True))

            # Test B2: With Playback session, inside NSApp
            print(f"\n{'='*60}")
            print("TEST B2: Playback session, inside NSApp run loop")
            print(f"{'='*60}")
            try:
                from AVFoundation import AVAudioSessionCategoryPlayback
                session = AVAudioSession.sharedInstance()
                session.setCategory_mode_options_error_(
                    AVAudioSessionCategoryPlayback, session.mode(), 32, None
                )
                session.setActive_error_(True, None)
                print(f"  Session: Playback, options=32")
            except Exception as e:
                print(f"  Session error: {e}")
            engine, player, fmt = create_engine()
            if engine:
                play_tone_and_report("B2", engine, player, fmt, "inside NSApp, Playback session")
                player.stop()
                engine.stop()
                time.sleep(0.3)
                results.append(("B2_NSAPP_PLAYBACK", True))

            # Test B3: With PlayAndRecord session, inside NSApp
            print(f"\n{'='*60}")
            print("TEST B3: PlayAndRecord session, inside NSApp run loop")
            print(f"{'='*60}")
            try:
                from AVFoundation import AVAudioSessionCategoryPlayAndRecord
                session = AVAudioSession.sharedInstance()
                session.setCategory_mode_options_error_(
                    AVAudioSessionCategoryPlayAndRecord, session.mode(), 40, None
                )
                session.setActive_error_(True, None)
                print(f"  Session: PlayAndRecord, options=40")
            except Exception as e:
                print(f"  Session error: {e}")
            engine, player, fmt = create_engine()
            if engine:
                play_tone_and_report("B3", engine, player, fmt, "inside NSApp, PlayAndRecord session")
                player.stop()
                engine.stop()
                time.sleep(0.3)
                results.append(("B3_NSAPP_PLAYANDRECORD", True))

            # Test B4: With PyAudio mic + PlayAndRecord, inside NSApp
            if HAS_PYAUDIO:
                print(f"\n{'='*60}")
                print("TEST B4: PyAudio mic + PlayAndRecord + NSApp (full app conditions)")
                print(f"{'='*60}")
                try:
                    pa = pyaudio.PyAudio()
                    dev = pa.get_default_input_device_info()
                    mic = pa.open(
                        format=pyaudio.paInt16, channels=1, rate=16000,
                        input=True, frames_per_buffer=1024,
                        input_device_index=dev['index'],
                    )
                    print(f"  🎤 Mic: {dev['name']}")

                    engine, player, fmt = create_engine()
                    if engine:
                        play_tone_and_report("B4", engine, player, fmt,
                                           "inside NSApp + mic + PlayAndRecord")
                        player.stop()
                        engine.stop()
                    mic.stop_stream()
                    mic.close()
                    pa.terminate()
                    results.append(("B4_NSAPP_FULL", True))
                except Exception as e:
                    print(f"  ❌ Error: {e}")

            print(f"\n{'='*60}")
            print("ALL NSAPP TESTS COMPLETE")
            print("If NONE of the B-tests produced sound → NSApp is the issue!")
            print("If A-tests worked but B-tests didn't → NSApp run loop conflict!")
            print(f"{'='*60}")

            # Quit the NSApp
            rumps.quit_application()

    print("  Starting NSApplication via rumps...")
    app = TestApp()
    app.run()


def main():
    print(f"\n🔊 NSApplication + AVAudioEngine Conflict Test")
    print(f"   Tone: {FREQUENCY_HZ}Hz, Duration: {DURATION_SEC}s")

    try:
        session = AVAudioSession.sharedInstance()
        route = session.currentRoute()
        outputs = route.outputs() if route else []
        if outputs and len(outputs) > 0:
            print(f"   Output: {outputs[0].portName()} ({outputs[0].portType()})")
    except Exception:
        pass

    # Part A: Without NSApplication
    run_without_nsapp()

    # Part B: With NSApplication
    run_with_nsapp()

    print(f"\n{'#'*60}")
    print("# SUMMARY")
    print(f"{'#'*60}")
    print("Part A (no NSApp): Did you hear all 3 tones?")
    print("Part B (with NSApp): Did you hear all 4 tones?")
    print()
    print("If Part A works but Part B doesn't → NSApplication interferes!")
    print("If both work → issue is deeper in the app's specific code")


if __name__ == "__main__":
    main()
