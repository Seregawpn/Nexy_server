# MCP order & audio contract audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
В MCP‑цепочке нет явного контракта порядка доставки ActionMessage относительно text/audio. В аудио‑контракте остаётся риск рассинхронизации между codec (pcm/mp3) и gRPC dtype при использовании legacy env `AUDIO_FORMAT`.

## Root Cause
MCP сообщение отправляется внутри основного цикла StreamAudio на уровне item‑ов, что делает порядок зависимым от последовательности генерации. AudioConfig теперь разделяет codec/dtype, но legacy окружения с `AUDIO_FORMAT=pcm` могут повлиять на dtype.

## Optimal Fix
Задокументировать порядок MCP сообщений (например: text/audio → ActionMessage, либо ActionMessage → text/audio) и зафиксировать его в gRPC. Для аудио — явное использование `AUDIO_CODEC` + лог предупреждения при `AUDIO_FORMAT` не совпадающем с dtype.

## Verification
Проверить на одном ответе с command+text, что порядок сообщений соответствует контракту. Проверить значения `audio.format` (dtype) и `audio.audio_format` (codec) в логах.

## Запрос/цель
Аудит порядка MCP и аудио‑контракта без изменений.

## Контекст
- Файлы: `server/modules/grpc_service/core/grpc_server.py`, `server/config/unified_config.py`, `server/modules/audio_generation/config.py`, `server/modules/audio_generation/providers/edge_tts_provider.py`
- Документы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/PROJECT_REQUIREMENTS.md`, `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: аудит без правок

## Решения/выводы
- MCP ActionMessage сейчас может идти до/после text/audio — порядок не закреплён.
- Dtype/codec разделены, но legacy `AUDIO_FORMAT` может приводить к dtype=pcm, если переменная не обновлена.

## Открытые вопросы
- Нужен ли строгий порядок MCP сообщений для клиента?
- Нужно ли жёстко валидировать `AUDIO_FORMAT` как dtype и предупреждать о значениях `pcm/mp3`?

## Следующие шаги
- Утвердить порядок MCP сообщений и закрепить в коде/доках.
- Добавить предупреждение при неверном dtype в конфиге.
