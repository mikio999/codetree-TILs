n = int(input())

def add(n) :
  num = 0
  for i in range(0,n+1):
    num += i
  return num//10

print(add(n))