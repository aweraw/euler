from primes import primes

primes = [x for x in primes(10000) if x > 1000]

def group_permutations():
  intlists = [map(int,x) for x in map(str,primes)]
  for l in intlists: l.sort()
  inttups = map(tuple,intlists)
  pairs = zip(inttups,primes)

  perms_dict = dict()

  for pair in pairs:
    t,p = pair
    if t in perms_dict:
      perms_dict[t].append(p)
    else:
      perms_dict[t] = [p]

  return (x for x in perms_dict.itervalues() if len(x) > 2)

def check(l):
  if len(l) < 3:
    return False
  head = l[0]
  tail = l[1:]
  for perm in tail:
    diff = perm - head
    if perm + diff in tail:
      return (head,perm,perm+diff)
  return check(tail)

def answer():
  sols = [check(x) for x in group_permutations() if check(x)]
  return int(reduce(lambda x,y: x+y, map(str,sols[1])))

if __name__ == '__main__':
  print answer()
