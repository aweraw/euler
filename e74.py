import operator
from digits import list_digits

def factorial(n):
    if n is 0:
        return 1
    return reduce(operator.mul, xrange(1, n+1))

chains = dict()
fdict = dict((x,factorial(x)) for x in xrange(10))

def gen_chain_len(n):
    if n in (1, 2, 145, 40585):
        return 1
    if n in (871, 872, 45361, 45362):
        return 2
    if n in (169, 1454, 363601):
        return 3
    if n in chains:
        return chains[n]
    dfsum = sum(fdict[x] for x in list_digits(n))
    chains[n] = 1 + gen_chain_len(dfsum)
    return chains[n]

def answer():
    c = 0
    for x in xrange(1,1000000):
        if gen_chain_len(x) is 60:
            c += 1
    return c

if __name__ == '__main__':
    print answer()
