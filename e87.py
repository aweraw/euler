from itertools import takewhile
from primes import primes

# all primes up to 7072, since it is the first square to exceed 50M
primes = primes(7072)

lt50M = lambda x: x < 50000000

def powers(n):
    return (b**n for b in primes)

def g(n,p):
    return takewhile(lt50M, (n+x for x in powers(p)))

def sums():
    for a in g(0,4):
        for b in g(a,3):
            for c in g(b,2):
                yield c

def answer():
    return len(set(x for x in sums()))

if __name__ == '__main__':
    print answer()
