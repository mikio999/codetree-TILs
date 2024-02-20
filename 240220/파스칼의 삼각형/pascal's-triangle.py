n = int(input())

triangle = []
for i in range(n):
  row = [1] * (i+1)
  triangle.append(row)

for x in range(2,n):
  for y in range(1,x):
    triangle[x][y] = triangle[x-1][y-1] + triangle[x-1][y]

for x in range(n):
  for y in range(x+1):
    print(triangle[x][y], end = ' ')
  print()