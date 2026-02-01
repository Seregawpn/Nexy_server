# Чек-лист тестирования TAL subsystem

## Статус: ✅ Готово к тестированию

Все улучшения применены:
- ✅ Идемпотентность hold/release
- ✅ Обработка фатальных ошибок
- ✅ Логирование с причинами
- ✅ Управление задачами

## Обзор проблемы и фикса
- **Симптом:** приложение умирало через ~5 секунд после перезапуска (особенно после выдачи разрешений), в логах `runningboardd`: `Assertion did invalidate due to timeout`.
- **Корень:** `SimpleModuleCoordinator._hold_tal_until_tray_ready()` не устанавливал hold, если `automaticTerminationSupportEnabled()` уже отключен, а `tray_controller` местами повторно управлял TAL.
- **Фикс:** принудительно ставим TAL hold и обновляем его каждые 30 секунд до `tray.ready`, увеличен таймаут до 120 секунд, логика управления сконцентрирована в `SimpleModuleCoordinator`, в tray-коде убрали повторное `enableAutomaticTermination_`.
- **Тестовый скрипт:** `scripts/check_tal_after_restart.py` анализирует объединённые логи Nexy + runningboardd.

## Быстрый self-check (ex TAL_RESTART_QUICK_CHECK)
1. Перезапусти `.app`, собери логи:
   ```bash
   log show --style compact --last 5m --predicate 'process == "Nexy" OR (process == "runningboardd" AND eventMessage CONTAINS "com.nexy.assistant")' > log.md
   python3 scripts/check_tal_after_restart.py log.md
   ```
2. Убедись, что в Nexy-логах появляются:
   - `TAL=hold (...)` сразу после перезапуска
   - `TAL=refresh (...) elapsed=30.0s` каждые 30 секунд
   - `tray.ready` до завершения
   - `TAL=released (reason=tray_ready|fatal_after_tray|fatal_before_tray)`
3. В `runningboardd` не должно быть:
   - `Assertion did invalidate due to timeout` до `tray.ready`
   - `termination reported by launchd` до `tray.ready`

## Подробная верификация (ex TAL_RESTART_VERIFICATION_CHECKLIST)
| Где смотреть | Что искать | Команды |
| --- | --- | --- |
| Логи Nexy | `launching: /usr/bin/open ...Nexy.app`, `TAL=hold`, периодический `TAL=refresh`, `tray.ready`, отсутствие `Entering exit handler.` до tray | `log show --style compact --process Nexy --last 5m` |
| `runningboardd` | `Acquiring assertion ... "App is holding power assertion"`, отсутствие `Assertion did invalidate...` и `termination reported...` пока tray не готов | `log show --style compact --last 5m --predicate 'process == "runningboardd" AND eventMessage CONTAINS "com.nexy.assistant"'` |
| Автоанализ | Совпадения паттернов, ссылки на строки с таймаутами | `python3 scripts/check_tal_after_restart.py log.md` |

### Ожидаемые паттерны
```
[14:01:52] TAL=hold (ts=..., auto_term_enabled=False)
[14:02:22] TAL=refresh (ts=..., elapsed=30.0s)
[14:03:15] tray.ready - TrayControllerIntegration запущен ...
[14:03:15] TAL=released (ts=..., duration=83.0s, reason=tray_ready)
```
И никаких `Assertion did invalidate due to timeout` до `tray.ready`.

### До исправления (для сравнения)
```
[14:01:57] Assertion did invalidate due to timeout ...
[14:01:57] Entering exit handler.
```
Если паттерн возвращается — фикс регрессирует.

---

## Сценарий 1: Нормальный happy-path (первый запуск + TCC + рестарт)

### Шаги:
1. Очистить флаги первого запуска:
   ```bash
   python3 scripts/clear_first_run_flags.py
   ```

2. Запустить приложение:
   ```bash
   open -a /Applications/Nexy.app
   # или
   python3 main.py
   ```

3. Выдать разрешения TCC (микрофон, экран, доступность)

4. Дождаться автоматического перезапуска

5. Проверить логи:
   ```bash
   python3 scripts/check_tal_after_restart.py log.md
   ```

### Ожидаемый результат:
- ✅ `TAL=hold` появился после перезапуска
- ✅ `TAL=refresh` появляется каждые 30 секунд до tray.ready
- ✅ `tray.ready` появился до завершения
- ✅ `TAL=released (reason=tray_ready, ...)` после tray.ready
- ✅ **НЕТ** `Assertion did invalidate due to timeout` до tray.ready
- ✅ **НЕТ** `Entering exit handler.` до tray.ready
- ✅ Приложение продолжает работать (не завершается само)

