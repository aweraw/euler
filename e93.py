from operator import add, sub, mul, truediv
from itertools import permutations


def int_sets():
    return ((a, b, c, d)
            for a in range(1, 10)
            for b in range(a + 1, 10)
            for c in range(b + 1, 10)
            for d in range(c + 1, 10))


def op_sets():
    ops = (add, sub, mul, truediv)
    return ((a, b, c)
            for a in ops
            for b in ops
            for c in ops)


# there are 2 ways to arrange 3 nodes in an ast
# root node with 2 children - binary
# root node has 1 child with 1 child - linear

def ast_linear(ints, ops):
    a, b, c, d = ints
    m, n, o = ops
    return float(m(n(o(a, b), c), d))


def ast_bin(ints, ops):
    a, b, c, d = ints
    m, n, o = ops
    return float(m(n(a, b), o(c, d)))


def score(nums):
    c = 0.0
    while c + 1 in nums:
        c += 1
    return c


scores = dict()

for ints in int_sets():
    evaluations = set()
    for p in permutations(ints):
        for ops in op_sets():
            evaluations.add(ast_linear(p, ops))
            evaluations.add(ast_bin(p, ops))
    scores[ints] = score(evaluations)

best = 0
winner = (1, 2, 3, 4)

for s in scores:
    if scores[s] > best:
        best = scores[s]
        winner = s

print(''.join(str(n) for n in winner))
