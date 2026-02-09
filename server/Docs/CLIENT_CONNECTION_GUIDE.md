# 🔌 Руководство по подключению клиента к серверу

**Дата:** 11 января 2026  
**Версия сервера:** Актуальная версия доступна через `/health` endpoint  
**Статус:** ✅ Активно используется

---

## 📋 Оглавление

1. [Быстрый старт](#быстрый-старт)
2. [Информация о сервере](#информация-о-сервере)
3. [gRPC подключение](#grpc-подключение)
4. [RPC методы](#rpc-методы)
5. [Примеры кода](#примеры-кода)
6. [Health checks](#health-checks)
7. [Обработка ошибок](#обработка-ошибок)
8. [Конфигурация](#конфигурация)

---

## 🚀 Быстрый старт

### **Минимальный пример подключения:**

```python
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

# Подключение к серверу
channel = aio.insecure_channel("20.63.24.187:443")
stub = streaming_pb2_grpc.StreamingServiceStub(channel)

# Создание запроса
request = streaming_pb2.StreamRequest(
    prompt="Привет, как дела?",
    hardware_id="your-hardware-id-here"
)

# Отправка запроса
async for response in stub.StreamAudio(request):
    if response.text_chunk:
        print(f"Текст: {response.text_chunk}")
    elif response.audio_chunk:
        print(f"Аудио получено: {len(response.audio_chunk.audio_data)} байт")
```

---

## 🌐 Информация о сервере

### **Публичные endpoints:**

| Endpoint | URL | Протокол | Описание |
|----------|-----|----------|----------|
| gRPC | `20.63.24.187:443` | HTTPS/gRPC | Основной gRPC сервис |
| Health | `https://20.63.24.187/health` | HTTPS | Проверка здоровья сервера |
| Status | `https://20.63.24.187/status` | HTTPS | Статус сервиса |

### **Внутренние порты (недоступны извне):**

- `127.0.0.1:8080` - HTTP health/status (только локально на сервере)
- `127.0.0.1:50051` - gRPC (только локально на сервере)
- `127.0.0.1:8081` - Update server (только локально на сервере)

**⚠️ Важно:** Все внутренние сервисы привязаны к `127.0.0.1` для безопасности. Внешний доступ осуществляется только через Nginx на порту 443 (HTTPS).

---

## 🔌 gRPC подключение

### **1. Получение protobuf файлов**

Protobuf файлы находятся в репозитории:
- `server/modules/grpc_service/streaming.proto` - определение протокола
- `server/modules/grpc_service/streaming_pb2.py` - сгенерированные Python классы
- `server/modules/grpc_service/streaming_pb2_grpc.py` - сгенерированные gRPC stub'ы

**Для генерации из .proto файла:**
```bash
python -m grpc_tools.protoc \
    -I. \
    --python_out=. \
    --grpc_python_out=. \
    streaming.proto
```

### **2. Подключение к серверу**

#### **Python (async):**

```python
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

# Для production (HTTPS порт 443)
# ВАЖНО: Для TLS порта 443 нужно использовать secure_channel
# Для self-signed сертификата скачиваем сертификат сервера
import subprocess

# Скачиваем сертификат сервера
result = subprocess.run(
    ['openssl', 's_client', '-connect', '20.63.24.187:443', '-showcerts'],
    input=b'', capture_output=True, timeout=5
)
cert_start = result.stdout.find(b'-----BEGIN CERTIFICATE-----')
cert_end = result.stdout.find(b'-----END CERTIFICATE-----', cert_start)
cert_pem = result.stdout[cert_start:cert_end + len(b'-----END CERTIFICATE-----')]

# Используем secure_channel с сертификатом
credentials = grpc.ssl_channel_credentials(root_certificates=cert_pem)
channel = aio.secure_channel("20.63.24.187:443", credentials)
stub = streaming_pb2_grpc.StreamingServiceStub(channel)

# Для локального тестирования (если есть прямой доступ)
# channel = aio.insecure_channel("localhost:50051")
```

#### **Python (sync):**

```python
import grpc
import streaming_pb2
import streaming_pb2_grpc

channel = grpc.insecure_channel("20.63.24.187:443")
stub = streaming_pb2_grpc.StreamingServiceStub(channel)
```

#### **С SSL сертификатом (для production с валидным сертификатом):**

```python
import grpc
from grpc import aio

# С валидным SSL сертификатом
credentials = grpc.ssl_channel_credentials()
channel = aio.secure_channel("20.63.24.187:443", credentials)
```

---

## 📡 RPC методы

### **1. StreamAudio - Стриминг аудио и текста**

**Тип:** `unary_stream` (один запрос, поток ответов)

**Запрос (`StreamRequest`):**
```python
request = streaming_pb2.StreamRequest(
    prompt="Текстовая команда пользователя",  # Обязательно
    hardware_id="unique-hardware-id",          # Обязательно
    session_id="optional-session-id",          # Опционально
    screenshot="base64-webp-image",            # Опционально
    screen_width=1920,                         # Опционально
    screen_height=1080                         # Опционально
)
```

**Ответ (`StreamResponse`):**
```python
async for response in stub.StreamAudio(request):
    if response.HasField('text_chunk'):
        # Текстовый чанк
        text = response.text_chunk
        print(f"Текст: {text}")
    
    elif response.HasField('audio_chunk'):
        # Аудио чанк
        audio = response.audio_chunk
        audio_data = audio.audio_data  # bytes
        sample_rate = audio.sample_rate  # int (например, 24000)
        channels = audio.channels  # int (например, 1)
        dtype = audio.dtype  # str (например, 'int16')
        shape = audio.shape  # list[int] (например, [4800, 1])
    
    elif response.HasField('end_message'):
        # Сообщение о завершении
        print(f"Завершено: {response.end_message}")
        break
    
    elif response.HasField('error_message'):
        # Ошибка
        print(f"Ошибка: {response.error_message}")
        break
```

**Пример полного использования:**
```python
import asyncio
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

async def stream_audio_example():
    # Подключение
    channel = aio.insecure_channel("20.63.24.187:443")
    stub = streaming_pb2_grpc.StreamingServiceStub(channel)
    
    # Создание запроса
    request = streaming_pb2.StreamRequest(
        prompt="Расскажи о погоде",
        hardware_id="my-device-12345"
    )
    
    # Получение потока ответов
    try:
        async for response in stub.StreamAudio(request):
            if response.HasField('text_chunk'):
                print(f"📝 {response.text_chunk}")
            
            elif response.HasField('audio_chunk'):
                audio = response.audio_chunk
                print(f"🔊 Аудио: {len(audio.audio_data)} байт, "
                      f"{audio.sample_rate}Hz, {audio.channels} канал(ов)")
                # Воспроизведение аудио...
            
            elif response.HasField('end_message'):
                print(f"✅ {response.end_message}")
                break
            
            elif response.HasField('error_message'):
                print(f"❌ {response.error_message}")
                break
    
    except grpc.RpcError as e:
        print(f"gRPC ошибка: {e.code()} - {e.details()}")
    finally:
        await channel.close()

# Запуск
asyncio.run(stream_audio_example())
```

---

### **2. InterruptSession - Прерывание сессии**

**Тип:** `unary_unary` (один запрос, один ответ)

**Запрос:**
```python
request = streaming_pb2.InterruptRequest(
    hardware_id="unique-hardware-id"  # Обязательно
)
```

**Ответ:**
```python
response = stub.InterruptSession(request)
if response.success:
    print(f"✅ Прервано сессий: {len(response.interrupted_sessions)}")
    for session_id in response.interrupted_sessions:
        print(f"  - {session_id}")
else:
    print(f"❌ Ошибка: {response.message}")
```

**Пример:**
```python
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

async def interrupt_example():
    channel = aio.insecure_channel("20.63.24.187:443")
    stub = streaming_pb2_grpc.StreamingServiceStub(channel)
    
    request = streaming_pb2.InterruptRequest(
        hardware_id="my-device-12345"
    )
    
    try:
        response = await stub.InterruptSession(request)
        if response.success:
            print(f"✅ Прервано: {response.message}")
        else:
            print(f"❌ {response.message}")
    except grpc.RpcError as e:
        print(f"Ошибка: {e.code()} - {e.details()}")
    finally:
        await channel.close()

asyncio.run(interrupt_example())
```

---

### **3. GenerateWelcomeAudio - Приветственное аудио**

**Тип:** `unary_stream` (один запрос, поток ответов)

**Запрос:**
```python
request = streaming_pb2.WelcomeRequest(
    text="Добро пожаловать!",  # Опционально
    session_id="session-123",  # Опционально
    voice="en-US-AriaNeural",   # Опционально
    language="en-US"            # Опционально
)
```

**Ответ:**
```python
async for response in stub.GenerateWelcomeAudio(request):
    if response.HasField('audio_chunk'):
        audio = response.audio_chunk
        # Обработка аудио...
    
    elif response.HasField('metadata'):
        metadata = response.metadata
        print(f"Метод: {metadata.method}")
        print(f"Длительность: {metadata.duration_sec} сек")
        print(f"Sample rate: {metadata.sample_rate} Hz")
    
    elif response.HasField('end_message'):
        break
    
    elif response.HasField('error_message'):
        print(f"Ошибка: {response.error_message}")
        break
```

---

## 🏥 Health checks

### **Проверка доступности сервера:**

```python
import requests

# Health endpoint
response = requests.get("https://20.63.24.187/health", verify=False)
if response.status_code == 200:
    data = response.json()
    print(f"Статус: {data['status']}")
    print(f"Версия: {data['latest_version']}")
    print(f"Build: {data['latest_build']}")

# Status endpoint
response = requests.get("https://20.63.24.187/status", verify=False)
if response.status_code == 200:
    data = response.json()
    print(f"Сервис: {data['service']}")
    print(f"Статус: {data['status']}")
```

**Ожидаемый ответ Health:**
```json
{
  "status": "OK",
  "latest_version": "<версия из VERSION файла>",
  "latest_build": "<версия из VERSION файла>"
}
```

**Ожидаемый ответ Status:**
```json
{
  "status": "running",
  "service": "voice-assistant",
  "latest_version": "<версия из VERSION файла>",
  "latest_build": "<версия из VERSION файла>",
  "update_server": "enabled",
  "endpoints": {
    "health": "/health",
    "status": "/status",
    "grpc": "port 50051",
    "updates": "port 8081"
  }
}
```

**Примечание:** Версия сервера синхронизируется из единого источника (`VERSION` файл) и автоматически обновляется при деплое.

---

## ⚠️ Обработка ошибок

### **gRPC коды ошибок:**

| Код | Название | Описание | Действие |
|-----|----------|----------|----------|
| `OK` | Успех | Запрос выполнен успешно | - |
| `CANCELLED` | Отменено | Запрос отменен клиентом | Повторить при необходимости |
| `DEADLINE_EXCEEDED` | Таймаут | Превышено время ожидания | Увеличить таймаут или повторить |
| `RESOURCE_EXHAUSTED` | Ресурсы исчерпаны | Лимиты превышены (backpressure) | Подождать и повторить |
| `UNAVAILABLE` | Недоступен | Сервер недоступен | Повторить позже |
| `UNAUTHENTICATED` | Не авторизован | Требуется аутентификация | Проверить credentials |
| `INTERNAL` | Внутренняя ошибка | Ошибка сервера | Сообщить в поддержку |

### **Пример обработки ошибок:**

```python
import grpc
from grpc import StatusCode

try:
    async for response in stub.StreamAudio(request):
        # Обработка ответов...
        pass

except grpc.RpcError as e:
    if e.code() == StatusCode.RESOURCE_EXHAUSTED:
        print("⚠️ Превышены лимиты. Подождите и повторите.")
    elif e.code() == StatusCode.DEADLINE_EXCEEDED:
        print("⏱️ Таймаут. Увеличьте время ожидания.")
    elif e.code() == StatusCode.UNAVAILABLE:
        print("🔌 Сервер недоступен. Повторите позже.")
    else:
        print(f"❌ Ошибка: {e.code()} - {e.details()}")
```

---

## ⚙️ Конфигурация

### **Рекомендуемые настройки:**

```python
# Таймауты
GRPC_TIMEOUT = 300  # 5 минут для длительных стримов (увеличено для длинных TTS ответов)
GRPC_CONNECT_TIMEOUT = 10  # 10 секунд на подключение

# Retry политика
MAX_RETRIES = 3
RETRY_DELAY = 1  # секунды

# Backpressure (актуальные настройки сервера)
# Сервер использует следующие лимиты:
# - max_concurrent_streams: 50 (prod)
# - idle_timeout_seconds: 900 (15 минут для длинных TTS ответов)
# - max_message_rate_per_second: 0 (отключено для аудио стримов)
```

### **Особенности текущего сервера:**

1. **Backpressure Manager:**
   - Автоматическое управление нагрузкой на стримы
   - Защита от "молчаливых" клиентов (idle timeout: 15 минут)
   - Rate limiting отключен для аудио стримов (0 = без ограничений)

2. **Graceful Shutdown:**
   - Сервер корректно завершает активные стримы при остановке
   - Все ресурсы освобождаются автоматически

3. **Структурированное логирование:**
   - Все логи в едином формате: `ts=... level=INFO scope=grpc method=... decision=... ctx={...}`
   - Автоматическая маскировка секретов в логах

4. **Метрики:**
   - Автоматический сбор метрик производительности
   - P95 latency, error rate, decision rate

### **Пример с retry:**

```python
import asyncio
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

async def stream_with_retry(prompt: str, hardware_id: str, max_retries: int = 3):
    for attempt in range(max_retries):
        try:
            channel = aio.insecure_channel("20.63.24.187:443")
            stub = streaming_pb2_grpc.StreamingServiceStub(channel)
            
            request = streaming_pb2.StreamRequest(
                prompt=prompt,
                hardware_id=hardware_id
            )
            
            async for response in stub.StreamAudio(request, timeout=300):
                yield response
            
            await channel.close()
            break  # Успешно, выходим из цикла
        
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.RESOURCE_EXHAUSTED:
                wait_time = 2 ** attempt  # Экспоненциальная задержка
                print(f"⚠️ Лимит превышен. Ожидание {wait_time} сек...")
                await asyncio.sleep(wait_time)
            elif attempt == max_retries - 1:
                raise  # Последняя попытка, пробрасываем ошибку
            else:
                await asyncio.sleep(1)  # Короткая задержка перед повтором
```

---

## 📦 Зависимости

### **Python:**

```bash
pip install grpcio grpcio-tools protobuf
```

### **Требуемые версии:**

- `grpcio >= 1.76.0`
- `grpcio-tools >= 1.76.0`
- `protobuf >= 6.33.3,<7.0.0`

---

## 🔐 Безопасность

### **Важные замечания:**

1. **Self-signed сертификат:** Сервер использует self-signed SSL сертификат. Для production рекомендуется использовать валидный сертификат.

2. **Hardware ID:** Всегда используйте уникальный `hardware_id` для каждого устройства.

3. **Таймауты:** Устанавливайте разумные таймауты для предотвращения зависаний. Рекомендуется использовать таймаут 300 секунд (5 минут) для длительных стримов.

4. **Backpressure:** 
   - Максимум 50 одновременных стримов на сервере (prod)
   - Idle timeout: 15 минут (для длинных TTS ответов)
   - Rate limiting отключен для аудио стримов
   - При превышении лимитов сервер вернёт `RESOURCE_EXHAUSTED`

5. **Внутренние порты:** Все внутренние сервисы (8080, 50051, 8081) привязаны к `127.0.0.1` и недоступны извне. Внешний доступ только через Nginx на порту 443.

---

## 📝 Полный пример клиента

```python
#!/usr/bin/env python3
"""
Полный пример клиента для Nexy Server
"""

import asyncio
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

class NexyClient:
    """Клиент для подключения к Nexy Server"""
    
    def __init__(self, host: str = "20.63.24.187", port: int = 443):
        self.host = host
        self.port = port
        self.channel = None
        self.stub = None
    
    async def connect(self):
        """Подключение к серверу"""
        address = f"{self.host}:{self.port}"
        self.channel = aio.insecure_channel(address)
        self.stub = streaming_pb2_grpc.StreamingServiceStub(self.channel)
        print(f"✅ Подключено к {address}")
    
    async def disconnect(self):
        """Отключение от сервера"""
        if self.channel:
            await self.channel.close()
            print("✅ Отключено от сервера")
    
    async def stream_audio(self, prompt: str, hardware_id: str):
        """Стриминг аудио и текста"""
        request = streaming_pb2.StreamRequest(
            prompt=prompt,
            hardware_id=hardware_id
        )
        
        try:
            async for response in self.stub.StreamAudio(request, timeout=300):
                if response.HasField('text_chunk'):
                    yield {'type': 'text', 'data': response.text_chunk}
                
                elif response.HasField('audio_chunk'):
                    audio = response.audio_chunk
                    yield {
                        'type': 'audio',
                        'data': audio.audio_data,
                        'sample_rate': audio.sample_rate,
                        'channels': audio.channels,
                        'dtype': audio.dtype
                    }
                
                elif response.HasField('end_message'):
                    yield {'type': 'end', 'data': response.end_message}
                    break
                
                elif response.HasField('error_message'):
                    yield {'type': 'error', 'data': response.error_message}
                    break
        
        except grpc.RpcError as e:
            yield {'type': 'error', 'data': f"gRPC ошибка: {e.code()} - {e.details()}"}
    
    async def interrupt_session(self, hardware_id: str):
        """Прерывание активной сессии"""
        request = streaming_pb2.InterruptRequest(hardware_id=hardware_id)
        
        try:
            response = await self.stub.InterruptSession(request)
            return {
                'success': response.success,
                'message': response.message,
                'interrupted_sessions': list(response.interrupted_sessions)
            }
        except grpc.RpcError as e:
            return {
                'success': False,
                'message': f"gRPC ошибка: {e.code()} - {e.details()}"
            }

async def main():
    """Пример использования"""
    client = NexyClient()
    
    try:
        await client.connect()
        
        # Стриминг аудио
        print("\n🎤 Отправка запроса...")
        async for chunk in client.stream_audio(
            prompt="Привет! Расскажи о себе.",
            hardware_id="test-device-12345"
        ):
            if chunk['type'] == 'text':
                print(f"📝 {chunk['data']}")
            elif chunk['type'] == 'audio':
                print(f"🔊 Аудио: {len(chunk['data'])} байт")
            elif chunk['type'] == 'end':
                print(f"✅ {chunk['data']}")
                break
            elif chunk['type'] == 'error':
                print(f"❌ {chunk['data']}")
                break
        
        # Прерывание сессии
        print("\n🛑 Прерывание сессии...")
        result = await client.interrupt_session("test-device-12345")
        print(f"Результат: {result}")
    
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📚 Дополнительные ресурсы

- **Protobuf определение:** `server/modules/grpc_service/streaming.proto`
- **gRPC Protocol Audit:** `Docs/GRPC_PROTOCOL_AUDIT.md`
- **Remote Server Configuration:** `Docs/REMOTE_SERVER_CONFIG.md` - Особенности удалённого сервера
- **Architecture Overview:** `server/Docs/ARCHITECTURE_OVERVIEW.md`
- **Performance Analysis:** `Docs/PERFORMANCE_BOTTLENECK_ANALYSIS.md`

---

## ✅ Чеклист подключения

- [ ] Установлены зависимости (`grpcio`, `grpcio-tools`, `protobuf`)
- [ ] Получены protobuf файлы (`streaming_pb2.py`, `streaming_pb2_grpc.py`)
- [ ] Проверен health endpoint (`https://20.63.24.187/health`)
- [ ] Создан gRPC channel к `20.63.24.187:443`
- [ ] Указан уникальный `hardware_id`
- [ ] Настроена обработка ошибок
- [ ] Установлены таймауты
- [ ] Протестировано подключение

---

**Готово к использованию!** 🚀
