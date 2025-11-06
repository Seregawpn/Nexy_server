# ✅ ФИНАЛЬНЫЙ ПЛАН МИГРАЦИИ: ТОЛЬКО server/ В КОРНЕ

**Дата:** 5 ноября 2025  
**Статус:** Готов к выполнению

---

## 📊 АНАЛИЗ РЕЗУЛЬТАТОВ

### Версии файлов (server/ актуальнее):
- `.cursorrules`: server/ больше (309 строк vs 207 строк) ✅
- `README.md`: server/ больше (217 строк vs 171 строка) ✅
- `main.py`: server/ больше (259 строк vs 95 строк) ✅
- `requirements.txt`: одинаковые ✅
- `.gitignore`: корень больше (78 строк vs 49 строк) ⚠️

### Важные файлы только в корне:
- `.github/workflows/` - **ВАЖНО** для CI/CD, нужно сохранить ✅
- `LICENSE` - можно оставить
- `RELEASE_MANAGEMENT.md` - можно переместить в Docs/
- `SECURITY.md` - проверить, есть ли в server/Docs/
- `CLEANUP_REPORT.md` - временный, можно удалить

---

## 🎯 ПЛАН ДЕЙСТВИЙ (пошагово)

### **ШАГ 1: ПОДГОТОВКА И BACKUP**

```bash
cd /Users/sergiyzasorin/Library/Mobile\ Documents/com~apple~CloudDocs/Development/Nexy

# Создать backup
BACKUP_DIR="/tmp/nexy_backup_$(date +%Y%m%d_%H%M%S)"
git clone --mirror . "$BACKUP_DIR.git"
echo "✅ Backup: $BACKUP_DIR.git"

# Проверить состояние
git status
git branch -a
```

**Ожидаемый результат:** Backup создан, состояние проверено

---

### **ШАГ 2: УДАЛЕНИЕ ДУБЛИКАТОВ ИЗ КОРНЯ**

```bash
# Удалить дубликаты файлов (версии из server/ актуальнее)
git rm .cursorrules README.md main.py requirements.txt

# Удалить дубликаты директорий
git rm -r config/ integrations/ modules/ monitoring/ utils/

# Удалить дубликаты документации
git rm Docs/ARCHITECTURE_OVERVIEW.md \
        Docs/CURRENT_STATUS_REPORT.md \
        Docs/GLOBAL_DELIVERY_PLAN.md \
        Docs/GO_TO_MARKET_BETA_PLAN_RU.md \
        Docs/PACKAGING_FINAL_GUIDE.md \
        Docs/PRODUCT_CONCEPT.md \
        SCALING_100_USERS_GUIDE.md

# .gitignore - оставить версию из корня (она больше и актуальнее)
# Или объединить обе версии
```

**Ожидаемый результат:** Дубликаты удалены из Git индекса

---

### **ШАГ 3: ПЕРЕМЕЩЕНИЕ СОДЕРЖИМОГО server/ В КОРЕНЬ**

```bash
# Переместить всё из server/ в корень
mv server/* .
mv server/.* . 2>/dev/null || true

# Удалить пустую папку server/
rmdir server/

# Обновить Git индекс
git add -A
git status
```

**Ожидаемый результат:** Содержимое server/ перемещено в корень

---

### **ШАГ 4: ОБРАБОТКА УНИКАЛЬНЫХ ФАЙЛОВ**

```bash
# Скопировать .github/workflows/ в корень (если его нет)
# (Он уже есть в корне, так что ничего не делать)

# Проверить, есть ли LICENSE в server/
if [ ! -f "LICENSE" ]; then
  # Если нет, можно оставить в корне или переместить
  echo "LICENSE уже в корне"
fi

# Удалить временные файлы
git rm CLEANUP_REPORT.md 2>/dev/null || true

# Обновить .gitignore (объединить версии из корня и server/)
# (Оставить версию из корня, она актуальнее)
```

**Ожидаемый результат:** Уникальные файлы обработаны

---

### **ШАГ 5: КОММИТ ИЗМЕНЕНИЙ**

```bash
git add -A
git commit -m "refactor: move server/ content to repository root

- Перемещено содержимое server/ в корень репозитория
- Удалены дубликаты файлов из корня (версии из server/ актуальнее)
- Сохранены уникальные файлы из корня (.github/workflows/, LICENSE)
- Обновлена структура репозитория для соответствия документации
- Теперь корень репозитория = серверная часть"
```

**Ожидаемый результат:** Изменения закоммичены

---

### **ШАГ 6: ОБНОВЛЕНИЕ ВСЕХ ВЕТОК**

```bash
# Обновить текущую ветку
git push --force origin server-only

# Обновить главную ветку
git checkout main
git rebase server-only
git push --force origin main

# Обновить все остальные ветки
for branch in $(git branch -r | grep -v HEAD | sed 's/origin\///' | grep -v "server-only" | grep -v "main"); do
  git checkout $branch
  git rebase server-only
  git push --force origin $branch
done

# Вернуться на server-only
git checkout server-only
```

**Ожидаемый результат:** Все ветки обновлены

---

### **ШАГ 7: ОБНОВЛЕНИЕ ТЕГОВ**

```bash
git push --force --tags origin
```

**Ожидаемый результат:** Все теги обновлены

---

### **ШАГ 8: ПРОВЕРКА**

```bash
# Проверить структуру
ls -la
git ls-files | head -20

# Проверить, что нет папки server/
if [ -d "server" ]; then
  echo "⚠️ Папка server/ все еще существует!"
else
  echo "✅ Папка server/ удалена"
fi

# Проверить количество файлов
echo "Файлов в репозитории: $(git ls-files | wc -l)"
```

**Ожидаемый результат:** Структура корректна, нет папки server/

---

## ⚠️ ВАЖНЫЕ ЗАМЕЧАНИЯ

1. **GitHub Actions workflows:**
   - `.github/workflows/` уже в корне ✅
   - После перемещения пути могут измениться
   - Проверить workflows после выполнения

2. **.gitignore:**
   - Версия из корня больше (78 строк vs 49 строк)
   - Оставить версию из корня или объединить

3. **Backup:**
   - Сохранить backup до проверки работы
   - Удалить только после успешной проверки

---

## 📋 ЧЕКЛИСТ ПЕРЕД ВЫПОЛНЕНИЕМ

- [ ] Backup создан
- [ ] Состояние проверено (git status)
- [ ] Все ветки проверены (git branch -a)
- [ ] Все теги проверены (git tag -l)
- [ ] Нет несохраненных изменений
- [ ] Понятно, какие файлы удалить
- [ ] Понятно, какие файлы переместить
- [ ] Готов к force-push

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

---

## ✅ ОЖИДАЕМЫЙ РЕЗУЛЬТАТ

После выполнения всех шагов:
- ✅ Корень репозитория = содержимое `server/`
- ✅ Нет дубликатов файлов
- ✅ Нет папки `server/`
- ✅ В GitHub отображается только серверная часть
- ✅ История Git сохранена
- ✅ Все ветки и теги обновлены
- ✅ GitHub Actions workflows работают

