# Руководство по централизации и синхронизации состояния микрофона

## Дата создания
2025-01-XX

## Обзор

Этот документ содержит практическое руководство по централизации и синхронизации управления состоянием микрофона, чтобы устранить проблему рассинхронизации.

---

## 🎯 Принципы централизации

### 1. Единый источник истины

**ApplicationStateManager** — единственный источник истины для состояния микрофона.

```
┌─────────────────────────────────────────────────────────────┐
│         ApplicationStateManager (ЕДИНЫЙ ИСТОЧНИК)          │
│                                                              │
│  ✅ is_microphone_active()  ← Все читают отсюда            │
│  ✅ set_microphone_state()  ← Все пишут сюда                │
│  ✅ get_microphone_state()  ← Все читают отсюда             │
│  ✅ force_close_microphone() ← Принудительное закрытие     │
└─────────────────────────────────────────────────────────────┘
```

### 2. Правило использования локальных флагов

**Локальные флаги используются ТОЛЬКО для внутренней логики, НЕ для проверок состояния.**

```python
# ❌ ПЛОХО: Использование локального флага для проверки состояния
if self._recording_started:  # Локальный флаг
    # ...

# ✅ ХОРОШО: Использование единого источника истины
if self.state_manager.is_microphone_active():  # Единый источник
    # ...
```

### 3. Правило синхронизации

**При каждом изменении состояния микрофона ОБЯЗАТЕЛЬНО обновлять ApplicationStateManager.**

```python
# ✅ ПРАВИЛЬНО: Синхронизация при изменении состояния
async def _on_recording_start(self, event):
    # 1. Обновляем локальный флаг (для внутренней логики)
    self._recording_started = True
    
    # 2. ОБЯЗАТЕЛЬНО: Обновляем единый источник истины
    self.state_manager.set_microphone_state("active", session_id=session_id)
    
    # 3. Публикуем событие
    await self.event_bus.publish("microphone.opened", {...})
```

---

## 📋 Пошаговый план централизации

### Этап 1: Аудит текущего использования локальных флагов

**Цель:** Найти все места, где используются локальные флаги для проверки состояния.

**Шаги:**

1. **Найти все проверки состояния через локальные флаги:**

```bash
# Найти все использования _recording_started для проверок
grep -n "_recording_started" integration/integrations/input_processing_integration.py | grep -E "if|and|or"

# Найти все использования _playback_active для проверок
grep -n "_playback_active" integration/integrations/input_processing_integration.py | grep -E "if|and|or"

# Найти все использования _google_recording_active для проверок
grep -n "_google_recording_active" integration/integrations/voice_recognition_integration.py | grep -E "if|and|or"
```

2. **Составить список мест для замены:**

| Файл | Строка | Текущий код | Заменить на |
|------|--------|-------------|-------------|
| `input_processing_integration.py` | 859 | `if mic_active and self._recording_started:` | `if mic_active:` |
| `input_processing_integration.py` | 1802 | `if self._playback_active:` | Использовать gateway |
| `voice_recognition_integration.py` | 948 | `if not self._google_recording_active:` | `if not self.state_manager.is_microphone_active():` |

---

### Этап 2: Замена проверок состояния на единый источник истины

**Цель:** Заменить все проверки состояния через локальные флаги на проверки через `ApplicationStateManager`.

#### Шаг 2.1: Проблема 1 — Закрытие микрофона после playback.completed

**Файл:** `integration/integrations/input_processing_integration.py`  
**Строка:** 859-875

**Текущий код (проблема):**
```python
async def _on_playback_finished(self, event):
    # ...
    mic_active = self.state_manager.is_microphone_active()  # ✅ Единый источник
    if mic_active and self._recording_started:  # ❌ Локальный флаг
        # ...
        return
    # ❌ ПРОБЛЕМА: Если mic_active=True, но _recording_started=False,
    # микрофон не закрывается!
```

