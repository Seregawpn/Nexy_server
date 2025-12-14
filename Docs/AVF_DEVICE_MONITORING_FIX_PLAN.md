# План исправления мониторинга устройств в AVFAudioEngine

## 🔍 Подтверждение проблемы

Анализ кода подтвердил все выявленные проблемы:

1. ✅ **AudioSystemIntegration не запускает DeviceMonitor** - просто создает AVFAudioEngine и говорит "автоматически использует системные default устройства"
2. ✅ **get_device_manager/get_output_manager возвращают None** - вся legacy система недоступна
3. ✅ **AVFAudioEngine не подписывается на нотификации** - импортирует `AudioObjectAddPropertyListener`, но не использует
4. ✅ **Нет подписки на AVAudioEngineConfigurationChangeNotification** - не отслеживает изменения конфигурации engine
5. ✅ **get_current_input_device/get_current_output_device возвращают жестко прошитые строки** - "System Default Input/Output"
6. ✅ **При смене устройства player_node отваливается, но флаг остается True** - нет переподключения
7. ✅ **speech_playback_integration не создает legacy player при _use_avf=True** - CoreAudio listener не запускается

## 🎯 Решение

### Этап 1: Добавить подписку на нотификации в AVFAudioEngine

**Файл**: `modules/audio_avf/core/avf_audio_engine.py`

**Изменения**:
1. Добавить подписку на `AVAudioEngineConfigurationChangeNotification`
2. Добавить подписку на `AudioObjectAddPropertyListener` для отслеживания смены default устройств
3. При смене устройства:
   - Сбрасывать `_player_node_connected = False`
   - Переподключать `player_node` к `output_node`
   - Переподключать `input_node` (если активен)
   - Публиковать события `audio.device.output_changed` / `audio.device.input_changed`

### Этап 2: Реализовать получение реальных имен устройств

**Файл**: `modules/audio_avf/core/avf_audio_engine.py`

**Изменения**:
1. Использовать CoreAudio API для получения реального имени устройства
2. Кэшировать имя устройства и обновлять при смене
3. Возвращать реальное имя в `get_current_input_device()` / `get_current_output_device()`

### Этап 3: Публикация событий в EventBus

**Файл**: `modules/audio_avf/core/avf_audio_engine.py`

**Изменения**:
1. Добавить `event_bus` в конструктор AVFAudioEngine (опционально)
2. Публиковать события `audio.device.output_changed` / `audio.device.input_changed` при смене устройства
3. Формат события совместим с legacy системой

### Этап 4: Интеграция с AudioSystemIntegration

**Файл**: `integration/integrations/audio_system_integration.py`

**Изменения**:
1. Передавать `event_bus` в AVFAudioEngine при создании
2. Подписываться на события `audio.device.*` для логирования/диагностики

## 📝 Детальная реализация

### 1. Подписка на AVAudioEngineConfigurationChangeNotification

```python
def _setup_configuration_change_notification(self):
    """Подписка на изменения конфигурации AVAudioEngine"""
    from Foundation import NSNotificationCenter, NSNotification
    
    def on_configuration_change(notification: NSNotification):
        """Обработчик изменения конфигурации engine"""
        logger.info("🔔 [AVF] AVAudioEngineConfigurationChangeNotification получена")
        self._handle_device_change()
    
    # Подписываемся на нотификацию
    NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
        self,
        "on_configuration_change:",
        "AVAudioEngineConfigurationChangeNotification",
        self._engine
    )
```

### 2. Подписка на AudioObjectAddPropertyListener

