A = [int(x) for x in input().split()]
addition = 0
i=0

while i<10 and A[i] < 250 :
  addition += A[i]
  i += 1

print(addition, round(addition/i,1))