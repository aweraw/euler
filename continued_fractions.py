from math import sqrt

def gcd(n,m):
  while m != 0: n,m = m, n % m
  return n

def lcm(n,m):
  return (n / gcd(n,m)) * m

def cf_ratio(n,d):
  cf = list()
  while d != 0:
    x,nd = divmod(n,d)
    cf.append(x)
    n,d = d,nd
  return cf

def cf_decimal(n):
  cf = [0]
  n = 1 / n
  while n < 4294967296:
    cf.append(int(n))
    if n - cf[-1] == 0 or len(cf) > 100:
      break
    n = 1 / (n - cf[-1])
  return cf

def cf_sqrt(n):
    cf = list()
    sn = sqrt(n)
    numerator = 1  
    denominator = 0
    constant = int(sn)

    cf.append(constant)
  
    if sn == constant:
        denominator = 1

    while denominator != 1:
        #simplified denominator
        denominator = (n - constant**2) / numerator
        #next digit in period
        x = (cf[0] + constant) / denominator
        cf.append(x)
        constant = -(constant - (denominator*x))
        numerator = denominator
  
    return cf[0],cf[1:]

def cf_fold(cf):
    cf = cf[:]
    d = cf.pop()
    n = 1
    while cf:
        n, d = d, cf.pop() * d + n
    return d,n

def reduce_ratio(n,d):
    return cf_fold(cf_ratio(n,d))

def convergents(cf):
    cvgs = [(1,0)]
    cf = iter(cf)
    n = cf.next()
    d = 1
    for x in cf:
        cvgs.append((n,d))
        yield cvgs[-1]
        n, d = (x * cvgs[-1][0] + cvgs[-2][0]), (x * cvgs[-1][1] + cvgs[-2][1])
        cvgs = cvgs[-2:]
    yield (n,d)
