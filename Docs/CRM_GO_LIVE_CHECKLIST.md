# CRM Go-Live Checklist v2.1

**Registry ID:** INS-009  
**Status:** Active  
**Source of Truth:** [CRM_CONSOLIDATED_RULES.md](./CRM_CONSOLIDATED_RULES.md)

---

## 📋 1. Правила (Design)

- [ ] `CRM_CONSOLIDATED_RULES.md` объявлен immutable
- [ ] Изменения правил → только через `type: decision`

---

## ⚙️ 2. Механизмы (Implementation)

### 2.1 Data Reliability
- [x] `meta.revision` добавлен в `PROJECT_KANBAN.json`
- [x] HTTP 409 при `revision mismatch` в `/api/save`
- [x] Atomic write (temp → rename)
- [x] Backup before save

### 2.2 Audit & Tracking
- [x] Append-only `CRM_AUDIT_LOG.ndjson` создан
- [ ] Ротация audit log настроена

### 2.3 Snapshot
- [x] `project_state` генерируется в `task_aggregator.py`
- [x] Snapshot включает goals/problems/risks/blockers

### 2.4 WIP Limits
- [x] Enforcement: max 1 `in_progress` per workspace
- [x] Enforcement: max 1 `testing` per workspace

---

## 🤖 3. Ассистенты (Sync)

- [x] System prompts обновлены:
  - [x] Обязательный snapshot-read
  - [x] Noise control правила
  - [x] Handoff контракт
  - [x] Запрет "тихих фиксов"
- [x] Поведение при HTTP 409 документировано
- [x] Все ассистенты знают `CRM_CONSOLIDATED_RULES.md`

---

## 🩺 4. Диагностика

- [x] `scripts/crm_doctor.py` создан
- [x] Проверяет:
  - [x] Schema + инварианты
  - [x] Циклы `blockedBy`
  - [x] Битые `registry_ref`
  - [x] Несоответствие ID ↔ workspace
  - [x] Превышение WIP-лимитов

---

## 🧪 5. Smoke Tests

### Сценарий 1: Конфликт (409)
- [ ] Ассистент A и B правят одну задачу
- [ ] Один получает 409
- [ ] Корректно перечитывает snapshot
- [ ] Отказывается/адаптируется

### Сценарий 2: Шум (Noise Control)
- [ ] Ассистент создаёт документ без влияния
- [ ] НЕ создаётся задача
- [ ] Фиксируется note или audit

### Сценарий 3: Блокер
- [ ] Задача заблокирована
- [ ] Ассистент не начинает работу
- [ ] Создаёт blocker / decision / escalation

---

## ✅ 6. Go-Live Criteria

**CRM v2.1 считается готовой к эксплуатации, когда:**

1. Все пункты 1-5 выполнены
2. Все 3 smoke-теста пройдены
3. `crm_doctor.py` не находит ошибок

---

## 📊 Progress Tracking

Прогресс автоматически считается через `kanban_progress_collector.py`:
- Текущий: **23/32** пунктов
- Статус: **in_progress**
