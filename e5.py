from primes import prime_factors

def answer():
  # get primes factorization of 2 -> 20
  pfzns = map(prime_factors, xrange(2,21))
  # find the unique primes in all prime factorizations
  unique_primes = list(set(reduce(lambda x,y: x+y, pfzns)))
  # get the largest number of each prime in any prime factorization
  counts = map(max, (map(lambda x: x.count(y), pfzns) for y in unique_primes))
  # return the product of all unique primes to the power of their largest count
  return reduce(lambda x,y: x*y, map(lambda x: x[0]**x[1], zip(unique_primes,counts)))

