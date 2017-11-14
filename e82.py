from __future__ import with_statement

class Node:
  
    def __init__(self,val):
        self.value = int(val)
        self.up = None
        self.right = None
        self.down = None
        self.bestroute = None
    
    def set_route(self):
        snodes = list()        
        
        try:
            if self.up.bestroute:
                snodes.append(self.up.bestroute)
        except AttributeError:
            pass
        try:
            if self.right.bestroute:
                snodes.append(self.right.bestroute)
        except AttributeError:
            pass
        try:
            if self.down.bestroute:
                snodes.append(self.down.bestroute)
        except AttributeError:
            pass
        
        self.bestroute = min(snodes) + self.value
    
    def __repr__(self):
        if not self.bestroute:
            br = 0
        else:
            br = self.bestroute
        return "Node(%d,%d)" % (self.value, br)

def init_matrix():
    with open('matrix.txt') as m:
        matrix = [[Node(x) for x in line.split(',')] for line in m]
    for i in xrange(79):
        for j in xrange(80):
            matrix[j][i].right = matrix[j][i+1]
    for i in xrange(1,79):
        matrix[0][i].down = matrix[1][i]
        matrix[79][i].up = matrix[78][i]
    for i in xrange(1,79):
        for j in xrange(1,79):
            matrix[j][i].up = matrix[j-1][i]
            matrix[j][i].down = matrix[j+1][i]
    return matrix

def set_routes(matrix):
    for hline in matrix:
        hline[-1].bestroute = hline[-1].value
    js = range(80)
    for i in range(1,79)[::-1]:
        for j in js:
            matrix[j][i].set_route()
        for j in js[::-1]:
            matrix[j][i].set_route()
    for j in xrange(80):
        matrix[j][0].set_route()

def answer():
    matrix = init_matrix()
    set_routes(matrix)
    return min(hline[0].bestroute for hline in matrix)

if __name__ == '__main__':
    print answer()
