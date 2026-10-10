# Recovery inventory (evidence-led)

**Inventory date:** 2026-10-10 UTC. **Status:** discovery and classification, **not** proof of upload or execution. Primary source: files physically listed in the user's ChatGPT Library and archived ZIP member lists. Codex/Windows workspaces are not directly accessible to this ChatGPT session. Consult `AGENTS.md` for the four-version rule, safety and responsibilities.

## Existing connected GitHub repositories

- `PrimeLootMaster/Pokemon-Save-File-Program` (`main`): minimal browser inspection scaffold, core JS, tests, ROADMAP, PROJECT_INFO, README. **Not the complete recovered editor.** This repo is currently the temporary recovery coordination hub.
- `PrimeLootMaster/single-click-copy` (`master`): existing repo, authorship/license not established for this workflow. **Do not modify**.
- Connected GitHub tooling in this ChatGPT session **does not expose repository creation**; Codex should create missing independent repos if its authorized environment supports it.

## A — Pokémon Save Editor / Save Workspace (one project)

**Source evidence in ChatGPT Library:**

- `PokemonProgram-FROZEN-REFERENCE-ARCHIVE.zip` — 40,423,130 bytes, retrieved from Library. **103 ZIP entries**. Freeze stamp in archive's README: `2026-10-04T15:36:24.769092+00:00`.
  - `FROZEN_REFERENCE_POLICY.md` — explicitly says v35 is a **reference only**, not the next base.
  - `00_START_HERE/00_READ_ME_FIRST.md` — says next build is fresh Whole Tree attempt, not v36.
  - `01_MODERN_V35_REFERENCE/PokemonSaveFileHacks-v35-ProgramManifest.json` — `build: v35-audited-fixed-family`, `trunk: v31-flare-new-trunk`, `status: APPROVAL CANDIDATES`, `branch_count: 16`, `history_through: CHANGE-090`.
  - `PokemonSaveFileHacks-v35-Branches-1-16-Audited-Fixed-Pack.zip`, `PokemonSaveFileHacks-v35-Verification.json`, `PokemonSaveFileHacks-v35-Audit-Report.md`, `PokemonSaveFileHacks-v35-SHA256.txt`.
  - v35 branch candidates cover Party, Boxes, Creation, Strengthening, Inventory, Story, Perfectdex, Battle Lab, Leaderboard, Save Manager, Game Database, Raw Hex Viewer, Save Structure, Diagnostics, Companion, Save Converter. **Branches are parallel candidates and must not be counted as 16 time-ordered versions.**
  - Historical v28–v34 builds, screenshots and audit/build scripts are inside the ZIP. Enumerate and checksum members before choosing four snapshots; do not upload the whole archive blindly.
- `PokemonSaveFileHacks-v28-Full-Tree-Approval-Candidate-v3-site-ready-pretest.html` — 1,066,143 bytes.
- `PokemonSaveFileHacks-v28-Full-Tree-Approval-Candidate-v3-live-search-fixed.html` — 937,172 bytes (a `(1)` duplicate also exists).
- `PokemonSaveFileHacks-v28-Full-Tree-Approval-Candidate-v3-1.html` — 758,636 bytes.
- `PokemonSaveFileHacks-v27-Hardened-Tree-1.html` — 619,046 bytes.
- `PokemonSaveFileHacks-v27-Clean-Clone-Alpha.html` — 72,116 bytes.
- `PokemonSaveFileHacks-v27-Closed-Beta-3-Unrestricted-Test.html`, `...-Current-3A.html`, `...-Current-3-Audit.html`, `...-Current-2.html` (duplicate `(1)`), `...-Current.html`, `...-Rare-Candy-Gate.html`.
- `PokemonSaveFileHacks-v27-Closed-Beta-2.html`, `PokemonSaveFileHacks-v27-Closed-Beta-1.html`, `closed_beta_phase1_results.json`.
- `PokemonSaveFileHacks-v26.8.html` (duplicate `(1)`, both 589,741 bytes), `v26.7.html`, `v26.6.html`, `v26.5.html`, `v26 (3).html`.
- `PokemonSaveFileHacks-v25.2.html`, `v25.1.html`, `v25.html`, `v24-BW.html` (several `(1)` duplicates).
- `PokemonSaveFileHacks-recovered.zip` — ChatGPT-generated smaller recovery package.
- `Pokemon_Save_File_Hacks_Recovery_2026-09-30T06-27-16-578Z.psehstate` — **potentially user-specific recovery state; do not publish**.
- Multiple `.sav`, `.gba`, `.ups` files in Library — **do not publish**.

**Classification:** All `PokemonSaveFileHacks-*.html` inspected to date are part of the save-file editing/workspace lineage. Their version numbers and distinct SHA hashes are evidence, but not a complete chronological dependency graph. The archived v35 files are reference candidates and must not replace the current main branch silently.

**Destination:** `PrimeLootMaster/Pokemon-Save-File-Program`, after reconciling source and expected next architecture. **Status: scaffold on GitHub; recovered program files not verified uploaded.**

## B — Separate Pokémon button-clicking website

**Source filename not yet found.** The owner explicitly states this is an independent app, not a revision of the save editor. Codex: find actual source in local/Codex sessions, inspect behavior, assign an independent repository; do not re-label a save-editor tab as this app.

**Status: project confirmed, file missing.**

## C — Separate Pokémon browser game website

