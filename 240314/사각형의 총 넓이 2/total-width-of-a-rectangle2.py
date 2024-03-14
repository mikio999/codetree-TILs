OFFSET = 100
N = int(input())
area = 0
grid =[[0]*200 for _ in range(200)]

for _ in range(N):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(x1+OFFSET, x2+OFFSET) :
    for j in range(y1+OFFSET,y2+OFFSET) :
      grid[i][j] += 1

for i in range(200):
  for j in range(200):
    if grid[i][j] > 0 :
      area += 1

print(area)