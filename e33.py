denominators = [x for x in range(10,100) if x%10 is not 0 and x%11 is not 0]

def numerators(d):
  str_d = str(d)
  ns = list()
  for n in str_d:
    ns += [x for x in denominators if x < d and n in str(x)]
  return list(set(ns))

def cancel(x,y):
  str_x,str_y = str(x),str(y)
  for n in str_x:
    if n in str_y:
      nx,ny = int(str_x.strip(n)),float(str_y.strip(n))
  return nx,ny

def answer():
  pairs = []
  for d in denominators:
    df = float(d)
    ns = numerators(d)
    for n in ns:
      cn,cd = cancel(n,d)
      if n/df == cn/cd:
        pairs.append((n,d))
  product = reduce(lambda x,y: (x[0]*y[0],x[1]*y[1]),pairs)
  # denominator is divisible by numerator... i checked
  return product[1]/product[0]
