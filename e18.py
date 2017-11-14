class node:
  def __init__(self,n):
    self.value = n
    self.left = None
    self.right = None
    self.bestroute = None

def init_tree():
  lines = open('18.txt').read().splitlines()
  tree = []
  for line in lines:
    tree.append([node(int(x)) for x in line.split()])
  return tree

def set_routes(node):
  if node.left is None:
    node.bestroute = node.value
    return node.bestroute
  if node.left.bestroute is None:
    set_routes(node.left)
  if node.right.bestroute is None:
    set_routes(node.right)
  node.bestroute = node.value + max(node.left.bestroute,node.right.bestroute) 

def build_tree():
  tree = init_tree()
  numrows = len(tree)
  for row in xrange(numrows):
    if (row+1) is numrows:
      continue
    for i in xrange(len(tree[row])):
      tree[row][i].left = tree[row+1][i]
      tree[row][i].right = tree[row+1][i+1]
  set_routes(tree[0][0])
  return tree[0][0]

def answer():
  return build_tree().bestroute

def answer2():
  lines = map(str.split, open('18.txt').readlines())
  i = len(lines) - 2
  totals = map(int, lines[i+1])
  while i >= 0:
    line = map(int, lines[i])
    totals = [max(x) for x in zip((sum(x) for x in zip(line,totals)),(sum(x) for x in zip(line,totals[1:])))]
    i -= 1
  return totals[0]
