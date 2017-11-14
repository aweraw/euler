words = dict()
words['1'] = 'one'
words['2'] = 'two'
words['3'] = 'three'
words['4'] = 'four'
words['5'] = 'five'
words['6'] = 'six'
words['7'] = 'seven'
words['8'] = 'eight'
words['9'] = 'nine'
words['10'] = 'ten'
words['11'] = 'eleven'
words['12'] = 'twelve'
words['13'] = 'thirteen'
words['14'] = 'fourteen'
words['15'] = 'fifteen'
words['16'] = 'sixteen'
words['17'] = 'seventeen'
words['18'] = 'eighteen'
words['19'] = 'nineteen'
words['20'] = 'twenty'
words['30'] = 'thirty'
words['40'] = 'forty'
words['50'] = 'fifty'
words['60'] = 'sixty'
words['70'] = 'seventy'
words['80'] = 'eighty'
words['90'] = 'ninety'
words['1000'] = 'onethousand'

strings = dict()
strings[1] = '%s'
strings[2] = '%s%s'
strings[3] = '%shundredand%s'
strings[4] = strings[1]

longstr = ''
for i in xrange(1,1001):
  numstr = str(i)
  strlen = len(numstr)
  word = strings[strlen]
  if strlen is 3:
    h = words[numstr[0]]
    t = numstr[1]
    o = numstr[2]
    if t is '0':
      if o is '0':
        longstr += h+'hundred'
        continue
      t = words[o]
    elif o is '0' or t is '1':
      t = words[t+o]
    else:
      t = words[t+'0'] + words[o]
    longstr += word % (h,t)
  elif strlen is 2:
    t = numstr[0]
    o = numstr[1]
    if t is '1' or o is '0':
      t = words[t+o]
      o = ''
    else:
      t = words[t+'0']
      o = words[o]
    longstr += word % (t,o)
  else:
    longstr += word % words[numstr]

print len(longstr)
