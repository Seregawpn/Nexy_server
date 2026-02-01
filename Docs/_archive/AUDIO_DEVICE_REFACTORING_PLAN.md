# План рефакторинга системы определения устройств

**Дата создания:** 2025-12-02  
**Статус:** В процессе реализации (Фаза 1, Шаг 1.1 завершен)  
**Цель:** Решить постоянные проблемы с определением дефолтных устройств

## Статус реализации

**✅ Фаза 1, Шаг 1.1 (завершен):**
- ✅ Feature flag `device_switch_v2` добавлен в `unified_config.yaml`
- ✅ `_query_system_default_output()` обновлен в `player.py` - использует `sd.default.device[1]` при включенном флаге
- ✅ `_get_system_default_input_index()` обновлен в `speech_recognizer.py` - использует `sd.default.device[0]` при включенном флаге
- ✅ Старая логика сохранена как fallback при выключенном флаге

**✅ Фаза 1, Шаг 1.2 (завершен):**
- ✅ `_get_current_input_device()` обновлен в `device_change_publisher.py` - использует `sd.default.device[0]` при включенном флаге
- ✅ `_get_current_output_device()` обновлен в `device_change_publisher.py` - использует `sd.default.device[1]` при включенном флаге
- ✅ Улучшено сравнение устройств в polling loop - сравнивает по `device_id` при включенном флаге
- ✅ `_get_device_name_via_macos_api()` помечен как deprecated (используется только для fallback)
- ✅ Старая логика сохранена как fallback при выключенном флаге

**⏳ Следующие шаги:**
- Тестирование Фазы 1 (Шаги 1.1 и 1.2)
- Фаза 2: Ввести CoreAudioDeviceManager

---

## Обзор

**Проблема:** Постоянные проблемы с определением дефолтного устройства из-за отсутствия единого источника истины (имя из SwitchAudioSource, ID из PortAudio).

**Решение:** Фаза 1-2 рефакторинга для создания единого источника истины через Core Audio.

**Время:** 5-8 дней  
**Риски:** Средние (постепенный rollout через feature flags)

---

## Фаза 1: Упростить логику переключения устройств (2-3 дня)

### Цель Фазы 1
Сделать так, чтобы переключение устройств логически выглядело так:
> "macOS говорит: дефолт сменился → мы просто пересоздаём поток на текущем дефолтном устройстве PortAudio"

### Шаг 1.1: Зафиксировать модель "следуем за системным дефолтом" (1 день)

#### Файлы для изменения:

**1. `modules/speech_playback/core/player.py`**

**Методы для изменения:**

- **`_query_system_default_output()` (строки ~1711-1754)**
  - **Что изменить:**
    - Убрать логику поиска устройства по имени через SwitchAudioSource
    - Вместо этого использовать `sd.default.device[1]` для получения текущего default output устройства PortAudio
    - Вернуть `(None, device_id)` где `device_id` - это индекс из `sd.default.device[1]`
    - Имя устройства получать через `sd.query_devices(device_id, 'output')['name']` только для логов
  - **Критерий успеха:**
    - Метод не вызывает SwitchAudioSource
    - Возвращает корректный `device_id` из PortAudio
    - Имя используется только для логов

- **`_get_output_device_name_via_macos_api_sync()` (строки ~1756-1820)**
  - **Что изменить:**
    - Пометить как `@deprecated` или переименовать в `_get_output_device_name_via_macos_api_sync_legacy()`
    - Добавить комментарий: "Используется только для логов и fallback диагностики"
  - **Критерий успеха:**
    - Метод не вызывается из критического пути
    - Используется только для диагностики/логов

- **`_check_and_update_output_device()` (строки ~264-300)**
  - **Что изменить:**
    - Убрать вызов `_get_output_device_name_via_macos_api_sync()`
    - Вместо этого использовать `sd.default.device[1]` напрямую
    - Сравнивать `device_id` вместо имени устройства
  - **Критерий успеха:**
    - Не вызывает SwitchAudioSource
    - Сравнивает устройства по `device_id`

**2. `modules/voice_recognition/core/speech_recognizer.py`**

**Методы для изменения:**

