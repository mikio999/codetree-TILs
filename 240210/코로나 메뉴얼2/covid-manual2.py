count = 0
C =[0,0,0,0]
for i in range(3):
    A, B = input().split()
    B = int(B)
    if A=='Y' and B >= 37:
        C[0] += 1
        count += 1
    elif A=='N' and B >= 37:
        C[1] += 1
    elif A == 'Y' and B < 37:
        C[2] += 1
    elif A == 'N' and B < 37:
        C[3] += 1

if count >= 2:
    C.append('E')

for i in C:
    print(i, end=' ')