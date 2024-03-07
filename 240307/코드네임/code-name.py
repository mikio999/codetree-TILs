class Spy:
  def __init__(self, name, score):
    self.name = name
    self.score = score

spy_list = []

for _ in range(5):
  name, score = tuple(input().split())
  spy_list.append(Spy(name, int(score)))

min_num = 0
for i in range(1,5):
  if spy_list[min_num].score > spy_list[i].score:
    min_num = i

print(spy_list[min_num].name, spy_list[min_num].score)