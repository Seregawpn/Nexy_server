# Hotkey Implementation Plan (Ctrl+N, Single Owner)

## 1. Цель и границы

Цель: внедрять изменения hotkey-пути без регрессий в `interrupt`, `mode.request`, `PTT lifecycle`.

Границы:
- Разрешён только один suppression path: `Ctrl+N`.
- Нецелевые комбинации всегда pass-through.
- Централизация обязательна: keyboard adapter не владеет режимами/сессиями.

---

## 2. Архитектурный контракт (фикс до начала работ)

### 2.1 Source of Truth
- Suppression policy owner: `modules/input_processing/keyboard/mac/quartz_monitor.py`
- PTT lifecycle owner: `integration/integrations/input_processing_integration.py`
- Mode transition executor: `integration/integrations/mode_management_integration.py`

### 2.2 Запрещённые дубли
- Запрещён второй путь suppression вне keyboard adapter.
- Запрещён второй путь mode transition вне `mode.request` owner flow.
- Запрещены локальные обходы в UI/tray/voiceover слоях.

### 2.3 Anti-race инварианты
- Один `terminal stop` на один `press_id`.
- Один `recording_start` в `start_in_flight`.
- Нет параллельных конфликтующих `mode.request` для одного контекста сессии.

---

## 3. Последовательный план внедрения

## Этап 0. Baseline и freeze контракта

### Цель
Зафиксировать эталон до правок, чтобы видеть регрессии.

### Шаги
1. Зафиксировать требования в `Docs/HOTKEY_COMBINATION_REQUIREMENTS.md`.
2. Снять baseline-логи сценариев:
- strict `Ctrl+N` (short/long/release)
- `Ctrl+Cmd+N`, `Ctrl+Opt+N`, `Ctrl+Shift+N`
- playback preempt
- secure input
3. Зафиксировать текущие owner-paths и точки публикации/подписки событий.

### Выход этапа
- Есть baseline и неизменяемый контракт owner-слоёв.

---

## Этап 1. Suppression policy (только keyboard adapter)

### Цель
Оставить suppression только для strict `Ctrl+N`.

### Шаги
1. Проверить strict chord gate:
- suppression только для `Control + N`;
- при `Cmd/Opt/Shift` только pass-through.
2. Проверить, что модификаторы сами не подавляются.
3. Проверить parity fallback path (без расширения suppression semantics).

### Anti-duplication
- Не вносить lifecycle-логику в adapter.

### Anti-race
- Проверить `flagsChanged` + `keyDown/keyUp` порядок и stale-guards.

### Выход этапа
- Нецелевые комбинации не подавляются.

---

## Этап 2. Lifecycle guards (только InputProcessingIntegration)

### Цель
Убрать дубли start/stop и конфликты terminal path.

### Шаги
1. Проверить dedup по `press_id` (`_terminal_stop_press_id`).
2. Проверить single-flight start (`_start_in_flight`).
3. Проверить short-tap/long-press/release развилки без двойных terminal actions.
4. Проверить reset ветки (`recognition_failed`, `grpc_failed`, `grpc_completed`).

### Anti-duplication
- Не дублировать stop/start в нескольких callbacks.

### Anti-race
- Синхронизация через `_lifecycle_lock` и idempotent guards.

### Выход этапа
- На одно нажатие нет двойных start/stop.

---

## Этап 3. Interrupt и mode transitions (owner only)

### Цель
Стабилизировать цепочку `interrupt.request` -> terminal stop -> `mode.request`.

### Шаги
1. Проверить owner path внешнего `interrupt.request`.
2. Проверить подавление дублей для keyboard-origin interrupt path.
3. Проверить порядок mode transitions:
- LISTENING после long-press start
- PROCESSING после release stop
- SLEEPING в terminal fail/cancel ветках
4. Проверить отсутствие конфликтующих mode.request в одном контексте.

### Anti-duplication
- Один owner mode transition через `mode.request`.

### Anti-race
- Дедуп источников interrupt и terminal action по `press_id/session_id`.

### Выход этапа
- Нет дубли mode transitions и конфликтов состояний.

---

## Этап 4. Secure Input и backend degradation

### Цель
Корректная деградация без побочных блокировок.

### Шаги
1. Проверить `tap_enabled=false` path:
- `ptt_available=false`
- корректный forced stop
- безопасный выход в `SLEEPING`
2. Проверить recovery после окончания secure input.
3. Проверить backend policy:
- `auto`, `quartz`, `pynput`
- без silent drift владельца suppression semantics.

### Anti-duplication
- Не добавлять отдельный secure-input owner.

### Anti-race
- cooldown guard на repeated force-stop.

### Выход этапа
- Secure input не ломает другие комбинации и не залипает состояние.

---

## Этап 5. VoiceOver и Focus изоляция

### Цель
Исключить боковое влияние на hotkey owner flow.

### Шаги
1. Проверить `engage_on_keyboard_events=false`.
2. Проверить отсутствие runtime forced focus path (`force_activate_on_startup=false` по умолчанию).
3. Проверить, что voiceover/focus слои не инициируют альтернативные hotkey решения.

### Выход этапа
- Никакого side-effect влияния на suppression/lifecycle owner flows.

---

## Этап 6. Интеграционное тестирование и DoD

### 6.1 Матрица тестов

1. Hotkey core:
- `Ctrl+N` short/long/release.
2. Non-target pass-through:
- `Ctrl+Cmd+N`
- `Ctrl+Opt+N`
- `Ctrl+Shift+N`
3. Interrupt/preempt:
- playback active + long-press preempt
- short-tap cancel в idle и processing
4. Mode transitions:
- `SLEEPING -> LISTENING -> PROCESSING -> SLEEPING`
5. Secure input:
- tap disabled/restore
6. VoiceOver/focus:
- active VoiceOver chords
- no runtime focus stealing

### 6.2 Обязательные проверки логов
- suppression reason только для strict `Ctrl+N`
- один terminal stop на `press_id`
- отсутствие дублей `mode.request` в одном контексте
- корректный reset waiting states

### 6.3 Exit Criteria (DoD)
1. Все этапы пройдены без регрессий.
2. Нет второго owner-path по suppression/mode transitions.
3. Нецелевые сочетания не деградируют.
4. PTT и interrupt стабильны в длительном прогонах.

---

## 4. Управление рисками

### Высокий риск
- Дубли terminal path (`release` vs `interrupt`).
- Ложный suppression из-за stale modifier state.

### Митигаторы
- Этапная поставка (не смешивать изменения этапов).
- Обязательные лог-проверки после каждого этапа.
- Небольшие PR/коммиты по этапам с точечным rollback.

---

## 5. Правила внедрения

1. Изменения только в owner-слое текущего этапа.
2. Нельзя делать cross-layer refactor в рамках одного этапа.
3. После каждого этапа:
- тест-матрица этапа
- запись результата в task-brief
- только затем переход к следующему этапу.
