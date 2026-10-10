# Pokémon Save File Library — beta

A browser application for inspecting and editing supported Pokémon saves, with a browser-local Transfer Hub. Uploaded saves are handled locally; optional artwork and links contact external hosts. No backend, shared cloud library, or global leaderboard service is included.

## Develop and check

Requires Python 3, Chromium, and Python Playwright for browser checks. The app itself has no package installation requirement.

```sh
python tools/build.py
python -m http.server 8766 --bind 127.0.0.1 --directory /workspace
```

From the repository, in another terminal:

```sh
python tests/browser_checks.py
APP_BASE=http://127.0.0.1:8766/Pokemon-Save-File-Program/ python tests/intro_checks.py
```

Set `APP_URL` when serving at another address and `CHROMIUM` for a different browser executable. Tests cover all 17 routes, 36 synthetic adapter routes, slot bounds, zero friendship, preservation across edit/transfer workflows, and refusal to overwrite unrecognized PC records. Results are written to `tests/results.json`.

## Deploy

Build with `python tools/build.py`. Publish **only `dist/`**, or unpack `pokemon-library-static.zip` into a static hosting site's document root. The root `index.html` works without a build server or SPA rewrites. Relative assets allow hosting below a path prefix. Serve over HTTPS with JavaScript, CSS and WebP MIME types. Netlify/Cloudflare Pages can apply the included `_headers`; other hosts require equivalent header configuration. Fingerprinted assets can be cached indefinitely; HTML should be revalidated.

The standalone `Pokemon-Save-File-Library-BETA.html` remains portable. Earlier `-pixel`, `-redrawn`, and `-refined` files are historical snapshots.

Do not upload the entire repository or any save files to hosting. Deploying on a new origin creates a separate browser-local library: export Transfer Hub backups before moving origins. No publication has been performed by this preparation.

## Release status

Deployable as a **beta**, not certified for all games or real-save writes. Use copies of saves and retain originals. Synthetic converter tests do not establish emulator compatibility. A release candidate still requires representative real saves, emulator load/save round trips, and an audit of every supported game version.

Known gaps:

- Unbound section 4 checksum rules are unknown; direct repairs remain blocked.
- Unbound party conversion and changed-move editing use provisional PP values instead of a verified move PP table.
- Backup restoration validates basic schemas and uses an atomic transaction. Broader Pokémon field validation and atomicity of other multi-record workflows remain release work.
- Learnsets are not bundled; creation does not validate move legality.
- Optional online artwork may fail offline. Global leaderboards/cloud synchronization are not implemented services.

See `RELEASE-REVIEW.md` for verification scope. Mew artwork is a reference-guided pixel repaint with eight 100 ms frames, transparent background and interior eye refinements.

## GitHub recovery copy

This is an isolated recovery of the uploaded standalone workspace, not a replacement for the repository inspector or an adoption of the frozen v35 archive. Embedded raster artwork is omitted pending redistribution permission. Layout placeholders replace it; the locally retained original includes the Mew animation. External artwork URLs remain optional references, not bundled assets. See PROVENANCE.json for exact input and publication hashes. No third-party licensing claim is made.

Serve from this directory (`python -m http.server 8000`); set `APP_URL=http://127.0.0.1:8000/dist/` and `APP_BASE=http://127.0.0.1:8000/` when running browser checks.

Independent fan utility; not affiliated with Nintendo, Game Freak, or The Pokémon Company.
