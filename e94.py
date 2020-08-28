# https://en.wikipedia.org/wiki/Heronian_triangle

# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples

A = [[1, -2, 2],
     [2, -1, 2],
     [2, -2, 3]]

B = [[1, 2, 2],
     [2, 1, 2],
     [2, 2, 3]]

C = [[-1, 2, 2],
     [-2, 1, 2],
     [-2, 2, 3]]


def matrix_product(m1, m2): return [[sum(a * b for a, b in zip(row, col))
                                     for col in zip(*m2)]
                                    for row in m1]


def perimeter(t): return (min(t[0]) + max(t[0])) * 2


triple = [[3, 4, 5]]
ms = [C, A]
answer = 0

while perimeter(triple) <= 1000000000:
    answer += perimeter(triple)
    triple = zip(*matrix_product(ms[0], zip(*triple)))
    ms = ms[::-1]

print(answer)
