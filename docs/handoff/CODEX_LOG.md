# Codex recovery log (writer: Codex only)

ChatGPT: read this file to coordinate and prevent duplicate changes, but do not overwrite Codex updates. Write to `CHATGPT_LOG.md` instead.

## Before starting

1. Read repository-root `AGENTS.md`.
2. Read `CODEX_START_HERE.md` and `RECOVERY_INVENTORY.md`.
3. Inventory actual local Windows directories and Codex workspaces; their files are not directly available to this ChatGPT session.
4. Work on independent `codex/recover-<project>` branches and record exact commit/PR URLs here.
5. The owner wants **the latest version and three immediately prior distinct updates** per independent application, not all old prototypes.

## Progress entries

_No Codex actions are recorded yet. Append one entry per project as work is actually performed._

```text
UTC time:
Project/repository:
Source file paths and SHA-256:
Version order evidence:
GitHub branch:
Commit/PR URL:
Files uploaded:
Tests/verification:
Security/copyright/privacy review:
Remaining blockers:
Next operation:
```

## Completion checklist per project

- [ ] Distinct application classified and destination repository verified
- [ ] Latest source and up to three prior chronological revisions located
- [ ] SHA-256 deduplication performed and required assets/dependencies retained
- [ ] User-owned/public-safe source reviewed (no ROMs, private saves, credentials or third-party asset violations)
- [ ] GitHub upload verified with commit and file listing
- [ ] README, STATUS/PROJECT_INFO, ROADMAP, CHANGELOG and .gitignore committed
- [ ] Exact functionality/test status documented without overstating
- [ ] ChatGPT coordination handoff updated in this Codex-owned log
