class Dot:
  def __init__(self, x, y, num):
    self.x = x
    self.y = y
    self.num = num

dots = []
n = int(input())

for i in range(1,n+1):
  x,y = tuple(map(int, input().split()))
  dots.append(Dot(x,y,i))

dots.sort(key= lambda k: (abs(-k.x) + abs(-k.y), k.num))

for j in dots:
  print(j.num)