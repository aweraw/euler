from primes import primes

ps = primes(1000000)

def triplets():
  i = 0
  while True:
    i += 2
    isq = i**2
    yield (isq + 1, (isq + 1) + i, isq - (i - 1))

def is_prime(n):
  nroot = int(n**0.5)
  i = 0
  while ps[i] <= nroot:
    if n % ps[i] is 0:
      return False
    i += 1
  return True

def answer():
  layers = 1
  diag_elems = 1.0
  num_primes = 0
  for triplet in triplets():
    layers += 1
    diag_elems += 4
    num_primes += sum(is_prime(n) for n in triplet)
    if num_primes / diag_elems < 0.1:
      return layers * 2 - 1
