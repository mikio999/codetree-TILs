import sys
n = int(input())
arr = [int(x) for x in input().split()]
count = 0

min_val = sys.maxsize
for elem in arr :
    if min_val > elem:
        min_val = elem

for i in arr :
    if i == min_val:
      count += 1

print(min_val, count, end= ' ')