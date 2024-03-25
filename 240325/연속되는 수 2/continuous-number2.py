n = int(input())
numbers=[int(input()) for _ in range(n)]

k = 1
sequences = []

for i in range(n):
  if i == 0 or numbers[i] != numbers[i-1]:
    sequences.append(k)
    k = 1
  else:
    k += 1

print(max(sequences))