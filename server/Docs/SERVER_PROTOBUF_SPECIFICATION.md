# Спецификация Protobuf для сервера GenerateWelcomeAudio

## Точные требования к формату ответа сервера

### 1. RPC Метод

```protobuf
rpc GenerateWelcomeAudio(WelcomeRequest) returns (stream WelcomeResponse);
```

**Важно:**
- Метод должен возвращать **stream** (поток) сообщений `WelcomeResponse`
- Не единичное сообщение, а поток!

---

### 2. Структура WelcomeRequest (что клиент отправляет)

```protobuf
message WelcomeRequest {
  string text = 1;                    // ОБЯЗАТЕЛЬНО: Текст приветствия
  optional string session_id = 2;     // Опционально: ID сессии
  optional string voice = 3;          // Опционально: Голос (например, "en-US")
  optional string language = 4;       // Опционально: Язык/локаль
}
```

**Пример запроса от клиента:**
```python
WelcomeRequest(
    text="Hi! Nexy is here. How can I help you?",
    session_id="welcome_1234567890.123",
    voice=None,  # или строка, если указана
    language=None  # или строка, если указана
)
```

---

### 3. Структура WelcomeResponse (что сервер ДОЛЖЕН отправлять)

```protobuf
message WelcomeResponse {
  oneof content {
    AudioChunk audio_chunk = 1;      // Аудио данные чанком
    WelcomeMetadata metadata = 2;    // Метаданные о сессии генерации
    string end_message = 3;          // Сообщение о завершении стрима
    string error_message = 4;        // Сообщение об ошибке
  }
}
```

**КРИТИЧЕСКИ ВАЖНО:**
- `oneof content` означает, что в каждом сообщении `WelcomeResponse` может быть **только одно** из полей: `audio_chunk`, `metadata`, `end_message` или `error_message`
- Нельзя отправлять несколько полей одновременно!

---

### 4. Структура AudioChunk

```protobuf
message AudioChunk {
  bytes audio_data = 1;        // ОБЯЗАТЕЛЬНО: Аудио данные в виде bytes
  string dtype = 2;           // Опционально: Тип данных (например, 'int16', 'float32')
  repeated int32 shape = 3;   // Опционально: Форма массива [samples, channels]
}
```

**Пример:**
```python
AudioChunk(
    audio_data=b'\x00\x01\x02\x03...',  # Сырые байты аудио
    dtype="int16",                      # Тип данных
    shape=[16000, 1]                    # [samples, channels]
)
```

---

### 5. Структура WelcomeMetadata

```protobuf
message WelcomeMetadata {
  string method = 1;          // ОБЯЗАТЕЛЬНО: Метод генерации (например, "server")
  double duration_sec = 2;    // ОБЯЗАТЕЛЬНО: Оценочная длительность в секундах
  int32 sample_rate = 3;      // ОБЯЗАТЕЛЬНО: Частота дискретизации (например, 16000, 22050, 44100)
  int32 channels = 4;         // ОБЯЗАТЕЛЬНО: Количество каналов (1 = mono, 2 = stereo)
}
```

**Пример:**
```python
WelcomeMetadata(
    method="server",
    duration_sec=2.5,
    sample_rate=22050,
    channels=1
)
```

---

## Правильная последовательность ответов сервера

### Сценарий успешной генерации:

1. **Метаданные** (опционально, но рекомендуется):
   ```
   WelcomeResponse {
     content: metadata {
       method: "server"
       duration_sec: 2.5
       sample_rate: 22050
       channels: 1
     }
   }
   ```

2. **Аудио чанки** (один или несколько):
   ```
   WelcomeResponse {
     content: audio_chunk {
       audio_data: <bytes>
       dtype: "int16"
       shape: [16000, 1]
     }
   }
   ```
   Может быть несколько чанков подряд.

3. **Завершение**:
   ```
   WelcomeResponse {
     content: end_message {
       "done"
     }
   }
   ```

### Сценарий ошибки:

```
WelcomeResponse {
  content: error_message {
    "Error generating audio: ..."
  }
}
```

---

## Требования для полного соответствия

### 1. Proto-файл на сервере

**Должен быть идентичен клиентскому:**

```protobuf
syntax = "proto3";

package streaming;

service StreamingService {
  rpc GenerateWelcomeAudio(WelcomeRequest) returns (stream WelcomeResponse);
}

message WelcomeRequest {
  string text = 1;
  optional string session_id = 2;
  optional string voice = 3;
  optional string language = 4;
}

message WelcomeResponse {
  oneof content {
    AudioChunk audio_chunk = 1;
    WelcomeMetadata metadata = 2;
    string end_message = 3;
    string error_message = 4;
  }
}

message WelcomeMetadata {
  string method = 1;
  double duration_sec = 2;
  int32 sample_rate = 3;
  int32 channels = 4;
}

message AudioChunk {
  bytes audio_data = 1;
  string dtype = 2;
  repeated int32 shape = 3;
}
```

**Проверка:**
- Сравните `streaming.proto` на сервере с клиентским файлом
- Должны совпадать: имена полей, номера полей, типы данных, `oneof` структуры

---

### 2. Версия protobuf библиотеки

**Клиент использует:** `protobuf 6.32.1`

