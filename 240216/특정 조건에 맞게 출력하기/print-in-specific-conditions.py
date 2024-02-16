a = [int(x) for x in input().split()]
b = []
i = 0

while a[i] != 0:
    b.append(a[i])
    i += 1

for j in b:
    if j%2 == 1:
        print(j+3, end=' ')
    elif j%2 == 0:
        print(j//2, end= ' ')