- **`_get_system_default_input_index()` (строки ~1389-1450)**
  - **Что изменить:**
    - Убрать логику поиска устройства по имени через SwitchAudioSource
    - Использовать `sd.default.device[0]` напрямую для получения default input устройства
    - Убрать вызов `_get_system_default_input_name()` и `_find_device_id_by_name_input()`
  - **Критерий успеха:**
    - Метод не вызывает SwitchAudioSource
    - Возвращает корректный индекс из `sd.default.device[0]`

- **`_get_system_default_input_name()` (если есть)**
  - **Что изменить:**
    - Пометить как `@deprecated` или переименовать в `_get_system_default_input_name_legacy()`
    - Добавить комментарий: "Используется только для логов"
  - **Критерий успеха:**
    - Метод не вызывается из критического пути

**3. `modules/audio_core/stream_manager.py`**

**Методы для изменения:**

- **`create_stream()` (основной метод)**
  - **Что изменить:**
    - Убрать логику, которая пытается найти устройство по имени
    - Если `device_id` передан - использовать его напрямую
    - Если `device_id=None` - использовать `sd.default.device` для соответствующего типа (input/output)
  - **Критерий успеха:**
    - Не использует имя устройства для поиска ID
    - Работает только с `device_id` или системным дефолтом

#### Тестирование Шага 1.1:

1. **Unit тесты:**
   - Проверить, что `_query_system_default_output()` возвращает корректный `device_id`
   - Проверить, что `_get_system_default_input_index()` возвращает корректный индекс
   - Проверить, что методы не вызывают SwitchAudioSource

2. **Интеграционные тесты:**
   - Запустить приложение и проверить, что переключение устройств работает
   - Проверить, что в логах нет вызовов SwitchAudioSource из критического пути
   - Проверить работу с BT устройствами (AirPods)

---

### Шаг 1.2: Ослабить зависимость от SwitchAudioSource (1-2 дня)

#### Файлы для изменения:

**1. `modules/audio_core/device_change_publisher.py`**

**Методы для изменения:**

- **`_get_current_input_device()` (строки ~419-441)** ✅ ВЫПОЛНЕНО
  - **Что изменено:**
    - ✅ Добавлена проверка feature flag `device_switch_v2`
    - ✅ При включенном флаге: использует `sd.default.device[0]` напрямую
    - ✅ При выключенном флаге: использует старую логику через `_get_device_name_via_macos_api()`
    - ✅ Кэш `_device_name_cache` сохранен для старой логики (будет удален в Фазе 2)
  - **Критерий успеха:** ✅
    - ✅ Не вызывает SwitchAudioSource при включенном флаге
    - ✅ Использует PortAudio напрямую при включенном флаге

- **`_get_current_output_device()` (строки ~443-465)** ✅ ВЫПОЛНЕНО
  - **Что изменено:**
    - ✅ Добавлена проверка feature flag `device_switch_v2`
    - ✅ При включенном флаге: использует `sd.default.device[1]` напрямую
    - ✅ При выключенном флаге: использует старую логику через `_get_device_name_via_macos_api()`
  - **Критерий успеха:** ✅
    - ✅ Не вызывает SwitchAudioSource при включенном флаге
    - ✅ Использует PortAudio напрямую при включенном флаге

- **`_get_device_name_via_macos_api()` (строки ~467-535)** ✅ ВЫПОЛНЕНО
  - **Что изменено:**
    - ✅ Помечен как deprecated в docstring
    - ✅ Добавлен комментарий: "Используется только для fallback диагностики при выключенном feature flag"
  - **Критерий успеха:** ✅
    - ✅ Метод не вызывается из критического пути при включенном флаге
    - ✅ Используется только для fallback диагностики

- **Улучшено сравнение устройств в polling loop** ✅ ВЫПОЛНЕНО
  - **Что изменено:**
    - ✅ При включенном feature flag: сравнивает по `device_id` (более надежно)
    - ✅ При выключенном feature flag: сравнивает по имени (старая логика)
  - **Критерий успеха:** ✅
    - ✅ Сравнение работает корректно в обоих режимах

**2. `modules/speech_playback/core/player.py`**

**Методы для изменения:**

- **`_start_audio_stream()` (строки ~513-700)**
  - **Что изменить:**
    - Убрать fallback на `_query_default_output_device()` (который использует SwitchAudioSource)
    - Если `device_id` не передан - использовать `sd.default.device[1]` напрямую
  - **Критерий успеха:**
    - Не вызывает SwitchAudioSource
    - Использует системный дефолт PortAudio

