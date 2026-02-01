# Финальное руководство: Решения проблем активации микрофона

## Дата создания
2025-01-XX

## Обзор

Этот документ содержит **финальные рекомендации** по решению трех проблем активации микрофона на основе тестирования и анализа.

---

## 🎯 Итоговые решения (на основе тестирования)

### ✅ Решение 1: Микрофон не закрывается после playback.completed

**Рекомендуемый вариант:** **Вариант 1.3 (Комбинированный подход)** ⭐

**Почему этот вариант:**
- ✅ Гарантирует закрытие микрофона (принудительное + событие)
- ✅ Синхронизируется с VoiceRecognitionIntegration
- ✅ Использует единый источник истины
- ✅ Нет задержек

**Код:**
```python
async def _on_playback_finished(self, event):
    # ✅ Принудительно закрываем микрофон, если он активен
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:
        logger.warning("⚠️ PLAYBACK: микрофон активен - принудительно закрываем")
        # ✅ Принудительно закрываем через state_manager (единый источник истины)
        self.state_manager.force_close_microphone(reason="playback_completed")
        # ✅ Публикуем событие для синхронизации с VoiceRecognitionIntegration
        await self._publish_recording_stop_with_debounce({
            "source": "playback_finished",
            "session_id": None,
        })
        # ✅ Ждём закрытия для гарантии
        await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="playback_finished")
```

**Файл:** `integration/integrations/input_processing_integration.py:859-875`

**Тест:** `test_solution_1_3_combined` ✅ ПРОЙДЕН

---

### ✅ Решение 2: AVF не деактивируется, разрешения пропущены

**Рекомендуемый вариант:** **Вариант 2.1 + 2.2 (Оба варианта)** ⭐

**Почему эти варианты:**
- ✅ Вариант 2.1 гарантирует деактивацию AVF (5 попыток)
- ✅ Вариант 2.2 гарантирует проверку разрешений (обязательная)
- ✅ Оба простые и не конфликтуют

**Код 2.1 (AVF деактивация):**
```python
# Гарантированная деактивация AVF (5 попыток)
max_avf_check_attempts = 5
for attempt in range(max_avf_check_attempts):
    if hasattr(self._avf_engine, 'is_input_active') and self._avf_engine.is_input_active:
        logger.warning(f"⚠️ [AVF] AVF все еще активен (попытка {attempt+1}/{max_avf_check_attempts})")
        await asyncio.sleep(0.2)
    else:
        logger.info(f"✅ [AVF] AVF полностью деактивирован (попытка {attempt+1})")
        break
else:
    logger.error("❌ [AVF] AVF не деактивирован после всех попыток")
    raise RuntimeError("AVF not deactivated after all attempts")
```

**Код 2.2 (Проверка разрешений):**
```python
# Обязательная проверка разрешений (ошибка → исключение)
try:
    from modules.permissions.core.permission_checker import PermissionChecker
    permission_checker = PermissionChecker()
    mic_permission = permission_checker.check_microphone_permission()
    if mic_permission != "granted":
        raise RuntimeError(f"Microphone permission not granted: {mic_permission}")
except RuntimeError:
    raise  # Пробрасываем RuntimeError
except Exception as perm_error:
    raise RuntimeError(f"Permission check failed: {perm_error}") from perm_error
```

**Файл:** `integration/integrations/voice_recognition_integration.py:842-847, 854-864`

**Тесты:** 
- `test_solution_2_1_avf_retry_loop` ✅ ПРОЙДЕН
- `test_solution_2_2_permission_check_required` ✅ ПРОЙДЕН

---

### ✅ Решение 3: LONG_PRESS блокируется во время PROCESSING

**Рекомендуемый вариант:** **Вариант 3.3 (Использовать gateway)** ⭐

**Почему этот вариант:**
- ✅ Соответствует архитектуре проекта (gateways для принятия решений)
- ✅ Централизованная логика принятия решений
- ✅ Легко тестировать и расширять
- ✅ Различает источник активации (keyboard vs автоматическая)

**Код:**

**Шаг 1: Создать gateway**
```python
# integration/core/gateways/audio_gateways.py
from integration.core.selectors import Snapshot
from integration.core.gateways.types import Decision
from integration.core.state_manager import AppMode

def decide_allow_shortcut_during_processing(snapshot: Snapshot, source: str) -> Decision:
    """
    Решает, разрешена ли активация через Shortcut во время PROCESSING.
    
    Правило:
    - Разрешаем активацию через Shortcut ВСЕГДА (для прерывания воспроизведения)
    - Блокируем только автоматическую активацию (когда source != "keyboard")
    """
    if snapshot.app_mode == AppMode.PROCESSING:
        if source == "keyboard":
            return Decision.START  # Разрешаем для прерывания
        else:
            return Decision.ABORT  # Блокируем автоматическую активацию
    return Decision.START
```

