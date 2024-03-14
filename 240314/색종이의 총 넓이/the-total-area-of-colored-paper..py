OFFSET = 100
MAX_R = 200

N = int(input())
grid = [[0] * MAX_R for _ in range(MAX_R)]

for _ in range(N) :
  x1, y1 = map(int, input().split())
  x2, y2 = x1+8, y1+8
  for i in range(x1+OFFSET,x2+OFFSET):
    for j in range(y1+OFFSET,y2+OFFSET):
      grid[i][j] += 1

area = 0
for i in range(MAX_R) :
  for j in range(MAX_R) :
    if grid[i][j] >= 1 :
      area += 1
print(area)