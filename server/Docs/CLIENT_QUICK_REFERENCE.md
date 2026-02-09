# 📋 Быстрая справка по подключению клиента

**Версия:** 1.6.0.35  
**Дата:** 11 января 2026

---

## 🔗 Endpoints

```
gRPC:     20.63.24.187:443
Health:   https://20.63.24.187/health
Status:   https://20.63.24.187/status
```

---

## 🚀 Минимальный пример

```python
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

# Подключение
channel = aio.insecure_channel("20.63.24.187:443")
stub = streaming_pb2_grpc.StreamingServiceStub(channel)

# Запрос
request = streaming_pb2.StreamRequest(
    prompt="Привет!",
    hardware_id="your-device-id"
)

# Ответ
async for response in stub.StreamAudio(request):
    if response.text_chunk:
        print(response.text_chunk)
    elif response.audio_chunk:
        # Обработка аудио
        audio_data = response.audio_chunk.audio_data
```

---

## 📡 RPC методы

### StreamAudio
```python
request = streaming_pb2.StreamRequest(
    prompt="текст",           # Обязательно
    hardware_id="device-id"   # Обязательно
)
async for response in stub.StreamAudio(request):
    # Обработка ответов
```

### InterruptSession
```python
request = streaming_pb2.InterruptRequest(
    hardware_id="device-id"
)
response = await stub.InterruptSession(request)
```

---

## 🏥 Health Check

```python
import requests
response = requests.get("https://20.63.24.187/health", verify=False)
print(response.json())
```

---

## ⚠️ Ошибки

- `RESOURCE_EXHAUSTED` - Превышены лимиты, подождите
- `DEADLINE_EXCEEDED` - Таймаут, увеличьте время
- `UNAVAILABLE` - Сервер недоступен, повторите позже

---

## 📦 Зависимости

```bash
pip install grpcio>=1.76.0 grpcio-tools>=1.76.0 protobuf>=6.33.3
```

---

**Полное руководство:** `Docs/CLIENT_CONNECTION_GUIDE.md`
