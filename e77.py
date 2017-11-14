from itertools import takewhile
from primes import primes

plist = primes(100)
pset = set(plist)

golbach = dict()

def partitions(n):

    if n in golbach:
        return golbach[n]

    primes = takewhile(lambda x: x < n, plist)
    parts = ((p,n-p) for p in primes)


    gparts = set()
    for s,l in parts:
        if l in pset:
            gparts.add((s,l))
        else:
            for p in partitions(l):
                gparts.add((s,) + tuple(sorted(p)))

    golbach[n] = sorted(set(tuple(sorted(x)) for x in gparts))

    return golbach[n]

def answer():

    for x in xrange(4,101):
        if len(partitions(x)) > 5000:
            return x

if __name__ == '__main__':
    print answer()
    
