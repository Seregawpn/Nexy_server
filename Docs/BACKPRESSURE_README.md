# Backpressure Configuration Guide

## Обзор

Backpressure система защищает сервер от перегрузки, ограничивая количество одновременно открытых стримов и частоту сообщений.

## Конфигурация

### YAML конфигурация (`unified_config.yaml`)

```yaml
backpressure:
  max_concurrent_streams: 50      # Максимум одновременно открытых StreamAudio
  idle_timeout_seconds: 300       # Таймаут для неактивных стримов (5 минут)
  max_message_rate_per_second: 10 # Максимум сообщений в секунду на стрим
  grace_period_seconds: 30        # Период ожидания перед принудительным закрытием
```

### Переменные окружения

```bash
BACKPRESSURE_MAX_STREAMS=50
BACKPRESSURE_IDLE_TIMEOUT=300
BACKPRESSURE_MAX_RATE=10
BACKPRESSURE_GRACE_PERIOD=30
```

### Дефолтные значения по окружениям

| **Параметр** | **dev** | **stage** | **prod** |
|-------------|---------|-----------|----------|
| `max_concurrent_streams` | 10 | 25 | 50 |
| `idle_timeout_seconds` | 60 (1 мин) | 180 (3 мин) | 300 (5 мин) |
| `max_message_rate_per_second` | 5 | 8 | 10 |
| `grace_period_seconds` | 10 | 20 | 30 |

Окружение определяется через `NEXY_ENV` (dev/stage/prod).

## Коды ошибок

### Stream Limit Exceeded

**Код:** `RESOURCE_EXHAUSTED`  
**Тип:** `stream_limit_exceeded`  
**Сообщение:** "Maximum concurrent streams limit reached (50)"  
**Действие клиента:** Retry через 60 секунд, максимум 2 попытки

### Rate Limit Exceeded

**Код:** `RESOURCE_EXHAUSTED`  
**Тип:** `rate_limit_exceeded`  
**Сообщение:** "Message rate limit exceeded (10 messages/second)"  
**Действие клиента:** Retry через 10 секунд, максимум 3 попытки

### Idle Timeout

**Код:** `DEADLINE_EXCEEDED`  
**Тип:** `stream_idle_timeout`  
**Сообщение:** "Stream closed due to idle timeout (300 seconds)"  
**Действие клиента:** Открыть новый стрим

## Логирование

Все события backpressure логируются в структурированном формате:

```
ts=... level=INFO scope=grpc method=StreamAudio decision=stream_acquired ctx={"stream_id": "...", "active_streams": 5, "max_streams": 50}
ts=... level=WARNING scope=grpc method=StreamAudio decision=stream_idle_timeout ctx={"stream_id": "...", "idle_time_seconds": 300}
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

### Низкая нагрузка (< 10 пользователей)

```yaml
backpressure:
  max_concurrent_streams: 20
  idle_timeout_seconds: 600  # 10 минут
  max_message_rate_per_second: 5
```

### Средняя нагрузка (10-50 пользователей)

```yaml
backpressure:
  max_concurrent_streams: 50
  idle_timeout_seconds: 300  # 5 минут
  max_message_rate_per_second: 10
```

### Высокая нагрузка (> 50 пользователей)

```yaml
backpressure:
  max_concurrent_streams: 100
  idle_timeout_seconds: 180  # 3 минуты
  max_message_rate_per_second: 20
```

## Troubleshooting

### Проблема: Слишком много отказов stream_limit_exceeded

**Решение:**
1. Увеличить `max_concurrent_streams` в конфиге
2. Проверить клиентскую политику повторов (должна быть экспоненциальная задержка)
3. Добавить jitter в клиентские повторы

### Проблема: Слишком много idle timeout

**Решение:**
1. Увеличить `idle_timeout_seconds` (если клиенты действительно нуждаются в длительных стримах)
2. Проверить клиентскую логику: клиенты должны отправлять keep-alive сообщения

### Проблема: Слишком много rate_limit_exceeded

**Решение:**
1. Увеличить `max_message_rate_per_second`
2. Проверить клиентскую логику: клиенты не должны отправлять сообщения слишком часто

## Ссылки

- `modules/grpc_service/core/backpressure.py` — реализация
- `config/unified_config.py` — конфигурация
- `Docs/ARCHITECTURE_OVERVIEW.md` — архитектура

