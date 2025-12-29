# Nexy Audio Migration

## Complete AVFoundation Implementation Document

**Статус:** FINAL / READY FOR IMPLEMENTATION  
**Версия:** 1.0  
**Платформа:** macOS  
**Технологии:** Python · PyObjC · AVFoundation · sounddevice · Google SR  
**Модель:** Reconcile-based Architecture  
**Готовность:** 100%

**Примечание**: Этот документ является детальной спецификацией. Главный нормативный документ: `Docs/AUDIO_MIGRATION_MASTER_SPECIFICATION.md`

---

## 0. Назначение документа

Данный документ является **полным и окончательным описанием реализации аудиосистемы Nexy** с переходом на AVFoundation для output и контролируемый Google Speech Recognition input.

Документ:

* заменяет любые устные договорённости;
* используется как **source of truth**;
* обязателен для реализации, ревью и тестирования;
* допускает только backward-compatible изменения.

---

## 1. Архитектурные гарантии

Система **гарантирует**:

* единственного владельца микрофона;
* отсутствие двойного input-захвата;
* корректную работу с Bluetooth / USB / Built-in;
* устойчивость к device storms и race conditions;
* управляемую деградацию при ошибках;
* детерминированные решения через reconcile loop.

---

## 2. Структура реализации

### Общая декомпозиция

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

## 3. Контракты данных (обязательные)

### DeviceSignature

* нормализованное имя
* transport (bluetooth / usb / built-in / unknown)
* количество каналов
* manufacturer hint (опционально)

### RouteSnapshot

* system default input
* desired input
* active input
* active output

### MappingResult

* device_index (или None)
* confidence (HIGH / MEDIUM / LOW / NONE)
* причина маппинга

---

## 4. Маппинг устройств

### Принципы

* AVFoundation → PortAudio
* нормализация имён
* Bluetooth aliases
* confidence-модель
* fallback на system default

### Кэш

* TTL: 24 часа или до disconnect
* кэш **не** повышает LOW/NONE до usable
* используется только для ранжирования

---

## 5. State Machines

### Input

```
STOPPED → STARTING → ACTIVE → STOPPING → STOPPED
                     ↓
                   FAILED
```

* timeout: 2.5s
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

## 6. Reconcile Loop (ядро системы)

### Гарантии

* single-flight
* pending-reconcile
* отсутствие логики в событиях

### Алгоритм

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

## 7. Debounce

Per-device debounce:

| Transport |              Initial | Increment |     Max |
| --------- | -------------------: | --------: | ------: |
| Bluetooth |               200 ms |   +200 ms | 1200 ms |
| USB       |               100 ms |   +100 ms |  600 ms |
| Built-in  |               100 ms |         — |  200 ms |
| Unknown   | Bluetooth worst-case |           |         |

---

## 8. Watchdog & Heartbeat

* heartbeat из `sounddevice.InputStream` callback
* timeout: 10s
* silence ≠ error
* превышение лимита → restart → fallback → FAILED

---

## 9. Output Queue

### Свойства

* очередь живёт отдельно от AVAudioEngine
* chunk_id, timestamp, priority
* удаление только после completion

### Лимиты

* 5000 ms
* 5 MB

### Overflow

* DROP_OLDEST
* priority chunks сохраняются
* RECREATING >2s → PAUSE_FEEDING

---

## 10. Error States

### MIC_BUSY

* микрофон занят другим приложением
* retry ×3
* затем user feedback

### NO_INPUT_AVAILABLE

* нет доступных устройств
* агрессивные retry запрещены

---

## 11. Latency SLA

### Input

* Built-in: ≤600 ms
* USB: ≤800 ms
* Bluetooth: ≤1200 ms (≤2000 ms допустимо)

### Output

* recreate ≤600 ms (≤900 ms допустимо)

UI feedback — только если >700 ms.

---

## 12. Integration Layer

### AudioRouteManagerIntegration

* feature flags
* kill-switch
* EventBus binding
* state_manager → DecisionContext
* callbacks:

  * input start / stop
  * output recreate

---

## 13. Тестирование

### Минимальные требования

* unit tests ≥80%
* integration tests
* сценарии:

  * Bluetooth disconnect during speech
  * output recreate mid-playback
  * MIC_BUSY
  * fallback to default

---

## 14. Финальное положение

Данный документ:

* завершён;
* согласован;
* готов к реализации;
* является обязательным.

Любая реализация, не соответствующая этому документу, считается **архитектурно некорректной**.

---

**Конец документа.**

