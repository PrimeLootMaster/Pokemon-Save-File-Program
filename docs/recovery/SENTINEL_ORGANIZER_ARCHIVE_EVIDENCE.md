# Sentinel Local and Organizer Local — recovered source evidence

> **Read-only inventory and static parsing, 2026-10-10.** These are two distinct Windows/Python applications, not versions of the Pokémon Save Editor. This document resides temporarily in the shared coordination repository until Codex creates their own GitHub repositories.

## Sentinel Local — four retained release/package snapshots

| Chronological candidate (newest first) | ZIP SHA-256 | `security_monitor.py` SHA-256 | Other important content |
|---|---|---|---|
| `SentinelLocal_RC1.zip` | `043df4a7e0df1080801c327d8a71907e6e4d05692455ce3137c4a8abe35c85f4` | `a6e6d45eaa6dae1384fc9ef20a8c7954c68743b353f2e33dbc7ee6efc63f5e2e` | `telemetry_acceptance_test.py`, `RUN_ACCEPTANCE_TEST.bat`, `README_RC1.txt`, `README.txt`, `RUN_SENTINEL.bat` |
| `SentinelLocal_v2_1.zip` | `109b56ee1d6f15773bd7e4a88dcaaab48b787ad245bb741639e7a9f9e1f00a1c` | `a6e6d45eaa6dae1384fc9ef20a8c7954c68743b353f2e33dbc7ee6efc63f5e2e` | `RUN_SENTINEL.bat`, `README.txt` |
| `SentinelLocal_v2.zip` | `e144927d56511d965f7c50f39b2bac8cf60be718e1548cfc9ce259e46be98eb5` | `9eee98bdd4bd9cd44ab25352ceffcace13ff63d7e468b2d930468a5352fd6eb1` | `RUN_SENTINEL.bat`, `README.txt` |
| `SentinelLocal_v1.zip` | `0b48441c55bbc1f990dac2f9018bd95e79139fd4401be5239054c2fdadfbf299` | `e21231bc08d335ff2f025d3b39187d033de41ad69435a06e4d9201e5d230a8fb` | `RUN_SENTINEL.bat`, `README.txt` |

**Duplicate:** `SentinelLocal_v2_final.zip` is byte-identical to `SentinelLocal_v2.zip` (same ZIP SHA-256). Do not count it as an update or publish it separately.

**Nuance:** The v2.1 and RC1 `security_monitor.py` modules are byte-identical. RC1 is nevertheless a distinct **package update** because it adds a telemetry acceptance test, a launcher for that test and RC1 documentation. Its README says it is a *read-only* Windows security monitoring release candidate, not a verified clean-PC guarantee. The acceptance test should report sensor health; **running a successful user interface is not evidence that telemetry is working**.

The module uses PowerShell/Defender event queries and writes local state/report files under `%LOCALAPPDATA%\SentinelLocal`. **Do not include any real Defender detection logs, state/report JSON, computer usernames or individual system paths in a public source repository.** RC1's `README_RC1.txt` mentions a particular real-world detection as a validation example; consider replacing that with a generic description in public docs while preserving the original privately.

**Static check:** `ast.parse` accepted `security_monitor.py` from v1, v2, v2.1 and RC1, and the RC1 acceptance-test script. This does **not** demonstrate that Windows Defender collection or administrator execution succeeds on an actual machine.

## Organizer Local — two retained snapshots

| Candidate (newest first) | ZIP SHA-256 | `organizer.py` SHA-256 | Core source size |
|---|---|---|---:|
| `OrganizerLocal_v1_1.zip` | `f7ee21cf6c71672488e0ea97e6307a2811db54b317393b9572e5389b9a09470b` | `d874a9c8f0a55c616a434f1598f67ea436267b9e41eb7916fcb92309e32837f8` | 10,060 bytes |
| `OrganizerLocal_v1.zip` | `8fbf804de6f843eafc5d9be558d69606a961e920ff930e28ecbeb39a2249548e` | `9ef869ff716c3eddbcb62f1eae3a7cd18ca45e271fcae53c4fd8167156758d63` | 7,494 bytes |

Both ZIPs also contain `RUN_ORGANIZER.bat` and `README.txt`.

**Classification:** Organizer categorizes existing Windows files and lets the user review/choose moves. v1.1 README specifically adds click-to-select, category filtering, check/uncheck/invert controls and selected-count feedback; v1 records moves and offers reversal. Unlike Sentinel, **Organizer intentionally moves user files** when `Organize Checked` is activated. Do not run acceptance tests against real directories without a controlled test fixture and backups.

**Static check:** Both source versions passed Python `ast.parse`; Windows file-move behavior, symlink handling, and undo correctness remain untested here. Default target is `%USERPROFILE%\Organized`; journal is under `%LOCALAPPDATA%\OrganizerLocal`.

## GitHub publication and collaboration

- **Suggested dedicated repositories:** `PrimeLootMaster/Sentinel-Local` and `PrimeLootMaster/Organizer-Local`. Codex should create them if its GitHub interface permits; ChatGPT's connected GitHub actions cannot create repositories.
- **No original source ZIP has been published by this report.** Existing bundles reside in the user's ChatGPT Library. The SHA-256 fingerprints let the agents reconcile copies found on Windows or in Codex without guessing.
- **Retention rule:** Sentinel: RC1, v2.1, v2, v1 (four package revisions, one redundant ZIP removed). Organizer: v1.1, v1 (only two known source revisions). Avoid manufacturing nonexistent older versions.
- **Production state:** both unfinished/unverified; do not call either production-ready from successful static syntax parsing alone.
- **Next:** Codex should extract source, inspect for secrets and privacy, test with contained fixtures/Windows telemetry, and upload to their own repositories. Record commit/PR links in `docs/handoff/CODEX_LOG.md`.

## Source paths inside the original ZIPs

```
SentinelLocal_RC1/security_monitor.py
SentinelLocal_RC1/telemetry_acceptance_test.py
SentinelLocal_RC1/RUN_ACCEPTANCE_TEST.bat
SentinelLocal_RC1/RUN_SENTINEL.bat
SentinelLocal_RC1/README_RC1.txt
SentinelLocal_RC1/README.txt
SentinelLocal_v2_1/security_monitor.py
SentinelLocal_v2/security_monitor.py
SentinelLocal/security_monitor.py

OrganizerLocal_v1_1/organizer.py
OrganizerLocal_v1_1/RUN_ORGANIZER.bat
OrganizerLocal_v1_1/README.txt
OrganizerLocal_v1/organizer.py
OrganizerLocal_v1/RUN_ORGANIZER.bat
OrganizerLocal_v1/README.txt
```

**Unrelated project:** Collector Local is not bundled in either package. Do not fold it into Organizer merely because their workflows are adjacent.
