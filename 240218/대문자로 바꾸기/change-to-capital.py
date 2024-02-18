lowercase_list = []

for _ in range(5):
  a =list(input().split())
  lowercase_list.append(a)


uppercase_list = lowercase_list
for i in range(5):
  for j in range(3):
    uppercase_list[i][j] = lowercase_list[i][j].upper()

for x in range(5):
  y = 0
  print()
  while y < 3:
    print(uppercase_list[x][y], end=' ')
    y += 1