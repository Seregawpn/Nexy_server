# Backpressure Configuration Guide

## Обзор

Backpressure система защищает сервер от перегрузки, ограничивая количество одновременно открытых стримов и частоту сообщений.

## Конфигурация

### YAML конфигурация (см. единый источник истины)

```yaml
backpressure:
  max_concurrent_streams: <int>      # Значение задается в unified_config.py
  idle_timeout_seconds: <int>        # Значение задается в unified_config.py
  max_message_rate_per_second: <int> # 0 = отключить rate limit
  grace_period_seconds: <int>        # Значение задается в unified_config.py
```

**Важно:** Установите `max_message_rate_per_second: 0` для полного отключения rate limit (полезно для аудио стримов с высокой частотой чанков).

### Переменные окружения

```bash
BACKPRESSURE_MAX_STREAMS=<int>
BACKPRESSURE_IDLE_TIMEOUT=<int>
BACKPRESSURE_MAX_RATE=<int>  # 0 = отключить rate limit
BACKPRESSURE_GRACE_PERIOD=<int>
```

### Дефолты по окружениям

Дефолтные значения и различия по окружениям задаются в `server/server/config/unified_config.py`.

Окружение определяется через `NEXY_ENV` (dev/stage/prod).

## Коды ошибок

### Stream Limit Exceeded

**Код:** `RESOURCE_EXHAUSTED`  
**Тип:** `stream_limit_exceeded`  
**Сообщение:** "Maximum concurrent streams limit reached (<value>)"  
**Действие клиента:** Retry с backoff (см. клиентскую политику повторов)

### Rate Limit Exceeded

**Код:** `RESOURCE_EXHAUSTED`  
**Тип:** `rate_limit_exceeded`  
**Сообщение:** "Message rate limit exceeded (<value> messages/second)"  
**Действие клиента:** Retry с backoff (см. клиентскую политику повторов)

### Idle Timeout

**Код:** `DEADLINE_EXCEEDED`  
**Тип:** `stream_idle_timeout`  
**Сообщение:** "Stream closed due to idle timeout (<value> seconds)"  
**Действие клиента:** Открыть новый стрим

## Логирование

Все события backpressure логируются в структурированном формате:

```
ts=... level=INFO scope=grpc method=StreamAudio decision=stream_acquired ctx={"stream_id": "...", "active_streams": <value>, "max_streams": <value>}
ts=... level=WARNING scope=grpc method=StreamAudio decision=stream_idle_timeout ctx={"stream_id": "...", "idle_time_seconds": <value>}
ts=... level=ERROR scope=grpc method=StreamAudio decision=error ctx={"error_type": "stream_limit_exceeded", "error_code": "RESOURCE_EXHAUSTED"}
```

## Мониторинг

### Проверка активных стримов

```bash
grep -E 'decision=stream_acquired|decision=stream_released' server.log | tail -100 | grep -oE 'active_streams=[0-9]+' | cut -d= -f2 | sort -n | tail -1
```

### Проверка отказов

```bash
grep -c 'error_type=stream_limit_exceeded\|error_type=rate_limit_exceeded' server.log
```

### Проверка idle timeout

```bash
grep -c 'decision=stream_idle_timeout' server.log
```

## Настройка для разных нагрузок

- Повышайте `max_concurrent_streams` при росте параллельных запросов.
- Увеличивайте `idle_timeout_seconds` для длинных TTS ответов.
- Уменьшайте `max_message_rate_per_second`, если нужна защита от “шторма” чанков.

### Длинные TTS ответы (рекомендуется для production)

Для длинных TTS ответов увеличьте `idle_timeout_seconds` и `text_processing.request_timeout`, а rate limit при необходимости отключите через `max_message_rate_per_second: 0`.

## Troubleshooting

### Проблема: Слишком много отказов stream_limit_exceeded

**Решение:**
1. Увеличить `max_concurrent_streams` в конфиге
2. Проверить клиентскую политику повторов (должна быть экспоненциальная задержка)
3. Добавить jitter в клиентские повторы

### Проблема: Слишком много idle timeout

**Решение:**
1. Увеличить `idle_timeout_seconds` для длинных TTS ответов (значение см. в unified_config.py)
2. Проверить клиентскую логику: клиенты должны отправлять keep-alive сообщения
3. Убедиться, что `request_timeout` в `text_processing` также увеличен (значение см. в unified_config.py)

### Проблема: Слишком много rate_limit_exceeded

**Решение:**
1. Увеличить `max_message_rate_per_second` (значение см. в unified_config.py)
2. **Отключить rate limit полностью:** установить `max_message_rate_per_second: 0` (для аудио стримов с высокой частотой чанков)
3. Проверить клиентскую логику: клиенты не должны отправлять сообщения слишком часто

**Отключение rate limit:**
```yaml
backpressure:
  max_message_rate_per_second: 0  # Отключает проверку частоты сообщений
```

Или через переменную окружения:
```bash
export BACKPRESSURE_MAX_RATE=0
```

## Ссылки

- `modules/grpc_service/core/backpressure.py` — реализация
- `config/unified_config.py` — конфигурация
- `Docs/ARCHITECTURE_OVERVIEW.md` — архитектура
