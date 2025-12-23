#!/bin/bash
# Добавление метрик в registry.md

set -e

REGISTRY_FILE="client/metrics/registry.md"

# Проверяем, что файл существует
if [ ! -f "$REGISTRY_FILE" ]; then
    echo "❌ Файл $REGISTRY_FILE не найден"
    exit 1
fi

# Проверяем, что метрики еще не добавлены
if grep -q "Audio Route Manager Metrics" "$REGISTRY_FILE"; then
    echo "⚠️ Метрики уже добавлены в $REGISTRY_FILE"
    exit 0
fi

# Добавляем в конец файла
cat >> "$REGISTRY_FILE" << 'EOF'

## Audio Route Manager Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `device_discovery_latency_ms{source}` | histogram | Задержка обнаружения устройства (event/polling) | event: 0ms, polling: ≤2000ms | `AVFoundationDeviceMonitor` |
| `input_switch_duration_ms{transport}` | histogram | Длительность переключения input устройства | Bluetooth: ≤1200ms, USB: ≤800ms, Built-in: ≤600ms | `AudioRouteManager` |
| `output_recreate_duration_ms` | histogram | Длительность пересоздания output | ≤600ms (target), ≤900ms (допустимо) | `AVFoundationAudioPlayback` |
| `mapping_confidence_distribution` | histogram | Распределение confidence маппинга | HIGH ≥80%, MEDIUM ≥15%, LOW ≤5% | `DeviceMapper` |
| `reconcile_duration_ms` | histogram | Длительность reconcile операций | ≤50ms | `AudioRouteManager` |
| `reconcile_pending_count` | gauge | Количество pending reconcile | ≤1 | `AudioRouteManager` |
| `active_device_signatures{transport}` | gauge | Активные устройства по типу транспорта | N/A | `AudioRouteManager` |
| `route_manager_decision_rate{type}` | counter | Распределение решений RouteManager (start/abort/retry/degrade) | N/A | `AudioRouteManager` |
EOF

echo "✅ Метрики добавлены в $REGISTRY_FILE"

