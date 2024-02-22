def min_num(*args):
  return min(args)

a,b,c = map(int, input().split())
print(min_num(a,b,c))