from math import sqrt

def cf_sqrt(n):
    cf = list()
    sn = sqrt(n)
    numerator = 1  
    denominator = 0
    constant = int(sn)

    cf.append(constant)
  
    if sn == constant:
        denominator = 1

    while denominator is not 1:
        #simplified denominator
        denominator = (n - constant**2) / numerator
        #next digit in period
        x = (cf[0] + constant) / denominator
        cf.append(x)
        constant = -(constant - (denominator*x))
        numerator = denominator
  
    return cf[0],cf[1:]

def answer():
    return sum(len(cf_sqrt(x)[1]) & 1 for x in xrange(10000))

if __name__ == '__main__':
    print answer()
