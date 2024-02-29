def print_hello_world(n):
  if n == 0: 
    return
  print_hello_world(n-1)
  print('HelloWorld')

n = int(input())

print_hello_world(n)