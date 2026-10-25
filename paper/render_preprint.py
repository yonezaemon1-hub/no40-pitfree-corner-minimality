#!/usr/bin/env python3
"""Typeset the unchanged audited proof bodies as the No.40 public preprint.
Optional typesetting dependencies: reportlab, matplotlib, Pillow.
The bundled mathematical verifiers use only Python's standard library.
"""
from pathlib import Path
import hashlib
import html
import json
import re
import textwrap

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                               TableStyle, Preformatted, Image, PageBreak, KeepTogether)

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'paper'
AUDIT = ROOT / 'audit_v0_5'
TITLE = 'Minimal Failure of Corner Tests for D4 Drainage with Two Fixed Boundary Sinks'
DATE = '26 October 2026'
VERSION = '1.0'
DOI = '10.5281/zenodo.23652373'

ABSTRACT = '''For a full rectangular unit D4 grid, add a shared two-axis tilt to
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
novelty and priority are not established.'''

CONTEXT = '''## Context and contribution

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

'''

AFTER = '''

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
'''


def figure():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})
    fig, (left, right) = plt.subplots(1, 2, figsize=(8.2, 2.8),
                                    gridspec_kw={'width_ratios': [1, 1.55]})
    grid = [[-6,-10,-6],[-3,10,-3],[1,5,1],[6,0,6]]
    left.set_xlim(-.5,2.5); left.set_ylim(3.5,-.5); left.set_aspect('equal')
    for r in range(4):
        for c in range(3):
            color = '#dbe9f2' if (r,c)==(0,1) else '#f4e0cd' if (r,c)==(3,1) else '#eeeeee' if (r,c)==(2,1) else 'white'
            left.add_patch(plt.Rectangle((c-.5,r-.5),1,1,facecolor=color,
                                         edgecolor='#59636b',linewidth=.7))
            label = ('A\n' if (r,c)==(0,1) else 'B\n' if (r,c)==(3,1) else 's\n' if (r,c)==(2,1) else '')+str(grid[r][c])
            left.text(c,r,label,ha='center',va='center',fontsize=10)
    left.axis('off'); left.set_title('(a) Baseline heights',fontsize=11,pad=8)
    b=np.linspace(-.5,.5,201)
    right.fill_betweenx(b,-2,-(1-b),color='#dbe9f2')
    right.fill_betweenx(b,-(1-b),1-b,color='#f4e0cd')
    right.fill_betweenx(b,1-b,2,color='#dbe9f2')
    right.plot(-(1-b),b,color='#26333d',lw=1.2)
    right.plot(1-b,b,color='#26333d',lw=1.2)
    right.axhline(0,color='white',lw=.7,zorder=0)
    right.axvline(0,color='white',lw=.7,zorder=0)
    for a in (-2,2):
        for bb in (-.5,.5): right.plot(a,bb,'o',color='#244d69',ms=4,clip_on=False)
    right.plot(0,0,'o',color='#874f27',ms=5)
    right.text(-1.75,0,'A',ha='center',va='center',weight='bold')
    right.text(1.75,0,'A',ha='center',va='center',weight='bold')
    right.text(0,.22,'B',ha='center',va='center',weight='bold')
    right.set_xlim(-2,2);right.set_ylim(-.5,.5)
    right.set_xticks([-2,-1,0,1,2]);right.set_yticks([-.5,0,.5])
    right.set_xlabel('a');right.set_ylabel('b',rotation=0,labelpad=12)
    right.set_title('(b) Source outlet in the tilt box',fontsize=11,pad=8)
    fig.tight_layout(w_pad=2)
    fig.savefig(PAPER/'witness_regions.png',dpi=260,bbox_inches='tight')
    fig.savefig(PAPER/'witness_regions.svg',bbox_inches='tight')
    plt.close(fig)


def register_fonts():
    folder=Path(matplotlib.get_data_path())/'fonts'/'ttf'
    for name,file in [('Serif','DejaVuSerif.ttf'),('Serif-Bold','DejaVuSerif-Bold.ttf'),
                      ('Serif-Italic','DejaVuSerif-Italic.ttf'),
                      ('Serif-BoldItalic','DejaVuSerif-BoldItalic.ttf'),
                      ('Sans','DejaVuSans.ttf'),('Mono','DejaVuSansMono.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(folder/file)))
    pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='Serif-Bold',
                                 italic='Serif-Italic',boldItalic='Serif-BoldItalic')


def inline(text):
    text=html.escape(text,quote=False)
    text=re.sub(r'`([^`]+)`',r'<font name="Mono" size="8.7">\1</font>',text)
    text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'(https://[^\s<]+)',lambda m:'<link href="'+m.group(1)+'" color="#244d69">'+m.group(1)+'</link>',text)
    return text


