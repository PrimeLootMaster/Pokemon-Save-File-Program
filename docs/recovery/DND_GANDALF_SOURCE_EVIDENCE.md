# D&D browser utilities — Gandalf and interactive battlemap recovery

> Evidence from actual recovered ChatGPT Library HTML files (2026-10-10). Each file was inspected for its title, scripts and behavior markers; JavaScript was extracted and checked with `node --check`. No browser interaction or D&D rules validation was performed. These are **two or three independent apps**, not Pokémon applications.

## 1. Gandalf interactive phone field app

One continuous **phone-app version lineage** with five distinct recovered HTML source files. The four newest by ChatGPT Library creation history:

| Retain | Exact file | Size | SHA-256 |
|---|---|---:|---|
| Current recovered | `Gandalf_Phone_App_MidSession.html` | 93,902 | `7a3364ddd0f89550766e486d87f220e9ccb6fb542aa4468677d121bfa3211d3e` |
| Previous 1 | `Gandalf_Phone_App_Emergent.html` | 87,317 | `e4d63cb912bf5422b5f7747fe924c1dbf6e9c019b6edf5a535d3d9678ab9ecf6` |
| Previous 2 | `Gandalf_Phone_App_Rimuru_Intel_Brain.html` | 69,748 | `f6e9ecdfbee7f235ad9bfd5a3e04c632a4f038f9480d2a3120fe09aa38fa25f0` |
| Previous 3 | `Gandalf_Phone_App_Rimuru_Intel.html` | 61,215 | `5a8597287f56ff8b1ca22eba08f9306edcec079d7e3e7926f7b3e39ce83e3e9e` |

Fifth, older file **not selected for GitHub's four retained snapshots**: `Gandalf_Phone_App.html` (29,672 bytes), SHA-256 `28c18f95d42b3b605d0f2e3ca38b4092ae005a33e16a91ad9a40fcaa74826330`.

The phone app identifies itself as `Gandalf — D&D Field App` or `Gandalf — Interactive D&D Field App`. Its visible UI includes character/turn state, spell slots, quick actions, and later a “Gandalf Brain” pane. These indicate a **stateful character/session assistant**, not a page-flipping e-book.

**Syntax:** all five inline JavaScript programs passed Node.js `node --check`. Each file consists of an independent HTML document with one inline script and no external script links found. `localStorage` is referenced in the phone-app sources: avoid migrating storage with real session/personal state into public code.

**Next:** open dedicated `Gandalf-Phone-App` repo; preserve the above four, their original filenames and UX differences. Static parsing is not functional testing.

## 2. Gandalf tap-only grimoire

| Exact file | Size | SHA-256 |
|---|---:|---|
| `Gandalf_Grimoire_Tap_Book_v2.html` | 28,090 | `b84d509a7e4985f8478446198eabe50720b1d473c8a1af3ae71cffbd98994111` |

The title is `Gandalf Grimoire — Tap Page Edition`. It has page-rendering templates and tap-based navigation rather than phone session tracking. **Inferred independent application** suitable for a `Gandalf-Grimoire` repo, rather than an update of the phone field app.

Its single inline JS script passed `node --check`. No images, external script references or `localStorage` references were identified in this static inspection. Only **one** source version recovered; do not fabricate three earlier updates.

## 3. Interactive D&D virtual tabletop / battlemap

| Retain | Exact file | Size | SHA-256 |
|---|---|---:|---|
| Current recovered | `dnd_battlemap_v2.html` | 27,167 | `41c8617c637d3e4949285ca739494d0035ea9f32b748a9959f3a056f639730f5` |
| Previous 1 | `dnd_battlemap_v1.html` | 20,757 | `a7bc592de919bc43591c11220f7ee5969d24c4a7446d7d0951101195c34d5e4b` |

The HTML titles are `Battlefield • D&D 5e VTT` and `Battlefield II · D&D 5e VTT`. Visible interface labels include **Encounter**, **Battlefield**, **DM Controls**, **Tokens**, and **Map artwork**. This is a separate **battlemap/VTT web app**, not an update to Gandalf's phone app.

Both inline JavaScript scripts passed `node --check`. The user also created numerous original forest/harbor battle-map images in separate ChatGPT sessions. Their relationships to the app source and any actual licensing must be checked before uploading art. Do not bundle every visual experiment simply because it depicts a battlemap. Suggested dedicated repository: `DND-Interactive-Battlemap`.

## Rights, privacy and quality gates

- D&D is a third-party game system. Distinguish original implementation from third-party rule text/illustrations, and review assets before public GitHub publication.
- No HTML source or private session data has been uploaded by this report. Dedicated repositories are needed.
- **All eight HTML source files had syntactically parseable JavaScript**. This proves neither correct interface rendering nor application logic, file persistence, accessibility, or game-rule correctness.
- Correct retention: Gandalf phone app **4 of 5**; tap grimoire **1 of 1**; battlemap **2 of 2**.
- Codex should confirm the actual newest Windows/Codex source before treating recovered ChatGPT Library versions as the absolute latest, then upload safe source with README, STATUS, CHANGELOG, ROADMAP, .gitignore and AGENTS.md to **separate** repositories.
- Log destinations/PRs in `docs/handoff/CODEX_LOG.md`; ChatGPT will not overwrite Codex-owned source.
