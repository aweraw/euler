
def _combos(n,m):
  if m <= 1:
    return [(1,)*n]
  if n is 0:
    return [()]
  return [(x,)+y for x in xrange(1,n+1) for y in _combos(n-x,x) if y == () or max(y) <= x]

def combos(n):
  c = _combos(n,n)
  c.pop()
  return c

def ilen(seq):
  c = 0
  for x in seq: c += 1
  return c

def answer(n=100):
  return ilen(combos(n,n)) - 1
