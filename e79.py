from __future__ import with_statement

with open('keylog.txt') as f:
  lines = [x.strip() for x in f]

digits = set([x for x in ''.join(lines)])
keys = dict((x,set()) for x in digits)

for key in lines:
  f,s,t = key
  keys[s].add(f)
  keys[t].add(f)
  keys[t].add(s)

ordered = sorted(keys.items(), lambda x,y: len(x[1])-len(y[1]))
print ''.join(c for c,s in ordered)
