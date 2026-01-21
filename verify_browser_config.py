
import sys
import os
import yaml

def check_yaml_config(file_path, config_type):
    print(f"\n--- Checking {config_type} Config ({file_path}) ---")
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        
        browser_use = data.get('browser_use', {})
        enabled = browser_use.get('enabled')
        
        print(f"{config_type} browser_use.enabled: {enabled}")
        
        if enabled is True:
            print(f"✅ {config_type} Config is ENABLED")
        else:
            print(f"❌ {config_type} Config is DISABLED or Missing (Value: {enabled})")
            
    except Exception as e:
        print(f"❌ Failed to load {config_type} config: {e}")

check_yaml_config('/Users/sergiyzasorin/Fix_new/server/server/config/unified_config.yaml', 'Server')
check_yaml_config('/Users/sergiyzasorin/Fix_new/client/config/unified_config.yaml', 'Client')

