combos = dict()

def get_num_combos(n,r):
  if (n,r) not in combos:
    if r is 1:
      combos[(n,r)] = n
    else:
      combos[(n,r)] = sum(get_num_combos(x,r-1) for x in xrange(r-1,n))
  return combos[(n,r)]

def answer():
  totals = (get_num_combos(n,r) for n in xrange(1,101) for r in xrange(1,n+1))
  return sum(1 for x in totals if x > 1000000)

if __name__ == '__main__':
  print answer()
