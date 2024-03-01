n = int(input())

def until_one(n, process=0):
  if n == 1:
    return process
  elif n%2 == 0:
    return until_one(n//2, process + 1)
  else :
    return until_one(n//3, process + 1)
  
print(until_one(n))