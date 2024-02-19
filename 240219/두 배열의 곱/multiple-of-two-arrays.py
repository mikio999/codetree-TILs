a = []
b = []
multiplication = [
  [0 for _ in range(3)]
  for _ in range(3)
]

for i in range(4):
  a.append([int(x) for x in input().split()])

for j in range(3):
  b.append([int(y) for y in input().split()])

for i in range(3):
  for j in range(3):
    multiplication[i][j] = a[i][j] * b[i][j]

for i in range(3):
  for j in range(3):
    print(multiplication[i][j], end = ' ')
  print()