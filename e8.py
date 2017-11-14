bignum = open('8.txt').read()
bignum = ''.join(bignum.splitlines())

prods = []
i = 0
while i+5 <= 1000:
  seg = map(lambda x: int(x), bignum[i:i+5])
  prods.append(reduce(lambda x,y:x*y, seg))
  i += 1

print max(prods)
