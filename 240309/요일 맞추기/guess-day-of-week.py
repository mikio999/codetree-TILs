m1,d1,m2,d2 = tuple(map(int,input().split()))

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
days_reverse = ['Mon', 'Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue']

date_list = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def elapsed_days(m,d):
  day_quantity = 0
  for i in range(1,m):
    day_quantity += date_list[i]
  day_quantity += d
  return day_quantity


def what_day(m1,d1,m2,d2) :
  if elapsed_days(m1,d1) <= elapsed_days(m2,d2) : 
    day_idx = (abs(elapsed_days(m1,d1) - elapsed_days(m2,d2)))%7
    return days[day_idx]
  else :
    day_idx = (abs(elapsed_days(m2,d2) - elapsed_days(m1,d1)))%7
    return days_reverse[day_idx]


print(what_day(m1,d1,m2,d2))