#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

# =============================================================================
# Complete Nexy Cleaner
# Полная очистка всех разрешений и следов Nexy на macOS
# =============================================================================

echo "🧹 Complete Nexy Cleaner"
echo "========================"
echo

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}[INFO]${NC} Начинаем полную очистку..."
echo

# 1. Сброс разрешений TCC
echo -e "${BLUE}[INFO]${NC} 1. Сброс разрешений TCC..."

bundle_ids=("com.nexy.assistant" "Nexy" "nexy" "com.sergiyzasorin.nexy.voiceassistant")
# В TCC сервис Input Monitoring называется ListenEvent
permissions=("Microphone" "ScreenCapture" "Accessibility" "ListenEvent" "Camera")

pretty_permission() {
    case "$1" in
        ListenEvent)
            echo "InputMonitoring (ListenEvent)"
            ;;
        *)
            echo "$1"
            ;;
    esac
}

for bundle_id in "${bundle_ids[@]}"; do
    for permission in "${permissions[@]}"; do
        friendly_name=$(pretty_permission "$permission")
        if tccutil reset "$permission" "$bundle_id" 2>/dev/null; then
            echo -e "${GREEN}[SUCCESS]${NC} $friendly_name для $bundle_id сброшен"
        else
            echo -e "${YELLOW}[INFO]${NC} $friendly_name для $bundle_id не найден или уже очищен"
        fi
    done
done

echo

# 2. Очистка флагов и файлов
echo -e "${BLUE}[INFO]${NC} 2. Очистка флагов и файлов..."

# Флаг первого запуска
if [ -f "$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag" ]; then
    rm -f "$HOME/Library/Application Support/Nexy/permissions_first_run_completed.flag"
    echo -e "${GREEN}[SUCCESS]${NC} Флаг первого запуска удален"
fi

# Application Support
if [ -d "$HOME/Library/Application Support/Nexy" ]; then
    rm -rf "$HOME/Library/Application Support/Nexy"
    echo -e "${GREEN}[SUCCESS]${NC} Application Support очищен"
fi

# Preferences
find "$HOME/Library/Preferences" -type f \( -iname "*nexy*" \) -print0 2>/dev/null | while IFS= read -r -d '' file; do
    rm -f "$file"
    echo -e "${GREEN}[SUCCESS]${NC} Настройка удалена: $file"
done

# Logs
find "$HOME/Library/Logs" \( -iname "*nexy*" \) -print0 2>/dev/null | while IFS= read -r -d '' file; do
    rm -rf "$file"
    echo -e "${GREEN}[SUCCESS]${NC} Лог удален: $file"
done

# Caches
find "$HOME/Library/Caches" \( -iname "*nexy*" \) -print0 2>/dev/null | while IFS= read -r -d '' file; do
    rm -rf "$file"
    echo -e "${GREEN}[SUCCESS]${NC} Кэш удален: $file"
done

# Receipts (пакеты установки)
find "$HOME/Library/Receipts" -type f \( -iname "*nexy*" \) -print0 2>/dev/null | while IFS= read -r -d '' file; do
    rm -f "$file"
    echo -e "${GREEN}[SUCCESS]${NC} Receipt удален: $file"
done

echo

# 3. Очистка launchctl
echo -e "${BLUE}[INFO]${NC} 3. Очистка launchctl сервисов..."

for bundle_id in "${bundle_ids[@]}"; do
    if launchctl list | grep -q "$bundle_id"; then
        launchctl unload "$HOME/Library/LaunchAgents/$bundle_id.plist" 2>/dev/null || true
        echo -e "${GREEN}[SUCCESS]${NC} Сервис остановлен: $bundle_id"
    fi
done

echo

# 4. Очистка Python кэша
echo -e "${BLUE}[INFO]${NC} 4. Очистка Python кэша..."

if [ -d "." ]; then
    find . -name "*.pyc" -delete 2>/dev/null
    find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
    echo -e "${GREEN}[SUCCESS]${NC} Python кэш очищен"
fi

echo

# 5. Очистка временных файлов
echo -e "${BLUE}[INFO]${NC} 5. Очистка временных файлов..."

find "/tmp" \( -iname "*nexy*" \) -print0 2>/dev/null | while IFS= read -r -d '' file; do
    rm -rf "$file"
    echo -e "${GREEN}[SUCCESS]${NC} Временный файл удален: $file"
done

echo

# 6. Финальная проверка
echo -e "${BLUE}[INFO]${NC} 6. Финальная проверка..."

remaining=0

# Проверка разрешений
for permission in "${permissions[@]}"; do
    permission_output="$(tccutil list "$permission" 2>/dev/null || true)"
    count=$(printf "%s\n" "$permission_output" | awk 'BEGIN{IGNORECASE=1}/nexy/{c++} END{print c+0}')
    if [ $count -gt 0 ]; then
        friendly_name=$(pretty_permission "$permission")
        echo -e "${YELLOW}[WARNING]${NC} Найдено $count записей в $friendly_name"
        remaining=1
    fi
done

# Проверка файлов (исключая CloudDocs и проект)
file_count=$(find "$HOME/Library" \( -iname "*nexy*" \) -print 2>/dev/null | awk '!/CloudDocs/ && !/Development/{c++} END{print c+0}')
if [ $file_count -gt 0 ]; then
    echo -e "${YELLOW}[WARNING]${NC} Найдено $file_count оставшихся файлов (исключая CloudDocs и проект)"
    remaining=1
fi

echo
echo "========================"

if [ $remaining -eq 0 ]; then
    echo -e "${GREEN}[SUCCESS]${NC} 🎉 Полная очистка завершена успешно!"
    echo -e "${GREEN}[SUCCESS]${NC} Все разрешения и следы Nexy удалены"
    echo -e "${BLUE}[INFO]${NC} При следующем запуске приложение будет работать как при первом запуске"
else
    echo -e "${YELLOW}[WARNING]${NC} ⚠️ Очистка завершена с предупреждениями"
    echo -e "${BLUE}[INFO]${NC} Проверьте System Settings > Privacy & Security для ручной очистки"
fi

echo
echo -e "${BLUE}[INFO]${NC} Для полной очистки TCC кэша выполните:"
echo -e "${BLUE}[INFO]${NC} sudo rm -rf ~/Library/Application\\ Support/com.apple.TCC/"
echo
echo -e "${BLUE}[INFO]${NC} Для удаления приложения из /Applications выполните:"
echo -e "${BLUE}[INFO]${NC} sudo rm -rf /Applications/Nexy.app"
echo
