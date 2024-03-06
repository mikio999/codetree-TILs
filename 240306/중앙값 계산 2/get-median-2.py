n = int(input())
a = [int(x) for x in input().split()]
b = []
ans = []
for i in range(n+1):
  if i % 2 == 1:
    b.append(a[:i])
    b.sort()

for j in range(len(b)):
  b[j].sort()
  ans.append(b[j][j])

for _ in ans:
  print(_, end = ' ')