# Minimal Failure of Corner Tests for D4 Drainage with Two Fixed Boundary Sinks

Ryutaro Yonezu - Yonezu Research Lab

Version 1.0, 26 October 2026

DOI: 10.5281/zenodo.23652373

## Abstract

For a full rectangular unit D4 grid, add a shared two-axis tilt to
the baseline heights and route each vertex to its lowest strictly lower
neighbor, using a fixed row-major tie order. Assume an interior source and
exactly two strict boundary sinks that remain fixed over an entire
nondegenerate closed axis-aligned parameter rectangle. We prove that 12 cells
is the smallest grid size for which the source reaches one sink at all four
parameter-box corners but the other sink at an interior parameter. An integer
4-by-3 terrain realizes the failure with the exact outlet rule A if and only
if |a|+b >= 1. An induced-path argument and a complete 3-by-3 case analysis
prove minimality. We also give a tie-aware encoding of the deterministic
drainage forest as a unique rooted minimum spanning forest, placing the example
inside established watershed theory. Exact rational certificates corroborate
the witness. The claimed residual is the constrained grid minimum; historical
novelty and priority are not established.

## Context and contribution

Uncertain drainage on graphs is established terrain-analysis background [1].
Watershed cuts and their minimum-spanning-forest interpretations are established
image-segmentation theory [2-4]. The local drainage mechanism, the general MSF
connection, and nonconvexity after grouping several forests by one outlet are
not proposed as new principles here. The specific result is an exact size
minimum under all of the following restrictions simultaneously: a full unit
D4 rectangle, an interior source, two strict boundary sinks fixed throughout
the parameter box, a shared spatial tilt, an axis-aligned box, and deterministic
strict descent. The explicit terrain is a mathematical construction, without
a claim of typicality or empirical runoff validation.

Part I reproduces the minimum-12 proof body from the audited v0.5 candidate.
Part II reproduces its MSF comparison proof body. Section numbers in each part
are local to that part. Added context, figure, audit notes and references are
editorial publication material; no mathematical theorem or verifier is changed.

@@FIGURE@@

# Part I. The exact minimum in the specified grid class

## 1. Exact model and theorem statements

The terrain is the FULL rectangular unit grid
`V = {0,...,R-1} x {0,...,C-1}`, with all orthogonal D4 edges.
The height at `(r,c)` is

    H_(r,c)(a,b) = h_(r,c) + a*c + b*r.

The parameter domain is an arbitrary nondegenerate closed axis-aligned rectangle.
From a cell, choose a neighbor of minimum height among those STRICTLY below the
current cell. Ties use one fixed total order on vertices, independent of `(a,b)`.
If no neighbor is lower, stop. Such a vertex is called a sink, even if it is on
the boundary. Boundary cells otherwise obey the same routing rule; they are
NOT automatically absorbing. Strict descent prevents cycles.

For the minimality theorem assume that the sink set throughout the domain is
exactly the same two distinct boundary vertices A and B, and both are strict
local minima throughout. The source is an interior cell. The statement to test
is: if the source reaches A at all four parameter-box corners, must it reach A
everywhere in the box?

**Theorem 1 (failure with 12 cells).** The answer is no on a 4-by-3 grid. A
specific integer-height example below has exactly two fixed strict boundary
sinks throughout the closed box, reaches A at all four box corners, and reaches
B at the box center. The exact source-outlet regions are given below.

**Theorem 2 (minimality in this class).** No smaller full rectangular D4 grid
with an interior source and exactly two fixed strict boundary sinks throughout
an axis-aligned parameter rectangle can have this failure. Thus 12 cells is
the exact minimum IN THIS CLASS, not among arbitrary graphs or other flow rules.

## 2. The 12-cell construction

Rows run downwards and columns run rightwards. Baseline heights are:

| r / c | 0 | 1 | 2 |
|---|---:|---:|---:|
| 0 | -6 | -10 (A) | -6 |
| 1 | -3 | 10 | -3 |
| 2 | 1 | 5 (source s) | 1 |
| 3 | 6 | 0 (B) | 6 |

Take `D = [-2,2] x [-1/2,1/2]`. The table below gives a fixed strictly lower
neighbor for every non-sink. The last column is a uniform positive lower bound
on the drop `H_v-H_u` throughout D. A fixed lower neighbor is enough to exclude
a sink; it need not be the chosen steepest neighbor.

