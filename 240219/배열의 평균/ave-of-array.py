grid = [list(map(int, input().split()))
for _ in range(2)]

print(sum(grid[0])/4, sum(grid[1])/4, end = ' ')
print()

for i in range(4):
  print((grid[0][i] + grid[1][i])/2, end = ' ')
print()

print(((sum(grid[0])/4) + (sum(grid[1])/4))/2)