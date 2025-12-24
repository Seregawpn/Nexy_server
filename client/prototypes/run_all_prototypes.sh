#!/bin/bash
# Скрипт для запуска всех прототипов последовательно

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Запуск всех прототипов${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

PROTOTYPES=(
    "test_device_discovery.py:Прототип 1: Поиск устройств"
    "test_device_mapping.py:Прототип 2: Маппинг устройств"
    "test_input_connection.py:Прототип 3: Подключение Input"
    "test_output_playback.py:Прототип 4: Воспроизведение Output"
)

SUCCESS_COUNT=0
FAILED_COUNT=0

for prototype_info in "${PROTOTYPES[@]}"; do
    IFS=':' read -r filename description <<< "$prototype_info"
    filepath="prototypes/$filename"
    
    if [ ! -f "$filepath" ]; then
        echo -e "${YELLOW}⚠️${NC} Файл не найден: $filepath (пропуск)"
        continue
    fi
    
    echo -e "${BLUE}Запуск: $description${NC}"
    echo -e "${BLUE}Файл: $filename${NC}"
    echo ""
    
    if python3 "$filepath"; then
        echo -e "${GREEN}✅ $description - УСПЕХ${NC}"
        ((SUCCESS_COUNT++))
    else
        echo -e "${RED}❌ $description - ПРОВАЛ${NC}"
        ((FAILED_COUNT++))
    fi
    
    echo ""
    echo -e "${BLUE}----------------------------------------${NC}"
    echo ""
done

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}ИТОГИ${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "${GREEN}✅ Успешных: $SUCCESS_COUNT${NC}"
echo -e "${RED}❌ Проваленных: $FAILED_COUNT${NC}"
echo ""

if [ $FAILED_COUNT -eq 0 ]; then
    echo -e "${GREEN}✅ ВСЕ ПРОТОТИПЫ ПРОЙДЕНЫ${NC}"
    echo -e "${GREEN}Можно приступать к полной реализации${NC}"
    exit 0
else
    echo -e "${RED}❌ ЕСТЬ ПРОВАЛЕННЫЕ ПРОТОТИПЫ${NC}"
    echo -e "${RED}Необходимо исправить проблемы перед полной реализацией${NC}"
    exit 1
fi

