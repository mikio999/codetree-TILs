def greatest_common_divisor(n,m):
  for i in range(min(n,m), 0, -1):
    if n % i == 0 and m % i == 0 :
      return i

a,b  = map(int, input().split())
print(greatest_common_divisor(a,b))