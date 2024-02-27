a, b = map(int, input().split())

def calculate_two_int(a, b):
  if a > b :
    a *= 2
    b += 10
  else :
    a += 10
    b *= 2
  return a, b

a,b = calculate_two_int(a,b)
print(a, b)