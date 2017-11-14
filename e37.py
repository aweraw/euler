from primes import primes

fdigits = ['2','3','5','7']
ldigits = ['3','7']
mdigits = set(['1','3','7','9'])

ps = primes(1000000)

def is_cadidate(p):
  str_p = str(p)
  return str_p[0] in fdigits \
     and str_p[-1] in ldigits \
     and mdigits.issuperset(set(str_p[1:-1]))

def candidates():
  return (x for x in ps if is_cadidate(x))

def trunc_l2r(prime):
  i = 1
  sects = list()
  while len(prime[i:]) > 0:
    sects.append(prime[i:])
    i += 1
  return map(int,sects)

def trunc_r2l(prime):
  i = 1
  sects = list()
  while len(prime[:-i]) > 0:
    sects.append(prime[:-i])
    i += 1
  return map(int,sects)

def is_prime(n):
  return n in ps

def answer():
  matches = list()
  for p in candidates():
    str_p = str(p)
    ptest = map(is_prime, trunc_l2r(str_p)+trunc_r2l(str_p))
    if all(ptest) and p > 7:
      matches.append(p)
      if len(matches)==11:
        break
  return sum(matches)
