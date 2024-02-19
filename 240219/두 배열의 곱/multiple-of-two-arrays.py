a = [
    list(map(int, input().split()))
    for i in range(3)
]

input()

b = [ list(map(int, input().split()))
    for i in range(3)]

multiplication = [
  [0 for _ in range(3)]
  for _ in range(3)
]

for i in range(3):
  for j in range(3):
    multiplication[i][j] = a[i][j] * b[i][j]

for i in range(3):
  for j in range(3):
    print(multiplication[i][j], end = ' ')
  print()