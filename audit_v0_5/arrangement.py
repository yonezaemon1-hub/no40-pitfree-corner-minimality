"""Rational representatives of EVERY face of a clipped line arrangement.
Includes 2D cells, 1D faces, and 0D vertices. No floating-point sampling.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from terrain import neighbors


def normalize(a, b, c):
    d = gcd(gcd(abs(a), abs(b)), abs(c))
    a, b, c = a//d, b//d, c//d
    if a < 0 or (a == 0 and b < 0):
        a, b, c = -a, -b, -c
    return a, b, c


def value(line, p):
    a, b, c = line
    return a*p[0]+b*p[1]+c


def inside(p, box, strict=False):
    alo, ahi, blo, bhi = box
    if strict:
        return alo < p[0] < ahi and blo < p[1] < bhi
    return alo <= p[0] <= ahi and blo <= p[1] <= bhi


def representatives(grid, box):
    """See ARRANGEMENT_CERTIFICATE.md for the coverage proof."""
    alo, ahi, blo, bhi = box
    corners = ((alo, blo), (alo, bhi), (ahi, blo), (ahi, bhi))
    shape = len(grid), len(grid[0])
    lines = set()
    for r, row in enumerate(grid):
        for c in range(len(row)):
            candidates = ((r, c),) + neighbors(shape, (r, c))
            for (r1, c1), (r2, c2) in combinations(candidates, 2):
                line = normalize(c1-c2, r1-r2, grid[r1][c1]-grid[r2][c2])
                signs = [value(line, p) for p in corners]
                if min(signs) <= 0 <= max(signs):
                    lines.add(line)
    # The four box sides also take part in face decomposition.
    for coef, edge in ((0, alo), (0, ahi), (1, blo), (1, bhi)):
        num, den = edge.numerator, edge.denominator
        lines.add((den, 0, -num) if coef == 0 else (0, den, -num))
    lines = tuple(sorted(lines))
    vertices = set(corners)
    for p, q in combinations(lines, 2):
        a, b, c = p
        d, e, f = q
        det = a*e-b*d
        if det:
            point = (F(b*f-c*e, det), F(c*d-a*f, det))
            if inside(point, box):
                vertices.add(point)
    cells = {}

    def add(point, dimension):
        signature = tuple((v > 0)-(v < 0) for v in (value(l, point) for l in lines))
        if signature in cells:
            assert cells[signature][0] == dimension
        else:
            cells[signature] = dimension, point

    for point in sorted(vertices):
        add(point, 0)
    for line in lines:
        points = sorted(p for p in vertices if value(line, p) == 0)
        for p, q in zip(points, points[1:]):
            middle = ((p[0]+q[0])/2, (p[1]+q[1])/2)
            add(middle, 1)
            normal = line[0], line[1]
            epsilon = F(1)
            for other in lines:
                val = value(other, middle)
                speed = other[0]*normal[0]+other[1]*normal[1]
                if val and speed:
                    epsilon = min(epsilon, abs(val/speed)/2)
            for sign in (-1, 1):
                candidate = (middle[0]+sign*epsilon*normal[0], middle[1]+sign*epsilon*normal[1])
                if inside(candidate, box, strict=True):
                    assert all(value(other, candidate) for other in lines)
                    add(candidate, 2)
    records = [(dim, p, signature) for signature, (dim, p) in cells.items()]
    records.sort(key=lambda item: (item[0], item[1], item[2]))
    return lines, records
