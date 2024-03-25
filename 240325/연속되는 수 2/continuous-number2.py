n = int(input())
numbers=[int(input()) for _ in range(n)]

sequences = []
cnt = 1

for i in range(n):
  if i == 0 :
    cnt = 1
  if i == n-1 or numbers[i] != numbers[i-1]:
    sequences.append(cnt)
    cnt = 1
  else:
    cnt += 1

print(max(sequences))