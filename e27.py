from primes import primes

ps = primes(150000)
r = [x for x in ps if x < 1000]
pairs = ((a,b) for a in (-x for x in r) for b in r)

def get_prime_seq_len(a,b):
  n = 0
  while (n**2+a*n+b) in ps:
    n += 1
  return n

def answer():
  seqlen = 0
  pair = (0,0)
  for (a,b) in pairs:
    l = get_prime_seq_len(a,b)
    if l > seqlen:
      seqlen = l
      pair = (a,b)
  return pair
