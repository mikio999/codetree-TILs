result = 0

A = [int(x) for x in input().split()]

for i in range(len(A)):
    result += A[i]

print(result)