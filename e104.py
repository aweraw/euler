from math import log10, ceil

def fibs():
    a, b, c = 0, 1, 1
    while True:
        yield b, c
        a, b, c = b, b + a, c + 1

tpt = 10**10

for fib, c in fibs():
    lst9 = set(str(fib % tpt))
    if len(lst9) == 9 and '0' not in lst9:
        fst9 = set(str(fib // 10**ceil(log10(fib) - 10)))
        if len(fst9) == 9 and '0' not in fst9:
            print(c)
            break
