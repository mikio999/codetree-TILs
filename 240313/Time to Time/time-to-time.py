a, b, c, d = tuple(map(int, input().split()))

hour = a
min = b
elapsed_time = 0
while True:
  if hour == c and min == d:
    break
  else:
    min += 1
    elapsed_time += 1
    if min == 60 :
      hour += 1
      min = 0

print(elapsed_time)