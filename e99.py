from decimal import Decimal
from math import log

def answer():
  lines = open('base_exp.txt').readlines()
  largest = Decimal(1)
  linenum = 0
  llinenum = 0

  for line in lines:
    b,e = map(int, line.split(','))
    linenum += 1
    if Decimal(int(log(b)*e)).exp() > largest:
      largest = Decimal(int(log(b)*e)).exp()
      llinenum = linenum
  return llinenum
 