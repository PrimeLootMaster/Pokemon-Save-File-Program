# Pokémon Save File Program

Local-first, ROM-agnostic save inspector and future editor. No ROMs, proprietary assets, or save files included.

## v0.1 inspection slice
Open `index.html` in a browser. Select a local file to inspect size, SHA-256 and hexadecimal preview, then export unchanged bytes. Nothing is uploaded. If browser security blocks ES modules from `file://`, serve the directory locally with `python -m http.server 8000` and open `http://localhost:8000`.

**Important:** No Pokémon-specific decoding, editing, save validation or checksum repair exists yet. Unknown formats are explicitly unsupported. Back up original saves.

## Architecture
`src/core.js` handles byte preservation and adapter selection. `src/adapters.js` defines the future adapter contract. `src/app.js` provides the browser UI. `tests/core.test.mjs` tests the core. `docs/ROADMAP.md` defines release gates.

Run `npm test` with a recent Node.js version. The application has no runtime dependencies.

The next release must implement and test one real game-specific adapter against lawful fixtures before advertising Pokémon editing.

Independent fan utility; not affiliated with Nintendo, Game Freak or The Pokémon Company.