def styles():
    return {
        'body':ParagraphStyle('body',fontName='Serif',fontSize=10.2,leading=13.8,
                              spaceAfter=6.5,splitLongWords=True,allowWidows=0,allowOrphans=0),
        'h1':ParagraphStyle('h1',fontName='Serif-Bold',fontSize=14,leading=18,
                           spaceBefore=15,spaceAfter=9,keepWithNext=True),
        'h2':ParagraphStyle('h2',fontName='Serif-Bold',fontSize=11.6,leading=15,
                           spaceBefore=11,spaceAfter=6,keepWithNext=True),
        'h3':ParagraphStyle('h3',fontName='Serif-Bold',fontSize=10.5,leading=14,
                           spaceBefore=9,spaceAfter=5,keepWithNext=True),
        'code':ParagraphStyle('code',fontName='Mono',fontSize=8.4,leading=11.5,
                             leftIndent=10,rightIndent=5,spaceBefore=3,spaceAfter=8),
        'cell':ParagraphStyle('cell',fontName='Serif',fontSize=8.9,leading=11.6,
                             splitLongWords=True),
        'caption':ParagraphStyle('caption',fontName='Serif',fontSize=8.6,leading=11,
                                spaceAfter=10),
        'claim':ParagraphStyle('claim',fontName='Serif',fontSize=10.2,leading=13.8,
                              spaceAfter=6.5,keepWithNext=True,splitLongWords=True),
    }


def parse(md,style,width):
    lines=md.splitlines();story=[];i=0
    while i<len(lines):
        line=lines[i]
        if not line.strip(): i+=1;continue
        if line=='@@FIGURE@@':
            from PIL import Image as PILImage
            with PILImage.open(PAPER/'witness_regions.png') as im: w,h=im.size
            story.append(Image(str(PAPER/'witness_regions.png'),width=width,height=width*h/w))
            story.append(Paragraph('Figure 1. The 12-cell witness and its exact source-outlet regions. '
                'The four box corners (blue dots) reach A; the center (brown dot) reaches B. '
                'The solid switching boundaries belong to A under the fixed tie rule.',style['caption']))
            i+=1;continue
        if line.startswith('#'):
            if line=='## 2. The 12-cell construction': story.append(PageBreak())
            level=len(line)-len(line.lstrip('#'))
            story.append(Paragraph(inline(line.lstrip('#').strip()),style['h'+str(min(level,3))]))
            i+=1;continue
        if line.startswith('    '):
            code=[]
            while i<len(lines) and (lines[i].startswith('    ') or not lines[i].strip()):
                code.append(lines[i][4:] if lines[i].startswith('    ') else '')
                i+=1
            wrapped=[]
            for c in code:
                wrapped.extend(textwrap.wrap(c,width=91,replace_whitespace=False,
                    drop_whitespace=False,break_long_words=False,break_on_hyphens=False) or [''])
            story.append(Preformatted('\n'.join(wrapped).rstrip(),style['code']))
            continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                cols=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?',c) for c in cols): rows.append(cols)
                i+=1
            n=len(rows[0]);cw=[width/n]*n
            if n==3: cw=[width*.42,width*.39,width*.19]
            cells=[[Paragraph(inline(x),style['cell']) for x in row] for row in rows]
            table=Table(cells,colWidths=cw,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#edf1f3')),
                ('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#73818c')),
                ('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#c6cdd2')),
                ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),
                ('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),
                ('BOTTOMPADDING',(0,0),(-1,-1),5)]))
            story.append(KeepTogether([table,Spacer(1,8)]))
            continue
        para=[]
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','    ','|')) and lines[i]!='@@FIGURE@@':
            para.append(lines[i].strip());i+=1
        text=' '.join(para)
        j=i
        while j<len(lines) and not lines[j].strip(): j+=1
        introduces_block=j<len(lines) and lines[j].startswith(('    ','|'))
        is_claim=text.startswith(('**Lemma','**Theorem')) or introduces_block
        story.append(Paragraph(inline(text),style['claim' if is_claim else 'body']))
    return story


