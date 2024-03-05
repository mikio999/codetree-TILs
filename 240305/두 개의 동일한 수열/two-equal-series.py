n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort()

if A == B :
  print('Yes')
else:
  print('No')