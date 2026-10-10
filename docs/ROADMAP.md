# Delivery plan

## v0.1 — local lossless inspector
- [x] Browser import, metadata, SHA-256, hex preview, unchanged export
- [x] Conservative empty adapter registry and testable byte core
- [ ] Verify in Chrome/Firefox using sample files, including empty and large inputs
- [ ] Run automated tests in CI and verify downloads byte-for-byte
- [ ] Tag release only after validation

## v0.2 — first actual editor adapter
- Choose **one** documented game and save format, not every ROM.
- Obtain lawful user-provided fixtures, including multiple saves and edge cases.
- Implement detect/parse/serialize/checksum and mutation tests.
- Expose only verified fields; preserve all unknown bytes.
- Require re-import verification before advertising editing support.

## Later
- Additional generation/game adapters; inventory, party, Pokédex.
- Cross-game migration only with explicit compatibility mappings and loss reports.
- Responsive UI polish and accessibility.
- Never bundle ROMs, proprietary sprites, or third-party save files.

## Definition of done
A release is shippable only after automated tests pass and a manual round-trip produces exactly the original bytes. Unsupported inputs must fail safely.
