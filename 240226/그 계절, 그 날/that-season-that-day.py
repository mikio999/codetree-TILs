Y, M, D = map(int, input().split())

def is_leap_year(Y) :
  if Y % 4 == 0:
    if Y%100 != 0:
      return True
    else:
      if Y % 400 == 0:
        return True
      else:
        return False
  else:
    return False
  
def find_season(M):
  if 3 <= M <= 5:
    return 'Spring'
  elif 6 <= M <= 8:
    return 'Summer'
  elif 9 <= M <= 11:
    return 'Fall'
  elif 1 <= M <= 2 or M == 12 :
    return 'Winter'
  
def find_day(Y,M,D):
  if M == 2 :
    if is_leap_year(Y) :
      if D >= 29 :
        return 'Winter'
      else:
        return -1
    else:
      return -1
  elif M < 8 :
    if M % 2 == 1 :
      if D <= 31 :
        return find_season(M)
    else :
      if D <= 30 :
        return find_season(M)
      else:
        return -1
  elif 9 <= M < 12:
    if M % 2 == 0 :
      if D <= 31 :
        return find_season(M)
      else:
        return -1
    else:
      if D <= 30 :
        return find_season(M)
      else:
        return -1

print(find_day(Y,M,D))