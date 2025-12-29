# Карта взаимодействий аудиосистемы

**Статус**: Нормативный документ  
**Версия**: 1.0  
**Дата**: 2025-01-XX

---

## 1. Обзор взаимодействий

### 1.1 Компоненты, взаимодействующие с аудио

| Компонент | Тип | Взаимодействие с аудио | Статус при миграции |
|-----------|-----|------------------------|---------------------|
| `InputProcessingIntegration` | Интеграция | Публикует `voice.recording_start/stop`, подписывается на `voice.mic_opened/closed`, `playback.*` | ✅ Сохранить (минимальные изменения) |
| `VoiceRecognitionIntegration` | Интеграция | Запускает/останавливает распознавание, публикует `voice.mic_opened/closed` | ⚠️ Адаптировать (добавить RouteManager) |
| `SpeechPlaybackIntegration` | Интеграция | Воспроизводит аудио, публикует `playback.started/completed` | ⚠️ Адаптировать (добавить AVFoundation) |
| `ModeManagementIntegration` | Интеграция | Управляет режимами, подписывается на `voice.recording_start`, `playback.completed` | ✅ Сохранить (только чтение событий) |
| `TrayControllerIntegration` | Интеграция | Отображает статус, подписывается на `voice.mic_opened/closed`, `app.mode_changed` | ✅ Сохранить (только чтение событий) |
| `InterruptManagementIntegration` | Интеграция | Обрабатывает прерывания, подписывается на `playback.*` | ✅ Сохранить (только чтение событий) |
| `ListeningWorkflow` | Workflow | Координирует переходы в LISTENING | ✅ Сохранить (только чтение событий) |
| `ProcessingWorkflow` | Workflow | Координирует переходы в PROCESSING | ✅ Сохранить (только чтение событий) |
| `AudioRouteManagerIntegration` | Интеграция | **НОВЫЙ** - управляет маршрутизацией аудио | 🆕 Создать |

---

## 2. Feature Flags и их влияние

### 2.1 Существующие флаги, влияющие на аудио

| Flag/Switch | Config Path | Влияние на аудио | Статус |
|-------------|-------------|------------------|--------|
| `permission_restart.enabled` | `unified_config.yaml` | Блокирует перезапуск input во время permission restart | ✅ Сохранить |
| `first_run_permissions.enabled` | `unified_config.yaml` | Блокирует активацию микрофона во время first run | ✅ Сохранить |
| `voice_recognition.simulate` | `unified_config.yaml` | Режим симуляции (не запускает реальный микрофон) | ✅ Сохранить |
| `voice_recognition.enabled` | `unified_config.yaml` | Включение модуля распознавания | ✅ Сохранить |
| `speech_playback.enabled` | `unified_config.yaml` | Включение модуля воспроизведения | ✅ Сохранить |
| `input_processing.enabled` | `unified_config.yaml` | Включение модуля обработки ввода | ✅ Сохранить |
| `mode_management.enabled` | `unified_config.yaml` | Включение модуля управления режимами | ✅ Сохранить |
| `tray_controller.enabled` | `unified_config.yaml` | Включение tray контроллера | ✅ Сохранить |
| `updater.enabled` | `unified_config.yaml` | Блокирует перезапуск input/output во время обновлений | ✅ Сохранить |

### 2.2 Новые флаги для миграции

| Flag/Switch | Config Path | Влияние на аудио | Статус |
|-------------|-------------|------------------|--------|
| `NEXY_FEATURE_AVFOUNDATION_AUDIO_V2` | `unified_config.yaml: audio_system.avfoundation_enabled` | Master switch для всей AVFoundation системы | 🆕 Создать |
| `NEXY_FEATURE_AVFOUNDATION_INPUT_MONITOR_V2` | `unified_config.yaml: audio_system.avfoundation_input_monitor_enabled` | AVFoundation мониторинг input устройств | 🆕 Создать |
| `NEXY_FEATURE_AVFOUNDATION_OUTPUT_V2` | `unified_config.yaml: audio_system.avfoundation_output_enabled` | AVFoundation output (AVAudioEngine) | 🆕 Создать |
| `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2` | `unified_config.yaml: audio_system.avfoundation_route_manager_enabled` | RouteManager для reconcile | 🆕 Создать |
| `NEXY_KS_AVFOUNDATION_INPUT_MONITOR_V2` | `unified_config.yaml: audio_system.ks_avfoundation_input_monitor` | Kill-switch для input мониторинга | 🆕 Создать |
| `NEXY_KS_AVFOUNDATION_OUTPUT_V2` | `unified_config.yaml: audio_system.ks_avfoundation_output` | Kill-switch для output | 🆕 Создать |
| `NEXY_KS_AVFOUNDATION_ROUTE_MANAGER_V2` | `unified_config.yaml: audio_system.ks_avfoundation_route_manager` | Kill-switch для RouteManager | 🆕 Создать |

