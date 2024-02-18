lowercase_list = []

for _ in range(5):
  a =list(input().split())
  lowercase_list.append(a)


for i in range(5):
  if i > 0:
    print()
  for j in range(3):
   lowercase_list[i][j] = lowercase_list[i][j].upper()
   print(lowercase_list[i][j], end=' ')