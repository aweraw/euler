import math
from collections import namedtuple

point = namedtuple('point', ('x', 'y'))

def dist(a, b):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

count = 0
with open('triangles.txt') as f:
    for line in f:
        ax, ay, bx, by, cx, cy = (int(n) for n in line.strip().split(','))
        a, b, c = point(ax, ay), point(bx, by), point(cx, cy)
        ab, ac, bc = dist(a, b), dist(a, c), dist(b, c)
        ao, bo, co = math.hypot(ax, ay), math.hypot(bx, by), math.hypot(cx,cy)
        oab = math.acos((ao ** 2 + bo ** 2 - ab ** 2) / (2 * ao * bo))
        oac = math.acos((ao ** 2 + co ** 2 - ac ** 2) / (2 * ao * co))
        obc = math.acos((bo ** 2 + co ** 2 - bc ** 2) / (2 * bo * co))
        if math.isclose(oab + oac + obc, 2 * math.pi):
            count += 1

print(count)
