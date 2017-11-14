from primes import prime_factors

def answer():
    return max(prime_factors(600851475143))

if __name__ == '__main__':
    print answer()
