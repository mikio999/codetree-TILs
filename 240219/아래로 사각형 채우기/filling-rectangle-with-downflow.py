n = int(input())

square = [ [0 for _ in range(5)] for _ in range(5) ]

num = 1

for i in range(n):
  for j in range(n):
    square[j][i] = num
    num += 1

for i in range(n):
  for j in range(n):
    print(square[i][j], end = ' ')
  print()