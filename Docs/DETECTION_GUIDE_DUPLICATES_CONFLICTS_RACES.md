# 🔍 Инструкция по выявлению дублирования, конфликтов и race conditions

**ЦЕЛЬ**: Предоставить конкретные методы, команды и примеры для правильного выявления дублирования кода, конфликтов и race conditions.

**ВАЖНО**: Эта инструкция используется ассистентом при выполнении проверок из раздела 11.2 `.cursorrules` и `DUPLICATE_CONFLICT_RACE_PREVENTION_CHECKLIST.md`.

**Дата создания**: 2025-01-XX  
**Версия**: 1.0

---

## 📋 Содержание

1. [Выявление дублирования кода](#1-выявление-дублирования-кода)
2. [Выявление конфликтов](#2-выявление-конфликтов)
3. [Выявление race conditions](#3-выявление-race-conditions)
4. [Автоматизированные проверки](#4-автоматизированные-проверки)
5. [Чек-лист проверки](#5-чек-лист-проверки)

---

## 1. Выявление дублирования кода

### 1.1 Поиск существующей функциональности

#### Метод 1: Поиск по имени функции/метода

**Команда**:
```bash
# Поиск функции по имени
grep -r "function_name" . --include="*.py"

# Поиск метода класса
grep -r "def.*method_name" . --include="*.py"

# Поиск с контекстом (показывает несколько строк вокруг)
grep -r -A 5 -B 5 "function_name" . --include="*.py"
```

**Пример**:
```bash
# Поиск функции is_bluetooth_device
grep -r "is_bluetooth_device" . --include="*.py"

# Результат:
# modules/audio_system/utils/device_utils.py:def is_bluetooth_device(name: str) -> bool:
# modules/voice_recognition/core/speech_recognizer.py:def _is_bluetooth_device(self, name: str) -> bool:
# modules/speech_playback/core/player.py:def _is_bluetooth_device(self, name: str) -> bool:
```

**Анализ результата**:
- ✅ Найдена централизованная функция: `device_utils.is_bluetooth_device()`
- ⚠️ Найдены дублирующие реализации: `speech_recognizer._is_bluetooth_device()`, `player._is_bluetooth_device()`
- **Действие**: Использовать `device_utils.is_bluetooth_device()` вместо создания новой функции

---

#### Метод 2: Семантический поиск через codebase_search

**Команда** (через инструмент codebase_search):
```python
# Поиск похожей функциональности
codebase_search("How is bluetooth device detected?")
codebase_search("Where is device type classification implemented?")
codebase_search("How are audio devices selected and configured?")
```

**Пример**:
```python
# Запрос: "How is bluetooth device detected?"
# Результат: Найдены реализации в device_utils.py, speech_recognizer.py, player.py
# Анализ: Есть централизованная функция, но есть дублирующие реализации
```

---

#### Метод 3: Поиск по паттернам кода

**Команда**:
```bash
# Поиск похожих паттернов кода
grep -r "bluetooth.*device\|device.*bluetooth" . --include="*.py" -i

# Поиск по ключевым словам
grep -r "any.*keyword.*in.*lowered" . --include="*.py"

# Поиск по структуре данных
grep -r "return.*any.*keyword" . --include="*.py"
```

**Пример**:
```bash
# Поиск паттерна определения Bluetooth устройств
grep -r "bluetooth.*device\|device.*bluetooth\|airpods\|beats" . --include="*.py" -i

# Результат показывает все места с похожей логикой
```

---

### 1.2 Проверка централизованных утилит

#### Метод 1: Поиск в утилитах

**Команда**:
```bash
# Поиск в модулях утилит
find . -path "*/utils/*.py" -exec grep -l "function_name" {} \;

# Поиск в audio_system/utils
grep -r "function_name" modules/audio_system/utils/ --include="*.py"

# Поиск в integration/core
grep -r "function_name" integration/core/ --include="*.py"
```

**Пример**:
```bash
# Поиск функций работы с устройствами в утилитах
grep -r "device" modules/audio_system/utils/ --include="*.py"

# Результат:
# modules/audio_system/utils/device_utils.py содержит:
#   - is_bluetooth_device()
#   - is_remote_device()
#   - find_device_id_by_name()
#   - get_system_default_device()
#   - classify_device()
```

---

#### Метод 2: Анализ импортов

**Команда**:
```bash
# Поиск импортов из утилит
grep -r "from.*utils.*import\|import.*utils" . --include="*.py"

# Поиск использования device_utils
grep -r "device_utils\|from.*device_utils" . --include="*.py"
```

**Пример**:
```bash
# Поиск использования device_utils
grep -r "device_utils" . --include="*.py"

# Результат показывает, кто использует централизованные утилиты
# Если функция не используется → возможно, есть дублирование
```

---

### 1.3 Сравнение реализаций

#### Метод: Анализ различий между реализациями

**Команда**:
```bash
# Сравнение двух функций
diff <(grep -A 10 "def function1" file1.py) <(grep -A 10 "def function2" file2.py)

# Просмотр реализаций рядом
grep -A 15 "def is_bluetooth_device" modules/audio_system/utils/device_utils.py
grep -A 15 "def _is_bluetooth_device" modules/voice_recognition/core/speech_recognizer.py
```

**Пример анализа**:
```python
# Реализация 1 (device_utils.py):
def is_bluetooth_device(name: str) -> bool:
    lowered = (name or "").lower()
    return any(keyword in lowered for keyword in ("bluetooth", "airpods", "beats", "headset", "earbud"))

# Реализация 2 (speech_recognizer.py):
def _is_bluetooth_device(self, name: str) -> bool:
    lowered = (name or "").lower()
    return any(keyword in lowered for keyword in ("bluetooth", "airpods", "beats", "headset", "earbud"))

# Анализ: Реализации идентичны → ДУБЛИРОВАНИЕ
# Действие: Использовать device_utils.is_bluetooth_device() вместо _is_bluetooth_device()
```

---

## 2. Выявление конфликтов

### 2.1 Проверка конфликтов имен

#### Метод 1: Поиск существующих имен

**Команда**:
```bash
# Поиск переменной по имени
grep -r "_variable_name\|variable_name" . --include="*.py"

# Поиск функции по имени
grep -r "def.*function_name\|function_name" . --include="*.py"

# Поиск класса по имени
grep -r "class.*ClassName\|ClassName" . --include="*.py"
```

**Пример**:
```bash
# Поиск переменной _mic_state
grep -r "_mic_state\|mic_state" . --include="*.py"

# Результат:
# modules/microphone_state_manager.py:self._mic_state = "opening"
# integration/integrations/voice_recognition_integration.py:self._mic_state = "opening"
# integration/core/application_state_manager.py:self._mic_state = "opening"

# Анализ: Найдено несколько мест с одинаковым именем → КОНФЛИКТ
# Действие: Использовать единый источник истины (MicrophoneStateManager)
```

---

#### Метод 2: Проверка импортов

**Команда**:
```bash
# Поиск импортов с одинаковыми именами
grep -r "from.*import.*Name\|import.*Name" . --include="*.py"

# Поиск конфликтов импортов
grep -r "from module1 import Name\|from module2 import Name" . --include="*.py"
```

**Пример**:
```bash
# Поиск импортов StateManager
grep -r "from.*import.*StateManager\|import.*StateManager" . --include="*.py"

# Результат:
# from integration.core.application_state_manager import ApplicationStateManager
# from modules.microphone_state_manager import MicrophoneStateManager

# Анализ: Разные классы с похожими именами → проверить конфликт использования
```

---

### 2.2 Проверка конфликтов состояний

#### Метод 1: Поиск управления состоянием

**Команда**:
```bash
# Поиск установки состояния
grep -r "\.state\s*=\|_state\s*=\|set_state\|update_state" . --include="*.py"

# Поиск чтения состояния
grep -r "\.state\|_state\|get_state\|read_state" . --include="*.py"
```

**Пример**:
```bash
# Поиск управления состоянием микрофона
grep -r "mic.*state\|microphone.*state" . --include="*.py" -i

# Результат:
# MicrophoneStateManager._set_state("opening")
# ApplicationStateManager.set_microphone_state("opening")

# Анализ: Два места управляют одним состоянием → КОНФЛИКТ
# Действие: Использовать только MicrophoneStateManager, синхронизировать через события
```

---

#### Метод 2: Анализ источников истины

**Команда**:
```bash
# Поиск источников истины в STATE_CATALOG.md
grep -r "source.*truth\|owner\|read.*write" Docs/STATE_CATALOG.md

# Поиск использования ApplicationStateManager
grep -r "ApplicationStateManager\|state_manager" . --include="*.py"
```

**Пример**:
```bash
# Проверка источника истины для состояния микрофона
grep -r "microphone\|mic" Docs/STATE_CATALOG.md

# Результат из STATE_CATALOG.md:
# permissions.mic:
#   - Owner: PermissionsIntegration
#   - Source of truth: ApplicationStateManager
#   - Readers: VoiceRecognitionIntegration, ScreenshotCaptureIntegration

# Анализ: Если код пишет в состояние напрямую, минуя ApplicationStateManager → КОНФЛИКТ
```

---

### 2.3 Проверка конфликтов архитектуры

#### Метод 1: Проверка порядка инициализации

**Команда**:
```bash
# Поиск порядка инициализации
grep -r "_create_integrations\|initialize\|__init__" integration/core/simple_module_coordinator.py

# Поиск зависимостей инициализации
grep -r "depends\|requires\|after\|before" integration/core/simple_module_coordinator.py
```

**Пример**:
```bash
# Проверка порядка инициализации
grep -A 50 "_create_integrations" integration/core/simple_module_coordinator.py

# Результат показывает порядок:
# 1. InstanceManager
# 2. HardwareId
# 3. FirstRunPermissions
# 4. PermissionRestart
# 5. Tray
# ...

# Анализ: Если изменение нарушает порядок → КОНФЛИКТ
```

---

#### Метод 2: Проверка EventBus событий

**Команда**:
```bash
# Поиск публикации событий
grep -r "event_bus\.publish\|publish.*event" . --include="*.py"

# Поиск подписки на события
grep -r "event_bus\.subscribe\|subscribe.*event" . --include="*.py"

# Поиск конкретного события
grep -r "audio\.device\.changed\|device\.changed" . --include="*.py"
```

**Пример**:
```bash
# Поиск события audio.device.changed
grep -r "audio\.device\.changed" . --include="*.py"

# Результат:
# integration/integrations/audio_system_integration.py:publish("audio.device.changed", ...)
# integration/integrations/speech_playback_integration.py:subscribe("audio.device.changed", ...)

# Анализ: Если создается новое событие с таким же именем → КОНФЛИКТ
# Действие: Использовать существующее событие или создать новое с уникальным именем
```

---

## 3. Выявление race conditions

### 3.1 Проверка thread-safety

#### Метод 1: Поиск общих данных

**Команда**:
```bash
# Поиск переменных класса (self._variable)
grep -r "self\._[a-z_]*\s*=" . --include="*.py"

# Поиск списков/словарей, которые могут изменяться
grep -r "self\._[a-z_]*\s*=\s*\[\|self\._[a-z_]*\s*=\s*{" . --include="*.py"

# Поиск операций append/extend/clear
grep -r "\.append\|\.extend\|\.clear\|\.pop\|\.remove" . --include="*.py"
```

**Пример**:
```bash
# Поиск _google_audio_chunks
grep -r "_google_audio_chunks" . --include="*.py"

# Результат:
# integration/integrations/voice_recognition_integration.py:
#   - self._google_audio_chunks = []  # Инициализация
#   - self._google_audio_chunks.append(audio)  # В callback потоке
#   - self._google_audio_chunks = []  # В основном async потоке

# Анализ: Данные изменяются из разных потоков → RACE CONDITION
# Действие: Добавить threading.Lock для синхронизации
```

---

#### Метод 2: Поиск блокировок

**Команда**:
```bash
# Поиск использования Lock
grep -r "threading\.Lock\|asyncio\.Lock\|Lock()" . --include="*.py"

# Поиск with lock:
grep -r "with.*lock\|with.*Lock" . --include="*.py" -i

# Поиск инициализации блокировок
grep -r "_lock\s*=\|lock\s*=" . --include="*.py"
```

**Пример**:
```bash
# Поиск блокировок для _google_audio_chunks
grep -r "_google_audio_chunks\|_google_audio_chunks_lock" . --include="*.py"

# Результат:
# Если найдено _google_audio_chunks, но НЕ найдено _google_audio_chunks_lock → RACE CONDITION
# Если найдено _google_audio_chunks_lock → проверить использование
```

---

#### Метод 3: Анализ потоков выполнения

**Команда**:
```bash
# Поиск callback функций
grep -r "callback\|def.*callback" . --include="*.py" -i

# Поиск threading.Thread
grep -r "threading\.Thread\|Thread(" . --include="*.py"

# Поиск asyncio.create_task
grep -r "asyncio\.create_task\|create_task" . --include="*.py"

# Поиск run_coroutine_threadsafe
grep -r "run_coroutine_threadsafe" . --include="*.py"
```

**Пример**:
```bash
# Поиск callback для _google_audio_chunks
grep -r -A 10 "callback.*audio\|def.*callback" integration/integrations/voice_recognition_integration.py

# Результат показывает:
# - Callback вызывается из фонового потока (AVFAudioEngine)
# - Основной код работает в async потоке
# - Оба обращаются к _google_audio_chunks → RACE CONDITION
```

---

### 3.2 Проверка async/await паттернов

#### Метод 1: Поиск async задач

**Команда**:
```bash
# Поиск создания задач
grep -r "asyncio\.create_task\|create_task" . --include="*.py"

# Поиск отслеживания задач
grep -r "_task\s*=\|\.task\s*=" . --include="*.py"

# Поиск отмены задач
grep -r "\.cancel()\|CancelledError" . --include="*.py"
```

**Пример**:
```bash
# Поиск async задач для прослушивания
grep -r -A 5 "create_task.*listen\|create_task.*recognition" . --include="*.py"

# Результат:
# asyncio.create_task(self._listen_loop())  # Без отслеживания
# asyncio.create_task(self._listen_loop())  # Еще один вызов

# Анализ: Задачи создаются без отслеживания → возможны дубликаты
# Действие: Добавить отслеживание задач и отмену предыдущих
```

---

#### Метод 2: Проверка таймаутов

**Команда**:
```bash
# Поиск async операций без таймаутов
grep -r "await.*\(\)" . --include="*.py" | grep -v "timeout\|wait_for"

# Поиск использования asyncio.wait_for
grep -r "asyncio\.wait_for\|wait_for" . --include="*.py"

# Поиск таймаутов в конфигурации
grep -r "timeout\|_timeout" config/unified_config.yaml
```

**Пример**:
```bash
# Поиск await операций без таймаутов
grep -r "await.*event_bus\|await.*grpc" . --include="*.py" | grep -v "wait_for"

# Результат показывает операции без таймаутов
# Анализ: Если операция может зависнуть → нужен таймаут
```

---

### 3.3 Проверка смешивания async и threading

#### Метод 1: Поиск run_coroutine_threadsafe

**Команда**:
```bash
# Поиск использования run_coroutine_threadsafe
grep -r "run_coroutine_threadsafe" . --include="*.py"

# Поиск правильного event loop
grep -r "event_bus\._loop\|get_event_loop\|new_event_loop" . --include="*.py"
```

**Пример**:
```bash
# Поиск вызовов async из потоков
grep -r -B 5 -A 5 "run_coroutine_threadsafe" . --include="*.py"

# Результат:
# def callback_from_thread():
#     loop = asyncio.new_event_loop()  # ❌ ПЛОХО: создание нового loop
#     loop.run_until_complete(self._publish_event())

# Анализ: Используется неправильный event loop → ПРОБЛЕМА
# Действие: Использовать event_bus._loop через run_coroutine_threadsafe
```

---

## 4. Автоматизированные проверки

### 4.1 Скрипты для проверки дублирования

**Создать скрипт** `scripts/check_code_duplication.py`:
```python
#!/usr/bin/env python3
"""Проверка дублирования кода"""

import ast
import os
from collections import defaultdict

def find_duplicate_functions():
    """Находит дублирующиеся функции"""
    functions = defaultdict(list)
    
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r') as f:
                        tree = ast.parse(f.read())
                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                # Извлекаем сигнатуру функции
                                sig = f"{node.name}({', '.join([arg.arg for arg in node.args.args])})"
                                functions[sig].append(path)
                except:
                    pass
    
    # Находим дубликаты
    duplicates = {sig: paths for sig, paths in functions.items() if len(paths) > 1}
    return duplicates

if __name__ == '__main__':
    duplicates = find_duplicate_functions()
    if duplicates:
        print("Найдены дублирующиеся функции:")
        for sig, paths in duplicates.items():
            print(f"\n{sig}:")
            for path in paths:
                print(f"  - {path}")
    else:
        print("Дублирующиеся функции не найдены")
```

---

### 4.2 Скрипты для проверки конфликтов

**Создать скрипт** `scripts/check_name_conflicts.py`:
```python
#!/usr/bin/env python3
"""Проверка конфликтов имен"""

import re
import os
from collections import defaultdict

def find_name_conflicts(pattern, file_pattern='*.py'):
    """Находит конфликты имен по паттерну"""
    conflicts = defaultdict(list)
    
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    for line_num, line in enumerate(f, 1):
                        matches = re.findall(pattern, line)
                        for match in matches:
                            conflicts[match].append((path, line_num))
    
    return {name: paths for name, paths in conflicts.items() if len(paths) > 1}

if __name__ == '__main__':
    # Проверка конфликтов переменных состояния
    state_conflicts = find_name_conflicts(r'self\._(\w+_state)\s*=')
    if state_conflicts:
        print("Найдены конфликты состояний:")
        for name, paths in state_conflicts.items():
            print(f"\n{name}:")
            for path, line_num in paths:
                print(f"  - {path}:{line_num}")
```

---

### 4.3 Скрипты для проверки race conditions

**Создать скрипт** `scripts/check_race_conditions.py`:
```python
#!/usr/bin/env python3
"""Проверка race conditions"""

import re
import os
from collections import defaultdict

def find_shared_data():
    """Находит общие данные, которые могут изменяться из разных потоков"""
    shared_data = defaultdict(list)
    
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    
                    # Поиск переменных класса (self._variable)
                    variables = re.findall(r'self\.(_\w+)', content)
                    
                    # Поиск операций изменения (append, extend, clear, =)
                    modifications = re.findall(r'self\.(_\w+)\s*\.(append|extend|clear|pop|remove|=\s*\[)', content)
                    
                    # Поиск callback функций
                    has_callback = 'callback' in content.lower() or 'def.*callback' in content
                    
                    # Поиск threading
                    has_threading = 'threading' in content or 'Thread(' in content
                    
                    # Поиск async
                    has_async = 'async def' in content or 'asyncio' in content
                    
                    # Поиск блокировок
                    has_lock = 'Lock()' in content or 'with.*lock' in content.lower()
                    
                    for var in variables:
                        if (has_callback or has_threading or has_async) and not has_lock:
                            shared_data[var].append((path, has_callback, has_threading, has_async))
    
    return shared_data

if __name__ == '__main__':
    shared_data = find_shared_data()
    if shared_data:
        print("Найдены потенциальные race conditions:")
        for var, locations in shared_data.items():
            print(f"\n{var}:")
            for path, has_callback, has_threading, has_async in locations:
                contexts = []
                if has_callback:
                    contexts.append("callback")
                if has_threading:
                    contexts.append("threading")
                if has_async:
                    contexts.append("async")
                print(f"  - {path} ({', '.join(contexts)})")
                print("    ⚠️  Проверить наличие блокировок!")
```

---

## 5. Чек-лист проверки

### 5.1 Проверка дублирования

- [ ] **Поиск по имени**: Выполнен `grep -r "function_name" . --include="*.py"`
- [ ] **Семантический поиск**: Выполнен `codebase_search("How is functionality implemented?")`
- [ ] **Проверка утилит**: Проверены `modules/*/utils/*.py` и `integration/core/*.py`
- [ ] **Сравнение реализаций**: Сравнены найденные реализации на идентичность
- [ ] **Решение**: Если найдено дублирование → использовать существующую функцию

---

### 5.2 Проверка конфликтов

- [ ] **Поиск имен**: Выполнен `grep -r "variable_name\|function_name\|ClassName" . --include="*.py"`
- [ ] **Проверка состояний**: Проверен источник истины в `STATE_CATALOG.md`
- [ ] **Проверка импортов**: Проверены конфликты импортов
- [ ] **Проверка архитектуры**: Проверены порядок инициализации и EventBus события
- [ ] **Решение**: Если найдены конфликты → использовать уникальные имена или единый источник истины

---

### 5.3 Проверка race conditions

- [ ] **Поиск общих данных**: Выполнен `grep -r "self\._[a-z_]*\s*=" . --include="*.py"`
- [ ] **Проверка потоков**: Проверены callback, threading, async операции
- [ ] **Проверка блокировок**: Проверено наличие `threading.Lock` или `asyncio.Lock`
- [ ] **Проверка async задач**: Проверено отслеживание и отмена задач
- [ ] **Проверка таймаутов**: Проверено наличие таймаутов для async операций
- [ ] **Решение**: Если найдены race conditions → добавить блокировки или исправить паттерны

---

## 📚 Примеры из реального проекта

### Пример 1: Дублирование is_bluetooth_device

**Проблема**: Функция `is_bluetooth_device()` дублируется в 3 местах.

**Выявление**:
```bash
# Шаг 1: Поиск по имени
grep -r "is_bluetooth_device" . --include="*.py"

# Результат:
# modules/audio_system/utils/device_utils.py:def is_bluetooth_device(name: str) -> bool:
# modules/voice_recognition/core/speech_recognizer.py:def _is_bluetooth_device(self, name: str) -> bool:
# modules/speech_playback/core/player.py:def _is_bluetooth_device(self, name: str) -> bool:

# Шаг 2: Сравнение реализаций
grep -A 5 "def.*is_bluetooth_device" modules/audio_system/utils/device_utils.py
grep -A 5 "def.*_is_bluetooth_device" modules/voice_recognition/core/speech_recognizer.py

# Шаг 3: Анализ
# Реализации идентичны → ДУБЛИРОВАНИЕ
# Решение: Использовать device_utils.is_bluetooth_device()
```

---

### Пример 2: Конфликт состояний микрофона

**Проблема**: Два места управляют состоянием микрофона.

**Выявление**:
```bash
# Шаг 1: Поиск управления состоянием
grep -r "mic.*state\|microphone.*state" . --include="*.py" -i

# Результат:
# MicrophoneStateManager._set_state("opening")
# ApplicationStateManager.set_microphone_state("opening")

# Шаг 2: Проверка источника истины
grep -r "microphone\|mic" Docs/STATE_CATALOG.md

# Результат из STATE_CATALOG.md:
# permissions.mic:
#   - Owner: PermissionsIntegration
#   - Source of truth: ApplicationStateManager

# Шаг 3: Анализ
# Два места управляют одним состоянием → КОНФЛИКТ
# Решение: Использовать только MicrophoneStateManager, синхронизировать через события
```

---

### Пример 3: Race condition в _google_audio_chunks

**Проблема**: `_google_audio_chunks` изменяется из разных потоков без синхронизации.

**Выявление**:
```bash
# Шаг 1: Поиск использования переменной
grep -r "_google_audio_chunks" . --include="*.py"

# Результат:
# integration/integrations/voice_recognition_integration.py:
#   - self._google_audio_chunks = []  # Инициализация
#   - self._google_audio_chunks.append(audio)  # В callback потоке
#   - self._google_audio_chunks = []  # В основном async потоке

# Шаг 2: Проверка потоков
grep -r -B 5 -A 5 "_google_audio_chunks" integration/integrations/voice_recognition_integration.py

# Результат:
# def callback(recognizer, audio):  # Callback из фонового потока
#     self._google_audio_chunks.append(audio)
#
# async def process_audio():  # Основной async поток
#     self._google_audio_chunks = []

# Шаг 3: Проверка блокировок
grep -r "_google_audio_chunks_lock\|Lock" integration/integrations/voice_recognition_integration.py

# Результат: Блокировки не найдены

# Шаг 4: Анализ
# Данные изменяются из разных потоков без блокировок → RACE CONDITION
# Решение: Добавить threading.Lock для синхронизации
```

---

## 📚 Связанные документы

- `DUPLICATE_CONFLICT_RACE_PREVENTION_CHECKLIST.md` — детальная проверка на этапе планирования
- `CODE_CHANGE_VALIDATION_RULES.md` — детальные правила валидации изменений кода
- `REAL_TIME_CODE_VALIDATION.md` — автоматическая валидация при генерации кода
- `.cursorrules` (раздел 11.2) — правила валидации изменений

---

**Версия**: 1.0  
**Дата создания**: 2025-01-XX
