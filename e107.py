#
# https://en.wikipedia.org/wiki/Minimum_spanning_tree
# https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm
# https://en.wikipedia.org/wiki/Prim%27s_algorithm
#

from heapq import heappop, heappush

class Network:
    def __init__(self, graph_table) -> None:
        self.nodes = set(range(len(graph_table)))
        self.edges = set()
        for i, node in enumerate(graph_table):
            for j, cost in enumerate(node):
                edge = (cost, (i, j) if i < j else (j, i))
                if cost: self.edges.add(edge)

    def connected_edges(self, n) -> set:
        return set(e for e in self.edges if n in e[1])

    def minimal_spanning_tree(self) -> dict[str, set]:
        heapq = list()
        tree = {
            'nodes': set(),
            'edges': set()
        }

        first_edge = min(self.edges)

        (_, (a, b)) = first_edge
        tree['nodes'].add(a)
        tree['nodes'].add(b)
        tree['edges'].add(first_edge)
        for e in self.connected_edges(a).union(self.connected_edges(b)):
            if e not in tree['edges']:
                heappush(heapq, e)

        while tree['nodes'] != self.nodes:
            next_edge = heappop(heapq)
            try:
                next_node = set(next_edge[1]).difference(tree['nodes']).pop()
            except:
                # we popped from an empty set
                # the edge connected nodes already in the tree, skip
                continue
            tree['nodes'].add(next_node)
            tree['edges'].add(next_edge)
            for e in self.connected_edges(next_node):
                if e not in tree['edges'] and e not in heapq:
                    heappush(heapq, e)

        return tree

with open('network.txt') as file:
    network = [[int(n) if n.isdigit() else None for n in line.split(',')] for line in file]

# network = [
#     [None, 16, 12, 21, None, None, None],
#     [16, None, None, 17, 20, None, None],
#     [12, None, None, 28, None, 31, None],
#     [21, 17, 28, None, 18, 19, 23],
#     [None, 20, None, 18, None, None, 11],
#     [None, None, 31, 19, None, None, 27],
#     [None, None, None, 23, 11, 27, None]
# ]

def answer():
    n = Network(network)
    mst = n.minimal_spanning_tree()
    return sum(cost for cost, _ in n.edges) - sum(cost for cost, _ in mst['edges'])
