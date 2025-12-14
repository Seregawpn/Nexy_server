# Анализ решений проблем активации микрофона с учетом архитектуры

## Дата создания
2025-01-XX

## Обзор

Этот документ анализирует возможные решения трех проблем активации микрофона с учетом архитектуры проекта, принципов и существующих паттернов.

---

## Архитектурные принципы проекта

### Ключевые принципы:
1. **EventBus** — все коммуникации через события
2. **ApplicationStateManager** — единый источник истины для состояния
3. **Gateways/Selectors** — паттерн принятия решений на основе Snapshot
4. **Interaction Matrix** — правила взаимодействия осей (hard_stop/graceful/preference)
5. **Workflows** — координаторы режимов (не дублируют логику интеграций)
6. **Интеграции** — тонкие обертки над модулями
7. **Запрет прямого доступа к состоянию** — только через selectors/gateways

### Существующие паттерны:
- `decide_start_listening(snapshot)` — gateway для принятия решений
- `Snapshot` — неизменяемый снимок всех осей состояния
- `interaction_matrix.yaml` — правила взаимодействия осей
- `force_close_microphone()` — метод принудительного закрытия микрофона
- `_publish_recording_stop_with_debounce()` — паттерн debounce для событий

---

## Варианты решений

### Вариант 1: Прямое исправление в интеграциях (простой)

**Уровень сложности:** Простой  
**Время реализации:** 2-4 часа  
**Соответствие архитектуре:** ⚠️ Частичное

#### Описание:
Прямое исправление проблем в существующих методах интеграций без изменения архитектуры.

#### Реализация:

**Проблема 1:**
```python
# input_processing_integration.py:_on_playback_finished()
async def _on_playback_finished(self, event):
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:  # ✅ Добавляем проверку без _recording_started
        await self._publish_recording_stop_with_debounce({...})
        await self._wait_for_mic_closed_with_timeout(...)
    # ...
```

**Проблема 2:**
```python
# voice_recognition_integration.py:_on_recording_start()
# Гарантированная деактивация AVF (5 попыток)
for attempt in range(5):
    if avf_engine.is_input_active:
        await asyncio.sleep(0.2)
    else:
        break
else:
    raise RuntimeError("AVF not deactivated")
```

**Проблема 3:**
```python
# input_processing_integration.py:_handle_long_press()
# Разрешаем активацию через Shortcut ВСЕГДА
if current_mode == AppMode.PROCESSING:
    # НЕ блокируем - продолжаем активацию
    pass
```

#### Преимущества:
- ✅ Быстрое внедрение
- ✅ Минимальные изменения кода
- ✅ Использует существующие методы (`force_close_microphone`, `_publish_recording_stop_with_debounce`)

#### Недостатки:
- ⚠️ Не использует gateways для принятия решений
- ⚠️ Логика остается в интеграциях (не централизована)
- ⚠️ Не соответствует паттерну selectors/gateways для проверки состояния

#### Риски:
- **Низкий:** Минимальные изменения, низкий риск регрессий
- **Средний:** Не соответствует архитектурным принципам (прямой доступ к состоянию)

---

### Вариант 2: Использование gateways для принятия решений (средний)

**Уровень сложности:** Средний  
**Время реализации:** 4-8 часов  
**Соответствие архитектуре:** ✅ Полное

#### Описание:
Создание новых gateways для принятия решений о закрытии микрофона и активации через Shortcut, использование существующего паттерна selectors/gateways.

#### Реализация:

**1. Добавить новые selectors:**
```python
# integration/core/selectors.py
def mic_active_after_playback(s: Snapshot) -> bool:
    """Проверяет, активен ли микрофон после завершения воспроизведения"""
    return s.mic_state == "active" and s.app_mode == AppMode.SLEEPING

def playback_active(s: Snapshot) -> bool:
    """Проверяет, активно ли воспроизведение"""
    return s.playback_active  # Нужно добавить в Snapshot
```

