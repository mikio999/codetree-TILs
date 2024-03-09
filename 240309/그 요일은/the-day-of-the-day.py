m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def elapsed_days(m,d):
  day_quantity = 0
  for i in range(1, m):
    day_quantity += day_list[i]
  day_quantity += d
  return day_quantity

def count_day(m1,d1,m2,d2):
  for i in range(7):
    if A == days[i]:
      num = i
  day_count = ((elapsed_days(m2, d2) + num) - elapsed_days(m1,d1))//7
  return day_count

print(count_day(m1,d1,m2,d2))