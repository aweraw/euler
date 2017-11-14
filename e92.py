
cycles = dict()

def crunch(n):
  try:
    return cycles[n]
  except:
    nn = sum(int(x)**2 for x in str(n))
    if nn in (1,89):
      cycles[n] = nn
    else:
      cycles[n] = crunch(nn)
    return cycles[n]

def init_cycles():
  for n in xrange(1,568):
    nn = sum(int(x)**2 for x in str(n))
    if nn in (1,89):
      cycles[n] = nn
    else:
      cycles[n] = crunch(nn)

def find(n):
  return cycles[sum(int(x)**2 for x in str(n))]

def answer():
  init_cycles()
  return sum(1 for x in xrange(568,10000000) if find(x) is 89) + cycles.values().count(89)
