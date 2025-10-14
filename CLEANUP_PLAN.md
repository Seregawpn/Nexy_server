# План очистки старого модуля audio_device_manager

## Что удалить

### 1. Полностью удалить модуль audio_device_manager
```
modules/audio_device_manager/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── audio_device_interface.py
│   ├── device_manager.py
│   ├── device_monitor.py
│   ├── device_switcher.py
│   └── types.py
├── macos/
│   ├── __init__.py
│   ├── switchaudio_bridge.py
│   ├── CERTIFICATION_REQUIREMENTS.md
│   ├── PACKAGING_GUIDE.md
│   ├── QUICK_CHECKLIST.md
│   └── requirements/
├── config/
│   ├── __init__.py
│   └── device_priorities.py
└── INTEGRATION_GUIDE.md
```

### 2. Удалить интеграцию
```
integration/integrations/audio_device_integration.py
```

### 3. Удалить тесты
```
tests/modules/diagnostic_audio_device_manager.py
tests/integrations/diagnostic_audio_device_integration.py
```

## Что изменить

### 1. SimpleModuleCoordinator
- Убрать импорт `AudioDeviceIntegration`
- Убрать импорт `AudioDeviceManagerConfig`
- Убрать инициализацию `AudioDeviceIntegration`
- Добавить импорт `DefaultAudioIntegration` (позже)

### 2. VoiceRecognitionIntegration
- Убрать зависимости от `AudioDeviceIntegration`
- Адаптировать под новый подход

### 3. SpeechRecognizer
- Убрать методы выбора устройств
- Упростить до использования `device=None`

### 4. SpeechPlayback
- Убрать логику выбора output устройств
- Упростить до использования `device=None`

### 5. Конфигурация
- Убрать секцию `audio.device_manager` из `unified_config.yaml`
- Добавить секцию `default_audio`

## Порядок удаления

### Этап 1: Подготовка
1. Создать backup текущего состояния
2. Проверить зависимости
3. Подготовить новые компоненты

### Этап 2: Удаление модуля
1. Удалить `modules/audio_device_manager/`
2. Удалить `integration/integrations/audio_device_integration.py`
3. Удалить тесты

### Этап 3: Обновление зависимостей
1. Обновить `SimpleModuleCoordinator`
2. Обновить `VoiceRecognitionIntegration`
3. Обновить `SpeechRecognizer`
4. Обновить `SpeechPlayback`

### Этап 4: Обновление конфигурации
1. Обновить `unified_config.yaml`
2. Обновить импорты в других модулях

### Этап 5: Тестирование
1. Проверить, что приложение запускается
2. Протестировать базовую функциональность
3. Исправить найденные проблемы

## Риски

### Высокий риск
- Приложение может не запуститься
- Потеря функциональности аудио
- Ошибки импорта

### Средний риск
- Проблемы с конфигурацией
- Ошибки в других модулях
- Проблемы с тестами

### Низкий риск
- Проблемы с документацией
- Проблемы с packaging

## Митигация

### Backup
- Создать git tag перед удалением
- Сохранить важные файлы

### Постепенное удаление
- Удалять по частям
- Тестировать после каждого этапа

### Откат
- Возможность быстро вернуть старый код
- Инструкции по восстановлению

## Критерии успеха

1. ✅ Приложение запускается без ошибок
2. ✅ Аудио функции работают
3. ✅ Нет ошибок импорта
4. ✅ Конфигурация корректна
5. ✅ Тесты проходят
