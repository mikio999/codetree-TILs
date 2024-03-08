n = int(input())

class Info:
  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight

people = []

for i in range(n):
  name, h, w = tuple(input().split())
  people.append(Info(name,int(h),int(w)))

people.sort(key= lambda x: (x.height, -x.weight))

for j in people:
  print(j.name, j.height, j.weight)