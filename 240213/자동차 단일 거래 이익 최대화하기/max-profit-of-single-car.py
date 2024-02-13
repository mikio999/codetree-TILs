n = int(input())
a = [int(x) for x in input().split()]

profit = []

for i in range(1,n):
  idx1 = 0
  while idx1 < n-1:
    if idx1+i < n and a[idx1 + i] - a[idx1] > 0:
      profit.append(a[idx1 + i] - a[idx1])
      idx1 += 1
    else:
      idx1 += 1

if len(profit) == 0:
  print(0)
else: 
  print(max(profit))