#!/bin/bash
# Interactive Debug Script for First-Run Permission Flow
# This script simulates a fresh install and runs the app in the foreground
# so you can manually verify the permission prompts and delays.

set -e

CLIENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FLAG_FILE="$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag"
RESTART_FLAG="$HOME/Library/Application Support/Nexy/restart_completed.flag"
APP_BUNDLE_ID="com.nexy.assistant"

echo "================================================================"
echo "🕵️  Nexy Interactive First-Run Debugger"
echo "================================================================"
echo ""
echo "This script will:"
echo "1. Kill existing Nexy processes"
echo "2. Delete first-run completion flags"
echo "3. Attempt to reset permissions via tccutil"
echo "4. Run main.py in the FOREGROUND"
echo ""
echo "⚠️  NOTE: When running from source (Python), permission prompts"
echo "    may differ slightly from the compiled .app behavior."
echo "    They might be attributed to 'Terminal' or 'Python'."
echo "================================================================"
echo ""

read -p "Press [Enter] to start..."

# 1. Cleanup
echo "🧹 Killing existing processes..."
PIDS=$(pgrep -f "python3 client/main.py" || true)
if [ -n "$PIDS" ]; then
    echo "$PIDS" | xargs kill -9 2>/dev/null || true
    echo "   ✅ Killed PIDs: $PIDS"
fi

# 2. Reset State
echo "🗑️  Resetting first-run state..."
rm -f "$FLAG_FILE"
rm -f "$RESTART_FLAG"
echo "   ✅ Flags deleted"

# 3. Reset Permissions (Best Effort)
echo "🔐 Resetting permissions (tccutil)..."
if command -v tccutil &> /dev/null; then
    tccutil reset All "$APP_BUNDLE_ID" || echo "   ⚠️  Could not reset bundle ID (running from source?)"
    # Also try resetting for the terminal wrapper if possible, but usually risky to reset Terminal itself
    echo "   ℹ️  Note: You may need to manually remove 'Python' or 'Terminal' from System Settings if prompts don't appear."
else
    echo "   ⚠️  tccutil not found"
fi

# 4. Run App
echo ""
echo "🚀 Starting Nexy (Source Mode)..."
echo "   ------------------------------------------------------------"
echo "   Watch for:"
echo "   1. 15-second delay between prompts"
echo "   2. Order: Mic -> Screen -> Contacts -> FDA -> Input"
echo "   3. 'Controller deferred' log message"
echo "   ------------------------------------------------------------"
echo ""

cd "$CLIENT_DIR"
# Force console logging to INFO/DEBUG to see output
export NEXY_LOG_CONSOLE_LEVEL=INFO
python3 main.py
