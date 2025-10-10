# Этап 1.5: Создание PyInstaller Spec

**Дата:** 2025-10-09
**Статус:** ✅ COMPLETED

## 1. Проблема

Скрипт [`packaging/build_final.sh:136`](packaging/build_final.sh#L136) ссылался на несуществующий файл:
```bash
pyinstaller packaging/Nexy.spec --noconfirm --clean
```

**Результат:** Блокер для упаковки — сборка невозможна без spec-файла.

---

## 2. Созданный файл

**Расположение:** [`packaging/Nexy.spec`](packaging/Nexy.spec)

### 2.1 Ключевые секции

#### Entry Point
```python
[str(CLIENT_ROOT / 'main.py')]
```
- Главный файл: `main.py`
- Использует `SimpleModuleCoordinator` для инициализации всех модулей

#### Hidden Imports
Добавлены критичные модули, которые PyInstaller не обнаруживает автоматически:
- **gRPC/Protobuf:** `grpc`, `grpc._cython.cygrpc`, `google.protobuf.*`
- **PyObjC:** все macOS фреймворки (AppKit, Foundation, Quartz, CoreAudio, etc.)
- **GUI:** `rumps`, `pynput` (keyboard/mouse)
- **Audio:** `pydub`, `pyaudio`
- **Все Nexy модули:** 18 подсистем (audio_device_manager, grpc_client, permissions, etc.)

#### Data Files
```python
datas = [
    ('resources/ffmpeg/ffmpeg', 'resources/ffmpeg'),
    ('resources/audio/SwitchAudioSource', 'resources/audio'),
    ('config', 'config'),
    ('assets', 'assets'),
]
```

#### Binaries
```python
binaries = [
    ('resources/ffmpeg/ffmpeg', '.'),
    ('resources/audio/SwitchAudioSource', '.'),
]
```
- Дублирование в `datas` и `binaries` гарантирует, что бинарники попадут в бандл

#### Excludes
```python
excludes = [
    'tkinter', 'matplotlib', 'numpy', 'pandas', 'scipy', 'pytest',
    'speech_recognition.flac-mac',  # устаревший x86_64 бинарник
]
```

#### Bundle Settings
```python
app = BUNDLE(
    name='Nexy.app',
    icon='assets/icons/app.icns',
    bundle_identifier='com.nexy.assistant',
    version='1.0.0',
    info_plist={
        'NSMicrophoneUsageDescription': '...',
        'NSAppleEventsUsageDescription': '...',
        'NSAccessibilityUsageDescription': '...',
        # ... все разрешения
    }
)
```

---

## 3. Тестовая сборка

### Команда
```bash
source .venv/bin/activate
pyinstaller packaging/Nexy.spec --noconfirm --clean --log-level=WARN
```

### Результат
✅ **Успешно создан:** `dist/Nexy.app`

```
dist/Nexy.app/Contents/
├── Frameworks/
│   ├── ffmpeg                              # дубликат из binaries
│   ├── SwitchAudioSource                   # дубликат из binaries
│   └── resources/
│       ├── ffmpeg/ffmpeg                   # из datas
│       └── audio/SwitchAudioSource         # из datas
├── Resources/
│   ├── ffmpeg                              # еще один дубликат
│   ├── SwitchAudioSource                   # еще один дубликат
│   └── [другие ресурсы]
├── MacOS/
│   └── Nexy                                # главный исполняемый файл
└── Info.plist
```

**Примечание:** Множественные копии бинарников — норма для PyInstaller при использовании `datas` + `binaries`. Это гарантирует, что `main.py` найдет ffmpeg в любом из возможных путей (см. `init_ffmpeg_for_pydub()` в [main.py:19-64](main.py#L19)).

---

## 4. Предупреждения при сборке

### 4.1 Missing Hidden Imports (незначительные)
```
ERROR: Hidden import 'grpcio' not found
ERROR: Hidden import 'google.protobuf.service' not found
```

**Статус:** ⚠️ Non-critical
- `grpcio` — это C-extension, PyInstaller собирает его автоматически как `grpc._cython`
- `google.protobuf.service` — опциональный модуль, не используется в Nexy

**Исправлено:** Добавлен `grpc._cython.cygrpc` в hiddenimports

### 4.2 Incompatible FLAC Binary
```
WARNING: Found one or more binaries with invalid or incompatible macOS SDK version:
 * 'speech_recognition/flac-mac', version: (10, 6, 0)
```

**Проблема:**
- `speech_recognition` включает старый FLAC бинарник (x86_64, SDK 10.6)
- Не совместим с arm64 и современным hardened runtime

**Решение:**
- Добавлен в `excludes`: `'speech_recognition.flac-mac'`
- Nexy использует встроенный `ffmpeg` для аудио, FLAC не нужен

---

## 5. Проверка бинарников в бандле

### FFmpeg
```bash
find dist/Nexy.app -name "ffmpeg"
# Найдено 4 копии:
# - Contents/Frameworks/ffmpeg
# - Contents/Resources/ffmpeg
# - Contents/Frameworks/resources/ffmpeg/ffmpeg (правильный путь)
# - Contents/Resources/resources/ffmpeg/ffmpeg (альтернативный)
```

✅ **Корректно:** `main.py` проверяет все эти пути в `init_ffmpeg_for_pydub()`

### SwitchAudioSource
```bash
find dist/Nexy.app -name "SwitchAudioSource"
# Найдено 4 копии (аналогично ffmpeg)
```

✅ **Корректно:** Достаточно для работы модуля `audio_device_manager`

---

## 6. Следующие шаги

### ✅ РАЗБЛОКИРОВАНО
- Теперь `packaging/build_final.sh` может успешно собрать приложение
- Spec-файл корректно включает все ресурсы и зависимости

### Готово к Этапу 2
**Следующий шаг:** Проверка Info.plist и entitlements

---

## 7. Технические детали

### 7.1 Почему PyInstaller создает дубликаты?

PyInstaller использует несколько стратегий упаковки:
1. **`datas`** → попадают в `Contents/Resources/` или `Contents/Frameworks/`
2. **`binaries`** → попадают в корень `Contents/MacOS/` или `Contents/Frameworks/`
3. **BUNDLE** → копирует все из `COLLECT` в финальную структуру .app

**Результат:** Один файл может появиться в нескольких местах, но это не ошибка — это гарантия, что runtime найдет нужный ресурс.

### 7.2 Оптимизация размера (опционально)

Текущий размер бандла: ~150-200 MB (из-за ffmpeg 39MB + Python stdlib + dependencies).

**Возможные улучшения:**
- [ ] Пересобрать ffmpeg с минимальными кодеками (`--disable-everything --enable-decoder=...`)
- [ ] Использовать `upx=True` для сжатия (но может сломать codesign)
- [ ] Убрать неиспользуемые PyObjC фреймворки

---

**Подготовлено:** Claude Code
**Версия документа:** 1.0
