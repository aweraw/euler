from itertools import count

def pentagonal(n):
    return n*(3*n-1)/2

def generalised_pentagonal(n):
    if n < 0: return 0    
    if n%2 == 0: return pentagonal(n/2+1)
    else: return pentagonal(-(n/2+1))

def partitions():
    pt = [1]

    for n in count(1):
        r = 0
        f = -1
        i = 0
        k = generalised_pentagonal(i)
        while k <= n:
            if i%2==0: f = -f
            r += f*pt[n - k]
            i += 1
            k = generalised_pentagonal(i)
        pt.append(r)
        yield r

def answer():
    c = 1
    for x in partitions():
        if x % 1000000 == 0:
            return c
        c += 1

if __name__ == '__main__':
    print answer()
