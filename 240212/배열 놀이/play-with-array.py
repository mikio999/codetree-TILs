n, q = map(int, input().split())
a = [int(x) for(x) in input().split()]

for _ in range(q):
  b = [int(y) for(y) in input().split()]
  if b[0] == 1:
    print(a[b[1]-1])
  elif b[0] == 2:
    if b[1] in a:
      print(a.index(b[1])+1)
    else:
      print(0)
  elif b[0] == 3:
    for i in a[b[1]-1:b[2]]:
      print (i, end=' ')
    print()