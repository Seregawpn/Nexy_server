#!/bin/bash
# JQ-выражения для мониторинга логов (PR-7)
# Готовые one-liner'ы для извлечения метрик из структурированных логов

# Формат логов: ts=... level=INFO scope=grpc method=StreamAudio decision=<...> ctx={...} dur_ms=123

LOG_FILE="${1:-server.log}"

echo "📊 JQ-выражения для мониторинга логов"
echo "======================================"
echo ""

# 1. Частота кодов ошибок по методу
echo "1. Частота кодов ошибок по методу:"
echo "   jq -r 'select(.scope == \"grpc\" and .decision == \"error\") | \"\\(.method) \\(.ctx.error_code // \"unknown\")\"' $LOG_FILE | sort | uniq -c | sort -rn"
echo ""

# 2. Распределение decision_rate
echo "2. Распределение decision_rate:"
echo "   grep -oE 'decision=[a-z]+' $LOG_FILE | cut -d= -f2 | sort | uniq -c | sort -rn"
echo ""

# 3. p95 latency по методу (окно 5 минут)
echo "3. p95 latency по методу (последние 5 минут):"
echo "   grep -E 'dur_ms=[0-9]+' $LOG_FILE | tail -100 | grep -oE 'method=([^ ]+) dur_ms=([0-9]+)' | awk -F'=' '{print \$2, \$4}' | sort -k2 -n | awk '{latencies[\$1][NR]=\$2} END {for (m in latencies) {n=length(latencies[m]); p95_idx=int(n*0.95); print m, latencies[m][p95_idx]}}'"
echo ""

# 4. Error rate по методу (за последний час)
echo "4. Error rate по методу (за последний час):"
echo "   grep -E 'scope=grpc method=' $LOG_FILE | tail -1000 | awk '{total[\$0]++} END {for (m in total) {if (m ~ /decision=error/) errors[m]++; else requests[m]++}} END {for (m in requests) print m, (errors[m] || 0) / requests[m] * 100}'"
echo ""

# 5. Топ ошибок по частоте
echo "5. Топ ошибок по частоте:"
echo "   grep -oE 'error_code=[A-Z_]+' $LOG_FILE | cut -d= -f2 | sort | uniq -c | sort -rn | head -10"
echo ""

# 6. Активные стримы (backpressure)
echo "6. Активные стримы (backpressure):"
echo "   grep -E 'decision=stream_acquired|decision=stream_released' $LOG_FILE | tail -100 | grep -oE 'active_streams=[0-9]+' | cut -d= -f2 | sort -n | tail -1"
echo ""

# 7. Transient vs Permanent ошибки
echo "7. Transient vs Permanent ошибки:"
echo "   grep -oE 'error_classified=(transient|permanent)' $LOG_FILE | cut -d= -f2 | sort | uniq -c"
echo ""

# 8. Метрики-агрегаты (последние)
echo "8. Метрики-агрегаты (последние):"
echo "   grep -E 'p95_latency|error_rate|decision_rate' $LOG_FILE | tail -5"
echo ""

# 9. Graceful shutdown события
echo "9. Graceful shutdown события:"
echo "   grep -E 'decision=shutdown|decision=stop' $LOG_FILE | tail -10"
echo ""

# 10. Rate limit срабатывания
echo "10. Rate limit срабатывания:"
echo "    grep -E 'rate.*limit|RESOURCE_EXHAUSTED' $LOG_FILE | wc -l"
echo ""

echo "======================================"
echo "💡 Подсказки:"
echo "   - Используйте tail -N для последних N строк"
echo "   - Используйте grep -E для фильтрации по времени"
echo "   - Для JSON парсинга используйте jq (если логи в JSON формате)"
echo ""

