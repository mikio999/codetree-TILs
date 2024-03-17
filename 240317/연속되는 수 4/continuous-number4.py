N = int(input())
num_list = []

for i in range(N) :
  x = int(input())
  num_list.append(x)

continue_list = []
index = 0

while index < N-1:
  if num_list[index] > num_list[index+1] :
    continue_list = []
    index += 1
  else :
    continue_list.append(num_list[index])
    index += 1

print(len(continue_list))