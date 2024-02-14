n = int(input())
a = [int(x) for x in input().split()]
b = set(a)
c = list(b)

for i in b:
  if a.count(i) >= 2:
    c.remove(i)

if len(c) > 0 :
  print(max(c))
else:
  print(-1)