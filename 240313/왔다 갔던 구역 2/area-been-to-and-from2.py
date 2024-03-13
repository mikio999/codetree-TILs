n = int(input())
command = []
x1_list = []
for i in range(n):
  x1, x2 = input().split()
  x1 = int(x1)
  x1_list.append(x1)
  command.append((x1,x2))

target = [0]
location = 0

for j in command:
  if j[1] == 'R':
    location = location + j[0]
    target.append(location)
  elif j[1] == 'L':
    location = location - j[0]
    target.append(location)

if min(target) < 0 :
  OFFSET = - min(target)
else :
  OFFSET = 0

min_num = min(target)
max_num = max(target)

dot_list = [0 for _ in range(min_num, max_num+1)]

for i in range(len(target)) : 
  target[i] += OFFSET


for i in range(1,len(target)):
    if target[i-1] < target[i]:
      for j in range(target[i-1], target[i]+1):
        dot_list[j] += 1

    else :
      for j in range(target[i-1], target[i]-1, -1) :
        dot_list[j] += 1


index_list = []

for i in range(len(dot_list)):
  if dot_list[i] >= 2:
    index_list.append(i)

answer = 0
start_idx = 0

for j in range(len(index_list)-1):
  if index_list[j+1] - index_list[j] != 1:
    answer += index_list[j] - start_idx
    start_idx = index_list[j+1]
  if j == (len(index_list) - 2) :
    answer += index_list[j+1] - start_idx

print(answer)