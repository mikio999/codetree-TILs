m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]

month, day=m1,d1
distance = 0
count = 0

while True:
  if month == m2 and day == d2+1:
    break
  else:
    day += 1
    distance += 1
    if days[distance%7] == A:
      count += 1
    if day == day_list[month]:
      month += 1
      day = 1

print(count)