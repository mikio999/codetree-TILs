n1 ,n2 = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

def consecutive_num(a,b) :
  for i in range(n1-n2+1):
    index1 = i
    index2 = i+n2
    num_list = []
    for j in range(index1, index2):
      num_list.append(a[j])
      if num_list == b:
        return 'Yes'
  return 'No'

print(consecutive_num(A,B))