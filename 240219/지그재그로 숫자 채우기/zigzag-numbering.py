n, m = map(int, input().split())

a = [
  [0 for _ in range(m)]
   for _ in range(n)
]

num = 0

for i in range(m):
    if i % 2 == 0 :
      for j in range(n):
        a[j][i] = num
        num += 1
    else:
      for j in range(n-1, -1,-1) : 
        a[j][i] = num
        num += 1

for i in range(n):
  for j in range(m):
    print(a[i][j], end = ' ')
  print()