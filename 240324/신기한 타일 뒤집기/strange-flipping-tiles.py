n = int(input())
commands = []
MAX_R = 1000 * 100 * 2
index = MAX_R//2

tile = ['gray']*MAX_R

for i in range(n):
  a, b = input().split()
  a = int(a)
  commands.append((a,b))

for command in commands:
  if command[1] == 'R':
    for i in range(index, index+command[0]):
      tile[i] = 'black'
    index += command[0]

  else : 
    for j in range(index-1, index-command[0]-1, -1):
      tile[j] = 'white'
    index -= command[0]

black_count = 0
white_count = 0

for t in tile:
  if t == 'white':
    white_count += 1
  if t == 'black':
    black_count += 1

print(white_count, black_count)