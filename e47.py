from primes import primes

ps = primes(1000000)

pfs_dict = dict()
pfs_dict[1] = []

def prime_factors(n):
  try:
    return pfs_dict[n]
  except:
    limit = int(n**0.5)+1
    pfs = list()
    product = 1
    i = 0
    while ps[i] < limit:
      if n % ps[i] is 0:
        pfs.append(ps[i])
        product *= ps[i]
      i += 1
    if len(pfs) is 0:
      pfs_dict[n] = [n]
    else:
      pfs_dict[n] = pfs + prime_factors(n/product)
    return pfs_dict[n]

def prime_factorization(n):
  pfzn = prime_factors(n)
  pfs = set(pfzn)
  return [(x,pfzn.count(x)) for x in pfs]

def flatten(seq):
  fseq = list()
  for i in seq:
      fseq += i
  return fseq

def find():
  i = 2
  while True:
    pfzn = prime_factorization(i)
    if len(pfzn)==4:
      next3 = map(prime_factorization, range(i+1,i+4))
      npfs = map(len,next3)
      upfs = set(pfzn+flatten(next3))
      if npfs==[4]*3 and len(upfs)==16:
        return [pfzn]+next3
      try:
        i += npfs.index(4)
      except ValueError:
        i += 3
    i += 1

def answer():
  a = find()
  return reduce(int.__mul__, map(lambda x: x[0]**x[1], a[0]))

if __name__ == '__main__':
  print answer()
