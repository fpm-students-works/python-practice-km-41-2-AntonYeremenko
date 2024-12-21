def fact(num):
 if num%1 == 0:
  fact0 = 1
  for i in range(0,num):
   fact0 *= num-i
  return fact0
 else:
  print('Cant take a factorial of non-natural number')