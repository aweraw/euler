from itertools import count
from math import log10

def cf_fold(cf):
    cf = cf[:]
    d = cf.pop()
    n = 1
    while cf:
        n, d = d, cf.pop() * d + n
    return d,n

def e_cf():
    yield 2
    yield 1
    for n in count(1):
      yield 2*n
      yield 1
      yield 1

def answer():
    e = e_cf()
    e = [e.next() for x in xrange(100)]
    n = cf_fold(e)[0]
    m = 10**int(log10(n))
    total = 0
    while m:
        x, n = divmod(n,m)
        m /= 10
        total += x
    return total

if __name__ == '__main__':
    print answer()
