from primes import primes, is_prime
from digits import list_digits

ps = primes(1000000)

tdict = dict()

for p in ps:
  ds = map(str, list_digits(p))
  for d in set(ds):
    if ds.count(d) > 1:
      t = ''.join(ds)
      t = t.replace(d,'_')
      if t in tdict:
        tdict[t].append(p)
      else:
        tdict[t] = [p]

for k in tdict:
  if len(tdict[k]) >= 6:
    c = 0
    for n in xrange(1,10):
      if is_prime(int(k.replace('_',str(n)))):
        c += 1
    if c is 8:
      print min(map(lambda x: int(k.replace('_',str(x))), xrange(1,10)))
