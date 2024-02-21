N = int(input())
dx, dy = [1,0,-1,0], [0,-1,0,1]
x, y = 0, 0

for i in range(N) : 
  a, b = input().split()
  b = int(b)
  if a == 'N':
    y = y + dy[3] * b
  elif a == 'E' :
    x = x + dx[0] * b
  elif a == 'S':
    y = y + dy[1] * b
  elif a == 'W' :
    x = x + dx[2] * b

print(x, y)