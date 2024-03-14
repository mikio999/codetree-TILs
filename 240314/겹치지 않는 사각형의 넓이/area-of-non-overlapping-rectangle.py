Ax1, Ay1, Ax2, Ay2 = map(int, input().split())
Bx1, By1, Bx2, By2 = map(int, input().split())
Mx1, My1, Mx2, My2 = map(int, input().split())

OFFSET = 1000
MAX_R = 2000
grid = [[0] * MAX_R for _ in range(MAX_R)]

for i in range(Ax1+OFFSET, Ax2+OFFSET) :
  for j in range(Ay1+OFFSET, Ay2+OFFSET) :
    grid[i][j] += 1

for i in range(Bx1+OFFSET, Bx2+OFFSET) :
  for j in range(By1+OFFSET, By2+OFFSET) :
    grid[i][j] += 1

for i in range(Mx1+OFFSET, Mx2+OFFSET) :
  for j in range(My1+OFFSET, My2+OFFSET):
    grid[i][j] -= 1


area = 0 
for i in range(MAX_R):
  for j in range(MAX_R) :
    if grid[i][j] == 1:
      area += 1

print(area)