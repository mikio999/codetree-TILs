n = int(input())
numbers = [int(input()) for _ in range(n)]

answer = 0
count = 0

for i in range(n):
  if i >= 1 and numbers[i] * numbers[i-1] > 0:
    count += 1
  else:
    count = 1
  
  answer = max(answer,count)

print(answer)