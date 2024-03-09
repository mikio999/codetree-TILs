a, b, c = tuple(map(int, input().split()))

def elapsed_minutes(a,b,c) :
  hours = 24 * a + b
  minutes = 60 * hours + c
  return minutes

if elapsed_minutes(a,b,c) - elapsed_minutes(11,11,11) >= 0 :
  print(elapsed_minutes(a,b,c) - elapsed_minutes(11,11,11))
else:
  print(-1)