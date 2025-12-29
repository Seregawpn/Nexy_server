#!/bin/bash
# Скрипт очистки артефактов перед merge PR #1 (close_app)

set -e

echo "🧹 Очистка артефактов для close_app PR..."
echo ""

# Переходим в корень проекта
cd "$(dirname "$0")/.."

# Проверяем наличие файлов перед удалением
ARTIFACTS_FOUND=0

# 1. Удалить edge_tts_output директорию
if [ -d "server/server/scripts/edge_tts_output" ]; then
    echo "❌ Найдена директория: server/server/scripts/edge_tts_output/"
    echo "   Удаление..."
    rm -rf server/server/scripts/edge_tts_output/
    echo "   ✅ Удалена"
    ARTIFACTS_FOUND=1
fi

# 2. Удалить тестовые mp3 файлы
for file in \
    "server/server/scripts/test_edge_tts_streaming.mp3" \
    "server/server/scripts/test_edge_tts_output.mp3"
do
    if [ -f "$file" ]; then
        echo "❌ Найден файл: $file"
        echo "   Удаление..."
        rm -f "$file"
        echo "   ✅ Удален"
        ARTIFACTS_FOUND=1
    fi
done

# 3. Удалить JSON отчеты
for file in \
    "server/server/scripts/edge_tts_check_report.json"
do
    if [ -f "$file" ]; then
        echo "❌ Найден файл: $file"
        echo "   Удаление..."
        rm -f "$file"
        echo "   ✅ Удален"
        ARTIFACTS_FOUND=1
    fi
done

# 4. Проверка MD отчетов (опционально - можно оставить для документации)
# Если нужно удалить:
# rm -f server/server/scripts/edge_tts_test_report.md

if [ $ARTIFACTS_FOUND -eq 0 ]; then
    echo "✅ Артефакты не найдены (возможно, уже удалены или в .gitignore)"
else
    echo ""
    echo "✅ Очистка завершена. Удалено артефактов: $ARTIFACTS_FOUND"
fi

echo ""
echo "📋 Проверка оставшихся артефактов:"
echo ""

# Проверяем, остались ли артефакты
REMAINING=$(find server/server/scripts -name "*.mp3" -o -name "*edge_tts*.json" 2>/dev/null | grep -v ".git" || true)

if [ -z "$REMAINING" ]; then
    echo "✅ Артефакты не найдены"
else
    echo "⚠️  Найдены оставшиеся артефакты:"
    echo "$REMAINING"
    echo ""
    echo "💡 Проверьте, нужно ли их удалить"
fi

echo ""
echo "✅ Готово к merge PR #1 (close_app)"
