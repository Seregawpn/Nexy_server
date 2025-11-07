#!/bin/bash
# Проверка каскада Aux и XPC/Scene-ошибок

echo "=========================================="
echo "AUX CASCADE & XPC ERROR CHECK"
echo "=========================================="
echo ""
echo "Checking for: BSServiceConnectionErrorDomain, InvalidScene, -Aux["
echo ""
echo "=========================================="
echo ""

log show --last 15m --style compact \
  --predicate 'process == "Nexy" AND (eventMessage CONTAINS[c] "BSServiceConnectionErrorDomain" OR eventMessage CONTAINS[c] "InvalidScene" OR eventMessage CONTAINS[c] "-Aux[" )'

echo ""
echo "=========================================="
echo "SUMMARY"
echo "=========================================="

count=$(log show --last 15m --style compact \
  --predicate 'process == "Nexy" AND (eventMessage CONTAINS[c] "BSServiceConnectionErrorDomain" OR eventMessage CONTAINS[c] "InvalidScene" OR eventMessage CONTAINS[c] "-Aux[" )' 2>/dev/null | wc -l | tr -d ' ')

if [ "$count" -eq 0 ]; then
    echo "✅ PASS: No Aux cascade or XPC errors found"
else
    echo "❌ FAIL: Found $count occurrences of Aux cascade or XPC errors"
    echo ""
    echo "Check the logs above for details"
fi

