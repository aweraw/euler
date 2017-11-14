class node:
  def __init__(self,n):
    self.value = n
    self.right = None
    self.down = None
    self.minroute = None

def set_route(node):
  if not node.right and not node.down:
    node.minroute = node.value
  elif not node.right and node.down:
    if not node.down.minroute:
      set_route(node.down)
    node.minroute = node.value + node.down.minroute
  elif node.right and not node.down:
    if not node.right.minroute:
      set_route(node.right)
    node.minroute = node.value + node.right.minroute
  else:
    if not node.down.minroute:      
      set_route(node.down)
    if not node.right.minroute:
      set_route(node.right)
    node.minroute = node.value + min(node.right.minroute,node.down.minroute)

def get_matrix():
  text = open('matrix.txt')
  matrix = []
  for line in text:
    matrix.append([node(int(x)) for x in line.split(',')])
  for row in range(len(matrix)):
    for i in range(len(matrix[row])):
      try:
        matrix[row][i].right = matrix[row][i+1]
      except IndexError:
        pass
      try:
        matrix[row][i].down = matrix[row+1][i]
      except IndexError:
        pass
  set_route(matrix[0][0])
  return matrix[0][0]

print get_matrix().minroute
