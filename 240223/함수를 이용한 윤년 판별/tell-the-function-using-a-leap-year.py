y = int(input())

def find_leap_year(n):
  is_leap_year = 'false'
  if n % 4 == 0 :
    is_leap_year = 'true'
    if n % 100 == 0 and n % 400 != 0:
      is_leap_year = 'false'
  return is_leap_year


print(find_leap_year(y))