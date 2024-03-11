A = list(input())

num = 0
for i in range(len(A)):
  num += int(A[i])*2**(len(A)-1-i)

print(num)