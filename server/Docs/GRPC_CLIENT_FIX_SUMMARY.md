# ✅ Резюме исправления клиентского подключения gRPC

**Дата:** 13 января 2026  
**Статус:** ✅ Исправлено

---

## 🎯 Проблема

Клиент использовал `insecure_channel` для подключения к TLS порту 443, что вызывало ошибку 400.

---

## ✅ Решение

Использовать `secure_channel` с сертификатом сервера для порта 443.

---

## 📝 Правильный код для клиента

```python
import grpc
from grpc import aio
import subprocess

def create_grpc_channel(host: str, port: int):
    """Создание gRPC канала с правильной настройкой TLS"""
    address = f"{host}:{port}"
    
    if port == 443:
        # Для TLS порта используем secure_channel
        # Скачиваем сертификат сервера для self-signed
        result = subprocess.run(
            ['openssl', 's_client', '-connect', address, '-showcerts'],
            input=b'', capture_output=True, timeout=5
        )
        
        cert_start = result.stdout.find(b'-----BEGIN CERTIFICATE-----')
        cert_end = result.stdout.find(b'-----END CERTIFICATE-----', cert_start)
        cert_pem = result.stdout[cert_start:cert_end + len(b'-----END CERTIFICATE-----')]
        
        credentials = grpc.ssl_channel_credentials(root_certificates=cert_pem)
        return aio.secure_channel(address, credentials)
    else:
        # Для локального тестирования
        return aio.insecure_channel(address)

# Использование
channel = create_grpc_channel("20.63.24.187", 443)
stub = streaming_pb2_grpc.StreamingServiceStub(channel)
```

---

## ✅ Результат

- ✅ Канал готов к использованию
- ✅ Запросы доходят до сервера
- ✅ HTTP 200 в логах Nginx

---

**Статус:** ✅ Проблема решена
