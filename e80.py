
def find_xy(c, p):
    x = 0
    while (20*p + x) * x <= c: x += 1
    x -= 1
    return x, (20*p + x) * x

def sqrt(n):
    digits = []
    p = 0
    c = n
    while len(digits) < 100 and c != 0:
        x,y = find_xy(c, p)
        digits.append(x)
        p = p*10 + x
        c = (c - y) * 100

    return digits

def answer():
    irrational_sqrts = set(xrange(1,100))
    perfect_sqares = set(x**2 for x in xrange(1,10))
    irrational_sqrts.difference_update(perfect_sqares)
    return sum(sum(x) for x in map(sqrt, irrational_sqrts))

if __name__ == '__main__':
    print answer()
    
