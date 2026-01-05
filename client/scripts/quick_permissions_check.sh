#!/bin/bash
# Быстрая проверка статуса разрешений через permissions_probe.py

echo "🔍 Быстрая проверка разрешений для com.nexy.assistant"
echo "=================================================="
echo ""

cd "$(dirname "$0")/.."
python3 scripts/permissions_probe.py

echo ""
echo "📋 Для сравнения с baseline:"
echo "   diff baseline_before.txt baseline_after.txt"
