n = int(input())
b = [int(x) for x in input().split()]

def only_divide_even(a):
  for i in range(n):
    if a[i] % 2 == 0:
      a[i] = a[i]//2

only_divide_even(b)

for j in range(n):
  print(b[j], end = ' ')