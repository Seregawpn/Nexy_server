#!/bin/bash
# Быстрый скрипт для приёмки tray icon

set -e

echo "=========================================="
echo "TRAY ICON ACCEPTANCE TEST"
echo "=========================================="
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Функция для проверки логов
check_logs() {
    local test_name="$1"
    local pattern="$2"
    local expected_count="${3:-1}"
    
    echo -e "${YELLOW}Checking: ${test_name}${NC}"
    
    # Проверяем наличие метрик в логах
    if log show --last 5m --style compact --predicate "process == 'Nexy' && eventMessage CONTAINS[c] '${pattern}'" 2>/dev/null | grep -q "${pattern}"; then
        count=$(log show --last 5m --style compact --predicate "process == 'Nexy' && eventMessage CONTAINS[c] '${pattern}'" 2>/dev/null | grep -c "${pattern}" || echo "0")
        if [ "$count" -ge "$expected_count" ]; then
            echo -e "${GREEN}✅ ${test_name}: Found ${count} occurrences${NC}"
            return 0
        else
            echo -e "${RED}❌ ${test_name}: Found only ${count} occurrences (expected ${expected_count})${NC}"
            return 1
        fi
    else
        echo -e "${RED}❌ ${test_name}: Not found${NC}"
        return 1
    fi
}

# Функция для проверки отсутствия проблем
check_no_problems() {
    local test_name="$1"
    local pattern="$2"
    
    echo -e "${YELLOW}Checking: ${test_name} (should NOT be present)${NC}"
    
    if log show --last 5m --style compact --predicate "process == 'Nexy' && eventMessage CONTAINS[c] '${pattern}'" 2>/dev/null | grep -q "${pattern}"; then
        count=$(log show --last 5m --style compact --predicate "process == 'Nexy' && eventMessage CONTAINS[c] '${pattern}'" 2>/dev/null | grep -c "${pattern}" || echo "0")
        if [ "$count" -gt 0 ]; then
            echo -e "${RED}❌ ${test_name}: Found ${count} occurrences (should be 0)${NC}"
            return 1
        else
            echo -e "${GREEN}✅ ${test_name}: Not found${NC}"
            return 0
        fi
    else
        echo -e "${GREEN}✅ ${test_name}: Not found${NC}"
        return 0
    fi
}

echo "=========================================="
echo "1. WARM START TEST"
echo "=========================================="
echo "Please:"
echo "  1. Quit Nexy completely"
echo "  2. Launch Nexy manually"
echo "  3. Wait 5 seconds"
echo "  4. Press Enter to check logs..."
read -r

check_logs "TRAY_SERIES_ID" "TRAY_SERIES_ID" 1
check_logs "TRAY_ATTEMPT1 result=ok" "TRAY_ATTEMPT1 result=ok" 1
check_logs "TAL=hold" "TAL=hold" 1
check_logs "TAL=released" "TAL=released" 1
check_no_problems "Aux cascade" "Aux\["

echo ""
echo "=========================================="
echo "2. COLD START TEST"
echo "=========================================="
echo "Please:"
echo "  1. Reboot macOS"
echo "  2. Launch Nexy (auto-start or manual)"
echo "  3. Wait 60 seconds"
echo "  4. Press Enter to check logs..."
read -r

check_logs "CC_READY" "CC_READY" 1
check_logs "TRAY_ATTEMPT" "TRAY_ATTEMPT" 1
check_logs "TRAY_BACKOFF_NEXT" "TRAY_BACKOFF_NEXT" 0  # Может быть 0 если успешно с первой попытки
check_logs "CIRCUIT_OPEN" "CIRCUIT_OPEN" 0  # Может быть 0 если нет ошибок
check_no_problems "Aux cascade" "Aux\["

echo ""
echo "=========================================="
echo "3. RESTART AFTER TCC TEST"
echo "=========================================="
echo "Please:"
echo "  1. Trigger first-run permissions flow"
echo "  2. Wait for auto-restart"
echo "  3. Wait 30 seconds after restart"
echo "  4. Press Enter to check logs..."
read -r

check_logs "RESTART_FLAG" "RESTART_FLAG" 1
check_logs "atomic write -> rename" "atomic write -> rename" 1
check_logs "atomic read-and-remove" "atomic read-and-remove" 1

echo ""
echo "=========================================="
echo "4. CONTROL CENTER RESTART TEST"
echo "=========================================="
echo "Please:"
echo "  1. Launch Nexy"
echo "  2. Wait for tray icon to appear"
echo "  3. Run: killall ControlCenter"
echo "  4. Wait 10 seconds"
echo "  5. Press Enter to check logs..."
read -r

check_logs "CIRCUIT_OPEN" "CIRCUIT_OPEN" 0  # Может быть 0 если нет 3 подряд ошибок
check_logs "CIRCUIT_CLOSE" "CIRCUIT_CLOSE" 0  # Может быть 0 если circuit не открывался

echo ""
echo "=========================================="
echo "SUMMARY"
echo "=========================================="
echo ""
echo "For detailed analysis, run:"
echo "  python scripts/parse_tray_metrics.py log.md --warm-start"
echo "  python scripts/parse_tray_metrics.py log.md --cold-start"
echo ""
echo "For full logs, check:"
echo "  log show --last 10m --style compact --predicate 'process == \"Nexy\"'"
echo ""

