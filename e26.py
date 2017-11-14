from decimal import setcontext, getcontext, Decimal, ExtendedContext

def get_decimal(p):
  setcontext(ExtendedContext)
  getcontext().prec = p
  return Decimal(1)

def get_str(n,p):
  d = get_decimal(p+1)
  str = (d/n).to_eng_string().split('.').pop()
  if str[0] == '0':
    if str[1] == '0':
      return str[2:-1]
    else:
      return str[1:-1]
  else:
    return str[:-1]

def primes(n):
  nroot = int(n**0.5)
  sieve = range(n+1)
  sieve[1] = 0
  for i in xrange(2, nroot+1):
    if sieve[i] != 0:
      m = n/i - i
      sieve[i*i: n+1:i] = [0] * (m+1)
  return [x for x in sieve if x]

def pattern_len(string):
  l = len(string)/2
  while l > 2:
    if string[:l] == string[l:l+l]:
      return l
    l -= 1
  return string

def get_pattern_len(n,p=100):
  l = pattern_len(get_str(n,p))
  if type(l) is int:
    return l
  else:
    return get_pattern_len(n,p+100)

def answer():
  ps = primes(1000)[3:]
  l = 0
  a = 0
  for p in ps:
    n = get_pattern_len(p)
    if n > l:
      a = p
      l = n
  return a
