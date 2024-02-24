a, o, c = input().split()

a= int(a)
c= int(c)

def addition(x,y) : 
  return x + y

def subtraction(x,y) :
  return x - y

def multiplication(x,y) :
  return x * y

def division(x,y) :
  return x//y

if o == '+' :
  print(f'{a} {o} {c} = {addition(a,c)}')
elif o == '-' :
  print(f'{a} {o} {c} = {subtraction(a,c)}')
elif o == '*' :
  print(f'{a} {o} {c} = {multiplication(a,c)}')
elif o == '/' :
  print(f'{a} {o} {c} = {division(a,c)}')
else :
  print(False)