---

## 3. Детальная карта взаимодействий

### 3.1 InputProcessingIntegration

**Текущие подписки**:
```python
# События записи
"voice.recording_start"      # → _on_recording_start (публикует voice.recording_start)
"voice.recording_stop"       # → _on_recording_stop (публикует voice.recording_stop)

# События распознавания
"voice.recognition_completed" # → _on_recognition_completed
"voice.recognition_failed"    # → _on_recognition_failed
"voice.recognition_timeout"   # → _on_recognition_failed

# События воспроизведения
"playback.started"            # → _on_playback_started (устанавливает _playback_active)
"playback.completed"          # → _on_playback_finished (сбрасывает _playback_active)
"playback.failed"             # → _on_playback_finished
"playback.cancelled"          # → _on_playback_finished

# События микрофона
"voice.mic_opened"            # → _on_mic_opened (устанавливает _mic_active)
"voice.mic_closed"            # → _on_mic_closed (сбрасывает _mic_active)

# События режимов
"mode.switch"                 # → _handle_mode_switch

# События gRPC
"grpc.request_completed"      # → _on_grpc_completed
"grpc.request_failed"        # → _on_grpc_failed
```

**Текущие публикации**:
```python
"voice.recording_start"       # При LONG_PRESS
"voice.recording_stop"        # При RELEASE
"mode.request"                # Запрос перехода режима (LISTENING/PROCESSING/SLEEPING)
"keyboard.press"              # События клавиатуры
"keyboard.short_press"        # Короткое нажатие
"keyboard.long_press"         # Долгое нажатие
"keyboard.release"            # Отпускание клавиши
```

**Влияние RouteManager**:
- [ ] **Минимальное**: InputProcessingIntegration продолжает публиковать `voice.recording_start/stop`
- [ ] **RouteManager реагирует**: RouteManager подписывается на `voice.recording_start` и запускает input через reconcile
- [ ] **Timing сохранен**: Сохранить ожидание `voice.mic_closed` перед обработкой
- [ ] **Нет дублирования**: RouteManager НЕ публикует `voice.recording_start/stop` (только читает)

**Изменения**: Минимальные (только если RouteManager изменяет timing событий)

---

### 3.2 VoiceRecognitionIntegration

**Текущие подписки**:
```python
"voice.recording_start"       # → _on_recording_start (запускает распознавание)
"voice.recording_stop"        # → _on_recording_stop (останавливает распознавание)
"keyboard.short_press"        # → _on_cancel_request (отмена распознавания)
"app.mode_changed"            # → _on_app_mode_changed (закрытие при выходе из LISTENING)
"permissions.first_run_started"   # → _on_first_run_started (блокировка)
"permissions.first_run_completed" # → _on_first_run_completed (разблокировка)
"permissions.first_run_failed"    # → _on_first_run_completed (разблокировка)
```

**Текущие публикации**:
```python
"voice.recognition_started"   # При начале распознавания
"voice.recognition_completed" # При завершении распознавания
"voice.recognition_failed"    # При ошибке распознавания
"voice.recognition_timeout"   # При таймауте распознавания
"voice.mic_opened"            # При открытии микрофона
"voice.mic_closed"            # При закрытии микрофона
"mode.request"                # Запрос перехода в SLEEPING при ошибке
```

**Влияние RouteManager**:
- [ ] **Адаптация**: Добавить проверку `_route_manager_enabled`
- [ ] **Если включен**: RouteManager управляет запуском input, VoiceRecognitionIntegration только публикует события
- [ ] **Если выключен**: Использовать текущую логику (fallback)
- [ ] **События сохранены**: Все существующие события публикуются как раньше

**Изменения**:
```python
async def _on_recording_start(self, event):
    if self._first_run_in_progress:
        return  # Блокировка
    
    # Если RouteManager включен → он управляет запуском
    if self._route_manager_enabled:
        # RouteManager сам запустит input через reconcile
        # Мы только публикуем событие для RouteManager
        await self.event_bus.publish("audio.input.request_start", {
            "session_id": event.get("session_id")
        })
    else:
        # Старая логика (fallback)
        if not self.config.simulate and self._recognizer:
            await self._recognizer.start_listening()
```

