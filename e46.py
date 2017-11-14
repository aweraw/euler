from primes import primes

p = primes(10000)
ocs = set(x for x in xrange(9,10000,2) if x not in p)
sums = set(dsq+prime for prime in p for dsq in (2*(x**2) for x in xrange(100)))

print ocs.difference(sums)
