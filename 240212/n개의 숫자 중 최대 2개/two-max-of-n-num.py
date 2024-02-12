N = int(input())

A = [int(x) for x in input().split()]
A.sort()
A.reverse()
print(A[0], A[1], end= ' ')