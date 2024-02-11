n = int(input())
a = [int(x) for x in input().split()]

count = 0
for i in range(n):
  if a[i] == 2:
    count += 1
    if count == 3:
      print(i+1)