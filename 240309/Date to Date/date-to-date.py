m1, d1, m2, d2 = map(int,input().split())

day_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]

month, day = m1, d1
elapsed_days = 0

while True:
  if month == m2 and day == d2 :
    elapsed_days += 1
    break
  else:
    day += 1
    elapsed_days += 1
    if day == day_list[month] :
      month += 1
      day = 1
      elapsed_days += 1

print(elapsed_days)