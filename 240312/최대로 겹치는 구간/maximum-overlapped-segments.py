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

lines = [0 for _ in range(min_dot, max_dot)]

for i in line_dots:
  i[0] += -min_dot
  i[1] += -min_dot


for i in line_dots:
  for j in range(i[0], i[1]-1):
    lines[j] += 1

print(max(lines))