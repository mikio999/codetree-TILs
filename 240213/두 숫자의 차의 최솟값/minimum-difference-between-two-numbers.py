n = int(input())

a = [int(x) for x in input().split()]
s = []
for i in range(1,n):
  c = a[i] - a[i-1]
  s.append(c)

print(min(s))