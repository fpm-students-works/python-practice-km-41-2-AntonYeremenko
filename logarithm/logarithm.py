import math
def log(a,b):
 if a > 0 and a != 1 and b > 0:
  return math.log(b,a)
 else:
  if a < 0:
   print('base cant be less than 0')
  elif a == 1:
   print('base cant be equal to 1')
  elif b <= 0:
   print('cant take a log from a non-positive number')

def ln(b):
 if b > 0:
  return math.log1p(b-1)
 else:
  print('cant take a log from a non-positive number')

def lg(b):
 if b > 0:
  return math.log10(b)
 else:
  print('cant take a log from a non-positive number')
