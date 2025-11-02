# ADR-001: First Run Restart Hotfix

## Статус
**ПРИНЯТО** (2025-11-02)

## Контекст
Production blocker - приложение не перезапускается после предоставления системных разрешений при первом запуске.

### Проблемы:
1. **Перезапуск не работает**: `subprocess.run(["/usr/bin/open", "-n", "-a", bundle_path])` возвращается немедленно без проверки что новый процесс запустился. После `os._exit(0)` старый процесс завершается, но новый может не успеть стартовать.

2. **Ассистент активируется досрочно**: Событие `permissions.first_run_completed` публикуется ДО перезапуска. `voice_recognition_integration` подписан на это событие и разблокирует микрофон за 2-3 секунды ДО фактического перезапуска.

3. **Отсутствие emergency controls**: Нет механизма экстренного отключения перезапуска в production.

### Анализ архитектуры:
Полный анализ показал нарушения .cursorrules (SIMPLE-гейт, Impact-гейт, Selectors/Gateways архитектура), но для production blocker требуется быстрый hotfix.

## Решение

### Phase 1: Pragmatic Hotfix (2-3 часа)

Минимальные изменения для решения критических проблем:

#### 1. Использовать `open -W` для ожидания запуска

**Файл**: `modules/permission_restart/macos/permissions_restart_handler.py`

**Изменения**:
- Заменить `open -n -a` на `open -n -W -a` (флаг `-W` блокирует до открытия приложения)
- Увеличить timeout с 5 до 10 секунд (PyInstaller unpacking требует времени)
- Проверять exit code и логировать stderr
- Добавить 3-секундную задержку после `open -W` для полной инициализации
- Возвращать `False` при любых ошибках (включая timeout)

**Обоснование**: `open -W` (--wait-apps) более надёжен чем polling через `pgrep`, работает с любым bundle path, не требует парсинга process names.

#### 2. Изменить порядок публикации событий

**Файл**: `integration/integrations/first_run_permissions_integration.py`

**Изменения**:
- **НЕ** публиковать `permissions.first_run_completed` в методе `start()`
- Установить persistent флаг `restart_completed.flag` перед перезапуском
- Публиковать ТОЛЬКО `permissions.first_run_restart_pending`
- В методе `initialize()` проверять флаг `restart_completed.flag` и публиковать `completed` в НОВОМ процессе

**Обоснование**: Это предотвращает race condition когда `voice_recognition` разблокируется до перезапуска.

#### 3. Добавить kill-switch

**Файл**: `modules/permission_restart/macos/permissions_restart_handler.py`

**Изменения**:
- Проверять `NEXY_KS_FIRST_RUN_RESTART` environment variable
- Если установлен в `true/yes/1`, перевести handler в dry-run режим

**Обоснование**: Позволяет экстренно отключить restart механизм в production без релиза.

### Объём изменений:
- **~100 LOC** (добавлено/изменено)
- **3 файла** изменены
- **0 новых зависимостей**

## Почему не v0 (≤60 LOC, ≤1 файл)

Согласно .cursorrules раздел 11.2 (SIMPLE-гейт), решение должно укладываться в v0:
- ≤60 LOC, ≤1 файл
- Использовать существующие selectors/gateways
- Добавить тесты

**Обоснование отклонения**:
1. **Race condition** требует изменений в subprocess handling (permissions_restart_handler.py)
2. **Event ordering** требует persistent state через file flag (first_run_permissions_integration.py)
3. **Verification logic** требует subprocess timeout и error handling (~50 LOC в одном методе)
4. **Kill-switch** требует environment variable check (~10 LOC)

**Итого**: Технически невозможно решить в ≤60 LOC и 1 файл без нарушения separation of concerns.

## Откат

### Emergency rollback:
```bash
# В production - установить kill-switch
export NEXY_KS_FIRST_RUN_RESTART=true
# Или через systemd/launchd environment
launchctl setenv NEXY_KS_FIRST_RUN_RESTART true

# Git rollback
git revert <commit-hash>

# Очистка persistent state (если нужно)
rm ~/Library/Application\ Support/Nexy/restart_completed.flag
```

### Fallback поведение:
При активном kill-switch restart mechanism отключается, приложение продолжает работать без перезапуска. Voice recognition может активироваться досрочно, но это менее критично чем broken restart flow.

## Технический долг

### Phase 2: Architectural Compliance (следующий спринт, ~5 дней)

Привести код к соответствию .cursorrules:

1. **Документация**:
   - Создать `change_impact.yaml` (оси, инварианты, guards, метрики, rollout)
   - Обновить `Docs/STATE_CATALOG.md` (добавить оси: `permissions.restart_pending`, `process.lifecycle`)
   - Обновить `config/interaction_matrix.yaml` (правило для coordinator restart logic)

2. **Selectors/Gateways архитектура**:
   - Добавить `restart_pending: bool` в `Snapshot` (integration/core/selectors.py)
   - Создать `decide_continue_integration_startup()` gateway (integration/core/gateways.py)
   - Refactor `simple_module_coordinator.py` для использования gateway вместо прямых проверок `_restart_pending`

3. **Тестирование**:
   - Pairwise тесты: ≥14 комбинаций осей (FirstRun × restart_pending × appMode × mic_permission)
   - 2 negative tests (restart fails, timeout)
   - Contract tests для EventBus событий

4. **Feature flag**:
   - Добавить `NEXY_FF_FIRST_RUN_RESTART` в `unified_config.yaml`
   - Rollout plan: 1% → 25% → 100%
   - Shadow mode для validation без применения

5. **Decision logging**:
   - Привести логи к формату: `decision=<start|abort|retry|degrade> ctx={...} source=<domain> duration_ms=<int>`

## Последствия

### Положительные:
- ✅ Решает production blocker за 2-3 часа
- ✅ Минимальные изменения → низкий риск регрессии
- ✅ Kill-switch позволяет emergency rollback
- ✅ Persistent flag `restart_completed.flag` предотвращает race condition
- ✅ `open -W` более надёжен чем polling

### Отрицательные:
- ❌ Не соответствует Selectors/Gateways архитектуре
- ❌ Отсутствуют pairwise тесты
- ❌ Технический долг для Phase 2
- ❌ Нет feature flag для gradual rollout

### Риски:
1. **`open -W` timeout**: Если приложение зависает на старте, `open -W` будет ждать 10 секунд. Mitigation: timeout + fallback to dev process.
2. **Persistent flag corruption**: Если флаг не удаляется, `completed` будет публиковаться при каждом запуске. Mitigation: try/catch в `initialize()`.
3. **PyInstaller bundle path**: `get_user_app_path()` всегда возвращает `/Applications/Nexy.app`. Если bundle в другой папке, restart не сработает. Mitigation: fallback to dev process.

## Владелец
@tech-lead

## Timeline
- **Phase 1** (hotfix): 2-3 часа (DONE)
- **Phase 2** (compliance): 5 дней в спринте N+1 (PLANNED)

## Связанные документы
- `.cursorrules` разделы 11.2, 18.x, 21.x
- `Docs/STATE_CATALOG.md`
- `config/interaction_matrix.yaml`
- `integration/core/gateways.py`

## История изменений
- 2025-11-02: Initial hotfix (Phase 1)
- TBD: Architectural compliance (Phase 2)
