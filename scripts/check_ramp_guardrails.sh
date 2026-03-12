#!/bin/bash
# Проверка гвардрайлов для раскатки трафика (PR-7)

set -euo pipefail

LOG_FILE="${1:-server.log}"
WINDOW_SIZE="${2:-100}"  # Количество последних записей для анализа

echo "📊 Проверка гвардрайлов для раскатки трафика"
echo "============================================"
echo "Лог файл: $LOG_FILE"
echo "Окно анализа: последние $WINDOW_SIZE записей"
echo "============================================"
echo ""

errors=0
warnings=0

# 1. p95 latency
echo "1. Проверка p95 latency..."
if [ -f "$LOG_FILE" ]; then
    p95=$(grep -E 'dur_ms=[0-9]+.*method=StreamAudio' "$LOG_FILE" | tail -"$WINDOW_SIZE" | grep -oE 'dur_ms=([0-9]+)' | cut -d= -f2 | sort -n | awk '{latencies[NR]=$1} END {n=length(latencies); if (n>0) {p95_idx=int(n*0.95); if (p95_idx==0) p95_idx=1; print latencies[p95_idx]} else print "0"}')
    
    if [ -n "$p95" ] && [ "$p95" != "0" ]; then
        if [ "$p95" -le 1000 ]; then
            echo "   ✅ p95 latency: ${p95}ms (≤ 1000ms)"
        else
            echo "   ❌ p95 latency: ${p95}ms (> 1000ms)"
            errors=$((errors + 1))
        fi
    else
        echo "   ⚠️ Недостаточно данных для расчета p95"
        warnings=$((warnings + 1))
    fi
else
    echo "   ⚠️ Лог файл не найден"
    warnings=$((warnings + 1))
fi

# 2. Error rate
echo "2. Проверка error rate..."
if [ -f "$LOG_FILE" ]; then
    total=$(grep -c 'scope=grpc method=StreamAudio' "$LOG_FILE" | tail -"$WINDOW_SIZE" || echo "0")
    errors_count=$(grep -c 'decision=error.*method=StreamAudio' "$LOG_FILE" | tail -"$WINDOW_SIZE" || echo "0")
    
    if [ "$total" -gt 0 ]; then
        error_rate=$(echo "scale=2; $errors_count * 100 / $total" | bc)
        if [ $(echo "$error_rate <= 5" | bc) -eq 1 ]; then
            echo "   ✅ Error rate: ${error_rate}% (≤ 5%)"
        else
            echo "   ❌ Error rate: ${error_rate}% (> 5%)"
            errors=$((errors + 1))
        fi
    else
        echo "   ⚠️ Недостаточно данных для расчета error rate"
        warnings=$((warnings + 1))
    fi
else
    echo "   ⚠️ Лог файл не найден"
    warnings=$((warnings + 1))
fi

# 3. Decision rate всплеск
echo "3. Проверка decision rate всплеска..."
if [ -f "$LOG_FILE" ]; then
    recent_retry_abort=$(grep -c 'decision=(retry|abort)' "$LOG_FILE" | tail -"$WINDOW_SIZE" || echo "0")
    baseline_retry_abort=$(grep -c 'decision=(retry|abort)' "$LOG_FILE" | head -"$WINDOW_SIZE" || echo "0")
    
    if [ "$baseline_retry_abort" -gt 0 ]; then
        threshold=$(echo "$baseline_retry_abort * 3 / 2" | bc)
        if [ "$recent_retry_abort" -le "$threshold" ]; then
            echo "   ✅ Decision rate всплеск: $recent_retry_abort ≤ $threshold (базовая линия ×1.5)"
        else
            echo "   ❌ Decision rate всплеск: $recent_retry_abort > $threshold (базовая линия ×1.5)"
            errors=$((errors + 1))
        fi
    else
        echo "   ⚠️ Недостаточно данных для проверки всплеска"
        warnings=$((warnings + 1))
    fi
else
    echo "   ⚠️ Лог файл не найден"
    warnings=$((warnings + 1))
fi

# 4. Backpressure отказы
echo "4. Проверка backpressure отказов..."
if [ -f "$LOG_FILE" ]; then
    backpressure_rejects=$(grep -c 'RESOURCE_EXHAUSTED.*stream\|stream.*limit.*exceeded' "$LOG_FILE" | tail -"$WINDOW_SIZE" || echo "0")
    total_streams=$(grep -c 'decision=stream_acquired' "$LOG_FILE" | tail -"$WINDOW_SIZE" || echo "0")
    
    if [ "$total_streams" -gt 0 ]; then
        reject_rate=$(echo "scale=2; $backpressure_rejects * 100 / $total_streams" | bc)
        if [ $(echo "$reject_rate <= 1" | bc) -eq 1 ]; then
            echo "   ✅ Backpressure reject rate: ${reject_rate}% (≤ 1%)"
        else
            echo "   ❌ Backpressure reject rate: ${reject_rate}% (> 1%)"
            errors=$((errors + 1))
        fi
    else
        echo "   ⚠️ Недостаточно данных для расчета backpressure reject rate"
        warnings=$((warnings + 1))
    fi
else
    echo "   ⚠️ Лог файл не найден"
    warnings=$((warnings + 1))
fi

echo ""
echo "============================================"
if [ $errors -eq 0 ]; then
    if [ $warnings -eq 0 ]; then
        echo "✅ Все гвардрайлы пройдены!"
        exit 0
    else
        echo "⚠️ Все гвардрайлы пройдены с $warnings предупреждениями"
        exit 0
    fi
else
    echo "❌ $errors гвардрайлов провалены"
    if [ $warnings -gt 0 ]; then
        echo "   и $warnings предупреждений"
    fi
    exit 1
fi

