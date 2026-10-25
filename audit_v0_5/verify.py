#!/usr/bin/env python3
"""Reproduce exact witness and the entire clipped parameter arrangement."""
import json
import sys
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path

# Resolve the distributed sibling modules even under Python isolated mode.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from arrangement import representatives
from terrain import global_routes, local_walk, neighbors, permanent_sink_set

ROOT = Path(__file__).resolve().parent


def main():
    w = json.loads((ROOT/'witness.json').read_text(encoding='utf-8'))
    grid = w['height']
    box = tuple(map(F, w['box']))
    source, A, B = (tuple(w[k]) for k in ('source', 'outlet_a', 'outlet_b'))
    shape = len(grid), len(grid[0])
    permanent, possible = permanent_sink_set(grid, box)
    assert permanent == possible == {A, B}
    # A separate robust descent certificate: a fixed downhill neighbor for
    # every other vertex, with a positive margin throughout the box.
    certificate = {}
    alo, ahi, blo, bhi = box
    corners = tuple(product((alo, ahi), (blo, bhi)))
    for r, row in enumerate(grid):
        for c, h in enumerate(row):
            v = r, c
            if v in (A, B):
                continue
            choices = []
            for rr, cc in neighbors(shape, v):
                margin = min(F(h-grid[rr][cc])+a*(c-cc)+b*(r-rr) for a, b in corners)
                if margin > 0:
                    choices.append((margin, (rr, cc)))
            assert choices
            margin, child = max(choices)
            certificate[str(v)] = {'downhill_neighbor': list(child), 'uniform_drop_margin': str(margin)}
    print('PASS: exactly two fixed strict boundary sinks for the WHOLE closed box')
    special = []
    for a, b in corners+((F(0), F(0)),):
        path = local_walk(grid, source, a, b)
        assert path[-1] == (A if (a, b) in corners else B)
        special.append({'a':str(a),'b':str(b),'path':[list(v) for v in path]})
    print('PASS: all four box corners reach A; (0,0) reaches B')
    lines, faces = representatives(grid, box)
    by_dim = Counter()
    routing_maps, terminal_maps = set(), set()
    evidence = []
    order = tuple((r, c) for r in range(shape[0]) for c in range(shape[1]))
    for dim, (a, b), signature in faces:
        successor, terminal = global_routes(grid, a, b)
        assert {v for v in order if successor[v] == v} == {A, B}
        for v in order:
            path = local_walk(grid, v, a, b)
            assert path[-1] == terminal[v]
            for i in range(len(path)):
                for j in range(i+2, len(path)):
                    assert sum(abs(x-y) for x, y in zip(path[i], path[j])) != 1
        assert terminal[source] == (A if abs(a)+b >= 1 else B)
        routing_maps.add(tuple(successor[v] for v in order))
        terminal_maps.add(tuple(terminal[v] for v in order))
        by_dim[dim] += 1
        evidence.append({'dimension':dim,'a':str(a),'b':str(b),'signs':list(signature),'terminal_map':[list(terminal[v]) for v in order]})
    # Explicitly test both switching boundaries, including deterministic ties.
    for b in (F(-1,2), F(0), F(1,2)):
        for sign in (-1, 1):
            a = sign*(1-b)
            assert local_walk(grid, source, a, b)[-1] == A
    print('PASS: two separately written routing implementations agree on all cells on every face')
    print('PASS: source formula, switching-line ties, and induced-path checks')
    result = {'version':'0.2','status':'PASS','box':w['box'],
              'permanent_strict_sinks':[list(v) for v in sorted(permanent)],
              'robust_descent_certificate':certificate,'special_paths':special,
              'comparison_and_boundary_lines':[list(l) for l in lines],
              'face_counts':{str(k):by_dim[k] for k in (0,1,2)},
              'routing_map_count':len(routing_maps),'terminal_map_count':len(terminal_maps),
              'face_representatives':evidence,
              'scope':'Finite exact arrangement certificate for this witness, not a computer proof of the universal minimality theorem.'}
    out = ROOT/'evidence'
    out.mkdir(exist_ok=True)
    (out/'witness_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Arrangement faces:',json.dumps(result['face_counts'],sort_keys=True))
    print('Routing maps:',len(routing_maps),'Terminal maps:',len(terminal_maps))
    print('PASS: exact witness checks complete; universal minimality uses PROOF.md')


if __name__ == '__main__':
    main()
