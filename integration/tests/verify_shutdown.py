import asyncio
import time
import logging
import threading
from modules.voice_recognition.core.audio_route_monitor import AudioRouteMonitor
from modules.speech_playback.core.avf_player import AVFoundationPlayer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_shutdown_speed():
    logger.info("🧪 Testing AudioRouteMonitor Shutdown Speed...")
    monitor = AudioRouteMonitor()
    monitor.start()
    
    start = time.monotonic()
    monitor.stop()
    end = time.monotonic()
    
    duration = end - start
    logger.info(f"⏱️ AudioRouteMonitor stop took {duration:.4f} seconds")
    
    if duration > 0.5:
        logger.error("❌ AudioRouteMonitor stop is still too slow!")
    else:
        logger.info("✅ AudioRouteMonitor stop is fast!")

    logger.info("🧪 Testing QuartzKeyboardMonitor Shutdown Speed...")
    from modules.input_processing.keyboard.mac.quartz_monitor import QuartzKeyboardMonitor
    from modules.input_processing.keyboard.types import KeyboardConfig
    
    kb_config = KeyboardConfig(
        key_to_monitor="left_shift",
        short_press_threshold=0.3,
        long_press_threshold=0.6,
        event_cooldown=0.1,
        hold_check_interval=0.05,
        debounce_time=0.05
    )
    kb_monitor = QuartzKeyboardMonitor(kb_config)
    # We don't necessarily need to start it (which might fail in CI/without permissions)
    # but we can test the stop() logic responsiveness if it was started.
    # However, to be realistic, let's try to start it.
    if kb_monitor.start_monitoring():
        start = time.monotonic()
        kb_monitor.stop_monitoring()
        end = time.monotonic()
        duration = end - start
        logger.info(f"⏱️ QuartzKeyboardMonitor stop took {duration:.4f} seconds")
        if duration > 0.5:
            logger.error("❌ QuartzKeyboardMonitor stop is too slow!")
        else:
            logger.info("✅ QuartzKeyboardMonitor stop is fast!")
    else:
        logger.warning("⚠️ Could not start QuartzKeyboardMonitor (permissions?), skipping its timing check.")

    logger.info("🧪 Testing AVFoundationPlayer Thread Tracking...")
    player = AVFoundationPlayer()
    player.initialize()
    player.start_playback()
    
    # Simulate a route change to trigger a recreate thread
    # We can't easily trigger a real notification, so we call the handler directly
    logger.info("Triggering mock route change...")
    player._on_route_change(None)
    
    # Give it a tiny bit of time to start
    await asyncio.sleep(0.1)
    
    start = time.monotonic()
    player.shutdown()
    end = time.monotonic()
    
    duration = end - start
    logger.info(f"⏱️ AVFoundationPlayer shutdown took {duration:.4f} seconds")
    
    # Check if recreate threads are still around
    alive_threads = [t for t in threading.enumerate() if t.name == "AVFRecreate"]
    if alive_threads:
        logger.error(f"❌ Lingering recreate threads found: {alive_threads}")
    else:
        logger.info("✅ No lingering recreate threads!")

if __name__ == "__main__":
    asyncio.run(test_shutdown_speed())