**2. Добавить новые gateways:**
```python
# integration/core/gateways/audio_gateways.py
def decide_microphone_cleanup_after_playback(s: Snapshot) -> Decision:
    """
    Решает, нужно ли принудительно закрыть микрофон после playback.completed
    """
    if mic_active_after_playback(s):
        return Decision.ABORT  # Принудительно закрыть
    return Decision.START  # Микрофон уже закрыт

def decide_allow_shortcut_during_processing(s: Snapshot, source: str) -> Decision:
    """
    Решает, разрешена ли активация через Shortcut во время PROCESSING
    """
    if s.app_mode == AppMode.PROCESSING and source == "keyboard":
        return Decision.START  # Разрешаем для прерывания
    if s.app_mode == AppMode.PROCESSING and source != "keyboard":
        return Decision.ABORT  # Блокируем автоматическую активацию
    return Decision.START
```

**3. Добавить правила в interaction_matrix.yaml:**
```yaml
rules:
  # Принудительное закрытие микрофона после playback.completed
  - when: {mic.state: active, app.mode: SLEEPING, playback.completed: true}
    decision: abort
    priority: hard_stop
    description: Microphone must be closed after playback completion
    gateway: decide_microphone_cleanup_after_playback
  
  # Разрешение активации через Shortcut во время PROCESSING
  - when: {app.mode: PROCESSING, source: keyboard}
    decision: start
    priority: preference
    description: Allow shortcut activation during PROCESSING for interruption
    gateway: decide_allow_shortcut_during_processing
```

**4. Использовать gateways в интеграциях:**
```python
# input_processing_integration.py:_on_playback_finished()
async def _on_playback_finished(self, event):
    snapshot = create_snapshot_from_state(self.state_manager)
    decision = decide_microphone_cleanup_after_playback(snapshot)
    if decision == Decision.ABORT:
        await self._publish_recording_stop_with_debounce({...})
        await self._wait_for_mic_closed_with_timeout(...)
```

#### Преимущества:
- ✅ Полное соответствие архитектуре (gateways/selectors)
- ✅ Централизованная логика принятия решений
- ✅ Легко тестировать (изолированные gateways)
- ✅ Правила в interaction_matrix.yaml (машинно-проверяемые)

#### Недостатки:
- ⚠️ Требует добавления новых осей в Snapshot (playback_active)
- ⚠️ Требует обновления STATE_CATALOG.md и interaction_matrix.yaml
- ⚠️ Больше изменений кода

#### Риски:
- **Средний:** Требует синхронизации STATE_CATALOG.md → interaction_matrix.yaml → gateways → тесты
- **Низкий:** Соответствует архитектуре, низкий риск регрессий

---

### Вариант 3: Создание нового workflow для координации (сложный)

**Уровень сложности:** Сложный  
**Время реализации:** 8-16 часов  
**Соответствие архитектуре:** ✅ Полное

#### Описание:
Создание нового `MicrophoneCleanupWorkflow` для координации закрытия микрофона после завершения воспроизведения, аналогично `ProcessingWorkflow` и `ListeningWorkflow`.

#### Реализация:

**1. Создать MicrophoneCleanupWorkflow:**
```python
# integration/workflows/microphone_cleanup_workflow.py
class MicrophoneCleanupWorkflow(BaseWorkflow):
    """
    Координирует закрытие микрофона после завершения воспроизведения
    """
    async def _handle_playback_completed(self, event):
        snapshot = create_snapshot_from_state(self.state_manager)
        decision = decide_microphone_cleanup_after_playback(snapshot)
        
        if decision == Decision.ABORT:
            # Принудительно закрываем микрофон
            await self.event_bus.publish("microphone.force_close", {
                "session_id": None,
                "reason": "playback_completed"
            })
            await self._wait_for_mic_closed()
```

