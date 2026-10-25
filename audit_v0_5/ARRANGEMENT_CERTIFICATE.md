# Coverage of the rational arrangement certificate

For every vertex take its own affine height and those of all D4 neighbors.
Include the equality line for each pair, if it intersects the closed parameter
box. Lines not meeting the box have a constant nonzero comparison sign there.
Add the four box supporting lines and remove coincident copies.

`arrangement.py` enumerates all pairwise nonparallel intersections in the box,
including its corners. These are all arrangement vertices. On each line it
sorts the vertices and takes a midpoint of every consecutive pair: these are
representatives of all relatively open 1D faces. Boundary segments are included.

To sample 2D faces, from each segment midpoint it moves in both normal
directions by a rational epsilon. For every other line with nonzero normal
speed, epsilon is at most HALF its distance-to-crossing along that normal.
Thus no other comparison changes sign. Only candidates strictly inside the
box are kept. Every 2D face has an arrangement edge on its boundary (the box
is bounded), and therefore receives a representative in this way.

Sign vectors deduplicate representatives of the same face. Each sign-defined
set is an intersection of open half-planes and line equalities and is convex,
so one nonempty sign vector is one face. The route, ties, sink set, and all
terminal assignments are constant on a face. This justifies checking one
rational representative per face, including 0D and 1D tie faces.

The source formula has boundaries `a+b=1` for a>=0 and `-a+b=1` for a<=0,
and these are among the source's neighbor-comparison lines. Its truth value
is also constant on every enumerated face. Fractions perform every comparison
exactly; no floating-point tolerance is used.

This certificate establishes the displayed example over the entire closed
box. It does not establish the 3-by-3 universal theorem, which uses PROOF.md.
