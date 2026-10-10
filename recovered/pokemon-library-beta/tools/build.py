"""Build the portable HTML into a static deployment directory."""
from pathlib import Path
import hashlib,re,shutil,zipfile
root=Path(__file__).resolve().parents[1]
out=root/'dist';out.mkdir(exist_ok=True);assets=out/'assets';assets.mkdir(exist_ok=True)
for old in assets.iterdir():
 if old.is_file():old.unlink()
s=(root/'Pokemon-Save-File-Library-BETA.html').read_text()
def emit(data,ext):
 name=hashlib.sha256(data).hexdigest()[:16]+'.'+ext
 (assets/name).write_bytes(data);return 'assets/'+name
def image(m):return emit(__import__('base64').b64decode(m[2]),{'jpeg':'jpg'}.get(m[1],m[1]))
s=re.sub(r'data:image/(png|jpeg|webp|gif);base64,([A-Za-z0-9+/=]+)',image,s)
def script(m):
 attrs,code=m[1],m[2]
 if 'src=' in attrs or 'application/json' in attrs:return m[0]
 return '<script'+attrs+' src="'+emit(code.encode(),'js')+'"></script>'
s=re.sub(r'<script([^>]*)>([\s\S]*?)</script>',script,s,flags=re.I)
s=re.sub(r'<style([^>]*)>([\s\S]*?)</style>',lambda m:'<link rel="stylesheet" href="'+emit(m[2].encode(),'css')+'">',s,flags=re.I)
(out/'index.html').write_text(s)
(out/'_headers').write_text('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: no-referrer
  X-Frame-Options: DENY
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Cache-Control: no-cache
/assets/*
  Cache-Control: public, max-age=31536000, immutable
''')
with zipfile.ZipFile(root/'pokemon-library-static.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(out.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(out))
print(f'Built {out}: {len(list(assets.iterdir()))} assets')
