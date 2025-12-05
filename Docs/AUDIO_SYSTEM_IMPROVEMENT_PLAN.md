# План улучшения аудиосистемы Nexy

## Дата создания
2025-12-02

## Цель

Реализовать запланированные циклы для стабильности CoreAudio и PortAudio:
- DeviceChangePublisher → единый поток событий
- AudioStreamManager → единый API управления потоками
- Избавление от дублирующего polling
- Observability и документация

---

## Цикл 1: CoreAudio + DeviceChangePublisher

### Цели
1. Исправить CoreAudioManager: обернуть callback в PyObjC closure
2. Внедрить DeviceChangePublisher - единый монитор устройств
3. Публикация событий `device.default_input_changed` / `device.default_output_changed`
4. Fallback на polling при недоступности Core Audio
5. Логирование источника (CoreAudio vs polling)

### Компоненты

#### 1.1 DeviceChangePublisher
**Файл:** `modules/audio_core/device_change_publisher.py` (новый)

**Ответственность:**
- Единый мониторинг INPUT и OUTPUT устройств
- Подписка на Core Audio нотификации (приоритет 1)
- Fallback на polling при недоступности Core Audio
- Публикация событий в EventBus: `device.default_input_changed` / `device.default_output_changed`
- Debounce для rapid device switch
- Логирование источника (CoreAudio vs polling)

**События:**
- **Публикует:**
  - `device.default_input_changed{device_name, device_id, source}` - смена INPUT устройства
  - `device.default_output_changed{device_name, device_id, source}` - смена OUTPUT устройства
  - `device.monitoring_started{source}` - мониторинг запущен
  - `device.monitoring_stopped` - мониторинг остановлен

**Интерфейс:**
```python
class DeviceChangePublisher:
    def __init__(self, event_bus: EventBus)
    async def start_monitoring(self, monitor_input: bool = True, monitor_output: bool = True) -> bool
    async def stop_monitoring(self)
    def get_current_input_device(self) -> Optional[DeviceInfo]
    def get_current_output_device(self) -> Optional[DeviceInfo]
    def is_core_audio_available(self) -> bool
```

#### 1.2 Улучшенный CoreAudioManager
**Файл:** `modules/speech_playback/macos/core_audio.py`

**Изменения:**
- Поддержка INPUT и OUTPUT нотификаций
- Правильная обёртка callback через `objc.callback`
- Возврат информации об устройстве в callback

### Интеграция

**INPUT (SpeechRecognizer):**
- Подписка на `device.default_input_changed`
- При смене устройства: `pending_device_switch = True`
- Пересоздание потока только если запись НЕ идёт

**OUTPUT (SequentialSpeechPlayer):**
- Подписка на `device.default_output_changed`
- При смене устройства: `pending_device_switch = True`
- Безопасное переключение с гарантированным закрытием старого потока

### Миграция

**Шаг 1:** Создать DeviceChangePublisher
**Шаг 2:** Интегрировать в SimpleModuleCoordinator
**Шаг 3:** Обновить SpeechRecognizer и SequentialSpeechPlayer для подписки на события
**Шаг 4:** Удалить старый polling из AudioDeviceMonitor и OutputMonitorThread

---

## Цикл 2: AudioStreamManager для PortAudio

### Цели
1. Вынести логику открытия/закрытия streams в общий менеджер
2. Единый API для управления `sd.InputStream` и `sd.OutputStream`
3. Lock, ожидание `active=False`, адаптивные задержки
4. Логирование PaErrorCode и обработка "неустойчивых" устройств

### Компоненты

#### 2.1 AudioStreamManager
**Файл:** `modules/audio_core/stream_manager.py` (новый)

**Ответственность:**
- Управление lifecycle PortAudio streams
- Гарантированное закрытие старого потока перед созданием нового
- Адаптивные задержки для BT устройств
- Retry логика с экспоненциальным backoff
- Логирование всех операций и ошибок

