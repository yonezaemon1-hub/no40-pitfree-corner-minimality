# Primary-source and equivalence comparison — v0.4

26 October 2026. Targeted author-side review, not an independent novelty audit.
The two v0.3 blockers have advanced: the final Driemel journal PDF was obtained,
and an exact rooted-MSF encoding is now proved in MSF_EQUIVALENCE.md. Neither
step establishes historical novelty of the minimum-12 theorem.

## 1. Driemel, Haverkort, Loffler, Silveira (2013), final journal text

Flow computations on imprecise terrains, JoCG 4(1), 38-78.
DOI: https://doi.org/10.20382/jocg.v4i1a3 .
Article: https://jocg.org/index.php/jocg/article/view/2939 .
Final PDF: https://jocg.org/index.php/jocg/article/download/2939/2633/7308 .

SUCCESSFULLY obtained the publisher's 41-page PDF, 764,548 bytes; SHA-256:
28f28eef07adcced41abe92d81ed57b739135ec5ee8fbb42db4e3a0e44abda27.
The final text, rather than only arXiv:1111.1651v2, was used in this follow-up.
The paper itself is not redistributed. Retrieval provenance and page anchors
are recorded in evidence/SOURCE_RECEIPTS.json.

Targeted passages checked: printed pp.40-41, 51, 55-56, 59, 62, 67, 72-74,
78. These cover the interval/network model, watershed overlay, algorithmic
results, regular-terrain relations, conclusions and the disconnected example.
This is not a page-by-page audit of all 41 pages.

Realizations independently choose vertex elevations within intervals; network
flow follows maximum nonnegative slope and can branch at ties or traverse
flat minima. Section 4.1.1, Definition 1 / Lemma 4 constructs a vertexwise
watershed overlay. Theorems 2-3 concern potential-watershed computation;
Theorem 5 concerns persistent watersheds. Appendix B, Lemma 21 / Figure 13,
gives a disconnected persistent watershed in the physical graph. That is
different from a source-label region in a two-dimensional parameter plane.
No statement directly yielding No.40's exact grid-size minimum was identified
in the targeted passages. Different models alone do not exclude equivalence.

Our elementary algebra explains one failed direct transfer: relative to any
baseline on a 2-by-2 patch, the two tilts have increments

| Cell | Tilt (1,-1) | Tilt (-1,1) | Vertexwise minimum |
|---|---:|---:|---:|
| (0,0) | 0 | 0 | 0 |
| (0,1) | 1 | -1 | -1 |
| (1,0) | -1 | 1 | -1 |
| (1,1) | 0 | 0 | 0 |

The minimum column forces a=b=-1 but would then give -2 at (1,1).
Thus this tilt family is not closed under coordinatewise minimum. This is
our comparison argument; it is not a theorem attributed to Driemel et al.
The overlay construction cannot simply be reused inside this restricted
family, although other reductions remain possible.

## 2. Cousty, Bertrand, Najman, Couprie (2009)

Watershed cuts: minimum spanning forests and the drop of water principle,
IEEE TPAMI 31(8), 1362-1374. DOI: https://doi.org/10.1109/TPAMI.2008.173 .
Primary author-uploaded paper:
https://www.researchgate.net/publication/26307310_Watershed_Cuts_Minimum_Spanning_Forests_and_the_Drop_of_Water_Principle .

Definitions 5/8, Lemma 9 and Theorem 10 establish watershed cuts and their
minimum-spanning-forest characterization relative to regional minima.
The old author PDF link failed; the author-uploaded primary text was readable.
This framework is known background. MSF_EQUIVALENCE.md now provides an exact
No.40 encoding, including ties, and distinguishes vertex seeds from regional
edge minima. Its pendant augmentation preserves basin labels, not original
rectangular grid size. No minimum-12 consequence was identified.

## 3. Allene, Audibert, Couprie, Keriven (2010)

Some links between extremum spanning forests, watersheds and min-cuts,
Image and Vision Computing 28(10), 1460-1471.
DOI: https://doi.org/10.1016/j.imavis.2009.06.017 .
Primary 27-page author manuscript:
https://imagine.enpc.fr/publications/papers/IMAVIS09.pdf .

Manuscript Theorem 5.3, pp.11-12, and Appendix B p.19 show that a minimum
spanning forest cut rooted in markers is a relative watershed. Remark 5.2
warns that the converse need not hold. Appendix A p.18 discusses deriving
rooted-MSF properties from an enlarged-graph MST. Theorem numbers here refer
to this manuscript, not an assumed identical numbering in the final article.
This directly supplies known context for the No.40 reduction; no claim that
every relative watershed is an MSF is made.

