MAX_R = 2000
OFFSET = 1000

grid = [[0] * MAX_R for _ in range(MAX_R)]

x1,y1,x2,y2 = map(int, input().split())

x1 += OFFSET
y1 += OFFSET
x2 += OFFSET
y2 += OFFSET

m1, k1, m2, k2 = map(int, input().split())

m1 += OFFSET
k1 += OFFSET
m2 += OFFSET
k2 += OFFSET

first_square = []
for i in range(x1,x2) :
  for j in range(y1,y2) :
    grid[i][j] += 1
    first_square.append((i,j))

for i in range(m1, m2):
  for j in range(k1, k2):
    grid[i][j] += 1

dots = []

for i in range(MAX_R):
  for j in range(MAX_R):
    if grid[i][j] == 2 :
      dots.append((i,j))

remain_square = []

for dot in dots:
  first_square.remove(dot)


new_dots = [[0] * MAX_R for _ in range(MAX_R)]

x_dots = []
y_dots = []

for e in first_square:
  x_dots.append(e[0])
  y_dots.append(e[1])

x_length = max(x_dots) - min(x_dots) + 1
y_length = max(y_dots) - min(y_dots) + 1

print(x_length * y_length)