# Release review

## Confirmed fixes

- Entry registers before app initialization, uses a clickable button, and recovers immediately if Matrix rendering fails. Actual desktop clicks, mobile taps and reduced-motion entry pass for both portable and deployment artifacts, including simulated canvas errors.

- Zero friendship survives boxed-to-party conversion.
- Box and preset slots reject fractional and out-of-range coordinates.
- PC writes refuse unrecognized nonempty species records rather than silently clearing them.
- Backup restore validates version, count, byte sizes and identifier syntax; uses one transaction across both stores; and removes imported writer-verification trust.
- Level-one creation retains the growth curve's zero EXP value.
- Mew's eye details were repainted at native resolution; frame count, timing, loop and silhouette remain unchanged.

## Verified

The portable HTML and extracted static deployment both execute in Chromium. All 17 routes render; the bundled 36-route adapter matrix passes using synthetic fixtures. Independent previous checks cover all 386 Gen III species mappings and five Hoenn species round trips. Intro keyboard, touch, reduced-motion and database-search checks passed on the updated portable page.

Release checks additionally exercise PC → party → nickname/friendship edit → PC → different box and assert preserved identity and cleared source slots. Assertions protect invalid coordinates and unrecognized-record writes. IndexedDB checks reject an unsafe backup identifier and restore an archive with writer verification reset.

These checks do not cover every inventory, training, battle, Pokédex, backup, undo, or game-specific operation. The combined workflow tests use constructed fixtures, not real save files. No blanket correctness claim is warranted.

## Deployment preparation

A standard-library build extracts embedded art, styles and scripts without changing their execution order. The output uses relative, fingerprinted assets and includes cache/privacy headers for compatible static hosts. A zip contains only deployable files. No site has been published.

## Required before a production release

Verify Unbound PP data and section checksums; complete Pokémon backup field validation and atomicity for other multi-record workflows; test real saves and emulator round trips; exercise remaining feature interactions and recovery from interrupted imports. The current deliverable is a deployable beta.
