# Пошаговый план исправления проблем активации микрофона

## Дата создания
2025-01-XX

## Обзор

Этот документ содержит **пошаговый план** исправления всех найденных проблем с конкретными изменениями кода и проверками.

---

## 🎯 Принципы исправления

1. ✅ **Единый источник истины** — все проверки через `state_manager.is_microphone_active()`
2. ✅ **Синхронизация** — все изменения состояния через `state_manager.set_microphone_state()`
3. ✅ **Thread-safety** — все операции thread-safe (уже соблюдается)
4. ✅ **Изоляция и тестирование** — изолированные тесты для каждого исправления

---

## 📋 Этап 1: Критические исправления (3 проблемы пользователя)

### Исправление 1.1: Принудительное закрытие микрофона после playback.completed

**Файл:** `integration/integrations/input_processing_integration.py`  
**Метод:** `_on_playback_finished()`  
**Строка:** 859-875

**Текущий код (проблема):**
```python
mic_active = self.state_manager.is_microphone_active()
if mic_active and self._recording_started:  # ❌ Смешанная проверка
    logger.warning(f"⚠️ PLAYBACK: микрофон активен с новой записью...")
    return  # ❌ ВЫХОДИМ, НЕ ЗАКРЫВАЯ МИКРОФОН!
```

**Исправленный код:**
```python
async def _on_playback_finished(self, event):
    """Обрабатывает завершение воспроизведения (completed/cancelled/failed) и сбрасывает сессию."""
    try:
        data = (event or {}).get("data", {}) or {}
        event_session_id = data.get("session_id")
        event_type = (event or {}).get("type", "unknown")
        logger.debug("PLAYBACK: finished (event=%s, session=%s)", event_type, event_session_id)
        
        active_session_id = self._get_active_session_id()
        
        # ✅ ИСПРАВЛЕНИЕ 1.1: Принудительно закрываем микрофон, если он активен
        # Используем ТОЛЬКО единый источник истины (state_manager)
        mic_active = self.state_manager.is_microphone_active()
        if mic_active:
            logger.warning(f"⚠️ PLAYBACK: микрофон активен после playback.completed - принудительно закрываем")
            # ✅ Используем существующий метод force_close_microphone (единый источник истины)
            self.state_manager.force_close_microphone(reason="playback_completed")
            # ✅ Публикуем voice.recording_stop для синхронизации с VoiceRecognitionIntegration
            await self._publish_recording_stop_with_debounce({
                "source": "playback_finished",
                "timestamp": time.time(),
                "session_id": None,  # Закрываем любой активный микрофон
            })
            # ✅ Ждём закрытия микрофона для гарантии
            await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
        
        # ✅ КРИТИЧНО: Проверяем, не активен ли микрофон с новой сессией
        # Если микрофон активен и _recording_started=True, значит LONG_PRESS уже активировал новую запись
        # В этом случае НЕ сбрасываем session_id, чтобы не потерять новую сессию
        # ✅ ИСПРАВЛЕНИЕ: Используем ТОЛЬКО state_manager для проверки, НЕ локальный флаг
        if mic_active:
            # Проверяем, есть ли новая запись (через state_manager, не локальный флаг)
            # _recording_started используется только для отслеживания публикации, не для проверок
            if self._recording_started:
                logger.warning(f"⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id")
                # ✅ КРИТИЧНО: НЕ сбрасываем _playback_active, если событие - playback.cancelled
                if event_type != "playback.cancelled":
                    pattern = data.get("pattern", "")
                    is_system = (
                        pattern in {"welcome_message", "signal"} or
                        (event_session_id and ("welcome_message" in str(event_session_id).lower() or "signal" in str(event_session_id).lower()))
                    )
                    self._notify_playback_idle(is_system_playback=is_system)
                else:
                    logger.warning(f"⚠️ PLAYBACK: playback.cancelled с активным микрофоном - НЕ сбрасываем _playback_active")
                return
        
        # Остальная логика сброса сессии...
        # ...
```

**Что изменилось:**
- ✅ Убрана смешанная проверка `if mic_active and self._recording_started:`
- ✅ Добавлено принудительное закрытие микрофона через `force_close_microphone()`
- ✅ Используется только `state_manager.is_microphone_active()` для проверки состояния
- ✅ Локальный флаг `_recording_started` используется только для отслеживания, не для проверок

**Проверка после исправления:**
```bash
python scripts/validate_microphone_state_source.py --file integration/integrations/input_processing_integration.py
# Должно показать меньше нарушений
```

