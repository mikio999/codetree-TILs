class Spy:
  def __init__(self, name, score):
    self.name = name
    self.score = score

spy_list = []

for _ in range(5):
  name, score = tuple(input().split())
  spy_list.append(Spy(name, score))

min_num = int(spy_list[0].score)
target = 0

for i in range(1,5):
  if int(spy_list[i].score) < min_num:
    target = i
    min_num = int(spy_list[i].score)
    print('target',target,'min_num',min_num)

print(spy_list[target].name, spy_list[target].score)