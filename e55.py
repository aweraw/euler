
def lychrel(n,i=0):
  if i is 50: return True
  str_n = str(n)
  if str_n == str_n[::-1] and i is not 0: return False
  return lychrel(n + int(str_n[::-1]), i+1)

def answer():
  return sum(lychrel(x) for x in xrange(10000))

if __name__ == '__main__':
  print answer()
