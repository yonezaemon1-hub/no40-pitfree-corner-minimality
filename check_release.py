#!/usr/bin/env python3
"""Verify this public snapshot before regenerating evidence. Standard library only."""
from pathlib import Path
from hashlib import sha256
root=Path(__file__).resolve().parent
count=0
for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
    digest,name=line.split('  ',1)
    assert sha256((root/name).read_bytes()).hexdigest()==digest,name
    count+=1
print('PASS public-release SHA256',count,'files')
