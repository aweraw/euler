from totient import totient_list

def answer():
    tlist = totient_list(1000000)
    largest = 1
    winner = 1
    for i in xrange(2,1000001):
        if float(i)/tlist[i] > largest:
            largest = float(i)/tlist[i]
            winner = i
    return winner

if __name__ == '__main__':
  print answer()
