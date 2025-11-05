# Shadow-Mode Testing Guide

## Цель
Руководство по тестированию shadow-mode диагностического логирования после нормализации Этапа 4.

## Что тестировать

### 1. Shadow-mode диагностические логи

**UpdaterIntegration:**
- При изменении `update_in_progress` должны появляться логи:
  - `[UPDATER] Shadow-mode sync: accessor=... == state_data=... (trigger=...)` - когда значения совпадают (DEBUG)
  - `[UPDATER] Shadow-mode mismatch: accessor=... vs state_data=... (trigger=...)` - когда значения расходятся (WARNING)

**SimpleModuleCoordinator:**
- При установке `restart_pending` должны появляться логи:
  - `[COORDINATOR] Shadow-mode sync: coordinator._restart_pending=... == state_data=... (session=...)` - когда значения совпадают (DEBUG)
  - `[COORDINATOR] Shadow-mode mismatch: coordinator._restart_pending=... vs state_data=... (session=...)` - когда значения расходятся (WARNING)

### 2. Сценарии для проверки

#### Сценарий 1: Обновление приложения
1. Запустить приложение
2. Инициировать проверку обновлений (через updater)
3. Проверить логи на наличие shadow-mode сообщений:
   ```bash
   grep -i "shadow-mode" logs/nexy.log | grep -i updater
   ```

#### Сценарий 2: Перезапуск после first-run
1. Запустить приложение с чистыми разрешениями (первый запуск)
2. Пройти процесс запроса разрешений
3. Проверить логи на наличие shadow-mode сообщений:
   ```bash
   grep -i "shadow-mode" logs/nexy.log | grep -i coordinator
   ```

#### Сценарий 3: Проверка расхождений
1. Вручную изменить `state_data` в ApplicationStateManager
2. Изменить доступ к accessor в интеграции
3. Проверить, что появляется WARNING о mismatch

### 3. Фич-флаги

Проверьте, что фич-флаги включены в `config/unified_config.yaml`:

```yaml
features:
  use_events_for_update_status:
    enabled: true
    rollout_percentage: 1
  use_events_for_restart_pending:
    enabled: true
    rollout_percentage: 1
```

### 4. Ожидаемое поведение

**Нормальное состояние (без расхождений):**
- DEBUG логи появляются периодически при синхронизации
- WARNING логи НЕ должны появляться

**Проблемное состояние (с расхождениями):**
- WARNING логи появляются при каждом расхождении
- Требуется расследование и исправление

### 5. Проверка логов

```bash
# Проверить наличие shadow-mode логов
grep -i "shadow-mode" logs/nexy.log

# Проверить только mismatch (проблемы)
grep -i "shadow-mode mismatch" logs/nexy.log

# Проверить только sync (норма)
grep -i "shadow-mode sync" logs/nexy.log

# Проверить логи по источникам
grep "\[UPDATER\] Shadow-mode" logs/nexy.log
grep "\[COORDINATOR\] Shadow-mode" logs/nexy.log
```

### 6. Метрики для мониторинга

- Количество mismatch логов за период (должно быть 0)
- Частота sync логов (должна соответствовать частоте изменений состояния)
- Время расхождения (если mismatch обнаружен)

## Следующие шаги

1. **Мониторинг (1-2 дня)**: Наблюдать логи на предмет mismatch
2. **При отсутствии проблем**: Увеличить `rollout_percentage` до 25%
3. **После стабильности на 25%**: Увеличить до 100%
4. **После 100% стабильности**: Рассмотреть удаление диагностического логирования (опционально)




