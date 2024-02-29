n = int(input())
def print_small_number(n):
  if n == 0:
    return
  print_small_number(n-1)
  print(n, end= ' ')

print_small_number(n)
print()
def print_big_number(n):
  if n == 0:
    return
  print(n, end=' ')
  print_big_number(n-1)

print_big_number(n)