def answer():
  names = open('22.txt').read()[1:-1].split('","')
  names.sort()
  total = 0
  i = 1
  for name in names:
    total += sum(map(lambda x: ord(x)-64, name)) * i
    i += 1
  return total
