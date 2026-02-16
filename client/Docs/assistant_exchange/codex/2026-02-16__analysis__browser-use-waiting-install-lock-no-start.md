# Analysis: browser_use waits on install lock and does not start

## Context
Пользовательский сценарий: команда `browser_use` приходит, но визуально "ничего не происходит".

## Log Facts
- Для сессии `3632cd6c-c1a1-41b8-a00f-1712de4cbbbb`:
  - действие дошло до `browser.use.request` и `Process called`.
  - далее: `Waiting for install lock...` (без последующего `Acquired install lock` для этой сессии).
  - нет `browser.started`, `browser.failed`, `BROWSER_TASK_FAILED` для этой сессии.
- Ранее в этом же запуске уже были процессы установки Chromium (`playwright install chromium`, `Installing browser (downloading)...`).
- Приложение было закрыто пользователем (`tray quit`) до появления terminal-события browser-задачи.

## Diagnosis
Задача browser-use зависает в очереди на install lock, пока идет/зависает другая установка Chromium; до реального старта браузерного таска выполнение не доходит.

## Architecture Note
- Owner установки корректный (`BrowserUseModule`, single-flight lock), но отсутствует таймаут/промежуточный user-visible прогресс при долгом ожидании lock.
- Дополнительно в логе есть несогласованность телеметрии: `ProcessingWorkflow ... browser=True` при `ModeManagement ... browser=False`.
