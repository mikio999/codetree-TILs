n = int(input())

numbers = [int(x) for x in input().split()]

def g(a,b) :
  for i in range(max(a,b), a*b + 1):
    if i % a == 0 and i % b == 0 :
      return i
    
def f(numbers, index=0) :
  if index == len(numbers) - 1:
    return numbers[index]
  else:
    return g(numbers[index], f(numbers, index+1))
  
print(f(numbers))