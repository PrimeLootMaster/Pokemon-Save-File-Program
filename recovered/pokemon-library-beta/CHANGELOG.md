# Recovered source lineage

Four distinct snapshots are now retained: original upload, earlier pixel revision, entry/release fixes, and complete backup field validation. Session actions establish this order; source creation dates are unverified. The redrawn/refined aliases duplicate the pixel snapshot and are not counted separately. The entry/release revision was preserved before this update. PROVENANCE.json records original and transformed hashes.

Current changes include species mapping, zero EXP detection, mobile drawer access, Matrix entry recovery, storage coordinate checks, zero friendship preservation and atomic basic backup restoration. See RELEASE-REVIEW.md for test scope and remaining limitations. All published snapshots omit embedded raster artwork; unmodified inputs remain local.

Backup validation now checks numeric fields and arrays, source relationships, representation bytes, bounded object nesting and unsafe object keys before any database mutation. Derived canonical identity is rebuilt instead of trusting backup metadata. Unknown read-only archive profiles remain recoverable. Fourteen pure validator regressions and a valid/invalid IndexedDB restore workflow pass.
