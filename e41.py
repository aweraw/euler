from math import floor, sqrt
from primes import primes

def get_permutation(seq,n):
  seqlen = len(seq)
  if seqlen < 1:
    return ''
  numperms = reduce(int.__mul__, xrange(1,seqlen+1))
  groupsize = numperms / seqlen
  if n > numperms:
    return None
  i = int(floor(n / groupsize))
  new_n = n - (i * groupsize)
  return seq[i] + get_permutation(seq.replace(seq[i],''),new_n)

ps = primes(31427)

def is_prime(n):
  nroot = floor(sqrt(n))
  i = 0
  while ps[i] <= nroot:
    if n % ps[i]==0:
      return None
    i += 1
  return True

def answer(string='987654321'):
  fact = reduce(int.__mul__, xrange(1,len(string)))
  for n in xrange(fact):
    if is_prime(int(get_permutation(string,n))):
      return int(get_permutation(string,n))
  return answer(string[1:])
