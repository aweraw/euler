from permutation import perm_n

string = '0123456789'
primes = [2,3,5,7,11,13,17]

def parts(string):
  ps = list()
  i = 1
  while i+3 <= 10:
    ps.append(int(string[i:i+3]))
    i += 1
  return ps

def answer():
  num_perms = reduce(lambda x,y: x*y, xrange(1,len(string)+1))
  sum = 0
  for n in xrange(num_perms):
    perm = ''.join(perm_n(string,n))
    if all((part % prime)==0 for part,prime in zip(parts(perm),primes)):
      sum += int(perm)
  return sum
