n = int(input())
MAX_R = 200
grid = [[0] * MAX_R for _ in range(MAX_R)]
OFFSET = 100

for num in range(n): 
  x1,y1,x2,y2 = map(int, input().split())
  x1 += OFFSET
  y1 += OFFSET
  x2 += OFFSET
  y2 += OFFSET
  if num % 2 == 0 :
    for i in range(x1, x2):
      for j in range(y1, y2):
        grid[i][j] = 1
  if num % 2 == 1:
    for i in range(x1, x2):
      for j in range(y1, y2):
        grid[i][j] = 2

area = 0

for i in range(200) :
  for j in range(200) :
    if grid[i][j] == 2:
      area += 1

print(area)