from __future__ import division
from primes import primes, prime_factors

def totient_list(n):
    tlist = range(n+1)
    tlist[:2] = [0,0]
    for p in primes(n):
        tlist[p] = p-1
        m = 2
        i = p*m
        while i <= n:
            tlist[i] *= (p-1)/p
            m += 1
            i = p*m
    return tuple(int(0.5+x) for x in  tlist)

def totient(n):
    pfs = prime_factors(n)
    upfs = set(pfs)
    t = 1
    for pf in upfs:
        t *= (pf - 1) * pf**(pfs.count(pf)-1)
    return t
