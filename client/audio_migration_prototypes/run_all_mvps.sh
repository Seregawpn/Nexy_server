#!/bin/bash
# Скрипт для запуска всех MVP последовательно

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Запуск всех MVP прототипов${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Список MVP в порядке выполнения (все 11 прототипов)
MVPS=(
    "mvp0_observability:test_observability.py:MVP-0: Observability"
    "mvp1_device_discovery:test_device_discovery.py:MVP-1: Device Discovery"
    "mvp1b_device_identity:test_device_identity.py:MVP-1b: Device Identity"
    "mvp2_device_mapping:test_device_mapping.py:MVP-2: Device Mapping"
    "mvp3_storm_reconcile:test_storm_reconcile.py:MVP-3: Storm/Reconcile"
    "mvp4_input_stream_quality:test_input_stream_quality.py:MVP-4: Input Stream Quality"
    "mvp5_input_google_sr:test_input_google_sr_pipeline.py:MVP-5: Input → Google SR"
    "mvp6_output_playback:test_output_playback.py:MVP-6: Output Playback"
    "mvp6b_output_recreate:test_output_recreate_midplay.py:MVP-6b: Output Recreate"
    "mvp7_permissions_gate:test_permissions_gate.py:MVP-7: Permissions Gate"
    "mvp8_end_to_end:test_end_to_end.py:MVP-8: End-to-End"
    "mvp9_live_device_switching:test_live_device_switching.py:MVP-9: Live Device Switching"
    "mvp10_device_switching_google_sr:test_device_switching_google_sr.py:MVP-10: Device Switching → Google SR"
    "mvp11_full_integration:test_full_integration.py:MVP-11: Full Integration (Push-to-Talk + Device Switching + Google SR)"
    "mvp12_full_input_output:test_full_input_output.py:MVP-12: Full Integration (Input + Output)"
)

SUCCESS_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0

for mvp_info in "${MVPS[@]}"; do
    IFS=':' read -r mvp_dir filename mvp_name <<< "$mvp_info"
    filepath="$mvp_dir/$filename"
    
    if [ ! -f "$filepath" ]; then
        echo -e "${YELLOW}⚠️${NC} Файл не найден: $filepath (пропуск)"
        ((SKIPPED_COUNT++))
        continue
    fi
    
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}Запуск: $mvp_name${NC}"
    echo -e "${CYAN}Файл: $filename${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    if python3 "$filepath"; then
        echo ""
        echo -e "${GREEN}✅ $mvp_name - УСПЕХ${NC}"
        ((SUCCESS_COUNT++))
    else
        echo ""
        echo -e "${RED}❌ $mvp_name - ПРОВАЛ${NC}"
        ((FAILED_COUNT++))
        
        # Спрашиваем, продолжать ли
        echo ""
        read -p "Продолжить выполнение остальных MVP? (y/n): " -n 1 -r
        echo ""
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${YELLOW}Выполнение прервано пользователем${NC}"
            break
        fi
    fi
    
    echo ""
done

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}ИТОГИ${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${GREEN}✅ Успешных: $SUCCESS_COUNT${NC}"
echo -e "${RED}❌ Проваленных: $FAILED_COUNT${NC}"
if [ $SKIPPED_COUNT -gt 0 ]; then
    echo -e "${YELLOW}⚠️ Пропущенных: $SKIPPED_COUNT${NC}"
fi
echo ""

if [ $FAILED_COUNT -eq 0 ] && [ $SKIPPED_COUNT -eq 0 ]; then
    echo -e "${GREEN}✅ ВСЕ MVP ПРОЙДЕНЫ${NC}"
    echo -e "${GREEN}Можно приступать к полной реализации${NC}"
    exit 0
elif [ $FAILED_COUNT -eq 0 ]; then
    echo -e "${YELLOW}⚠️ ЕСТЬ ПРОПУЩЕННЫЕ MVP${NC}"
    echo -e "${YELLOW}Проверьте наличие всех файлов${NC}"
    exit 0
else
    echo -e "${RED}❌ ЕСТЬ ПРОВАЛЕННЫЕ MVP${NC}"
    echo -e "${RED}Необходимо исправить проблемы перед полной реализацией${NC}"
    exit 1
fi

