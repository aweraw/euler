from heap import Heap
from operator import concat

import time

inf = float('infinity')

class Node:

    def __init__(self,v):
        self.value = float(v)
        self.cost = inf
        self.dest = None
        self.parent = None
        self.coords = None
        self.pathlen = 1
        self.neighbors = list()

def matrix(fn):
    m = [[Node(x) for x in line.split(',')] for line in open(fn)]

    # top left
    m[0][0].cost = m[0][0].value
    m[0][0].neighbors.extend([m[0][1],m[1][0]])
    m[0][0].coords = (0,0)
    # top right
    m[0][79].neighbors.extend([m[0][78],m[1][79]])
    m[0][79].coords = (79,0)
    # bottom left
    m[79][0].neighbors.extend([m[79][1],m[78][0]])
    m[79][0].coords = (0,79)
    # bottom right
    m[79][79].dest = True
    m[79][79].neighbors.extend([m[79][78],m[78][79]])
    m[79][79].coords = (79,79)
        
    # set edges
    for i in xrange(1,79):
        # top
        m[0][i].neighbors.extend([m[0][i-1],m[0][i+1],m[1][i]])
        m[0][i].coords = (i,0)
        # bottom
        m[79][i].neighbors.extend([m[79][i-1],m[79][i+1],m[78][i]])
        m[79][i].coords = (i,79)
        # left
        m[i][0].neighbors.extend([m[i-1][0],m[i+1][0],m[i][1]])
        m[i][0].coords = (0,i)
        # right
        m[i][79].neighbors.extend([m[i-1][79],m[i+1][79],m[i][78]])
        m[i][79].coords = (79,i)

        # set inner
        for j in xrange(1,79):
            node = m[i][j]
            node.neighbors.extend([m[i-1][j],m[i][j-1],m[i][j+1],m[i+1][j]])
            node.coords = (j,i)

    m = reduce(concat, m)
    return Heap([m[0]], key=lambda x: x.cost)
    #return Heap([m[0]], key=lambda x: (x.cost / x.pathlen) + x.value)

def answer():
    m = matrix('matrix.txt')
    visited = set()
    
    for n in m:
        for x in n.neighbors:
            if x.cost > (n.cost + x.value):
                x.cost = n.cost + x.value
                x.parent = n
                x.pathlen = n.pathlen + 1
                if x.dest:
                    return x.cost
                if x not in visited and x not in m:
                    m.push(x)
    
        visited.add(n)

if __name__ == '__main__':
    print answer()
    
