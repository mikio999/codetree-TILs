class Location:
  def __init__(self, idx, number) :
    self.idx = idx
    self.number = number

n = int(input())
numbers = [int(x) for x in input().split()]
num_list = []

for i in range(n):
  args = (i+1, numbers[i])
  num_list.append(Location(*args))

num_list.sort(key= lambda x: (x.number, x.idx))

ans = []

for k in range(1,n+1):
  i = 0
  while k != num_list[i].idx:
    i += 1
  ans.append(i+1)

for j in ans:
  print(j, end=' ')