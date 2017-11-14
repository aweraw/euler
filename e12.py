from math import sqrt

def trinum(n):
  return n*(n+1)/2

def divs_lt_sqrt(n):
  divs = []
  sqrtn = sqrt(n)
  i = 1
  while i <= sqrtn:
    if (n%i)==0:
      divs.append(i)
    i += 1
  return divs

def potential_factors(fs,n):
  pfs = []
  i = 0
  for d in fs:
    for f in fs[i:]:
      pfs.append(f*d)
    i += 1
  return list(set([x for x in pfs if x <= (n/2)]))

def factors(n,pfs=None):
  if pfs is None:
    pfs = potential_factors(divs_lt_sqrt(n),n)
  tfs = []
  for pf in pfs:
    tndiv, tnmod = divmod(n,pf)
    if tnmod is 0:
      tfs.append(pf)
      if pfs.count(tndiv) is 0:
        tfs.append(tndiv)
  tfs.sort()
  return tfs

def answer():
  i = 1
  while True:
    tn = trinum(i)
    i += 1
    ndivs = divs_lt_sqrt(tn)
    if len(ndivs) < 22:
      continue
    pfs = potential_factors(ndivs,tn)
    if len(pfs) < 500:
      continue
    tfs = factors(tn,pfs)
    if len(tfs) >= 500:
      return tn

# to find the number of divisors of the nth triangular number
# we can mulltiply the number of divisors of n and n/2
def better_answer():
  n = 2
  b = len(factors(n/2))
  while True:
    a = b
    if (n%2) is 0:
      b = len(factors(n+1))
    else:
      b = len(factors((n+1)/2))
    if a*b >= 500:
      return trinum(n)
    n += 1

print better_answer()
