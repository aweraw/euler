
def children(triplet):
    a,b,c = triplet
    yield (a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c)
    yield (a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c)
    yield (-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)

def calc_num_perimeters(triplet, l, limit=1500000):
    s = sum(triplet)
    if s > limit: return None
    for i in xrange(s,limit,s): l[i] += 1
    for child in children(triplet): calc_num_perimeters(child, l)

def answer():
    l = [0]*1500000
    calc_num_perimeters((3,4,5),l)

    return sum(1 for i in xrange(1500000) if l[i] is 1)

if __name__ == '__main__':
    print answer()
