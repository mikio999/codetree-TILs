grid = [list(map(int, input().split()))
for _ in range(2)]

# 가로 평균
for i in range(2):
  sum_val = 0
  for j in range(4):
    sum_val += grid[i][j]
  print(sum_val/4, end = ' ')
print()

# 새로 평균
for i in range(4):
  sum_val = 0
  for j in range(2):
    sum_val += grid[j][i]
  print(sum_val/2, end= ' ')
print()

# 전체 평균
total = 0
for i in range(2):
  for j in range(4):
    total += grid[i][j]
print(f"{total/8:.1f}")