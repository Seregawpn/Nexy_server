
import asyncio
import logging
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)
sys.path.append(client_dir)

from integration.core.event_bus import EventBus
from integration.integrations.browser_use_integration import BrowserUseIntegration

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MANUAL_TEST")

async def main():
    print("Browser Use Integration - Manual Verification Script")
    
    from config.unified_config_loader import unified_config
    
    # Try to load from config first
    config_data = unified_config._load_config()
    browser_use_config = config_data.get('browser_use', {})
    
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or browser_use_config.get('gemini_api_key')
    
    if not api_key:
        print("❌ API Key not found in environment variables or unified_config.yaml.")
        return
    
    os.environ["GEMINI_API_KEY"] = api_key
    
    event_bus = EventBus()
    integration = BrowserUseIntegration(event_bus)
    
    if not await integration.initialize():
        print("Failed to initialize integration")
        return

    import subprocess

    async def speak(text):
        if not text: return
        try:
            # Run 'say' in background so it doesn't block the browser step
            subprocess.Popen(["say", text])
        except Exception as e:
            print(f"Error speaking: {e}")

    async def on_step(event):
        data = event.get('data', event)
        step_desc = data.get('description', '')
        print(f"[STEP {data.get('step_number')}] {step_desc}")
        # Removed manual speak() to verify integration's TTS request
        
    async def on_tts_request(event):
        data = event.get('data', event)
        text = data.get('text', '')
        print(f"🔊 [TTS REQUEST] '{text}'")
        await speak(text)

    await event_bus.subscribe("browser.step", on_step)
    await event_bus.subscribe("grpc.tts_request", on_tts_request)

    async def on_completed(event):
        print("[COMPLETED] Task finished successfully!")
        print(f"🔊 Speaking: 'Task completed'")
        await speak("Browser task completed successfully")
        setattr(event_bus, '_test_completed', True)

    async def on_failed(event):
        data = event.get('data', event)
        error_msg = data.get('error')
        print(f"[FAILED] Task failed: {error_msg}")
        print(f"🔊 Speaking: 'Task failed'")
        await speak("Browser task failed")
        setattr(event_bus, '_test_completed', True)

    await event_bus.subscribe("browser.step", on_step)
    await event_bus.subscribe("browser.completed", on_completed)
    await event_bus.subscribe("browser.failed", on_failed)
    
    task_prompt = "Go to youtube.com/results?search_query=eminem+without+me and click on the first video."
    
    payload = {
        "session_id": "manual_test",
        "task": task_prompt,
        "config_preset": "fast"
    }
    
    print(f"Sending Task: '{task_prompt}'")
    await event_bus.publish("browser.use.request", payload)
    
    try:
        # Simulate wait before interruption
        await asyncio.sleep(5)
        print("🛑 SIMULATING INTERRUPTION (keyboard.short_press)...")
        await event_bus.publish("keyboard.short_press", {"source": "manual_test"})
        
        # Wait a bit to see cancellation effects
        await asyncio.sleep(2)
        
        while not hasattr(event_bus, '_test_completed'):
            await asyncio.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        await integration.stop()

if __name__ == "__main__":
    asyncio.run(main())
