#!/bin/bash
# Скрипт для очистки Python кэша (__pycache__) для решения проблем с устаревшими версиями модулей

set -e

echo "🧹 Очистка Python кэша..."

# Находим и удаляем все __pycache__ директории
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

# Удаляем .pyc файлы
find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Удаляем .pyo файлы
find . -type f -name "*.pyo" -delete 2>/dev/null || true

# Удаляем .pytest_cache если есть
find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true

# Специфичные пути для grpc_client
echo "🧹 Очистка кэша grpc_client..."
rm -rf client/modules/grpc_client/core/__pycache__ 2>/dev/null || true
rm -rf modules/grpc_client/core/__pycache__ 2>/dev/null || true
rm -rf integration/integrations/__pycache__ 2>/dev/null || true

echo "✅ Python кэш очищен"
echo ""
echo "⚠️  ВАЖНО: Перезапустите приложение для применения изменений"
