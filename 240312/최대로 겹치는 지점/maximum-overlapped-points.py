n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
MAX_R = 100

checked = [0] * MAX_R

for i in lines:
  for j in range(i[0], i[1]+1) :
    checked[j] += 1

print(max(checked))