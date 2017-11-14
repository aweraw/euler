def get_grid(n):
  row = n+1
  grid = []
  i = 1
  while i <= row:
    grid.append(map(lambda x: 0, range(row)))
    i += 1
  return grid

def get_node(grid,x,y):
  max_i = len(grid)-1
  if x is max_i or y is max_i:
    grid[y][x] = 1
    return 1
  if grid[y][x] is 0:
    if grid[y+1][x] is 0:
      left = get_node(grid,x,y+1)
    else:
      left = grid[y+1][x]
    if grid[y][x+1] is 0:
      down = get_node(grid,x+1,y)
    else:
      down = grid[y][x+1]
    grid[y][x] = left + down
  return grid[y][x]

def answer(n=20):
  grid = get_grid(n)
  get_node(grid,0,0)
  return grid[0][0]

print answer()
