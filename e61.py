
def get_seq(func):
  seq = list()
  n = 0
  i = 1
  while n < 1000:
    n = func(i)
    i += 1
  while n < 10000:
    seq.append(n)
    n = func(i)
    i += 1
  return seq

seqs = {'triangle':get_seq(lambda x: x*(x+1)/2),
        'square':get_seq(lambda x: x*x),
        'pentagonal':get_seq(lambda x: x*(3*x-1)/2),
        'hexagonal':get_seq(lambda x: x*(2*x-1)),
        'heptagonal':get_seq(lambda x: x*(5*x-3)/2),
        'octagonal':get_seq(lambda x: x*(3*x-2))}

sset = set(seqs.keys())
      
def cyclic_pairs(n,seq):
  min = (n % 100)*100
  max = min + 100
  if min < 1000:
    return []
  return [x for x in seq if min < x < max]

def chains(n,kset):
  if not kset:
    return [[n]]
  return [[n] + pchain for seqk in kset
                       for p in cyclic_pairs(n,seqs[seqk])
                       for pchain in chains(p,kset.difference(set([seqk])))]

def is_cyclic(seq):
  return seq[-1] % 100 == seq[0] / 100

def answer():
  nsset = sset.difference(set(['octagonal']))
  for n in seqs['octagonal']:
    for chain in chains(n,nsset):
      if is_cyclic(chain):
        return sum(chain)

if __name__ == '__main__':
  print answer()
