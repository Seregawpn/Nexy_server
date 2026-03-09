import sys
import os
from pathlib import Path

# Add server directory to path
server_dir = Path(__file__).resolve().parent.parent.parent / "server"
sys.path.append(str(server_dir))

from server.config.unified_config import get_config, UnifiedServerConfig
import server.config.prompts as prompts

def verify_prompt():
    print("🚀 Starting Prompt Builder Verification...")
    
    # 1. Load default config
    config = get_config()
    initial_prompt = config.text_processing.gemini_system_prompt
    
    print(f"✅ Initial Prompt Length: {len(initial_prompt)}")
    
    # Check for core components
    if "You are Nexy Assistant" in initial_prompt:
        print("✅ Core Header present")
    else:
        print("❌ Core Header MISSING")
        
    # Check for WhatsApp (assuming enabled by default or in current env)
    whatsapp_enabled = config.whatsapp.enabled
    print(f"ℹ️ WhatsApp Enabled: {whatsapp_enabled}")
    
    if whatsapp_enabled:
        if "WHATSAPP ACTIONS" in initial_prompt:
            print("✅ WhatsApp instructions present (Correct)")
        else:
            print("❌ WhatsApp instructions MISSING but feature is enabled")
    else:
        if "WHATSAPP ACTIONS" in initial_prompt:
            print("❌ WhatsApp instructions PRESENT but feature is disabled")
        else:
            print("✅ WhatsApp instructions absent (Correct)")

    # 2. Test Dynamic Switching
    print("\n🔄 Testing Dynamic Switching...")
    
    # Force Disable WhatsApp
    print("   → Disabling WhatsApp...")
    config.whatsapp.enabled = False
    new_prompt_no_wa = config._build_system_prompt()
    
    if "WHATSAPP ACTIONS" not in new_prompt_no_wa:
        print("✅ WhatsApp instructions successfully REMOVED")
    else:
        print("❌ WhatsApp instructions STILL PRESENT after disabling")
        
    # Force Enable WhatsApp
    print("   → Enabling WhatsApp...")
    config.whatsapp.enabled = True
    new_prompt_wa = config._build_system_prompt()
    
    if "WHATSAPP ACTIONS" in new_prompt_wa:
        print("✅ WhatsApp instructions successfully ADDED")
    else:
        print("❌ WhatsApp instructions MISSING after enabling")

    # Force Disable Browser
    print("   → Disabling Browser...")
    config.browser_use.enabled = False
    new_prompt_no_browser = config._build_system_prompt()
    
    if "Browser Automation Intent" not in new_prompt_no_browser:
        print("✅ Browser instructions successfully REMOVED")
    else:
        print("❌ Browser instructions STILL PRESENT after disabling")
        
    # Force Enable Browser
    print("   → Enabling Browser...")
    config.browser_use.enabled = True
    new_prompt_browser = config._build_system_prompt()
    
    if "Browser Automation Intent" in new_prompt_browser:
        print("✅ Browser instructions successfully ADDED")
    else:
        print("❌ Browser instructions MISSING after enabling")

    # Force Disable Payment
    print("   → Disabling Payment...")
    config.payment_use.enabled = False
    new_prompt_no_payment = config._build_system_prompt()
    
    if "Subscription & Payment Intent" not in new_prompt_no_payment:
        print("✅ Payment instructions successfully REMOVED")
    else:
        print("❌ Payment instructions STILL PRESENT after disabling")
        
    # Force Enable Payment
    print("   → Enabling Payment...")
    config.payment_use.enabled = True
    new_prompt_payment = config._build_system_prompt()
    
    if "Subscription & Payment Intent" in new_prompt_payment:
        print("✅ Payment instructions successfully ADDED")
    else:
        print("❌ Payment instructions MISSING after enabling")

    print("\n✨ Verification Complete!")

if __name__ == "__main__":
    verify_prompt()