**Шаг 2: Использовать в _handle_long_press()**
```python
async def _handle_long_press(self, event: KeyEvent):
    # ✅ Используем gateway для принятия решения
    from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
    from integration.core.selectors import create_snapshot_from_state
    from integration.core.gateways.types import Decision
    
    # Создаем snapshot для gateway (используем существующую функцию)
    snapshot = create_snapshot_from_state(self.state_manager)
    decision = decide_allow_shortcut_during_processing(snapshot, source="keyboard")
    
    if decision == Decision.ABORT:
        logger.warning("🔒 LONG_PRESS blocked by gateway decision")
        self._long_press_in_progress = False
        return
    
    # ✅ Разрешаем активацию через Shortcut для прерывания воспроизведения
    logger.info("✅ LONG_PRESS: разрешена активация микрофона (gateway decision: START)")
    
    # Принудительное закрытие микрофона перед новой записью
    mic_active = self.state_manager.is_microphone_active()
    if mic_active:
        logger.warning("⚠️ LONG_PRESS: микрофон активен - принудительно закрываем")
        await self._publish_recording_stop_with_debounce({...})
        await self._wait_for_mic_closed_with_timeout(timeout=1.0, source="LONG_PRESS")
    
    # Продолжаем активацию...
```

**Файл:** 
- Новый: `integration/core/gateways/audio_gateways.py`
- Изменение: `integration/integrations/input_processing_integration.py:1790-1814`

**Тест:** `test_solution_3_3_use_gateway` ✅ ПРОЙДЕН

---

## 📊 Результаты тестирования всех вариантов

### Проблема 1: Тесты вариантов

| Вариант | Гарантия закрытия | Синхронизация | Единый источник | Тест | Рекомендация |
|---------|------------------|---------------|-----------------|------|--------------|
| 1.1: Принудительное | ✅ | ❌ | ✅ | ✅ | ❌ |
| 1.2: Публикация + ожидание | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| 1.3: Комбинированный ⭐ | ✅ | ✅ | ✅ | ✅ | ✅ **ЛУЧШИЙ** |

### Проблема 2: Тесты вариантов

| Вариант | Гарантия AVF | Гарантия разрешений | Тест | Рекомендация |
|---------|--------------|---------------------|------|--------------|
| 2.1: Цикл проверки AVF ⭐ | ✅ | - | ✅ | ✅ **ЛУЧШИЙ** |
| 2.2: Обязательная проверка разрешений ⭐ | - | ✅ | ✅ | ✅ **ЛУЧШИЙ** |

**Вывод:** Оба варианта нужны и не конфликтуют.

### Проблема 3: Тесты вариантов

| Вариант | Разрешает Shortcut | Блокирует автоматическую | Архитектура | Тест | Рекомендация |
|---------|-------------------|-------------------------|-------------|------|--------------|
| 3.1: Убрать блокировку | ✅ | ❌ | ❌ | ✅ | ❌ |
| 3.2: Разрешить только keyboard | ✅ | ✅ | ⚠️ | ✅ | ⚠️ |
| 3.3: Использовать gateway ⭐ | ✅ | ✅ | ✅ | ✅ | ✅ **ЛУЧШИЙ** |

---

## 🎯 План реализации (детальный)

### Этап 1: Исправление Проблемы 1 (1 час)

**Файл:** `integration/integrations/input_processing_integration.py`

**Изменение в `_on_playback_finished()` (строка 859-875):**

```python
async def _on_playback_finished(self, event):
    """Обрабатывает завершение воспроизведения (completed/cancelled/failed) и сбрасывает сессию."""
    try:
        data = (event or {}).get("data", {}) or {}
        event_session_id = data.get("session_id")
        event_type = (event or {}).get("type", "unknown")
        logger.debug("PLAYBACK: finished (event=%s, session=%s)", event_type, event_session_id)
        
        active_session_id = self._get_active_session_id()
        
        # ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 1: Принудительно закрываем микрофон, если он активен
        # Это гарантирует, что микрофон не останется активным после playback.completed
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
        if mic_active and self._recording_started:
            logger.warning(f"⚠️ PLAYBACK: микрофон активен с новой записью (_recording_started=True) - НЕ сбрасываем session_id")
            # ... остальная логика ...
            return
        
        # ... остальной код ...
```

**Тестирование:**
- Запустить: `pytest tests/test_solution_options.py::TestProblem1Solutions::test_solution_1_3_combined -v`
- Проверить: микрофон закрывается корректно

---

### Этап 2: Исправление Проблемы 2 (45 минут)

**Файл:** `integration/integrations/voice_recognition_integration.py`

**Изменение 1: AVF деактивация (строка 842-847):**

```python
# ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 2.1: Гарантированная деактивация AVF (5 попыток)
if self._use_avf and self._avf_engine is not None:
    # ... существующий код AVF диагностики ...
    await self._avf_engine.stop_input()
    await asyncio.sleep(0.2)
    
    # ✅ Гарантированная деактивация AVF (5 попыток)
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
        raise RuntimeError("AVF not deactivated after all attempts - cannot activate Google Speech Recognition")
```

