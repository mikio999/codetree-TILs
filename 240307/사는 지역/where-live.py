class Address:
  def __init__(self, name, number, location):
    self.name = name
    self.number = number
    self.location =location

n = int(input())

address_list = []
for i in range(n) :
  name, number, location = tuple(input().split())
  address_list.append(Address(name, number, location))

target = 0
for j in range(1,n):
  if address_list[j].name > address_list[target].name :
    target = j

print(f'name {address_list[target].name}\naddr {address_list[target].number}\ncity {address_list[target].location}')