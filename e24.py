import math

def get_permutation(seq,n):
  seqlen = len(seq)
  if seqlen < 1:
    return ''
  numperms = reduce(int.__mul__, xrange(1,seqlen+1))
  groupsize = numperms / seqlen
  if n > numperms:
    return None
  i = int(math.floor(n / groupsize))
  new_n = n - (i * groupsize)
  return seq[i] + get_permutation(seq.replace(seq[i],''),new_n)