**Интерфейс:**
```python
class AudioStreamManager:
    def __init__(self, stream_type: Literal["input", "output"])
    async def create_stream(
        self,
        device_id: Optional[int],
        device_name: Optional[str],
        config: StreamConfig,
        callback: Callable,
        max_retries: int = 5
    ) -> Optional[sd.Stream]
    async def close_stream(self, stream: sd.Stream, is_bluetooth: bool = False) -> bool
    async def switch_device(
        self,
        old_stream: Optional[sd.Stream],
        new_device_id: Optional[int],
        new_device_name: Optional[str],
        config: StreamConfig,
        callback: Callable,
        is_bluetooth: bool = False
    ) -> Optional[sd.Stream]
```

**Особенности:**
- Lock для защиты от concurrent операций
- Ожидание `active=False` перед закрытием
- Адаптивные задержки (2.5с для BT, 0.3с для обычных)
- Кэширование безопасных конфигураций
- Обработка ошибок -9986/-10851

### Интеграция

**INPUT (SpeechRecognizer):**
- Использование `AudioStreamManager.create_stream()` вместо прямого создания
- Использование `AudioStreamManager.switch_device()` при смене устройства

**OUTPUT (SequentialSpeechPlayer):**
- Использование `AudioStreamManager.create_stream()` вместо прямого создания
- Использование `AudioStreamManager.switch_device()` при смене устройства

### Миграция

**Шаг 1:** Создать AudioStreamManager
**Шаг 2:** Рефакторинг SpeechRecognizer для использования менеджера
**Шаг 3:** Рефакторинг SequentialSpeechPlayer для использования менеджера
**Шаг 4:** Удалить дублирующую логику из обоих компонентов

---

## Цикл 3: Единый монитор + избавление от polling

### Цели
1. Убрать все polling циклы из INPUT/OUTPUT
2. Перенести polling в DeviceChangePublisher
3. Подписки INPUT/OUTPUT на события `device.default_*_changed`
4. Debounce для rapid device switch

### Компоненты

#### 3.1 Улучшенный DeviceChangePublisher
**Файл:** `modules/audio_core/device_change_publisher.py`

**Добавления:**
- Polling fallback при недоступности Core Audio
- Debounce механизм (300ms) для rapid device switch
- Единый polling цикл для INPUT и OUTPUT
- Логирование источника (CoreAudio vs polling)

**Polling логика:**
- Интервал: 5.0s для BT устройств, 1.0s для обычных
- Использует SwitchAudioSource как единственный источник истины
- Сравнение по имени устройства (не ID)

### Миграция

**Шаг 1:** Добавить polling в DeviceChangePublisher
**Шаг 2:** Удалить `_monitor_loop` из AudioDeviceMonitor
**Шаг 3:** Удалить `_output_monitor_loop` из SequentialSpeechPlayer
**Шаг 4:** Удалить классы AudioDeviceMonitor и OutputMonitorThread (если не используются)

---

## Цикл 4: Observability + документация

### Цели
1. Расширенное логирование всех операций
2. Метрики и счётчики (если есть система)
3. Обновление чек-листов и документации
4. Прописать invariants и сценарии тестирования

### Компоненты

#### 4.1 Расширенное логирование

**DeviceChangePublisher:**
- Логирование каждого `device_changed` события
- Логирование источника (CoreAudio vs polling)
- Логирование debounce срабатываний

**AudioStreamManager:**
- Логирование каждого `stream_open_attempt`
- Логирование ошибок -9986/-10851 с контекстом
- Логирование fallback стратегий
- Логирование времени операций

#### 4.2 Метрики (опционально)

Если есть система метрик:
- `device_switch_count{type, source}` - количество переключений устройств
- `stream_open_success_rate{type}` - процент успешных открытий потоков
- `stream_open_latency_ms{type}` - задержка открытия потока
- `stream_error_count{type, error_code}` - количество ошибок по типам

#### 4.3 Документация

**Обновить:**
- `Docs/AUDIO_SYSTEM_ARCHITECTURE.md` - добавить описание новых компонентов
- `Docs/AUDIO_CORE_ARCHITECTURE_PLAN.md` - описать lifecycle через AudioStreamManager
- `Docs/AUDIO_CORE_ARCHITECTURE_VALIDATION_CHECKLIST.md` - добавить тесты для новых компонентов

**Добавить:**
- `Docs/AUDIO_DEVICE_CHANGE_PUBLISHER.md` - документация DeviceChangePublisher
- `Docs/AUDIO_STREAM_MANAGER.md` - документация AudioStreamManager
- `Docs/AUDIO_INVARIANTS.md` - invariants системы

