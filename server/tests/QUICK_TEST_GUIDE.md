# 🚀 Быстрое руководство по тестированию

## ⚡ Быстрый старт (1 команда)

```bash
# Запуск всех тестов автоматически
python server/scripts/run_all_tests.py
```

## 📋 Пошаговое тестирование

### 1. Unit тесты (2-3 минуты)
```bash
pytest server/tests/ -v
```

### 2. Smoke тесты (1-2 минуты)
```bash
# Production сервер
python server/scripts/grpc_smoke.py nexy-server.canadacentral.cloudapp.azure.com 443

# Локальный сервер
python server/scripts/grpc_smoke.py localhost 50051
```

### 3. Health checks (30 секунд)
```bash
python server/scripts/check_grpc_health.py nexy-server.canadacentral.cloudapp.azure.com 443
```

### 4. E2E тесты (3-5 минут)
```bash
python server/scripts/test_full_pipeline_e2e.py
```

## 🎯 Минимальный набор (перед деплоем)

```bash
# 1. Unit тесты
pytest server/tests/ -v

# 2. Smoke тест
python server/scripts/grpc_smoke.py nexy-server.canadacentral.cloudapp.azure.com 443

# 3. Health check
python server/scripts/check_grpc_health.py nexy-server.canadacentral.cloudapp.azure.com 443
```

## 📊 Полное тестирование

```bash
# Все тесты с детальным выводом
python server/scripts/run_all_tests.py --level all

# Только unit тесты
python server/scripts/run_all_tests.py --level unit

# Только smoke тесты
python server/scripts/run_all_tests.py --level smoke --host nexy-server.canadacentral.cloudapp.azure.com --port 443
```

## ✅ Ожидаемые результаты

### Unit тесты
```
✅ Все тесты должны пройти (PASSED)
❌ Если есть FAILED - исправить перед деплоем
```

### Smoke тесты
```
✅ Подключение к серверу установлено
✅ InterruptSession успешен
✅ StreamAudio успешен
```

### Health checks
```
✅ Health endpoint доступен: HTTP 200
✅ Status endpoint доступен: HTTP 200
✅ Версии согласованы
```

## 🔍 Дополнительная информация

Полная документация: `Docs/COMPREHENSIVE_TESTING_GUIDE.md`
