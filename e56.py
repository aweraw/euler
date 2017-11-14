def answer():
  print max(sum(int(z) for z in str(x**y)) for x in xrange(1,100) for y in xrange(1,100))

if __name__ == '__main__':
  print answer()
