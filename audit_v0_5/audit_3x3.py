#!/usr/bin/env python3
"""Bounded adversarial diagnosis of PROOF.md, not a minimality proof.
Random weighted-distance terrains, all boundary root pairs, exact filtering,
and exhaustive parameter-arrangement faces for every accepted terrain.
"""
import argparse
import heapq
import json
import random
import sys
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

# Resolve the distributed sibling modules even under Python isolated mode.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from arrangement import representatives
from terrain import global_routes, local_walk, permanent_sink_set


def distance_terrain(rng, roots):
    adjacency = [[] for _ in range(9)]
    for r in range(3):
        for c in range(3):
            v = 3*r+c
            for rr, cc in ((r+1,c),(r,c+1)):
                if rr < 3 and cc < 3:
                    w = 3*rr+cc
                    cost = rng.randint(1,12)
                    adjacency[v].append((w,cost))
                    adjacency[w].append((v,cost))
    dist = [10**9]*9
    todo = []
    for r,c in roots:
        v = 3*r+c
        dist[v] = rng.randint(-4,4)
        heapq.heappush(todo,(dist[v],v))
    while todo:
        d,v = heapq.heappop(todo)
        if d != dist[v]:
            continue
        for w,cost in adjacency[v]:
            if d+cost < dist[w]:
                dist[w] = d+cost
                heapq.heappush(todo,(dist[w],w))
    return [dist[3*r:3*r+3] for r in range(3)]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--trials-per-pair',type=int,default=40)
    args = p.parse_args()
    assert args.trials_per_pair > 0
    seed = 4020261026
    rng = random.Random(seed)
    boundary = [(r,c) for r in range(3) for c in range(3) if (r,c)!=(1,1)]
    boxes = [tuple(map(F,b)) for b in
             [('-2','2','-1/2','1/2'),('-1','1','-1','1'),('1/4','7/4','-3/2','1/2')]]
    attempted = accepted = unanimous = faces_checked = 0
    pair_counts = {}
    corpus = []
    for roots in combinations(boundary,2):
        passed = 0
        for trial in range(args.trials_per_pair):
            attempted += 1
            grid = distance_terrain(rng,roots)
            box = boxes[trial%len(boxes)]
            permanent,possible = permanent_sink_set(grid,box)
            if permanent != set(roots) or possible != set(roots):
                continue
            accepted += 1
            passed += 1
            corners = tuple(product(box[:2],box[2:]))
            corner_outlets = [local_walk(grid,(1,1),a,b)[-1] for a,b in corners]
            target = corner_outlets[0] if len(set(corner_outlets))==1 else None
            unanimous += target is not None
            lines,faces = representatives(grid,box)
            for dim,(a,b),signature in faces:
                successor,terminal = global_routes(grid,a,b)
                for v in terminal:
                    path = local_walk(grid,v,a,b)
                    assert path[-1] == terminal[v]
                path = local_walk(grid,(1,1),a,b)
                assert 1 <= len(path)-1 <= 2, (grid,box,path)
                if target is not None:
                    assert terminal[(1,1)] == target, (grid,box,(a,b),target)
                faces_checked += 1
            corpus.append({'height':grid,'box':list(map(str,box)),
                           'roots':[list(v) for v in roots],
                           'corner_outlets':[list(v) for v in corner_outlets],
                           'face_count':len(faces)})
        pair_counts[str(roots)] = passed
    result = {'status':'PASS','seed':seed,'trials_per_pair':args.trials_per_pair,
              'boundary_root_pairs':28,'candidate_terrains':attempted,
              'accepted_fixed_two_sink_terrains':accepted,
              'unanimous_corner_cases':unanimous,'exact_faces_checked':faces_checked,
              'counterexamples':0,'accepted_by_pair':pair_counts,'corpus':corpus,
              'limits':'Only the retained weighted-distance corpus is covered. This is not exhaustive over terrain heights or parameter rectangles. The universal 3x3 theorem is analytical.'}
    out = Path(__file__).resolve().parent/'evidence'
    out.mkdir(exist_ok=True)
    (out/'small_grid_diagnosis.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: candidate terrains',attempted,'accepted fixed-two-sink terrains',accepted)
    print('PASS: unanimous corner cases',unanimous,'exact arrangement faces',faces_checked)
    print('PASS: 3x3 diagnosis; no counterexample in this finite corpus')
    print('NOT an exhaustive height-space search; see the analytical minimality proof')


if __name__ == '__main__':
    main()
