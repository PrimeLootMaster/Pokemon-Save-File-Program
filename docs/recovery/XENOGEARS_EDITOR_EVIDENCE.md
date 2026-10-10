# Xenogears DuckStation Save Editor — original-source recovery evidence

> Evidence captured 2026-10-10 from ChatGPT Library files. This project is independent of the Pokémon save editor and belongs in its own repository, **not** in this coordination repository.

## Distinct recovered artifacts

| File | Size | SHA-256 | Classification |
|---|---:|---|---|
| `Xenogears_DuckStation_Save_Editor.html` | 19,030 bytes | `0d616a652815ca7c04dd9b1085a8cb158428453273ce6861d27212af15680551` | Original editor application |
| `Xenogears_Save_Editor_Bundle.zip` | 1,836,566 bytes | `52b4d6210957339a259d394ddea9999fd8ce7cd7fda6510ed768234454694b6c` | Original editor + README + **private save fixture**, not public upload safe |
| `Xenogears-DuckStation-Save-Editor.zip` | 9,652 bytes | `8db8ef5bcf058b441e255e279494ba6997c8f126d6d23869fa199219cfb6e86c` | ChatGPT-generated project packaging; original editor plus README, `.gitignore`, `package.json` and two Node structural tests |

The `index.html` file in the smaller project ZIP is **byte-identical** to the original `Xenogears_DuckStation_Save_Editor.html`: both have SHA-256 `0d616a652815ca7c04dd9b1085a8cb158428453273ce6861d27212af15680551`. There is **only one confirmed editor source version**, not three separate historical revisions. The ZIPs are packaging variants, **not** application updates.

## Package members

**Original bundle:**

```
Xenogears_DuckStation_Save_Editor.html
Xenogears_DuckStation_uncompressed_base.sav   # EXCLUDE from public GitHub
README_Xenogears_Save_Editor.txt
```

**Safe-to-stage project structure (subject to source licensing review):**

```
Xenogears-DuckStation-Save-Editor/
  .gitignore
  index.html
  package.json
  README.md
  tests/structure.test.mjs
```

No extra user-private save games, copyrighted game ROMs or save-state fixtures should be shipped in the repository.

## Behavior indicated by source (NOT certified)

The HTML title is `Xenogears Save-State Editor` and its interface describes support for DuckStation save state v87 and Xenogears USA SLUS-00664. It has local upload, selection, reset, and Apply + Export operations; a named `Unlock All Deathblows — All Characters` preset appears in the source. That supports classifying this as a **save-state modifier**, not a playable browser game.

The HTML includes an external script dependency from `https://unpkg.com/fzstd@0.1.1`. Therefore, **fully offline runtime operation is not established** despite the UI being local-file oriented; review this third-party dependency, availability, licensing and vendoring before describing the editor as fully offline.

## Validation performed

- Verified the original HTML and packaged `index.html` by independent SHA-256: **match**.
- Extracted **only** the safe project ZIP's `index.html`, `package.json` and structural tests into a temporary workspace.
- Ran `node --version`: v22.16.0.
- Ran `npm test`: **2/2 structural tests passed** (import/export controls, DuckStation/game identity checks).
- **No** game-state round-trip test, real-save export correctness test, browser functional run, emulator integration or licensing review performed. Thus this is a recovered **unfinished prototype**, not a certified working editor.

## GitHub publication handoff

- Codex: create dedicated `PrimeLootMaster/Xenogears-DuckStation-Save-Editor` if authorized.
- Preserve the original `index.html` unchanged; include packaging scripts and tests from the smaller ZIP only as separate additive material.
- `.gitignore` should exclude `*.sav`, ROMs, game images, credentials, exported saves, `node_modules/`, and user-specific machine logs.
- `README.md` should distinguish what buttons/source exist from functionality actually confirmed. Add `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, `AGENTS.md` and a version-provenance note.
- Retain **one** confirmed source version until earlier or later actual implementations are located. Don't invent the three missing predecessors.
- Test with synthetic, licensed or privately held fixtures without publishing personal save data.
- Record a verified GitHub commit or PR link in `docs/handoff/CODEX_LOG.md`.

This document records checks and recommended classification only. **No Xenogears source is uploaded to GitHub yet** by this contribution.
