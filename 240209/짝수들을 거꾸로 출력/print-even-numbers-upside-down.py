n = int(input())
A = [int(x) for x in input().split()]

even_list = []

for i in range(n):
    if A[i]%2 == 0:
        even_list.append(A[i])
even_list.reverse()

for i in even_list:
    print(i, end=' ')