#### 4.4 Invariants

**INPUT:**
- INPUT не перезапускает stream при `LISTENING` (state == LISTENING)
- INPUT всегда использует системный default (SwitchAudioSource)
- INPUT пересоздает stream только при `IDLE` или `PENDING`

**OUTPUT:**
- OUTPUT всегда закрывает старый stream перед созданием нового
- OUTPUT всегда использует системный default (SwitchAudioSource)
- OUTPUT для BT устройств использует `device=None`

**Общие:**
- Все операции с streams защищены lock
- Все ошибки -9986/-10851 обрабатываются с retry
- Все device changes публикуются через DeviceChangePublisher

---

## Параллельные задачи

### Tray и Mode Transitions

**Проблема:** TrayControllerIntegration может получать `new_mode` как строку вместо Enum

**Решение:**
- Нормализация `new_mode` до `AppMode` в `_on_mode_changed()`
- Добавить логирование преобразования
- Проверка типа перед использованием

**Файл:** `integration/integrations/tray_controller_integration.py`

---

## Порядок реализации

### Фаза 1: Цикл 1 (CoreAudio + DeviceChangePublisher)
1. ✅ Исправить CoreAudioManager (уже частично сделано)
2. ⏳ Создать DeviceChangePublisher
3. ⏳ Интегрировать в SimpleModuleCoordinator
4. ⏳ Обновить INPUT/OUTPUT для подписки на события
5. ⏳ Удалить старый polling

### Фаза 2: Цикл 2 (AudioStreamManager)
1. ⏳ Создать AudioStreamManager
2. ⏳ Рефакторинг SpeechRecognizer
3. ⏳ Рефакторинг SequentialSpeechPlayer
4. ⏳ Тестирование

### Фаза 3: Цикл 3 (Единый монитор)
1. ⏳ Добавить polling в DeviceChangePublisher
2. ⏳ Удалить polling из INPUT/OUTPUT
3. ⏳ Добавить debounce
4. ⏳ Тестирование

### Фаза 4: Цикл 4 (Observability)
1. ⏳ Расширенное логирование
2. ⏳ Метрики (если есть система)
3. ⏳ Обновление документации
4. ⏳ Прописать invariants и тесты

### Параллельно: Tray Fix
1. ⏳ Нормализация `new_mode` в TrayControllerIntegration
2. ⏳ Тестирование

---

## Критерии успеха

### Цикл 1
- [ ] DeviceChangePublisher создан и работает
- [ ] Core Audio нотификации работают без ошибок
- [ ] Fallback на polling работает
- [ ] INPUT/OUTPUT подписаны на события
- [ ] Старый polling удален

### Цикл 2
- [ ] AudioStreamManager создан
- [ ] SpeechRecognizer использует менеджер
- [ ] SequentialSpeechPlayer использует менеджер
- [ ] Дублирующая логика удалена
- [ ] Тесты проходят

### Цикл 3
- [ ] Polling перенесен в DeviceChangePublisher
- [ ] Debounce работает
- [ ] INPUT/OUTPUT не имеют собственного polling
- [ ] Тесты проходят

### Цикл 4
- [ ] Расширенное логирование работает
- [ ] Метрики собираются (если есть система)
- [ ] Документация обновлена
- [ ] Invariants прописаны
- [ ] Тесты добавлены

---

## Риски и митигация

### Риск 1: PyObjC callback может не работать
**Митигация:** Fallback на polling, логирование ошибок

### Риск 2: Рефакторинг может сломать существующую функциональность
**Митигация:** Постепенная миграция, тестирование на каждом этапе

### Риск 3: Debounce может пропустить важные события
**Митигация:** Настраиваемый debounce интервал, логирование всех событий

---

## Следующие шаги

1. **Сейчас:** Начать реализацию Цикла 1 - создать DeviceChangePublisher
2. **После Цикла 1:** Перейти к Циклу 2 - создать AudioStreamManager
3. **После Цикла 2:** Реализовать Цикл 3 - убрать polling
4. **После Цикла 3:** Завершить Цикл 4 - observability и документация