---

### 3.3 SpeechPlaybackIntegration

**Текущие подписки**:
```python
"grpc.audio_chunk"            # → _on_audio_chunk (добавляет чанк в плеер)
"playback.cancelled"          # → _on_playback_cancelled (отмена воспроизведения)
"app.mode_changed"            # → _on_app_mode_changed (остановка при выходе из PROCESSING)
```

**Текущие публикации**:
```python
"playback.started"            # При начале воспроизведения
"playback.completed"          # При завершении воспроизведения
"playback.failed"             # При ошибке воспроизведения
"playback.cancelled"          # При отмене воспроизведения
```

**Влияние RouteManager**:
- [ ] **Адаптация**: Добавить проверку `_avfoundation_output_enabled`
- [ ] **Если включен**: Использовать `AVFoundationAudioPlayback` вместо `sounddevice.OutputStream`
- [ ] **Если выключен**: Использовать текущую логику (fallback)
- [ ] **События сохранены**: Все существующие события публикуются как раньше

**Изменения**:
```python
async def _on_audio_chunk(self, event):
    # Если AVFoundation включен → используем AVFoundationAudioPlayback
    if self._avfoundation_output_enabled:
        # Конвертация numpy → AVAudioPCMBuffer
        audio_buffer = self._convert_to_avf_buffer(audio_data)
        self._avf_playback.schedule_buffer(audio_buffer)
    else:
        # Старая логика (fallback)
        self._player.add_audio_data(audio_data, ...)
```

---

### 3.4 ModeManagementIntegration

**Текущие подписки**:
```python
"mode.request"                # → _on_mode_request (применяет переход режима)
"app.mode_changed"            # → _on_app_mode_changed (обработка изменения режима)
"voice.recording_start"       # → _on_voice_recording_start (контекст для режимов)
"playback.completed"          # → _bridge_playback_done (переход в SLEEPING)
"playback.failed"             # → _bridge_playback_done (переход в SLEEPING)
```

**Текущие публикации**:
```python
"app.mode_changed"            # Через StateManager (факт смены режима)
```

**Влияние RouteManager**:
- [ ] **Минимальное**: ModeManagementIntegration только читает события
- [ ] **RouteManager подписывается**: RouteManager подписывается на `app.mode_changed` для проверки активных сессий
- [ ] **Нет конфликтов**: RouteManager НЕ публикует `app.mode_changed` (только читает)

**Изменения**: Минимальные (RouteManager только читает события)

---

### 3.5 TrayControllerIntegration

**Текущие подписки**:
```python
"app.mode_changed"            # → _on_app_mode_changed (обновление иконки)
"voice.mic_opened"            # → _on_voice_mic_opened (обновление статуса)
"voice.mic_closed"            # → _on_voice_mic_closed (обновление статуса)
"tray.status_updated"         # → _on_tray_status_updated (обновление UI)
```

**Текущие публикации**:
```python
"tray.status_updated"         # Обновление статуса tray
```

**Влияние RouteManager**:
- [ ] **Минимальное**: TrayControllerIntegration только читает события
- [ ] **События сохранены**: Все существующие события (`voice.mic_opened/closed`) публикуются как раньше
- [ ] **Нет конфликтов**: RouteManager НЕ публикует события tray (только читает)

**Изменения**: Минимальные (RouteManager только читает события)

---

### 3.6 InterruptManagementIntegration

**Текущие подписки**:
```python
"keyboard.short_press"        # → Прерывание
"voice.recognition_*"         # → Контекст для прерываний
"playback.*"                  # → Прерывание воспроизведения
"app.shutdown"                # → Очистка при завершении
```

**Текущие публикации**:
```python
"interrupt.request"           # Запрос прерывания
"interrupt.completed"         # Завершение прерывания
"mode.request"                # Запрос перехода в SLEEPING
```

**Влияние RouteManager**:
- [ ] **Минимальное**: InterruptManagementIntegration работает независимо от RouteManager
- [ ] **Прерывания сохранены**: Все существующие механизмы прерываний работают как раньше
- [ ] **Нет конфликтов**: RouteManager НЕ обрабатывает прерывания (это делает InterruptManagementIntegration)

**Изменения**: Минимальные (RouteManager не влияет на прерывания)

---

### 3.7 ListeningWorkflow и ProcessingWorkflow