**Исправленный код:**
```python
async def _on_playback_finished(self, event):
    """Обрабатывает завершение воспроизведения и сбрасывает сессию."""
    try:
        data = (event or {}).get("data", {}) or {}
        event_session_id = data.get("session_id")
        event_type = (event or {}).get("type", "unknown")
        logger.debug("PLAYBACK: finished (event=%s, session=%s)", event_type, event_session_id)
        
        active_session_id = self._get_active_session_id()
        
        # ✅ ИСПРАВЛЕНИЕ: Используем ТОЛЬКО единый источник истины
        # Не проверяем локальный флаг _recording_started
        mic_active = self.state_manager.is_microphone_active()
        
        if mic_active:
            # ✅ КРИТИЧНО: Проверяем, не активен ли микрофон с новой сессией
            # Если микрофон активен и _recording_started=True, значит LONG_PRESS уже активировал новую запись
            # В этом случае НЕ сбрасываем session_id, чтобы не потерять новую сессию
            if self._recording_started:
                logger.warning(f"⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id")
                # ... (остальная логика для новой записи)
                return
            
            # ✅ ИСПРАВЛЕНИЕ: Принудительно закрываем микрофон, если он активен
            logger.warning(f"⚠️ PLAYBACK: микрофон активен после playback.completed - принудительно закрываем")
            # Используем существующий метод force_close_microphone (единый источник истины)
            self.state_manager.force_close_microphone(reason="playback_completed")
            # Публикуем voice.recording_stop для синхронизации с VoiceRecognitionIntegration
            await self._publish_recording_stop_with_debounce({
                "source": "playback_finished",
                "timestamp": time.time(),
                "session_id": None,  # Закрываем любой активный микрофон
            })
            # Ждём закрытия микрофона для гарантии
            await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
        
        # Остальная логика сброса сессии...
        # ...
```

**Что изменилось:**
- ✅ Убрана проверка `and self._recording_started` из условия закрытия микрофона
- ✅ Используется только `state_manager.is_microphone_active()` (единый источник истины)
- ✅ Добавлено принудительное закрытие микрофона через `force_close_microphone()`

#### Шаг 2.2: Проблема 2 — Деактивация AVF и проверка разрешений

**Файл:** `integration/integrations/voice_recognition_integration.py`  
**Строка:** 842-847, 854-864

**Текущий код (проблема):**
```python
async def _on_recording_start(self, event: Dict[str, Any]):
    # ...
    if self._use_avf and self._avf_engine is not None:
        await self._avf_engine.start_input()
        await asyncio.sleep(1.0)
        await self._avf_engine.stop_input()
        await asyncio.sleep(0.2)
        
        # ❌ ПРОБЛЕМА: Проверка выполняется только один раз
        if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
            logger.warning("⚠️ [AVF] AVF все еще активен...")
            await asyncio.sleep(0.5)
            if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
                logger.error("❌ [AVF] AVF все еще активен...")
                # ❌ ПРОБЛЕМА: Продолжаем работу, не выбрасывая исключение!
    
    # ❌ ПРОБЛЕМА: Проверка разрешений может быть пропущена
    try:
        mic_permission = permission_checker.check_microphone_permission()
        if mic_permission != "granted":
            raise RuntimeError("...")
    except Exception as perm_error:
        logger.warning("⚠️ Не удалось проверить разрешения...")
        # ❌ ПРОБЛЕМА: Продолжаем работу, не выбрасывая исключение!
```

**Исправленный код:**
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
        avf_deactivated = False
        for attempt in range(max_avf_check_attempts):
            if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
                logger.warning(f"⚠️ [AVF] AVF все еще активен (попытка {attempt+1}/{max_avf_check_attempts})")
                await asyncio.sleep(0.2)
            else:
                logger.info(f"✅ [AVF] AVF полностью деактивирован (попытка {attempt+1})")
                avf_deactivated = True
                break
        
        if not avf_deactivated:
            logger.error("❌ [AVF] AVF не деактивирован после всех попыток - возможен конфликт с Google Speech Recognition")
            # ✅ КРИТИЧНО: Выбрасываем исключение для предотвращения конфликта
            raise RuntimeError("AVF not deactivated after all attempts - cannot activate Google Speech Recognition")
    
    # ✅ ИСПРАВЛЕНИЕ: Обязательная проверка разрешений (ошибка → исключение)
    try:
        from modules.permissions.core.permission_checker import PermissionChecker
        permission_checker = PermissionChecker()
        mic_permission = permission_checker.check_microphone_permission()
        logger.info(f"🔍 [Google] Проверка разрешений микрофона: {mic_permission}")
        if mic_permission != "granted":
            logger.error(f"❌ [Google] Разрешение микрофона не предоставлено: {mic_permission}")
            raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
    except RuntimeError:
        # Пробрасываем RuntimeError (отсутствие разрешений)
        raise
    except Exception as perm_error:
        # ✅ КРИТИЧНО: Пробрасываем любую ошибку проверки разрешений
        logger.error(f"❌ [Google] Критическая ошибка проверки разрешений: {perm_error}")
        raise RuntimeError(f"Microphone permission check failed: {perm_error}") from perm_error
    
    # Продолжаем активацию Google Speech Recognition...