- **`_query_default_output_device()` (если есть)**
  - **Что изменить:**
    - Пометить как `@deprecated` или переименовать в `_query_default_output_device_legacy()`
    - Добавить комментарий: "Используется только для диагностики"
  - **Критерий успеха:**
    - Метод не вызывается из критического пути

#### Тестирование Шага 1.2:

1. **Unit тесты:**
   - Проверить, что `_get_current_input_device()` и `_get_current_output_device()` не вызывают SwitchAudioSource
   - Проверить, что методы корректно работают с Core Audio и PortAudio

2. **Интеграционные тесты:**
   - Запустить приложение без SwitchAudioSource в PATH
   - Проверить, что переключение устройств работает
   - Проверить работу с разными типами устройств (BT, USB, встроенные)

---

### Feature Flag для Фазы 1

**Имя флага:** `NEXY_FEATURE_DEVICE_SWITCH_V2`

**Где добавить:**
- `config/unified_config.yaml`:
  ```yaml
  features:
    device_switch_v2:
      enabled: false  # По умолчанию выключено
      rollout_percentage: 0  # 0% пользователей
  ```

**Где использовать:**
- `modules/speech_playback/core/player.py` - проверка флага перед использованием новой логики
- `modules/voice_recognition/core/speech_recognizer.py` - проверка флага перед использованием новой логики
- `modules/audio_core/device_change_publisher.py` - проверка флага перед использованием новой логики

**Критерий успеха:**
- Старая логика работает по умолчанию (флаг выключен)
- Новая логика включается через флаг
- Можно переключаться между старой и новой логикой без перезапуска

---

## Фаза 2: Ввести CoreAudioDeviceManager (3-5 дней)

### Цель Фазы 2
Создать единый источник истины для Core Audio устройств и облегчить DeviceChangePublisher.

### Шаг 2.1: Создать CoreAudioDeviceManager (2 дня)

#### Новый файл: `modules/audio_core/core_audio_device_manager.py`

**Структура класса:**

```python
@dataclass
class CoreAudioDeviceInfo:
    """Информация об устройстве Core Audio"""
    core_audio_id: int  # AudioDeviceID
    uid: str  # Уникальный идентификатор устройства
    name: str  # Имя устройства
    is_bluetooth: bool  # Флаг Bluetooth устройства
    is_builtin: bool  # Флаг встроенного устройства
    is_external: bool  # Флаг внешнего устройства

class CoreAudioDeviceManager:
    """Менеджер для работы с Core Audio устройствами"""
    
    def __init__(self):
        """Инициализация менеджера"""
        # Инициализация Core Audio через PyObjC
        
    def get_default_input_device(self) -> Optional[CoreAudioDeviceInfo]:
        """Получить текущее default input устройство"""
        # Использовать Core Audio API для получения устройства
        # Вернуть CoreAudioDeviceInfo или None
        
    def get_default_output_device(self) -> Optional[CoreAudioDeviceInfo]:
        """Получить текущее default output устройство"""
        # Использовать Core Audio API для получения устройства
        # Вернуть CoreAudioDeviceInfo или None
        
    def get_available_devices(self, device_type: str) -> List[CoreAudioDeviceInfo]:
        """Получить список доступных устройств"""
        # device_type: "input" или "output"
        # Вернуть список CoreAudioDeviceInfo
        
    def is_bluetooth_device(self, device_info: CoreAudioDeviceInfo) -> bool:
        """Проверить, является ли устройство Bluetooth"""
        # Проверка через Core Audio свойства устройства
```

**Что реализовать:**

1. **Инициализация Core Audio:**
   - Использовать PyObjC для доступа к Core Audio API
   - Проверка доступности Core Audio
   - Обработка ошибок инициализации

2. **Получение default устройств:**
   - Использовать `kAudioHardwarePropertyDefaultInputDevice` для input
   - Использовать `kAudioHardwarePropertyDefaultOutputDevice` для output
   - Получение свойств устройства (имя, UID, флаги)

3. **Определение типа устройства:**
   - Проверка через Core Audio свойства, является ли устройство Bluetooth
   - Проверка, является ли устройство встроенным или внешним

4. **Получение списка устройств:**
   - Перечисление всех доступных устройств через Core Audio API
   - Фильтрация по типу (input/output)

