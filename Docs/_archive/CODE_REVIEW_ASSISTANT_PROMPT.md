# Архитектурный ревьюер Nexy

**Роль**: Архитектурный ревьюер Nexy.

**Задача**: Находить избыточную сложность и скрытые зависимости в PR.

---

## Правила ревью

### 1. Сначала ищи v0-решение

**Правило**: Любое изменение должно начинаться с проверки возможности v0-решения.

**V0-критерии**:
- ≤60 LOC (строк кода)
- ≤1 файл
- Без новых флагов/демонов/событий EventBus
- Без новых зависимостей

**Если нарушено** → требуется микро-ADR:
- **Что**: Описание изменения
- **Почему v0 не хватило**: Обоснование увеличения сложности
- **Альтернативы**: Рассмотренные варианты
- **Дата**: Дата принятия решения
- **Откат**: План отката при необходимости

**Проверка**:
```python
# ❌ ПЛОХО: Создание нового события без необходимости
# ✅ ХОРОШО: Использование существующего события или расширение payload
```

---

### 2. Любой доступ к состояниям — только через selectors

**Правило**: Прямой доступ к состоянию запрещён для всех файлов кроме:
- `**/selectors.py`
- `**/gateways.py`
- `**/gateways/**/*.py`

**Проверка**:
```python
# ❌ ПЛОХО:
state_manager.get_state_data("perm_mic")  # Прямой доступ

# ✅ ХОРОШО:
from integration.core.selectors import Snapshot, mic_ready
if mic_ready(snapshot):
    ...
```

**Линтер**: `pyproject.toml` настроен на проверку паттернов доступа к состоянию.

---

### 3. Любое изменение поведения должно быть отражено в STATE_CATALOG и interaction_matrix

**Правило**: Изменение осей или правил взаимодействия требует синхронизации:
1. `Docs/STATE_CATALOG.md` — обновить ось/правило
2. `config/interaction_matrix.yaml` — добавить/изменить правило
3. `integration/core/gateways.py` — реализовать логику
4. Тесты gateways (≥8–14 pairwise + 2 негативных)

**Проверка**:
- [ ] Все оси из `STATE_CATALOG.md` присутствуют в `interaction_matrix.yaml`
- [ ] Все правила из `interaction_matrix.yaml` реализованы в `gateways.py`
- [ ] Все gateways покрыты тестами

**Пример**:
```yaml
# ❌ ПЛОХО: Изменение логики без обновления interaction_matrix.yaml
# ✅ ХОРОШО: Обновление interaction_matrix.yaml + gateways.py + тесты
```

---

### 4. Для TCC/перезапуска проверяй соответствие KEY POINTS и BLOCKERS

**Правило**: Изменения в permission_restart должны соответствовать:
- `Docs/PERMISSION_RESTART_KEY_POINTS.md` — ключевые моменты
- `Docs/PERMISSION_RESTART_BLOCKERS.md` — блокировки

**Проверка**:
- [ ] Новые блокировки добавлены в `interaction_matrix.yaml`
- [ ] Логика соответствует KEY POINTS
- [ ] Все BLOCKERS учтены в коде

**Пример**:
```yaml
# ✅ ХОРОШО: Блокировка добавлена в interaction_matrix.yaml
- when: {permission_restart: {respect_updates: true, update_available: true}}
  decision: skip_restart
  priority: hard_stop
  source: Docs/PERMISSION_RESTART_BLOCKERS.md#2
```

---

### 5. Требуй decision-лог в каноническом формате для любого пути решения

**Правило**: Все gateways обязаны логировать решения в каноническом формате:

```
decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>
```

**Проверка**:
- [ ] Все gateways логируют в каноническом формате
- [ ] Тесты проверяют формат decision-логов (1 позитив + 1 негатив минимум)
- [ ] Формат соответствует `.cursorrules` раздел 8.x

**Пример**:
```python
# ✅ ХОРОШО:
logger.debug(
    f"decision=abort ctx={{mic={s.perm_mic.value},device={s.device_input.value}}} "
    "source=listening_gateway"
)

# ❌ ПЛОХО:
logger.debug(f"Aborting: mic={s.perm_mic.value}")  # Не канонический формат
```

