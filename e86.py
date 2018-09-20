
cnt = 0
target = 1000000
adj = 2

while cnt < target:
    adj += 1
    for oppos in range(3, 2*adj + 1):
        hyp = (adj**2 + oppos**2)**0.5
        if hyp == int(hyp):
            cnt += int(oppos/2.0) if oppos <= adj else (adj - int((oppos+1)/2.0)) + 1

print adj