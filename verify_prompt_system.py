#!/usr/bin/env python3
"""
Verification script for modular prompt system.
Tests various feature flag combinations by spawning fresh processes.
"""
import subprocess
import os

def test_scenario(name: str, env_vars: dict):
    """Test a specific scenario with given environment variables."""
    print(f"\n{'='*60}")
    print(f"📋 SCENARIO: {name}")
    print(f"{'='*60}")
    
    # Build the test command
    test_code = '''
import sys
sys.path.insert(0, ".")
from server.config.unified_config import UnifiedServerConfig

config = UnifiedServerConfig()
prompt = config.text_processing.gemini_system_prompt

# Check what's in the prompt
checks = {
    "System Actions (open_app)": "open_app" in prompt and "**SYSTEM ACTIONS" in prompt,
    "Messages Actions": "**MESSAGES ACTIONS" in prompt,
    "WhatsApp Actions": "**WHATSAPP ACTIONS" in prompt,
    "Browser Automation": "**BROWSER AUTOMATION" in prompt,
    "Subscription Actions": "**SUBSCRIPTION/PAYMENT ACTIONS" in prompt,
}

# Check allowed commands
if "MUST be exactly one of:" in prompt:
    rules_start = prompt.find("MUST be exactly one of:")
    rules_end = prompt.find("\\n", rules_start)
    allowed_commands_line = prompt[rules_start:rules_end]
    print(f"ALLOWED: {allowed_commands_line[24:]}")

# Check priority list
if "[Processing Priority]" in prompt:
    priority_start = prompt.find("[Processing Priority]")
    priority_end = prompt.find("━━━", priority_start + 1)
    priority_section = prompt[priority_start:priority_end]
    lines = [l.strip() for l in priority_section.split("\\n") if l.strip() and l[0].isdigit()]
    for line in lines[:7]:
        print(f"PRIORITY: {line}")

# Print feature checks
for feature, present in checks.items():
    status = "YES" if present else "NO"
    print(f"FEATURE: {feature} = {status}")
'''
    
    # Prepare environment
    env = os.environ.copy()
    env.update(env_vars)
    
    # Run in subprocess
    result = subprocess.run(
        ["python3", "-c", test_code],
        cwd="/Users/sergiyzasorin/Fix_new/server",
        env=env,
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"❌ ERROR: {result.stderr}")
        return
    
    # Parse output
    output = result.stdout.strip()
    for line in output.split('\n'):
        if line.startswith("ALLOWED:"):
            print(f"\n📜 Allowed Commands: {line[8:].strip()}")
        elif line.startswith("PRIORITY:"):
            print(f"   {line[10:].strip()}")
        elif line.startswith("FEATURE:"):
            parts = line[8:].strip().split(" = ")
            status = "✓" if parts[1] == "YES" else "✗"
            print(f"   [{status}] {parts[0]}")


def main():
    print("🔍 MODULAR PROMPT SYSTEM VERIFICATION (Fresh Process)")
    print("="*60)
    
    # Scenario 1: All defaults (everything enabled where appropriate)
    test_scenario("All Features at Default", {})
    
    # Scenario 2: Enable everything
    test_scenario("All Features ENABLED", {
        "MANAGE_APPS_ENABLED": "true",
        "BROWSER_USE_ENABLED": "true",
        "WHATSAPP_ENABLED": "true",
        "SUBSCRIPTION_ENABLED": "true"
    })
    
    # Scenario 3: Disable App Management
    test_scenario("App Management DISABLED", {
        "MANAGE_APPS_ENABLED": "false",
        "BROWSER_USE_ENABLED": "true",
        "SUBSCRIPTION_ENABLED": "true"
    })
    
    # Scenario 4: Disable Browser
    test_scenario("Browser DISABLED", {
        "MANAGE_APPS_ENABLED": "true",
        "BROWSER_USE_ENABLED": "false",
        "SUBSCRIPTION_ENABLED": "true"
    })
    
    # Scenario 5: Disable Subscription
    test_scenario("Subscription DISABLED", {
        "MANAGE_APPS_ENABLED": "true",
        "BROWSER_USE_ENABLED": "true",
        "SUBSCRIPTION_ENABLED": "false"
    })
    
    # Scenario 6: Only Messages (all others off)
    test_scenario("Only Messages (All Others DISABLED)", {
        "MANAGE_APPS_ENABLED": "false",
        "BROWSER_USE_ENABLED": "false",
        "WHATSAPP_ENABLED": "false",
        "SUBSCRIPTION_ENABLED": "false"
    })
    
    print("\n" + "="*60)
    print("✅ VERIFICATION COMPLETE")
    print("="*60)


if __name__ == "__main__":
    main()
