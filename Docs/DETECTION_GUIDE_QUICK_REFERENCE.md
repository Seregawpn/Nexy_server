# ⚡ Быстрая справка: Выявление дублирования, конфликтов и race conditions

**ЦЕЛЬ**: Быстрая справка с командами для выявления дублирования, конфликтов и race conditions.

**ВАЖНО**: Для детальной инструкции см. `DETECTION_GUIDE_DUPLICATES_CONFLICTS_RACES.md`.

**Дата создания**: 2025-01-XX  
**Версия**: 1.0

---

## 🔍 Дублирование кода

### Поиск функции по имени
```bash
grep -r "function_name" . --include="*.py"
```

### Семантический поиск
```python
codebase_search("How is functionality implemented?")
```

### Поиск в утилитах
```bash
grep -r "function_name" modules/*/utils/*.py
grep -r "function_name" integration/core/*.py
```

---

## ⚔️ Конфликты

### Поиск переменной/функции/класса
```bash
grep -r "variable_name\|function_name\|ClassName" . --include="*.py"
```

### Поиск управления состоянием
```bash
grep -r "\.state\s*=\|_state\s*=\|set_state" . --include="*.py"
```

### Проверка источника истины
```bash
grep -r "axis_name\|state_name" Docs/STATE_CATALOG.md
```

---

## 🏃 Race conditions

### Поиск общих данных
```bash
grep -r "self\._[a-z_]*\s*=" . --include="*.py"
```

### Поиск потоков
```bash
grep -r "callback\|threading\|async def" . --include="*.py"
```

### Поиск блокировок
```bash
grep -r "threading\.Lock\|asyncio\.Lock\|Lock()" . --include="*.py"
grep -r "with.*lock\|with.*Lock" . --include="*.py" -i
```

### Поиск async задач
```bash
grep -r "asyncio\.create_task\|create_task" . --include="*.py"
grep -r "_task\s*=\|\.task\s*=" . --include="*.py"
```

---

## 📚 Детальная инструкция

См. `DETECTION_GUIDE_DUPLICATES_CONFLICTS_RACES.md` для:
- Детальных методов выявления
- Примеров из реального проекта
- Автоматизированных скриптов проверки
- Полных чек-листов проверки

---

**Версия**: 1.0  
**Дата создания**: 2025-01-XX


