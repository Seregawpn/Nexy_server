# 📋 ПЛАН МИГРАЦИИ: ТОЛЬКО server/ В КОРНЕ РЕПОЗИТОРИЯ

**Дата:** 5 ноября 2025  
**Цель:** Преобразовать репозиторий так, чтобы корень содержал ТОЛЬКО содержимое `server/`

---

## 🔍 АНАЛИЗ ТЕКУЩЕЙ СИТУАЦИИ

### Статистика:
- **Файлов в корне (не в server/):** 126
- **Файлов в server/:** 168
- **Дубликаты файлов:** 9 файлов

### Дубликаты (есть и в корне, и в server/):
1. `.cursorrules`
2. `.gitignore`
3. `Docs/ARCHITECTURE_OVERVIEW.md`
4. `Docs/CURRENT_STATUS_REPORT.md`
5. `Docs/GLOBAL_DELIVERY_PLAN.md`
6. `Docs/GO_TO_MARKET_BETA_PLAN_RU.md`
7. `Docs/PACKAGING_FINAL_GUIDE.md`
8. `Docs/PRODUCT_CONCEPT.md`
9. `README.md`
10. `SCALING_100_USERS_GUIDE.md`

### Файлы только в корне (нужно удалить или переместить):
- `LICENSE`
- `RELEASE_MANAGEMENT.md`
- `SECURITY.md`
- `VERSION_3.8.0_RELEASE_REPORT.md`
- `CLEANUP_REPORT.md`
- `__init__.py`
- `config/` (дублируется с `server/config/`)
- `integrations/` (дублируется с `server/integrations/`)
- `modules/` (дублируется с `server/modules/`)
- `main.py` (дублируется с `server/main.py`)
- `monitoring/` (дублируется с `server/monitoring/`)
- `requirements.txt` (дублируется с `server/requirements.txt`)
- `scripts/` (есть только в корне)
- `updates/` (есть только в корне)
- `utils/` (дублируется с `server/utils/`)
- `.github/workflows/` (есть только в корне)

---

## ✅ ПЛАН ДЕЙСТВИЙ (пошагово)

### **ЭТАП 1: ПОДГОТОВКА (5 минут)**

1. **Создать backup:**
   ```bash
   cd /Users/sergiyzasorin/Library/Mobile\ Documents/com~apple~CloudDocs/Development/Nexy
   BACKUP_DIR="/tmp/nexy_backup_$(date +%Y%m%d_%H%M%S)"
   git clone --mirror . "$BACKUP_DIR.git"
   echo "✅ Backup создан: $BACKUP_DIR.git"
   ```

2. **Проверить текущее состояние:**
   ```bash
   git status
   git branch -a
   git tag -l
   ```

3. **Убедиться, что нет несохраненных изменений:**
   ```bash
   git diff-index --quiet HEAD -- || echo "⚠️ Есть несохраненные изменения!"
   ```

---

### **ЭТАП 2: АНАЛИЗ ДУБЛИКАТОВ (10 минут)**

1. **Сравнить версии дубликатов:**
   - Определить, какие версии актуальнее (вероятно, из `server/`)
   - Проверить даты модификации
   - Проверить размеры файлов

2. **Определить стратегию:**
   - Оставить версии из `server/` (они актуальнее)
   - Удалить дубликаты из корня
   - Переместить уникальные файлы из корня в `server/` (если нужно)

---

### **ЭТАП 3: УДАЛЕНИЕ ДУБЛИКАТОВ ИЗ КОРНЯ (5 минут)**

1. **Удалить дубликаты из Git индекса:**
   ```bash
   # Удалить дубликаты файлов
   git rm .cursorrules .gitignore README.md __init__.py main.py requirements.txt
   git rm -r config/ integrations/ modules/ monitoring/ utils/
   ```

2. **Удалить дубликаты документации:**
   ```bash
   git rm Docs/ARCHITECTURE_OVERVIEW.md
   git rm Docs/CURRENT_STATUS_REPORT.md
   git rm Docs/GLOBAL_DELIVERY_PLAN.md
   git rm Docs/GO_TO_MARKET_BETA_PLAN_RU.md
   git rm Docs/PACKAGING_FINAL_GUIDE.md
   git rm Docs/PRODUCT_CONCEPT.md
   git rm SCALING_100_USERS_GUIDE.md
   ```

---

