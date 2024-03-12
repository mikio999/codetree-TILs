N, K = map(int, input().split())
blocks = [0 for _ in range(N)]

for i in range(K):
  a,b = map(int, input().split())
  while a < b+1:
    blocks[a] += 1
    a += 1
print(max(blocks))