n = int(input())
input_list = []

for i in range(n):
  a = input()
  input_list.append(a)

for j in sorted(input_list):
  print(j)