| Vertex/vertices v | Fixed lower neighbor u | Minimum drop |
|---|---|---:|
| (0,0), (0,2) | A | 2 |
| (1,0), (1,2) | directly above | 5/2 |
| (1,1) | A | 39/2 |
| (2,0), (2,2) | directly above | 7/2 |
| s=(2,1) | B | 9/2 |
| (3,0), (3,2) | B | 4 |

Every neighbor is strictly higher than A throughout D: the horizontal margins
are at least 2 and the vertical margin is at least 39/2. Every neighbor is
strictly higher than B: horizontal margins are at least 4 and the vertical
margin is at least 9/2. Hence the sink set is exactly `{A,B}` for ALL parameters,
including switching lines and the boundary of D. In particular, there are no
interior sinks and no sink is created or removed as the tilt varies.

The two side cells `(2,0)` and `(2,2)` always choose the cell directly above;
the latter cells always choose directly above again, and the two top corners
always choose A. These are minimum-height choices, not merely descending
edges: at each of the six side-path vertices, comparing the listed successor
with every other neighbor gives a positive affine margin throughout D.

Subtract the common term `a+2b` from the source and its four neighbor heights.
The source has height 5 and the neighbors have relative heights:

    West: 1-a; East: 1+a; North: 10-b; South (B): b.

The northern neighbor cannot be minimal. The minimum of West and East is
`1-|a|`; B has height b. Both competing minima are below the source throughout
D. Use increasing `(row,column)` as the tie order: either side neighbor precedes
B. It follows EXACTLY that

    terminal(s; a,b) = A    iff |a| + b >= 1,
                       B    iff |a| + b < 1.

At a=0, the two side cells tie with each other but cannot be chosen because
`b <= 1/2 < 1`. At `|a|+b=1`, the side cell wins its tie with B, as stipulated.
Thus the equality case in the formula is also covered.

All four parameter-box corners have `|a|=2`, so they reach A. At `(0,0)` the
source reaches B. The A-region consists of two disconnected side trapezoids,
separated by a B-region of positive width. This proves Theorem 1.

## 3. Greedy descent paths are induced

**Lemma.** A path generated by the minimum-neighbor rule has no chord in the
underlying graph.

Proof. Write the path as `v_0,...,v_k`, with strictly decreasing heights. If
`v_i` were adjacent to `v_j` with `j >= i+2`, then
`H_(v_j) < H_(v_(i+1))`. The rule at `v_i` could not have selected `v_(i+1)`
over the strictly lower neighbor `v_j`. Contradiction. This also covers any
fixed deterministic tie rule, since the displayed inequality is strict.

## 4. Reducing every smaller rectangle to 3-by-3

An interior source requires `R >= 3` and `C >= 3`. If `R*C < 12`, the only
possible full rectangle is 3-by-3, with its center as the unique interior
vertex. Call this source o. Its four orthogonal neighbors are N,W,E,S and the
other four cells are the grid corners.

Any descent path from o has length at most two. After a first step to N,W,E or
S, a further step can only reach a grid corner; if that corner were not a sink,
its next step would return to a different neighbor of o. This contradicts the
induced-path lemma (and returning to the previous vertex contradicts descent).
Consequently every path stops either at its first neighbor or at a grid corner
adjacent to that neighbor.

**Useful consequence.** If a neighbor u of o is selected first, then either u
is a sink, or the terminal sink is one of the grid corners adjacent to u. If
exactly one of A,B is such a corner, the terminal sink is forced. If neither
is, u cannot be the selected neighbor at any parameter in the domain.

## 5. Corner unanimity is sound on 3-by-3

We prove this for every baseline height vector, every parameter rectangle,
and any fixed total tie order, assuming the same two strict boundary sinks
throughout the whole rectangle. Translate the coordinate origin to o; the
common height shift cancels from all routing decisions. Relative neighbor
heights have the form

    N = n-b, W = w-a, E = e+a, S = d+b,

with constants n,w,e,d. Square symmetries preserve the class of axis-aligned
parameter rectangles and a fixed total tie order.

### 5.1 The target sink A is adjacent to o

