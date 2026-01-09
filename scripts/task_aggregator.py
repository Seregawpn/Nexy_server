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

def generate_snapshot(cards: list) -> dict:
    """Generate project_state snapshot from cards."""
    snapshot = {
        "focus": "master",  # Default, can be overridden
        "active_goals": [],
        "current_problems": [],
        "current_risks": [],
        "top_blockers": [],
        "wip_status": {
            "master": {"in_progress": 0, "testing": 0},
            "client": {"in_progress": 0, "testing": 0},
            "server": {"in_progress": 0, "testing": 0}
        },
        "last_sync_at": datetime.now().isoformat()
    }
    
    for card in cards:
        card_id = card.get('id', '')
        card_type = card.get('type', 'task')
        status = card.get('status', '')
        priority = card.get('priority', '')
        workspace = card.get('workspace', 'master')
        blocked_by = card.get('blockedBy', [])
        
        # Skip archived
        if card.get('archived'):
            continue
        
        # Collect goals/problems/risks
        if card_type == 'goal' and status != 'released':
            snapshot['active_goals'].append(card_id)
        elif card_type == 'problem' and status != 'released':
            snapshot['current_problems'].append(card_id)
        elif card_type == 'risk' and status != 'released':
            snapshot['current_risks'].append(card_id)
        
        # Collect blockers (only for non-released tasks)
        if blocked_by and status not in ['released']:
            for blocker_id in blocked_by:
                # Determine impact based on priority
                impact = 'high' if priority in ['P0', 'P1'] else 'medium'
                snapshot['top_blockers'].append({
                    'task': card_id,
                    'blocked_by': blocker_id,
                    'impact': impact
                })
        
        # Count WIP
        if workspace not in snapshot['wip_status']:
            workspace = 'master'
        
        if status == 'in_progress':
            snapshot['wip_status'][workspace]['in_progress'] += 1
        elif status == 'testing':
            snapshot['wip_status'][workspace]['testing'] += 1
    
    # Sort blockers by impact
    snapshot['top_blockers'].sort(key=lambda x: 0 if x['impact'] == 'high' else 1)
    
    # Determine focus based on where most in_progress tasks are
    max_wip = 0
    for ws, counts in snapshot['wip_status'].items():
        total = counts['in_progress'] + counts['testing']
        if total > max_wip:
            max_wip = total
            snapshot['focus'] = ws
    
    return snapshot


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
    
    # Generate project snapshot
    print("\n=== Generating Snapshot ===")
    snapshot = generate_snapshot(master_cards)
    master['project_state'] = snapshot
    
    # Log snapshot summary
    print(f"  Focus: {snapshot['focus']}")
    print(f"  Active goals: {len(snapshot['active_goals'])}")
    print(f"  Problems: {len(snapshot['current_problems'])}")
    print(f"  Risks: {len(snapshot['current_risks'])}")
    print(f"  Top blockers: {len(snapshot['top_blockers'])}")
    for ws, counts in snapshot['wip_status'].items():
        print(f"  WIP {ws}: {counts['in_progress']} in_progress, {counts['testing']} testing")
    
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
