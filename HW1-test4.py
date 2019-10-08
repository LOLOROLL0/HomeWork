a,b=map(int, input().split())
if a >= 0 and b >=0 :
  while b != 0:
    a,b = b, a%b
  print('NOD:',a, sep='')
  