```

**Что изменилось:**
- ✅ Добавлен цикл гарантированной деактивации AVF (5 попыток)
- ✅ Выбрасывается исключение, если AVF не деактивирован
- ✅ Обязательная проверка разрешений с пробросом исключений

#### Шаг 2.3: Проблема 3 — Разрешение активации через Shortcut

**Файл:** `integration/integrations/input_processing_integration.py`  
**Строка:** 1790-1814

**Текущий код (проблема):**
```python
async def _handle_long_press(self, event: KeyEvent):
    # ...
    if current_mode == AppMode.PROCESSING:
        if self._playback_active:  # ❌ Локальный флаг
            logger.warning("🔒 LONG_PRESS blocked...")
            return  # ❌ Блокируем ВСЕ активации
```

**Исправленный код (с использованием gateway):**
```python
async def _handle_long_press(self, event: KeyEvent):
    """Обработка длинного нажатия клавиши/комбинации"""
    try:
        logger.info(f"🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        
        # ✅ ИСПРАВЛЕНИЕ: Используем gateway для принятия решения
        # Это соответствует архитектуре проекта (gateways для принятия решений)
        from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
        from integration.core.selectors import (
            Snapshot, PermissionStatus, DeviceStatus, NetworkStatus,
            create_snapshot_from_state_manager
        )
        from integration.core.gateways.types import Decision
        
        # Создаем snapshot для gateway
        snapshot = create_snapshot_from_state_manager(self.state_manager)
        
        # Принимаем решение через gateway
        decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
        
        if decision == Decision.ABORT:
            logger.warning("🔒 LONG_PRESS blocked by gateway decision (automatic activation during PROCESSING)")
            async with self._state_lock:
                self._long_press_in_progress = False
            return
        
        # ✅ Разрешаем активацию через Shortcut для прерывания воспроизведения
        logger.info("✅ LONG_PRESS: разрешена активация микрофона (gateway decision: START)")
        
        # Принудительное закрытие микрофона перед новой записью
        mic_active = self.state_manager.is_microphone_active()  # ✅ Единый источник истины
        if mic_active:
            logger.warning(f"⚠️ LONG_PRESS: микрофон активен перед новой записью - принудительно закрываем")
            await self._publish_recording_stop_with_debounce({
                "source": "long_press_cleanup",
                "timestamp": event.timestamp,
                "session_id": None,
            })
            await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="LONG_PRESS")
        
        # Продолжаем активацию...
        # ...
```

**Создать новый gateway:**

**Файл:** `integration/core/gateways/audio_gateways.py` (новый файл)

```python
"""
Audio gateways for microphone activation decisions.
"""
from __future__ import annotations

import logging
from integration.core.selectors import Snapshot
from integration.core.gateways.types import Decision
from integration.core.state_manager import AppMode

logger = logging.getLogger(__name__)


def decide_allow_shortcut_during_processing(snapshot: Snapshot, source: str) -> Decision:
    """
    Решает, разрешена ли активация через Shortcut во время PROCESSING.
    
    Правило:
    - Разрешаем активацию через Shortcut ВСЕГДА (для прерывания воспроизведения)
    - Блокируем только автоматическую активацию (когда source != "keyboard")
    
    Args:
        snapshot: Снимок состояния системы
        source: Источник активации ("keyboard" для Shortcut, другие для автоматической)
    
    Returns:
        Decision.START - разрешить активацию
        Decision.ABORT - заблокировать активацию
    """
    if snapshot.app_mode == AppMode.PROCESSING:
        if source == "keyboard":
            # ✅ Разрешаем активацию через Shortcut для прерывания воспроизведения
            logger.info("✅ [AUDIO_GATEWAY] Разрешаем активацию через Shortcut во время PROCESSING (прерывание воспроизведения)")
            return Decision.START
        else:
            # ❌ Блокируем автоматическую активацию во время PROCESSING
            logger.warning("🔒 [AUDIO_GATEWAY] Блокируем автоматическую активацию во время PROCESSING")
            return Decision.ABORT
    
    # В других режимах разрешаем активацию
    return Decision.START
