class Private:
  def __init__(self, name, height, weight):
    self.name = name
    self.height = height
    self.weight = weight

n = 5
people = []
for i in range(n):
  name, height, weight = tuple(input().split())
  people.append(Private(name, int(height), float(weight)))

people.sort(key= lambda x: x.name )

print('name')
for j in people:
  print(j.name, j.height, j.weight)

print()

people.sort(key=lambda x: -x.height)
print('height')
for k in people:
  print(k.name, k.height, k.weight)