from primes import primes, is_prime

ps = primes(10000)[1:]

def prime_pair(x,y):
  str_x = str(x)
  str_y = str(y)
  xy = int(str_x+str_y)
  yx = int(str_y+str_x)
  return is_prime(xy) and is_prime(yx)

pp = dict()

def pairs(n):
  if n in pp:
    return pp[n]

  i = ps.index(n) + 1
  pset = set()
  for x in ps[i:]:
    if prime_pair(n,x):
      pset.add(x)
  pp[n] = pset

  return pp[n]

def intersect(n,s):
  return pairs(n).intersection(s)

def chain_set(n,s):
  if not s:
    return [[n]]
  return [[n]+y for x in s for y in chain_set(x,intersect(x,s))]

def answer():
  for n in ps:
    chains = chain_set(n,pairs(n))
    chain_lens = [len(x) for x in chains]
    if max(chain_lens) is 5:
      return sum(chains[chain_lens.index(5)])

if __name__ == '__main__':
  print answer()
