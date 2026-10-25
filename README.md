# No.40 - Minimal Failure of Corner Tests for D4 Drainage with Two Fixed Boundary Sinks

Ryutaro Yonezu / Yonezu Research Lab. Public preprint v1.0, 26 October 2026.

**Unrefereed, AI-assisted preprint. Historical novelty INCONCLUSIVE.
No priority claim. All rights reserved.**

## Exact scope and result

The minimum 12 applies ONLY to a full rectangular unit D4 grid, an interior
source, exactly two strict boundary sinks fixed over the whole nondegenerate
closed axis-aligned tilt box, shared heights H_(r,c)=h_(r,c)+a*c+b*r, and
lowest-strictly-lower-neighbor routing with a fixed row-major tie order.
Boundary cells follow the ordinary routing rule.

A 4-by-3 integer terrain reaches A at all four parameter-box corners and B
at the center, without creating an interior sink or changing either sink.
Its exact source rule is A iff |a|+b >= 1. The analytical 3-by-3 obstruction
establishes the exact minimum of 12 in this specified class.

The tie-aware rooted-MSF encoding applies known graph/watershed theory.
The general mechanism and nonconvexity after source-label aggregation are
not proposed as new contributions. The residual prior-equivalence question
concerns only the constrained grid minimum.

## Paper, evidence and citation

- [Nine-page English paper](paper/No40_PitFree_Corner_Preprint_v1_0.pdf).
- [Editable paper Markdown](paper/No40_PitFree_Corner_Preprint_v1_0.md) and
  [optional PDF renderer](paper/render_preprint.py).
- [Frozen v0.5 candidate ZIP](archive/No40_PitFree_Corner_Candidate_v0_5_20261026.zip).
- [Audited model and proof](audit_v0_5/PROOF.md),
  [MSF comparison](audit_v0_5/MSF_EQUIVALENCE.md),
  [primary-source comparison](audit_v0_5/SOURCE_COMPARISON.md).
- [Latest v0.5 audit receipt](publication/No40_v0_5_Audit_Receipt_20261026.md).
- [Publication status](PUBLICATION_STATUS.md) and
  [manuscript provenance](publication/MANUSCRIPT_PROVENANCE.json).

Zenodo DOI: **10.5281/zenodo.23652373**. See CITATION.cff for citation metadata.
The complete companion ZIP is supplied with the preprint record and in the
repository's publication folder. Its checksum is recorded in publication metadata.

## Offline verification

Python 3.12+ and the standard library suffice for all mathematical verifiers.
No API, network, paid service, package installation or GPU is required.
From the extracted public package, on Windows PowerShell:

    py -3.12 -I .\check_release.py
    py -3.12 -I .\audit_v0_5\check_hashes.py
    py -3.12 -I .\audit_v0_5\verify.py
    py -3.12 -I .\audit_v0_5\audit_3x3.py
    py -3.12 -I .\audit_v0_5\audit_msf_equivalence.py

Use python3 instead of py -3.12 on Linux. Use absolute script paths from
another working directory. Run hash checks BEFORE regenerating JSON evidence.
Fresh author-side release runs use Linux/Python 3.12.14; the latest received
AI differential review reports Linux/Python 3.13. Windows execution on the
author's own machine remains unconfirmed. The commands above are instructions,
not a claimed Windows receipt.

The 47-face witness certificate is exact. The finite 3-by-3 corpus is not a
universal height-space proof. The MSF oracle compares all 3,255 rooted forests
at 47 representatives (152,985 exact comparisons); the continuum equivalence
rests on the cut-property proof. The published proof bodies, original six
Python scripts and mathematical JSON evidence remain unchanged from v0.5.

PDF regeneration is optional and separate from mathematical verification.
It uses ReportLab, Matplotlib, NumPy and Pillow, including Matplotlib's bundled
DejaVu fonts. The generated PNG/SVG figure is an exact illustration of the
audited witness, not an empirical terrain model.

## Audit limits and rights

Received AI reports give mathematical PASS, including the MSF argument and
the v0.5 differential audit. They did not perform an independent novelty
search or verify the cited Allene/Cousty/Driemel passages. Author-side source
checks and their access limits are documented separately. No human peer review,
formal proof-assistant certification or historical first-discovery claim is made.

The reviewer-reported 56.7-million / 44-control and 45,000 / one-control
searches remain separate, unreproduced reports. Extra reviewer code and raw
logs were not supplied; no pooled count or detection rate is inferred.

The original audit files retain preparation-stage HOLD labels. The author
subsequently instructed this qualified public upload on 26 October 2026.
This changes dissemination status only; see PUBLICATION_STATUS.md.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved. No general reuse,
redistribution or modification license is granted. No third-party paper is
redistributed. This is a finite mathematical model, not validated runoff physics.

Research inquiries and earlier overlapping work: yonezaemon1+research@gmail.com.
Repository: https://github.com/yonezaemon1-hub/no40-pitfree-corner-minimality
