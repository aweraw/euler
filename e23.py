import sys
from math import sqrt
from numberlib import abundants

numbers = open('e23.txt').read().split()
for n in xrange(1,20162):
  i = 0
  q = True
  while abundants[i] <= n/2:
    if (n-abundants[i]) in abundants[i:]:
      q = False
      break
    i += 1
  if q:
    sys.stdout.write(str(n)+" ")
    sys.stdout.flush()
    numbers.append(n)
print    
print sum(numbers)