### Проверка в runningboardd:
```bash
log show --style compact --last 5m --predicate 'process == "runningboardd" AND eventMessage CONTAINS "com.nexy.assistant"'
```

**Ожидаемое:**
- ✅ `Acquiring assertion ... "App is holding power assertion"`
- ❌ **НЕТ** `Assertion did invalidate due to timeout` до tray.ready
- ❌ **НЕТ** `termination reported by launchd` до tray.ready

---

## Сценарий 2: Холодный логин (LaunchAgent)

### Шаги:
1. Настроить LaunchAgent для автоматического запуска Nexy при логине

2. Перезагрузить систему или выйти/войти в систему

3. После логина проверить логи Nexy

4. Проверить runningboardd логи

### Ожидаемый результат:
- ✅ `TAL=hold` появился при старте
- ✅ `TAL=refresh` появляется каждые 30 секунд
- ✅ `tray.ready` появился
- ✅ `TAL=released (reason=tray_ready, ...)` после tray.ready
- ✅ **НЕТ** `Assertion did invalidate due to timeout` до tray.ready
- ✅ Приложение не завершается через 5–10 секунд без причины
- ✅ Tray icon виден и приложение работает

### Проверка в runningboardd:
- ✅ `Acquiring assertion ... "App is holding power assertion"`
- ❌ **НЕТ** `Assertion did invalidate due to timeout` до tray.ready

---

## Сценарий 3: Фатальная ошибка до tray.ready

### Шаги:
1. Временно добавить искусственную ошибку в `SimpleModuleCoordinator.run()` **до** `tray.ready`:
   ```python
   # В integration/core/simple_module_coordinator.py, в методе run()
   # После _hold_tal_until_tray_ready(), но до tray.ready
   if not self._tray_ready:
       raise RuntimeError("TEST: Fatal error before tray ready")
   ```

2. Запустить приложение

3. Проверить логи Nexy

4. Проверить runningboardd логи

### Ожидаемый результат:
- ✅ `TAL=hold` появился при старте
- ✅ Приложение упало с ошибкой
- ✅ В логах есть: `⚠️ [FATAL] TAL hold активен в finally блоке (tray=not_ready) - явно снимаем`
- ✅ В логах есть: `TAL=released (ts=..., duration=...s, reason=fatal_before_tray, ...)`
- ✅ **НЕТ** висящих assertion в runningboardd после смерти процесса

### Проверка в runningboardd:
```bash
log show --style compact --last 2m --predicate 'process == "runningboardd" AND eventMessage CONTAINS "com.nexy.assistant"'
```

**Ожидаемое:**
- ✅ `Acquiring assertion ... "App is holding power assertion"`
- ✅ После смерти процесса: assertion должен быть освобождён (нет висящих assertion)

---

## Сценарий 4: Фатальная ошибка после tray.ready

### Шаги:
1. Временно добавить искусственную ошибку в `SimpleModuleCoordinator.run()` **после** `tray.ready`:
   ```python
   # В integration/core/simple_module_coordinator.py, в методе run()
   # После tray.ready
   if self._tray_ready:
       raise RuntimeError("TEST: Fatal error after tray ready")
   ```

2. Запустить приложение

3. Дождаться tray.ready

4. Проверить логи Nexy

5. Проверить runningboardd логи

### Ожидаемый результат:
- ✅ `TAL=hold` появился при старте
- ✅ `tray.ready` появился
- ✅ `TAL=released (reason=tray_ready, ...)` после tray.ready
- ✅ Приложение упало с ошибкой после tray.ready
- ✅ В логах есть: `⚠️ [FATAL] TAL hold активен в finally блоке (tray=ready) - явно снимаем`
- ✅ В логах есть: `TAL=released (ts=..., duration=...s, reason=fatal_after_tray, ...)`
- ✅ **НЕТ** висящих assertion в runningboardd после смерти процесса

### Проверка в runningboardd:
- ✅ После смерти процесса: assertion должен быть освобождён (нет висящих assertion)

---

## Сценарий 5: Идемпотентность (опционально)

### Шаги:
1. Добавить временные логи или breakpoint в `_hold_tal_until_tray_ready()` и `_release_tal_hold()`

