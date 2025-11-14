# Nexy Client — Global Delivery Plan

**Версия:** 0.9 (черновик обновлён 2025-01-15)  
**Владелец:** Release/Delivery (Tech Lead клиента)  
**Назначение:** единый план вывода настольного клиента Nexy на dev/beta/prod окружения, включая упаковку, подпись, распространение и Azure/AppCast интеграцию.

---

## 1. Цели и критерии готовности

| Цель | Метрика/критерий | Источник проверки |
|------|------------------|-------------------|
| Надёжный first-run/permission restart | TAL hold ≥120 с, нет auto-termination до `tray.ready` | `Docs/TAL_TESTING_CHECKLIST.md`, логи `log.md` |
| Предсказуемая упаковка/нотаризация | PyInstaller → pkgbuild/productbuild → notarization проходят без ручных шагов | `Docs/PACKAGING_FINAL_GUIDE.md`, `Docs/PRE_PACKAGING_VERIFICATION.md` |
| Отсутствие регрессий в критических модулях | `scripts/test_critical_paths.py`, `scripts/test_tray_termination.py`, `scripts/test_tal_assertion.py` green | `Docs/CRITICAL_PATHS_TEST_REPORT.md`, CI |
| Telemetry/metrics готовы | `client/metrics/registry.md` заполнен, `tests/perf/test_slo.py` green | CI logs |
| Rollback within 30 min | Kill-switch и дистрибуция через AppCast позволяют остановить rollout | `Docs/FEATURE_FLAGS.md`, AppCast config |

---

## 2. Фазы поставки

| Фаза | Цель | Длительность | Гейты |
|------|------|--------------|-------|
| **Dev (internal)** | Быстрый цикл, CLI запуск, ffmpeg из `resources/` | непрерывно | Lint + unit + schema + manual smoke |
| **Beta (signed .app)** | Тестирование PyInstaller `.app` + PKG на внутреннем ring | ≤ 2 недели | Packaging Regression Checklist, notarization dry-run, TAL checklist |
| **RC / Staged rollout** | Раскатка на 10‑25 % Azure VM / AppCast каналов | 1 неделя | AppCast staging feed, telemetry OK, no critical bugs 48 ч |
| **GA** | 100 % пользователей, публичный канал | — | RC success + Ops sign-off |

---

## 3. Технический пайплайн

1. **Сборка:** `rebuild_from_scratch.sh` (PyInstaller) → артефакт в `dist/Nexy.app`.
2. **PKG:** следуем `Docs/PACKAGING_FINAL_GUIDE.md` (pkgbuild + productbuild).
3. **Подпись:** Developer ID Application / Installer (certs в CI keychain).
4. **Нотарификация:** `xcrun notarytool submit ... --wait`, stapler на `.pkg`.
5. **Smoke:** `cold_start_diagnostics.sh`, manual run из `dist/`.
6. **Публикация:**  
   - `.pkg` грузится в защищённый Azure Storage / CDN.  
   - `appcast.xml` обновляется новым `<item>` (версия, подпись, SHA256).  
   - Sparkle (или кастомный апдейтер) указывает на staging feed до GA.
7. **Telemetry hook:** после публикации следим за `client/metrics/registry.md` метриками: `permission_flow_success`, `start_listening_p95`, `stream_open_success_rate`.

---

## 4. Azure / AppCast инфраструктура

| Объект | Назначение | Примечания |
|--------|-----------|------------|
| Azure Storage (prod) | Хранение `.pkg` | Версии именуем `Nexy-<semver>.pkg`; доступ только CI и release-боту. |
| Azure Storage (staging) | Beta/RC пакеты | Используем отдельный контейнер `nexy-stage`. |
| AppCast feed | Sparkle совместимый XML | Ведём два feed'а: `appcast-stage.xml`, `appcast-prod.xml`. Update/push выполняем скриптом `scripts/fire_manual_update.py`. |
| Telemetry dashboard | Проверка SLO | Сбор логов через `scripts/monitor_tray_metrics.sh` + централизованная таблица. |

---

## 5. Контрольные точки перед rollout

1. **Code complete** — все PR прошли `.cursorrules` гейты, `change_impact.yaml` загружен.
2. **Docs updated** — `Docs/CURRENT_STATUS_REPORT.md`, `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md` ссылаются на актуальные логи.
3. **Feature flags** — `Docs/FEATURE_FLAGS.md` содержит запись о включаемых фичах + kill-switch.
4. **Security/permissions** — `PERMISSIONS_REPORT.md` обновлён, TCC/TAL тесты выполнены.
5. **AppCast staging** — новая версия провалидирована через staging feed (минимум 24 ч мониторинга).
6. **Release Go/No-Go** — встреча с Ops (Azure) и Support:
   - Логи `log.md`, `rebuild_logs/` без ошибок.  
   - Метрики + user journey smoke (push-to-talk, tray, restart).

---

## 6. Роллаут и откат

1. **Rollout**  
   - Publish в `appcast-stage.xml`.  
   - Мониторинг telemetry + логов (scripts `monitor_tray_metrics.sh`, `parse_tray_metrics.py`).  
   - При отсутствии критических алертов → копируем item в `appcast-prod.xml`.

2. **Откат**  
   - Удаляем/отключаем item в feed.  
   - Активируем kill-switch (`FEATURE_FLAGS.md` / `unified_config.yaml`).  
   - При необходимости выкладываем hotfix `.pkg` с тем же процессом (быстрая ветка `hotfix/<issue>`).

---

## 7. Communication & Owners

| Направление | Owner | Контакты |
|-------------|-------|----------|
| Packaging / notarization | Release eng | release@nexy |
| Permissions / TAL | Permissions SWAT | permissions@nexy |
| Updater / AppCast | Infrastructure | infra@nexy |
| Support comms | PM / Support lead | support@nexy |

---

## 8. Артефакты

- Packaging инструкции — `Docs/PACKAGING_FINAL_GUIDE.md`, модульные `modules/*/MACOS_PACKAGING_GUIDE.md`.
- Checklists — `Docs/PRE_PACKAGING_VERIFICATION.md`, `Docs/PACKAGING_READINESS_CHECKLIST.md`, `.cursorrules §11.2`.
- Status/health — `Docs/CURRENT_STATUS_REPORT.md`, `Docs/TAL_TESTING_CHECKLIST.md`, `PERMISSIONS_REPORT.md`.

---

**Примечание:** документ — «один источник истины» по поставке. Любые изменения пайплайна, окружений или гейтов отражаем здесь и синхронизируем с `.cursorrules` (раздел 1.1).
