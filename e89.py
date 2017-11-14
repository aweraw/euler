
c2n = {'I':1,
       'V':5,
       'X':10,
       'L':50,
       'C':100,
       'D':500,
       'M':1000}

def to_roman(n):
    if n == 0:
        return ''
        
    if n >= 1000:
        return 'M' + to_roman(n-1000)
    elif n >= 900:
        return 'CM' + to_roman(n-900)
    elif n >= 500:
        return 'D' + to_roman(n-500)
    elif n >= 400:
        return 'CD' + to_roman(n-400)
    elif n >= 100:
        return 'C' + to_roman(n-100)
    elif n >= 90:
        return 'XC' + to_roman(n-90)
    elif n >= 50:
        return 'L' + to_roman(n-50)
    elif n >= 40:
        return 'XL' + to_roman(n-40)
    elif n >= 10:
        return 'X' + to_roman(n-10)
    elif n == 9:
        return 'IX' + to_roman(n-9)
    elif n >= 5:
        return 'V' + to_roman(n-5)
    elif n == 4:
        return 'IV' + to_roman(n-4)
    else:
        return 'I' + to_roman(n-1)

def from_roman(s):
    t = s[1:]+'I'
    vals = list()
    skip = None
    for i,c in enumerate(s):
        if skip:
            skip = None
            continue
        if c2n[c] < c2n[t[i]]:
            vals.append(c2n[t[i]]-c2n[c])
            skip = True
        else:
            vals.append(c2n[c])
    return sum(vals)

def answer():
    corrected = [to_roman(from_roman(x.strip()))
                 for x in open('roman.txt')]
    return 10848 - len('\r\n'.join(corrected))
