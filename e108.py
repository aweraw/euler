
def yValueFunc(n: int):
    return lambda x: (n * x) / (x - n)

def solutionsFor(n: int):
    yFunc = yValueFunc(n)
    pairs = ((x, yFunc(x)) for x in range(n+1, (2*n)+1))
    return list(filter(lambda p: p[1] == int(p[1]), pairs))

