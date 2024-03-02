n = int(input())
a = [int(x) for x in input().split()]
def f(args):
  if len(args) == 1:
    return args[0]
  else :
    return max(args[0], f(args[1:]))
  

print(f(a))