```

**Что изменилось:**
- ✅ Используется gateway для принятия решения (централизованная логика)
- ✅ Различается источник активации (keyboard vs автоматическая)
- ✅ Используется `state_manager.is_microphone_active()` (единый источник истины)

---

### Этап 3: Синхронизация локальных флагов с единым источником истины

**Цель:** Гарантировать, что локальные флаги синхронизированы с `ApplicationStateManager` при каждом изменении состояния.

#### Правило синхронизации:

**При каждом изменении состояния микрофона ОБЯЗАТЕЛЬНО обновлять ApplicationStateManager.**

#### Шаг 3.1: Синхронизация при активации микрофона

**Файл:** `integration/integrations/voice_recognition_integration.py`

**Текущий код:**
```python
async def _on_recording_start(self, event: Dict[str, Any]):
    # ...
    self._google_recording_active = True  # Локальный флаг
    # ...
    self.state_manager.set_microphone_state("active", session_id=session_id)  # ✅ Синхронизация
```

**Правило:** ✅ Уже синхронизировано — при установке `_google_recording_active = True` обновляется `state_manager`.

#### Шаг 3.2: Синхронизация при деактивации микрофона

**Файл:** `integration/integrations/voice_recognition_integration.py`

**Текущий код:**
```python
async def _on_recording_stop(self, event: Dict[str, Any]):
    # ...
    self._google_recording_active = False  # Локальный флаг
    # ...
    self.state_manager.set_microphone_state("idle", None)  # ✅ Синхронизация
```

**Правило:** ✅ Уже синхронизировано — при установке `_google_recording_active = False` обновляется `state_manager`.

#### Шаг 3.3: Синхронизация при ошибках

**Файл:** `integration/integrations/voice_recognition_integration.py`

**Исправленный код:**
```python
async def _on_recording_start(self, event: Dict[str, Any]):
    try:
        # ... активация микрофона ...
    except Exception as e:
        # ✅ КРИТИЧНО: Синхронизируем состояние при ошибке
        self._google_recording_active = False  # Локальный флаг
        self.state_manager.set_microphone_state("idle", None, reason="error")  # ✅ Синхронизация
        # ...
```

---

### Этап 4: Удаление проверок состояния через локальные флаги

**Цель:** Заменить все проверки состояния через локальные флаги на проверки через `ApplicationStateManager`.

#### Чек-лист замены:

- [ ] `if self._recording_started:` → `if self.state_manager.is_microphone_active():`
- [ ] `if self._playback_active:` → Использовать gateway для принятия решения
- [ ] `if self._google_recording_active:` → `if self.state_manager.is_microphone_active():`
- [ ] `if mic_active and self._recording_started:` → `if mic_active:` (убрать проверку локального флага)

---

## 📊 Схема: До и После централизации

### До централизации (проблема):

```
┌─────────────────────────────────────────────────────────────┐
│  InputProcessingIntegration                                 │
│                                                              │
│  if mic_active and self._recording_started:  ❌            │
│      # Использует два источника истины                      │
│      # Могут быть рассинхронизированы                       │
└─────────────────────────────────────────────────────────────┘
```

### После централизации (решение):

```
┌─────────────────────────────────────────────────────────────┐
│  InputProcessingIntegration                                 │
│                                                              │
│  mic_active = self.state_manager.is_microphone_active()  ✅│
│  if mic_active:  ✅                                         │
│      # Использует только единый источник истины            │
│      # Всегда синхронизировано                             │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ Чек-лист централизации

### Перед началом:
- [ ] Провести аудит всех проверок состояния через локальные флаги
- [ ] Составить список мест для замены
- [ ] Определить, какие локальные флаги можно оставить (только для внутренней логики)

### Во время реализации:
- [ ] Заменить все проверки состояния на `state_manager.is_microphone_active()`
- [ ] Гарантировать синхронизацию при каждом изменении состояния
- [ ] Использовать gateways для принятия решений (где необходимо)
- [ ] Добавить обязательные проверки с исключениями (AVF, разрешения)