**Сервер должен использовать:** совместимую версию (желательно ту же)

**Проверка на сервере:**
```bash
pip show protobuf
# или
python -c "import google.protobuf; print(google.protobuf.__version__)"
```

---

### 3. Сгенерированные stubs на сервере

**Должны быть пересобраны после изменения proto-файла:**

```bash
# На сервере
protoc --python_out=. streaming.proto
protoc --grpc_python_out=. --plugin=protoc-gen-grpc_python=grpc_tools.protoc_compiler streaming.proto
```

**Проверка:**
- Убедитесь, что `streaming_pb2.py` и `streaming_pb2_grpc.py` на сервере сгенерированы из актуального proto-файла
- Дата модификации stubs должна быть после последнего изменения proto-файла

---

### 4. Реализация метода на сервере

**Правильная реализация (пример на Python):**

```python
async def GenerateWelcomeAudio(
    self,
    request: streaming_pb2.WelcomeRequest,
    context: grpc.aio.ServicerContext
) -> AsyncIterator[streaming_pb2.WelcomeResponse]:
    """Генерирует приветственное аудио"""
    
    try:
        # 1. Отправляем метаданные (опционально)
        metadata = streaming_pb2.WelcomeMetadata(
            method="server",
            duration_sec=2.5,
            sample_rate=22050,
            channels=1
        )
        yield streaming_pb2.WelcomeResponse(metadata=metadata)
        
        # 2. Генерируем и отправляем аудио чанками
        audio_data = generate_audio(request.text)  # Ваша функция генерации
        
        # Разбиваем на чанки (например, по 16KB)
        chunk_size = 16384
        for i in range(0, len(audio_data), chunk_size):
            chunk = audio_data[i:i+chunk_size]
            
            audio_chunk = streaming_pb2.AudioChunk(
                audio_data=chunk,
                dtype="int16",
                shape=[len(chunk) // 2, 1]  # int16 = 2 bytes per sample
            )
            yield streaming_pb2.WelcomeResponse(audio_chunk=audio_chunk)
        
        # 3. Отправляем завершение
        yield streaming_pb2.WelcomeResponse(end_message="done")
        
    except Exception as e:
        # 4. В случае ошибки
        yield streaming_pb2.WelcomeResponse(error_message=str(e))
```

**КРИТИЧЕСКИ ВАЖНО:**
- Используйте `yield` для отправки каждого сообщения (stream)
- В каждом `WelcomeResponse` устанавливайте **только одно** поле из `oneof content`
- Не смешивайте поля в одном сообщении!

---

## Частые ошибки на сервере

### ❌ Ошибка 1: Неправильная структура oneof

```python
# НЕПРАВИЛЬНО:
response = WelcomeResponse()
response.audio_chunk = audio_chunk
response.metadata = metadata  # ❌ Ошибка! Можно только одно поле

# ПРАВИЛЬНО:
response1 = WelcomeResponse(metadata=metadata)
response2 = WelcomeResponse(audio_chunk=audio_chunk)
```

### ❌ Ошибка 2: Неправильные типы данных

```python
# НЕПРАВИЛЬНО:
audio_chunk.audio_data = "base64_string"  # ❌ Должен быть bytes, не string

# ПРАВИЛЬНО:
audio_chunk.audio_data = b'\x00\x01\x02...'  # ✅ bytes
```

### ❌ Ошибка 3: Неправильные номера полей

```python
# НЕПРАВИЛЬНО (если на сервере proto-файл с другими номерами):
message WelcomeResponse {
  oneof content {
    AudioChunk audio_chunk = 2;  # ❌ На клиенте это поле = 1!
  }
}

# ПРАВИЛЬНО (номера должны совпадать):
message WelcomeResponse {
  oneof content {
    AudioChunk audio_chunk = 1;  # ✅ Совпадает с клиентом
  }
}
```

### ❌ Ошибка 4: Старые stubs

```python
# Если proto-файл обновлен, но stubs не пересобраны:
# Сервер использует старую структуру → DecodeError на клиенте

# РЕШЕНИЕ: Пересобрать stubs
protoc --python_out=. streaming.proto
```

---

## Чек-лист для проверки на сервере

- [ ] **Proto-файл идентичен клиентскому**
  - Сравнить `streaming.proto` на сервере с клиентским
  - Проверить все поля, номера, типы, `oneof` структуры

- [ ] **Stubs пересобраны**
  - `streaming_pb2.py` и `streaming_pb2_grpc.py` сгенерированы из актуального proto
  - Дата модификации stubs после последнего изменения proto

- [ ] **Версия protobuf совместима**
  - Проверить версию: `pip show protobuf`
  - Рекомендуется: та же версия, что на клиенте (6.32.1)

- [ ] **Реализация метода правильная**
  - Использует `yield` для stream
  - В каждом `WelcomeResponse` только одно поле из `oneof content`
  - `audio_data` имеет тип `bytes`, не `string`
  - Номера полей совпадают с proto-файлом

- [ ] **Тестирование**
  - Протестировать метод локально
  - Проверить, что клиент может десериализовать ответ

---

## Канонический путь к proto-файлу

```
server/server/modules/grpc_service/streaming.proto
```

Этот файл является источником истины для серверной стороны; любые изменения синхронизируются с клиентом через канон протокола.








