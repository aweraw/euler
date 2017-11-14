from collections import defaultdict
from operator import add

def mk_triplets(i, n):
    s = set()
    c = range(1,10)
    if i is not 10: c.remove(i)
    for x in c:
        m = n - (i + x)
        if 10 > m > 0:
            if m in (i, x):
                continue
            else:
                s.add((i,x,m))
    return s

def mk_dict():
    d = defaultdict(set)
    for x in xrange(1,11):
        for y in xrange(13,19):
            d[y].update(mk_triplets(x,y))
    return d

def pairs(t,tset):
    return set(x for x in tset if t[2] is x[1])

def eliminate(t,tset):
    test = lambda x: not (x[0] in (t[1],t[2]) or 
                          t[0] in (x[1],x[2]) or 
                          t[0] is x[0] or
                          t[1] is x[1] or
                          t[2] is x[2])
    return set(x for x in tset if test(x))

def chain(t,tset):
    eset = eliminate(t,tset)
    if not tset or not eset:
        return [[t]]
    return [[t]+y for x in pairs(t,eset) for y in chain(x,eset)]

def mk_gon(tset):
    return [sort_gon(sorted(y)) for x in tset for y in chain(x,tset) if len(y) > 4]

def concat(tset):
    return ''.join(str(x) for x in reduce(add, tset))

def sort_gon(gon):
    ngon = [gon[0]]
    while len(ngon) < 5:
        for x in gon[1:]:
            if ngon[-1][2] is x[1]:
                ngon.append(x)
    return ngon

def answer():
    gons = dict()
    d = mk_dict()
    for k in d:
        for gon in mk_gon(d[k]):
            gons[concat(gon)] = 1
    return max(x for x in gons.keys())

if __name__ == '__main__':
    print answer()
