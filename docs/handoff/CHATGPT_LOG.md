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