**Source filename not yet found.** Owner describes a game inside a website, with playable world, Pokémon-style buildings and interactive overworld. Codex: locate actual code, dependencies and assets; independently classify it from the click-only website and save editor. Avoid copyrighted sprite or ROM publication without authorization.

**Status: project confirmed, file missing.**

## D — Xenogears / DuckStation Save Editor

- `Xenogears_DuckStation_Save_Editor.html` — 19,030 bytes.
- `Xenogears_Save_Editor_Bundle.zip` — 1,836,566 bytes.
- `Xenogears-DuckStation-Save-Editor.zip` — 9,652 bytes (recent ChatGPT project packaging).
- `Xenogears_DuckStation_uncompressed_base.sav`, `Xenogearssavefile.sav`, `Xenogears.zip` — fixtures/game content **not approved for public GitHub**.

**Status:** source recovered in Library; needs source inspection / version matching and separate repo; exclude save games and game ZIP.

## E — Sentinel Local security monitor (independent project)

- `SentinelLocal_RC1.zip` — 9,027 bytes.
- `SentinelLocal_v2_1.zip` — 6,911 bytes.
- `SentinelLocal_v2_final.zip`, `SentinelLocal_v2.zip` — 6,759 bytes each; need hash-based duplicate check.
- `SentinelLocal_v1.zip` — 6,189 bytes.

**Status:** multiple iterations recovered; chronology and exact scripts inside ZIP must be compared. Suggested separate `Sentinel-Local` repository. Do not upload machine-specific logs/secrets.

## F — Organizer Local (independent project)

- `OrganizerLocal_v1_1.zip` — 4,534 bytes.
- `OrganizerLocal_v1.zip` — 4,151 bytes.

**Status:** two iterations recovered; separate repo. **Collector Local** is a related but independent project mentioned in conversations; no distinct source ZIP listed yet; find in Codex/Windows. Do not conflate Organizer and Collector without source evidence.

## G — Gandalf phone assistant and mobile grimoire

**Gandalf Phone App** variants (same app lineage):
- `Gandalf_Phone_App_MidSession.html` — 93,902 bytes.
- `Gandalf_Phone_App_Emergent.html` — 87,317 bytes.
- `Gandalf_Phone_App_Rimuru_Intel_Brain.html` — 69,748 bytes.
- `Gandalf_Phone_App_Rimuru_Intel.html` — 61,215 bytes.
- `Gandalf_Phone_App.html` — 29,672 bytes.

**Gandalf tap grimoire**:
- `Gandalf_Grimoire_Tap_Book_v2.html` — 28,090 bytes.
- Related `Gandalf_Grimoire_Level_9.pdf` and character sheets exist (reference/outputs, not app versions).

**Status:** HTML source recovered. Inspect whether grimoire is a separate product or an interface/component of the phone app before deciding repo boundary. Keep at most four updates for each confirmed app.

## H — Interactive D&D Battlemap

- `dnd_battlemap_v2.html` — 27,167 bytes.
- `dnd_battlemap_v1.html` — 20,757 bytes.
- Related original map artwork includes `Druidic Grove Forest Battle Map.png`, `Enchanted Forest Adventure Map.png`, `Enchanted Forest Crossroads Map.png`, `Mossy Forest Clearing Battle Map.png` and Harbor-series artwork.

**Status:** two browser app revisions recovered. Preserve original asset attribution; avoid indiscriminate upload of unrelated map variations.

## I — God & Reality Reader

- `God_and_Reality_Reading_Book_Dark.html` — 7,086,386 bytes.
- `God_and_Reality_Current_Manuscript.zip` — 58,420,354 bytes; current manuscript docs/PDFs and editorial plan are in a separate Library folder.

**Status:** reader HTML found. The book/manuscript is a separate *content* artifact, not necessarily a software app. **Do not automatically publish private manuscript text to public GitHub.** Inspect whether HTML embeds full private manuscript; keep source in private staging or await approval for publication.

## J — Other known or referenced projects

- **Micro-Coach**: previously produced as an iPhone Python console; exact source filename not found in Library listing. Codex/Windows lookup required.
- **AION**: discontinued historically; do not reactivate or publish personal-memory data.
- **Pokémon Unbound cheat collections**: `PokemonUnboundLimitless_Evolution_Families_Clean_Final.cheats`, `PokemonUnboundLimitless_Full_Honorable_Eevee_Final.cheats`, `PokemonUnbound_2.1.1.1_mGBA_Master_FINAL.cheats` and related `.cheats` variants. Separate cheat-reference collection if licensed; no game ROMs or saves.
- **single-click-copy**: pre-existing GitHub repository, not an archival destination until provenance is established.
- Other applications may exist only in Codex workspaces or Windows directories. Continue discovering; do not assume this inventory is exhaustive.

## Operational status key

- `located` = file name/bytes located in an accessible source.
- `classified` = independently assigned to the correct app by code/feature evidence.
- `versioned` = latest plus up to 3 distinct predecessors chosen with substantiated order.
- `reviewed` = checked for publishability, source rights, secrets and private data.
- `uploaded` = GitHub commit URL exists and actual expected files confirmed.
- `documented` = README/STATUS/CHANGELOG/ROADMAP reflect implementation.
- `complete` = all prior stages satisfy project-specific completion criteria; **not** equivalent to finished app.

Update source facts as discovered; do not mark `uploaded` on the strength of a local ZIP or a plan alone.
