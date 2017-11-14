from math import log10

def numsdivs():
  a,b = 3,2
  x,y = 7,5
  for i in xrange(998):
    a,b,x,y = x, y, (a + 2 * x), (b + 2 * y)
    yield x,y

def answer():
  score = 0
  for num,div in divsnums():
    if int(log10(num)) > int(log10(div)):
      score += 1
  return score

if __name__ == '__main__':
  print answer()
