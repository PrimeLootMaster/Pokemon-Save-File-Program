import { SaveDocument, hexPreview, detectAdapters } from './core.js';
import { adapters } from './adapters.js';
const input = document.querySelector('#file');
const output = document.querySelector('#details');
const download = document.querySelector('#download');
let current = null;
input.addEventListener('change', async () => {
  download.disabled = true;
  current = null;
  const file = input.files?.[0];
  if (!file) { output.textContent = 'No file selected.'; return; }
  try {
    const bytes = new Uint8Array(await file.arrayBuffer());
    current = new SaveDocument(bytes, file.name);
    const digest = await crypto.subtle.digest('SHA-256', bytes);
    const sha = Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, '0')).join('');
    const matches = detectAdapters(bytes, adapters);
    output.textContent = 'Name: ' + file.name + '\nSize: ' + current.size + ' bytes\nSHA-256: ' + sha +
      '\nAdapter: ' + (matches.length === 1 ? matches[0].id : 'Unsupported / unknown') +
      '\n\nFirst 256 bytes (hex):\n' + hexPreview(bytes);
    download.disabled = false;
  } catch (error) { output.textContent = 'Unable to inspect file: ' + error.message; }
});
download.addEventListener('click', () => {
  if (!current) return;
  const url = URL.createObjectURL(new Blob([current.exportBytes()], {type:'application/octet-stream'}));
  const link = document.createElement('a');
  link.href = url;
  link.download = current.filename;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
