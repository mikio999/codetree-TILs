n1, n2 = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

i = 0 
while i < n1-n2+1:
    if A[i:i+n2] == B:
      print('Yes')
      break
    else:
      i += 1
      if i == n1-n2+1:
        print('No')