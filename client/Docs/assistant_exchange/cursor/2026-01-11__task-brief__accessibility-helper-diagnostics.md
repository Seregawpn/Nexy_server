# Accessibility Helper Diagnostics (task brief)

## Goal
Улучшить диагностику вызова `trigger_accessibility_prompt.py` helper'а для проверки, что prompt реально вызывается и не падает.

## Changes

### 1. Улучшенное логирование в `activate_accessibility()`

**Файл**: `modules/permissions/first_run/activator.py`

**Что добавлено**:
- Явный лог exit code helper'а с интерпретацией:
  - `0` = Разрешение уже есть или диалог показан успешно
  - `1` = Разрешения нет, диалог должен был появиться
  - `2` = Ошибка выполнения
  - `-1` = Timeout
  - `-2` = Exception при запуске
- Логирование stdout/stderr helper'а (первые 100 символов)
- Логирование статуса до/после вызова helper'а
- Краткий статус для log.md через `print()` (для console.app)

**Пример логов**:
```
♿ Accessibility: prompt helper завершён — exit_code=1 (Разрешения нет (trusted=False) — диалог должен был появиться) stdout=(пусто) stderr=(пусто)
♿ [ACTIVATOR] Accessibility prompt helper: exit=1 (Разрешения нет (trusted=False) — диалог должен был появиться)
♿ Accessibility: статус до/после prompt helper — not_determined → not_determined (helper exit=1)
```

### 2. Тестовый скрипт для прямой проверки

**Файл**: `test_accessibility_helper.py`

**Функциональность**:
1. Сброс разрешения через `tccutil` (опционально)
2. Прямой запуск helper'а с выводом exit code
3. Проверка статуса до/после вызова
4. Инструкции по мониторингу tccd логов
5. Итоговый отчёт с рекомендациями

**Использование**:
```bash
python3 test_accessibility_helper.py
```

**Выходные данные**:
- Exit code helper'а с интерпретацией
- Статус до/после вызова
- Рекомендации по диагностике

## Verification (DoD)

### Шаги проверки:

1. **Сброс разрешения** (опционально):
   ```bash
   sudo tccutil reset Accessibility com.nexy.assistant
   ```

2. **Запуск тестового скрипта**:
   ```bash
   python3 test_accessibility_helper.py
   ```

3. **Проверка exit code**:
   - `0` = prompt показан или уже granted
   - `1` = не granted, prompt должен появиться
   - `2` = ошибка

4. **Мониторинг tccd логов** (в отдельном терминале):
   ```bash
   log show --last 2m --predicate 'process == "tccd"' | grep -i accessibility
   ```

5. **Проверка статуса после выдачи**:
   ```python
   from modules.permissions.first_run.status_checker import check_accessibility_status
   print(check_accessibility_status())
   ```

### Expected behavior/logs:

- Появляется системный диалог Accessibility
- В tccd логах нет фатальных ошибок
- Helper возвращает 0/1 без падения
- В логах приложения виден явный exit code и интерпретация

### Regression checks:

- Другие разрешения не затрагиваются
- Нет краша основного процесса
- Логирование не замедляет работу

## Criteria: "стало проще/стабильнее"

✅ **Прямой запуск helper'а** однозначно показывает:
- Есть ли prompt (exit code 0/1)
- Есть ли ошибка в вызове (exit code 2)
- Что произошло (интерпретация exit code)

✅ **Улучшенное логирование** в `activate_accessibility()`:
- Явный exit code helper'а в логах
- Статус до/после вызова
- Краткий статус для log.md

✅ **Тестовый скрипт** для воспроизводимой проверки:
- Автоматизированная диагностика
- Инструкции по мониторингу tccd
- Итоговый отчёт с рекомендациями

## Files Modified

- `modules/permissions/first_run/activator.py` — улучшенное логирование
- `test_accessibility_helper.py` — новый тестовый скрипт

## Rationale

Без прямого запуска helper'а и мониторинга tccd/логов невозможно подтвердить, что prompt вызывается и есть ли ошибка. Теперь:
1. Логирование в `activate_accessibility()` показывает явный exit code и интерпретацию
2. Тестовый скрипт позволяет воспроизводимо проверить работу helper'а
3. Мониторинг tccd логов даёт дополнительную диагностику системного уровня
