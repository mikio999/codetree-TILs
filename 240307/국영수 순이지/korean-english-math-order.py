n = int(input())

class Grade :
  def __init__(self, name, kor, eng, math):
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math

grades = []

for i in range(n):
  name, kor, eng, math = tuple(input().split())
  grades.append(Grade(name,int(kor),int(eng), int(math)))

grades.sort(key= lambda x: ( -x.kor, -x.eng, -x.math))

for j in grades:
  print(j.name, j.kor, j.eng, j.math)