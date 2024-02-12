from collections import deque
N =int(input())

a = [int(x) for x in input().split()]

b = set(a)
myDeque = deque(b)


while len(myDeque) > 0 and a.count(myDeque[-1]) >= 2:
  myDeque.pop()
if len(myDeque) > 0 and a.count(myDeque[-1]) == 1:
  print(myDeque[-1])
else:
  print(-1)