```python
def _setup_core_audio_listeners(self):
    """Подписка на Core Audio нотификации о смене устройств"""
    from CoreAudio import (
        AudioObjectAddPropertyListener,
        kAudioObjectSystemObject,
        kAudioHardwarePropertyDefaultOutputDevice,
        kAudioHardwarePropertyDefaultInputDevice,
        AudioObjectPropertyAddress,
        kAudioObjectPropertyScopeGlobal,
        kAudioObjectPropertyElementMain,
    )
    
    def output_device_changed_callback(
        inObjectID: int,
        inNumberAddresses: int,
        inAddresses: Any,
        inClientData: Any
    ) -> int:
        """Callback для смены OUTPUT устройства"""
        logger.info("🔔 [AVF] Core Audio: default OUTPUT устройство изменилось")
        # Вызываем обработчик в главном потоке
        threading.Thread(
            target=self._handle_output_device_change,
            daemon=True
        ).start()
        return 0
    
    def input_device_changed_callback(
        inObjectID: int,
        inNumberAddresses: int,
        inAddresses: Any,
        inClientData: Any
    ) -> int:
        """Callback для смены INPUT устройства"""
        logger.info("🔔 [AVF] Core Audio: default INPUT устройство изменилось")
        threading.Thread(
            target=self._handle_input_device_change,
            daemon=True
        ).start()
        return 0
    
    # Подписываемся на OUTPUT
    output_address = AudioObjectPropertyAddress(
        kAudioHardwarePropertyDefaultOutputDevice,
        kAudioObjectPropertyScopeGlobal,
        kAudioObjectPropertyElementMain
    )
    result = AudioObjectAddPropertyListener(
        kAudioObjectSystemObject,
        output_address,
        output_device_changed_callback,
        None
    )
    if result == 0:
        logger.info("✅ [AVF] Подписка на OUTPUT device changes активирована")
        self._output_listener_active = True
    else:
        logger.warning(f"⚠️ [AVF] Не удалось подписаться на OUTPUT device changes: {result}")
    
    # Подписываемся на INPUT
    input_address = AudioObjectPropertyAddress(
        kAudioHardwarePropertyDefaultInputDevice,
        kAudioObjectPropertyScopeGlobal,
        kAudioObjectPropertyElementMain
    )
    result = AudioObjectAddPropertyListener(
        kAudioObjectSystemObject,
        input_address,
        input_device_changed_callback,
        None
    )
    if result == 0:
        logger.info("✅ [AVF] Подписка на INPUT device changes активирована")
        self._input_listener_active = True
    else:
        logger.warning(f"⚠️ [AVF] Не удалось подписаться на INPUT device changes: {result}")
```

### 3. Обработчик смены устройства

```python
def _handle_output_device_change(self):
    """Обработка смены OUTPUT устройства"""
    try:
        logger.info("🔄 [AVF] Обработка смены OUTPUT устройства...")
        
        # Получаем новое имя устройства
        new_device_name = self._get_real_output_device_name()
        old_device_name = self._cached_output_device_name
        
        if new_device_name == old_device_name:
            logger.debug(f"🔍 [AVF] Устройство не изменилось: {new_device_name}")
            return
        
        logger.info(f"🔄 [AVF] Смена OUTPUT устройства: {old_device_name} → {new_device_name}")
        
        # Обновляем кэш
        self._cached_output_device_name = new_device_name
        
        # Сбрасываем флаг подключения
        with self._lock:
            self._player_node_connected = False
        
        # Переподключаем player_node к output_node
        self._reconnect_player_node()
        
        # Публикуем событие
        if self._event_bus:
            asyncio.create_task(
                self._event_bus.publish("audio.device.output_changed", {
                    "device_name": new_device_name,
                    "old_device_name": old_device_name,
                    "source": "AVF_CORE_AUDIO"
                })
            )
        
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка обработки смены OUTPUT устройства: {e}", exc_info=True)

def _reconnect_player_node(self):
    """Переподключение player_node к output_node после смены устройства"""
    try:
        # Останавливаем engine если запущен
        was_running = self._engine.isRunning()
        if was_running:
            self._engine.stop()
            logger.debug("🛑 [AVF] Engine остановлен для переподключения")
        
        # Отключаем старый player_node
        if self._player_node_connected:
            try:
                self._engine.disconnectNodeInput_(self._output_node)
            except Exception:
                pass  # Может быть уже отключен
        
        # Получаем новый формат output_node
        output_format_avf = self._output_node.inputFormatForBus_(0)
        if output_format_avf is None:
            logger.error("❌ [AVF] output_format_avf is None при переподключении")
            return False
        
        # Подключаем заново
        self._engine.connect_to_format_(
            self._player_node,
            self._output_node,
            output_format_avf
        )
        
        with self._lock:
            self._player_node_connected = True
        
        logger.info("✅ [AVF] Player node переподключен к output node")
        
        # Запускаем engine обратно если был запущен
        if was_running:
            self._engine.prepare()
            error_ref = objc.NULL
            success = self._engine.startAndReturnError_(error_ref)
            if success:
                logger.info("✅ [AVF] Engine перезапущен после переподключения")
            else:
                logger.error("❌ [AVF] Не удалось перезапустить engine после переподключения")
        
        return True
        
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка переподключения player node: {e}", exc_info=True)
        return False
```