### После реализации:
- [ ] Создать изолированные тесты для проверки синхронизации
- [ ] Запустить существующие тесты для проверки регрессий
- [ ] Проверить, что все компоненты используют единый источник истины

---

## 🎯 Правила использования

### Правило 1: Чтение состояния

**ВСЕГДА используйте `state_manager.is_microphone_active()` для проверки состояния микрофона.**

```python
# ✅ ПРАВИЛЬНО
if self.state_manager.is_microphone_active():
    # ...

# ❌ НЕПРАВИЛЬНО
if self._recording_started:  # Локальный флаг
    # ...
```

### Правило 2: Запись состояния

**ВСЕГДА обновляйте `state_manager.set_microphone_state()` при изменении состояния микрофона.**

```python
# ✅ ПРАВИЛЬНО
self._google_recording_active = True  # Локальный флаг (для внутренней логики)
self.state_manager.set_microphone_state("active", session_id=session_id)  # ✅ Синхронизация

# ❌ НЕПРАВИЛЬНО
self._google_recording_active = True  # Только локальный флаг, без синхронизации
```

### Правило 3: Локальные флаги

**Локальные флаги используются ТОЛЬКО для внутренней логики, НЕ для проверок состояния.**

```python
# ✅ ПРАВИЛЬНО: Локальный флаг для внутренней логики
self._recording_started = True  # Для отслеживания публикации voice.recording_start
# Проверка состояния через единый источник:
if self.state_manager.is_microphone_active():
    # ...

# ❌ НЕПРАВИЛЬНО: Локальный флаг для проверки состояния
if self._recording_started:  # Локальный флаг
    # ...
```

### Правило 4: Принятие решений

**Используйте gateways для принятия решений на основе множественных осей состояния.**

```python
# ✅ ПРАВИЛЬНО: Использование gateway
from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
if decision == Decision.ABORT:
    return

# ❌ НЕПРАВИЛЬНО: Решение на основе локального флага
if self._playback_active:  # Локальный флаг
    return
```

---

## 📝 Примеры правильной реализации

### Пример 1: Проверка состояния микрофона

```python
# ✅ ПРАВИЛЬНО
async def _on_playback_finished(self, event):
    # Используем только единый источник истины
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:
        # Принудительно закрываем микрофон
        self.state_manager.force_close_microphone(reason="playback_completed")
        await self._publish_recording_stop_with_debounce({...})
```

### Пример 2: Синхронизация при активации

```python
# ✅ ПРАВИЛЬНО
async def _on_recording_start(self, event):
    # 1. Обновляем локальный флаг (для внутренней логики)
    self._google_recording_active = True
    
    # 2. ОБЯЗАТЕЛЬНО: Обновляем единый источник истины
    self.state_manager.set_microphone_state("active", session_id=session_id)
    
    # 3. Публикуем событие
    await self.event_bus.publish("microphone.opened", {...})
```

### Пример 3: Принятие решения через gateway

```python
# ✅ ПРАВИЛЬНО
async def _handle_long_press(self, event):
    # Создаем snapshot для gateway
    snapshot = create_snapshot_from_state_manager(self.state_manager)
    
    # Принимаем решение через gateway
    decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
    
    if decision == Decision.ABORT:
        return
    
    # Продолжаем активацию...
```

---

## 🔍 Диагностика рассинхронизации

### Как проверить, что состояние синхронизировано:

```python
# Проверка синхронизации
def check_microphone_state_sync(self):
    """Проверяет синхронизацию состояния микрофона"""
    state_manager_active = self.state_manager.is_microphone_active()
    local_flag_active = self._recording_started  # Локальный флаг
    
    if state_manager_active != local_flag_active:
        logger.warning(
            f"⚠️ РАССИНХРОНИЗАЦИЯ: state_manager={state_manager_active}, "
            f"local_flag={local_flag_active}"
        )
        # Принудительная синхронизация
        if state_manager_active:
            self._recording_started = True
        else:
            self._recording_started = False
```

---

## Связанные документы

- `Docs/SYNC_PROBLEM_VISUAL_DIAGRAM.md` — визуальная схема проблемы
- `Docs/ROOT_CAUSE_ANALYSIS.md` — анализ корневой причины
- `Docs/SOLUTIONS_IMPLEMENTATION_PLAN.md` — план реализации решений
