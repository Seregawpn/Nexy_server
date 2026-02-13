# Task Brief: Single Version Source and Parallel Beta Release

## Goal
- Сделать `VERSION` единственным источником версии.
- Настроить единый деплой: GitHub release + параллельный push версии на Azure.
- Убрать хардкод `1.0.1` из рабочих скриптов.

## Changes
- Updated: `server/scripts/update_server_version.sh`
  - Если версия не передана аргументом, берется из корневого `VERSION`.
  - Дефолт `1.0.1` удален.

- Rewritten: `server/scripts/deploy.sh`
  - Поддержка каналов: `stable` и `beta`.
  - По умолчанию читает версию из `VERSION`.
  - Запускает `update_server_version.sh` параллельно с публикацией GitHub release.
  - После публикации обновляет удаленный `manifest.json` и `manifest_<version>.json`.
  - Выполняет финальные проверки `/updates/health` и `/updates/appcast.xml`.

## Why version was 1.0.1
- В старом `deploy.sh` и ряде legacy-скриптов версия была хардкодом.
- Это обходило единый source of truth (`VERSION` / `SERVER_VERSION`).

## Operational Notes
- Stable tag format: `v<version>`
- Beta tag format: `beta-v<version>` + prerelease flag
- Manifest update writes both:
  - `updates/manifests/manifest.json`
  - `updates/manifests/manifest_<version>.json`

