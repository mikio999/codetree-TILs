n = int(input())

a = [
  [0 for _ in range(n)]
  for _ in range(n)
]

num = 1

if n%2 == 0 : 
  for i in range(n-1,-1,-1):
    if i%2 == 1:
      for j in range(n-1,-1,-1):
        a[j][i] = num
        num += 1
    else:
      for j in range(n):
        a[j][i] = num
        num += 1
else :
    for i in range(n-1,-1,-1):
      if i%2 == 0:
        for j in range(n-1,-1,-1):
          a[j][i] = num
          num += 1
      else:
        for j in range(n):
          a[j][i] = num
          num += 1

for x in range(n) :
  for y in range(n) :
    print(a[x][y], end=' ')
  print()