from itertools import count
from digits import list_digits

cache = dict()

def gen_cubes():
  for i in count(1):
    yield i**3

def answer():
  for cube in gen_cubes():
    k = ''.join(str(x) for x in sorted(list_digits(cube)))
    if k in cache:
      cache[k].append(cube)
      if len(cache[k]) is 5:
        return min(cache[k])
    else:
      cache[k] = [cube]

if __name__ == '__main__':
  print answer()