**2. Интегрировать в SimpleModuleCoordinator:**
```python
# integration/core/simple_module_coordinator.py
self.microphone_cleanup_workflow = MicrophoneCleanupWorkflow(...)
await self.microphone_cleanup_workflow.initialize()
```

#### Преимущества:
- ✅ Полное соответствие архитектуре (workflows для координации)
- ✅ Изоляция логики координации от интеграций
- ✅ Легко расширять и тестировать

#### Недостатки:
- ❌ Избыточно для простых проверок
- ❌ Требует создания нового workflow (overhead)
- ❌ Усложняет архитектуру без необходимости

#### Риски:
- **Высокий:** Избыточная сложность для простых проблем
- **Средний:** Требует интеграции в SimpleModuleCoordinator

---

### Вариант 4: Расширение interaction_matrix.yaml с новыми правилами (средний)

**Уровень сложности:** Средний  
**Время реализации:** 4-6 часов  
**Соответствие архитектуре:** ✅ Полное

#### Описание:
Добавление новых правил в `interaction_matrix.yaml` для управления закрытием микрофона и активацией через Shortcut, использование существующего DecisionEngine.

#### Реализация:

**1. Добавить новые оси в STATE_CATALOG.md:**
```markdown
#### 10) playback.active
- **владелец**: SpeechPlaybackIntegration owner
- **пишет**: `speech_playback_integration`
- **читает**: `input_processing`, `voice_recognition`
- **источник истины**: `InputProcessingIntegration._playback_active`
- **метрики**: `playback_duration_ms`
```

**2. Добавить правила в interaction_matrix.yaml:**
```yaml
axes:
  playback.active: [true, false]
  mic.state: [idle, active, opening, closing, error]

rules:
  # Принудительное закрытие микрофона после playback.completed
  - when: {mic.state: active, playback.active: false, playback.completed: true}
    decision: abort
    priority: hard_stop
    description: Microphone must be closed after playback completion
    gateway: decide_microphone_cleanup_after_playback
  
  # Разрешение активации через Shortcut во время PROCESSING
  - when: {app.mode: PROCESSING, source: keyboard, playback.active: true}
    decision: start
    priority: preference
    description: Allow shortcut activation during PROCESSING for interruption
    gateway: decide_allow_shortcut_during_processing
```

**3. Использовать DecisionEngine в интеграциях:**
```python
# input_processing_integration.py:_on_playback_finished()
async def _on_playback_finished(self, event):
    snapshot = create_snapshot_from_state(self.state_manager)
    engine = get_engine("decide_microphone_cleanup_after_playback")
    decision = engine.decide(snapshot, source="playback_finished", ctx=ctx)
    
    if decision == Decision.ABORT:
        await self._publish_recording_stop_with_debounce({...})
```

#### Преимущества:
- ✅ Полное соответствие архитектуре (interaction_matrix.yaml)
- ✅ Использует существующий DecisionEngine
- ✅ Правила машинно-проверяемые
- ✅ Легко расширять новыми правилами

#### Недостатки:
- ⚠️ Требует добавления новых осей в Snapshot
- ⚠️ Требует обновления STATE_CATALOG.md
- ⚠️ Требует создания новых gateways

#### Риски:
- **Средний:** Требует синхронизации STATE_CATALOG.md → interaction_matrix.yaml → gateways → тесты
- **Низкий:** Соответствует архитектуре

---

### Вариант 5: Комбинированный подход (оптимальный) ⭐

**Уровень сложности:** Средний  
**Время реализации:** 4-6 часов  
**Соответствие архитектуре:** ✅ Полное

#### Описание:
Комбинация прямых исправлений для простых случаев и использования gateways для сложных решений, максимальное использование существующих паттернов.

#### Реализация:

**Проблема 1: Прямое исправление (простое)**
```python
# input_processing_integration.py:_on_playback_finished()
async def _on_playback_finished(self, event):
    # ✅ Используем существующий метод force_close_microphone
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:
        # Принудительно закрываем через существующий метод
        self.state_manager.force_close_microphone(reason="playback_completed")
        await self._publish_recording_stop_with_debounce({
            "session_id": None,
            "source": "playback_finished"
        })
        await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
    # ...
```

