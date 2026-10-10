# Codex: start here

Read the repository root `AGENTS.md` **before touching source**. This is the temporary collaboration hub until every independent application has its own repository.

## Immediate workflow on Windows/Codex

1. Inventory **actual Codex workspaces and Windows directories** containing project source. Record exact path, filename, SHA-256, filesystem dates, Git remote, language, and any README; do not rely on conversational guesses. Exclude secrets, personal data, ROMs and user save files from public commits.
2. Reconcile with the ChatGPT Library filenames in `RECOVERY_INVENTORY.md`. The Library is not automatically mounted into your Windows/Codex environment; **do not invent access**. Request transfer of a specific missing artifact only when needed.
3. Determine project boundaries by executable/UI behavior and code, **not common franchise names**:
   - **Pokémon save editor / Save Workspace** (files named `PokemonSaveFileHacks-*.html`, historic v24–v35; contains save import/export).
   - **Pokémon button-clicking website** (independent web application; source location not yet verified).
   - **Pokémon browser-playable game website** (overworld/tile movement/buildings/interactions; independent application; source location not yet verified).
   - Do not assume v35 branches represent sixteen separate products; each branch candidate is a development facet of the save editor.
4. For each app, identify latest *genuine* source and its previous **three chronological updates** using source/Git history, not names alone. Deduplicate identical hashes. Preserve all files/modules required by each retained version.
5. Create a separate GitHub repository for every independent, publishable project under the owner's account **if authorized tools permit**; user has authorized organization/upload of their projects. Suggested descriptive slugs appear below. Write project-specific README, STATUS/PROJECT_INFO, ROADMAP, CHANGELOG, .gitignore, and AGENTS.md. Mark uncertain claims unverified.
6. Work on your `codex/recover-<slug>` branches. Open PRs, or if no PR capability exists, preserve safe incremental commits and record the exact GitHub URL/SHA. Never force-push.
7. Update **only** `docs/handoff/CODEX_LOG.md` in this coordination repository with per-project provenance, repository link, commit SHA, validation and blockers. Do not overwrite `CHATGPT_LOG.md`; read it to avoid duplication.

## Important Pokémon warning

`PokemonProgram-FROZEN-REFERENCE-ARCHIVE.zip` is a **historical frozen reference archive dated 2026-10-04**. Its internal `FROZEN_REFERENCE_POLICY.md` and `00_START_HERE/00_READ_ME_FIRST.md` say:
- v35 comprises 16 audited branch candidates, a program manifest, validation/audit evidence, and prior v28–v34 references;
- **v35 is the newest archived reference, not the active next source base**;
- future Whole Tree work should start with a clean architecture, reusing only intentionally selected algorithms and evidence.

The current `PrimeLootMaster/Pokemon-Save-File-Program` repository is **a separate minimal inspection scaffold**. Do not delete it, overwrite the archive, or represent it as implementing v35 functionality. Before publication, inspect the archive for copyrighted visuals/user data. Publish **only user-owned, approved source**, using the four-snapshot retention rule.

## Proposed independent destinations (create only where source is confirmed)

| Project | Suggested GitHub repository | Source-finding status |
| --- | --- | --- |
| Pokémon save editor | Existing `Pokemon-Save-File-Program` | Scaffold on GitHub; historical source v24–v35 recovered in ChatGPT |
| Pokémon button-clicking website | `Pokemon-Button-Website` | Separate project confirmed by user, filename unresolved |
| Pokémon playable game website | `Pokemon-Browser-Game` | Separate project confirmed by user, filename unresolved |
| Xenogears DuckStation Save Editor | `Xenogears-DuckStation-Save-Editor` | Recovered HTML + ZIP bundle |
| Sentinel Local security monitor | `Sentinel-Local` | Five or more ZIP iterations, including RC1 |
| Organizer Local | `Organizer-Local` | v1 and v1.1 ZIPs |
| Collector utility | `Collector-Local` | Known project; source not yet located |
| Gandalf phone character assistant | `Gandalf-Phone-App` | Five HTML variants located |
| Gandalf tap grimoire | `Gandalf-Grimoire` | HTML v2 located; independent if behavior/source warrants |
| Interactive D&D battle maps | `DND-Interactive-Battlemap` | v1/v2 HTML plus related image assets |
| God & Reality reading book | `God-and-Reality-Reader` | Dark-mode HTML located; handle private manuscript content carefully; do not publish private writing without checking scope |
| Micro-Coach | `Micro-Coach` | Referenced historically; file not located in Library listing |
| AION | `AION` | Historical, discontinued; **do not reactivate** or create a new implementation without instruction |
| Pokémon Unbound cheat collections | `Pokemon-Unbound-Cheat-Notes` (optional) | Several `.cheats` files; verify provenance and redistribution constraints |

No source yet proves whether the button-based site or playable game is newer; don't guess. Additional projects may exist in Codex or local Windows; add them with evidence.

## Public upload guard

- **Do not** commit `.gba`, `.nds`, `.ups`, `.sav`, `.psehstate`, personal screenshots, secret-bearing diagnostics, large game archives, or non-licensed third-party artwork.
- Prefer private staging repositories when data ownership/privacy remains unclear. If only public repositories are available, hold suspect material for review rather than leaking it.
- `single-click-copy` is **not** a dumping ground; leave it unchanged until ownership/license is verified.
- Keep a source inventory with `SHA-256`, exact original filename, version provenance and upload commit.
- Do **not** silently flatten unrelated experiments into one monorepo.

## Handoff format

In `CODEX_LOG.md`, make one entry per project:
```text
UTC timestamp | project | local/Codex source paths | SHA-256 | version lineage
repo | working branch | commit/PR link | validation done | blockers | next operation
```

**Stop condition per project:** all recoverable user-owned source for the latest + up to 3 legitimate predecessors uploaded in the right repository; required docs present; data safety reviewed; statuses truthful; verification and blockers recorded. You do not need to finish the application to archive it.
