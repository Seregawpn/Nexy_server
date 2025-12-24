# Nexy Audio Migration

## Master Normative Document (FINAL)

**Статус:** FINAL / APPROVED  
**Платформа:** macOS  
**Технологии:** Python · PyObjC · AVFoundation · sounddevice · Google Speech Recognition  
**Архитектурная модель:** Reconcile-based, single-owner audio model  
**Обязательность:** 100%

---

## 1. Назначение

Данный документ является **единым нормативным источником истины** для миграции и дальнейшего развития аудиосистемы Nexy.

Документ:

* заменяет все разрозненные описания;
* обязателен для реализации, ревью, CI и релиза;
* допускает **только backward-compatible изменения**;
* используется как контракт между архитектурой, кодом и тестами.

---

## 2. Архитектурные инварианты

Система **обязана** обеспечивать:

1. Единственного владельца микрофона
2. Полное отсутствие двойного input-захвата
3. Разделение input (Google SR) и output (AVFoundation)
4. Устойчивость к:

   * Bluetooth/USB device storms
   * race conditions
   * system default changes
5. Детерминированные решения **только через reconcile loop**

Любое отклонение — **архитектурная ошибка**.

---

## 3. Архитектурная модель (кратко)

### Input

* `sounddevice.InputStream`
* mono / 16 kHz
* callback = heartbeat
* Google SR работает **только на буферах**

### Output

* `AVAudioEngine`
* native device format
* отдельная persistent queue
* recreate вместо hot-switch

### Decision Layer

* `AudioRouteManager`
* single-flight reconcile
* per-device debounce
* explicit state machines

---

## 4. Структура реализации (обязательная)

```
modules/
 └─ voice_recognition/
    └─ core/
       └─ avfoundation/
          ├─ contracts.py
          ├─ mapping.py
          ├─ debounce_manager.py
          ├─ decision_engine.py
          ├─ reconcile_engine.py
          ├─ route_manager.py
          ├─ input_state_machine.py
          ├─ output_state_machine.py
          └─ adapters/
             ├─ avf_monitor.py
             ├─ avf_output.py
             └─ google_input.py
```

```
integration/
 └─ integrations/
    └─ audio_route_manager_integration.py
```

---

## 5. Reconcile как единственная точка решений

### Запрещено

* логика в event-handlers
* прямые реакции на device events

### Разрешено

* event → trigger → `reconcile_routes()`

### Алгоритм (обязателен)

```
1. Snapshot
2. Desired route
3. Mapping
4. Compare
5. Decision
6. Apply
7. Emit events
```

---

## 6. State Machines (обязательные)

### Input

```
STOPPED → STARTING → ACTIVE → STOPPING → STOPPED
                ↓
              FAILED
```

* start timeout: 2.5s
* retries: 3
* backoff: 1s → 2s → 4s
* max 6 рестартов / 10 минут

### Output

```
READY → RECREATING → READY
        ↓
      ERROR
```

* recreate timeout: 1.5s
* retries: 2

---

## 7. Queue & Playback Guarantees

* очередь живёт независимо от AVAudioEngine
* chunk удаляется **только после completion**
* лимиты:

  * 5000 ms
  * 5 MB

Overflow:

* DROP_OLDEST
* priority chunks сохраняются
* RECREATING >2s → PAUSE_FEEDING

---

## 8. Error States (обязательные)

### MIC_BUSY

* микрофон занят другим приложением
* retry ×3
* затем state = MIC_BUSY + user feedback

### NO_INPUT_AVAILABLE

* нет доступных input-устройств
* агрессивные retry запрещены

---

## 9. Latency SLA

### Input switch

* Built-in ≤600 ms
* USB ≤800 ms
* Bluetooth ≤1200 ms (≤2000 допустимо)

### Output recreate

* ≤600 ms (≤900 допустимо)

UI/voice feedback — **только если >700 ms**.

---

## 10. CI / QA требования (обязательные)

Перед **каждым PR** и **каждым мерджем** обязателен полный проход CI-чеклиста:

* линтеры
* unit tests ≥80%
* integration tests
* pairwise tests
* feature flags validation
* pre-build gate

**Подробный перечень требований**: `Docs/AUDIO_MIGRATION_CI_CHECKLIST.md`

---

## 11. PR-модель реализации (обязательная)

* 9 PR
* 9 этапов
* feature flags по умолчанию `false`
* каждый PR мержится независимо

**Пошаговый план по дням**: `Docs/AUDIO_MIGRATION_PR_PLAN.md`

---

## 12. Документация и артефакты

Обязательные артефакты:

* `Docs/AUDIO_MIGRATION_SPECIFICATION.md` — детальная спецификация
* `Docs/AUDIO_MIGRATION_CI_CHECKLIST.md` — CI/QA требования
* `Docs/AUDIO_MIGRATION_PR_PLAN.md` — пошаговый план реализации
* `Docs/STATE_CATALOG.md` — оси состояния
* `config/interaction_matrix.yaml` — правила взаимодействия
* `Docs/ADRs/ADR_2025-01-XX_avfoundation_audio_migration.md` — архитектурное решение
* `.impact/change_impact_avfoundation_audio.yaml` — оценка влияния

**Связанные документы**:

* `Docs/AUDIO_SYSTEM_LOGIC_SCHEMA.md` — схемы работы логики
* `Docs/AUDIO_MIGRATION_COMPLETE_IMPLEMENTATION_PLAN.md` — полный план реализации
* `Docs/AUDIO_MIGRATION_FULL_FILE_CHECKLIST.md` — чек-лист всех файлов

---

## 13. Финальное положение

Этот документ:

* завершён;
* согласован;
* обязателен;
* является **единственным source of truth**.

Любая реализация, не соответствующая данному документу и связанным артефактам, считается **архитектурно некорректной** и не допускается к релизу.

---

**Конец документа.**

