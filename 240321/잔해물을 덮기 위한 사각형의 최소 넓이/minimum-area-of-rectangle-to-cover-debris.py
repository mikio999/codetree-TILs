x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

OFFSET = 1000
MAX_R = 2000

x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
x3, y3, x4, y4 = x3+OFFSET, y3+OFFSET, x4+OFFSET, y4+OFFSET

grid = [[0] * MAX_R for _ in range(MAX_R)]

for i in range(x1,x2):
  for j in range(y1,y2):
    grid[i][j] = 1

for i in range(x3,x4):
  for j in range(y3,y4):
    grid[i][j] = 2

min_x, max_x, min_y, max_y = MAX_R, 0, MAX_R, 0
first_rect_exist = False

for x in range(MAX_R):
  for y in range(MAX_R):
    if grid[x][y] == 1:
      first_rect_exist = True
      min_x = min(min_x, x)
      max_x = max(max_x, x)
      min_y = min(min_y, y)
      max_y = max(max_y, y)

if not first_rect_exist:
  area = 0
else :
  area = (max_x - min_x + 1) * (max_y - min_y + 1)

print(area)