# Analysis: macOS Gatekeeper notarization status

## Context
Проверен текущий статус подписи/нотаризации клиентского приложения и release-пайплайна.

## Findings
- Release flow присутствует и централизован:
  - `scripts/release_build.sh` запускает `packaging/build_final.sh` в режиме `release`.
  - В `release` включены timestamp + notarization.
- В `packaging/build_final.sh` реализованы:
  - подпись `codesign` (hardened runtime);
  - notarization через `xcrun notarytool submit`;
  - stapling через `xcrun stapler staple`;
  - финальные валидации `codesign --verify` и `xcrun stapler validate`.
- Фактическая локальная проверка артефакта:
  - `codesign --verify --deep --strict dist/Nexy.app` → exit code 0;
  - `xcrun stapler validate dist/Nexy.app` → `The validate action worked!`.

## Conclusion
На текущем окружении подпись и notarization для `dist/Nexy.app` настроены и проходят. Gatekeeper-предупреждение у конечного пользователя вероятнее всего связано не с этим артефактом/потоком (например, установка из другого билда/канала дистрибуции).

## Verification
- Прочитаны скрипты:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/release_build.sh`
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/packaging/build_final.sh`
- Выполнены команды:
  - `codesign --verify --deep --strict dist/Nexy.app`
  - `xcrun stapler validate dist/Nexy.app`

## Информация об изменениях
- Что изменено:
  - Добавлен отчет с результатом проверки статуса подписи/нотаризации.
- Список файлов:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/assistant_exchange/codex/2026-02-17__analysis__macos-gatekeeper-notarization-status.md`
- Причина/цель изменений:
  - Зафиксировать факт наличия и работоспособности release signing/notarization flow.
- Проверка (что выполнено для валидации):
  - Чтение release/packaging скриптов;
  - Локальная валидация codesign/stapler текущего `dist/Nexy.app`.
