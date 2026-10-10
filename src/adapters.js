// Each verified adapter must implement:
// { id: string, detect(bytes: Uint8Array): boolean,
//   parse(bytes: Uint8Array): object,
//   serialize(model: object, originalBytes: Uint8Array): Uint8Array }
// Detection is conservative: ambiguous/unknown formats remain unsupported.
// Do not register an adapter without real save fixtures and round-trip tests.
export const adapters = [];
