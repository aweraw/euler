def fact(n):
  return reduce(int.__mul__, xrange(1,n+1),1)

factorials = dict((str(n),fact(n)) for n in xrange(10))

def sumFactDigits(n):
  return sum(factorials[x] for x in str(n))

def answer():
  return sum(x for x in xrange(3,fact(10)+1) if x==sumFactDigits(x))

if __name__ == '__main__':
    print answer()
