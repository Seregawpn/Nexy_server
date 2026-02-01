# First-Run Permissions Architecture (Current)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-008

## Diagnosis
Текущая архитектура first-run переведена в строгий последовательный поток без статус‑проверок, с блокировкой раннего запуска input/voice/screenshot во время first‑run.

## Root Cause
Ранее параллельные TCC‑диалоги (Input Monitoring + Accessibility) ломали UX и блокировали Mic/Screen в том же запуске. Это устранено gate‑логикой.

## Optimal Fix
Фиксируется единый оркестратор first‑run, чёткий порядок из конфигурации, и запрет стартовать зависимые модули до завершения first‑run.

## Verification
Тесты `scripts/test_first_run_integration.sh` + offline‑check `scripts/check_first_run_state.py`.

## Запрос/цель
Передать другому ассистенту техническое описание текущей архитектуры first‑run и известных проблем.

## Контекст
- Ограничения: Accessibility остаётся dialog‑only (без Settings)

## Решения/выводы
- Оркестратор first‑run запускает разрешения строго последовательно, по списку конфигурации.
- Status‑checks в restart‑флоу отключены; readiness считается выданным (assume GRANTED).
- Input/voice/screenshot не стартуют при `first_run_in_progress` или `permissions_restart_pending`.
- Contacts prompt требует наличия Contacts framework в сборке.

## Архитектура (текущая)

### 1) Последовательность разрешений (актуальный порядок)
1. Accessibility
2. Microphone
3. Screen Capture
4. Contacts
5. Full Disk Access (settings-only)
6. Input Monitoring

На каждый шаг:
- Оркестратор запускает соответствующий системный триггер разрешения.
- Держит окно `activation_hold_duration_sec` (обычно 15 сек).
- Делает паузу `pause_between_requests_sec` перед следующим разрешением.

### 2) Технические инструменты и библиотеки (что именно используется)
**Библиотеки (Python/PyObjC)**  
- `Quartz` → `CGRequestPostEventAccess()` для Accessibility.  
- `AVFoundation` + `sounddevice` → микрофон через `InputStream`.  
- `AppKit` → вспомогательные системные части (menu/tray).  
- `Contacts` (PyObjC) → `CNContactStore.requestAccessForEntityType`.  
- `IOKit` (ctypes) → `IOHIDRequestAccess`, `IOHIDCheckAccess` (Input Monitoring).  
- `ScreenCapturePermissionManager` (внутренний wrapper) → `CGRequestScreenCaptureAccess`.  

**Системные инструменты**  
- `System Settings` (URL) → Full Disk Access (settings-only).  
- TCC (macOS) → хранит решение (GRANTED/DENIED/UNKNOWN).  

### 3) Как именно запрашиваются разрешения (по шагам)
**Accessibility**  
- Вызов: `CGRequestPostEventAccess()`  
- Диалог показывается системой, если статус `NOT_DETERMINED`.  

**Microphone**  
- Вызов: `sounddevice.InputStream`  
- Диалог показывается системой, если статус `NOT_DETERMINED`.  

**Screen Capture**  
- Вызов: `CGRequestScreenCaptureAccess()`  
- Диалог показывается системой, если статус `NOT_DETERMINED`.  

**Contacts**  
- Вызов: `CNContactStore.requestAccessForEntityType`  
- Диалог появляется только если Contacts framework доступен.  

**Full Disk Access**  
- Диалога нет → открываем System Settings.  

**Input Monitoring**  
- Вызов: `IOHIDRequestAccess(kIOHIDRequestTypeListenEvent)`  
- Диалог показывается системой, если статус `NOT_DETERMINED`.  

### 4) Gates (анти‑гонки)
- В coordinator: не запускать `input`, `voice_recognition`, `screenshot_capture`, если:
  - `first_run_in_progress=True` **или** `permissions_restart_pending=True`.
- В input_processing: не стартовать при `first_run_in_progress`.

### 5) Флаги
- `~/Library/Application Support/Nexy/permissions_first_run_completed.flag`
- `~/Library/Application Support/Nexy/restart_completed.flag`

### 6) Рестарт
- После цикла публикуется `permissions.first_run_restart_pending`.
- Перезапуск инициируется отдельным рестарт‑модулем (без статус‑чеков).
- `permissions.first_run_completed` публикуется **после рестарта**.

### 6) Accessibility
- Остаётся dialog‑only. System Settings **не открывается**.

## Критические проблемы и причины (актуальные)
1) **Contacts prompt не показывался**  
   - Признак: `Contacts framework not available; no dialog can be shown`.  
   - Причина: Contacts framework отсутствует в сборке.  
   - Решение: добавить `Contacts` в PyInstaller hiddenimports и перепаковать.  

2) **Input Monitoring не появлялся в System Settings**  
   - Признак: `IOHIDRequestAccess(ListenEvent) ... result=True`, но Nexy нет в списке.  
   - Причина: TCC уже имеет решение (DENIED/GRANTED) или требуется reset.  
   - Решение: `tccutil reset ListenEvent com.nexy.assistant` → запуск из `/Applications/Nexy.app`.  

3) **Параллельные диалоги → блокировка Mic/Screen**  
   - Признак: Accessibility + Input Monitoring одновременно, потом тишина.  
   - Причина: ранний старт input_processing во время first‑run.  
   - Решение: gates в coordinator + self‑guard input_processing.  

4) **Запуск не из app bundle**  
   - Признак: TCC не добавляет запись, список пуст.  
   - Причина: запуск `python3 main.py` вместо `/Applications/Nexy.app`.  
   - Решение: тестировать только из .app.  

## Проверки/тесты (поведение)
- Тест проверяет последовательность activator‑вызовов и факт `restart_pending`.
- Offline‑проверка валидирует наличие флагов и отсутствие публикаций `permissions.status_checked`.

## Лог‑маркеры
- `🔐 [FIRST_RUN_PERMISSIONS] Активация <perm>` — старт шага.
- `IOHIDRequestAccess(ListenEvent)` — фактический системный запрос Input Monitoring.
- `Contacts framework not available` — проблема отсутствия Contacts framework.
- `permissions.first_run_restart_pending` — сигнал на рестарт.

## Открытые вопросы
- Нужно ли локализовать логи (EN‑only)?
- Нужны ли дополнительные guards для модулей, которые могут триггерить TCC?

## Следующие шаги
1) Перепаковать приложение (Contacts уже добавлен в spec).
2) TCC reset для ListenEvent/Contacts перед запуском.
3) Подтвердить появление Contacts/Input Monitoring в UI.