---

### Исправление 1.2: Гарантированная деактивация AVF и проверка разрешений

**Файл:** `integration/integrations/voice_recognition_integration.py`  
**Метод:** `_on_recording_start()`  
**Строки:** 842-847 (AVF), 854-864 (разрешения)

**Текущий код (проблема AVF):**
```python
if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
    logger.warning("⚠️ [AVF] AVF все еще активен...")
    await asyncio.sleep(0.5)  # Одна попытка
    if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
        logger.error("❌ [AVF] AVF все еще активен...")
        # ❌ ПРОБЛЕМА: Продолжаем работу, не выбрасывая исключение!
```

**Исправленный код (AVF):**
```python
if self._use_avf and self._avf_engine is not None:
    # AVF диагностика...
    await self._avf_engine.start_input()
    await asyncio.sleep(1.0)
    await self._avf_engine.stop_input()
    await asyncio.sleep(0.2)
    
    # ✅ ИСПРАВЛЕНИЕ 1.2: Гарантированная деактивация AVF (5 попыток)
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
```

**Текущий код (проблема разрешений):**
```python
try:
    mic_permission = permission_checker.check_microphone_permission()
    if mic_permission != "granted":
        raise RuntimeError("...")
except Exception as perm_error:
    logger.warning("⚠️ Не удалось проверить разрешения...")
    # ❌ ПРОБЛЕМА: Продолжаем работу, не выбрасывая исключение!
```

**Исправленный код (разрешения):**
```python
# ✅ ИСПРАВЛЕНИЕ 1.2: Обязательная проверка разрешений (ошибка → исключение)
try:
    from modules.permissions.core.permission_checker import PermissionChecker
    permission_checker = PermissionChecker()
    mic_permission = permission_checker.check_microphone_permission()
    logger.info(f"🔍 [Google] Проверка разрешений микрофона: {mic_permission}")
    if mic_permission != "granted":
        logger.error(f"❌ [Google] Разрешение микрофона не предоставлено: {mic_permission}")
        raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
except RuntimeError:
    # ✅ Пробрасываем RuntimeError (отсутствие разрешений)
    raise
except Exception as perm_error:
    # ✅ КРИТИЧНО: Пробрасываем любую ошибку проверки разрешений
    logger.error(f"❌ [Google] Критическая ошибка проверки разрешений: {perm_error}")
    raise RuntimeError(f"Microphone permission check failed: {perm_error}") from perm_error
```

**Что изменилось:**
- ✅ Гарантированная деактивация AVF (5 попыток вместо 1)
- ✅ Выброс исключения при неудачной деактивации AVF
- ✅ Обязательная проверка разрешений с выбросом исключения при ошибке

---

### Исправление 1.3: Разрешение активации через Shortcut во время PROCESSING

**Файл 1:** `integration/core/gateways/audio_gateways.py` (новый файл)

**Создать новый gateway:**
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

**Файл 2:** `integration/integrations/input_processing_integration.py`  
**Метод:** `_handle_long_press()`  
**Строка:** 1790-1814

**Текущий код (проблема):**
```python
if current_mode == AppMode.PROCESSING:
    if self._playback_active or is_playback_recently_started:
        logger.warning("🔒 LONG_PRESS blocked...")
        # ❌ ПРОБЛЕМА: Блокируем ВСЕ активации, включая пользовательские!
        self._long_press_in_progress = False
        return  # ❌ ВЫХОДИМ, НЕ АКТИВИРУЯ МИКРОФОН!
```

**Исправленный код:**
```python
async def _handle_long_press(self, event: KeyEvent):
    """Обработка длинного нажатия клавиши/комбинации"""
    try:
        logger.info(f"🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        
        # ✅ ИСПРАВЛЕНИЕ 1.3: Используем gateway для принятия решения
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
        
        # ✅ ЭТАП 0.3: Атомарная проверка-и-установка для защиты от повторных LONG_PRESS
        async with self._state_lock:
            if self._long_press_in_progress:
                logger.warning("⚠️ LONG_PRESS уже выполняется, игнорируем повторный вызов")
                return
            self._long_press_in_progress = True
        
        # ✅ ИСПРАВЛЕНИЕ: Принудительное закрытие микрофона перед новой записью
        # Используем ТОЛЬКО единый источник истины
        mic_active = self.state_manager.is_microphone_active()
        if mic_active:
            logger.warning(f"⚠️ LONG_PRESS: микрофон активен перед новой записью - принудительно закрываем")
            await self._publish_recording_stop_with_debounce({
                "source": "long_press_cleanup",
                "timestamp": event.timestamp,
                "session_id": None,  # Закрываем любой активный микрофон
            })
            # Ждём закрытия с увеличенным таймаутом
            closed = await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="LONG_PRESS")
            if not closed:
                logger.error("❌ LONG_PRESS: микрофон не закрылся после принудительной остановки - возможна проблема")
                # Продолжаем, но логируем ошибку
        
        # Продолжаем активацию...
        # ...
```

