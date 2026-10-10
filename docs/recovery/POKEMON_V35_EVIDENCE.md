# Pokémon v35 — Frozen archive integrity and development lineage

> **Evidence report, not production acceptance.** Generated from an independently examined ChatGPT Library artifact on 2026-10-10. **No original Pokémon game binaries or save files are included here.**

## Source identity

| Property | Value |
|---|---|
| Archive filename | `PokemonProgram-FROZEN-REFERENCE-ARCHIVE.zip` |
| Archive size | 40,423,130 bytes |
| Archive SHA-256 | `743c56403d64c9850a87a6fe5c2061711cce4aa147ec2c6b72235111cf60cec3` |
| Archive entries | 103 |
| Internal freeze timestamp | `2026-10-04T15:36:24.769092+00:00` |
| v35 HTML candidates | 16 |
| v35 hashes checked | 16/16 matched |
| Problems found by *metadata/hash audit* | 0 |
| Independently re-run browser tests | **None** |
| Public release safety | **Not yet reviewed / not approved** |

The archive itself states in `FROZEN_REFERENCE_POLICY.md` and `00_START_HERE/00_READ_ME_FIRST.md` that the entire v35 family is **reference-only** and the next Whole Tree attempt should start from a clean architecture, not automatic patch inheritance.

## Exact candidate byte hashes

All entries below reside under `PokemonProgram-FROZEN-REFERENCE-ARCHIVE/01_MODERN_V35_REFERENCE/` inside the source ZIP. The file names are `PokemonSaveFileHacks-v35-Branch-<number>-<feature>-Audited-Fixed-New-Trunk-Descendant.html`; the complete exact filenames can be recovered from the ZIP and its `PokemonSaveFileHacks-v35-Verification.json`.

| Branch | Feature | Bytes | SHA-256 | Manifest check |
|---:|---|---:|---|---|
| 1 | Party Pokémon | 869,548 | `18ec836fe7365ca10c8194495f26b3089dcf5ebe9ca98b448bcc7a10575e7877` | Match |
| 2 | PC Boxes | 869,492 | `226ee4d7d05da73dbc54ecc204482ed36eb7981fe9a33d1bc2ebf1dc70cef424` | Match |
| 3 | Pokémon Creation | 869,632 | `fd9026440396895df4398394c3282a4943665076e83bcef22886637ea17f4bb3` | Match |
| 4 | Strengthening | 885,782 | `2eb4f6458b4dfd2df6779a00262f8d6a02f98f4d2c71dd034093803afe7eb86c` | Match |
| 5 | Inventory | 885,688 | `1beb485027c0547dcb8276d7f424c777199f9d714bd4b3c97abfc63e218341b2` | Match |
| 6 | Story Progress | 885,618 | `926f9b2634179cf769686e9cef8d0a84f554f4dfa0295ec223537d869fd4429b` | Match |
| 7 | Perfectdex | 904,432 | `2d68da7420819d3ce696c8cd9a86f3a05f4fc031f098e99725baaa4a15ed14df` | Match |
| 8 | Battle Lab | 904,272 | `10546a02ad33e32b7469d1abe75e4d58b51eb189be9d46076767db07787c71b4` | Match |
| 9 | Leaderboard | 904,341 | `4eb8f7c91e582040e6ff754df7a584e1aeb4fd76b14c67fe9ce30d1c580ad805` | Match |
| 10 | Save Manager | 904,384 | `2fe5d2dd6b7797a4ed25343689a7b717184fdf012899f9207d4683126ac4a08e` | Match |
| 11 | Game Database | 904,367 | `8dffe03d9ff774cd748005b98dacf5c9184fe14fc28a9d1c51007fe2f95019df` | Match |
| 12 | Raw Hex Viewer | 904,296 | `975cc7dd036cc3b19a0ebaa96f6a168792ca8fb3bea0e38b8a80dd2c60a9cdef` | Match |
| 13 | Save Structure | 904,388 | `9d219c810f0952cb206cc33a920ca9d8b9eb15e73098fc8abcb289704b5dd986` | Match |
| 14 | Diagnostics | 904,373 | `ced7bcfa4c84a72efbc7f382a0d137c2355bd16dc7bbe5e1836827bc7259d705` | Match |
| 15 | Companion | 904,374 | `4f8a14b53b6d30f04fa61758c1b217b5843908012413a16518ed9c885ada0dcd` | Match |
| 16 | Save Converter | 904,425 | `84e9193c574e08b21a80b600405dbe766a720bc11f691b596eb09bc88e388df1` | Match |

