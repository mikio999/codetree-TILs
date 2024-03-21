n = int(input())
commands = []

for _ in range(n):
  num, dir = input().split()
  num = int(num)
  commands.append((num,dir))

MAX_R = 100001
line = [''] * MAX_R

start = MAX_R//2

for cmd in commands:
  if cmd[1] == 'R':
    for i in range(start, start + cmd[0]):
      line[i] += 'B'
    start += cmd[0]-1
  if cmd[1] == 'L':
    for j in range(start, start - cmd[0], -1) :
      line[j] += 'W'
    start -= cmd[0]-1


white = 0
black = 0
gray = 0

for dot in line:
  if len(dot) >= 4 :
    b_count = 0
    w_count = 0
    for color in dot:
      if color == 'B':
        b_count += 1
      elif color == 'W':
        w_count += 1
    if b_count >= 2 and w_count >= 2 :
      gray += 1
    else :
      if dot[-1] == 'B':
        black += 1
      elif dot[-1] == 'W':
        white += 1
    
  else:
    if 1 <= len(dot) < 4:
      if dot[-1] == 'B':
        black += 1
      elif dot[-1] == 'W':
        white += 1
    else:
      pass

print(white, black, gray)