**Что изменилось:**
- ✅ Убрана блокировка всех активаций во время PROCESSING
- ✅ Добавлен gateway для принятия решения
- ✅ Разрешена активация через Shortcut для прерывания воспроизведения
- ✅ Используется только `state_manager.is_microphone_active()` для проверки состояния

**Обновить:** `integration/core/gateways/__init__.py`
```python
from .audio_gateways import decide_allow_shortcut_during_processing

__all__ = [
    # ... существующие экспорты ...
    'decide_allow_shortcut_during_processing',
]
```

---

## 📋 Этап 2: Устранение нарушений автопроверок

### Исправление 2.1: Замена локальных флагов на state_manager (10+ нарушений)

**Файл:** `integration/integrations/input_processing_integration.py`

**Найденные нарушения:**
1. Строка 534: `if self._recording_started:`
2. Строка 649: `if self._playback_active:`
3. Строка 784: `if self._recording_started:`
4. Строка 860: `if mic_active and self._recording_started:` (уже исправлено в 1.1)
5. Строка 963: `if self._recording_started:`
6. Строка 986: `if self._recording_started:`
7. Строка 1112: `if self._playback_active:`
8. И другие...

**Правило замены:**
```python
# ❌ НЕПРАВИЛЬНО (локальный флаг для проверки состояния)
if self._recording_started:
    # ...

# ✅ ПРАВИЛЬНО (единый источник истины)
if self.state_manager.is_microphone_active():
    # ...

# ✅ ПРАВИЛЬНО (локальный флаг только для отслеживания)
self._recording_started = True  # Для отслеживания публикации voice.recording_start
# НЕ используется для проверок состояния!
```

**Конкретные замены:**

**Строка 534:**
```python
# ❌ БЫЛО:
if self._recording_started:

# ✅ СТАЛО:
if self.state_manager.is_microphone_active():
```

**Строка 649:**
```python
# ❌ БЫЛО:
if self._playback_active:

# ✅ СТАЛО:
# Проверяем через state_manager или другие механизмы
# _playback_active используется только для отслеживания воспроизведения
```

**И так далее для всех найденных нарушений...**

**Проверка после исправления:**
```bash
python scripts/validate_microphone_state_source.py --file integration/integrations/input_processing_integration.py
# Должно показать 0 нарушений
```

---

### Исправление 2.2: Добавление синхронизации state_manager (21+ нарушение)

**Файл:** `integration/integrations/input_processing_integration.py`

**Найденные нарушения:**
1. Строка 505: `voice.recording_stop` публикуется, но `state_manager` не обновляется
2. Строка 508: `voice.recording_stop` опубликовано, но `state_manager` не обновляется
3. И другие...

**Правило синхронизации:**
```python
# ✅ ПРАВИЛЬНО: После публикации события обновляем state_manager
await self.event_bus.publish("voice.recording_stop", data)
# ✅ Синхронизация с state_manager
self.state_manager.set_microphone_state("idle", None, reason="voice_recording_stop")
```

**Конкретные исправления:**

**Строка 505 (`_publish_recording_stop_with_debounce`):**
```python
async def _publish_recording_stop_with_debounce(self, data: Dict[str, Any]):
    """Публикует voice.recording_stop с debounce."""
    # ... существующий код debounce ...
    
    await self.event_bus.publish("voice.recording_stop", data)
    
    # ✅ ИСПРАВЛЕНИЕ 2.2: Синхронизация с state_manager
    # VoiceRecognitionIntegration обновит state_manager при обработке события,
    # но для гарантии синхронизации обновляем здесь тоже
    if self.state_manager.is_microphone_active():
        self.state_manager.set_microphone_state("idle", None, reason="voice_recording_stop_published")
    
    logger.debug(f"✅ [DEBOUNCE] voice.recording_stop опубликовано (session_id={data.get('session_id')})")
```

