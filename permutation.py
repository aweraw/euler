def perm_n(seq, n):
  """Returns the nth permutation of seq"""
  seqc = list (seq [:])
  result = []
  fact = reduce(int.__mul__, range(1, len(seq)+1))
  n %= fact
  while seqc:
    fact = fact / len(seqc)
    choice, n = n // fact, n % fact
    result += [seqc.pop(choice)]
  return result
