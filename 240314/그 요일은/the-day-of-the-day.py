m1, d1, m2, d2 = map(int, input().split())
A = input()

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]

month = m1
day = d1


elapsed_day = d1
for i in range(m1):
  elapsed_day+= day_list[i]
start_day = elapsed_day % 7


A_index = days.index(A)
day_distance = 0

if A_index >= start_day:
  day_distance = A_index - start_day
else:
  7 - (start_day - A_index)

elapsed_day = 0

month = m1
day = d1
while True:
  if month == m2 and day == d2 :
    elapsed_day += 1
    break
  else:
    if day_list[month] == day :
      month += 1
      day = 1
      elapsed_day += 1
    else :
      day += 1
      elapsed_day += 1

answer = (elapsed_day - day_distance) // 7 + 1

print(answer)