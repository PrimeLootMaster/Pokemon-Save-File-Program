import test from 'node:test';
import assert from 'node:assert/strict';
import { SaveDocument, hexPreview, detectAdapters } from '../src/core.js';
test('export is byte-identical and copy-isolated', () => {
 const source = Uint8Array.from([0,1,127,255]);
 const doc = new SaveDocument(source);
 source[0] = 99;
 assert.deepEqual(doc.exportBytes(), Uint8Array.from([0,1,127,255]));
 const exported = doc.exportBytes(); exported[1] = 99;
 assert.equal(doc.exportBytes()[1], 1);
});
test('empty files round-trip', () => assert.equal(new SaveDocument(new Uint8Array()).exportBytes().length,0));
test('hex preview bounded', () => assert.equal(hexPreview(Uint8Array.from([0,15,255]),2),'00 0f'));
test('unknown formats stay unknown', () => assert.deepEqual(detectAdapters(new Uint8Array([1,2])),[]));
test('adapter detection requires explicit true', () => assert.equal(detectAdapters(new Uint8Array(),[{detect:()=>true},{detect:()=>false},{detect:()=>1}]).length,1));
