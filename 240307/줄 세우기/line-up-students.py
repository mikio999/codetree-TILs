class Information:
  def __init__(self, h, w, num):
    self.h = h
    self.w = w
    self.num = num

n = int(input())
students = []
for i in range(1,n+1):
  h, w = tuple(map(int, input().split()))
  num = i
  students.append(Information(h,w,num))

students.sort(key= lambda x: (-x.h, -x.w, x.num))

for j in students:
  print(j.h, j.w, j.num)