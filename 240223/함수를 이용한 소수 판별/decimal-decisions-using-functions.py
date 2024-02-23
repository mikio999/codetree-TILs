a, b = tuple(map(int, input().split()))

def find_prime(n):
  is_prime = True
  for i in range(2, n) :
    if n % i == 0:
      is_prime = False
  return is_prime

def add_prime(a,b):
  sum_prime = 0
  if a>1:
    for i in range(a, b+1):
      if find_prime(i) :
        sum_prime += i
  return sum_prime

print(add_prime(a,b))