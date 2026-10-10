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

## 2026-10-10T05:56:01.247901+00:00 — Pokémon Library beta recovery

Project/repository: Pokémon save workspace, `PrimeLootMaster/Pokemon-Save-File-Program`.

Classification: recovered standalone save editor beta; relationship to v35 unverified. Existing inspector source and ChatGPT-owned documentation preserved.

GitHub branch: `codex/recover-pokemon-library-beta`. Upload and PR confirmation are recorded after the actual operation; preparation is not an upload claim.

Source evidence:

- `/workspace/Pokemon-Save-File-Program/Pokemon-Save-File-Library-BETA.html` — 3544157 bytes; SHA-256 `9e33e770c5edfbd50d1751993737a33ed15d336bbd5911838eb52b13fb718c66`. Current session revision including entry fixes. Published transformation hash `23deaf7c3d69f40e810fea31cbbe1f81247015294b0b8d772b435765932efb1c`.
- `/workspace/Pokemon-Save-File-Program/Pokemon-Save-File-Library-BETA-pixel.html` — 3541015 bytes; SHA-256 `7914d4830e89dd18a0ac6d50d4ea755e6d720f9a2780f1c73789462136a67918`. Earlier session revision; redrawn/refined aliases have the same bytes. Published transformation hash `b11e397f8e13aac7f7e945186b8256d512a7cf01ed3af78057a5e021a6e5d2bd`.
- `/workspace/attachments/597df15b-13ea-45e0-8674-9ad0be6415be/Pokemon-Save-File-Library-BETA.html` — 3616589 bytes; SHA-256 `3185d9763046e35b2bfbd128f966ee0a3179611c0ec1f00227b0e3bbfd959105`. User upload preceding session edits; source creation timestamp unverified. Published transformation hash `85dfecb5f5e58d87534fa64946b3faf26155e36d9a142d3bea92464987ce6891`.

Three distinct snapshots retained; pixel/redrawn/refined inputs are byte-identical. No fourth predecessor located. Embedded raster images replaced with blank placeholders for publication pending redistribution permission. Unmodified inputs preserved locally. No saves, ROMs, credentials or unvetted archives included. Code origin is the user-uploaded older-model artifact plus this session’s edits; no third-party license invented.

Files prepared: `recovered/pokemon-library-beta/` source, two prior versions, build/browser checks, provenance, README, STATUS, ROADMAP, CHANGELOG, AGENTS and release review.

Verification: existing inspector Node tests 5/5 passed; recovered browser and entry check results recorded below after completion.

Blockers: no real saves/emulator certification; unresolved artwork permission; provisional Unbound PP and section 4 checksum. API authentication currently fails; Git read succeeds.

Verification completed: recovered copy passes 17 route renders, 36 synthetic adapter routes, edit/transfer integration, backup checks, and 10 actual pointer/touch/reduced-motion/canvas-failure entry checks across standalone and static build. No uncaught browser errors. Existing inspector: 5/5 Node tests.

GitHub upload confirmed: branch `codex/recover-pokemon-library-beta`, recovery commit `0ca55f3` (remote SHA verified with `git ls-remote`). Source: https://github.com/PrimeLootMaster/Pokemon-Save-File-Program/tree/codex/recover-pokemon-library-beta/recovered/pokemon-library-beta . PR creation attempted with gh; GitHub GraphQL returned Forbidden. No PR was created and main was not modified. Manual PR creation: https://github.com/PrimeLootMaster/Pokemon-Save-File-Program/pull/new/codex/recover-pokemon-library-beta . Next operation: resolve API authentication or create the PR through GitHub; review source and asset restrictions before merging.
