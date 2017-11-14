from continued_fractions import cf_sqrt, cf_fold, convergents
from math import sqrt

def mk_sqrt_convergent(sn):
  cf = cf_sqrt(sn)
  yield cf[0]
  i = 0
  while True:
    yield cf[1][i]
    i += 1
    if i == len(cf[1]):
      i = 0

def find_xy(n):
  g = mk_sqrt_convergent(n)
  for (x,y) in convergents(g):
      if x**2 - n*(y**2) == 1:
          return x,y

def non_sq():
  sqs = set([4])
  n = 3
  while n is not 32:
      sqs.add(n**2)
      n += 1
  return (x for x in set(xrange(2,1001)).difference(sqs))

def answer():
  return max((find_xy(x)[0],x) for x in non_sq())[1]

if __name__ == '__main__':
  print answer()
