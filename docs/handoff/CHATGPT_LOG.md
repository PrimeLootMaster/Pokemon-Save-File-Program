# ChatGPT recovery log (writer: ChatGPT only)

This file is the **durable continuation point** for future ChatGPT conversations. Codex: read but do not overwrite; write your updates to `CODEX_LOG.md`.

## 2026-10-10 — coordination bootstrap

**Repository:** `PrimeLootMaster/Pokemon-Save-File-Program` on `main`.

Actions verified committed:
- `AGENTS.md`: shared agent instructions, commit `95b8d5fbdac1444a25bf007cec44870904f44cce`.
- `docs/handoff/CODEX_START_HERE.md`: Codex-specific tasks, commit `c0cdfeebc91b962c6ccdfac6615cc1a7685962d1`.
- `docs/handoff/RECOVERY_INVENTORY.md`: source filenames, boundaries and safety concerns, commit `924c0f4610b301ffcf7b4dff2441484e170068e6`.

**Verified sources in ChatGPT Library:** Pokémon v24–v28 files, frozen v35 reference archive (103 ZIP entries), Xenogears HTML + ZIP, Sentinel v1/v2/RC1 ZIPs, Organizer v1/v1.1 ZIPs, Gandalf phone app HTML variants and grimoire HTML, D&D battlemap v1/v2 HTML, dark-mode God & Reality reader HTML. Exact names in `RECOVERY_INVENTORY.md`.