def footer(canvas,doc):
    canvas.saveState();canvas.setFont('Sans',7.7);canvas.setFillColor(colors.HexColor('#52606b'))
    canvas.drawString(doc.leftMargin,A4[1]-29,'No.40 | Unrefereed, AI-assisted preprint v1.0')
    canvas.drawString(doc.leftMargin,25,'Ryutaro Yonezu | '+DATE+' | All rights reserved')
    canvas.drawRightString(A4[0]-doc.rightMargin,25,str(doc.page))
    canvas.restoreState()


def main():
    PAPER.mkdir(parents=True,exist_ok=True)
    proof=(AUDIT/'PROOF.md').read_bytes();panchor=b'## 1. Exact model and theorem statements'
    proof=proof[proof.index(panchor):]
    assert hashlib.sha256(proof).hexdigest()=='fea16217acefce10ac24072447ea75b694c56fa2888640a2d44a298a25aeff14'
    msf=(AUDIT/'MSF_EQUIVALENCE.md').read_bytes();manchor=b'## 1. Vertex rule and edge weights'
    msf=msf[msf.index(manchor):]
    md=CONTEXT+proof.decode()+'\n\n# Part II. Encoding in the known rooted-MSF framework\n\n'+msf.decode()+AFTER
    (PAPER/'No40_PitFree_Corner_Preprint_v1_0.md').write_text(
        '# '+TITLE+'\n\nRyutaro Yonezu - Yonezu Research Lab\n\nVersion 1.0, '+DATE+
        '\n\nDOI: '+DOI+'\n\n## Abstract\n\n'+ABSTRACT+'\n\n'+md,encoding='utf-8')
    figure();register_fonts();st=styles()
    pdf=PAPER/'No40_PitFree_Corner_Preprint_v1_0.pdf'
    doc=SimpleDocTemplate(str(pdf),pagesize=A4,leftMargin=54,rightMargin=54,
        topMargin=49,bottomMargin=43,title=TITLE,author='Ryutaro Yonezu',
        subject='Exact minimum 12 in a restricted D4 tilt-correlated drainage model',
        creator='Yonezu Research Lab; ReportLab')
    title_style=ParagraphStyle('title',fontName='Serif-Bold',fontSize=17.5,leading=21.8,
                               alignment=TA_CENTER,spaceAfter=10)
    meta_style=ParagraphStyle('meta',fontName='Serif',fontSize=10.2,leading=14,
                              alignment=TA_CENTER,spaceAfter=5)
    note_style=ParagraphStyle('note',fontName='Serif',fontSize=8.9,leading=11.5)
    story=[Paragraph(TITLE,title_style),Paragraph('Ryutaro Yonezu<br/>Yonezu Research Lab',meta_style),
        Paragraph('Research Note No.40 | Version 1.0 | '+DATE,meta_style),
        Paragraph('DOI: '+DOI,meta_style),Spacer(1,5)]
    scope=Paragraph('<b>Scope and status.</b> Exact minimum only for full rectangular unit D4 grids, '
        'an interior source, exactly two fixed strict boundary sinks throughout a shared two-axis '
        'tilt box, an axis-aligned parameter rectangle, and deterministic strict descent. '
        'Unrefereed, AI-assisted preprint. Historical novelty: INCONCLUSIVE. No priority claim.',note_style)
    box=Table([[scope]],colWidths=[doc.width])
    box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#f0f3f5')),
        ('BOX',(0,0),(-1,-1),.4,colors.HexColor('#bcc7ce')),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.extend([box,Spacer(1,8),Paragraph('Abstract',st['h2']),Paragraph(inline(ABSTRACT),st['body'])])
    story.extend(parse(md,st,doc.width))
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    provenance={
        'public_preprint_version':'1.0','client_publication_date':'2026-10-26',
        'doi':DOI,'audited_candidate':'0.5','proof_body_sha256':hashlib.sha256(proof).hexdigest(),
        'msf_body_sha256':hashlib.sha256(msf).hexdigest(),
        'proof_body_verbatim_in_markdown':proof.decode() in md,
        'msf_body_verbatim_in_markdown':msf.decode() in md,
        'typesetting_changes':'Formatting only; added abstract, context, exact figure, audit notes and references.',
        'new_mathematical_theorem_or_verifier':False,
        'novelty':'INCONCLUSIVE','human_peer_review':'Not performed',
        'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest()
    }
    (ROOT/'publication/MANUSCRIPT_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print('PDF:',pdf)
    print('Proof body SHA256:',provenance['proof_body_sha256'])
    print('Both audited proof bodies reproduced verbatim in the Markdown source.')


if __name__=='__main__':
    main()
