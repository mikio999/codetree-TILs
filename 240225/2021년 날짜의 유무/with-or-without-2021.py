M, D = map(int, input().split())

def month(m) :
  if 1 <= m <= 12 :
    return True
  else:
    return False
  
def day(m,d) :
  if m == 2:
    if 1<=d<=28:
      return True
    else:
      return False
  elif 1 <= m < 7:
    if m%2 == 1:
      if 1 <= d <= 31:
        return True
      else:
        return False
    else :
      if 1<= d <= 30:
        return True
      else:
        return False
  elif 8 <= m <= 12 :
    if m%2 == 0:
      if 1 <= d <= 31:
        return True
      else:
        return False
    else:
      if 1 <= d <= 30:
        return True
      else:
        return False
  else:
    return False
  
def exist(m,d):
  if month(m) and day(m,d) :
    print('Yes')
  else:
    print('No')

exist(M,D)