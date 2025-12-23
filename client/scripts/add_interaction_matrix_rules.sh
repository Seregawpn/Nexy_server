#!/bin/bash
# Добавление правил RouteManager в interaction_matrix.yaml

set -e

MATRIX_FILE="config/interaction_matrix.yaml"

# Проверяем, что файл существует
if [ ! -f "$MATRIX_FILE" ]; then
    echo "❌ Файл $MATRIX_FILE не найден"
    exit 1
fi

# Проверяем, что правила еще не добавлены
if grep -q "AUDIO ROUTE MANAGER RULES" "$MATRIX_FILE"; then
    echo "⚠️ Правила уже добавлены в $MATRIX_FILE"
    exit 0
fi

# Находим место для вставки (перед последней строкой или в конец секции rules)
python3 << 'PYTHON'
import yaml
import sys

matrix_file = "config/interaction_matrix.yaml"

try:
    with open(matrix_file, 'r') as f:
        content = f.read()
    
    # Ищем место после последнего правила (перед концом файла или после последнего правила)
    # Ищем секцию rules и добавляем в конец
    
    rules_to_add = '''  # ============================================================================
  # AUDIO ROUTE MANAGER RULES
  # ============================================================================

  # Hard stop: RouteManager блокируется во время first_run
  - when: {app.first_run: true}
    decision: abort
    priority: hard_stop
    description: First run in progress - block RouteManager reconcile
    gateway: decide_route_manager_reconcile

  # Hard stop: RouteManager блокируется во время permission_restart
  - when: {app.restart_pending: true}
    decision: abort
    priority: hard_stop
    description: Permission restart pending - block RouteManager reconcile
    gateway: decide_route_manager_reconcile

  # Hard stop: RouteManager блокируется во время update
  - when: {app.update_in_progress: true}
    decision: abort
    priority: hard_stop
    description: Update in progress - block RouteManager reconcile
    gateway: decide_route_manager_reconcile

  # Graceful: Device busy - retry with backoff
  - when: {device.busy: true, app.mode: listening}
    decision: retry
    priority: graceful
    description: Device busy - retry input switch with backoff
    gateway: decide_route_manager_reconcile

  # Graceful: Network offline - degrade (can still listen)
  - when: {network.offline: true, app.mode: listening}
    decision: degrade
    priority: graceful
    description: Network offline - degrade but allow listening
    gateway: decide_route_manager_reconcile
'''
    
    # Добавляем перед концом файла (после последнего правила)
    if 'rules:' in content:
        # Ищем конец секции rules (пустая строка после последнего правила или конец файла)
        lines = content.split('\n')
        insert_index = len(lines)
        
        # Ищем последнее правило (строка начинающаяся с "  - when:")
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip().startswith('- when:'):
                # Ищем конец этого правила (пустая строка или следующее правило)
                for j in range(i + 1, len(lines)):
                    if lines[j].strip() == '' or (lines[j].strip().startswith('#') and '===' in lines[j]):
                        insert_index = j
                        break
                    elif lines[j].strip().startswith('- when:'):
                        # Следующее правило - вставляем перед ним
                        insert_index = j
                        break
                break
        
        # Вставляем правила
        lines.insert(insert_index, rules_to_add.rstrip())
        content = '\n'.join(lines)
    
    # Записываем обратно
    with open(matrix_file, 'w') as f:
        f.write(content)
    
    print("✅ Правила добавлены в $MATRIX_FILE")
    
except Exception as e:
    print(f"❌ Ошибка: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
PYTHON

echo "✅ Готово!"

