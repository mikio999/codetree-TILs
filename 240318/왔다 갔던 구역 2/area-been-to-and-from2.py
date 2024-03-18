n = int(input())
commands = []

for _ in range(n) :
  x, y = input().split()
  x = int(x)
  commands.append((x,y))

MAX_R = 1000
index = MAX_R // 2
grid = [0 for _ in range(MAX_R)]


for x, direction in commands:
    if direction == 'R':
        for i in range(index, index + x):
            grid[i] += 1
        index += x
    else: 
        for i in range(index - 1, index - x - 1, -1):
            grid[i] += 1
        index -= x

revisited = 0

for i in grid:
    if i > 1:
        revisited += 1

print(revisited)