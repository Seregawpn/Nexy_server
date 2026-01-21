#!/bin/bash
#
# Скрипт для настройки cron задач для периодических задач платежной системы
#
# Использование:
#   ./cron_setup.sh install    - Установить cron задачи
#   ./cron_setup.sh remove     - Удалить cron задачи
#   ./cron_setup.sh show       - Показать текущие cron задачи
#
# Feature ID: F-2025-017-stripe-payment
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/venv"
PYTHON_SCRIPT="$SCRIPT_DIR/run_periodic_tasks.py"

# Проверка существования скрипта
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "❌ Error: $PYTHON_SCRIPT not found"
    exit 1
fi

# Проверка существования venv
if [ ! -d "$VENV_PATH" ]; then
    echo "❌ Error: Virtual environment not found at $VENV_PATH"
    exit 1
fi

# Функция для создания cron команды
create_cron_command() {
    local task_name=$1
    local schedule=$2
    local command="cd $SCRIPT_DIR && source $VENV_PATH/bin/activate && python $PYTHON_SCRIPT $task_name >> $SCRIPT_DIR/logs/${task_name}.log 2>&1"
    echo "$schedule $command"
}

# Функция для установки cron задач
install_cron() {
    echo "📋 Установка cron задач..."
    
    # Создаем директорию для логов
    mkdir -p "$SCRIPT_DIR/logs"
    
    # Получаем текущие cron задачи
    crontab -l > /tmp/cron_backup_$$ 2>/dev/null || true
    
    # Удаляем старые задачи (если есть)
    grep -v "run_periodic_tasks.py" /tmp/cron_backup_$$ > /tmp/cron_new_$$ || true
    
    # Добавляем новые задачи
    {
        cat /tmp/cron_new_$$
        echo ""
        echo "# Payment System Periodic Tasks (F-2025-017-stripe-payment)"
        echo "# Trial Handler - каждые 6 часов"
        create_cron_command "trial_handler" "0 */6 * * *"
        echo "# Grace Period Handler - каждые 6 часов"
        create_cron_command "grace_period_handler" "0 */6 * * *"
        echo "# Sync Service - каждый час"
        create_cron_command "sync_service" "0 * * * *"
        echo "# Quota Reset - ежедневно в 00:00 UTC (автоматически определяет weekly/monthly)"
        create_cron_command "quota_reset" "0 0 * * *"
        echo "# Monitoring - каждые 15 минут"
        create_cron_command "monitoring" "*/15 * * * *"
    } | crontab -
    
    rm -f /tmp/cron_backup_$$ /tmp/cron_new_$$
    
    echo "✅ Cron задачи установлены"
    echo ""
    echo "Расписание:"
    echo "  - Trial Handler: каждые 6 часов (0:00, 6:00, 12:00, 18:00)"
    echo "  - Grace Period Handler: каждые 6 часов (0:00, 6:00, 12:00, 18:00)"
    echo "  - Sync Service: каждый час"
    echo "  - Quota Reset: ежедневно в 00:00 UTC (автоматически weekly/monthly)"
    echo "  - Monitoring: каждые 15 минут"
    echo ""
    echo "Логи сохраняются в: $SCRIPT_DIR/logs/"
}

# Функция для удаления cron задач
remove_cron() {
    echo "🗑️  Удаление cron задач..."
    
    # Получаем текущие cron задачи
    crontab -l > /tmp/cron_backup_$$ 2>/dev/null || true
    
    # Удаляем задачи, связанные с run_periodic_tasks.py
    grep -v "run_periodic_tasks.py" /tmp/cron_backup_$$ | grep -v "Payment System Periodic Tasks" | crontab -
    
    rm -f /tmp/cron_backup_$$
    
    echo "✅ Cron задачи удалены"
}

# Функция для показа текущих cron задач
show_cron() {
    echo "📋 Текущие cron задачи для платежной системы:"
    echo ""
    crontab -l 2>/dev/null | grep -A 3 "run_periodic_tasks.py" || echo "  Нет установленных задач"
}

# Основная логика
case "$1" in
    install)
        install_cron
        ;;
    remove)
        remove_cron
        ;;
    show)
        show_cron
        ;;
    *)
        echo "Использование: $0 {install|remove|show}"
        echo ""
        echo "Команды:"
        echo "  install - Установить cron задачи"
        echo "  remove  - Удалить cron задачи"
        echo "  show    - Показать текущие cron задачи"
        exit 1
        ;;
esac

exit 0
