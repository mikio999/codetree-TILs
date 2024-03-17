N = int(input())
num_list = []

for i in range(N) :
  x = int(input())
  num_list.append(x)

continue_list = []

if N > 1 :
  for j in range(N-1):
    if num_list[j] < num_list[j+1] :
      continue_list.append(num_list[j])
  if num_list[N-1] > num_list[N-2]:
    continue_list.append(num_list[N-1])
else :
  continue_list = num_list
print(len(continue_list))