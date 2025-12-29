#!/bin/bash
# Скрипт для проверки "битых" ссылок в документации после архивации
# Использование: ./scripts/check_documentation_links.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

echo "🔍 Проверка ссылок в документации..."
echo ""

ERRORS=0

# Функция для проверки существования файла
check_file() {
    local file="$1"
    local context="$2"
    
    # Проверяем разные возможные пути
    if [[ -f "$file" ]]; then
        return 0
    elif [[ -f "$REPO_ROOT/$file" ]]; then
        return 0
    elif [[ -f "$REPO_ROOT/client/$file" ]]; then
        return 0
    elif [[ -f "$REPO_ROOT/server/server/$file" ]]; then
        return 0
    else
        echo "❌ Файл не найден: $file (контекст: $context)"
        ((ERRORS++))
        return 1
    fi
}

# Проверка client/.cursorrules
echo "📄 Проверка client/.cursorrules..."
if [[ -f "client/.cursorrules" ]]; then
    while IFS= read -r line; do
        # Извлекаем ссылки на .md файлы
        if [[ "$line" =~ \`([^\`]+\.md)\` ]]; then
            file="${BASH_REMATCH[1]}"
            # Пропускаем ссылки на архивные документы (они уже в архиве)
            if [[ "$file" != *"_archive"* ]] && [[ "$file" != *"NEXY_FIRST_RUN_LOG_EXPECTED"* ]] && [[ "$file" != *"PERMISSION_RESTART_BLOCKERS"* ]] && [[ "$file" != *"RELEASE_INTEGRITY_PLAN"* ]]; then
                # Нормализуем путь
                if [[ "$file" == Docs/* ]]; then
                    check_file "client/$file" "client/.cursorrules"
                elif [[ "$file" == client/Docs/* ]]; then
                    check_file "$file" "client/.cursorrules"
                fi
            fi
        fi
    done < <(grep -E '`[^`]+\.md`' client/.cursorrules || true)
else
    echo "⚠️  Файл client/.cursorrules не найден"
fi

# Проверка server/server/.cursorrules
echo ""
echo "📄 Проверка server/server/.cursorrules..."
if [[ -f "server/server/.cursorrules" ]]; then
    while IFS= read -r line; do
        if [[ "$line" =~ \`([^\`]+\.md)\` ]]; then
            file="${BASH_REMATCH[1]}"
            if [[ "$file" != *"_archive"* ]] && [[ "$file" != *"STREAMING_WORKFLOW_FIX_IMPLEMENTATION"* ]]; then
                if [[ "$file" == Docs/* ]]; then
                    check_file "server/server/$file" "server/server/.cursorrules"
                elif [[ "$file" == server/Docs/* ]]; then
                    check_file "$file" "server/server/.cursorrules"
                fi
            fi
        fi
    done < <(grep -E '`[^`]+\.md`' server/server/.cursorrules || true)
else
    echo "⚠️  Файл server/server/.cursorrules не найден"
fi

# Проверка client/Docs/DOCUMENTATION_MAP.md
echo ""
echo "📄 Проверка client/Docs/DOCUMENTATION_MAP.md..."
if [[ -f "client/Docs/DOCUMENTATION_MAP.md" ]]; then
    while IFS= read -r line; do
        if [[ "$line" =~ \`([^\`]+\.md)\` ]]; then
            file="${BASH_REMATCH[1]}"
            # Пропускаем архивные документы и комментарии
            if [[ "$line" != *"<!--"* ]] && [[ "$file" != *"_archive"* ]]; then
                if [[ "$file" == Docs/* ]]; then
                    check_file "client/$file" "client/Docs/DOCUMENTATION_MAP.md"
                elif [[ "$file" == client/Docs/* ]]; then
                    check_file "$file" "client/Docs/DOCUMENTATION_MAP.md"
                fi
            fi
        fi
    done < <(grep -E '`[^`]+\.md`' client/Docs/DOCUMENTATION_MAP.md || true)
else
    echo "⚠️  Файл client/Docs/DOCUMENTATION_MAP.md не найден"
fi

# Проверка server/server/Docs/ARCHITECTURE_OVERVIEW.md
echo ""
echo "📄 Проверка server/server/Docs/ARCHITECTURE_OVERVIEW.md..."
if [[ -f "server/server/Docs/ARCHITECTURE_OVERVIEW.md" ]]; then
    while IFS= read -r line; do
        if [[ "$line" =~ \`([^\`]+\.md)\` ]]; then
            file="${BASH_REMATCH[1]}"
            if [[ "$file" != *"_archive"* ]]; then
                if [[ "$file" == Docs/* ]]; then
                    check_file "server/server/$file" "server/server/Docs/ARCHITECTURE_OVERVIEW.md"
                elif [[ "$file" == server/Docs/* ]]; then
                    check_file "$file" "server/server/Docs/ARCHITECTURE_OVERVIEW.md"
                fi
            fi
        fi
    done < <(grep -E '`[^`]+\.md`' server/server/Docs/ARCHITECTURE_OVERVIEW.md || true)
else
    echo "⚠️  Файл server/server/Docs/ARCHITECTURE_OVERVIEW.md не найден"
fi

# Проверка на ссылки на архивные документы в активных файлах
echo ""
echo "🔍 Проверка ссылок на архивные документы в активных файлах..."
ARCHIVE_REFS=0

# Проверяем client/.cursorrules
if grep -q "NEXY_FIRST_RUN_LOG_EXPECTED\|PERMISSION_RESTART_BLOCKERS\|RELEASE_INTEGRITY_PLAN\.md" client/.cursorrules 2>/dev/null; then
    echo "⚠️  Найдены ссылки на архивные документы в client/.cursorrules"
    grep -n "NEXY_FIRST_RUN_LOG_EXPECTED\|PERMISSION_RESTART_BLOCKERS\|RELEASE_INTEGRITY_PLAN\.md" client/.cursorrules || true
    ((ARCHIVE_REFS++))
fi

# Проверяем server/server/.cursorrules
if grep -q "STREAMING_WORKFLOW_FIX_IMPLEMENTATION" server/server/.cursorrules 2>/dev/null; then
    echo "⚠️  Найдены ссылки на архивные документы в server/server/.cursorrules"
    grep -n "STREAMING_WORKFLOW_FIX_IMPLEMENTATION" server/server/.cursorrules || true
    ((ARCHIVE_REFS++))
fi

# Итоги
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [[ $ERRORS -eq 0 ]] && [[ $ARCHIVE_REFS -eq 0 ]]; then
    echo "✅ Все проверки пройдены успешно!"
    exit 0
else
    echo "❌ Найдены проблемы:"
    [[ $ERRORS -gt 0 ]] && echo "   - Битые ссылки: $ERRORS"
    [[ $ARCHIVE_REFS -gt 0 ]] && echo "   - Ссылки на архивные документы: $ARCHIVE_REFS"
    echo ""
    echo "📖 См. инструкцию: Docs/DOCUMENTATION_POST_ARCHIVE_UPDATE_INSTRUCTIONS.md"
    exit 1
fi
