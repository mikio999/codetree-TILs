class Student:
  def __init__(self, idx, h, w):
    self.idx, self.h, self.w = idx, h, w

n = int(input())
students = []

for i in range(1,n+1):
  h,w = map(int, input().split())
  students.append(Student(i,h,w))

students.sort(key= lambda x: (x.h, -x.w))

for j in students:
  print(j.h, j.w, j.idx)