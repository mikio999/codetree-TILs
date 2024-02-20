n = int(input())

square = [
  [1 for _ in range(n)]
  for _ in range(n)
]

for i in range(1, n) :
  for j in range(1, n) :
    square[i][j] = square[i-1][j-1] + square[i][j-1] + square[i-1][j]

for x in range(n) :
  for y in range(n) :
    print(square[x][y], end= ' ')
  print()