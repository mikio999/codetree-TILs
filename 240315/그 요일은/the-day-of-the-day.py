m1, d1, m2, d2 = map(int, input().split())
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day_list = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

A = input()

distance = 0

while True:
  if days[distance] == A:
    break
  else:
    distance += 1

month = m1
day = d1  + distance
elapsed_day = 0
count = 0

if m1 == m2 and d2 - d1 < distance:
    count = 0
else:
    day = d1
    while True:
        if month == m2 and day == d2:
           if elapsed_day%7 >= distance:
              count += 1
              break
           else :
              break
        else: 
          if day == day_list[month]:
              month += 1
              day = 1
              elapsed_day += 1
          else:
              day += 1
              elapsed_day += 1

print(elapsed_day//7 + count)