**Проверка после исправления:**
```bash
python scripts/validate_microphone_sync.py --file integration/integrations/input_processing_integration.py
# Должно показать меньше нарушений
```

---

## 📋 Этап 3: Тестирование и проверка

### Шаг 3.1: Изолированные тесты

**Создать/обновить тесты:**

1. **Тест для проблемы 1:**
```python
# tests/test_microphone_activation_issues_isolation.py
async def test_problem1_microphone_closed_after_playback_completed():
    """Изолированный тест: проверяем, что микрофон закрывается после playback.completed"""
    # ... тест из существующего файла ...
```

2. **Тест для проблемы 2:**
```python
async def test_problem2_avf_deactivation_guaranteed():
    """Изолированный тест: проверяем гарантированную деактивацию AVF"""
    # ... новый тест ...
```

3. **Тест для проблемы 3:**
```python
async def test_problem3_long_press_allowed_during_processing():
    """Изолированный тест: проверяем, что LONG_PRESS разрешен во время PROCESSING"""
    # ... тест из существующего файла ...
```

### Шаг 3.2: Запуск автоматических проверок

```bash
# Проверка единого источника истины
python scripts/validate_microphone_state_source.py

# Проверка thread-safety
python scripts/validate_microphone_thread_safety.py

# Проверка синхронизации
python scripts/validate_microphone_sync.py
```

### Шаг 3.3: Запуск существующих тестов

```bash
# Изолированные тесты
pytest tests/test_microphone_activation_issues_isolation.py -v

# Другие тесты
pytest tests/test_microphone_activation.py -v
pytest tests/test_interrupt_playback.py -v
```

---

## 📋 Чек-лист реализации

### Перед началом:
- [ ] Прочитать `Docs/PRE_CHANGE_PLANNING_CHECKLIST.md` и пройти этапы 1-6
- [ ] Создать Impact Map с таблицей влияния
- [ ] Создать `.impact/change_impact.yaml`
- [ ] Обновить `Docs/STATE_CATALOG.md` (если добавляются новые оси)

### Этап 1: Критические исправления
- [ ] Исправить `_on_playback_finished()` — принудительное закрытие микрофона
- [ ] Улучшить деактивацию AVF — гарантированная деактивация (5 попыток)
- [ ] Улучшить проверку разрешений — обязательная проверка (ошибка → исключение)
- [ ] Создать gateway `decide_allow_shortcut_during_processing`
- [ ] Исправить `_handle_long_press()` — использовать gateway для принятия решения

### Этап 2: Устранение нарушений автопроверок
- [ ] Заменить локальные флаги на state_manager (10+ мест)
- [ ] Добавить синхронизацию state_manager (21+ место)

### Этап 3: Тестирование
- [ ] Создать изолированные тесты для каждого исправления
- [ ] Запустить автоматические проверки (все должны пройти)
- [ ] Запустить существующие тесты (проверка регрессий)
- [ ] Запустить `scripts/pre_build_gate.sh` для проверки всех обязательных проверок

### После реализации:
- [ ] Обновить документацию (если нужно)
- [ ] Запустить `scripts/validate_microphone_state_source.py` — должно быть 0 нарушений
- [ ] Запустить `scripts/validate_microphone_sync.py` — должно быть 0 нарушений
- [ ] Проверить, что все компоненты используют единый источник истины

---

## 🎯 Порядок реализации (рекомендуемый)

### Фаза 1: Критические исправления (1-2 часа)
1. Исправление 1.1: Принудительное закрытие микрофона
2. Исправление 1.2: Гарантированная деактивация AVF и проверка разрешений
3. Исправление 1.3: Разрешение активации через Shortcut

### Фаза 2: Устранение нарушений (2-3 часа)
1. Исправление 2.1: Замена локальных флагов на state_manager
2. Исправление 2.2: Добавление синхронизации state_manager

### Фаза 3: Тестирование (1-2 часа)
1. Изолированные тесты
2. Автоматические проверки
3. Существующие тесты

**Общее время:** 4-7 часов

---

## Связанные документы

- `Docs/SOLUTIONS_IMPLEMENTATION_PLAN.md` — детальный план реализации
- `Docs/ANALYSIS_SUMMARY.md` — итоговый отчет анализа
- `Docs/CENTRALIZATION_SYNC_VISUAL_GUIDE.md` — визуальное руководство по централизации
