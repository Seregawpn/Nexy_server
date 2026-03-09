#!/bin/bash
# Скрипт для активации виртуального окружения
# Использование: source activate.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/.venv"

if [ -d "$VENV_PATH" ]; then
    source "$VENV_PATH/bin/activate"
    echo "✅ Виртуальное окружение активировано: $VENV_PATH"
    echo "Python: $(which python)"
    echo "Версия: $(python --version)"
else
    echo "❌ Виртуальное окружение не найдено: $VENV_PATH"
    return 1
fi
