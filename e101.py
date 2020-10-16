# https://en.wikipedia.org/wiki/Approximation_theory
# https://en.wikipedia.org/wiki/Lagrange_polynomial

from functools import reduce, partial
from operator import mul

def d10polynominal(n):
    return n**10 - n**9 + n**8 - n**7 + n**6 - n**5 + n**4 - n**3 + n**2 - n + 1

def polyPart(x, nx):
    def inner(n):
        return (n - nx) / (x - nx)
    return inner

def polyBasis(x, xset):
    def inner(n):
        return reduce(mul, (polyPart(x, nx)(n) for nx in xset), 1)
    return inner

def polyBasisFuncs(xs):
    return (polyBasis(x, set(xs).difference({x})) for x in xs)

def lagrangePolynomial(xs, ys):
    def inner(n):
        return sum(ce*bf(n) for ce, bf in zip(ys, polyBasisFuncs(xs)))
    return inner

xs = list(range(1, 11))
ys = [d10polynominal(x) for x in xs]

L_funcs = [lagrangePolynomial(xs[:n], ys[:n]) for n in xs]

answer = sum(lf(i + 2) for i, lf in enumerate(L_funcs))
print(answer)
