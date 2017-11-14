from math import log10

def answer():
  return sum(1 for x in xrange(1,10) for y in xrange(1,22) if int(log10(x**y)) == y-1)

if __name__ == '__main__':
  print answer()
