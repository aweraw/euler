from random import randint
from mr_prime import MillerRabin


def primes(n):
    nroot = int(n**0.5)
    sieve = list(range(n+1))
    sieve[1] = 0

    for i in range(2, nroot+1):
        if sieve[i] != 0:
            m = int(n/i) - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    return [x for x in sieve if x]


def get_primes(n):
    return primes(n)


def is_prime(n):
    return MillerRabin(n)


ps = primes(1000000)

pfs_dict = dict()
pfs_dict[1] = []


def prime_factors(n):
    try:
        return pfs_dict[n]
    except:
        limit = int(n**0.5)+1
        pfs = list()
        product = 1
        i = 0
        while ps[i] < limit:
            if n % ps[i] == 0:
                pfs.append(ps[i])
                product *= ps[i]
            i += 1
        if len(pfs) == 0:
            pfs_dict[n] = [n]
        else:
            pfs_dict[n] = pfs + prime_factors(n/product)
        return pfs_dict[n]
