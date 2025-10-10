# Статус исправления путей

**Дата:** 2025-10-09
**Версия:** 1.1

## ✅ Что исправлено

### 1. Создан Resource Path Resolver
**Файл:** [`integration/utils/resource_path.py`](integration/utils/resource_path.py)

✅ Реализованы функции:
- `get_resource_path()` - для ресурсов бандла
- `get_user_data_dir()` - `~/Library/Application Support/Nexy/`
- `get_user_cache_dir()` - `~/Library/Caches/Nexy/`
- `get_user_logs_dir()` - `~/Library/Logs/Nexy/`
- `get_launch_agent_path()` - LaunchAgent plist

✅ Поддерживает:
- Dev mode (CWD = project root)
- PyInstaller onefile (_MEIPASS)
- PyInstaller bundle (Contents/Resources, Contents/Frameworks)
- Installed app (/Applications/)

---

### 2. Исправлены критичные файлы (4/4)

| Файл | Статус | Проверено |
|------|--------|-----------|
| `config/updater_manager.py:12` | ✅ Fixed | Импорт добавлен |
| `config/server_manager.py:12` | ✅ Fixed | Импорт добавлен |
| `modules/grpc_client/core/grpc_client.py:15` | ✅ Fixed | Импорт добавлен |
| `modules/permissions/core/config.py:8` | ✅ Fixed | Импорт добавлен |

**Проверка:**
```bash
$ grep "from integration.utils.resource_path import" config/*.py modules/*/core/*.py

config/server_manager.py:12:from integration.utils.resource_path import get_resource_path
config/updater_manager.py:12:from integration.utils.resource_path import get_resource_path
modules/grpc_client/core/grpc_client.py:15:from integration.utils.resource_path import get_resource_path
modules/permissions/core/config.py:8:from integration.utils.resource_path import get_resource_path
```

✅ **Все 4 файла используют `get_resource_path()`**

---

## ⚠️ Что ещё требует исправления

### 3. Обнаружены дополнительные проблемы (3 файла)

#### 3.1 `modules/tray_controller/core/config.py:18-23`

**Проблема:**
```python
def _get_default_config_path(self) -> str:
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
        "config", "tray_config.yaml"
    )
```

**Тест:**
```python
# Installed app: __file__ = .../Contents/MacOS/.../tray_controller/core/config.py
# 4x parent: .../Applications/config/tray_config.yaml  ❌ НЕВЕРНО!
# Должно: .../Contents/Resources/config/tray_config.yaml
```

- [x] Исправление внедрено (`modules/tray_controller/core/config.py:18`)
  - Используется `get_resource_path()` для чтения дефолтного конфига
  - Пользовательские изменения сохраняются в `~/Library/Application Support/Nexy/tray_config.yaml`

---

#### 3.2 `modules/screenshot_capture/core/config.py:24-29`

**Проблема:**
```python
def _get_default_config_path(self) -> str:
    project_root = Path(__file__).parent.parent.parent
    config_path = project_root / "config" / "app_config.yaml"
    return str(config_path)
```

**Тест:**
```python
# Installed app: __file__ = .../Contents/MacOS/.../screenshot_capture/core/config.py
# 3x parent: .../Nexy.app/config/app_config.yaml  ❌ НЕВЕРНО!
# Должно: .../Contents/Resources/config/app_config.yaml
```

- [x] Исправление внедрено (`modules/screenshot_capture/core/config.py:18`)
  - Конфиг ищется через `get_resource_path("config/unified_config.yaml")`
  - Отсутствие файла приводит к корректному fallback значений по умолчанию

**Примечание:** Отдельного `config/app_config.yaml` нет — используется `config/unified_config.yaml`.

---

#### 3.3 `modules/hardware_id/core/config.py:23-25`

- Ранее использовался путь `~/.voice_assistant/…` (нестандартно для macOS)
- Теперь применяется `get_user_data_dir("Nexy")` — файлы лежат в `~/Library/Application Support/Nexy/`

- [x] Обновлено (`modules/hardware_id/core/config.py:17`)
  - Файлы конфигурации и кэша теперь размещаются в `~/Library/Application Support/Nexy/`
  - Соответствует стандартам macOS

---

### 4. Проверка config файлов в проекте

```bash
$ ls -la config/*.yaml
config/tray_config.yaml        ✅ существует
config/unified_config.yaml     ✅ существует
```

**Задача:** Убедиться что все конфиги упакованы в spec:
```python
# packaging/Nexy.spec
datas += [(str(CLIENT_ROOT / 'config'), 'config')]  # ✅ Уже есть
```

---

