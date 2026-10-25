"""Exact D4 routing. Python 3.12+, standard library only."""
from fractions import Fraction as F


def neighbors(shape, v):
    nr, nc = shape
    r, c = v
    return tuple((rr, cc) for rr, cc in
                 ((r-1, c), (r, c-1), (r, c+1), (r+1, c))
                 if 0 <= rr < nr and 0 <= cc < nc)


def global_routes(grid, a, b):
    """Implementation A: global heights, sorting and dynamic programming.
    Ties use increasing (row, column), independent of parameters.
    """
    shape = len(grid), len(grid[0])
    heights = {(r, c): F(h) + a*c + b*r
               for r, row in enumerate(grid) for c, h in enumerate(row)}
    successor, terminal = {}, {}
    for v in heights:
        lower = [w for w in neighbors(shape, v) if heights[w] < heights[v]]
        successor[v] = min(lower, key=lambda w: (heights[w], w)) if lower else v
    for v in sorted(heights, key=lambda v: (heights[v], v)):
        w = successor[v]
        terminal[v] = v if w == v else terminal[w]
    return successor, terminal


def local_walk(grid, source, a, b):
    """Implementation B: direct local drops and path traversal.
    Does not call global_routes, neighbors, or the global-height DP.
    """
    nr, nc = len(grid), len(grid[0])
    path = [source]
    r, c = source
    for _ in range(nr*nc):
        options = []
        for rr, cc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= rr < nr and 0 <= cc < nc:
                drop = F(grid[rr][cc])-F(grid[r][c])+a*(cc-c)+b*(rr-r)
                if drop < 0:
                    options.append((drop, rr, cc))
        if not options:
            return tuple(path)
        _, r, c = min(options)
        assert (r, c) not in path, 'Strict-descent cycle'
        path.append((r, c))
    raise AssertionError('Path exceeds the number of cells')


def permanent_sink_set(grid, box):
    """Exact check that the sink set is the same throughout a closed box.
    Sink-feasibility at a D4 vertex is an axis-aligned rectangle of tilts.
    Returns (permanent strict sinks, vertices that can ever be sinks).
    """
    alo, ahi, blo, bhi = box
    shape = len(grid), len(grid[0])
    permanent, possible = set(), set()
    for r, row in enumerate(grid):
        for c, h in enumerate(row):
            v = r, c
            lows, highs = [alo, blo], [ahi, bhi]
            strict = True
            for rr, cc in neighbors(shape, v):
                dc, dr = cc-c, rr-r
                offset = F(grid[rr][cc])-F(h)
                minimum = offset + (alo if dc > 0 else ahi)*dc + (blo if dr > 0 else bhi)*dr
                strict &= minimum > 0
                axis, coef = (0, dc) if dc else (1, dr)
                threshold = -offset/coef
                if coef > 0:
                    lows[axis] = max(lows[axis], threshold)
                else:
                    highs[axis] = min(highs[axis], threshold)
            if strict:
                permanent.add(v)
            if lows[0] <= highs[0] and lows[1] <= highs[1]:
                possible.add(v)
    return permanent, possible