**Текущие подписки**:
```python
# ListeningWorkflow
"app.mode_changed"            # → Переход в LISTENING
"voice.recognition_*"         # → Обработка результатов распознавания

# ProcessingWorkflow
"app.mode_changed"            # → Переход в PROCESSING
"screenshot.captured"        # → Захват скриншота
"grpc.request_*"             # → gRPC запросы
"playback.*"                  # → Воспроизведение
"keyboard.short_press"        # → Прерывания
```

**Влияние RouteManager**:
- [ ] **Минимальное**: Workflows только читают события
- [ ] **События сохранены**: Все существующие события публикуются как раньше
- [ ] **Нет конфликтов**: RouteManager НЕ влияет на workflows (только читает события)

**Изменения**: Минимальные (RouteManager не влияет на workflows)

---

## 4. Новый компонент: AudioRouteManagerIntegration

### 4.1 Подписки RouteManager

**События устройств**:
```python
"audio.device.connected"      # От AVFoundationDeviceMonitor
"audio.device.disconnected"   # От AVFoundationDeviceMonitor
"audio.device.default_changed" # От AVFoundationDeviceMonitor
```

**События записи**:
```python
"voice.recording_start"       # Запрос запуска input (от InputProcessingIntegration)
"voice.recording_stop"        # Запрос остановки input (от InputProcessingIntegration)
```

**События режимов**:
```python
"app.mode_changed"            # Проверка активных сессий
```

**События блокировок**:
```python
"permissions.first_run_started"   # Блокировка input
"permissions.first_run_completed" # Разблокировка input
"permission_restart.scheduled"    # Блокировка input
"permission_restart.executing"    # Блокировка input
"updater.in_progress.changed"     # Блокировка input/output
```

### 4.2 Публикации RouteManager

**События маршрутизации**:
```python
"audio.route.snapshot"         # Снимок состояния маршрутизации
"audio.input.active"          # Input стал активным
"audio.input.failed"          # Input не удалось запустить
"audio.output.ready"          # Output готов к воспроизведению
"audio.output.error"          # Ошибка output
```

**Важно**: RouteManager НЕ публикует события, которые уже публикуют другие интеграции (`voice.recording_start/stop`, `voice.mic_opened/closed`, `playback.*`). RouteManager только читает эти события и управляет маршрутизацией.

---

## 5. Матрица взаимодействий (кто читает/пишет что)

| Событие | Публикует | Читает | RouteManager |
|---------|-----------|--------|--------------|
| `voice.recording_start` | InputProcessingIntegration | VoiceRecognitionIntegration, ModeManagementIntegration, RouteManager | ✅ Читает |
| `voice.recording_stop` | InputProcessingIntegration | VoiceRecognitionIntegration, RouteManager | ✅ Читает |
| `voice.mic_opened` | VoiceRecognitionIntegration | InputProcessingIntegration, TrayControllerIntegration | ❌ Не публикует |
| `voice.mic_closed` | VoiceRecognitionIntegration | InputProcessingIntegration, TrayControllerIntegration | ❌ Не публикует |
| `voice.recognition_started` | VoiceRecognitionIntegration | InputProcessingIntegration, ListeningWorkflow | ❌ Не публикует |
| `voice.recognition_completed` | VoiceRecognitionIntegration | InputProcessingIntegration, ListeningWorkflow | ❌ Не публикует |
| `playback.started` | SpeechPlaybackIntegration | InputProcessingIntegration, ProcessingWorkflow, InterruptManagementIntegration | ❌ Не публикует |
| `playback.completed` | SpeechPlaybackIntegration | InputProcessingIntegration, ModeManagementIntegration, ProcessingWorkflow | ❌ Не публикует |
| `app.mode_changed` | ModeManagementIntegration (через StateManager) | VoiceRecognitionIntegration, TrayControllerIntegration, RouteManager, Workflows | ✅ Читает |
| `audio.route.snapshot` | RouteManager | (для диагностики) | ✅ Публикует |
| `audio.input.active` | RouteManager | (для диагностики) | ✅ Публикует |
| `audio.output.ready` | RouteManager | (для диагностики) | ✅ Публикует |

**Принцип**: RouteManager **НЕ дублирует** существующие события. Он только читает их и управляет маршрутизацией, публикуя новые диагностические события.

---

## 6. Порядок инициализации и зависимости

### 6.1 Текущий порядок (из SimpleModuleCoordinator)

