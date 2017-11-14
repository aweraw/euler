def add_digits(n,p):
  return int(n) == reduce(lambda x,y: x+int(y)**p,n,0)

def answer():
  return sum((x for x in xrange(100,354294) if add_digits(str(x),5)))

if __name__ == '__main__':
  print answer()