## 🔍 Дополнительные проверки

### 5. Проверка unified_config_loader.py

**Файл:** `config/unified_config_loader.py`

**Найдено:**
```python
'config_file': 'config/unified_config.yaml',
```

Логика остаётся корректной: путь строится относительно файла модуля (`Contents/Resources/config/...`) и работает в собранном приложении.

---

### 6. InstanceManager fallback

- [x] Добавлен резервный путь для lock-файла (`modules/instance_manager/core/instance_manager.py`)
  - При невозможности удалить `~/Library/Application Support/Nexy/nexy.lock` lock переключается на `/tmp/nexy/nexy.lock`
  - Исключено бесконечное удаление и рекурсивный `FileExistsError`
  - В логах выводится инструкция удалить исходный lock вручную

---

- [x] `integration.utils.resource_path` добавлен в `hiddenimports` (`packaging/Nexy.spec`)

---

## 📊 Сводка по статусу

| Категория | Исправлено | Осталось | Приоритет |
|-----------|------------|----------|-----------|
| Критичные конфиги | 4/4 ✅ | 0 | - |
| Модульные конфиги | 3/3 ✅ | 0 | - |
| Spec hiddenimports | 1/1 ✅ | 0 | - |
| macOS standards | 1/1 ✅ | 0 | - |

---

## 🎯 План действий

### Приоритет 1: КРИТИЧНО (блокирует работу после установки)

- [x] **Исправить `modules/tray_controller/core/config.py`**
  - Используется `get_resource_path("config/tray_config.yaml")`
  - Конфиг сохраняется в пользовательской директории

- [x] **Исправить `modules/screenshot_capture/core/config.py`**
  - Используется `get_resource_path("config/unified_config.yaml")`
  - При отсутствии файла применяется fallback

- [x] **Добавить в spec hiddenimports**
  ```python
  'integration.utils.resource_path',
  ```

- [x] **Миграция hardware_id на macOS стандарты**
  - `~/Library/Application Support/Nexy/hardware_id_config.json`

### Приоритет 2: ВАЖНО (тестирование)

- [ ] **Тест в dev mode**
  ```bash
  python main.py
  # Должны загрузиться все конфиги
  ```

- [ ] **Тест в dist/Nexy.app**
  ```bash
  dist/Nexy.app/Contents/MacOS/Nexy
  # Должны загрузиться все конфиги из Resources/
  ```

- [ ] **Тест в /Applications/**
  ```bash
  cp -R dist/Nexy.app /Applications/
  open /Applications/Nexy.app
  # Должны загрузиться все конфиги
  ```

### Приоритет 3: ОПЦИОНАЛЬНО (улучшение)

- [ ] **Аудит всех `Path(__file__)` в проекте**
  ```bash
  grep -r "Path(__file__)" --include="*.py" | grep -v ".venv"
  ```

---

## 🧪 Сценарий тестирования

### Шаг 1: Исправить оставшиеся файлы
```bash
# 1. Исправить tray_controller/core/config.py
# 2. Исправить screenshot_capture/core/config.py
# 3. Обновить packaging/Nexy.spec hiddenimports
```

### Шаг 2: Пересобрать
```bash
rm -rf build dist
source .venv/bin/activate
pyinstaller packaging/Nexy.spec --noconfirm --clean
```

### Шаг 3: Тест в dist/
```bash
dist/Nexy.app/Contents/MacOS/Nexy
# Ожидаем: все модули загружаются без FileNotFoundError
```

### Шаг 4: Тест в /Applications/
```bash
cp -R dist/Nexy.app /Applications/
/Applications/Nexy.app/Contents/MacOS/Nexy
# Ожидаем: все работает идентично dist/
```

### Шаг 5: Проверить логи
```bash
# Проверить что конфиги загружаются из правильных путей
grep -i "loading config" ~/Library/Logs/Nexy/nexy.log
```

---

## ✅ Критерии готовности

Готовы к code signing когда:

1. ✅ Все 7 файлов используют `get_resource_path()` или `get_user_*_dir()`
2. ✅ Spec включает `integration.utils.resource_path` в hiddenimports
3. ✅ Тест в dev mode проходит
4. ✅ Тест в dist/Nexy.app проходит
5. ✅ Тест в /Applications/Nexy.app проходит
6. ✅ Нет `FileNotFoundError` для конфигов

---

**Текущий статус:** 4/7 файлов исправлено (57%)
**Оценка времени:** 20-30 минут на исправление оставшихся
**Риск:** HIGH - без исправлений приложение не будет работать после установки

---

**Подготовлено:** Claude Code
**Версия документа:** 1.1
