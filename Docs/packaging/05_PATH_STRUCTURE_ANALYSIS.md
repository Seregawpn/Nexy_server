# Анализ структуры путей для macOS приложения

**Дата:** 2025-10-09
**Статус:** ⚠️ ТРЕБУЕТ ИСПРАВЛЕНИЯ

## Проблема

При упаковке Nexy в `.app` бандл и установке в `/Applications/` обнаружены **критичные проблемы с путями**.

---

## 1. Структура macOS .app Bundle

### 1.1 Стандартная структура
```
Nexy.app/
├── Contents/
│   ├── Info.plist                    # Метаданные приложения
│   ├── MacOS/
│   │   └── Nexy                      # Исполняемый файл (CWD здесь!)
│   ├── Resources/                    # Ресурсы, иконки, Python пакеты
│   │   ├── config/
│   │   │   ├── unified_config.yaml
│   │   │   └── permissions_config.yaml
│   │   ├── assets/
│   │   └── [Python packages]
│   ├── Frameworks/                   # Бинарные библиотеки, native extensions
│   │   ├── resources/
│   │   │   ├── ffmpeg/ffmpeg
│   │   │   └── audio/
│   │   │       ├── SwitchAudioSource
│   │   │       └── flac
│   │   └── [dylibs]
│   └── _CodeSignature/               # Подпись приложения
```

### 1.2 Текущая рабочая директория (CWD)

**Важно:** Когда приложение запускается:
```bash
# Dev mode (из исходников)
CWD: /Users/.../Nexy/client/
Путь "config/unified_config.yaml" → /Users/.../Nexy/client/config/unified_config.yaml ✅

# Installed app (из /Applications/)
CWD: /Applications/Nexy.app/Contents/MacOS/
Путь "config/unified_config.yaml" → /Applications/Nexy.app/Contents/MacOS/config/unified_config.yaml ❌

# Правильный путь:
→ /Applications/Nexy.app/Contents/Resources/config/unified_config.yaml
```

---

## 2. Обнаруженные проблемы

### 2.1 Конфигурационные файлы

