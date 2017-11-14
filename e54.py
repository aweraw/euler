from __future__ import with_statement

cards = dict((c,i+2) for i,c in enumerate('23456789TJQKA'))

def dealer():
  with open('poker.txt') as f:
    for line in f:
      deal = line.strip().split()
      p1 = [(cards[v],s) for v,s in deal[:5]]
      p2 = [(cards[v],s) for v,s in deal[5:]]
      yield (p1,p2)

def is_consecutive(vals):
  return vals[0]+4 == vals[4]

def score_hand(hand):
  values = sorted(x[0] for x in hand)
  vset = set(values)
  vslen = len(vset)

  if vslen is 5:
    suits = [x[1] for x in hand]
    if len(set(suits)) is 1:
      if is_consecutive(values):
        return (9,values[0])
      else:
        return (6,max(values))
    else:
      if is_consecutive(values):
        return (5,values[0])
      else:
        return (1,max(values))
  else:
    if vslen is 4:
      return (2,[x for x in vset if values.count(x) is 2].pop())
    elif vslen is 3:
      s = list()
      for n in vset:
        if values.count(n) is 3:
          s.append((4,n))
        elif values.count(n) is 2:
          s.append((3,n))
      return max(s)
    else:
      if values.count(vset.copy().pop()) in (4,1):
        return (8,[x for x in vset if values.count(x) is 4].pop())
      else:
        return (7,[x for x in vset if values.count(x) is 3].pop())

def answer():
  p1 = 0
  for p1_hand, p2_hand in dealer():
    if score_hand(p1_hand) > score_hand(p2_hand):
      p1 += 1
  return p1

if __name__ == '__main__':
  print answer()
