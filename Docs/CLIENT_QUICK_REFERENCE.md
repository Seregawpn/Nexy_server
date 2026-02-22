# Быстрая справка клиента

**Обновлено:** 21 February 2026

## Endpoints

- gRPC: `nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443`
- Health: `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health`
- Status: `https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status`

## Важно

- Для production `:443` использовать `secure_channel`.
- `insecure_channel` для production не использовать.

## Minimal Python

```python
import grpc
from grpc import aio

credentials = grpc.ssl_channel_credentials()
channel = aio.secure_channel(
    "nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443",
    credentials,
)
```

## Быстрые проверки

```bash
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health
curl -fsS https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status
```
