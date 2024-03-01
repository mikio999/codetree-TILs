n = int(input())

def square(n):
  if n < 10 :
    return n**2
  return square(n // 10) + (n%10)**2

print(square(n))