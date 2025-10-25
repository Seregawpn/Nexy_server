# 🚀 Система развертывания обновлений Nexy

## 🎯 Назначение
Автоматизированная система для развертывания обновлений через GitHub Releases с фиксированным тегом "Update".

---

## 📁 Файлы

### `deploy.sh` - Развертывание обновления
```bash
./deploy.sh Nexy.dmg
```

**Что делает:**
- ✅ Создает релиз с тегом "Update" в GitHub
- ✅ Загружает DMG файл в релиз
- ✅ Вычисляет размер и SHA256 хеш автоматически
- ✅ Обновляет манифест на Azure сервере
- ✅ Проверяет доступность файла
- ✅ Обновляет AppCast XML автоматически

---

## 🚀 Использование

### 1. Подготовка
```bash
# Установить GitHub CLI
brew install gh
gh auth login

# Установить Azure CLI
brew install azure-cli
az login

# Перейти в папку скриптов
cd scripts/

# Сделать скрипт исполняемым
chmod +x deploy.sh
```

### 2. Развертывание
```bash
# Развернуть обновление
./deploy.sh ../Nexy.dmg
```

**Готово!** Обновление развернуто.

### 3. Проверка результата
```bash
# Проверить доступность файла
curl -I https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg

# Проверить AppCast XML
curl -s http://20.151.51.172:8081/appcast.xml | grep -A 5 "enclosure"
```

---

## 🚨 Частые ошибки

### GitHub CLI не установлен
```
❌ GitHub CLI не установлен
```
**Решение:** `brew install gh && gh auth login`

### Azure CLI не установлен
```
❌ Azure CLI не установлен
```
**Решение:** `brew install azure-cli && az login`

### Файл не найден
```
❌ Файл не найден: Nexy.dmg
```
**Решение:** Проверьте путь к файлу

### Релиз уже существует
```
❌ Release Update already exists
```
**Решение:** 
```bash
# Удалить существующий релиз
gh release delete Update --repo Seregawpn/Nexy_production

# Или пересоздать релиз
gh release delete Update --repo Seregawpn/Nexy_production --yes
./deploy.sh ../Nexy.dmg
```

### Не авторизован в GitHub
```
❌ Не авторизован в GitHub CLI
```
**Решение:** `gh auth login`

### Не авторизован в Azure
```
❌ Не авторизован в Azure CLI
```
**Решение:** `az login`

---

## ✅ Успешное развертывание

```
🚀 Развертывание обновления...
✅ GitHub релиз создан
✅ Манифест обновлен на сервере
✅ AppCast XML обновлен

🎉 ОБНОВЛЕНИЕ РАЗВЕРНУТО УСПЕШНО!

📊 Результат:
   🏷️  Тег: Update
   📁 Файл: Nexy.dmg
   📏 Размер: 97356894 байт
   🔐 SHA256: e62a4571190d94e68a0c95a793729c96610e5c5267945b794f7dfa45bb9cf480
   🔗 GitHub: https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg
   🖥️  Сервер: http://20.151.51.172:8081

🔗 Ссылки:
   📥 Скачать: https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg
   📰 AppCast: http://20.151.51.172:8081/appcast.xml
   📋 Манифест: http://20.151.51.172:8081/manifests/manifest_1.0.0.json
   📁 Релиз: https://github.com/Seregawpn/Nexy_production/releases/tag/Update

✅ Система обновлений готова!
```

---

## 🔧 Требования

- ✅ **GitHub CLI** (`brew install gh && gh auth login`)
- ✅ **Azure CLI** (`brew install azure-cli && az login`)
- ✅ **DMG файл** готов к загрузке
- ✅ **Права доступа** к репозиторию `Seregawpn/Nexy_production`
- ✅ **Права доступа** к Azure VM `nexy-regular`

---

## 📝 Важные моменты

- **Тег релиза**: `Update` (фиксированный, перезаписывается при каждом развертывании)
- **Файлы**: DMG (любой размер, поддерживается до 2GB)
- **GitHub CDN**: Быстрая загрузка через глобальную сеть доставки
- **Автоматика**: Размер, SHA256, дата - все вычисляется автоматически
- **Безопасность**: SHA256 проверка целостности файлов
- **Совместимость**: macOS 11.0+ (Intel + Apple Silicon)

---

## 🎯 Результат

После развертывания:
- ✅ **GitHub релиз** создан с тегом `Update`
- ✅ **DMG файл** доступен по прямой ссылке
- ✅ **Azure сервер** обновлен с новой ссылкой
- ✅ **AppCast XML** обновлен автоматически
- ✅ **Клиенты** получают обновления через GitHub CDN
- ✅ **Проверка целостности** работает (SHA256)

**Система готова к использованию!**

---

## 🔄 Обновление существующего релиза

Если релиз `Update` уже существует:
```bash
# Удалить старый релиз
gh release delete Update --repo Seregawpn/Nexy_production --yes

# Создать новый
./deploy.sh ../Nexy.dmg
```

**Или просто перезаписать:**
```bash
# Скрипт автоматически перезапишет существующий релиз
./deploy.sh ../Nexy.dmg
```
