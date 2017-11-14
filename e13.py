def get_nums():
  nums = open('13.txt').read()
  nums = map(lambda x: int(x), nums.splitlines())
  return nums

def answer():
  total = sum(get_nums())
  return str(total)[:10]

print answer()
