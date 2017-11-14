def answer():
  looking_for = 1
  up_to = 0
  i = 1
  total = 1

  while looking_for <= 1000000:
    up_to += len(str(i))
    if up_to >= looking_for:
      total *= int(str(i)[-(up_to-looking_for+1)])
      looking_for *= 10
    i += 1

  return total