**Критерий успеха:**
- Класс изолирован и не знает про PortAudio, EventBus, интеграции
- Все методы возвращают `CoreAudioDeviceInfo` или `None`
- Корректно определяет тип устройств (BT, встроенные, внешние)
- Обрабатывает ошибки и недоступность Core Audio

#### Тестирование Шага 2.1:

1. **Unit тесты:**
   - Проверить получение default input/output устройств
   - Проверить определение типа устройств (BT, встроенные)
   - Проверить обработку ошибок

2. **Интеграционные тесты:**
   - Запустить приложение и проверить, что CoreAudioDeviceManager корректно получает устройства
   - Проверить работу с разными типами устройств

---

### Шаг 2.2: Обновить DeviceChangePublisher (1-2 дня)

#### Файл: `modules/audio_core/device_change_publisher.py`

**Что изменить:**

1. **Добавить зависимость на CoreAudioDeviceManager:**
   - Импортировать `CoreAudioDeviceManager` из `modules.audio_core.core_audio_device_manager`
   - Создать экземпляр в `__init__()`
   - Проверка доступности CoreAudioDeviceManager

2. **Обновить `DeviceInfo` dataclass:**
   - Добавить поля: `core_audio_id: Optional[int]`, `uid: Optional[str]`
   - Сохранить обратную совместимость (старые поля остаются)

3. **Обновить `_get_current_input_device()`:**
   - Использовать `CoreAudioDeviceManager.get_default_input_device()` вместо SwitchAudioSource
   - Преобразовать `CoreAudioDeviceInfo` в `DeviceInfo`
   - Сохранить `core_audio_id` и `uid` в `DeviceInfo`
   - Fallback на PortAudio, если CoreAudioDeviceManager недоступен

4. **Обновить `_get_current_output_device()`:**
   - Аналогично `_get_current_input_device()`
   - Использовать `CoreAudioDeviceManager.get_default_output_device()`

5. **Обновить `_handle_device_change()`:**
   - Сравнивать устройства по `core_audio_id` или `uid` вместо имени
   - Если `core_audio_id`/`uid` недоступны - использовать имя как fallback
   - Публиковать событие с полной информацией об устройстве (`core_audio_id`, `uid`, `name`, флаги)

6. **Убрать все использования SwitchAudioSource:**
   - Удалить методы `_get_device_name_via_macos_api()` и аналогичные
   - Убрать импорты `subprocess`, `json`, `shutil` (если они использовались только для SwitchAudioSource)

**Критерий успеха:**
- DeviceChangePublisher не вызывает SwitchAudioSource
- Сравнение устройств происходит по `core_audio_id`/`uid`
- События содержат полную информацию об устройстве
- Fallback на PortAudio работает, если CoreAudioDeviceManager недоступен

#### Тестирование Шага 2.2:

1. **Unit тесты:**
   - Проверить, что `_get_current_input_device()` и `_get_current_output_device()` используют CoreAudioDeviceManager
   - Проверить сравнение устройств по `core_audio_id`/`uid`
   - Проверить fallback на PortAudio

2. **Интеграционные тесты:**
   - Запустить приложение и проверить, что DeviceChangePublisher корректно определяет изменения устройств
   - Проверить работу с разными типами устройств
   - Проверить работу без CoreAudioDeviceManager (fallback)

---

### Шаг 2.3: Обновить AudioStreamManager (1 день)

#### Файл: `modules/audio_core/stream_manager.py`

**Что изменить:**

1. **Обновить обработку событий `device.default_*_changed`:**
   - Использовать `core_audio_id` или `uid` из события вместо имени
   - Если `core_audio_id`/`uid` недоступны - использовать `device_id` из события
   - Если ничего не доступно - использовать системный дефолт PortAudio

2. **Упростить логику переключения устройств:**
   - Убрать логику поиска устройства по имени
   - Работать только с `device_id` или системным дефолтом

**Критерий успеха:**
- AudioStreamManager использует `core_audio_id`/`uid` из событий
- Не использует имя устройства для поиска ID
- Корректно работает с системным дефолтом PortAudio

#### Тестирование Шага 2.3:

1. **Unit тесты:**
   - Проверить обработку событий с `core_audio_id`/`uid`
   - Проверить fallback на системный дефолт

2. **Интеграционные тесты:**
   - Запустить приложение и проверить переключение устройств
   - Проверить работу с разными типами устройств

---

## План rollout

### Неделя 1: Реализация Фазы 1

