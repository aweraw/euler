from math import log10

def num_digits(n):
  return int(log10(n))

def list_digits(n):
  ndigits = num_digits(n)
  while ndigits > 0:
    d,n = divmod(n,10**ndigits)
    ndigits -= 1
    yield d
  yield n
