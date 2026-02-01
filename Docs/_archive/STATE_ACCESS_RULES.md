# Правила доступа к состоянию через selectors/gateways

**Дата создания:** 2026-01-11  
**Статус:** ✅ Активно  
**Версия:** 1.0

## Цель

Закрепить централизованную модель чтения состояния через selectors и принятия решений через gateways, предотвратить регрессии и повторный прямой доступ к `state_manager`.

## Архитектурные правила (REQ-003/004)

### 1. Чтение состояния ТОЛЬКО через selectors

**Правило:** Все чтения состояния из `ApplicationStateManager` должны идти через selectors из `integration/core/selectors.py`.

**Запрещено:**
```python
# ❌ НЕПРАВИЛЬНО: Прямой доступ к state_manager
current_mode = self.state_manager.get_current_mode()
session_id = self.state_manager.get_current_session_id()
ptt_pressed = self.state_manager.get_state_data("ptt_pressed", False)
```

**Разрешено:**
```python
# ✅ ПРАВИЛЬНО: Чтение через selectors
from integration.core.selectors import (
    get_current_mode,
    get_current_session_id,
    is_ptt_pressed,
    is_first_run_in_progress
)

current_mode = get_current_mode(self.state_manager)
session_id = get_current_session_id(self.state_manager)
ptt_pressed = is_ptt_pressed(self.state_manager)
first_run = is_first_run_in_progress(self.state_manager)
```

### 2. Принятие решений ТОЛЬКО через gateways

**Правило:** Все решения (start/abort/retry/degrade) должны приниматься через gateways из `integration/core/gateways/*`.

**Запрещено:**
```python
# ❌ НЕПРАВИЛЬНО: Локальное принятие решений в интеграции
if current_mode == AppMode.LISTENING and not ptt_pressed:
    await self._abort_recording()  # Решение в интеграции
```

**Разрешено:**
```python
# ✅ ПРАВИЛЬНО: Решение через gateway
from integration.core.gateways import decide_start_listening, Decision
from integration.core.selectors import create_snapshot_from_state

snapshot = create_snapshot_from_state(self.state_manager)
decision = decide_start_listening(snapshot)

if decision == Decision.START:
    await self.event_bus.publish("voice.recognition.start", {...})
elif decision == Decision.ABORT:
    await self.event_bus.publish("voice.recognition.error", {...})
```

### 3. Интеграции только публикуют события

**Правило:** Интеграции не принимают решения, а только:
- Читают состояние через selectors
- Публикуют события через EventBus
- Обрабатывают события от других интеграций

**Пример правильной интеграции:**
```python
class VoiceRecognitionIntegration:
    async def _on_recording_start(self, event):
        # 1. Читаем состояние через selectors
        snapshot = create_snapshot_from_state(self.state_manager)
        current_mode = get_current_mode(self.state_manager)
        
        # 2. Решение принимается через gateway (если нужно)
        decision = decide_start_listening(snapshot)
        if decision != Decision.START:
            return
        
        # 3. Публикуем событие (не принимаем решение локально)
        await self.event_bus.publish("voice.recognition.started", {
            "session_id": get_current_session_id(self.state_manager)
        })
```

## Доступные selectors

### Основные selectors

| Selector | Возвращает | Описание |
|----------|-----------|----------|
| `get_current_mode(state_manager)` | `AppMode` | Текущий режим приложения (SLEEPING/LISTENING/PROCESSING) |
| `get_current_session_id(state_manager)` | `Optional[str]` | Текущий session_id (uuid4 строка) |
| `is_ptt_pressed(state_manager)` | `bool` | Состояние PTT (нажата/отпущена) |
| `is_first_run_in_progress(state_manager)` | `bool` | Флаг first_run в процессе |
| `is_restart_completed_fallback(state_manager)` | `bool` | Флаг завершения restart fallback |

### Создание Snapshot

