n = int(input())
a = [int(x) for x in input().split()]

a.sort()

for i in range(n//2 + 1):
  print(a[i], end=' ')