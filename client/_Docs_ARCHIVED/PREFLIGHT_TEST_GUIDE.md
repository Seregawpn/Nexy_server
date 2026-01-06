# Preflight-тест First-Run Permissions Flow

## Цель
Подтвердить, что текущий flow (запрос → проверка → рестарт) работает корректно **без изменений кода** и не зависает.

## Подготовка

### 1. Запустите скрипт подготовки

```bash
./scripts/preflight_first_run_test.sh
```

Скрипт выполнит:
- Сброс TCC разрешений для `com.nexy.assistant`
- Очистку флагов first-run
- Выведет инструкции для теста

### 2. Альтернативная подготовка (вручную)

```bash
# Сброс TCC разрешений
sudo tccutil reset Microphone com.nexy.assistant
sudo tccutil reset Accessibility com.nexy.assistant
sudo tccutil reset ScreenCapture com.nexy.assistant
sudo tccutil reset ListenEvent com.nexy.assistant

# Очистка флагов
rm ~/Library/Application\ Support/Nexy/permissions_first_run_completed.flag
rm ~/Library/Application\ Support/Nexy/restart_completed.flag
```

## Выполнение теста

### 1. Запуск приложения

```bash
python3 main.py
```

### 2. Мониторинг логов

**Вариант A: Console.app (рекомендуется)**
- Откройте Console.app (Applications → Utilities)
- В поиске введите: `Nexy` или `com.nexy.assistant`
- Или фильтр по процессу: `nexy`

**Вариант B: Файл логов**
- Логи сохраняются в `log.md`
- Для проверки событий: `./scripts/check_first_run_events.sh log.md`

### 3. Ожидаемая последовательность событий

#### 3.1 Начало flow

```
permissions.first_run_started
  - session_id: <uuid>
  - source: permissions_integration
```

#### 3.2 Проверка статусов (до запроса)

```
permissions.status_checked
  - permission: microphone
  - status: not_determined
  - source: permissions.pre_activation
```

Повторяется для каждого разрешения:
- `microphone`
- `accessibility`
- `input_monitoring`
- `screen_capture`

#### 3.3 Запрос разрешений

Для каждого разрешения:

1. **Активация** (показ системного диалога)
2. **Проверка после активации**:
   ```
   permissions.status_checked
     - permission: <type>
     - status: <status>
     - source: permissions.post_activation
   ```

3. **Если не GRANTED** → открытие System Settings и ожидание:
   ```
   permissions.status_checked
     - permission: <type>
     - status: <status>
     - source: permissions.waiting_after_settings
   ```
   (публикуется каждые 10 секунд во время ожидания)

4. **При изменении статуса**:
   ```
   permissions.changed
     - permission: <type>
     - old_status: not_determined
     - new_status: granted
   ```

#### 3.4 Перезапуск (после критических разрешений)

После выдачи критических разрешений (Accessibility, Input Monitoring, Screen Capture):

```
permissions.first_run_restart_pending
  - session_id: <uuid>
  - source: permissions_integration
  - reason: "Critical permissions granted"
```

```
permission_restart.scheduled
  - session_id: <uuid>
  - reason: "Critical permissions granted"
  - delay_sec: 5.0
  - critical_permissions: ["accessibility", "input_monitoring", "screen_capture"]
```

```
Перезапуск приложения запрошен
  (лог из SimpleModuleCoordinator)
```

#### 3.5 Завершение flow (после рестарта)

```
permissions.first_run_completed
  - session_id: <uuid>
  - source: permissions_integration
  - all_granted: true
  - restart_needed: false
```

### 4. Порядок выдачи разрешений

1. **Microphone**
   - Системный диалог → "Allow"
   - Не требует перезапуска

2. **Accessibility**
   - Системный диалог → "Open System Settings"
   - В System Settings включите переключатель для Nexy
   - Требует перезапуска

3. **Input Monitoring**
   - Системный диалог → "Open System Settings"
   - В System Settings включите переключатель для Nexy
   - Требует перезапуска

4. **Screen Capture**
   - Системный диалог → "Open System Settings"
   - В System Settings включите переключатель для Nexy
   - Требует перезапуска

## Критерии успеха (DoD)

### ✅ Все события опубликованы

- [ ] `permissions.first_run_started`
- [ ] `permissions.status_checked` (для каждого разрешения, до запроса)
- [ ] `permissions.status_checked` (после активации)
- [ ] `permissions.status_checked` (во время ожидания, если требуется)
- [ ] `permissions.changed` (при изменении статуса)
- [ ] `permissions.first_run_restart_pending` (после критических разрешений)
- [ ] `permission_restart.scheduled`
- [ ] `permissions.first_run_completed` (после рестарта)

### ✅ Нет зависаний

- [ ] Приложение не застревает в ожидании разрешений
- [ ] Перезапуск выполняется корректно (не более 15 секунд после выдачи критических разрешений)
- [ ] Нет бесконечных циклов в логах

### ✅ Повторный запуск не запрашивает права

- [ ] Флаг `permissions_first_run_completed.flag` создан
- [ ] При следующем запуске flow пропускается
- [ ] Событие `permissions.first_run_completed` публикуется сразу

## Проверка результатов

### 1. Проверка событий в логах

```bash
./scripts/check_first_run_events.sh log.md
```

### 2. Проверка флагов

```bash
ls -la ~/Library/Application\ Support/Nexy/*.flag
```

Ожидаемые флаги:
- `permissions_first_run_completed.flag` (после завершения flow)
- `restart_completed.flag` (после рестарта)

### 3. Проверка статуса разрешений

```bash
python3 scripts/permissions_probe.py
```

После выдачи прав все методы должны показывать `GRANTED`.

## Известные проблемы

### Расхождения между status_checker и tccutil

- **Причина**: `status_checker` проверяет текущий процесс (Python), `tccutil` проверяет TCC для `com.nexy.assistant`
- **Решение**: После выдачи прав для `com.nexy.assistant` результаты должны совпадать

### Бесконечное ожидание

- **Причина**: Разрешение не выдано, но статус не обновляется
- **Решение**: Проверить, что разрешение действительно выдано в System Settings для `com.nexy.assistant`

## После теста

1. Зафиксируйте результаты в `baseline_after.txt` (если использовали `permissions_probe.py`)
2. Сохраните логи для анализа
3. Если тест успешен — можно внедрять изменения в код
4. Если есть проблемы — зафиксируйте их для анализа
