from primes import primes

ps = primes(5000)

def ptest(n):
  nroot = int(n**0.5)
  i = 0
  while ps[i] <= nroot:
    if n % ps[i] is 0:
      return False
    i += 1
  return True

def get_seq(offset=0,limit=0):
  if limit is 0:
    while sum(ps[offset:limit]) < 1000000:
      limit += 1
    limit -= 1
  s = sum(ps[offset:limit])
  if ptest(s):
    return s
  else:
    if s + ps[limit] < 1000000:	
      return get_seq(offset,limit+1)
    else:
      return get_seq(offset+1,limit)

if __name__ == '__main__':
  print get_seq()
