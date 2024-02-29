n, m = map(int, input().split())
A = [int(x) for x in input().split()]

for i in range(m):
  a1, a2 = map(int, input().split())
  sum_A = sum(A[a1-1:a2])
  print(sum_A)