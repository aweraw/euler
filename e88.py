
prod = lambda s: reduce(lambda x,y: x*y, s, 1)

def factor_combinations(limit):
    factors = [2,2]
    llen = 2
    while prod(factors) <= limit:
        yield factors
        factors[-1] += 1
        if prod(factors) > limit:
            for i in range(1, llen+1):
                if factors[-i] > limit**(1.0/i) / prod(factors[:-i]):
                    if i == llen:
                        # next power of 2
                        llen += 1
                        factors = [2 for x in xrange(llen)]
                    else:
                        factors[-(i+1)] += 1
                        factors[-i:] = [factors[-(i+1)] for x in xrange(len(factors[-i:]))]
                        if prod(factors) <= limit:
                            break

def answer(n=12000):
    ks_dict = {n:n*2 for n in range(2,n*2 + 1)}

    for combo in factor_combinations(n*2):
        p, s, l = prod(combo), sum(combo), len(combo)
        k = p - s + l
        if p < ks_dict[k]:
            ks_dict[k] = p

    valid = set(v for k,v in ks_dict.items() if k <= n)

    return sum(valid)