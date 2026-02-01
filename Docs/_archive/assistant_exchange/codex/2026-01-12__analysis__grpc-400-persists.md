# grpc 400 persists

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-12
- ID (INS-###): INS-005

## Diagnosis
400 на HTTP/2 preface сохраняется, значит Nginx не принимает gRPC как HTTP/2 TLS на текущем входе.

## Root Cause
Чаще всего это несоответствие TLS/ALPN и режима клиента: insecure_channel к 443 + HTTPS приводит к некорректному preface, либо upstream gRPC недоступен/не слушает на ожидаемом протоколе.

## Optimal Fix
Перейти на secure_channel и параллельно проверить прямую доступность backend на 127.0.0.1:50051 (grpcurl), чтобы исключить upstream проблему.

## Verification
secure_channel должен проходить и в логах Nginx не должно быть 400 на "PRI * HTTP/2.0"; grpcurl к backend возвращает список сервисов.

## Запрос/цель
Определить следующий шаг: secure_channel или прямой тест backend.

## Контекст
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ARCHITECTURE_OVERVIEW.md
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ASSISTANT_COORDINATION_PROTOCOL.md
- Документы: /Users/sergiyzasorin/Fix_new/Docs/CODEX_PROMPT.md
- Документы: /Users/sergiyzasorin/Fix_new/Docs/ANTIGRAVITY_PROMPT.md

## Решения/выводы
- Следующий минимально-дешевый шаг: secure_channel на 443.
- Вторая проверка — grpcurl к 127.0.0.1:50051 для исключения upstream.

## Открытые вопросы
- Есть ли TLS сертификат/ALPN h2 на 443 (Nginx)?
- Уверены ли мы, что backend слушает HTTP/2 gRPC на 50051?

## Следующие шаги
- Перевести клиента на secure_channel и повторить запрос.
- Выполнить grpcurl на backend.