**GitHub constraints:** Only two owned/accessible repositories returned: `Pokemon-Save-File-Program` (user's existing minimal inspection scaffold) and `single-click-copy` (unresolved provenance). Available GitHub connector supports source updates but not **creating new repositories**. Codex has been asked to handle repo creation if authorized.

**Important archive evidence:** `PokemonProgram-FROZEN-REFERENCE-ARCHIVE.zip` says v35 is historical reference only; build a new Whole Tree, don't promote archived candidates uncritically. Its sixteen branches are *parallel branch candidates*, not sixteen version updates.

**Current publication state:** Coordination docs are being committed here. The main recovered source ZIPs and original HTML versions have NOT been confirmed uploaded to GitHub as part of this handoff. Treat all as **located, not uploaded**.

## Next operations for ChatGPT on resumed conversation

1. Read root `AGENTS.md`, `RECOVERY_INVENTORY.md` and **both agent logs** freshly from GitHub. Review new branches/PRs/repositories created by Codex before taking ownership of work.
2. Reconcile Codex discoveries to source provenance and update inventory *through an isolated branch/PR* to avoid racing with Codex.
3. Compare hashes and latest versions within each project, then prepare *only publicly safe* extracted source and explanatory docs. Do not push bundled ROMs, saves, private manuscript or copyrighted visuals.
4. Verify specific GitHub commit SHA and repository file presence before marking `uploaded`. Don't overwrite Codex changes.
5. Repeat source discovery (ChatGPT Library + other relevant accessible archives) for remaining projects as user continues the workflow.

## Standard per-entry format

```
UTC time:
Project:
Source filename/location:
SHA-256:
Classification/version order:
Repo + branch + commit/PR:
Verification performed:
Open risks/blockers:
Next action:
```

**Do not infer that this file grants asynchronous execution.** Future ChatGPT instances should read it when the user resumes the task.

## 2026-10-10 — independent v35 integrity audit (ChatGPT branch)

**Working branch:** `chatgpt/catalog-v35-evidence`. No direct modifications to the minimal save-inspector source on `main`.

**Source artifact:** `PokemonProgram-FROZEN-REFERENCE-ARCHIVE.zip` (40,423,130 bytes). SHA-256: `743c56403d64c9850a87a6fe5c2061711cce4aa147ec2c6b72235111cf60cec3`. Zip member count: 103.

**Verified:** Computed SHA-256 from bytes of each of 16 `01_MODERN_V35_REFERENCE/*.html` files and matched each against archived `PokemonSaveFileHacks-v35-Verification.json`; **16/16 match**. Archived `ok:true` Chrome/test statuses are historical and were NOT independently replayed. All 16 HTML candidates contain `data:image/` assets; public redistribution rights remain unverified. No source HTML from v35 has been pushed.

**New code:** `tools/audit_frozen_reference.py` (read-only ZIP metadata/hashes) and `tests/test_audit_frozen_reference.py` (three synthetic tests). Locally executed `python -m unittest discover -s tests -p 'test_audit_frozen_reference.py' -v`, 3 passing. Executed script against original archived ZIP with zero reported issues; the archived browser-feature tests were not rerun.

**New documentation:** `docs/recovery/POKEMON_V35_EVIDENCE.md`, complete v35 SHA-256 table and publishing guardrails.

**Next:** Submit PR to `main` for this non-conflicting tooling/doc contribution. Codex should focus on recovering the actual app source and identifying newest+three true chronological snapshots; no one should treat the 16 parallel v35 candidates as time-ordered versions.

## 2026-10-10 — Sentinel and Organizer source package deduplication

**Source:** five Sentinel ZIP names and two Organizer ZIPs independently recovered from ChatGPT Library and inspected locally. All six distinct `security_monitor.py` / `organizer.py` source instances passed Python `ast.parse`; plus RC1 `telemetry_acceptance_test.py` passed. **No Windows runtime tests performed.**

**Result:** `SentinelLocal_v2_final.zip` is exactly identical to `SentinelLocal_v2.zip` (archive SHA-256 match); `SentinelLocal_RC1.zip` and `SentinelLocal_v2_1.zip` contain identical `security_monitor.py` but RC1 adds a telemetry acceptance test and runner, so they are *distinct package updates*. Retain RC1, v2.1, v2, v1. Organizer currently has only v1.1 and v1, both distinct.

**Documentation committed:** `docs/recovery/SENTINEL_ORGANIZER_ARCHIVE_EVIDENCE.md` with ZIP hashes, inner source hashes, exact ZIP member paths, privacy warnings, status and Codex next operations. Original source not uploaded because dedicated repositories are not yet available through this connector.

**Safety note:** Sentinel RC1 README mentions a user-specific prior malware detection; original logs and README must be assessed before public upload. Organizer is a tool that actually moves files and must only be tested with expendable fixtures, not live user data.

## 2026-10-10 — Codex PR assistance and Xenogears package verification

**Concurrent Codex activity detected:** `codex/recover-pokemon-library-beta` exists. Its `docs/handoff/CODEX_LOG.md` records 4 distinct beta snapshots and test evidence. Codex's CLI reported authorization denied on PR creation, so ChatGPT opened a **draft, unmerged** review PR: `https://github.com/PrimeLootMaster/Pokemon-Save-File-Program/pull/2`. ChatGPT has not edited the Codex branch or certified its browser claims; preserve Codex's file ownership.

**Xenogears recovered source:** Original `Xenogears_DuckStation_Save_Editor.html` has SHA-256 `0d616a652815ca7c04dd9b1085a8cb158428453273ce6861d27212af15680551`; packaged `index.html` has the **same bytes**. Original bundle includes a `.sav` file, excluded from public release. The trimmed project ZIP includes 2 Node structural tests: independently executed under Node v22.16.0, both passed. The application links an external `fzstd@0.1.1` script; fully offline behavior not certified.

**Documentation committed:** `docs/recovery/XENOGEARS_EDITOR_EVIDENCE.md` with source/package fingerprints, precise members, dependency note, 2/2 test evidence and Codex repo-creation instructions. No Xenogears source was uploaded to the temporary Pokémon repository.

**Remaining:** dedicated Xenogears repo missing; full DuckStation state behavior not validated; other applications pending. The ChatGPT evidence PR is `https://github.com/PrimeLootMaster/Pokemon-Save-File-Program/pull/1` and remains unmerged.
