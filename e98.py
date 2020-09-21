from collections import defaultdict

with open('words.txt') as f:
    words = f.read().replace('"', '').split(',')

wdict = defaultdict(list)

for w in words:
    k = ''.join(sorted(w))
    wdict[k].append(w)

anagrams = [wdict[k] for k in wdict if len(wdict[k]) > 1]

square_numbers = [n ** 2 for n in range(1, 31623)]
sq_dict = defaultdict(list)
for sq in square_numbers:
    sq_str = str(sq)
    k = ''.join(sorted(sq_str))
    sq_dict[k].append(sq_str)

anagramatic_squares = {tuple(sqs) for sqs in sq_dict.values() if len(sqs) > 1}

encodings = defaultdict(list)
for n in {len(s[0]) for s in anagrams}:
    ans = [s for s in anagrams if len(s[0]) == n]
    sqs = [s for s in anagramatic_squares if len(s[0]) == n]
    for aset in ans:
        for sset in sqs:
            encs = [''.join(sorted(x + y for x, y in zip(a, s)))
                    for a in aset for s in sset]
            if len(encs) > len(set(encs)):
                k = (','.join(aset), tuple(int(s) for s in sset))
                enc_set = {enc for enc in encs if encs.count(enc) > 1}
                encodings[k].extend(enc_set)

maximum = 0
for ((words, sqns), encs) in encodings.items():
    for enc in encs:
        vdict = defaultdict(set)
        for k, v in zip(*[iter(reversed(enc))] * 2):
            vdict[k].add(v)
        ws = words.split(',')
        if all(len(s) == 1 for s in vdict.values()) and len(ws[0]) == len(set(ws[0])):
            edict = dict(zip(*[iter(enc)]*2))
            for word in ws:
                i = int(''.join(edict[c] for c in word))
                if i > maximum:
                    maximum = i

print(maximum)
