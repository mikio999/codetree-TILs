n = 5
square = [
  [0 for _ in range(n)]
  for _ in range(n)
]

for i in range(n):
  square[0][i] = 1
  square[i][0] = 1

for i in range(1,n):
  for j in range(1,n):
    square[i][j] = square[i-1][j] + square[i][j-1]

for i in range(n):
  for j in range(n):
    print(square[i][j], end=' ')
  print()