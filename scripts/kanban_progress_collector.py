#!/usr/bin/env python3
import json
import os
import re
import sys

# Configuration
DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Docs')
JSON_PATH = os.path.join(DOCS_DIR, 'PROJECT_KANBAN.json')
REGISTRY_PATH = os.path.join(DOCS_DIR, 'CRM_INSTRUCTION_REGISTRY.md')

def load_registry():
    """Parses CRM_INSTRUCTION_REGISTRY.md to map INS-IDs to file paths."""
    registry = {}
    if not os.path.exists(REGISTRY_PATH):
        print(f"Error: Registry not found at {REGISTRY_PATH}")
        return registry

    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find | **INS-XXX** | ... | [Title](./File) |
    # Matches: | (**)?(INS-\d+)(**)? | .*? | \[(.*?)\]\((.*?)\) |
    pattern = r'\|\s*(?:\*\*)?(INS-\d+)(?:\*\*)?\s*\|.*?\|\s*\[.*?\]\((.*?)\)\s*\|'
    matches = re.finditer(pattern, content)
    
    for m in matches:
        ins_id = m.group(1)
        rel_path = m.group(2)
        # Resolve path relative to DOCS_DIR
        full_path = os.path.normpath(os.path.join(DOCS_DIR, rel_path))
        registry[ins_id] = full_path
        
    print(f"Loaded {len(registry)} registry entries.")
    return registry

def calculate_progress(file_path):
    """Reads a markdown file and counts [x] vs [ ]."""
    if not os.path.exists(file_path):
        print(f"Warning: File not found {file_path}")
        return 0, []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total = 0
    done = 0
    evidence = []

    for line in lines:
        line = line.strip()
        if re.match(r'^[-*]\s*\[[xX]\]', line):
            done += 1
            total += 1
            evidence.append(line[6:].strip()) # Store text after "- [x] "
        elif re.match(r'^[-*]\s*\[\s*\]', line):
            total += 1
    
    percent = int((done / total * 100)) if total > 0 else 0
    return percent, evidence

def main():
    print(f"--- Kanban Progress Collector ---")
    
    # 1. Load Registry
    registry_map = load_registry()
    if not registry_map:
        return

    # 2. Load JSON
    if not os.path.exists(JSON_PATH):
        print(f"Error: JSON not found at {JSON_PATH}")
        return

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cards = data.get('cards', [])
    updated_count = 0

    # 3. Update Tasks
    for card in cards:
        ref = card.get('registry_ref')
        if ref:
            if ref in registry_map:
                file_path = registry_map[ref]
                print(f"Processing Task '{card['title']}' -> {ref} ({os.path.basename(file_path)})")
                
                progress, evidence = calculate_progress(file_path)
                
                # Update only if changed (simple check) or just overwrite
                card['progress'] = progress
                card['evidence'] = evidence  # Store list of completed items per Contract
                
                print(f"  -> Progress: {progress}% ({len(evidence)} items done)")
                updated_count += 1
            else:
                print(f"Warning: Task '{card['title']}' has unknown registry_ref '{ref}'")

    # 4. Save
    if updated_count > 0:
        with open(JSON_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Saved {updated_count} updated tasks to {JSON_PATH}")
    else:
        print("No tasks with registry_ref found or updated.")

if __name__ == '__main__':
    main()
