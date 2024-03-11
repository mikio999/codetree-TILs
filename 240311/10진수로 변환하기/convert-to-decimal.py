A = list(input())

num = 0

# for i in range(len(A)):
#   num += int(A[i])*2**(len(A)-1-i)

for i in range(len(A)):
    num = num * 2 + int(A[i])

print(num)