**Проблема 2: Прямое исправление (простое)**
```python
# voice_recognition_integration.py:_on_recording_start()
# Гарантированная деактивация AVF (5 попыток)
max_avf_check_attempts = 5
for attempt in range(max_avf_check_attempts):
    if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
        await asyncio.sleep(0.2)
    else:
        break
else:
    raise RuntimeError("AVF not deactivated after all attempts")
```

**Проблема 3: Использование gateway (сложное решение)**
```python
# Добавить gateway для принятия решения
def decide_allow_shortcut_during_processing(s: Snapshot, source: str) -> Decision:
    """Решает, разрешена ли активация через Shortcut во время PROCESSING"""
    if s.app_mode == AppMode.PROCESSING and source == "keyboard":
        return Decision.START  # Разрешаем для прерывания
    return Decision.ABORT  # Блокируем автоматическую активацию

# Использовать в _handle_long_press()
async def _handle_long_press(self, event: KeyEvent):
    snapshot = create_snapshot_from_state(self.state_manager)
    decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
    if decision == Decision.ABORT:
        return  # Блокируем
    # Продолжаем активацию...
```

#### Преимущества:
- ✅ Баланс между простотой и соответствием архитектуре
- ✅ Использует существующие методы (`force_close_microphone`)
- ✅ Использует gateways для сложных решений
- ✅ Минимальные изменения кода
- ✅ Быстрое внедрение

#### Недостатки:
- ⚠️ Смешанный подход (не полностью через gateways)

#### Риски:
- **Низкий:** Использует существующие паттерны, минимальный риск регрессий

---

## Сравнительная таблица решений

| Критерий | Вариант 1 (Прямое) | Вариант 2 (Gateways) | Вариант 3 (Workflow) | Вариант 4 (Matrix) | Вариант 5 (Комбинированный) ⭐ |
|---------|-------------------|---------------------|---------------------|-------------------|-------------------------------|
| **Уровень сложности** | Простой | Средний | Сложный | Средний | Средний |
| **Время реализации** | 2-4 часа | 4-8 часов | 8-16 часов | 4-6 часов | 4-6 часов |
| **Соответствие архитектуре** | ⚠️ Частичное | ✅ Полное | ✅ Полное | ✅ Полное | ✅ Полное |
| **Использование gateways** | ❌ Нет | ✅ Да | ✅ Да | ✅ Да | ✅ Частично |
| **Использование существующих методов** | ✅ Да | ⚠️ Частично | ❌ Нет | ⚠️ Частично | ✅ Да |
| **Централизация логики** | ❌ Нет | ✅ Да | ✅ Да | ✅ Да | ⚠️ Частично |
| **Тестируемость** | ⚠️ Средняя | ✅ Высокая | ✅ Высокая | ✅ Высокая | ✅ Высокая |
| **Расширяемость** | ❌ Низкая | ✅ Высокая | ✅ Высокая | ✅ Высокая | ⚠️ Средняя |
| **Риск регрессий** | Низкий | Низкий | Средний | Низкий | Низкий |

---

## Рекомендуемое решение: Вариант 5 (Комбинированный подход) ⭐

### Обоснование:

1. **Баланс простоты и архитектуры:**
   - Использует существующие методы (`force_close_microphone`) для простых случаев
   - Использует gateways для сложных решений (активация через Shortcut)
   - Минимальные изменения кода

2. **Соответствие принципам:**
   - Использует `ApplicationStateManager` как единый источник истины
   - Использует EventBus для коммуникации
   - Использует gateways для принятия решений (где необходимо)

3. **Быстрое внедрение:**
   - 4-6 часов реализации
   - Низкий риск регрессий
   - Легко тестировать