Для комплексных проверок используйте `create_snapshot_from_state()`:

```python
from integration.core.selectors import create_snapshot_from_state

snapshot = create_snapshot_from_state(self.state_manager)
# snapshot содержит все оси состояния: permissions, device, network, first_run, app_mode, etc.
```

## Доступные gateways

### Основные gateways

| Gateway | Возвращает | Описание |
|---------|-----------|----------|
| `decide_start_listening(snapshot)` | `Decision` | Решение о запуске listening режима |
| `decide_permission_restart_safety(snapshot)` | `Decision` | Решение о безопасности permission restart |
| `decide_process_audio(snapshot)` | `Decision` | Решение о обработке аудио |

### Типы Decision

```python
from integration.core.gateways.types import Decision

# Decision.START   - разрешить действие
# Decision.ABORT  - прервать действие
# Decision.RETRY   - повторить с backoff
# Decision.DEGRADE - деградировать функционал
```

## Чек-лист перед мерджем

### Обязательные проверки

- [ ] **Нет прямых обращений к `state_manager.get_*()`**
  ```bash
  grep -r "state_manager\.get_current_mode\|state_manager\.get_current_session_id\|state_manager\.get_state_data" integration/integrations/
  # Должно быть: No matches found
  ```

- [ ] **Все чтения состояния через selectors**
  ```bash
  grep -r "get_current_mode\|get_current_session_id\|is_ptt_pressed\|is_first_run_in_progress" integration/integrations/
  # Должны быть использованы selectors
  ```

- [ ] **Решения принимаются через gateways**
  ```bash
  grep -r "decide_\|Decision\." integration/integrations/
  # Должны быть использованы gateways для решений
  ```

- [ ] **Проверка через скрипт**
  ```bash
  python3 client/scripts/verify_no_direct_state_access.py
  # Должно быть: Errors: 0
  ```

- [ ] **Импорты selectors присутствуют**
  ```python
  from integration.core.selectors import (
      get_current_mode,
      get_current_session_id,
      is_ptt_pressed,
      is_first_run_in_progress,
      create_snapshot_from_state
  )
  ```

### Ручные проверки поведения

- [ ] **Mode transitions**
  - SLEEPING → LISTENING → PROCESSING → SLEEPING
  - Проверить корректность переключений режимов

- [ ] **Tray icon updates**
  - Проверить обновление иконки при смене режима

- [ ] **Update start/stop**
  - Проверить работу updater при разных режимах

- [ ] **Interrupt request/cancel**
  - Проверить обработку прерываний

- [ ] **PTT press/long_press → recording flow**
  - Проверить цепочку: PTT → recording → processing

## Правила для новых изменений

### При добавлении новой интеграции

1. **Используйте selectors для чтения состояния:**
   ```python
   from integration.core.selectors import get_current_mode, get_current_session_id
   
   current_mode = get_current_mode(self.state_manager)
   session_id = get_current_session_id(self.state_manager)
   ```

2. **Используйте gateways для принятия решений:**
   ```python
   from integration.core.gateways import decide_start_listening, Decision
   from integration.core.selectors import create_snapshot_from_state
   
   snapshot = create_snapshot_from_state(self.state_manager)
   decision = decide_start_listening(snapshot)
   ```

3. **Публикуйте события, не принимайте решения локально:**
   ```python
   await self.event_bus.publish("module.action", {
       "session_id": session_id,
       "data": {...}
   })
   ```

### При добавлении нового selector

1. **Добавьте функцию в `integration/core/selectors.py`:**
   ```python
   def is_new_flag(state_manager: ApplicationStateManager) -> bool:
       """Check if new_flag is set.
       
       Source of truth is ApplicationStateManager.
       """
       try:
           return bool(state_manager.get_state_data("new_flag", False))
       except Exception:
           return False
   ```

2. **Документируйте selector:**
   - Добавьте описание в таблицу "Доступные selectors"
   - Укажите источник истины

