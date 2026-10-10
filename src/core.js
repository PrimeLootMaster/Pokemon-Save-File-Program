export class SaveDocument {
  constructor(bytes, filename = 'save.sav') {
    if (!(bytes instanceof Uint8Array)) throw new TypeError('Expected Uint8Array');
    this.bytes = new Uint8Array(bytes);
    this.filename = filename;
  }
  exportBytes() { return new Uint8Array(this.bytes); }
  get size() { return this.bytes.byteLength; }
}
export function hexPreview(bytes, limit = 256) {
  if (!(bytes instanceof Uint8Array)) throw new TypeError('Expected Uint8Array');
  return Array.from(bytes.slice(0, limit), b => b.toString(16).padStart(2, '0')).join(' ');
}
export function detectAdapters(bytes, adapters = []) {
  return adapters.filter(adapter => adapter && typeof adapter.detect === 'function' && adapter.detect(bytes) === true);
}
