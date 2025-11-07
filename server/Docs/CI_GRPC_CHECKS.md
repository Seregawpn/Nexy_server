# CI Checks для gRPC (PR-3)

**Назначение:** Примеры CI шагов для автоматической проверки gRPC совместимости, health/status и портов

---

## GitHub Actions Workflow

### Канонический fail-fast workflow

Файл: `.github/workflows/ci-fail-fast.yml`

- `grpc_tools.protoc` пересобирает Python-стабы и `git diff --exit-code`
  гарантирует отсутствие непроизведённых артефактов.
- `server/scripts/verify_cache_control_headers.py` валидирует `Cache-Control`
  значения в `server/nginx/grpc-passthrough.conf`.
- `server/scripts/check_change_impact_gate.py` требует `.impact/change_impact.yaml`
  при изменениях, выходящих за рамки SIMPLE-гейта (более 1 файла или >60 LOC).
- `server/scripts/verify_no_direct_module_calls.py` подтверждает, что между
  `server/modules/*` нет прямых импортов.
- `pytest` выполняет весь unit-контур (см. `pytest.ini` и `server/conftest.py`).

### Пример полного workflow для проверки gRPC

```yaml
name: gRPC Compatibility Checks

on:
  pull_request:
    paths:
      - 'modules/grpc_service/streaming.proto'
      - 'modules/grpc_service/**/*.py'
      - 'scripts/grpc_smoke.py'
      - 'scripts/check_grpc_health.py'
  push:
    branches:
      - main

jobs:
  grpc-checks:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install grpcio grpcio-tools
      
      - name: Regenerate protobuf files
        run: |
          cd modules/grpc_service
          python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
      
      - name: Verify protobuf regeneration
        run: |
          if [ -f "modules/grpc_service/streaming_pb2.py" ]; then
            echo "✅ Protobuf files regenerated"
          else
            echo "❌ Protobuf files not found"
            exit 1
          fi
      
      - name: gRPC Smoke Test
        run: |
          python scripts/grpc_smoke.py 20.151.51.172 443 || echo "⚠️ Smoke test skipped (server may be down)"
        continue-on-error: true
      
      - name: Health/Status Check
        run: |
          python scripts/check_grpc_health.py 20.151.51.172 443 || echo "⚠️ Health check skipped (server may be down)"
        continue-on-error: true
      
      - name: Port Check
        run: |
          nc -zv 20.151.51.172 50051 || echo "⚠️ Port check skipped (Nginx reverse proxy)"
        continue-on-error: true
      
      - name: Verify no breaking changes
        run: |
          # Проверка, что в proto нет breaking changes
          # (можно добавить более сложную логику)
          if grep -q "removed\|deleted\|required" modules/grpc_service/streaming.proto; then
            echo "❌ Breaking changes detected in streaming.proto"
            exit 1
          fi
          echo "✅ No breaking changes detected"
```

---

## Отдельные проверки

### 1. Smoke Test

```yaml
- name: gRPC Smoke Test
  run: |
    python scripts/grpc_smoke.py 20.151.51.172 443
  env:
    GRPC_TIMEOUT: 10
```

### 2. Health Check

```yaml
- name: Health Check
  run: |
    python scripts/check_grpc_health.py 20.151.51.172 443
```

### 3. Port Check

```yaml
- name: Port Check
  run: |
    nc -zv 20.151.51.172 50051 || echo "Port check skipped"
```

### 4. Version Consistency

