
def value_of(string,digits):

  digit_val_dict = dict(x[::-1] for x in enumerate(digits))
  base_n = len(digits)

  total = 0
  e = 0

  for d in string[::-1]:
    total += digit_val_dict[d] * (base_n ** e)
    e += 1

  return total

def make_number_rep(n,digits):

  digit_val_dict = dict(x for x in enumerate(digits))
  base_n = len(digits)
  
  rep = ''
  e = 1
  
  while n >= base_n**e:
    e += 1
  e -= 1
  
  while e >= 0:
    m, n = divmod(n,base_n**e)
    rep += digit_val_dict[m]
    e -= 1
  
  return rep

def convert(string,ndigits,fdigits):

  return make_number_rep(value_of(string,ndigits),fdigits)
