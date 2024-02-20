n,m = map(int, input().split())

grid = [
  [0 for _ in range(n)]
  for _ in range(n)
]

for i in range(m):
  r,c = map(int, input().split())
  grid[r-1][c-1] = 1

for x in range(n) :
  for y in range(n) :
    print(grid[x][y], end=' ')
  print()