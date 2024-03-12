OFFSET = 100
MAX_R = 200

n = int(input())
segments = [
  tuple(map(int,input().split())) for _ in range(n)
]

checked = [0] * (MAX_R + 1)

for x1, x2 in segments :
  x1, x2 = x1 + OFFSET, x2 + OFFSET
  for i in range(x1, x2) :
     checked[i] += 1

print(max(checked))

'''
n = int(input())
line_dots = []
x2_dots = []
x1_dots = []
max_dot = 0
for i in range(n):
  x1, x2 = tuple(map(int, input().split()))
  line_dots.append([x1,x2])
  x1_dots.append(x1)
  x2_dots.append(x2)

max_dot = max(x2_dots)
min_dot = min(x1_dots)

lines = [0 for _ in range(max_dot - min_dot + 1)]

for i in line_dots:
  i[0] += -min_dot
  i[1] += -min_dot


for i in line_dots:
  for j in range(i[0], i[1]):
    lines[j] += 1


print(max(lines))

'''