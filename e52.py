from itertools import count

def test(n,x=1):
  if sorted(str(n*x)) == sorted(str(n*(x+1))):
    if x is 5:
      return True
    else:
      return test(n,x+1)
  else:
    False

def answer():
  for n in count(1):
    if test(n): 
      return n

if __name__ == '__main__':
  print answer()