## 4. Cousty, Najman, Perret, Maia (2026)

Playing with Kruskal: A State-of-the-Art Report on Watershed Cuts,
JMIV 68, article 65, published 4 September 2026.
https://link.springer.com/article/10.1007/s10851-026-01347-0 .

The open primary full text was inspected for the seeded/unseeded definitions,
Section 3.2 Theorem 3, and the seed-based algorithms. Theorem 3 restates the
marker-rooted-MSF-to-watershed implication, citing Allene et al. Its definition
requires a spanning forest with exactly one marker per component and minimum
total edge weight. This closes the known-framework classification question
when combined with our explicit reduction. It does not establish a smallest
full D4 rectangle for failure of corner testing.

## 5. Meyer (2012)

Watersheds, waterfalls, on edge or node weighted graphs:
https://arxiv.org/html/1204.2837v1 .
The primary full text was readable. The node/edge relation, scissor choices,
drainage forests and MSF discussion provide existing conceptual background.
No minimum-12 result was identified in those inspected portions.

The distinct work The steepest watershed: from graphs to images was also
obtained in full in this follow-up:
https://arxiv.org/pdf/1204.2134 . It has 29 pages, 2,542,609 bytes, SHA-256
f3fc9c364ddc801507ccf05e90feeccd92e81bcc84cbf01019b9ef2ecc13b5ea.
The PDF has an arXiv:1204.2134v1 / 10 April 2012 banner but its title page
prints 15 September 2021; these observations are recorded without assuming
that the two dates describe the same event.

Inspected Sections 2.2-2.4 (pp.4-6) and 6-7 (pp.24,26-27). The drainage graph
retains lowest-neighbor directions; the full-path lexicographic criterion
prunes alternatives by subsequent heights, rather than by No.40's fixed local
vertex order. Section 7 also discusses retaining one lowest-neighbor arrow
and labeling connected components, with a citation to Bieniek and Moga (2000).
The basic routing mechanism is therefore firmly known background. No direct
minimum-12 theorem was identified in these inspected passages. The cited
2000 paper was not itself fully reviewed here.

## 6. Remaining partially inspected works

Meyer, The Waterfall Hierarchy on Weighted Graphs (ISMM 2015),
https://doi.org/10.1007/978-3-319-18720-4_28 .
Institutional primary PDF:
https://people.cmm.minesparis.psl.eu/users/marcoteg/cv/publi_pdf/MM_refs/meyer/2015_ismm_waterfall_meyer_paper.pdf .
Only introductory flooding/forest material was accessible; later-page requests
and a direct-download retry (HTTP 503) failed. No full-text exclusion is claimed.

Straehle et al., Seeded watershed cut uncertainty estimators for guided
interactive segmentation (CVPR 2012), 765-772.
Primary proceedings, indexed Section 3.2, printed p.767:
https://projet.liris.cnrs.fr/imagine/pub/proceedings/CVPR2012/data/papers/097_P1B-44.pdf .
Author report:
https://hci.iwr.uni-heidelberg.de/sites/default/files/publications/files/1508043927/straehle_12_seeded.pdf .
Inspected indexed text concerns edge exchanges and weight perturbations that
change seeded segmentations. Full PDF attempts failed. This is related robustness
research; a full-text equivalence check remains incomplete.

## 7. Disposition

| Claim or former blocker | Result |
|---|---|
| Final Driemel PDF unavailable | RESOLVED: final publisher PDF obtained; targeted passages checked |
| Could No.40 be encoded as a rooted MSF / watershed cut? | YES: explicit cut-property proof, fixed ties included |
| General watershed/MSF connection | KNOWN; not a candidate contribution |
| Generic nonconvexity after grouping forests by source label | Elementary; not a candidate contribution |
| Exact minimum 12 in the full stated model | No match/direct derivation identified in inspected sources; INCONCLUSIVE |
| Exhaustive literature exclusion / historical priority | NOT ESTABLISHED |

Both search engines and citation chaining were used. Terms included correlated
elevation errors, affine/shared tilt, parametric drainage, corner testing,
fixed sinks, seeded forests, watershed cuts, and small rectangular grids.
Sparse exact-phrase results are weak negative evidence. The two specific
v0.3 questions are addressed author-side, while the broader historical search
and independent novelty review remain incomplete. Publication remains HOLD.
