#!/bin/bash
# Анализ SLO после прогона

set -e

echo "=========================================="
echo "SLO ANALYSIS"
echo "=========================================="
echo ""

# Сохраняем логи
LOG_FILE="log_$(date +%Y%m%d_%H%M%S).md"
echo "Saving logs to: $LOG_FILE"
log show --last 15m --style compact --predicate 'process == "Nexy"' > "$LOG_FILE"

echo ""
echo "=========================================="
echo "WARM START ANALYSIS"
echo "=========================================="
python scripts/parse_tray_metrics.py "$LOG_FILE" --warm-start

echo ""
echo "=========================================="
echo "COLD START ANALYSIS"
echo "=========================================="
python scripts/parse_tray_metrics.py "$LOG_FILE" --cold-start

echo ""
echo "=========================================="
echo "DONE"
echo "=========================================="
echo "Log file: $LOG_FILE"

