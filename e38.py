def answer():
  pds = list()
  for n in xrange(9000,10000):
    pd = str()
    i = 1
    while len(pd) < 9:
      pd += str(n*i)
      i += 1
    if len(set(pd))==len(pd)==9 and '0' not in pd:
      pds.append(int(pd))
  return max(pds)
