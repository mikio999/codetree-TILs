n1, n2 = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

found = False
for i in range(n1-n2+1):
  if A[i:i+n2] == B:
    print('Yes')
    found = True
    break

if found == False:
  print('No')