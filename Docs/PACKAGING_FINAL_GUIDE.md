# Nexy Client — Packaging Final Guide

**Версия:** 1.0 (обновлено 2025-01-15)

> Это базовый и единственный источник инструкций по сборке `.app` + `.pkg`, подписи и нотарификации. Все чек-листы (`Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`, `.cursorrules §11.2`) обязаны ссылаться на этот файл и фиксировать фактические результаты.

**Связанные документы:**
- `Docs/PROJECT_REQUIREMENTS.md` — единый snapshot требований (REQ-016, REQ-017, REQ-018)
- `scripts/prepare_release.sh` — полная цепочка подготовки релиза (см. `.cursorrules` раздел 11.6)
- `scripts/validate_release_bundle.py` — проверка метаданных артефакта (см. `.cursorrules` раздел 11.7)
- `.cursorrules` — правила разработки и Packaging Regression Checklist (раздел 11.2)

---

## 1. Требования окружения
-	m macOS 13+
-	Python 3.11 (используем `venv` из репозитория)
-	Xcode Command Line Tools (`xcode-select --install`)
-	Developer ID Application / Installer сертификаты в keychain (CI или локально)
-	Доступ к Apple Developer аккаунту для notarization (`notarytool` JSON key)
-	Установленный `pyinstaller`, `pkgbuild`, `productbuild`, `notarytool`, `stapler`
-	FFmpeg упакован в `client/resources/ffmpeg/ffmpeg`

---

## 2. Сборка `.app` (PyInstaller)

**ВАЖНО:** Перед сборкой убедись, что выполнены все проверки из `scripts/prepare_release.sh` (pre-build gate, release suite). См. `.cursorrules` раздел 11.6.

1. Активируй виртуальное окружение (`source .venv/bin/activate`).
2. Выполни `./rebuild_from_scratch.sh` **или** вручную:
   ```bash
   cd client
   pyinstaller main.py \
     --name Nexy \
     --onefile --windowed \
     --add-data "resources:resources" \
     --icon assets/icons/AppIcon.icns \
     --paths .
   ```
3. Готовый `.app` появляется в `dist/Nexy.app`. Проверь, что:
   - В `Contents/Resources/` присутствует `ffmpeg`, assets, конфиги.
   - `Info.plist` содержит правильный `CFBundleIdentifier` (`com.nexy.assistant`).

---

## 3. Подготовка `.pkg`
1. Создай временный payload:
   ```bash
   mkdir -p build/pkgroot/Applications
   cp -R dist/Nexy.app build/pkgroot/Applications/
   ```
2. `pkgbuild` (component):
   ```bash
   pkgbuild \
     --root build/pkgroot \
     --identifier com.nexy.assistant \
     --version <SEMVER> \
     --install-location /Applications \
     --component-plist packaging/Component.plist \
     build/Nexy.component.pkg
   ```
3. `productbuild` (distribution):
   ```bash
   productbuild \
     --distribution packaging/Distribution.xml \
     --package-path build \
     --resources packaging/resources \
     dist/Nexy-<SEMVER>.pkg
   ```

---

## 4. Подпись
1. Подписываем `.app` (до pkgbuild):
   ```bash
   codesign --deep --force --options runtime \
     --entitlements packaging/entitlements.plist \
     --sign "Developer ID Application: <Team>" dist/Nexy.app
   ```
2. Подписываем `.pkg`:
   ```bash
   productsign --sign "Developer ID Installer: <Team>" \
     dist/Nexy-<SEMVER>.pkg dist/Nexy-<SEMVER>-signed.pkg
   mv dist/Nexy-<SEMVER>-signed.pkg dist/Nexy-<SEMVER>.pkg
   ```

---

## 5. Нотарификация и stapler
1. Отправка:
   ```bash
   xcrun notarytool submit dist/Nexy-<SEMVER>.pkg \
     --apple-id <apple-id> \
     --team-id <team> \
     --keychain-profile NexyNotary \
     --wait
   ```
2. После успеха:
   ```bash
   xcrun stapler staple dist/Nexy-<SEMVER>.pkg
   ```

---

## 6. Валидация релизного бандла

**ОБЯЗАТЕЛЬНО:** Перед загрузкой на сервер выполни валидацию метаданных:

```bash
# Валидация .app
python scripts/validate_release_bundle.py dist/Nexy.app

# Валидация .app и .pkg
python scripts/validate_release_bundle.py dist/Nexy.app dist/Nexy.pkg
```

Скрипт проверяет:
- Структуру .app (обязательные пути)
- Info.plist (валидность и обязательные ключи)
- VERSION_INFO.json (метаданные версии и требований)
- release_suite_report.json (отчёт Release Suite)
- Подпись кода и нотарификацию

См. `.cursorrules` раздел 11.7 для деталей.

---

## 7. Smoke-тесты после сборки
1. Запустить `.app` напрямую из `dist/`.
2. Выполнить `./cold_start_diagnostics.sh`.
3. Пройти сценарии из `Docs/PRE_PACKAGING_VERIFICATION.md` (tray quit handler, first-run, TAL).
4. Обновить `Docs/PACKAGING_READINESS_CHECKLIST.md` статусом (дата, тесты, логи).

---

## 8. Публикация / AppCast
1. Загрузить `.pkg` в staging Azure Storage или CDN (`nexy-stage`).
2. Обновить `appcast-stage.xml` (Sparkle) через `scripts/fire_manual_update.py`.
3. Мониторить telemetry ≥24 ч, затем перенести item в `appcast-prod.xml`.
4. Обновить `Docs/CURRENT_STATUS_REPORT.md` и `Docs/GLOBAL_DELIVERY_PLAN.md`.

---

## 9. Траблшутинг
- **Auto-termination после запуска:** см. `Docs/EXIT_HANDLER_ISSUE_ANALYSIS.md`, `Docs/TAL_TESTING_CHECKLIST.md`.
- **Permission restart issues:** см. `PERMISSIONS_REPORT.md`, `Docs/first_run_flow_spec.md`.
- **Ошибки notarization:** проверь права на Apple ID, корректность `--primary-bundle-id`, повтори `notarytool history --limit 5`.
- **Отсутствие ресурсов в `.app`:** убедись, что `--add-data` PyInstaller включает нужные каталоги; проверь `collect_all_resources()` в packaging hooks.

---

## 10. Чек-листы и отчёты
- **Перед упаковкой:** `Docs/PRE_PACKAGING_VERIFICATION.md`.
- **Резюме статуса:** `Docs/PACKAGING_READINESS_CHECKLIST.md`.
- **Process rules:** `.cursorrules §11.2 Packaging Regression Checklist`.

После каждого релиза **обязательно** обновите все три документа ссылками на реальные логи/версии.
