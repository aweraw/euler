from itertools import izip

def get_ciphered_text():
  return [int(x) for x in open('cipher1.txt').read().strip().split(',')]

def keys():
  chars = range(97,123)
  return (((x,y,z)*400)+(x,) for x in chars for y in chars for z in chars)

def decipher(key,ctext):
  return ''.join(chr(x^y) for x,y in izip(key,ctext))

def check(dtext):
  return max(dtext.count(x) for x in '#$%&*^`|~') < 1

def brute_force():
  ctext = get_ciphered_text()
  return (decipher(key,ctext) for key in keys() if check(decipher(key,ctext)).next()

def answer():
  return sum(ord(x) for x in brute_force())

if __name__ == '__main__':
  print answer()