### 4. Получение реального имени устройства

```python
def _get_real_output_device_name(self) -> Optional[str]:
    """Получить реальное имя OUTPUT устройства через CoreAudio API"""
    try:
        from CoreAudio import (
            AudioObjectGetPropertyData,
            kAudioObjectSystemObject,
            kAudioHardwarePropertyDefaultOutputDevice,
            AudioObjectPropertyAddress,
            kAudioObjectPropertyScopeGlobal,
            kAudioObjectPropertyElementMain,
        )
        
        # Получаем device ID
        address = AudioObjectPropertyAddress(
            kAudioHardwarePropertyDefaultOutputDevice,
            kAudioObjectPropertyScopeGlobal,
            kAudioObjectPropertyElementMain
        )
        
        device_id = ctypes.c_uint32()
        data_size = ctypes.sizeof(device_id)
        result = AudioObjectGetPropertyData(
            kAudioObjectSystemObject,
            address,
            0,
            None,
            ctypes.byref(ctypes.c_uint32(data_size)),
            ctypes.byref(device_id)
        )
        
        if result != 0:
            logger.warning(f"⚠️ [AVF] Не удалось получить OUTPUT device ID: {result}")
            return "System Default Output"
        
        # Получаем имя устройства
        from CoreAudio import kAudioObjectPropertyName
        
        name_address = AudioObjectPropertyAddress(
            kAudioObjectPropertyName,
            kAudioObjectPropertyScopeGlobal,
            kAudioObjectPropertyElementMain
        )
        
        # Получаем размер имени
        name_size = ctypes.c_uint32()
        AudioObjectGetPropertyData(
            device_id.value,
            name_address,
            0,
            None,
            ctypes.byref(ctypes.c_uint32(ctypes.sizeof(name_size))),
            ctypes.byref(name_size)
        )
        
        # Получаем имя
        name_buffer = ctypes.create_string_buffer(name_size.value)
        result = AudioObjectGetPropertyData(
            device_id.value,
            name_address,
            0,
            None,
            ctypes.byref(name_size),
            name_buffer
        )
        
        if result == 0:
            device_name = name_buffer.value.decode('utf-8')
            logger.debug(f"✅ [AVF] Реальное имя OUTPUT устройства: {device_name}")
            return device_name
        else:
            logger.warning(f"⚠️ [AVF] Не удалось получить имя OUTPUT устройства: {result}")
            return "System Default Output"
            
    except Exception as e:
        logger.error(f"❌ [AVF] Ошибка получения реального имени OUTPUT устройства: {e}")
        return "System Default Output"
```

## 🧪 Тестирование

### Тест 1: Подключение наушников во время воспроизведения
1. Запустить воспроизведение аудио
2. Подключить наушники
3. Проверить логи на наличие нотификаций
4. Проверить, что аудио продолжает воспроизводиться

### Тест 2: Отключение наушников
1. Воспроизводить аудио на наушниках
2. Отключить наушники
3. Проверить, что аудио переключается на динамики

### Тест 3: Переключение между устройствами
1. Подключить несколько устройств
2. Переключать default устройство в системных настройках
3. Проверить, что AVFAudioEngine реагирует на изменения

## 📋 Чек-лист реализации

- [ ] Добавить подписку на AVAudioEngineConfigurationChangeNotification
- [ ] Добавить подписку на AudioObjectAddPropertyListener для OUTPUT
- [ ] Добавить подписку на AudioObjectAddPropertyListener для INPUT
- [ ] Реализовать _handle_output_device_change()
- [ ] Реализовать _handle_input_device_change()
- [ ] Реализовать _reconnect_player_node()
- [ ] Реализовать _reconnect_input_node()
- [ ] Реализовать _get_real_output_device_name()
- [ ] Реализовать _get_real_input_device_name()
- [ ] Обновить get_current_input_device() / get_current_output_device()
- [ ] Добавить публикацию событий в EventBus
- [ ] Обновить AudioSystemIntegration для передачи event_bus
- [ ] Тесты пройдены




