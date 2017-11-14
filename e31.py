coins = [1,2,5,10,20,50,100,200]

def coin_combos(ncoins=8,amount=200):
  if ncoins is 1:
    return [[amount]]
  combos = ([n,amount-n*coins[ncoins-1]] for n in xrange(amount/coins[ncoins-1]+1))
  return [x+[combo[0]] for combo in combos for x in coin_combos(ncoins-1,combo[1])]

def answer():
  return len(coin_combos())
