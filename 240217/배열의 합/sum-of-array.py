arr_2d = []

for _ in range(4):
  a = [int(x) for x in input().split()]
  arr_2d.append(a)

for i in range(4):
  print(sum(arr_2d[i]))