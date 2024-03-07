class Body:
  def __init__(self,name,height,weight) :
    self.name = name
    self.height = height
    self.weight = weight

n = int(input())

information = []
for i in range(n):
  name, height, weight = tuple(input().split())
  information.append(Body(name, int(height), int(weight)))

information.sort(key= lambda x: x.height)
for j in information:
  print(j.name, j.height, j.weight)