# No.40 candidate v0.5 — Minimal failure of corner tests for tilt-correlated drainage

26 October 2026. Ryutaro Yonezu / Yonezu Research Lab.

**Scope of the minimum.** The exact value 12 applies only to FULL rectangular
unit D4 grids, an INTERIOR source, EXACTLY TWO strict BOUNDARY sinks fixed
throughout a nondegenerate closed axis-aligned box of the SHARED two-axis tilt
H_(r,c)=h_(r,c)+a*c+b*r, and lowest-STRICTLY-lower-neighbor routing with a fixed
row-major tie order. Boundary cells obey the ordinary routing rule.

**RESEARCH CANDIDATE. Received external AI reports give mathematical PASS,
including the v0.4 MSF encoding. Historical novelty INCONCLUSIVE.
Publication HOLD.**

Distribution v0.5 records the received v0.4 review and emphasizes the exact
model restrictions above. The minimum-12 proof body, MSF proof body, all six
Python scripts, witness and mathematical JSON evidence are byte-identical to
v0.4. Only their editorial status/scope notes and review documentation change.
Version 0.2 inside the original witness/evidence identifies the audited model.

The previously unconfirmed PROOF.md comparison is now documented explicitly:
v0.3 to v0.4 changes exactly ONE line, the editorial distribution version.
The mathematical body is identical. See evidence/PROOF_V03_TO_V04.diff and
the corresponding byte/hash receipt. This check is author-side, not attributed
to the reviewer who left it unconfirmed.

## Candidate result

Under the full unit D4 rectangular-grid rule
H_(r,c)(a,b) = h_(r,c) + a*c + b*r, choose the lowest STRICTLY lower neighbor,
with fixed row-major ties. Boundary cells obey the same rule as other cells.

1. A 4-by-3 integer terrain has the SAME TWO strict boundary sinks for the
   whole closed parameter rectangle, with no interior sink at any tilt.
2. An interior source reaches A at all four parameter-box corners, but B at
   the center. Its exact rule is A iff |a|+b >= 1.
3. An analytical proof excludes 3-by-3 grids with the same assumptions.
   An interior source requires both side lengths at least three, so
   **12 cells is the exact minimum within this specified class**.

The general drainage/forest mechanism and nonconvexity after source-label
aggregation are NOT proposed as new. The sole residual candidate contribution
is this constrained exact minimum. No historical priority claim is made.

## Reproduce on a local PC

Python 3.12+; standard library only; no network, API, installation or GPU.
In Windows PowerShell, from this extracted folder:

    py -3.12 -I .\check_hashes.py
    py -3.12 -I .\verify.py
    py -3.12 -I .\audit_3x3.py
    py -3.12 -I .\audit_msf_equivalence.py

Use python or python3 on other installations. Isolated execution from another
working folder is supported when an absolute script path is supplied. Run
hash checks BEFORE regenerating evidence JSONs. The exact witness and MSF
checks are deterministic; the finite 3-by-3 corpus is retained for inspection.

verify.py checks two separately written routing implementations, uniform sink
inequalities and ALL 47 arrangement faces, including boundary/tie faces.
audit_3x3.py is auxiliary finite diagnosis, not the universal minimum proof.
audit_msf_equivalence.py enumerates all 3,255 feasible rooted forests and
compares their exact costs at each of 47 representatives, alongside Kruskal
and augmented constructions. Universal encoding rests on its cut-property
proof; representative checks alone do not prove continuum equivalence.

## Contents for review

- PROOF.md: exact model, witness and analytical 3-by-3 obstruction.
- witness.json, terrain.py, arrangement.py, verify.py: original exact certificate.
- audit_3x3.py: bounded finite diagnostic corpus.
- ARRANGEMENT_CERTIFICATE.md: parameter-face coverage argument.
- MSF_EQUIVALENCE.md, audit_msf_equivalence.py: known-framework reduction
  and independent combinatorial optimization oracle for the witness.
- SOURCE_COMPARISON.md, PRIOR_ART.md: source results, access limits and disposition.
- AUDIT_STATUS.md: author and received-review evidence, distinguished explicitly.
- INDEPENDENT_AUDIT_REQUEST.md: remaining citation/equivalence/novelty questions.
- reviews/: user-supplied v0.2, v0.3 and v0.4 external AI reports.
- evidence/: JSONs, captured logs, source receipts and revision receipt.
- history/: prior archives, including the exact audited v0.3 and v0.4 ZIPs.

The v0.4 reviewer reports Python 3.13 execution, 26,001 independent rational
points, approximately 45,000 accepted 3-by-3 two-sink terrains with no
counterexample, and one 4-by-3 positive control. These are received reports;
independent code/raw logs were not supplied. They are not pooled with the
earlier reported 56.7-million search / 44 controls or presented as author runs.
The OS and distinct-reviewer count are unspecified; no Windows execution or
human peer review is claimed. Author-side computations used Python 3.12.14.

The received mathematical PASS is separate from citation verification and
historical novelty, which the reviewer did not assess. This is an explicit
mathematical construction in a finite routing model; no empirical runoff or
frequency-in-real-terrain claim is made. No third-party paper is redistributed.

Research inquiries: yonezaemon1+research@gmail.com.

Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.
