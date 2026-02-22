# Analysis: first-run latency and Full Disk Access visibility

## Context
Investigated `client/log.md` for slow first run and missing Nexy in Full Disk Access UI.

## Findings
- Startup itself is fast; latency is dominated by chained TCC permission flow.
- From first launch to FDA update: ~2m11s (`00:00:11` -> `00:02:22`).
- Multiple services are requested in one first-run session (mic, screen, contacts, apple events, listen/post event, accessibility, full disk), producing long interactive flow.
- Full Disk Access entry was actually created for bundle `com.nexy.assistant`.

## Key evidence
- Launch starts: `log.md:11` (`com.nexy.assistant` launch)
- Mic prompt: `log.md:192` (`kTCCServiceMicrophone`)
- Screen capture modify: `log.md:315`, `log.md:322`
- Contacts prompt: `log.md:381`
- ListenEvent modify: `log.md:545`, `log.md:549`
- PostEvent modify: `log.md:584`, `log.md:588`
- Accessibility modify: `log.md:603`
- Full Disk Access modify: `log.md:655`
- Security pane loaded FDA entry: `log.md:658` (`kTCCServiceSystemPolicyAllFiles com.nexy.assistant full`)

## Conclusion
- “Very long” is caused by over-serialized first-run permissions workflow, not packaging/notarization or launch failure.
- “Nexy missing in Full Disk list” is not confirmed by logs; TCC registered FDA entry. Most likely UI refresh/race during settings transition/restart.

## Verification
- Confirmed explicit `kTCCServiceSystemPolicyAllFiles` modify + SecurityPrivacyExtension “new entry”.
- Confirmed app relaunch around FDA stage (`log.md:666+`).

## Информация об изменениях
- Изменения не вносились.
- Список файлов: отсутствует.
- Причина/цель изменений: анализ причин задержки и видимости Full Disk Access.
- Проверка: выполнен разбор таймлайна `log.md` и сопоставление событий TCC.
