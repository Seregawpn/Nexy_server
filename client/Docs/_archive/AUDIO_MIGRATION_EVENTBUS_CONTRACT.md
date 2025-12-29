# Контракт EventBus для AudioRouteManagerIntegration

**Статус**: Обязательный контракт  
**Версия**: 1.0  
**Дата**: 2025-12-23

---

## 📋 Общая информация

**Модуль**: `audio_route_manager`  
**Интеграция**: `AudioRouteManagerIntegration`  
**Версия контракта**: 1.0

---

## 🔌 Входные события (подписки)

### 1. voice.recording_start

**Источник**: `InputProcessingIntegration`  
**Описание**: Запрос начала записи (push-to-talk)

**Payload**:
```python
{
    "session_id": "string (uuid4, required)",
    "timestamp": "float (optional)",
    "source": "string (optional, default: input_processing)"
}
```

**Обработка**: AudioRouteManagerIntegration запускает input через reconcile loop

---

### 2. voice.recording_stop

**Источник**: `InputProcessingIntegration`  
**Описание**: Запрос остановки записи

**Payload**:
```python
{
    "session_id": "string (uuid4, required)",
    "timestamp": "float (optional)",
    "source": "string (optional, default: input_processing)"
}
```

**Обработка**: AudioRouteManagerIntegration останавливает input stream

---

### 3. app.mode_changed

**Источник**: `ModeManagementIntegration`  
**Описание**: Изменение режима приложения

**Payload**:
```python
{
    "old_mode": "AppMode (SLEEPING|LISTENING|PROCESSING)",
    "new_mode": "AppMode (SLEEPING|LISTENING|PROCESSING)",
    "session_id": "string (uuid4, optional)"
}
```

**Обработка**: AudioRouteManagerIntegration проверяет необходимость переключения устройств

---

### 4. permissions.first_run_started

**Источник**: `FirstRunPermissionsIntegration`  
**Описание**: Начало процесса первого запуска

**Payload**:
```python
{
    "session_id": "string (uuid4, optional)"
}
```

**Обработка**: AudioRouteManagerIntegration блокирует активацию input/output

---

### 5. permissions.first_run_completed

**Источник**: `FirstRunPermissionsIntegration`  
**Описание**: Завершение процесса первого запуска

**Payload**:
```python
{
    "session_id": "string (uuid4, optional)"
}
```

**Обработка**: AudioRouteManagerIntegration разблокирует активацию input/output

---

### 6. permissions.first_run_failed

**Источник**: `FirstRunPermissionsIntegration`  
**Описание**: Ошибка процесса первого запуска

**Payload**:
```python
{
    "session_id": "string (uuid4, optional)",
    "error": "string (optional)"
}
```

**Обработка**: AudioRouteManagerIntegration разблокирует активацию input/output

---

## 📤 Выходные события (публикации)

### 1. audio.input.request_start

**Описание**: Запрос запуска audio input (внутреннее событие, опционально)

**Payload**:
```python
{
    "session_id": "string (uuid4, required)",
    "source": "string (optional, default: audio_route_manager)"
}
```

**Подписчики**: Нет (внутреннее событие для координации)

---

### 2. audio.input.active

**Описание**: Audio input активен, можно получать данные

**Payload**:
```python
{
    "session_id": "string (uuid4, required)",
    "device_uid": "string (required)",
    "device_name": "string (required)",
    "device_index": "int (optional)",
    "sample_rate": "int (optional)",
    "channels": "int (optional, default: 1)"
}
```

**Подписчики**:
- `VoiceRecognitionIntegration` (получение аудио-данных)

**Валидация**:
```python
@dataclass
class AudioInputActivePayload:
    session_id: str
    device_uid: str
    device_name: str
    device_index: Optional[int] = None
    sample_rate: Optional[int] = None
    channels: int = 1
    
    def validate(self) -> bool:
        if not self.session_id or not self.device_uid or not self.device_name:
            return False
        if self.channels < 1:
            return False
        return True
```

---

### 3. audio.input.inactive

**Описание**: Audio input неактивен

**Payload**:
```python
{
    "session_id": "string (uuid4, required)",
    "reason": "string (optional, stop|error|device_switch)"
}
```

**Подписчики**:
- `VoiceRecognitionIntegration` (очистка состояния)

---

### 4. audio.input.device_changed

**Описание**: Input устройство изменилось

**Payload**:
```python
{
    "old_device_uid": "string (required)",
    "new_device_uid": "string (required)",
    "old_device_name": "string (optional)",
    "new_device_name": "string (optional)",
    "old_device_index": "int (optional)",
    "new_device_index": "int (optional)"
}
```

**Подписчики**:
- `VoiceRecognitionIntegration` (адаптация к новому устройству)

---

### 5. audio.output.ready

