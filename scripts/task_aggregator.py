#!/usr/bin/env python3
"""
Task Aggregator for Federated CRM Workspaces

Scans client/.crm/TASKS.json and server/.crm/TASKS.json,
merges them into Docs/PROJECT_KANBAN.json preserving workspace isolation.

Rules:
1. Key = id + workspace
2. If local updated_at > master → update master
3. Never delete master cards (only add/update)
4. Cards without workspace are protected (master-only)
"""
import json
import os
from datetime import datetime

# Configuration
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(ROOT_DIR, 'Docs')
MASTER_JSON = os.path.join(DOCS_DIR, 'PROJECT_KANBAN.json')

WORKSPACES = [
    {
        'name': 'client',
        'path': os.path.join(ROOT_DIR, 'client', '.crm', 'TASKS.json')
    },
    {
        'name': 'server', 
        'path': os.path.join(ROOT_DIR, 'server', '.crm', 'TASKS.json')
    }
]

def load_json(path):
    """Load JSON file, return empty dict if not found."""
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_json(path, data):
    """Save JSON with pretty printing."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def parse_datetime(dt_str):
    """Parse ISO datetime string, return epoch 0 if invalid."""
    if not dt_str:
        return datetime.min
    try:
        # Handle various formats
        for fmt in ['%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d']:
            try:
                return datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
            except:
                continue
        return datetime.min
    except:
        return datetime.min

def main():
    print("=== Task Aggregator ===")
    
    # Load master
    master = load_json(MASTER_JSON)
    if not master:
        print(f"Error: Master JSON not found at {MASTER_JSON}")
        return
    
    master_cards = master.get('cards', [])
    
    # Index master cards by (id, workspace) for quick lookup
    master_index = {}
    for card in master_cards:
        key = (card.get('id'), card.get('workspace'))
        master_index[key] = card
    
    added = 0
    updated = 0
    
    # Process each workspace
    for ws in WORKSPACES:
        ws_name = ws['name']
        ws_path = ws['path']
        
        if not os.path.exists(ws_path):
            print(f"Workspace '{ws_name}': No TASKS.json found, skipping.")
            continue
        
        ws_data = load_json(ws_path)
        ws_tasks = ws_data.get('tasks', [])
        print(f"Workspace '{ws_name}': Found {len(ws_tasks)} tasks")
        
        for task in ws_tasks:
            task_id = task.get('id')
            if not task_id:
                continue

            if not task.get('created_by'):
                print(f"  Skipping: {task_id} (missing created_by)")
                continue

            if not task.get('updated_at'):
                print(f"  Skipping: {task_id} (missing updated_at)")
                continue
            
            # Ensure workspace field is set
            task['workspace'] = ws_name
            # Owner is the workspace by policy
            task['owner'] = ws_name
            
            key = (task_id, ws_name)
            
            if key in master_index:
                # Task exists in master, check if update needed
                master_card = master_index[key]
                local_time = parse_datetime(task.get('updated_at'))
                master_time = parse_datetime(master_card.get('updated_at'))
                
                if local_time > master_time:
                    # Update master with local data
                    master_card.update(task)
                    print(f"  Updated: {task_id}")
                    updated += 1
            else:
                # New task, add to master
                master_cards.append(task)
                master_index[key] = task
                print(f"  Added: {task_id}")
                added += 1
    
    # Update master
    master['cards'] = master_cards
    master['meta']['updated_at'] = datetime.now().isoformat()
    
    # Save
    save_json(MASTER_JSON, master)
    
    print(f"\n=== Summary ===")
    print(f"Added: {added}")
    print(f"Updated: {updated}")
    print(f"Master now has {len(master_cards)} cards")

if __name__ == '__main__':
    main()
