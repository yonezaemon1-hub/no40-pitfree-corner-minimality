#!/usr/bin/env python3
"""Check the distributed files; run before regenerating evidence."""
from hashlib import sha256
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = root/'SHA256SUMS'
count = 0
for line in manifest.read_text(encoding='utf-8').splitlines():
    digest, name = line.split('  ', 1)
    assert sha256((root/name).read_bytes()).hexdigest() == digest, name
    count += 1
print('PASS SHA256',count,'files')
