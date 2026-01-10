# CRM Weekly Ritual (Manual for Humans)

> **Frequency:** Once per week (e.g. Friday)  
> **Role:** Director / Lead  
> **Duration:** 5-10 minutes

## 1. Запуск Housekeeping
Этот скрипт проверит "протухшие" задачи, битые ссылки и создаст задачи.

```bash
# 1. Запустить проверку (Dry Run)
python3 scripts/crm_housekeeper.py --dry-run
```

**Что проверить в выводе:**
- Есть ли задачи, которые будут помечены как `stale`?
- Есть ли `broken references`?

```bash
# 2. Применить изменения (если всё ок)
python3 scripts/crm_housekeeper.py
```

## 2. Проверка состояния через UI
Откройте `http://localhost:8000`:
1. **Views → Archived**: "Не накопилось ли здесь чего-то важного?"
2. **Top Blockers** (справа вверху): Есть ли блокирующие задачи?

## 3. Ручная синхронизация (если нужно)
Обычно происходит автоматически, но можно форсировать:
```bash
python3 scripts/task_aggregator.py
```

## 4. Очистка логов (Optional)
Если `CRM_AUDIT_LOG.ndjson` стал слишком большим (>10MB):
```bash
mv Docs/CRM_AUDIT_LOG.ndjson Docs/logs/audit_$(date +%F).ndjson
```

---
**Tip:** Если видите задачу `NEXY-XXX` с типом `problem` — это автоматический сигнал от системы (битая ссылка, нарушение правил). Не удаляйте её, а решите проблему.
