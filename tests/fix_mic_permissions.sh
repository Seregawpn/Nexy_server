#!/bin/bash

# Скрипт для диагностики и исправления разрешений микрофона на macOS
# Использование: bash tests/fix_mic_permissions.sh

echo "================================================================================"
echo "                    ДИАГНОСТИКА МИКРОФОНА macOS                                 "
echo "================================================================================"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Проверка системных настроек
echo ""
echo "1. Проверка системных настроек звука..."
echo "--------------------------------------------------------------------------------"

if system_profiler SPAudioDataType | grep -A 5 "MacBook Air Microphone" > /dev/null; then
    echo -e "${GREEN}✅ MacBook Air Microphone обнаружен${NC}"
    system_profiler SPAudioDataType | grep -A 5 "MacBook Air Microphone"
else
    echo -e "${RED}❌ MacBook Air Microphone не найден${NC}"
fi

# 2. Проверка Python
echo ""
echo "2. Проверка установок Python..."
echo "--------------------------------------------------------------------------------"

echo "Homebrew Python:"
HOMEBREW_PYTHON="/opt/homebrew/bin/python3"
if [ -f "$HOMEBREW_PYTHON" ]; then
    REAL_PYTHON=$(readlink -f "$HOMEBREW_PYTHON" 2>/dev/null || \
                  python3 -c "import os; print(os.path.realpath('$HOMEBREW_PYTHON'))")
    echo "  Путь: $HOMEBREW_PYTHON"
    echo "  Реальный: $REAL_PYTHON"
    echo -e "${GREEN}✅ Найден${NC}"
else
    echo -e "${RED}❌ Не найден${NC}"
fi

echo ""
echo "Системный Python:"
SYSTEM_PYTHON="/usr/bin/python3"
if [ -f "$SYSTEM_PYTHON" ]; then
    echo "  Путь: $SYSTEM_PYTHON"
    "$SYSTEM_PYTHON" --version
    echo -e "${GREEN}✅ Найден${NC}"
else
    echo -e "${RED}❌ Не найден${NC}"
fi

# 3. Проверка PyAudio
echo ""
echo "3. Проверка PyAudio..."
echo "--------------------------------------------------------------------------------"

if python3 -c "import pyaudio" 2>/dev/null; then
    echo -e "${GREEN}✅ PyAudio установлен для Homebrew Python${NC}"
    python3 -c "import pyaudio; p = pyaudio.PyAudio(); print(f'Версия: {p.get_version_text()}'); p.terminate()"
else
    echo -e "${RED}❌ PyAudio НЕ установлен для Homebrew Python${NC}"
    echo "  Установите: pip3 install pyaudio"
fi

if "$SYSTEM_PYTHON" -c "import pyaudio" 2>/dev/null; then
    echo -e "${GREEN}✅ PyAudio установлен для системного Python${NC}"
else
    echo -e "${YELLOW}⚠️  PyAudio НЕ установлен для системного Python${NC}"
    echo "  Установите: $SYSTEM_PYTHON -m pip install --user pyaudio"
fi

# 4. Инструкции по разрешениям
echo ""
echo "4. Инструкции по настройке разрешений..."
echo "--------------------------------------------------------------------------------"

echo ""
echo -e "${YELLOW}🔧 ДЛЯ ИСПРАВЛЕНИЯ ПРОБЛЕМЫ:${NC}"
echo ""
echo "Вариант 1: Через System Preferences (GUI)"
echo "  1. Откройте System Preferences"
echo "  2. Security & Privacy > Privacy > Microphone"
echo "  3. Нажмите замок внизу (введите пароль)"
echo "  4. Добавьте одно из приложений:"
echo "     - Terminal.app (если запускаете из Terminal)"
echo "     - Visual Studio Code (если запускаете из VSCode)"
echo "  5. Поставьте галочку"
echo "  6. Перезапустите приложение"
echo ""
echo "Вариант 2: Добавить Python напрямую"
echo "  1. В System Preferences > Security & Privacy > Microphone"
echo "  2. Нажмите '+' и добавьте:"
echo "     $REAL_PYTHON"
echo "  3. Перезапустите Terminal/VSCode"
echo ""
echo "Вариант 3: Использовать GUI приложение"
echo "  Запустите: python3 tests/mic_permission_app.py"
echo "  GUI приложения имеют больше прав для запроса разрешений"
echo ""

# 5. Быстрый тест
echo ""
echo "5. Быстрый тест микрофона..."
echo "--------------------------------------------------------------------------------"

read -p "Запустить тест микрофона? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Запуск теста..."
    python3 tests/test_mic_permission.py
else
    echo "Тест пропущен"
fi

echo ""
echo "================================================================================"
echo "                              РЕКОМЕНДАЦИИ                                      "
echo "================================================================================"
echo ""
echo -e "${GREEN}✅ Лучший способ: Запустите GUI приложение${NC}"
echo "   python3 tests/mic_permission_app.py"
echo ""
echo -e "${YELLOW}⚠️  Альтернатива: Добавьте Terminal в разрешения микрофона${NC}"
echo "   System Preferences > Security & Privacy > Microphone > Terminal"
echo ""
echo -e "${YELLOW}⚠️  После изменений: ПЕРЕЗАПУСТИТЕ Terminal/VSCode${NC}"
echo ""
echo "================================================================================"
