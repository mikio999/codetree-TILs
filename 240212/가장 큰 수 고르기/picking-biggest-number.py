import sys

arr = [int(x) for x in input().split()]
max_val = -sys.maxsize
for elem in arr:
    if elem > max_val:
        max_val = elem

print(max_val)