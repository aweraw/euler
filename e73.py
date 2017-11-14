from __future__ import division

def calc_ds(low=3, high=2, max_d=10000):
    l = [low, high]
    i = 0
    
    while True:
        while l[i] + l[i+1] <= max_d:
            l.insert(i+1, l[i] + l[i+1])
        i += 1
        if i + 1 == len(l):
            break
    return l

def answer():
    return len(calc_ds()) - 2

if __name__ == '__main__':
    print answer()
