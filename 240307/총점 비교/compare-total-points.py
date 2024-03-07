class Score :
  def __init__(self, name,score1, score2, score3) :
    self.name = name
    self.score1 = score1
    self.score2 = score2
    self.score3 = score3

n = int(input())
scores = []
for i in range(n):
  name, score1, score2, score3 = tuple(input().split())
  scores.append(Score(name, int(score1), int(score2), int(score3)))

scores.sort(key= lambda x: x.score1 + x.score2 + x.score3)

for j in scores:
  print(j.name, j.score1, j.score2, j.score3)