**День 1-2:** Шаг 1.1 (Зафиксировать модель "следуем за системным дефолтом")
- Реализация изменений в `player.py` и `speech_recognizer.py`
- Unit тесты
- Интеграционные тесты

**День 3:** Шаг 1.2 (Ослабить зависимость от SwitchAudioSource)
- Реализация изменений в `device_change_publisher.py`
- Unit тесты
- Интеграционные тесты

**День 4-5:** Feature flag и тестирование Фазы 1
- Добавление feature flag `NEXY_FEATURE_DEVICE_SWITCH_V2`
- Тестирование с флагом выключенным и включенным
- Исправление багов

### Неделя 2: Начало Фазы 2

**День 1-2:** Шаг 2.1 (Создать CoreAudioDeviceManager)
- Реализация `CoreAudioDeviceManager`
- Unit тесты
- Интеграционные тесты

**День 3:** Шаг 2.2 (Обновить DeviceChangePublisher) - начало
- Добавление зависимости на CoreAudioDeviceManager
- Обновление `DeviceInfo`

### Неделя 3: Завершение Фазы 2

**День 1-2:** Шаг 2.2 (Обновить DeviceChangePublisher) - завершение
- Обновление методов получения устройств
- Обновление сравнения устройств
- Удаление SwitchAudioSource

**День 3:** Шаг 2.3 (Обновить AudioStreamManager)
- Обновление обработки событий
- Упрощение логики переключения

**День 4-5:** Тестирование Фазы 2
- Полное тестирование с новой архитектурой
- Исправление багов
- Подготовка к rollout

### Неделя 4: Постепенный rollout

**День 1:** Rollout 1% пользователей
- Включить feature flag для 1% пользователей
- Мониторинг метрик и логов
- Исправление критических багов

**День 2-3:** Rollout 25% пользователей
- Увеличить процент до 25%
- Мониторинг метрик и логов
- Исправление багов

**День 4-5:** Rollout 100% пользователей
- Включить для всех пользователей
- Мониторинг метрик и логов
- Финальные исправления

---

## Критерии успеха

### Фаза 1:
- ✅ Переключение устройств работает без SwitchAudioSource
- ✅ Логика не зависит от имени устройства для принятия решений
- ✅ Имя используется только для логов и UI
- ✅ Feature flag работает корректно

### Фаза 2:
- ✅ CoreAudioDeviceManager изолирован и тестируем
- ✅ DeviceChangePublisher не знает про PortAudio и SwitchAudioSource
- ✅ События содержат полную информацию об устройстве (`core_audio_id`, `uid`, флаги)
- ✅ Сравнение устройств происходит по `core_audio_id`/`uid`
- ✅ Fallback на PortAudio работает, если CoreAudioDeviceManager недоступен

### Общие:
- ✅ Нет регрессий в функциональности
- ✅ Переключение устройств работает стабильно
- ✅ Проблемы с BT устройствами решены
- ✅ Ошибки -9986 и -10851 не возникают из-за несоответствия имени и ID

---

## Риски и митигация

### Риск 1: Регрессии при миграции
**Митигация:**
- Feature flag для постепенного rollout
- Сохранение старой логики как fallback
- Тщательное тестирование на каждом этапе

### Риск 2: Несовместимость Core Audio API
**Митигация:**
- Fallback на PortAudio, если Core Audio недоступен
- Проверка доступности Core Audio перед использованием
- Тестирование на разных версиях macOS

### Риск 3: Потеря функциональности
**Митигация:**
- Сохранение старой логики как fallback
- Постепенный rollout с мониторингом
- Возможность отката через feature flag

---

## Метрики для мониторинга

### Метрики успеха:
- Количество успешных переключений устройств
- Время переключения устройств
- Количество ошибок -9986 и -10851
- Количество проблем с BT устройствами

### Метрики проблем:
- Количество fallback'ов на старую логику
- Количество ошибок при получении устройств
- Количество случаев, когда устройство не найдено

---

## Следующие шаги

1. **Создать feature flag** `NEXY_FEATURE_DEVICE_SWITCH_V2` в `unified_config.yaml`
2. **Начать с Фазы 1, Шаг 1.1** - упростить логику в `player.py` и `speech_recognizer.py`
3. **Тестировать каждый шаг** перед переходом к следующему
4. **Мониторить метрики** на каждом этапе rollout

