# Pokémon Save File Program

> **Shared project-recovery coordination:** This repository also hosts temporary ChatGPT + Codex handoff instructions while the owner's independent projects are being organized. Start at [AGENTS.md](AGENTS.md), [Codex Start Here](docs/handoff/CODEX_START_HERE.md), [Recovery Inventory](docs/handoff/RECOVERY_INVENTORY.md), [ChatGPT Log](docs/handoff/CHATGPT_LOG.md), and [Codex Log](docs/handoff/CODEX_LOG.md). Work on separate branches; see file ownership in AGENTS.md.
>
> **Historical reference distinction:** This repository's current source code is a small inspector prototype. The owner's separate, much larger v35 Pokémon Save File Hacks archive is explicitly *frozen reference material*, not an approved new base. Do not silently replace the inspector or portray reference implementations as finished features.

Local-first, ROM-agnostic save inspector and future editor. No ROMs, proprietary assets, or save files included.

## v0.1 inspection slice
Open `index.html` in a browser. Select a local file to inspect size, SHA-256 and hexadecimal preview, then export unchanged bytes. Nothing is uploaded. If browser security blocks ES modules from `file://`, serve the directory locally with `python -m http.server 8000` and open `http://localhost:8000`.

**Important:** No Pokémon-specific decoding, editing, save validation or checksum repair exists yet. Unknown formats are explicitly unsupported. Back up original saves.

## Architecture
`src/core.js` handles byte preservation and adapter selection. `src/adapters.js` defines the future adapter contract. `src/app.js` provides the browser UI. `tests/core.test.mjs` tests the core. `docs/ROADMAP.md` defines release gates.

Run `npm test` with a recent Node.js version. The application has no runtime dependencies.

The next release must implement and test one real game-specific adapter against lawful fixtures before advertising Pokémon editing.

Independent fan utility; not affiliated with Nintendo, Game Freak or The Pokémon Company.