**Проблемные файлы:**
- [`config/updater_manager.py:44`](config/updater_manager.py#L44)
- [`config/server_manager.py`](config/server_manager.py)
- [`modules/permissions/core/config.py`](modules/permissions/core/config.py)
- [`modules/grpc_client/core/grpc_client.py`](modules/grpc_client/core/grpc_client.py)

**Код:**
```python
def __init__(self, config_path: str = "config/unified_config.yaml"):
    with open(config_path, 'r') as f:  # ❌ Относительный путь!
        self._config = yaml.safe_load(f)
```

**Проблема:**
```python
# Dev mode:
open("config/unified_config.yaml")  # ✅ Работает

# Installed app:
open("config/unified_config.yaml")  # ❌ FileNotFoundError
# Ищет в: /Applications/Nexy.app/Contents/MacOS/config/...
# Должен: /Applications/Nexy.app/Contents/Resources/config/...
```

---

### 2.2 Пользовательские данные

**Проблемные места:**
- [`modules/instance_manager/core/types.py:29`](modules/instance_manager/core/types.py#L29)

**Код:**
```python
lock_file: str = "~/Library/Application Support/Nexy/nexy.lock"
```

✅ **Правильно!** Использует `~` для home directory.

**НО:** Требуется `os.path.expanduser()` перед использованием:
```python
lock_path = os.path.expanduser(self.config.lock_file)  # ✅
lock_path = self.config.lock_file  # ❌ Литеральная строка "~/..."
```

---

### 2.3 LaunchAgent plist

**Файл:** [`modules/autostart_manager/macos/launch_agent.py:15`](modules/autostart_manager/macos/launch_agent.py#L15)

**Код:**
```python
self.plist_path = os.path.expanduser(config.launch_agent_path)
```

✅ **Правильно!** Использует `expanduser()`.

**Путь:**
```
~/Library/LaunchAgents/com.nexy.assistant.plist
```

✅ **Соответствует macOS стандартам**

---

## 3. Решение: Resource Path Resolver

### 3.1 Новый модуль

**Создан:** [`integration/utils/resource_path.py`](integration/utils/resource_path.py)

**API:**
```python
from utils.resource_path import (
    get_resource_path,      # Ресурсы бандла
    get_user_data_dir,      # ~/Library/Application Support/Nexy/
    get_user_cache_dir,     # ~/Library/Caches/Nexy/
    get_user_logs_dir,      # ~/Library/Logs/Nexy/
    get_launch_agent_path   # ~/Library/LaunchAgents/...
)
```

### 3.2 Как работает

```python
def get_resource_path(relative_path: str) -> Path:
    """
    Автоматически определяет правильный путь в зависимости от режима:

    1. PyInstaller onefile: sys._MEIPASS/relative_path
    2. PyInstaller bundle:  Contents/Resources/relative_path
                           или Contents/Frameworks/relative_path
    3. Dev mode:           project_root/relative_path
    4. Fallback:           cwd/relative_path
    """
```

**Пример использования:**
```python
# До:
with open("config/unified_config.yaml", 'r') as f:  # ❌

# После:
config_path = get_resource_path("config/unified_config.yaml")
with open(config_path, 'r') as f:  # ✅
```

---

## 4. Файлы требующие исправления

### 4.1 Критичные (блокируют работу)

1. **config/updater_manager.py:44**
   ```python
   # До:
   def __init__(self, config_path: str = "config/unified_config.yaml"):
       with open(config_path, 'r') as f:

   # После:
   from utils.resource_path import get_resource_path

   def __init__(self, config_path: str = "config/unified_config.yaml"):
       full_path = get_resource_path(config_path)
       with open(full_path, 'r') as f:
   ```

2. **config/server_manager.py** (аналогично)

3. **modules/permissions/core/config.py**

4. **modules/grpc_client/core/grpc_client.py** (2 места)

### 4.2 Важные (могут вызвать проблемы)

5. **modules/instance_manager/** - проверить expanduser()

6. **Все модули с `config/*.yaml`** - grep показал 13 файлов

---

## 5. Рекомендуемая структура директорий

### 5.1 Внутри бандла (read-only)

```
Nexy.app/Contents/
├── Resources/          # Конфиги приложения (read-only)
│   ├── config/
│   │   ├── unified_config.yaml
│   │   ├── permissions_config.yaml
│   │   └── tray_config.yaml
│   └── assets/
│       └── icons/
└── Frameworks/         # Бинарники (read-only)
    └── resources/
        ├── ffmpeg/ffmpeg
        └── audio/
            ├── SwitchAudioSource
            └── flac
```

**Доступ:** `get_resource_path("config/unified_config.yaml")`

### 5.2 Пользовательские данные (read-write)

```
~/Library/Application Support/Nexy/
├── nexy.lock                      # Instance lock
├── cache/                         # Hardware ID cache
│   └── hardware_id.json
└── user_config/                   # Переопределения конфигов (опционально)
    └── user_preferences.yaml

~/Library/Caches/Nexy/
└── [временные файлы]

~/Library/Logs/Nexy/
└── nexy.log

~/Library/LaunchAgents/
└── com.nexy.assistant.plist
```

**Доступ:**
- `get_user_data_dir()` - для постоянных данны��
- `get_user_cache_dir()` - для кеша
- `get_user_logs_dir()` - для логов

---

## 6. План миграции

### Приоритет 1 (КРИТИЧНО)
- [x] Исправить `config/updater_manager.py`
- [x] Исправить `config/server_manager.py`
- [x] Исправить `modules/grpc_client/core/grpc_client.py`
- [x] Исправить `modules/permissions/core/config.py`

### Приоритет 2 (ВАЖНО)
- [ ] Аудит всех `open()` с относительными путями
- [ ] Проверить `os.path.expanduser()` для `~/` путей
- [x] Добавить `integration/utils/resource_path.py` в spec hiddenimports

### Приоритет 3 (ТЕСТИРОВАНИЕ)
- [ ] Тест в dev mode
- [ ] Тест в dist/Nexy.app (до установки)
- [ ] Тест в /Applications/Nexy.app (после установки)
- [ ] Тест после перезагрузки macOS

---

## 7. Проверка после исправлений

### 7.1 Тестовый сценарий

```bash
# 1. Собрать приложение
pyinstaller packaging/Nexy.spec --noconfirm --clean

# 2. Копировать в /Applications/
cp -R dist/Nexy.app /Applications/

# 3. Запустить из /Applications/
open /Applications/Nexy.app

# 4. Проверить логи
tail -f ~/Library/Logs/Nexy/nexy.log

# 5. Проверить создание файлов
ls -la ~/Library/Application\ Support/Nexy/
```

### 7.2 Ожидаемый результат

✅ Приложение запускается без ошибок
✅ Конфиги загружаются из `Contents/Resources/config/`
✅ Lock file создаётся в `~/Library/Application Support/Nexy/`
✅ FFmpeg находится и работает
✅ Все модули инициализируются

---

## 8. Дополнительные рекомендации

### 8.1 Никогда не пишите в бандл!

❌ **Неправильно:**
```python
# Попытка записи в Contents/Resources/cache/
cache_file = get_resource_path("cache/data.json")
with open(cache_file, 'w') as f:  # PermissionError!
```

✅ **Правильно:**
```python
# Запись в пользовательскую директорию
cache_dir = get_user_cache_dir()
cache_file = cache_dir / "data.json"
with open(cache_file, 'w') as f:  # ✅
```

### 8.2 Используйте pathlib.Path

```python
from pathlib import Path
from integration.utils.resource_path import get_resource_path

# Современный способ
config = get_resource_path("config/unified_config.yaml")
with config.open('r') as f:  # ✅ Path поддерживает .open()
    data = yaml.safe_load(f)
```

### 8.3 Логирование путей

```python
import logging
logger = logging.getLogger(__name__)

config_path = get_resource_path("config/unified_config.yaml")
logger.debug(f"Loading config from: {config_path}")
logger.debug(f"Config exists: {config_path.exists()}")
```

---

## 9. Следующие шаги

**БЛОКЕР для релиза:** Без исправления путей приложение **не будет работать** после установки в /Applications/.

**Рекомендация:**
1. Исправить все 4 критичных файла
2. Добавить `integration/utils/resource_path.py` в spec
3. Пересобрать приложение
4. Провести тест в /Applications/
5. Только после этого переходить к code signing

---

**Подготовлено:** Claude Code
**Версия документа:** 1.0
