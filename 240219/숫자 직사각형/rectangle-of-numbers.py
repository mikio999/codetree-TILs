n, m = map(int, input().split())

grid = [
  [0 for _ in range(m)]
  for _ in range(n)
]

num = 1
for i in range(n):
  for j in range(m):
    grid[i][j] = num
    num += 1

for i in range(n):
  for j in range(m):
    print(grid[i][j], end= ' ')
  print()