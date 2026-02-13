# Analysis: docs sync with current runtime cleanup contracts

Дата: 2026-02-12
Ассистент: Codex
Тип: analysis

## Контекст
Запрошена синхронизация документации с текущей логикой после серии cleanup-изменений в runtime (quit/restart guards, playback pipeline, first-run V2 ownership).

## Что обновлено

1. `Docs/ARCHITECTURE_OVERVIEW.md`
- Актуализированы контракты `permission_restart_integration`:
  - подписка на `app.shutdown`;
  - отмена scheduled restart на shutdown;
  - повторный guard `USER_QUIT_INTENT` перед `trigger_restart()`.
- Актуализированы контракты `speech_playback_integration`:
  - реальные подписки (`playback.raw_audio`, `playback.signal`, `grpc.request_cancel`, `playback.cancelled`, `voice.mic_closed`);
  - публикация `playback.ready`;
  - единый ingress `_queue_session_audio`, gRPC start confirm/reassert, mic-closed recovery.
- Исправлены диаграммы:
  - `mode.request(SLEEPING)` после playback теперь от `ProcessingWorkflow`;
  - interrupt-flow через `InterruptManagementIntegration` (а не прямой путь через SpeechPlayback);
  - в схеме централизации mode-request owner обновлен узел на `ProcessingWorkflow`.

2. `Docs/FLOW_INTERACTION_SPEC.md`
- Обновлены payload-контракты playback-событий (`session_id` optional, `signal` для `playback.started`).
- Для `permissions.first_run_restart_pending` добавлен режим совместимости и V2-owner примечание.
- Расширен контракт `app.shutdown` (optional `source`, `user_initiated`) и добавлен контракт `tray.quit_clicked`.
- Переписаны 4.2/4.3 под фактический V2 owner path:
  - Source of Truth = ledger, а не флаги;
  - single post-trigger probe вместо polling-loop;
  - shutdown cancel + pre-trigger `USER_QUIT_INTENT` guard.
- Обновлен welcome-flow: единый `session_id` для `mode.request(PROCESSING)` и playback path.
- Добавлен `4.11 User Quit Flow` с single-flight и owner-path shutdown.

3. `Docs/first_run_flow_spec.md`
- Добавлен runtime ownership note: при `permissions_v2.enabled=true` owner restart-cycle = V2 orchestrator/ledger.
- Обновлен раздел completion/restart:
  - `permissions.first_run_restart_pending` как legacy compatibility signal;
  - явные runtime guards (cancel on shutdown, pre-trigger quit guard).

4. `Docs/STATE_CATALOG.md`
- Исправлен раздел `session_id`:
  - удалено устаревшее утверждение, что локальные session-поля полностью удалены;
  - зафиксировано текущее правило: локальные runtime-cache допустимы только для anti-race/diagnostics, SoT остается `ApplicationStateManager`.

## Результат
Документация приведена к текущему runtime-контракту по ключевым зонам, где были обнаружены архитектурные рассинхроны: first-run/restart ownership, quit/shutdown path, playback/interrupt ownership, session_id policy.
