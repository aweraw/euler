
def next_pair(p):
    a, b = p
    c = (a[0]+b[0], a[1]+b[1])
    return (c, (c[0]+a[0], c[1]+a[1]))

def gen_pairs():
    p = (2, 3), (3, 4)
    yield p
    while True:
      p = next_pair(p)
      yield p

def answer():
    m = 1
    n = 1
    limit = 10**12
    for a, b in gen_pairs():
        if a[1]*m > limit:
            return max((a[0]*m, a[1]*m), (b[0]*n, b[1]*n))[0]
        n, m = a

if __name__ == '__main__':
    print answer()