**Описание**: Audio output готов, можно воспроизводить

**Payload**:
```python
{
    "device_uid": "string (required)",
    "device_name": "string (required)",
    "device_index": "int (optional)",
    "sample_rate": "int (optional)",
    "channels": "int (optional, default: 2)"
}
```

**Подписчики**:
- `SpeechPlaybackIntegration` (проверка готовности перед воспроизведением)

**Валидация**:
```python
@dataclass
class AudioOutputReadyPayload:
    device_uid: str
    device_name: str
    device_index: Optional[int] = None
    sample_rate: Optional[int] = None
    channels: int = 2
    
    def validate(self) -> bool:
        if not self.device_uid or not self.device_name:
            return False
        if self.channels < 1:
            return False
        return True
```

---

### 6. audio.output.device_changed

**Описание**: Output устройство изменилось

**Payload**:
```python
{
    "old_device_uid": "string (required)",
    "new_device_uid": "string (required)",
    "old_device_name": "string (optional)",
    "new_device_name": "string (optional)",
    "old_device_index": "int (optional)",
    "new_device_index": "int (optional)"
}
```

**Подписчики**:
- `SpeechPlaybackIntegration` (адаптация к новому устройству)

---

### 7. audio.device.changed

**Описание**: Уведомление о смене устройства (input или output)

**Payload**:
```python
{
    "type": "string (input|output, required)",
    "old_device_uid": "string (required)",
    "new_device_uid": "string (required)",
    "old_device_name": "string (optional)",
    "new_device_name": "string (optional)"
}
```

**Подписчики**:
- `VoiceRecognitionIntegration` (если type == "input")
- `SpeechPlaybackIntegration` (если type == "output")

**Валидация**:
```python
@dataclass
class AudioDeviceChangedPayload:
    type: str  # "input" | "output"
    old_device_uid: str
    new_device_uid: str
    old_device_name: Optional[str] = None
    new_device_name: Optional[str] = None
    
    def validate(self) -> bool:
        if self.type not in ("input", "output"):
            return False
        if not self.old_device_uid or not self.new_device_uid:
            return False
        return True
```

---

### 8. audio.route.snapshot

**Описание**: Снимок состояния маршрутизации (для диагностики)

**Payload**:
```python
{
    "input_state": "string (idle|starting|active|stopping|error, required)",
    "output_state": "string (idle|initializing|ready|playing|error, required)",
    "input_device_uid": "string (optional)",
    "output_device_uid": "string (optional)",
    "reconcile_pending": "bool (optional, default: false)",
    "timestamp": "float (optional)"
}
```

**Подписчики**: Нет (только для диагностики/логирования)

---

## 🔍 Валидация payload

### Место валидации

Валидация выполняется на границе интеграции (в `AudioRouteManagerIntegration`) перед публикацией событий.

### Метод валидации

Использовать Pydantic или dataclasses с type hints и методами валидации.

### Пример валидации

```python
from dataclasses import dataclass
from typing import Optional, Literal

@dataclass
class AudioInputActivePayload:
    session_id: str
    device_uid: str
    device_name: str
    device_index: Optional[int] = None
    sample_rate: Optional[int] = None
    channels: int = 1
    
    def validate(self) -> tuple[bool, Optional[str]]:
        """Валидация payload. Возвращает (is_valid, error_message)"""
        if not self.session_id:
            return False, "session_id is required"
        if not self.device_uid:
            return False, "device_uid is required"
        if not self.device_name:
            return False, "device_name is required"
        if self.channels < 1:
            return False, "channels must be >= 1"
        return True, None
```

---

## 🧪 Тесты контракта

### Unit тесты

- [ ] Валидация всех payload схем
- [ ] Проверка обязательных полей
- [ ] Проверка типов данных
- [ ] Проверка граничных значений

### Integration тесты

- [ ] Публикация событий работает
- [ ] Подписки на события работают
- [ ] Payload передается корректно
- [ ] Обработка событий работает

---

## 📝 Версионирование

### Текущая версия: 1.0

**Правила версионирования**:
- **Мажорные изменения** (breaking): новая версия события (`audio.input.active.v2`)
- **Минорные изменения** (совместимые): добавление optional полей
- **Обратная совместимость**: старые события поддерживаются 2 версии

### Миграция

При необходимости миграции использовать feature flags и shadow-mode (см. `.cursorrules` раздел 16.5.1).

---

## ✅ Чек-лист контракта

- [x] Все события документированы с полными payload схемами
- [ ] Валидация payload на границе интеграции
- [ ] Обработка ошибок через ErrorHandler с кодами
- [ ] Тесты контракта (unit + integration)
- [ ] Примеры использования в README
- [x] Версионирование для breaking changes
- [x] Обратная совместимость соблюдена