4. **Расширяемость:**
   - Можно добавить правила в `interaction_matrix.yaml` позже
   - Можно создать workflow для координации позже (если понадобится)

---

## Детальный план реализации (Вариант 5)

### Этап 1: Исправление проблемы 1 (2 часа)

**Файл:** `integration/integrations/input_processing_integration.py`

**Изменение:**
```python
async def _on_playback_finished(self, event):
    # ...
    # ✅ ИСПРАВЛЕНИЕ: Принудительно закрываем микрофон, если он активен
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:
        logger.warning(f"⚠️ PLAYBACK: микрофон активен после playback.completed - принудительно закрываем")
        # Используем существующий метод force_close_microphone
        self.state_manager.force_close_microphone(reason="playback_completed")
        await self._publish_recording_stop_with_debounce({
            "source": "playback_finished",
            "timestamp": time.time(),
            "session_id": None,  # Закрываем любой активный микрофон
        })
        await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
    
    # Проверка новой записи (если mic_active && _recording_started)
    if mic_active and self._recording_started:
        # НЕ сбрасываем сессию
        return
    # ...
```

**Тестирование:**
- Изолированный тест: `test_problem1_microphone_closed_after_playback_completed`
- Проверка: микрофон закрыт, `voice.recording_stop` опубликован

---

### Этап 2: Исправление проблемы 2 (1 час)

**Файл:** `integration/integrations/voice_recognition_integration.py`

**Изменение:**
```python
async def _on_recording_start(self, event: Dict[str, Any]):
    # ...
    if self._use_avf and self._avf_engine is not None:
        # AVF диагностика...
        await self._avf_engine.start_input()
        await asyncio.sleep(1.0)
        await self._avf_engine.stop_input()
        await asyncio.sleep(0.2)
        
        # ✅ ИСПРАВЛЕНИЕ: Гарантированная деактивация AVF (5 попыток)
        max_avf_check_attempts = 5
        for attempt in range(max_avf_check_attempts):
            if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
                logger.warning(f"⚠️ [AVF] AVF все еще активен (попытка {attempt+1}/{max_avf_check_attempts})")
                await asyncio.sleep(0.2)
            else:
                logger.info(f"✅ [AVF] AVF полностью деактивирован (попытка {attempt+1})")
                break
        else:
            logger.error("❌ [AVF] AVF не деактивирован после всех попыток - возможен конфликт")
            raise RuntimeError("AVF not deactivated after all attempts")
    
    # ✅ ИСПРАВЛЕНИЕ: Обязательная проверка разрешений (ошибка → исключение)
    try:
        from modules.permissions.core.permission_checker import PermissionChecker
        permission_checker = PermissionChecker()
        mic_permission = permission_checker.check_microphone_permission()
        if mic_permission != "granted":
            raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
    except Exception as perm_error:
        logger.error(f"❌ [Google] Критическая ошибка проверки разрешений: {perm_error}")
        raise  # Пробрасываем ошибку, не продолжаем
    # ...
```

**Тестирование:**
- Изолированный тест: проверка деактивации AVF (5 попыток)
- Проверка: исключение выбрасывается, если AVF не деактивирован

---

### Этап 3: Исправление проблемы 3 (1-2 часа)

**Файл 1:** `integration/core/gateways/audio_gateways.py` (новый файл)

**Создать gateway:**
```python
from integration.core.selectors import Snapshot
from integration.core.gateways.types import Decision

def decide_allow_shortcut_during_processing(snapshot: Snapshot, source: str) -> Decision:
    """
    Решает, разрешена ли активация через Shortcut во время PROCESSING.
    
    Правило: Разрешаем активацию через Shortcut ВСЕГДА (для прерывания воспроизведения).
    Блокируем только автоматическую активацию (когда source != "keyboard").
    """
    if snapshot.app_mode == AppMode.PROCESSING:
        if source == "keyboard":
            return Decision.START  # Разрешаем для прерывания
        else:
            return Decision.ABORT  # Блокируем автоматическую активацию
    return Decision.START  # Разрешаем в других режимах
```

