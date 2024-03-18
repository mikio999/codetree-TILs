n = int(input())
commands = []

for _ in range(n) :
  x, y = input().split()
  x = int(x)
  commands.append((x,y))

MAX_R = 201
index = MAX_R // 2
grid = [[0] for _ in range(MAX_R)]

for command in commands :
  if command[1] == 'R':
    for i in range(index, index+command[0]+1) :
      grid[i][0] += 1
    index += command[0]
  elif command[1] == 'L':
    for i in range(index, index - command[0]-1, -1) :
      grid[i][0] += 1
    index -= command[0]

dots = []

for i in range(len(grid)):
  if grid[i][0] >= 2 :
    dots.append(i)

answer = 0

result = []
sequence =[dots[0]]

for i in range(1, len(dots)):
  if dots[i] == dots[i-1] + 1:
    sequence.append(dots[i])
  else:
    result.append(sequence)
    sequence = [dots[i]]

result.append(sequence)

answer = 0
for i in result:
  answer += len(i) - 1

print(answer)