pdict = dict()

def partitions(k,n):
    if (k,n) in pdict:
        return pdict[(k,n)]

    if k > n:
        return 0
    elif k is n:
        return 1
    pdict[(k,n)] = partitions(k+1,n) + partitions(k,n-k)
    return pdict[(k,n)]

def answer():
    return partitions(1,100) - 1

if __name__ == '__main__':
    print answer()
