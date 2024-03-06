n = int(input())
a = [int(x) for x in input().split()]

for i in range(n) : 
  if i % 2 == 0:
    sorted_arr = sorted(a[:i+1])
    print(sorted_arr[i//2], end= ' ')