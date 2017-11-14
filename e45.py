from itertools import count

hexagonals = (x*(2*x-1) for x in count(144))
pentagonals = (x*(3*x-1)/2 for x in count(166))

for h in hexagonals:
  p = pentagonals.next()
  while p < h:
    p = pentagonals.next()
  if h == p:
    print h
    break