**Файл 2:** `integration/integrations/input_processing_integration.py`

**Изменение:**
```python
async def _handle_long_press(self, event: KeyEvent):
    # ...
    # ✅ ИСПРАВЛЕНИЕ: Используем gateway для принятия решения
    from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
    from integration.core.selectors import create_snapshot_from_state
    
    snapshot = create_snapshot_from_state(self.state_manager)
    decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
    
    if decision == Decision.ABORT:
        logger.warning("🔒 LONG_PRESS blocked by gateway decision")
        self._long_press_in_progress = False
        return
    
    # Принудительное закрытие микрофона перед новой записью
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:
        logger.warning(f"⚠️ LONG_PRESS: микрофон активен перед новой записью - принудительно закрываем")
        await self._publish_recording_stop_with_debounce({
            "source": "long_press_cleanup",
            "timestamp": event.timestamp,
            "session_id": None,
        })
        await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="LONG_PRESS")
    
    # Продолжаем активацию...
```

**Тестирование:**
- Изолированный тест: `test_problem3_long_press_allowed_during_processing`
- Проверка: `voice.recording_start` публикуется, активация разрешена

---

## Чек-лист реализации

### Перед началом:
- [ ] Прочитать `Docs/PRE_CHANGE_PLANNING_CHECKLIST.md` и пройти этапы 1-6
- [ ] Создать Impact Map с таблицей влияния
- [ ] Создать `.impact/change_impact.yaml`
- [ ] Обновить `Docs/STATE_CATALOG.md` (если добавляются новые оси)
- [ ] Обновить `config/interaction_matrix.yaml` (если добавляются новые правила)

### Во время реализации:
- [ ] Исправить `_on_playback_finished()` - принудительное закрытие микрофона
- [ ] Улучшить деактивацию AVF - гарантированная деактивация (5 попыток)
- [ ] Улучшить проверку разрешений - обязательная проверка (ошибка → исключение)
- [ ] Создать gateway `decide_allow_shortcut_during_processing`
- [ ] Исправить `_handle_long_press()` - использовать gateway для принятия решения

### После реализации:
- [ ] Создать изолированные тесты для проверки исправленной функциональности
- [ ] Запустить существующие тесты для проверки регрессий
- [ ] Обновить документацию (если нужно)
- [ ] Запустить `scripts/pre_build_gate.sh` для проверки всех обязательных проверок

---

## Оценка рисков

### Риски реализации:

1. **Низкий риск:** Исправление проблемы 1 (принудительное закрытие микрофона)
   - Использует существующий метод `force_close_microphone`
   - Минимальные изменения кода
   - Легко тестировать

2. **Низкий риск:** Исправление проблемы 2 (деактивация AVF)
   - Простое добавление цикла проверки
   - Не затрагивает другие компоненты
   - Легко тестировать

3. **Средний риск:** Исправление проблемы 3 (gateway для активации)
   - Требует создания нового gateway
   - Требует интеграции в `_handle_long_press()`
   - Нужно протестировать все сценарии

### Управление рисками:

- **Изоляция:** Каждое исправление изолировано и тестируется отдельно
- **Тестирование:** Изолированные тесты для каждой проблемы
- **Постепенное внедрение:** Исправления можно внедрять по одному
- **Откат:** Каждое исправление можно откатить независимо

---

## Связанные документы

- `Docs/CURRENT_VS_IDEAL_COMPARISON.md` — сравнение текущей и идеальной системы
- `Docs/ISOLATION_TEST_RESULTS.md` — результаты изолированного тестирования
- `Docs/IDEAL_AUDIO_SYSTEM_DIAGRAM.md` — идеальная система
- `tests/test_microphone_activation_issues_isolation.py` — изолированные тесты

