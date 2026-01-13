# nginx grpc 400

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-005

## Diagnosis
Nginx принимает HTTP/2 preface как обычный HTTP-запрос и отвечает 400, потому что gRPC-модуль отсутствует.

## Root Cause
Nginx собран без ngx_http_grpc_module → директива grpc_pass неактивна → gRPC preface обрабатывается как HTTP/1.x → 400 на "PRI * HTTP/2.0".

## Optimal Fix
Поддержка gRPC в Nginx через пакет с grpc-модулем или пересборку Nginx с ngx_http_grpc_module; точка правды — конфигурация ingress/reverse proxy.

## Verification
Проверить nginx -V на наличие grpc, валидировать успешный TLS + HTTP/2 upgrade и отсутствие 400 на preface; gRPC запросы доходят до сервера.

## Запрос/цель
Объяснить, что означает отсутствие grpc-модуля в Nginx и дать оптимальный путь исправления.

## Контекст
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md
- Документы: /Users/sergiyzasorin/Fix_new/Docs/CODEX_PROMPT.md
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ANTIGRAVITY_PROMPT.md

## Решения/выводы
- Корневая причина — сборка Nginx без ngx_http_grpc_module.
- Исправление должно происходить в инфраструктурном слое (reverse proxy).

## Открытые вопросы
- Какая ОС/репозиторий пакетов используется для Nginx (для выбора пакета с grpc)?
- Где хранится инфраструктурная конфигурация (IaC/Ansible/Compose)?

## Следующие шаги
- Установить nginx с grpc-модулем или пересобрать, затем повторно проверить gRPC preface.
