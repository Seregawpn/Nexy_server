#!/bin/bash
# 🚀 Скрипт для деплоя обновленного промта на Azure
# Использование: ./deploy_prompt_to_azure.sh

set -e

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}ℹ️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_step() { echo -e "${BLUE}🔄 $1${NC}"; }

echo "🚀 =========================================="
echo "🚀    ДЕПЛОЙ ПРОМТА НА AZURE"
echo "🚀 =========================================="
echo ""

# Определяем текущую директорию проекта
CURRENT_DIR="/Users/sergiyzasorin/Development/Nexy/server"
TEMP_DIR="/tmp/nexy_server_temp"
REPO_URL="https://github.com/Seregawpn/Nexy_server.git"

# ШАГ 1: ПОДГОТОВКА
log_step "ШАГ 1: Подготовка..."

# Проверяем, что текущая директория существует
if [ ! -d "$CURRENT_DIR" ]; then
    log_error "Директория проекта не найдена: $CURRENT_DIR"
    exit 1
fi

log_info "Текущая директория проекта: $CURRENT_DIR"

# Очищаем временную директорию
if [ -d "$TEMP_DIR" ]; then
    log_info "Очистка временной директории..."
    rm -rf "$TEMP_DIR"
fi

# ШАГ 2: КЛОНИРОВАНИЕ РЕПОЗИТОРИЯ
log_step "ШАГ 2: Клонирование репозитория Nexy_server..."

cd /tmp
git clone "$REPO_URL" nexy_server_temp
cd nexy_server_temp

if [ $? -ne 0 ]; then
    log_error "Ошибка клонирования репозитория"
    exit 1
fi

log_success "Репозиторий клонирован"

# ШАГ 3: ОЧИСТКА И КОПИРОВАНИЕ
log_step "ШАГ 3: Очистка и копирование файлов..."

# Очищаем все старые файлы (кроме .git)
find . -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +

# Копируем файлы из текущего проекта
log_info "Копирование файлов из $CURRENT_DIR..."
cp -r "$CURRENT_DIR"/* .

# Проверяем, что файл с промтом скопирован
if [ ! -f "server/config/unified_config.py" ]; then
    log_error "Файл unified_config.py не найден после копирования!"
    exit 1
fi

log_success "Файлы скопированы"

# ШАГ 4: НАСТРОЙКА GIT
log_step "ШАГ 4: Настройка Git..."

# Убеждаемся, что remote настроен правильно
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

log_success "Git настроен"

# ШАГ 5: COMMIT И PUSH
log_step "ШАГ 5: Commit и Push..."

# Добавляем все файлы
git add .

# Проверяем статус
CHANGES=$(git status --short)
if [ -z "$CHANGES" ]; then
    log_warning "Нет изменений для коммита. Возможно, все уже задеплоено."
    log_info "Проверяем последний коммит..."
    git log --oneline -1
    exit 0
fi

# Создаем commit
COMMIT_DATE=$(date '+%d.%m.%Y %H:%M')
git commit -m "🚀 Обновление промта для ассистента

- Дата: $COMMIT_DATE
- Изменения: Обновлен system prompt для Gemini Live API
- Модули: text_processing, config
- Детали:
  * Добавлен Search Intent Detection
  * Улучшена обработка WebSearch запросов
  * Обновлены инструкции для Action-Oriented и Descriptive ответов"

if [ $? -ne 0 ]; then
    log_error "Ошибка создания commit"
    exit 1
fi

log_success "Commit создан"

# Push в main ветку
log_info "Отправка изменений в GitHub..."
git push origin main --force

if [ $? -ne 0 ]; then
    log_error "Ошибка отправки в GitHub"
    exit 1
fi

log_success "Изменения отправлены в GitHub"

# ШАГ 6: ОЧИСТКА
log_step "ШАГ 6: Очистка..."

cd /tmp
rm -rf nexy_server_temp

log_success "Временная директория очищена"

# РЕЗУЛЬТАТ
echo ""
echo "🎉 =========================================="
echo "🎉    ДЕПЛОЙ ЗАПУЩЕН УСПЕШНО!"
echo "🎉 =========================================="
echo ""
log_success "📊 Результат:"
echo "   ✅ Изменения отправлены в GitHub"
echo "   ✅ GitHub Actions автоматически задеплоит на Azure"
echo "   ⏱️  Время деплоя: 2-3 минуты"
echo ""
log_info "🔗 Ссылки для мониторинга:"
echo "   📊 GitHub Actions: https://github.com/Seregawpn/Nexy_server/actions"
echo "   🏥 Health Check: https://20.63.24.187/health"
echo "   📋 Status API: https://20.63.24.187/status"
echo ""
log_info "⏳ Следующие шаги:"
echo "   1. Дождитесь завершения GitHub Actions (2-3 минуты)"
echo "   2. Проверьте health endpoint: curl -sk https://20.63.24.187/health"
echo "   3. Проверьте логи сервиса на Azure VM"
echo ""
log_success "✅ Деплой инициирован!"

