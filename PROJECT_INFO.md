# Project information

## Purpose
Local-first Pokémon save-file inspection and eventual editing using game-specific adapters. No ROM hosting or bundled copyrighted game assets.

## Current state
**Prototype / unfinished.** This repository currently contains a minimal browser inspector scaffold, not a completed Pokémon save editor. Game-specific editing, automatic format detection and cross-game migration remain unimplemented.

## Stack
Vanilla HTML, CSS, JavaScript ES modules; Node.js built-in test runner. No runtime dependencies.

## Architecture
- `index.html` and `src/app.js`: browser UI, local file selection, preview, unchanged download.
- `src/core.js`: byte-preserving save document, hex preview, adapter detection.
- `src/adapters.js`: empty registry reserved for verified game-specific implementations.
- `tests/core.test.mjs`: core behavior tests; not yet confirmed running in CI.

## Archive policy
Retain at most the newest available implementation and three immediately preceding updates for this **specific application**, with version lineage verified from original artifacts. Other Pokémon applications (button-clicking website and game website) are separate projects and must not be treated as versions of this one.

## Known limitations
No verified game adapter, checksum repair, or supported mutation. Keep backups. Browser ES modules may require a local HTTP server rather than `file://`.

## Next steps
1. Locate the newest genuine historical save-editor implementation and up to three predecessors.
2. Compare recovered work to the scaffold; preserve source rather than overwrite blindly.
3. Verify round-trip integrity and introduce the first game-specific adapter.
