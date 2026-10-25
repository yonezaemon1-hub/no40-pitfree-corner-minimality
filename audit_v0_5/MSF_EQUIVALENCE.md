# Exact encoding in the known rooted-MSF / watershed-cut framework

26 October 2026. The mathematical body below is unchanged from v0.4.
This applies the standard MST cut property; no new algorithm or priority is
claimed. A user-supplied external AI review of v0.4 reports PASS for this
reduction, including symbolic ties and both augmentation conventions. Its
source-citation verification and novelty search were NOT performed. See
reviews/RECEIVED_V04_AI_REVIEW_20261026.md. No human peer review is claimed.

## 1. Vertex rule and edge weights

Let G=(V,E) be a finite connected undirected graph. At a fixed parameter theta,
give each vertex v a real height H_v and a distinct integer tie rank rho(v).
Every non-sink chooses its lowest strictly lower neighbor, breaking equal
neighbor heights by increasing rho. Let R be the set of ALL sinks. In No.40,
G is the unit D4 rectangle, rho(r,c)=r*C+c, and R={A,B} throughout the box.

Assign the undirected edge {u,v} the ordered-pair weight

    W_theta({u,v}) = (H_u(theta)+H_v(theta), rho(u)+rho(v)),

ordered lexicographically. Forest cost is the componentwise sum of its edge
weights, compared lexicographically. The second coordinate is symbolic; it
does not perturb the actual height or permit a horizontal step.

At a non-sink v, a lowest neighbor is strictly lower than v. Among incident
edges, the contributions H_v and rho(v) are common. Therefore its chosen edge
is the UNIQUE lightest edge incident to v under W_theta. This includes exact
height ties and reproduces the fixed vertex order.

The selected directed edges strictly decrease height. Their undirected edges
form a forest F_theta with one sink in each component. One way to exclude an
undirected cycle is to take its highest vertex: both cycle edges would have
to point out of that vertex, contrary to outdegree at most one. Following any
successor path terminates at a sink; endpoints of a selected edge have the
same terminal sink. Consequently F_theta has |V|-|R| edges and its components
are precisely the drainage basins.

## 2. Cut-property proof of the unique rooted minimum spanning forest

Add one new vertex z and an edge {z,r} for every r in R. Choose a real C below
the primary weight of EVERY original edge, and give these new edges weight
(C,0). For a compact affine parameter box, one uniform choice is

    C = min_{e in E, theta a box corner} (H_u(theta)+H_v(theta)) - 1.

Affine minima on the box occur at corners, so the strict bound holds on the
whole box. For the supplied witness C=-23.

At every non-sink v, its selected edge is uniquely lightest across the cut
{v}. At every sink r, its new edge {r,z} is uniquely lightest across {r}.
By the MST cut property, every minimum spanning tree of the augmented graph
contains all these edges. The exchange proof of that property applies to
ordered pairs: replacing a heavier crossing edge by the unique lighter one
strictly decreases the summed lexicographic cost.

These forced edges are F_theta plus the |R| new root edges. They already form
a spanning tree on |V|+1 vertices. Thus this augmented MST is UNIQUE.

A spanning forest on V containing exactly one prescribed root per component,
augmented with all root edges, is a spanning tree. Its extra cost is the same
constant |R|*(C,0). Therefore F_theta is the UNIQUE minimum spanning forest
rooted at R. All vertex root labels, not only the source label, coincide.

This proves equivalence at every parameter, including switching lines and
their intersections. It does not depend on finite sampling.

## 3. Relation to the cited watershed definitions

The established seeded-MSF-to-watershed implication is stated in Allene et al.,
Some links between extremum spanning forests, watersheds and min-cuts,
author manuscript Theorem 5.3, pp.11-12, proof Appendix B p.19:
https://imagine.enpc.fr/publications/papers/IMAVIS09.pdf .
The manuscript also warns that the converse need not hold (Remark 5.2).
Its enlarged-graph MST construction is discussed in Appendix A p.18.

