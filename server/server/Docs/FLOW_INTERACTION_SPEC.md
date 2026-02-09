# FLOW_INTERACTION_SPEC (SERVER)

Единый источник истины по взаимодействию серверных Flow, контрактам gRPC и требованиям к формату обмена. Все профильные документы должны ссылаться сюда и не дублировать общий контракт.

## 0) Область и источники истины

- Область: серверная часть Nexy (gRPC + module orchestration).
- Источник истины по протоколу: `Docs/GRPC_PROTOCOL_AUDIT.md` и `modules/grpc_service/streaming.proto`.
- Источник истины по архитектуре: `Docs/ARCHITECTURE_OVERVIEW.md`.
- Этот документ: Source of Truth по server flow и gRPC контрактам.

## 1) Инварианты

- `session_id` и gRPC статусы формируются только в `grpc_service/core/grpc_server.py`.
- Один активный StreamAudio на `session_id` (single-flight).
- Ошибка до старта стрима → `error_message`; после частичных данных → тихое завершение (без смешивания ошибок и данных).
- Все лимиты/таймауты — из `config/unified_config.yaml`, никаких магических чисел.

## 2) gRPC контракты (канонические)

Source: `modules/grpc_service/streaming.proto`

### 2.1 StreamAudio

Request: `StreamRequest`
```yaml
required:
  prompt: str
  hardware_id: str
optional:
  screenshot: str   # base64 WebP
  screen_width: int
  screen_height: int
  session_id: str
```

Response: `StreamResponse` (oneof)
```yaml
content:
  text_chunk: str
  audio_chunk:
    audio_data: bytes
    dtype: str
    shape: list[int]
    sample_rate: int
    channels: int
  end_message: str
  error_message: str
```

### 2.2 InterruptSession

Request: `InterruptRequest`
```yaml
required:
  hardware_id: str
```

Response: `InterruptResponse`
```yaml
required:
  success: bool
  interrupted_sessions: list[str]
  message: str
```

### 2.3 GenerateWelcomeAudio

Request: `WelcomeRequest`
```yaml
optional:
  text: str
  session_id: str
  voice: str
  language: str
```

Response: `WelcomeResponse` (oneof)
```yaml
content:
  audio_chunk: AudioChunk
  metadata:
    method: str
    duration_sec: float
    sample_rate: int
    channels: int
  end_message: str
  error_message: str
```

## 3) Flow Specs

### 3.1 StreamAudio Flow (основной запрос)

Coordinator: `GrpcServiceManager`  
Source of Truth: `grpc_service/core/grpc_server.py`  

Sequence:
1. `StreamAudio` получает `StreamRequest`.
2. Валидация: `hardware_id`, `prompt`, размер/формат скриншота (если есть).
3. `session_id`:
   - если пришел — используется как внешний идентификатор,
   - иначе создается сервером.
4. Проверка single-flight по `session_id`; при конфликте — `error_message`.
5. Формируется контекст запроса (session, metadata, policies).
6. Вызов `GrpcServiceManager` → `ModuleCoordinator` для пайплайна:
   - `text_processing` (нормализация, фильтры),
   - `memory_management` (контекст),
   - `audio_generation` (TTS/streaming),
   - `interrupt_handling` (подписка на прерывания).
7. Стриминг ответа:
   - `text_chunk` (опционально)  
   - `audio_chunk` (обязательны `sample_rate`, `channels`, `dtype`, `shape`)  
8. Завершение:
   - 정상ное: `end_message`
   - ошибка до стрима: `error_message`
   - ошибка после чанков: graceful stop (без `error_message`)

Requirements:
- Нельзя публиковать пустые `audio_chunk`.
- `sample_rate` и `channels` обязательны в каждом `audio_chunk`.
- Все ошибки логируются и маппятся на корректный gRPC статус.

### 3.2 InterruptSession Flow

Coordinator: `interrupt_handling` + `session_management`  
Source of Truth: `SessionRegistry` (`modules/session_management/core/session_registry.py`)  
Interrupt Flags: `GlobalFlagProvider` (`modules/interrupt_handling/providers/global_flag_provider.py`)  

Sequence:
1. `InterruptSession` получает `hardware_id`.
2. Находит активные сессии, связанные с `hardware_id`.
3. Инициирует cancellation в `interrupt_handling`.
4. Возвращает список `interrupted_sessions`.

Requirements:
- Идемпотентность: повторный interrupt не вызывает ошибок.
- Прерывание не должно оставлять активные стримы.

### 3.3 Welcome Audio Flow

Coordinator: `GrpcServiceManager`  
Source of Truth: `audio_generation`  

Sequence:
1. `GenerateWelcomeAudio` получает `WelcomeRequest`.
2. Если `text` пуст — используется дефолтный шаблон.
3. Публикуется `metadata` один раз в начале.
4. Стримятся `audio_chunk`, затем `end_message`.
5. При ошибке до стрима — `error_message`.

Requirements:
- `metadata` отправляется один раз на старте.

### 3.4 Update / Maintenance Flows (сервер)

Coordinator: `modules/update`  
Source of Truth: `config/unified_config.yaml`  

Sequence:
1. Обновления проверяются и устанавливаются согласно `UPDATE_SYSTEM_FIXES.md`.
2. Наблюдаемость: метрики и алерты обязаны отражать состояние обновления.

## 4) Запреты и совместимость

- Запрещено изменять протокол без синхронизации `streaming.proto` + `GRPC_PROTOCOL_AUDIT.md`.
- Запрещены локальные обходы single-flight.
- Любые новые gRPC методы должны появиться здесь и в `ARCHITECTURE_OVERVIEW.md`.