3. **Обновите этот документ:**
   - Добавьте новый selector в таблицу

### При добавлении нового gateway

1. **Добавьте функцию в `integration/core/gateways/*`:**
   ```python
   def decide_new_action(snapshot: Snapshot) -> Decision:
       """Decide whether to perform new action.
       
       Args:
           snapshot: Current system state snapshot
           
       Returns:
           Decision (START/ABORT/RETRY/DEGRADE)
       """
       # Логика принятия решения на основе snapshot
       if snapshot.app_mode == AppMode.SLEEPING:
           return Decision.ABORT
       return Decision.START
   ```

2. **Добавьте canonical logging:**
   ```python
   logger.info(
       f"decision=<start|abort|retry|degrade> "
       f"ctx={{mic={snapshot.perm_mic},mode={snapshot.app_mode}}} "
       f"source=<domain> duration_ms=<int>"
   )
   ```

3. **Обновите этот документ:**
   - Добавьте новый gateway в таблицу

## Исключения

### Разрешённые прямые обращения

**Только в следующих файлах разрешён прямой доступ к `state_manager`:**
- `integration/core/selectors.py` — сами selectors
- `integration/core/gateways/*` — gateways (для чтения состояния)
- `integration/core/state_manager.py` — сам state_manager

**Все остальные файлы обязаны использовать selectors.**

## Автоматические проверки

### CI/CD проверки

Скрипт `client/scripts/verify_no_direct_state_access.py` автоматически проверяет:
- Отсутствие прямых обращений к `state_manager.get_*()` в интеграциях
- Использование selectors для чтения состояния

**Запуск:**
```bash
python3 client/scripts/verify_no_direct_state_access.py
```

**Ожидаемый результат:**
```
Errors:   0
Warnings: <число> (только комментарии)
```

### Линтер проверки

`pyproject.toml` настроен на проверку паттернов доступа к состоянию:
- Проверка прямых обращений к `state_manager.get_*()`
- Проверка использования selectors

## Примеры правильной реализации

### Пример 1: Чтение режима

```python
# ✅ ПРАВИЛЬНО
from integration.core.selectors import get_current_mode

current_mode = get_current_mode(self.state_manager)
if current_mode == AppMode.LISTENING:
    await self._handle_listening()
```

### Пример 2: Принятие решения через gateway

```python
# ✅ ПРАВИЛЬНО
from integration.core.gateways import decide_start_listening, Decision
from integration.core.selectors import create_snapshot_from_state

snapshot = create_snapshot_from_state(self.state_manager)
decision = decide_start_listening(snapshot)

if decision == Decision.START:
    await self.event_bus.publish("voice.recognition.start", {
        "session_id": get_current_session_id(self.state_manager)
    })
```

### Пример 3: Комплексная проверка состояния

```python
# ✅ ПРАВИЛЬНО
from integration.core.selectors import (
    create_snapshot_from_state,
    get_current_mode,
    is_ptt_pressed
)

snapshot = create_snapshot_from_state(self.state_manager)
current_mode = get_current_mode(self.state_manager)
ptt_pressed = is_ptt_pressed(self.state_manager)

if current_mode == AppMode.LISTENING and ptt_pressed:
    # Публикуем событие
    await self.event_bus.publish("input.ptt_pressed", {...})
```

## Связанные документы

- `Docs/ARCHITECTURE_OVERVIEW.md` — обзор архитектуры
- `Docs/STATE_CATALOG.md` — каталог осей состояния
- `config/interaction_matrix.yaml` — матрица взаимодействий
- `integration/core/selectors.py` — реализация selectors
- `integration/core/gateways/` — реализация gateways

## История изменений

- **2026-01-11**: Создан документ с правилами доступа к состоянию
- **2026-01-11**: Зафиксированы selectors и gateways после централизации

---

**Важно:** Любые изменения, нарушающие эти правила, должны быть отклонены на ревью.
