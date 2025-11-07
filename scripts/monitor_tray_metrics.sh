#!/bin/bash
# Онлайн-мониторинг только нужных метрик tray

echo "=========================================="
echo "TRAY METRICS MONITORING"
echo "=========================================="
echo ""
echo "Monitoring: TRAY_*, CC_READY, CIRCUIT_*, TAL=*, RESTART_FLAG"
echo "Press Ctrl+C to stop"
echo ""
echo "=========================================="
echo ""

log stream --style compact \
  --predicate 'process == "Nexy" && (eventMessage CONTAINS[c] "TRAY_" OR eventMessage CONTAINS[c] "CC_READY" OR eventMessage CONTAINS[c] "CIRCUIT_" OR eventMessage CONTAINS[c] "TAL=" OR eventMessage CONTAINS[c] "RESTART_FLAG")'

