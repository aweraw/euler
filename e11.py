def get_text():
  return open('11.txt').read()

def get_hlines(text=None):
  if text is None:	
    text = get_text()
  lines = []
  for line in text.splitlines():
    linearr = line.split()
    lines.append(map(lambda x: int(x), linearr))
  return lines

def get_vlines(text=None):
  lines = get_hlines(text)
  vlines = []
  for i in xrange(20):
     vline = []
     for j in xrange(20):
       vline.append(lines[j][i])
     vlines.append(vline)
  return vlines

class vec:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __add__(self,v):
    return vec(self.x+v.x, self.y+v.y)
  def __eq__(self,v):
    return self.x is v.x and self.y is v.y
  def __ne__(self,v):
    return self.x is not v.x or self.y is not v.y

def get_diagonals(lines):
  left = [vec(0,x) for x in xrange(20)]
  left.pop()
  bottom = [vec(x,19) for x in xrange(20)]
  sps = left + bottom
  
  top = [vec(x,0) for x in xrange(20)]
  top.pop()
  right = [vec(19,x) for x in xrange(20)]
  eps = top + right
  
  dvecs = zip(sps,eps)
  ulvec = vec(1,-1)
  diags = []
  
  for sp,ep in dvecs:
    if sp==ep:
      diag = [lines[sp.y][sp.x]]
    else:
      diag = []
      while sp!=ep:
        diag.append(lines[sp.y][sp.x])
        sp += ulvec
      diag.append(lines[ep.y][ep.x])
    diags.append(diag)
  return [line for line in diags if len(line)>3]

def answer():
  text = get_text()
  hlines = get_hlines(text)
  vlines = get_vlines(text)
  all_lines = hlines + vlines + get_diagonals(hlines) + get_diagonals(vlines)

  prods = []
  for line in all_lines:
    length = len(line)
    i = 0
    while i+4 <= length:
      prods.append(reduce(lambda x,y: x*y, line[i:i+4]))
      i += 4
  return max(prods)

print answer()
