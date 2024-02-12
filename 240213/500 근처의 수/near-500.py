a = [int(x) for x in input().split()]

under_500 = []
over_500 =[]

for i in a:
  if i > 500 :
    over_500.append(i)
  else:
    under_500.append(i)

print(max(under_500), min(over_500))