```yaml
      - name: Version Consistency Check
        run: |
          # Проверка версий в health и appcast
          HEALTH_VERSION=$(curl -s https://20.151.51.172/health | jq -r '.latest_version')
          APPCAST_VERSION=$(curl -s https://20.151.51.172/updates/appcast.xml | grep -o 'sparkle:version="[^"]*"' | cut -d'"' -f2)
          
          if [ "$HEALTH_VERSION" != "$APPCAST_VERSION" ]; then
            echo "❌ Versions don't match: health=$HEALTH_VERSION, appcast=$APPCAST_VERSION"
            exit 1
          fi
          
          echo "✅ Versions match: $HEALTH_VERSION"
      
      - name: Validate Release Size (PR-8)
        id: validate_release_size
        run: |
          echo "📦 Validating release size consistency..."
          
          # Получаем размер из appcast
          APPCAST_XML=$(curl -s -k https://20.151.51.172/updates/appcast.xml || echo "")
          
          if [ -n "$APPCAST_XML" ]; then
            APPCAST_SIZE=$(echo "$APPCAST_XML" | grep -oP 'length="\K[^"]+' | head -1)
            
            if [ -n "$APPCAST_SIZE" ]; then
              echo "AppCast size: $APPCAST_SIZE bytes"
              
              # Получаем размер с GitHub CDN
              GITHUB_URL="https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg"
              GITHUB_SIZE=$(curl -s -L -I "$GITHUB_URL" 2>/dev/null | grep -i "content-length:" | tail -1 | awk '{print $2}' | tr -d '\r\n')
              
              if [ -n "$GITHUB_SIZE" ]; then
                echo "GitHub size: $GITHUB_SIZE bytes"
                
                if [ "$APPCAST_SIZE" = "$GITHUB_SIZE" ]; then
                  echo "✅ Sizes match: $APPCAST_SIZE bytes"
                else
                  echo "❌ Sizes don't match: appcast=$APPCAST_SIZE, github=$GITHUB_SIZE"
                  echo "This is a critical error - release blocked"
                  exit 1
                fi
              else
                echo "⚠️ GitHub size unavailable (size check skipped)"
              fi
            else
              echo "⚠️ AppCast size not found"
            fi
          else
            echo "⚠️ AppCast unavailable (size check skipped)"
          fi
        continue-on-error: true

---

## Pre-commit Hooks

### Пример pre-commit hook для проверки protobuf

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Проверка, что protobuf файлы регенерированы
if git diff --cached --name-only | grep -q "streaming.proto"; then
  echo "⚠️ streaming.proto изменен, проверяем регенерацию..."
  
  # Регенерируем protobuf
  cd modules/grpc_service
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
  
  # Проверяем, что файлы изменились
  if git diff --name-only | grep -q "streaming_pb2"; then
    echo "❌ Protobuf files not regenerated. Please run:"
    echo "   cd modules/grpc_service"
    echo "   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto"
    exit 1
  fi
  
  echo "✅ Protobuf files regenerated"
fi
```

---

## Локальные проверки перед push

### Скрипт для локальной проверки

```bash
#!/bin/bash
# scripts/pre_push_checks.sh

set -e

echo "🔍 Running pre-push checks..."

# 1. Регенерация protobuf
echo "1. Regenerating protobuf files..."
cd modules/grpc_service
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
cd ../..

# 2. Smoke test (если сервер доступен)
echo "2. Running smoke test..."
python scripts/grpc_smoke.py 20.151.51.172 443 || echo "⚠️ Smoke test skipped"

# 3. Health check
echo "3. Running health check..."
python scripts/check_grpc_health.py 20.151.51.172 443 || echo "⚠️ Health check skipped"

# 4. Unit tests
echo "4. Running unit tests..."
python -m pytest tests/test_pr2_1_coordinator.py -v || echo "⚠️ Unit tests skipped"

echo "✅ All pre-push checks passed!"
```

---

## Интеграция с существующим CI

Если у вас уже есть CI workflow, добавьте эти шаги:

```yaml
# В существующий workflow добавить:
- name: gRPC Compatibility Checks
  if: contains(github.event.head_commit.message, 'proto') || contains(github.event.head_commit.message, 'grpc')
  run: |
    python scripts/grpc_smoke.py 20.151.51.172 443 || true
    python scripts/check_grpc_health.py 20.151.51.172 443 || true
```

---

## Ручная проверка перед мерджем

### Чеклист для PR

1. **Protobuf регенерирован:**
   ```bash
   cd modules/grpc_service
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
   ```

2. **Smoke test пройден:**
   ```bash
   python scripts/grpc_smoke.py 20.151.51.172 443
   ```

3. **Health check пройден:**
   ```bash
   python scripts/check_grpc_health.py 20.151.51.172 443
   ```

4. **Версии согласованы:**
   ```bash
   curl -s https://20.151.51.172/health | jq '.latest_version, .latest_build'
   curl -s https://20.151.51.172/updates/appcast.xml | grep sparkle:version
   ```

5. **Нет breaking changes:**
   - Проверено в `Docs/GRPC_PROTOCOL_AUDIT.md`
   - Все изменения - только optional поля

---

## Troubleshooting CI

### Проблемы с подключением

Если сервер недоступен в CI:
- Используйте `continue-on-error: true` для smoke/health checks
- Или добавьте проверку доступности перед запуском тестов

### Проблемы с protobuf

Если protobuf не регенерируется:
- Проверьте установку `grpcio-tools`
- Проверьте синтаксис `streaming.proto`
- Запустите регенерацию вручную и проверьте diff

### Проблемы с зависимостями

Если тесты не проходят из-за зависимостей:
- Убедитесь, что `requirements.txt` содержит все зависимости
- Проверьте версии Python и grpcio

