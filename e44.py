from numberlib import Series
from itertools import count

def pentagonal(n):
    return n*(3*n-1)/2

def ipentagonal(n):
    return ((24*n+1)**0.5+1)/6

def is_pentagonal(n):
    p = ipentagonal(n)
    return p == int(p)

def next_pentagonal(n):
    return pentagonal(int(ipentagonal(n))+1)

pentagonals = Series(lambda x: True, next_pentagonal, 'pentagonals.pickle', [1])

def answer():
  for i in count(1):
    n = i - 1
    pi = pentagonals[i]
    last_diff = pentagonals[i] - pentagonals[i-1]
    while pentagonals[n] >= last_diff:
      pn = pentagonals[n]
      if is_pentagonal(pi-pn) and is_pentagonal(pi+pn):
        return abs(pn-pi)
      n -= 1