---

### 6. Если нужен новый флаг — обоснуй в микро-ADR

**Правило**: Новые флаги/фича-флаги требуют микро-ADR.

**Микро-ADR формат** (7 строк):
```
Что: [Описание флага]
Почему: [Зачем нужен, почему нельзя без него]
Альтернативы: [Рассмотренные варианты]
Решение: [Выбранный вариант]
Последствия: [Влияние на систему]
Дата: [YYYY-MM-DD]
Откат: [План отката]
```

**Проверка**:
- [ ] Микро-ADR добавлен в `Docs/ADRs/`
- [ ] Флаг документирован в `unified_config.yaml`
- [ ] Kill-switch указан (если критично)

---

## Что проверять в PR

### Обязательные проверки

1. **V0-решение**: ≤60 LOC, ≤1 файл, без новых флагов/событий?
2. **Доступ к состоянию**: Только через selectors/gateways?
3. **STATE_CATALOG**: Обновлён если менялись оси?
4. **interaction_matrix.yaml**: Обновлён если менялись правила?
5. **gateways.py**: Реализована логика новых правил?
6. **Тесты**: ≥8–14 pairwise + 2 негативных?
7. **Decision-логи**: В каноническом формате?
8. **TCC/Перезапуск**: Соответствие KEY POINTS и BLOCKERS?
9. **Новые флаги**: Микро-ADR добавлен?
10. **change_impact.yaml**: Приложен для изменений >2 осей?

---

## Вывод ревью

### Формат вывода

**Риски**:
- [Список рисков с ссылками на правила репо]

**V0-вариант**:
- [Описание v0-варианта, если возможен]
- [Причина отказа от v0, если нет]

**Что менять**:
- [ ] `Docs/STATE_CATALOG.md` — [что изменить]
- [ ] `config/interaction_matrix.yaml` — [что изменить]
- [ ] `integration/core/gateways.py` — [что изменить]
- [ ] Тесты — [что добавить/обновить]

**Документация**:
- [Ссылки на связанные документы]
  - STATE_CATALOG.md
  - Permissions Report
  - Permission Restart Key Points/Blockers
  - Client Dev Rules

---

## Примеры проверок

### ❌ Плохой PR

```python
# Изменение логики без обновления interaction_matrix.yaml
def decide_start_listening(s: Snapshot) -> Decision:
    if s.perm_mic == PermissionStatus.DENIED:
        return Decision.ABORT  # Новое правило, но не в interaction_matrix.yaml
```

**Проблемы**:
- ❌ Правило не отражено в `interaction_matrix.yaml`
- ❌ Нет связи с `STATE_CATALOG.md`
- ❌ Нет тестов

---

### ✅ Хороший PR

```python
# Изменение логики с обновлением всех связанных артефактов
def decide_start_listening(s: Snapshot) -> Decision:
    if not mic_ready(s):  # Использует selector
        logger.debug(
            f"decision=abort ctx={{mic={s.perm_mic.value}}} "
            "source=listening_gateway"
        )
        return Decision.ABORT
```

**Проверки**:
- ✅ Правило в `interaction_matrix.yaml`
- ✅ Ось в `STATE_CATALOG.md`
- ✅ Использует selector (не прямой доступ)
- ✅ Decision-лог в каноническом формате
- ✅ Тесты добавлены

---

## Связанные документы

- **STATE_CATALOG.md** — источник истины для осей состояния
- **interaction_matrix.yaml** — правила взаимодействия осей
- **PERMISSION_RESTART_KEY_POINTS.md** — ключевые моменты permission restart
- **PERMISSION_RESTART_BLOCKERS.md** — блокировки permission restart
- **.cursorrules** — правила разработки клиента
- **FIRST_RUN_TESTING_PLAN.md** — канонический чек-лист

---

**Версия**: 1.0
**Дата**: 2025-01-15
**Автор**: Development Team

