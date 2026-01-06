# PKG AppleDouble Fix Review

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-01-02

## Запрос/цель
Проверить корректность изменений в упаковке PKG (AppleDouble/xattr cleanup) и их соответствие текущим документам.

## Контекст
- Файлы: packaging/build_final.sh
- Документы: Docs/PACKAGING_FINAL_GUIDE.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без реархитектуры; один источник истины для упаковки

## Решения/выводы
Статус: НЕ СООТВЕТСТВУЕТ

## Найденные проблемы (если review)
- Несоответствие SoT: в Docs/PACKAGING_FINAL_GUIDE.md:7.1 требуется копирование через ditto без --noextattr для сохранения печати, а в packaging/build_final.sh используется --noextattr и агрессивный xattr wipe. Риск потери шага notarization/staple и нарушение REQ-015.
- Валидация xattrs по строкам `xattr -lr` не отражает реальное наличие xattrs на файлах и допускает их сохранение (warn-only), что противоречит цели «0 xattrs» для устранения AppleDouble.
- Удален post-fix `clean_appledouble_from_pkg` без гарантии отсутствия xattrs/._*; отсутствует резервный механизм при регрессии.
- Дублирование очистки (clean_xattrs + дополнительный xattr -cr/find -exec xattr -c) нарушает принцип централизованной логики.

## Открытые вопросы
- Нужно ли официально изменить Docs/PACKAGING_FINAL_GUIDE.md под новый подход (если подтверждено, что stapled ticket не зависит от xattrs)?

## Следующие шаги
- Либо вернуть поведение скрипта к Docs/PACKAGING_FINAL_GUIDE.md, либо обновить документ и сделать zero-xattr policy единым правилом.
- Упростить очистку до одного владельца (clean_xattrs) и сделать строгую валидацию (fail on any xattr/._*).
