# Minimal failure of corner tests for D4 drainage with two fixed boundary sinks

**Scope of the minimum.** The exact value 12 applies only to FULL rectangular
unit D4 grids, an INTERIOR source, EXACTLY TWO strict BOUNDARY sinks fixed
throughout a nondegenerate closed axis-aligned box of the SHARED two-axis tilt
H_(r,c)=h_(r,c)+a*c+b*r, and lowest-STRICTLY-lower-neighbor routing with a fixed
row-major tie order. Boundary cells obey the ordinary routing rule.

Mathematical text: v0.2, 26 October 2026, unchanged in distribution v0.5.
An external AI proof audit of v0.2 was received and reports PASS; see
reviews/RECEIVED_AI_REVIEW_20261026.md. This status note is editorial only.
The received v0.4 external AI report also gives mathematical PASS, including
the separate MSF encoding; see reviews/RECEIVED_V04_AI_REVIEW_20261026.md.
Historical novelty remains INCONCLUSIVE; no human peer review is claimed.

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
