# AGENTS.md — Shared instructions for ChatGPT and Codex

> This repository currently serves two purposes: the **Pokémon Save File Program** prototype and a **temporary portfolio-recovery coordination hub**. These instructions apply to both agents until a dedicated coordination repository exists.

## Mission

Recover and organize the owner's unfinished projects from ChatGPT Library, prior ChatGPT artifacts, local Windows files, Codex workspaces, and the connected GitHub account. Publish authentic, recoverable **project source**, one independent application per repository, with accurate README/STATUS/ROADMAP/CHANGELOG documentation. **Preservation, classification, traceability, and honest status come before new feature development.** Do not pretend unfinished software is finished.

## Non-negotiable rules

1. **Newest plus three prior updates** per independent project (at most four distinct chronological snapshots). Do not count byte-identical duplicates twice. Do not fabricate absent history. If a version is itself a multi-file application, preserve all files required for that snapshot to work. Git's normal commit history is not a substitute for documenting the four retained snapshots.
2. **Separate products stay separate**. In particular, Pokémon **save-file editor/workspace**, Pokémon **button-clicking website**, and Pokémon **playable game-in-a-browser website** are three distinct applications unless actual source evidence proves otherwise. Do not confuse interface tabs/branches with independent projects or versions.
3. **Copy/preserve first; make surgical edits only as needed.** Hash original inputs; preserve filenames, source, and attribution. Do not overwrite existing work with a new scaffold simply because the scaffold is simpler.
4. **Verify provenance, state, and permissions**. Do not publish ROMs, game assets without permission, user-specific save games, credentials, tokens, personal/private data, or large unvetted archives to public GitHub. Audit archive members before publishing. Do not claim another author's work as original; establish third-party licenses.
5. **No unverified claims**. Distinguish: source located, source inspected, syntax tested, behavior tested, uploaded, and working. Preserve failed/rejected experiments as evidence outside the four-version publication window when needed locally, rather than uploading every discarded attempt.
6. **Do not rewrite the Pokémon v35 frozen archive into the production codebase.** Its own `FROZEN_REFERENCE_POLICY.md` declares v35 **reference only**, and calls for a fresh Whole Tree architecture. v35 has sixteen parallel branch candidates, *not* sixteen chronological updates or independent browser games. Read the archive's `00_START_HERE/00_READ_ME_FIRST.md` before adopting code.
7. **Never force-push or overwrite the default branch.** Use short-lived working branches; compare upstream before committing; open pull requests for merges where feasible; preserve existing user-created work.
8. **No destructive changes to `PrimeLootMaster/single-click-copy`**. Its provenance/ownership and license are not established for this archiving workflow.

## Work split to avoid collisions

- **Codex / Windows owner:** enumerate local PC and Codex workspace files; recover full source directories, manifests, dependencies and true chronological versions; create missing per-project repositories if access permits; upload source on `codex/recover-<project>` branches; document execution/test results; create PRs. **Codex owns code migrations and code branches.**
- **ChatGPT / Library owner:** enumerate ChatGPT Library and accessible conversation artifacts; inspect source archives and record real filenames/checksums/provenance; maintain the project classification, inventory, documentation and cross-project tracking. **ChatGPT owns coordination documentation and `chatgpt/catalog-<project>` branches.**
- Both may investigate the same project **read-only**, but do not edit each other's working files or branch. To transfer discoveries, update only your own log and cite precise paths/SHAs. If another agent has already done an upload, verify before duplicating.
- **Writer-owned logs:** ChatGPT edits `docs/handoff/CHATGPT_LOG.md`; Codex edits `docs/handoff/CODEX_LOG.md`. Agents should *read* both. Coordinate shared inventory changes through a PR or a careful single-writer handoff.

## Required per-project GitHub contents

- `README.md`: what it is, exact status, features (confirmed vs planned), how to run, dependencies, known limitations, independent affiliation disclaimer where applicable.
- `PROJECT_INFO.md` or `STATUS.md`: original filename/source location, hash, classification, compatibility, state, blockers.
- `ROADMAP.md` / `docs/ROADMAP.md`: remaining work with checkboxes and evidence.
- `CHANGELOG.md`: version lineage and rationale for retaining the latest four distinct updates.
- `src/` or the original executable root, plus `versions/` with up to three previous snapshots when applicable. **Never delete required source modules solely to meet an arbitrary four-file count**.
- Appropriate `.gitignore` preventing local saves, ROMs, temporary binaries, user data, credentials and outputs from publication.
- `LICENSE` only after ownership/licensing is resolved. Do not invent a license for third-party code.
- Copy/adapt a project-local `AGENTS.md` so the instructions persist after moving out of this temporary coordination repository.

## Minimal evidence record for every recovery

`project | source system | exact file/path | file size | SHA-256 | version/date evidence | duplicates? | classification | destination repo | commit/PR | tested? | public-safe? | next step`

Use **UTC timestamps** for actions; timestamp of retrieval is not proof of source-version chronology. Include code references where possible. If missing, write `unverified`, not an inference presented as fact.

## Concurrent Git workflow

1. Before writes, `git fetch --all` / check current remote HEAD, `git status`, and existing remote branches and PRs.
2. Work in `codex/recover-<slug>` or `chatgpt/catalog-<slug>` (or uniquely suffixed variant); avoid unrelated changes. Never rebase or reset somebody else's branch.
3. Commit small, descriptive changes; do not overwrite same paths edited by another active agent. If a merge conflict arises, stop that path, record it in the owned log, and reconcile by reviewing both sides.
4. Create a PR and report repo, branch, PR URL, commit SHA, file hashes, verification and outstanding issues. Do not mark complete before GitHub confirms the upload.
5. Run `git diff --check`, relevant tests, and re-open GitHub artifacts when possible; explain anything not tested.

## Starting references

- See `docs/handoff/CODEX_START_HERE.md` for immediate tasks and project boundaries.
- See `docs/handoff/RECOVERY_INVENTORY.md` for evidence-backed filenames and current access limits.
- See `docs/handoff/CHATGPT_LOG.md` and `docs/handoff/CODEX_LOG.md` to avoid repeating already-completed work.

**Completion condition:** every recoverable project is classified; each approved/publishable project's latest source plus up to three actual predecessors and accurate documentation are in the correct GitHub repository; unpublishable, missing, or third-party files are explicitly recorded as blockers; no project is silently skipped. This instruction does **not** authorize unattended work by ChatGPT outside active conversations.
