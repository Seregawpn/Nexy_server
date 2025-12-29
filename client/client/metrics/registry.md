# Metrics Registry

**Цель**: Единый реестр всех метрик Nexy с их семантикой и порогами SLO.

## Обязательные метрики (Decision Logs)

| Метрика | Тип | Семантика | Порог SLO (p95) | Gateway | Источник |
|---------|-----|-----------|-----------------|---------|----------|
| `decision_rate{type}` | counter | Распределение решений (start/abort/retry/degrade) по типам | N/A | Все gateways | `integration/core/gateways.py` |
| `decision_latency_ms` | histogram | Задержка принятия решения | ≤10ms | Все gateways | `integration/core/gateways.py` |

## TCC/Permission Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `tcc_prompt_duration_ms` | histogram | Длительность последовательности разрешений (от первого запроса до завершения) | ≤5 сек | `first_run_permissions_integration.py` |
| `permission_flow_success` | rate | Процент успешных завершений потока разрешений (без критических ошибок) | ≥99% | События `permissions.first_run_completed` vs `permissions.first_run_failed` |
| `permission_restart_success_rate` | rate | Процент успешных автоматических перезапусков после предоставления разрешений | ≥98% | `permission_restart_integration.py` |
| `permission_restart_latency_ms` | histogram | Задержка перезапуска (от `permission_restart.scheduled` до готовности нового процесса) | ≤15 сек | `permission_restart_integration.py` |

## Audio/Processing Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `start_listening_latency_ms` | histogram | Задержка запуска listening режима | ≤600ms | `listening_workflow.py` |
| `stream_open_success_rate` | rate | Доля удачных запусков аудио | ≥98% | `voice_recognition_integration.py` |

## Network Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `network_online_ratio` | rate | Процент времени онлайн | ≥95% | `network_manager.py` |
| `grpc_request_latency_ms` | histogram | Задержка gRPC запросов | ≤1000ms | `grpc_client_integration.py` |

## Mode Transition Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `mode_transition_latency_ms` | histogram | Задержка перехода между режимами (SLEEPING → LISTENING → PROCESSING) | ≤100ms | `mode_management_integration.py` |

## Правила добавления метрик

1. **Обязательная метрика** добавляется в этот реестр
2. **SLO порог** указывается для всех критичных метрик
3. **Источник** указывает модуль/интеграцию, генерирующую метрику
4. **Тип метрики**: counter, gauge, histogram, rate
5. **Семантика**: краткое описание что измеряется

## Проверка SLO в CI

Все метрики с SLO порогами проверяются в `tests/perf/test_slo.py` (см. раздел 20 `.cursorrules`).


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

## Power/Battery Metrics

| Метрика | Тип | Семантика | Порог SLO (p95) | Источник |
|---------|-----|-----------|-----------------|----------|
| `idle_cpu_pct` | gauge | Процент использования CPU в idle-режиме (после полной инициализации) | ≤5% | Системные метрики (psutil) |
| `idle_ram_mb` | gauge | Потребление RAM в idle-режиме (после полной инициализации) | ≤200 MB | Системные метрики (psutil) |
| `tal_hold_duration_ms` | histogram | Длительность TAL (Termination and Launch) assertion (от установки до освобождения) | ≤120 сек | `SimpleModuleCoordinator._hold_tal_until_tray_ready()` |
| `tal_refresh_interval_ms` | histogram | Интервал обновления TAL assertion | ~30 сек (target), ≤35 сек (допустимо) | `SimpleModuleCoordinator._periodically_refresh_tal_hold()` |
| `power_assertion_active_count` | gauge | Количество активных power assertions (вне TAL-окна) | 0 (в idle-режиме) | `pmset -g assertions` |
