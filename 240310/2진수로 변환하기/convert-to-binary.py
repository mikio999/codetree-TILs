n = int(input())
two_digits = []

while True:
  if n < 2:
    two_digits.append(n)
    break
  else:
    two_digits.append(n%2)
    n //= 2

two_digits.reverse()
for i in two_digits:
  print(i,end='')