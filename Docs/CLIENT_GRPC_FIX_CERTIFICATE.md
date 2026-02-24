# ✅ Исправление: Отсутствие сертификата для production сервера

**Дата:** 13 января 2026  
**Проблема:** Клиент не может подключиться к production серверу из-за отсутствия сертификата

---

## 🔍 Проблема

Клиент пытается загрузить сертификат из файла:
- `client/resources/certs/production_server.pem`

Если файла нет, клиент использует `insecure_channel`, что **не работает** с TLS портом 443.

---

## ✅ Решение

### Шаг 1: Скачать сертификат сервера

```bash
openssl s_client -connect nexy-prod-sergiy.canadacentral.cloudapp.azure.com:443 -showcerts </dev/null 2>/dev/null | \
  openssl x509 -outform PEM > client/resources/certs/production_server.pem
```

### Шаг 2: Проверить конфигурацию

В `config/unified_config.yaml` должно быть:
```yaml
grpc:
  servers:
    production:
      host: nexy-prod-sergiy.canadacentral.cloudapp.azure.com
      port: 443
      ssl: true
      ssl_verify: false  # ВАЖНО для self-signed
```

### Шаг 3: Проверить логи

После исправления в логах должно быть:
```
✅ Загружен self-signed сертификат: .../production_server.pem
✅ _ensure_connected: gRPC connected to production
Starting gRPC stream for session ...
```

---

## 🔧 Альтернативное решение

Если файл сертификата недоступен, можно изменить `connection_manager.py` чтобы он скачивал сертификат автоматически (как в тестовом скрипте):

```python
# В connection_manager.py, вместо загрузки из файла:
try:
    import subprocess
    result = subprocess.run(
        ['openssl', 's_client', '-connect', address, '-showcerts'],
        input=b'', capture_output=True, timeout=5
    )
    cert_start = result.stdout.find(b'-----BEGIN CERTIFICATE-----')
    cert_end = result.stdout.find(b'-----END CERTIFICATE-----', cert_start)
    cert_pem = result.stdout[cert_start:cert_end + len(b'-----END CERTIFICATE-----')]
    credentials = grpc.ssl_channel_credentials(root_certificates=cert_pem)
except Exception as e:
    logger.error(f"Не удалось скачать сертификат: {e}")
    # Fallback...
```

---

## ✅ Проверка

После исправления:
1. ✅ Сертификат должен быть в `client/resources/certs/production_server.pem`
2. ✅ В логах должно быть "Загружен self-signed сертификат"
3. ✅ В логах должно быть "gRPC connected to production"
4. ✅ Запросы должны отправляться на сервер

---

**Статус:** ✅ Сертификат скачан и размещён в правильной директории
