a = [int(x) for x in input().split()]

def f(a):
  if len(a) == 1:
    return a[0]
  return f(a[1:]) * a[0]

result = str(f(a))

num = 0
for i in range(len(result)):
  num += int(result[i])
print(num)