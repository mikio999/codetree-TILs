n, m = map(int, input().split())

a = [
  list(map(int, input().split()))
  for _ in range(m)
]

b = [
  list(map(int, input().split()))
  for _ in range(m)
]

new_grid = [
  [0 for _ in range(n)]
  for _ in range(m)
]

for i in range(n):
  for j in range(m):
    if a[i][j] == b[i][j]:
      new_grid[i][j] = 0
    else:
      new_grid[i][j] = 1

for i in range(n):
  for j in range(m):
    print(new_grid[i][j], end= ' ')
  print()