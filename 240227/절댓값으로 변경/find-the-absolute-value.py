N = int(input())

def absolute_num(a) :
  if a < 0 :
    a *= -1
  print(a , end = ' ')

b = [int(x) for x in input().split()]

for i in b :
  absolute_num(i)