from collections import defaultdict

def dice(s,n):
    die = range(1,s+1)
    rolls = (sum(t) for t in combos(s, n))
    probs = defaultdict(int)
    for x in rolls: probs[x] += 1
    r = float(s**n)
    for k in probs: probs[k] /= r
    return dict(probs.items())

def combos(n, m, g=None):
    if m < 1:
        return g
    if not g:
        g = ((x,) for x in xrange(1,n+1))
        return combos(n, m-1, g)
    return combos(n, m-1, (t+(x,) for t in g for x in xrange(1,n+1)))

def board():
    b = defaultdict(list)
    d = dice(6,2)
    for n in xrange(40):
        b[n] = d.values()
        
    # g2j
    b[10].extend(b[30])
    b[30] = [0]
    
    return b

