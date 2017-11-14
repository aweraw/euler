from math import sqrt

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
  d = dict()
  d[1] = 1
  for i in xrange(2,10000):
    facts = factors(i)
    facts.pop()
    d[i] = sum(facts)
  pairs = []
  for k in d.keys():
    if d[k] < 10000 and d[d[k]] == k and d[k] != k:
      pairs.append(k)
  return sum(pairs)
