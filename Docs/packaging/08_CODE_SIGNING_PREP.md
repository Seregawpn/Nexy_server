# Этап 3: Подготовка к code signing и notarization

**Дата:** 2025-10-09  
**Скрипт упаковки:** `packaging/build_final.sh`

---

## 1. Предварительные проверки

| Чек | Статус | Комментарий |
|-----|--------|-------------|
| Developer ID Application cert | ⚠️ | `security find-identity -v -p codesigning` в sandboxе → `0 valid identities` (нужно проверить на реальной машине). |
| Developer ID Installer cert | ⚠️ | Аналогично выше. |
| Notary profile | ⚠️ | `xcrun notarytool history --keychain-profile nexy-notary` необходимо выполнить локально. |
| Entitlements | ✅ | `packaging/entitlements.plist` — микрофон, камера, audio-in, network, file RW, JIT. |
| Info.plist | ⚠️ | `LSUIElement` сейчас `False` — для меню-бара нужно `True` перед финальной сборкой. |
| PyInstaller build | ✅ | `pyinstaller packaging/Nexy.spec --noconfirm --clean` проходит без ошибок. |
| Lock fallback | ✅ | InstanceManager при отказе TCC переключается на `/tmp/nexy/nexy.lock`. |

**Важно:** все проверки с сертификатами выполняются за пределами тюрем/CI. Если сертификатов нет в login.keychain — импортировать перед запуском `build_final.sh`.

---

## 2. Содержимое пакета

- `packaging/entitlements.plist` — готов к передаче в codesign (`--options runtime`).  
- `packaging/Nexy.spec` — указывает target_arch `arm64`, включает нужные datas и присваивает `bundle_identifier`.  
- BUNDLE `info_plist` содержит UsageDescription для Microphone, AppleEvents, Camera, ScreenCapture, Accessibility (перед релизом проставить `LSUIElement: true`, удалить `NSSystemAdministrationUsageDescription`, если не требуется).  
- `resources/audio/flac` (1.5.0 arm64) и `resources/ffmpeg/ffmpeg` — включены в datas.

---

## 3. Рекомендуемая последовательность

1. Убедиться, что нужные сертификаты видны системе:  
   `security find-identity -v -p codesigning` и `security find-identity -v -p basic | grep "Developer ID Installer"`.  
2. Проверить notary-профиль: `xcrun notarytool history --keychain-profile nexy-notary`.  
3. При необходимости обновить `LSUIElement` и UsageDescription в `packaging/Nexy.spec`.  
4. Запустить `./packaging/build_final.sh` (создаёт чистую копию, подписывает, отправляет на notarization, упаковывает в DMG).  
5. После stapler — протестировать `.app` и DMG (spctl, запуск без devtools).  
6. При проблемах с lock-файлом удалить `~/Library/Application Support/Nexy/nexy.lock` и повторить.

---

## 4. Результаты скрипта

`build_final.sh` выполняет:
- PyInstaller сборку → чистая копия → очистка extended attributes.
- Подпись всех Mach-O (предварительная без entitlements) + ffmpeg/SwitchAudioSource.
- Подпись главного бинари и бандла с `packaging/entitlements.plist`.
- `codesign --verify --deep --strict --verbose=2` и `spctl --assess` проверки.
- Нотаризация через `xcrun notarytool submit ... --wait`, stapler.
- Генерация DMG (`hdiutil create`, `codesign`, `spctl`).

Итоговые артефакты: 
- `/tmp/Nexy.app` — «чистая» версия для проверки.  
- `dist/Nexy.dmg` — готовый инсталляционный образ.  
- `dist/Nexy-app-for-notarization.zip` — архив, который отправлялся на нотаризацию.  
- `dist/manifest.json` — при необходимости формируется скриптом `generate_manifest.py`.

---

## 5. Оставшиеся действия перед подписью

- [ ] Проверить наличие сертификатов в login.keychain (вне sandbox).  
- [ ] Обновить `LSUIElement` → `true`, чтобы приложение работало как меню-бар.  
- [ ] Убедиться, что UsageDescription поля соответствуют актуальным функциям.  
- [ ] Прогнать финальный smoke-тест после notarization (старт, меню-бар, микрофон, скриншоты, клавиатура).  
- [ ] При необходимости обновить инструкцию/README для релиза.

При выполнении всех пунктов можно переходить к фактической подписи и публикации.

