import sys

max_perim = 1000

m = 2
n = 1

while True:
  while m > n:
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    t = (a,b,c)
    if sum(t)==max_perim:
      print reduce(lambda x,y:x*y, t)
      sys.exit()
    n += 1
  m += 1
  n = 1
