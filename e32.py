multiplicands = [x for x in xrange(1,100) if x%11 != 0 and x%10 != 0]

def multipliers(n):
  if n < 10:
    start = 1000
  else:
    start = 100
  str_n = str(n)
  return (x for x in xrange(start,(10000/n)+1) 
            if len(set(str(x))) == len(str(x)) 
              and len(set(str(x)+str_n)) == len(str(x)+str_n)
              and str(x).find('0') is -1)

def answer():
  total = []
  for x in multiplicands:
    for y in multipliers(x):
      product = x*y
      str_product = str(product)
      if str_product.find('0') is not -1:
        continue
      elif len(set(str_product+str(x)+str(y))) == 9:
        total.append(product)
  return sum(set(total))
