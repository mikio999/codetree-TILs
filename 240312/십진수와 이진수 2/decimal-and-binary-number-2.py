N = list(input())

num = 0
for i in range(len(N)):
  num = num*2 + int(N[i])

target = num * 17
binary_list = []

while True:
  if target < 2:
    binary_list.append(1)
    break
  else:
    binary_list.append(target%2)
    target = target//2

binary_list.reverse()

for i in binary_list:
  print(i, end='')