**Изменение 2: Проверка разрешений (строка 854-864):**

```python
# ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 2.2: Обязательная проверка разрешений (ошибка → исключение)
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
    # ✅ Пробрасываем любую ошибку проверки разрешений
    logger.error(f"❌ [Google] Критическая ошибка проверки разрешений: {perm_error}")
    raise RuntimeError(f"Microphone permission check failed: {perm_error}") from perm_error
```

**Тестирование:**
- Запустить: `pytest tests/test_solution_options.py::TestProblem2Solutions -v`
- Проверить: AVF деактивируется, разрешения проверяются

---

### Этап 3: Исправление Проблемы 3 (1-2 часа)

**Шаг 1: Создать gateway**

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

**Шаг 2: Обновить __init__.py**

**Файл:** `integration/core/gateways/__init__.py`

```python
# Добавить экспорт нового gateway
from .audio_gateways import decide_allow_shortcut_during_processing

__all__ = [
    # ... существующие экспорты ...
    'decide_allow_shortcut_during_processing',
]
```

**Шаг 3: Использовать в _handle_long_press()**

**Файл:** `integration/integrations/input_processing_integration.py:1790-1814`

```python
async def _handle_long_press(self, event: KeyEvent):
    """Обработка длинного нажатия клавиши/комбинации"""
    try:
        logger.info(f"🎤 _handle_long_press ВЫЗВАН! duration={event.duration:.3f}s")
        
        # ✅ ИСПРАВЛЕНИЕ ПРОБЛЕМЫ 3: Используем gateway для принятия решения
        # Это соответствует архитектуре проекта (gateways для принятия решений)
        from integration.core.gateways.audio_gateways import decide_allow_shortcut_during_processing
        from integration.core.selectors import create_snapshot_from_state
        from integration.core.gateways.types import Decision
        
        # Создаем snapshot для gateway (используем существующую функцию)
        snapshot = create_snapshot_from_state(self.state_manager)
        
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
        # ... остальной код ...
```

**Тестирование:**
- Запустить: `pytest tests/test_solution_options.py::TestProblem3Solutions::test_solution_3_3_use_gateway -v`
- Проверить: активация разрешена через Shortcut, блокируется автоматическая

---

## 📋 Итоговый чек-лист реализации

### Перед началом:

- [ ] Прочитать `Docs/PRE_CHANGE_PLANNING_CHECKLIST.md` и пройти этапы 1-6
- [ ] Создать Impact Map
- [ ] Создать `.impact/change_impact.yaml`
- [ ] Запустить автоматические проверки:
  - `python scripts/validate_microphone_state_source.py`
  - `python scripts/validate_microphone_thread_safety.py`
  - `python scripts/validate_microphone_sync.py`

### Реализация (Приоритет 1):

- [ ] **Исправить Проблему 1:** Вариант 1.3 (Комбинированный подход)
  - Файл: `integration/integrations/input_processing_integration.py:859-875`
  - Тест: `test_solution_1_3_combined` ✅

- [ ] **Исправить Проблему 2:** Варианты 2.1 + 2.2 (AVF + разрешения)
  - Файл: `integration/integrations/voice_recognition_integration.py:842-847, 854-864`
  - Тесты: `test_solution_2_1_avf_retry_loop` ✅, `test_solution_2_2_permission_check_required` ✅

- [ ] **Исправить Проблему 3:** Вариант 3.3 (Использовать gateway)
  - Новый файл: `integration/core/gateways/audio_gateways.py`
  - Изменение: `integration/integrations/input_processing_integration.py:1790-1814`
  - Тест: `test_solution_3_3_use_gateway` ✅

### После реализации:

- [ ] Запустить изолированные тесты: `pytest tests/test_solution_options.py -v`
- [ ] Запустить автоматические проверки:
  - `python scripts/validate_microphone_state_source.py`
  - `python scripts/validate_microphone_thread_safety.py`
  - `python scripts/validate_microphone_sync.py`
- [ ] Запустить существующие тесты для проверки регрессий
- [ ] Запустить `scripts/pre_build_gate.sh`

---

## 📊 Оценка времени и сложности

| Этап | Время | Сложность | Риск |
|------|-------|-----------|------|
| Исправление Проблемы 1 | 1 час | Средний | Низкий |
| Исправление Проблемы 2 | 45 минут | Простой | Низкий |
| Исправление Проблемы 3 | 1-2 часа | Средний | Низкий |
| **ИТОГО (Приоритет 1)** | **2.5-3.5 часа** | **Средний** | **Низкий** |

---

## Связанные документы

- `Docs/SOLUTION_OPTIONS_ANALYSIS.md` — анализ всех вариантов решений
- `Docs/BEST_SOLUTIONS_RECOMMENDATION.md` — рекомендации по лучшим решениям
- `tests/test_solution_options.py` — изолированные тесты вариантов решений
- `Docs/ANALYSIS_SUMMARY.md` — итоговый отчет анализа

