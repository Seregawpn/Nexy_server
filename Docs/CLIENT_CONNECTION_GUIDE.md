# Руководство по подключению клиента к серверу

**Обновлено:** 21 February 2026  
**Production host:** `nexy-prod-sergiy.canadacentral.cloudapp.azure.com`

## 1) Endpoint Contract

- gRPC: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443`
- Health: `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health`
- Status: `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status`

Важно:
- Для `:443` использовать только TLS (`secure_channel`).
- `insecure_channel` для production запрещён.

## 2) Python gRPC (Canonical)

```python
import grpc
from grpc import aio
import streaming_pb2
import streaming_pb2_grpc

host = "nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443"
credentials = grpc.ssl_channel_credentials()
channel = aio.secure_channel(host, credentials)
stub = streaming_pb2_grpc.StreamingServiceStub(channel)

request = streaming_pb2.StreamRequest(
    prompt="Привет",
    session_id="session-123",
    hardware_id="device-123"
)

async for response in stub.StreamAudio(request):
    if response.HasField("text_chunk"):
        print(response.text_chunk)
    elif response.HasField("audio_chunk"):
        print(len(response.audio_chunk.audio_data))
    elif response.HasField("end_message"):
        print(response.end_message)
        break
```

## 3) Required Request Fields

Для `StreamAudio` обязательно:
- `prompt`
- `session_id`
- `hardware_id`

Для `InterruptSession` обязательно:
- `hardware_id`

## 4) Health Check

```bash
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status
```

## 5) Typical Errors

- `UNAVAILABLE`: сеть/TLS/DNS или сервер недоступен.
- `INVALID_ARGUMENT`: не переданы обязательные поля (`session_id`, `hardware_id`, `prompt`).
- `RESOURCE_EXHAUSTED`: защита нагрузки, нужен retry/backoff.

## 6) Retry Guidance

- exponential backoff: 1s -> 2s -> 4s -> 8s
- max retries: 4
- при `INVALID_ARGUMENT` не ретраить, сначала исправить payload.
