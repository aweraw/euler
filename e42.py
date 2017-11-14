tnums = [int((0.5*n)*(n+1)) for n in xrange(1,21)]

def word_num(word):
  return sum(map(lambda x: ord(x)-64, word))

def words():
  return (word for word in open('words.txt').read().replace('"','').split(','))

def answer():
  return len([x for x in words() if word_num(x) in tnums])
