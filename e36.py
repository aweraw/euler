def magnitudes(i):
  x = 1
  ms = []
  while x <= i:
    ms.append(x)
    x *= 2
  ms.reverse()
  return ms

def binrep(i):
  s = ''
  mags = magnitudes(i)
  for m in mags:
    if m <= i:
      s += '1'
      i -= m
    else:
      s += '0'
  return s

def is_palindromic(s):
  l = list(s)
  l.reverse()
  return s == ''.join(l)

def answer():
  total = 0
  for n in xrange(1,1000000,2):
    if is_palindromic(str(n)):
      if is_palindromic(binrep(n)):
        total += n
  return total