### **ЭТАП 4: ПЕРЕМЕЩЕНИЕ СОДЕРЖИМОГО server/ В КОРЕНЬ (10 минут)**

1. **Переместить всё из server/ в корень:**
   ```bash
   # Переместить все файлы и папки
   mv server/* .
   mv server/.* . 2>/dev/null || true
   
   # Удалить пустую папку server/
   rmdir server/
   ```

2. **Обновить Git индекс:**
   ```bash
   # Добавить все перемещенные файлы
   git add -A
   
   # Проверить статус
   git status
   ```

---

### **ЭТАП 5: ОБРАБОТКА УНИКАЛЬНЫХ ФАЙЛОВ ИЗ КОРНЯ (5 минут)**

1. **Файлы, которые есть только в корне:**
   - `LICENSE` → переместить в `server/` или оставить в корне
   - `RELEASE_MANAGEMENT.md` → переместить в `server/Docs/` или удалить
   - `SECURITY.md` → проверить, есть ли в `server/Docs/`
   - `VERSION_3.8.0_RELEASE_REPORT.md` → переместить в `server/Docs/` или удалить
   - `CLEANUP_REPORT.md` → удалить (временный файл)
   - `scripts/` → проверить, есть ли в `server/scripts/`
   - `updates/` → проверить, есть ли в `server/updates/`
   - `.github/workflows/` → переместить в корень (важно для CI/CD)

2. **Действия:**
   - Переместить нужные файлы в соответствующие места
   - Удалить временные файлы
   - Обновить `.gitignore` если нужно

---

### **ЭТАП 6: КОММИТ ИЗМЕНЕНИЙ (5 минут)**

1. **Закоммитить изменения:**
   ```bash
   git add -A
   git commit -m "refactor: move server/ content to repository root

   - Перемещено содержимое server/ в корень репозитория
   - Удалены дубликаты файлов из корня
   - Обновлена структура репозитория для соответствия документации
   - Теперь корень репозитория = серверная часть"
   ```

2. **Проверить результат:**
   ```bash
   git ls-files | head -20
   git log --oneline -1
   ```

---

### **ЭТАП 7: ОБНОВЛЕНИЕ ВСЕХ ВЕТОК (15 минут)**

1. **Обновить текущую ветку:**
   ```bash
   git push --force origin server-only
   ```

2. **Обновить все остальные ветки:**
   ```bash
   for branch in $(git branch -r | grep -v HEAD | sed 's/origin\///'); do
     git checkout $branch
     git rebase server-only
     git push --force origin $branch
   done
   ```

3. **Обновить теги:**
   ```bash
   git push --force --tags origin
   ```

---

### **ЭТАП 8: ПРОВЕРКА И ФИНАЛИЗАЦИЯ (10 минут)**

1. **Проверить структуру:**
   ```bash
   ls -la
   git ls-files | head -20
   ```

2. **Проверить GitHub:**
   - Открыть https://github.com/Seregawpn/Nexy_server
   - Проверить, что отображается только содержимое server/
   - Проверить, что нет лишних файлов

3. **Проверить GitHub Actions:**
   - Проверить, что workflows работают
   - Обновить пути в workflows если нужно

---

## ⚠️ ВАЖНЫЕ ЗАМЕЧАНИЯ

1. **GitHub Actions workflows:**
   - После перемещения пути могут измениться
   - Проверить `.github/workflows/*.yml`
   - Обновить пути если нужно

2. **Документация:**
   - Проверить ссылки на пути в документации
   - Обновить если нужно

3. **Скрипты:**
   - Проверить пути в скриптах
   - Обновить если нужно

4. **Backup:**
   - Сохранить backup до проверки работы
   - Удалить только после успешной проверки

---

## 📊 РЕЗУЛЬТАТ

После выполнения всех этапов:
- ✅ Корень репозитория = содержимое `server/`
- ✅ Нет дубликатов файлов
- ✅ В GitHub отображается только серверная часть
- ✅ История Git сохранена
- ✅ Все ветки и теги обновлены

---

## 🔄 ОТКАТ (если что-то пошло не так)

```bash
# Восстановить из backup
cd /tmp
git clone nexy_backup_YYYYMMDD_HHMMSS.git nexy_restore
cd nexy_restore
git remote add origin https://github.com/Seregawpn/Nexy_server.git
git push --force --all origin
git push --force --tags origin
```

