n = int(input())
numbers=[int(input()) for _ in range(n)]

cnt = 0
ans = 0

for i in range(n):
  if i==0 or numbers[i] > numbers[i-1]:
    cnt += 1
  else :
    cnt = 1
  ans = max(ans,cnt)

print(ans)