Each hash was calculated again from the actual ZIP member bytes and compared to the embedded verification record. All 16 match. The two separate `LATEST_BRANCH_REFERENCES/` and `01_MODERN_V35_REFERENCE/` listings are repeat presentations of the same branch family, not proof of separate revision history.

## Archived test records — explicitly not rerun

The ZIP's `PokemonSaveFileHacks-v35-Verification.json` describes its historical runtime as **Chromium set_content, external network aborted**, viewport 1536×864, and reports `ok: true` for each of the 16 branches. It also claims two passing synthetic checks:
- FireRed → Emerald converter test with 14/14 sector checks and one test insertion.
- Species-mapping round trip for Treecko and Metagross.

Those claims remain **historical test artifacts**. The present audit confirms file integrity only. No fresh browser emulation, Pokémon game compatibility, save mutation correctness, or complete usability has been verified by this ChatGPT contribution.

All 16 v35 HTML files contain embedded `data:image/` content (at least some pictures or icons). These require attribution/copyright review before considering their upload to public GitHub. The archive has no members ending in `.gba`, `.nds`, `.sav`, `.ups`, or `.psehstate`; this is only an extension-level screen and **does not** prove the archive is publishable.

## Chronology and four-snapshot preservation rule

The reference archive includes explicit v29 and v30 trunks, v31 branch candidates, a v32 tree, v33 partial branches, v34 feature branches, and the v35 audited family.

**Do not select four random files from the sixteen v35 branches.** A branch is a feature/variant within a version family; a chronological snapshot is an implementable, coherent state at a point in the project's history. Establish which of these source candidates constitutes each true snapshot using the archived manifests and earlier source, rather than choosing by file size or copy timestamp.

The user requests at most **current + three immediately prior distinct updates per independent application**. Keep the complete necessary source for each snapshot and do not mistake a single HTML file for the whole product if dependencies exist. The v35 reference archive remains available as an off-repository preservation source; older/discarded experiments can remain locally without violating the four-version GitHub rule.

The existing `index.html` plus `src/` files on `main` are a minimal browser inspector prototype; they are **not** a verified v35 replacement. Keep the historical lineage clearly separate from the new work.

## Reproduction (Python 3 standard library, read-only archive)

```bash
python tools/audit_frozen_reference.py /path/to/PokemonProgram-FROZEN-REFERENCE-ARCHIVE.zip --output v35-evidence.json
python -m unittest discover -s tests -p 'test_audit_frozen_reference.py' -v
```

The program does not extract archive entries. On success it returns exit status 0 and reports explicit `manifest_sha256_match` flags; 1 means an integrity or layout issue, 2 means the verification couldn't run. Preserve the original ZIP unmodified.

## Next handoff to Codex

1. Read `AGENTS.md` and `docs/handoff/CODEX_START_HERE.md`; inspect `CODEX_LOG.md` for new findings.
2. If the original archive is on Windows, verify the archive SHA-256 above and run this auditor locally. **Do not require the user to re-upload source already recoverable through other means.**
3. Trace commit/order evidence for v32–v35; identify the **four most recent true chronological snapshots** and necessary dependencies. Do not label the 16 v35 branches as 16 projects.
4. Audit embedded images, URLs, licensing and secrets before public GitHub source upload. Prefer an isolated working branch and PR to overwriting the inspector.
5. Record exact uploaded paths, branch/PR, file SHA-256, and tests performed in `docs/handoff/CODEX_LOG.md`.

**Other Pokémon projects:** button-clicking website and playable-browser-game website are explicitly separate user projects. Neither is established by the v35 save-editor archive. Do not use this repository as their permanent destination.