Any path from o reaching A must go directly to A: reaching a different first
neighbor and then A would violate the induced-path lemma. The set of parameters
where the source chooses A is convex. Indeed, it is the intersection of the
strict affine inequality `H_A < H_o` and the comparisons with the other three
neighbors. A comparison is strict if that competitor precedes A in the tie
order, and weak otherwise. These open or closed half-planes are convex.
Therefore, if this set contains the four box vertices, it contains their
convex hull, the whole box. This treats every placement of B.

### 5.2 The target sink is the northwestern grid corner

By a square symmetry, this covers every case where A is a grid corner.
Since A and B are distinct strict local minima, they cannot be adjacent.
There remain five possible placements of B, grouped as follows.

**B is E or S, or the southeastern grid corner.**

For B=E, possible first neighbors are N,W (which must end at A) and E (already
B); S has no adjacent corner sink and cannot be chosen. For B=S the roles of
E and S are exchanged. For B=southeast, N,W end at A and E,S end at B.
In all three cases increasing a can only favor an A-labeled choice over a
B-labeled choice: W becomes lower, E becomes higher, and N,S are unchanged.
Similarly, increasing b can only favor A: N becomes lower, S becomes higher,
and W,E are unchanged. A tie settled by a fixed total order does not reverse
either monotonicity. Thus the source's A-outcome is nondecreasing in both a
and b. If it holds at the lower-left parameter corner, it holds throughout
the box. In particular, unanimity at all four corners is sufficient.

**B is the northeastern grid corner.**

The possible first neighbors are W (ends at A), E (ends at B), and N. S cannot
be chosen because neither adjacent grid corner is a sink. When N is chosen,
its next step goes to the lower of A and B, with their fixed tie order: both
are strict local minima adjacent to N. Their height difference is

    H_A - H_B = h_A - h_B - 2a,

independent of b. Therefore the outcome after a first step to N is
nondecreasing from B to A as a increases.

For a fixed b, increasing a lowers the A-labeled W, raises the B-labeled E,
leaves N unchanged, and can only switch N's label from B to A. Consequently
the source's A-outcome is nondecreasing in a.

For a fixed a, the lower of W,E is fixed, as is its tie order; N=n-b decreases
as b increases. S is never chosen. Hence the source can switch at most once
between the fixed W/E choice and the N choice. N's outlet label is constant
as b varies. In particular, if the source reaches A at both ends of a vertical
parameter segment, it reaches A throughout that segment. The same conclusion
holds at equality points under the fixed tie order.

Now assume all four parameter-box corners reach A. The two corners with
`a=a_min` imply A on that entire vertical side. Monotonicity in a then implies
A at every parameter in the box.

**B is the southwestern grid corner.** Interchange a with b and W/E with N/S
in the preceding argument. The same conclusion follows.

These cases exhaust all placements of B not adjacent to A. This proves corner
unanimity on 3-by-3 and, with Section 4 and Theorem 1, proves Theorem 2.

## 6. Additional elementary comparison: trees

On a tree, the source-to-target path is unique. Requiring the minimum-neighbor
rule to follow that path and stop at the target imposes only affine strict or
weak inequalities, depending on tie priorities. Their intersection is convex.
Thus box-vertex unanimity is sound on a tree for affine height families. This
is an elementary observation, not a claimed new general theorem.

## 7. Claim boundaries

The exact minimum 12 is for full rectangular unit D4 grids, an INTERIOR source,
exactly TWO fixed strict boundary sinks throughout the ENTIRE axis-aligned
parameter rectangle, the stated height-tilt family, and minimum-neighbor strict
descent. It does not cover D8, holes or arbitrary grid subgraphs, automatically
absorbing boundary cells, changing sink sets, arbitrary affine coefficient
vectors, non-axis-aligned parameter polytopes, depression filling, or continuous
surface flow. The result is mathematical; it does not certify actual runoff,
flooding, or the calibration of real elevation errors.

The analytical argument is the basis for universal minimality. Exact face
enumeration certifies the particular 12-cell example. The finite 3-by-3 corpus
is a falsification check, not an exhaustive proof over all real heights.


# Part II. Encoding in the known rooted-MSF framework

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


## Audit, reproducibility and publication status

