def collatz(n,cm):
    if n not in cm:
        d,m = divmod(n,2)
        if m == 0:
            cn = d
        else:
            cn = n * 3 + 1
        collatz(cn,cm)
        cm[n] = 1 + cm[cn]
    return cm[n]

def collatzMap(n):
    cmap = {1:1}
    for i in xrange(2,n):
        collatz(i, cmap)
    return cmap

def answer():
    return reduce(lambda x, y: x if x[1] > y[1] else y, collatzMap(1000000).iteritems())[0]

if __name__ == '__main__':
    print answer()
