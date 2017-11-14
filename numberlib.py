from math import sqrt
import cPickle

class Primes():
  def __init__(self):
    try:
      self.primes = cPickle.load(open('primes.pickle'))
    except IOError:
      self.primes = [2,3]
    self.startlen = len(self.primes)

  def isPrime(self,n):
    i = 1
    while self.primes[i] <= sqrt(n):
      if (n % self.primes[i]) is 0:
        return False
      i += 1
    return True

  def pickle(self):
    if self.startlen < len(self.primes):
      cPickle.dump(self.primes, open('primes.pickle','w+'))
      return "saved"
    else:
      return "no point saving. no new primes"

  def __contains__(self,n):
    i = 0
    while self.primes[i] < n:
      i += 1
    return self.primes[i] == n

  def __getitem__(self,i):
    try:
      return self.primes[i]
    except IndexError:
      next = self[-1] + 2
      need = i - (len(self.primes)-1)
      for x in xrange(need):
        while not self.isPrime(next):
          next += 2
        self.primes.append(next)
        next += 2
      return self.primes[i]

primes = Primes()

def primeFactors(n):
  if n&1:
    limit = n / 3
  else:
    limit = n / 2  
  i = 0
  factors = []
  while primes[i] <= limit:
    if n % primes[i] is 0:
      factors.append(primes[i])
    i += 1
  return factors

def primeFactorization(n,pfs=None):
  if pfs is None:
    pfs = primeFactors(n)
  elif len(pfs) is 0:
    return []
  if (n % pfs[0]) is 0:
    return pfs[:1] + primeFactorization((n/pfs[0]),pfs)
  else:
    return primeFactorization(n,pfs[1:])

# http://mathforum.org/library/drmath/view/54350.html
def sumFactors(n):
  pfs = primeFactors(n)
  pfactorization = primeFactorization(n,pfs)
  total = 1
  for pf in pfs:
    sum = 1
    for i in xrange(pfactorization.count(pf)):
      sum = (sum * pf) + 1
    total *= sum
  return total - n

def isAbundant(n):
  return sumFactors(n) > n

def isDeficient(n):
  return sumFactors(n) < n

def isPerfect(n):
  return sumFactors(n) == n

def isPrime(n):
  i = 0
  while primes[i] <= sqrt(n):
    if (n % primes[i]) is 0:
      return False
    i += 1
  return True

class Series:
  def __init__(self,testfunc,nextfunc,filename,startwith):
    self.test = testfunc
    self.next = nextfunc
    self.filename = filename
    try:
      self.seq = cPickle.load(open(filename))
    except IOError:
      self.seq = startwith
    self.startlen = len(self.seq)

  def pickle(self):
    if self.startlen < len(self.seq):
      cPickle.dump(self.seq, open(self.filename,'w+'))
      return "saved"
    else:
      return "no point saving. no new terms"

  def __contains__(self,n):
    if n > self.seq[-1]:
      i = self.seq.index(self.seq[-1])
      while self.seq[i] < n:
        i += 1
        self.__getitem__(i)
    else:
      i = 0
      while self.seq[i] < n:
        i += 1
    return self.seq[i] == n

  def __getitem__(self,i):
    try:
      return self.seq[i]
    except IndexError:
      next = self.next(self[-1])
      need = i - (len(self.seq)-1)
      for x in xrange(need):
        while not self.test(next):
          next = self.next(next)
        self.seq.append(next)
        next = self.next(next)
      return self.seq[i]
  
  def __len__(self):
    return self.seq.__len__()

deficients = Series(isDeficient,lambda x: x+1,'deficient.pickle',[2])
abundants = Series(isAbundant,lambda x: x+1,'abundant.pickle',[12])
perfects = Series(isPerfect,lambda x: x+2,'perfect.pickle',[6])

def save():
  print "deficient numbers:", deficients.pickle()
  print "abundant numbers:", abundants.pickle()
  print "perfect numbers:", perfects.pickle()
  print "prime numbers:", primes.pickle()
