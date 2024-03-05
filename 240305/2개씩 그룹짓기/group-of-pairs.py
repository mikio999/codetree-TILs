n = int(input())
A = [int(x) for x in input().split()]
B = []

A.sort()


for i in range(n):
    B.append((A[i],A[len(A)-1-i]))


sum_list = []
for j in B:
    sum_list.append(sum(j))

print(max(sum_list))