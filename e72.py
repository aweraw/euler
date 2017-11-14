import totient

def answer():
    return sum(totient.totient_list(1000000))

if __name__ == '__main__':
    print answer()