Cousty et al., Playing with Kruskal (2026), Section 3.2, Theorem 3, restates
the seeded implication and defines the rooted minimum spanning forest:
https://link.springer.com/article/10.1007/s10851-026-01347-0 .
The numerical encoding and its proof in Sections 1-2 above are our comparison
argument; they are not quotations or theorem statements attributed to either
paper. In particular, we do not identify every relative watershed with an MSF.

If a cited definition requires scalar nonnegative edge weights, the finite
lexicographic edge ordering can, at EACH fixed theta, be mapped to increasing
positive ranks. The same unique-lightest-cut proof still forces this forest.
A uniform additive shift also removes negative primary weights without
changing any fixed-edge-count forest comparison. Neither observation gives
one fixed positive epsilon that implements the symbolic coordinate throughout
the continuum. Primary differences approach zero near comparison lines.
We make NO uniform-epsilon assertion and do not silently transfer theorems
requiring a scalar-affine family to a pointwise rank encoding.

For the unseeded edge-watershed theorem rooted at regional EDGE minima,
two vertex seeds must not simply be called two edge minima. There is an exact
augmentation: attach a SEPARATE pendant leaf to each original root, giving
each pendant edge weight (C,0). Do not join the two roots to one common vertex
in this construction. The pendant edges are two disjoint regional edge minima.
Every original edge has a strictly lighter adjacent edge: choose its lower
endpoint; either it is a root with a pendant, or it has a still lower neighbor.
Thus no other regional edge minimum exists. A forest rooted at these two
minimum components is exactly an original rooted forest plus the pendants.
The resulting unseeded watershed cut projects to the same original labels.
This uses the known MSF/watershed-cut characterization of Cousty et al. (2009),
Theorem 10, with the finite scalar-order interpretation if needed.

The common super-root in Section 2 is an MST proof device; as an unseeded
edge map it has one connected minimum and does NOT itself represent two
catchment basins. The separate-pendant augmentation adds |R| vertices. It
preserves labels, but does not preserve a claim about minimum ORIGINAL grid
size. The No.40 minimum is not a minimum among arbitrary watershed graphs.

## 4. What this resolves, and what it does not

The edge primary weights are affine in (a,b). For any fixed rooted forest F,
the region where F is optimal is an intersection of comparisons with all
other forests. Each comparison is an affine strict or weak half-plane,
according to the constant symbolic secondary costs, so the region is convex.
The label of a source can aggregate several different optimal forests. Such
a union need not be convex. In this witness, (-2,0) and (2,0) have source label
A, while their midpoint (0,0) has label B.

This is elementary parametric optimization inside a KNOWN watershed/MSF
framework. Neither the framework nor generic nonconvexity after label
aggregation is a proposed new contribution. The residual candidate is ONLY
the exact 12-cell minimum under all original rectangular D4 / interior-source /
fixed two strict boundary sinks / shared tilt / axis-aligned-box constraints.
The inspected MSF theorems supply no 3-by-3 obstruction or grid-size bound by
themselves. No direct derivation of that precise result was identified; this
bounded comparison does not prove that none exists.

## 5. Exact finite cross-check

Run, from any working directory using an absolute script path if necessary:

    python3 -I audit_msf_equivalence.py

Only the Python standard library is used. The script constructs the original
12-vertex / 17-edge graph and enumerates ALL 19,448 subsets of ten edges.
Exactly 3,255 are spanning forests with one of A,B in each component.
At every one of the 47 No.40 arrangement face representatives, it compares
all 3,255 exact lexicographic costs (152,985 comparisons in total).

The unique minimizer agrees with the drainage forest, a separate root-aware
Kruskal implementation, the ordinary super-root MST, and all terminal labels.
There are three distinct optimum forests. Separate-pendant root-aware Kruskal
also agrees, and only the two pendants are regional edge minima. Boundaries
and fixed ties are included. Results are in
evidence/msf_equivalence_verification.json and the captured execution log.

This is an independent combinatorial optimization oracle for the witness,
not an independent reproduction of the external reviewer's search. Comparing
representatives alone does not certify every candidate-forest cost comparison
over a face. The full-continuum equivalence rests on Sections 1-2; universal
3-by-3 minimality rests on PROOF.md. Neither follows merely from this finite
enumeration.