2. Запустить приложение

3. Попытаться вызвать `_hold_tal_until_tray_ready()` дважды (если есть способ)

4. Попытаться вызвать `_release_tal_hold()` дважды

### Ожидаемый результат:
- ✅ При повторном `_hold_tal_until_tray_ready()`:
  - Лог: `TAL=hold (ts=..., reason=duplicate_call, already_active=True)`
  - Assertion обновлён, но состояние не сломано
- ✅ При повторном `_release_tal_hold()`:
  - Лог: `TAL=released (ts=..., reason=..., had_active_hold=False, duplicate_release=True)`
  - Состояние не сломано

---

## Команды для быстрой проверки

### Автоматический анализ логов:
```bash
python3 scripts/check_tal_after_restart.py log.md
```

### Проверка TAL событий в логах Nexy:
```bash
grep -E "TAL=hold|TAL=refresh|TAL=released" log.md
```

### Проверка assertion timeout:
```bash
grep "Assertion did invalidate due to timeout" log.md | grep "com.nexy.assistant"
```

### Проверка перезапуска:
```bash
grep "launching:.*Nexy.app" log.md
```

### Проверка tray.ready:
```bash
grep -i "tray.*ready\|TrayControllerIntegration запущен" log.md
```

### Проверка runningboardd:
```bash
log show --style compact --last 5m --predicate 'process == "runningboardd" AND eventMessage CONTAINS "com.nexy.assistant"'
```

---

## Критерии успеха

Если все сценарии проходят успешно:

✅ **TAL subsystem в порядке боевой готовности**

Признаки здорового поведения:
- TAL hold устанавливается при старте
- TAL refresh работает каждые 30 секунд
- TAL released только после tray.ready или при явном shutdown
- Нет висящих assertion после смерти процесса
- Нет assertion timeout до tray.ready
- Приложение не завершается само до tray.ready

---

## Сводка изменений (ex TAL_FIX_SUMMARY)
- **SimpleModuleCoordinator**
  - `\_hold_tal_until_tray_ready` всегда вызывает `disableAutomaticTermination_()` и запускает фоновые задачи обновления.
  - `\_periodically_refresh_tal_hold` гоняет refresh каждые 30 секунд (макс. 120 секунд).
  - `\_release_tal_hold_after_timeout` увеличен до 120 секунд.
  - Расширенное логирование `TAL=hold|refresh|released` + причины.
- **TrayControllerIntegration**
  - Убрано повторное `enableAutomaticTermination_`, чтобы не нарушить hold до `tray.ready`.
- **Тесты и скрипты**
  - `scripts/check_tal_after_restart.py`, `scripts/test_tal_assertion.py`, negative scenarios для fatal-before/after tray.

## Детали фикса таймаута (ex TAL_ASSERTION_TIMEOUT_FIX)
- Таймаут TAL увеличен с 60 до 120 секунд (медленные системы).
- Периодическое обновление удерживает assertion живым до появления tray.
- При падении до `tray.ready` finally-блок явно снимает hold и логирует `reason=fatal_before_tray`.
- Для menu bar приложения automatic termination **не** включаем обратно после tray — это ожидаемое поведение.

## Отчёт о тестах (ex TAL_ASSERTION_TEST_REPORT)
- **Всего тестов:** 6 (установка hold, refresh-loop, async, timeout, интеграция с SM, отсутствие дублирования).
- **Результат:** 6/6 ✅.
- Скрипт: `python3 scripts/test_tal_assertion.py`.
- Критические проверки:
  1. `automaticTerminationSupportEnabled` доступен и корректно управляется.
  2. Refresh цикл выполняет ≥3 итераций без ошибок.
  3. Таймаут 120s, отложенный release и логирование причин.
  4. Нет повторного `enableAutomaticTermination_` вне SimpleModuleCoordinator.

## После тестирования

После успешного прохождения всех сценариев:

1. Удалить временные `raise RuntimeError("TEST: ...")` из кода.
2. Обновить этот документ (секции "Сводка изменений" и "Отчёт о тестах"), если появились новые случаи.
3. Закоммитить изменения.

---

## Примечания

- Все тесты должны выполняться на реальном `.app` bundle, а не только через `python3 main.py`.
- Разница в поведении между терминалом и `.app` bundle была одной из причин проблемы.
- Для сценария 3 и 4 можно использовать временные `raise` или специальный feature flag для тестирования.

