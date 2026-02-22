#!/bin/bash
# Скрипт проверки Beta Gate Checklist (PR-7)

set -euo pipefail

# Цвета для вывода
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Параметры
HOST="${1:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"
PORT="${2:-443}"

echo "🔍 Beta Gate Checklist Check"
echo "============================"
echo "Host: $HOST"
echo "Port: $PORT"
echo "============================"
echo ""

errors=0
warnings=0

# 1. CI Checks - Smoke Test
echo "1. Checking smoke test..."
if python scripts/grpc_smoke.py "$HOST" "$PORT" > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓${NC} Smoke test passed"
else
    echo -e "   ${RED}✗${NC} Smoke test failed"
    errors=$((errors + 1))
fi

# 2. Structured Logging
echo "2. Checking structured logging..."
if [ -f "server.log" ] && grep -q "decision=" server.log 2>/dev/null; then
    echo -e "   ${GREEN}✓${NC} Structured logging found"
else
    echo -e "   ${YELLOW}⚠${NC} Structured logging not found (may be normal if server just started)"
    warnings=$((warnings + 1))
fi

# 3. Contract Tests
echo "3. Checking contract tests..."
if python scripts/grpc_contract_tests.py "$HOST" "$PORT" > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓${NC} Contract tests passed"
else
    echo -e "   ${RED}✗${NC} Contract tests failed"
    errors=$((errors + 1))
fi

# 4. Feature Flag
echo "4. Checking feature flag..."
if python -c "from config.unified_config import get_config; c = get_config(); assert hasattr(c, 'features')" 2>/dev/null; then
    echo -e "   ${GREEN}✓${NC} Feature flags available"
else
    echo -e "   ${RED}✗${NC} Feature flags not available"
    errors=$((errors + 1))
fi

# 5. Update Invariants
echo "5. Checking update invariants..."
if bash scripts/validate_updates.sh "$HOST" "$PORT" > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓${NC} Update invariants passed"
else
    echo -e "   ${RED}✗${NC} Update invariants failed"
    errors=$((errors + 1))
fi

# 6. Health/Status Check
echo "6. Checking health/status..."
if python scripts/check_grpc_health.py "$HOST" "$PORT" > /dev/null 2>&1; then
    echo -e "   ${GREEN}✓${NC} Health/status check passed"
else
    echo -e "   ${YELLOW}⚠${NC} Health/status check failed (server may be down)"
    warnings=$((warnings + 1))
fi

echo ""
echo "============================"
if [ $errors -eq 0 ]; then
    if [ $warnings -eq 0 ]; then
        echo -e "${GREEN}✅ All checks passed!${NC}"
        exit 0
    else
        echo -e "${YELLOW}⚠️ All checks passed with $warnings warnings${NC}"
        exit 0
    fi
else
    echo -e "${RED}❌ $errors checks failed${NC}"
    if [ $warnings -gt 0 ]; then
        echo -e "${YELLOW}   and $warnings warnings${NC}"
    fi
    exit 1
fi

