n = int(input())
a = [int(x) for x in input().split()]

a.sort()

for i in a:
  print(i, end=' ')

print()

a.sort(reverse=True)

for j in a:
  print(j, end= ' ')