```
1. instance_manager
2. tray
3. hardware_id
4. first_run_permissions      ← Блокирует активацию микрофона
5. permission_restart          ← Автоматический перезапуск
6. mode_management
7. input                      ← Использует voice_recognition
8. voice_recognition          ← Зависит от permissions
9. network
10. interrupt
11. screenshot_capture
12. grpc
13. speech_playback           ← Зависит от grpc
14. signals
15. updater
16. welcome_message
17. voiceover_ducking
18. autostart_manager
```

### 6.2 Новый порядок (с RouteManager)

```
1. instance_manager
2. tray
3. hardware_id
4. first_run_permissions      ← Блокирует активацию микрофона
5. permission_restart          ← Автоматический перезапуск
6. mode_management
7. input                      ← Использует voice_recognition
8. voice_recognition          ← Зависит от permissions
8.5. audio_route_manager      ← НОВЫЙ (после voice_recognition, перед использованием)
9. network
10. interrupt
11. screenshot_capture
12. grpc
13. speech_playback           ← Зависит от grpc (может использовать RouteManager)
14. signals
15. updater
16. welcome_message
17. voiceover_ducking
18. autostart_manager
```

**Зависимости RouteManager**:
- [ ] **Создается после**: `voice_recognition`, `speech_playback` (нужны ссылки на интеграции)
- [ ] **Инициализируется перед**: Использованием аудио (перед `input` активацией)
- [ ] **Условная инициализация**: Только если `NEXY_FEATURE_AVFOUNDATION_ROUTE_MANAGER_V2 = true`

---

## 7. Проверка на конфликты и дублирование

### 7.1 Потенциальные конфликты

| Конфликт | Описание | Решение |
|----------|----------|---------|
| **Дублирование запуска input** | VoiceRecognitionIntegration и RouteManager оба запускают input | ✅ RouteManager управляет запуском, VoiceRecognitionIntegration только публикует события |
| **Дублирование событий** | RouteManager публикует те же события, что и другие интеграции | ✅ RouteManager НЕ публикует существующие события, только новые диагностические |
| **Конфликт выбора устройств** | SpeechRecognizer и RouteManager оба выбирают устройства | ✅ RouteManager выбирает устройство, передает в SpeechRecognizer |
| **Конфликт timing** | RouteManager изменяет timing событий | ✅ RouteManager сохраняет существующий timing событий |

### 7.2 Проверка дублирования

**События, которые НЕ должны дублироваться**:
- [ ] `voice.recording_start/stop` - публикует только InputProcessingIntegration
- [ ] `voice.mic_opened/closed` - публикует только VoiceRecognitionIntegration
- [ ] `playback.started/completed` - публикует только SpeechPlaybackIntegration
- [ ] `app.mode_changed` - публикует только ModeManagementIntegration (через StateManager)

**События, которые RouteManager может публиковать**:
- [ ] `audio.route.snapshot` - новое диагностическое событие
- [ ] `audio.input.active` - новое диагностическое событие
- [ ] `audio.output.ready` - новое диагностическое событие

---

## 8. Чек-лист интеграции

### Перед реализацией
- [ ] Проверить все существующие подписки на аудио события
- [ ] Проверить все существующие публикации аудио событий
- [ ] Определить, какие события RouteManager должен читать
- [ ] Определить, какие события RouteManager может публиковать (только новые)
- [ ] Проверить порядок инициализации и зависимости

### Во время реализации
- [ ] RouteManager НЕ публикует существующие события
- [ ] RouteManager только читает существующие события
- [ ] Сохранить все существующие публикации событий
- [ ] Сохранить все существующие подписки на события
- [ ] Добавить feature flags для постепенного роллаута

### Тестирование
- [ ] Проверить, что все существующие события публикуются как раньше
- [ ] Проверить, что все существующие подписки работают как раньше
- [ ] Проверить, что RouteManager не дублирует события
- [ ] Проверить, что RouteManager не конфликтует с другими интеграциями
- [ ] Проверить порядок инициализации и зависимости

---

## 9. Заключение

**Принципы интеграции**:
1. ✅ **Минимальные изменения**: Существующие интеграции изменяются минимально
2. ✅ **Обратная совместимость**: Все существующие события сохраняются
3. ✅ **Нет дублирования**: RouteManager НЕ публикует существующие события
4. ✅ **Нет конфликтов**: RouteManager только читает события и управляет маршрутизацией
5. ✅ **Feature flags**: Постепенный роллаут с возможностью отката

**Критически важно**:
- RouteManager НЕ должен дублировать функциональность существующих интеграций
- RouteManager НЕ должен публиковать события, которые уже публикуют другие интеграции
- Все существующие взаимодействия должны сохраниться без изменений