This is an AI-assisted, unrefereed preprint. User-supplied external AI reports
give mathematical PASS for the witness, the universal 3-by-3 obstruction, the
MSF argument and the v0.5 differential audit. These reports are preserved with
attribution; model identities and the number of distinct reviewers are not
inferred. They are not human journal or conference peer review, formal
proof-assistant certification, or a historical novelty assessment.

The author-side primary-source comparison is bounded. Driemel's final journal
PDF and the specific Allene/Cousty passages were inspected author-side; the
external reviewer explicitly did not verify those citations or search the
literature. Partial access/inspection limits for other related works remain
in SOURCE_COMPARISON.md. No historical priority or absence-of-prior-work claim
is made. Historical novelty remains INCONCLUSIVE.

The witness certificate covers 16 vertices, 23 one-dimensional faces and
8 two-dimensional cells of the parameter arrangement. The finite 3-by-3
diagnosis uses 1,120 candidate terrains, 362 accepted fixed-two-sink terrains,
233 unanimous-corner cases and 10,028 exact faces. It is not an exhaustive
search over all heights. The MSF oracle compares all 3,255 feasible rooted
forests at 47 representatives, totaling 152,985 exact cost comparisons.
Universal minimality and continuum MSF equivalence rest on the proofs, not
on finite representative counts or Euler consistency alone.

Reviewer-reported larger searches are not author reproductions. The earlier
approximately 56.7-million search / 44 positive controls and the later
approximately 45,000 accepted terrains / one positive control remain separate
reports; no pooled count, detection rate or independence is inferred. Additional
reviewer source code and raw logs were not supplied. The latest differential
report specifies Linux and Python 3.13. Author runs used Linux and Python
3.12.14. Windows execution on the author's own PC remains unconfirmed.

Offline reproduction from the extracted package uses only the standard library:

    python3 -I audit_v0_5/check_hashes.py
    python3 -I audit_v0_5/verify.py
    python3 -I audit_v0_5/audit_3x3.py
    python3 -I audit_v0_5/audit_msf_equivalence.py

Use absolute script paths when running from another working directory.
Check hashes before regenerating the evidence JSONs. The public package keeps
the complete audited v0.5 archive and extracted files byte for byte. Its
historical HOLD annotations describe preparation-stage review status. The
author subsequently instructed public upload on 26 October 2026. This changes
dissemination status only; novelty, Windows validation and human-review status
are not upgraded. See PUBLICATION_STATUS.md and the manuscript-provenance receipt.

## References

[1] A. Driemel, H. J. Haverkort, M. Löffler and R. I. Silveira.
Flow computations on imprecise terrains. Journal of Computational Geometry
4(1), 38-78 (2013). DOI: 10.20382/jocg.v4i1a3.
https://doi.org/10.20382/jocg.v4i1a3

[2] J. Cousty, G. Bertrand, L. Najman and M. Couprie.
Watershed cuts: minimum spanning forests and the drop of water principle.
IEEE Transactions on Pattern Analysis and Machine Intelligence 31(8),
1362-1374 (2009). DOI: 10.1109/TPAMI.2008.173.
https://doi.org/10.1109/TPAMI.2008.173

[3] C. Allene, J.-Y. Audibert, M. Couprie and R. Keriven.
Some links between extremum spanning forests, watersheds and min-cuts.
Image and Vision Computing 28(10), 1460-1471 (2010).
DOI: 10.1016/j.imavis.2009.06.017. Part II cites the primary 27-page author
manuscript's Theorem 5.3 and Remark 5.2; identical final-journal theorem
numbering is not asserted.
https://imagine.enpc.fr/publications/papers/IMAVIS09.pdf

[4] J. Cousty, L. Najman, B. Perret and D. S. Maia.
Playing with Kruskal: A State-of-the-Art Report on Watershed Cuts.
Journal of Mathematical Imaging and Vision 68, article 65 (2026),
published 4 September 2026. DOI: 10.1007/s10851-026-01347-0.
Section 3.2, Theorem 3 is the seeded-MSF implication used as prior context.
https://doi.org/10.1007/s10851-026-01347-0

Research inquiries and earlier overlapping work: yonezaemon1+research@gmail.com.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved. No general reuse or
redistribution license is granted. Third-party papers are referenced, not
redistributed in the companion package.
