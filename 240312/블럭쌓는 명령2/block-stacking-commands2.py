N, K = map(int, input().split())
blocks = [0 for i in range(N)]

for i in range(K):
  a,b = map(int, input().split())
  for j in range(a,b+1):
    blocks[j] += 1

print(max(blocks))