def f(n, process=0):
  if n == 1:
    return process
  if n % 2 == 0:
    process += 1
    return f(n//2, process)
  if n % 2 == 1:
    process += 1
    return f(3*n+1, process)
  
n = int(input())
print(f(n))