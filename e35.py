from primes import primes

def get_candidates():
  digits = set('1379')
  ps = primes(1000000)
  return [2,5]+[p for p in ps if set(str(p)).issubset(digits)]

def get_rotations(n):
  str_n = str(n)
  rotations = list([n])
  for i in xrange(len(str_n)-1):
    str_n = str_n[1:]+str_n[:1]    
    rotations.append(int(str_n))
  return rotations

def answer():
  candidates = get_candidates()
  circular = list()
  for c in candidates:
    c_rotations = get_rotations(c)
    i = 0
    for cr in c_rotations:
      if cr in candidates:
        i += 1
    if i == len(c_rotations):
      circular.append(c)
  return len(circular)
