#!/usr/bin/env python3
"""Prior-art equivalence audit, not a new drainage algorithm or novelty proof.
Exact comparison: D4 descent, rooted Kruskal, ALL rooted spanning forests,
and ordinary MST with a super-root. Includes fixed ties on all 47 faces.
"""
import json
import sys
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from arrangement import representatives
from terrain import global_routes

ROOT = Path(__file__).resolve().parent


def graph_data(grid):
    nr,nc = len(grid),len(grid[0])
    vertices=[(r,c) for r in range(nr) for c in range(nc)]
    edges=[]
    for v,(r,c) in enumerate(vertices):
        for rr,cc in ((r+1,c),(r,c+1)):
            if rr<nr and cc<nc:
                edges.append((v,rr*nc+cc))
    return vertices,edges


def rooted_forest(n,edges,chosen,roots):
    """Independent finite combinatorial feasibility check."""
    parent=list(range(n))
    def find(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for i in chosen:
        u,v=edges[i]
        u,v=find(u),find(v)
        if u==v:
            return None
        parent[u]=v
    root_components=[find(r) for r in roots]
    if len(set(root_components))!=len(roots):
        return None
    labels=[]
    for v in range(n):
        component=find(v)
        if component not in root_components:
            return None
        labels.append(roots[root_components.index(component)])
    return tuple(labels)


def rooted_kruskal(n,edges,weights,roots):
    parent=list(range(n))
    label={r:r for r in roots}
    def find(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    selected=[]
    for i in sorted(range(len(edges)),key=lambda i:(weights[i],edges[i])):
        u,v=edges[i]
        u,v=find(u),find(v)
        if u==v or (u in label and v in label):
            continue
        parent[u]=v
        if u in label:
            label[v]=label.pop(u)
        selected.append(i)
    assert len(selected)==n-len(roots)
    return tuple(sorted(selected))


def ordinary_mst(n,edges,weights):
    parent=list(range(n))
    def find(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    selected=[]
    for i in sorted(range(len(edges)),key=lambda i:(weights[i],edges[i])):
        u,v=edges[i]
        u,v=find(u),find(v)
        if u!=v:
            parent[u]=v
            selected.append(i)
    assert len(selected)==n-1
    return tuple(sorted(selected))


def main():
    witness=json.loads((ROOT/'witness.json').read_text(encoding='utf-8'))
    grid=witness['height']
    box=tuple(map(F,witness['box']))
    vertices,edges=graph_data(grid)
    n=len(vertices)
    roots=tuple(vertices.index(tuple(witness[k])) for k in ('outlet_a','outlet_b'))
    source=vertices.index(tuple(witness['source']))
    edge_index={edge:i for i,edge in enumerate(edges)}
    # Each forest cost is affine in (a,b), plus a symbolic tie coordinate.
    affine=[]
    for u,v in edges:
        ru,cu=vertices[u]
        rv,cv=vertices[v]
        affine.append((grid[ru][cu]+grid[rv][cv],cu+cv,ru+rv,u+v))
    all_forests=[]
    candidates=0
    for chosen in combinations(range(len(edges)),n-len(roots)):
        candidates+=1
        labels=rooted_forest(n,edges,chosen,roots)
        if labels is not None:
            coefficients=tuple(sum(affine[i][j] for i in chosen) for j in range(4))
            all_forests.append((chosen,coefficients,labels))
    assert all_forests
    alo,ahi,blo,bhi=box
    corners=tuple(product((alo,ahi),(blo,bhi)))
    const=min(F(p)+a*q+b*r for p,q,r,t in affine for a,b in corners)-1
    lines,faces=representatives(grid,box)
    outcomes=[]
    distinct=set()
    for dim,(a,b),signs in faces:
        succ,terminal=global_routes(grid,a,b)
        directed_forest=tuple(sorted(edge_index[tuple(sorted((i,vertices.index(succ[v]))))]
                                    for i,v in enumerate(vertices) if succ[v]!=v))
        weights=[(F(p)+a*q+b*r,t) for p,q,r,t in affine]
        kruskal=rooted_kruskal(n,edges,weights,roots)
        assert kruskal==directed_forest
        best=None
        minimizers=[]
        for chosen,(p,q,r,t),labels in all_forests:
            cost=(F(p)+a*q+b*r,t)
            if best is None or cost<best:
                best=cost
                minimizers=[(chosen,labels)]
            elif cost==best:
                minimizers.append((chosen,labels))
        assert len(minimizers)==1
        chosen,labels=minimizers[0]
        assert chosen==directed_forest
        assert labels==tuple(vertices.index(terminal[v]) for v in vertices)
        super_edges=edges+[(r,n) for r in roots]
        super_weights=weights+[(const,0)]*len(roots)
        spanning=ordinary_mst(n+1,super_edges,super_weights)
        assert all(i in spanning for i in range(len(edges),len(super_edges)))
        assert tuple(i for i in spanning if i<len(edges))==directed_forest
        # Separate pendants, rather than a common super-root, preserve the
        # two regional minima needed by the unseeded edge-watershed theorem.
        pendant_edges=edges+[(r,n+j) for j,r in enumerate(roots)]
        pendant_weights=weights+[(const,0)]*len(roots)
        pendant_forest=rooted_kruskal(n+len(roots),pendant_edges,
                                      pendant_weights,tuple(range(n,n+len(roots))))
        assert tuple(i for i in pendant_forest if i<len(edges))==directed_forest
        assert all(i in pendant_forest for i in range(len(edges),len(pendant_edges)))
        for i,edge in enumerate(edges):
            assert any(pendant_weights[j]<weights[i]
                       for j,other in enumerate(pendant_edges)
                       if set(edge).intersection(other))
        distinct.add(chosen)
        outcomes.append({'dimension':dim,'a':str(a),'b':str(b),
                         'unique_rooted_msf_edge_indices':list(chosen),
                         'source_outlet':list(vertices[labels[source]]),
                         'minimum_cost':[str(best[0]),best[1]]})
    # The uniform primary bound comes from the minimum over box corners.
    assert all(const<weight[0] for _,(a,b),_ in faces
               for weight in [(F(p)+a*q+b*r,t) for p,q,r,t in affine])
    result={'status':'PASS','purpose':'Known-MSF equivalence audit, not a novelty claim',
            'vertices':n,'grid_edges':len(edges),'subset_candidates':candidates,
            'feasible_rooted_spanning_forests':len(all_forests),
            'exact_faces_checked':len(faces),'forest_cost_comparisons':len(faces)*len(all_forests),
            'unique_optimum_at_every_face':True,'distinct_rooted_msfs':len(distinct),
            'super_root_edges_constant_primary_weight':str(const),
            'edge_encoding':'(H_u+H_v, row_major_rank(u)+row_major_rank(v)), lexicographic',
            'checks':['all rooted forests enumerated','rooted Kruskal agrees',
                      'ordinary augmented MST agrees','all terminal labels agree',
                      'separate-pendant forest agrees; only pendants are regional edge minima',
                      'every boundary/tie face included'],
            'scope':'The general reduction uses the cut-property proof in MSF_EQUIVALENCE.md. This finite check does not prove the universal 3x3 theorem or historical novelty.',
            'faces':outcomes}
    out=ROOT/'evidence'/'msf_equivalence_verification.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: D4 descent = rooted Kruskal = exhaustive rooted MSF = augmented MST')
    print('Grid:',n,'vertices,',len(edges),'edges; subset candidates:',candidates)
    print('Feasible rooted forests:',len(all_forests),'exact parameter faces:',len(faces))
    print('Exhaustive cost comparisons:',result['forest_cost_comparisons'])
    print('Distinct rooted MSFs:',len(distinct),'; all optimum forests unique, including fixed ties')
    print('PASS: separate-pendant encoding has exactly two regional edge minima')
    print('This establishes a known-framework encoding, not novelty or a new minimality proof.')


if __name__=='__main__':
    main()
